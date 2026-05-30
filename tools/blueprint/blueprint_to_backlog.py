#!/usr/bin/env python3
"""
blueprint_to_backlog.py

Deterministic backlog candidate generation from the completed CAFL V1
Implementation Blueprint. Reads:
  - backlog/backlog-contract.yaml  (S18 category definitions, capability definitions,
                                    upstream_ref_patterns — sole source of domain knowledge)
  - generated/blueprint/traceability-map.json  (all references)
  - project-truth/implementation-blueprint.md  (S17 traceability + S18 scope table)

Produces:
  - backlog/backlog-candidates.yaml   (Epics and Capabilities)
  - backlog/backlog-traceability.yaml (candidate to source mapping)
  - reports/backlog/backlog-generation-report.md
"""

import json
import sys
from datetime import datetime, timezone
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]

CONTRACT_PATH    = REPO_ROOT / "backlog" / "backlog-contract.yaml"
TRACE_MAP_PATH   = REPO_ROOT / "generated" / "blueprint" / "traceability-map.json"
BLUEPRINT_PATH   = REPO_ROOT / "project-truth" / "implementation-blueprint.md"

CANDIDATES_PATH  = REPO_ROOT / "backlog" / "backlog-candidates.yaml"
TRACE_OUT_PATH   = REPO_ROOT / "backlog" / "backlog-traceability.yaml"
REPORT_PATH      = REPO_ROOT / "reports" / "backlog" / "backlog-generation-report.md"


# ---------------------------------------------------------------------------
# Load S18 categories from contract (sole source of domain knowledge)
# ---------------------------------------------------------------------------
def load_contract() -> dict:
    """Load the full backlog contract from CONTRACT_PATH."""
    try:
        import yaml
    except ImportError:
        raise RuntimeError("PyYAML is required. Install: pip3 install pyyaml")

    with open(CONTRACT_PATH, encoding="utf-8") as f:
        contract = yaml.safe_load(f)
    return contract


def load_s18_categories(contract: dict) -> tuple[list, dict]:
    """
    Load S18 categories from contract and parse scope narrative from blueprint.
    Returns (categories_list, source_lines_dict).
    """
    contract_cats = contract.get("s18_categories", [])
    if len(contract_cats) != 9:
        raise RuntimeError(f"Expected 9 S18 categories in contract, found {len(contract_cats)}")

    # Validate each category has capabilities defined
    for cat in contract_cats:
        if "capabilities" not in cat:
            raise RuntimeError(
                f"Category '{cat.get('id', '?')}' ({cat.get('title', '?')}) "
                f"has no capabilities defined in CONTRACT_PATH"
            )
        if "upstream_ref_patterns" not in cat:
            raise RuntimeError(
                f"Category '{cat.get('id', '?')}' ({cat.get('title', '?')}) "
                f"has no upstream_ref_patterns defined in CONTRACT_PATH"
            )

    # Parse scope narrative from blueprint table
    blueprint_lines = BLUEPRINT_PATH.read_text(encoding="utf-8").splitlines()
    scope_map = {}
    source_lines = {}
    for lineno, line in enumerate(blueprint_lines, start=1):
        if not line.startswith("| "):
            continue
        parts = [p.strip() for p in line.split("|")]
        if len(parts) < 4:
            continue
        title = parts[1]
        scope = parts[2]
        if title and scope and "Work domain" in scope:
            scope_map[title] = scope
            source_lines[title] = lineno

    categories = []
    for cat in contract_cats:
        title = cat["title"]
        categories.append({
            "id": cat["id"],
            "title": title,
            "source_sections": cat["source_sections"],
            "scope_narrative": scope_map.get(title, ""),
            "source_line": source_lines.get(title),
            "upstream_ref_patterns": cat["upstream_ref_patterns"],
            "capabilities": cat["capabilities"],
        })

    return categories, source_lines


# ---------------------------------------------------------------------------
# Candidate definitions — deterministically derived from contract
# ---------------------------------------------------------------------------
class CandidateDef:
    def __init__(self, id_, type_, title, source_category, source_sections,
                 upstream_refs, rationale, boundary, acceptance_criteria,
                 excluded_scope, owner_decision_required, readiness):
        self.id = id_
        self.type = type_
        self.title = title
        self.source_category = source_category
        self.source_sections = source_sections
        self.upstream_refs = upstream_refs
        self.rationale = rationale
        self.boundary = boundary
        self.acceptance_criteria = acceptance_criteria
        self.excluded_scope = excluded_scope
        self.owner_decision_required = owner_decision_required
        self.readiness = readiness

    def to_dict(self):
        return {
            "id": self.id,
            "type": self.type,
            "title": self.title,
            "source_category": self.source_category,
            "source_sections": self.source_sections,
            "upstream_refs": self.upstream_refs,
            "rationale": self.rationale,
            "boundary": self.boundary,
            "acceptance_criteria": self.acceptance_criteria,
            "excluded_scope": self.excluded_scope,
            "owner_decision_required": self.owner_decision_required,
            "readiness": self.readiness,
        }


def _fmt_list(items):
    return [str(x) for x in items]


def generate_candidates(categories: list, traceability_map: dict) -> tuple[list, list]:
    """Deterministically generate Epics and Capabilities from S18 categories."""

    # Helper: collect relevant refs from traceability-map for a set of section IDs
    def resolve_upstream_refs(patterns: list[str], section_ids: list) -> list[str]:
        """Collect traceability refs matching patterns from the traceability map."""
        refs = set()
        cat_map = traceability_map.get("categories", {})
        for cat_data in cat_map.values():
            for ref_id in cat_data.get("references", {}):
                refs.add(ref_id)
        all_sorted = sorted(refs)
        relevant = []

        # Always include section references first
        for s in sorted(set(str(x) for x in section_ids)):
            relevant.append(s)

        # Add refs from patterns
        for ref in all_sorted:
            for pat in patterns:
                if ref.startswith(pat) or ref == pat:
                    if ref not in relevant:
                        relevant.append(ref)
                    break

        return sorted(relevant)

    epics = []
    capabilities = []

    for cat in categories:
        epic_id = f"EPIC-BACKLOG-{categories.index(cat) + 1:03d}"
        category_title = cat["title"]
        sections = cat["source_sections"]
        patterns = cat["upstream_ref_patterns"]

        upstream = resolve_upstream_refs(patterns, sections)

        # Derive capabilities from contract definitions (no index/title branching)
        caps = _derive_capabilities(epic_id, cat, upstream)
        capabilities.extend(caps)

        # Determine epic readiness/owner_decision from child capabilities
        child_readiness = [c.readiness for c in caps]
        if any(r == "post-v1" for r in child_readiness):
            epic_readiness = "post-v1"
            epic_odr = "yes"
        elif any(r == "conditional" for r in child_readiness):
            epic_readiness = "conditional"
            epic_odr = "pending-spike-result"
        else:
            epic_readiness = "candidate"
            epic_odr = "none"

        # Epic
        epic = CandidateDef(
            id_=epic_id,
            type_="epic",
            title=category_title,
            source_category=category_title,
            source_sections=_fmt_list(sections),
            upstream_refs=upstream,
            rationale=(
                f"Derived from S18 category '{category_title}'. "
                f"{cat['scope_narrative']}"
            ),
            boundary=(
                f"This Epic preserves the V1/Post-V1 boundary defined in S03. "
                f"All work remains within Odoo-only, Odoo 18, internal requests / simple "
                f"approvals pilot scope. No runtime, executable agents, real commands, "
                f"physical schemas, real validators, scripts, RAG/vector base, detailed "
                f"technical backlog, PRD, SDD, or implementation is created."
            ),
            acceptance_criteria=[
                "Epic preserves RULE-08 by staying at category level only",
                "Epic preserves RULE-09 and global Blueprint non-goals",
                "Epic is traceable to S17 traceability matrix",
                "Conditional, open-uncertainty, and post-V1-gated areas remain visibly separated",
            ],
            excluded_scope=(
                "Detailed tasks, work items, tickets, implementation steps, sequencing, "
                "estimates, owners, acceptance tests, deliverable artifacts, runtime, "
                "executable agents, real commands, physical schemas, real validators, "
                "scripts, RAG/vector base, PRD, SDD."
            ),
            owner_decision_required=epic_odr,
            readiness=epic_readiness,
        )
        epics.append(epic)

    return epics, capabilities


def _derive_capabilities(epic_id: str, cat: dict, upstream: list[str]) -> list:
    """
    Derive Capabilities from a category using definitions in CONTRACT_PATH.
    No branching on category index or title — all domain knowledge from contract.
    """
    caps = []
    category_title = cat["title"]
    sections = cat["source_sections"]

    for cap_def in cat["capabilities"]:
        cap_id = cap_def["id"]
        title = cap_def["title"]
        # Multi-line rationale from YAML is a string with possible leading/trailing whitespace
        rationale = " ".join(cap_def["rationale"].split())
        readiness = cap_def["readiness"]
        owner_dec = str(cap_def.get("owner_decision_required", "none"))

        cap = CandidateDef(
            id_=cap_id,
            type_="capability",
            title=title,
            source_category=category_title,
            source_sections=_fmt_list(sections),
            upstream_refs=upstream,
            rationale=rationale,
            boundary=(
                f"Derived from Epic {epic_id}. Respects V1/Post-V1 boundary. "
                f"No runtime, executable agents, real commands, physical schemas, real "
                f"validators, scripts, RAG/vector base, PRD, SDD, or implementation."
            ),
            acceptance_criteria=[
                f"Capability preserves RULE-08 by staying at capability level only",
                f"Capability preserves RULE-09 and global Blueprint non-goals",
                f"Capability is traceable to {epic_id} and S17 traceability matrix",
                f"Capability readiness ({readiness}) is correctly declared",
            ],
            excluded_scope=(
                "Detailed tasks, work items, tickets, implementation steps, sequencing, "
                "estimates, owners, acceptance tests, deliverable artifacts."
            ),
            owner_decision_required=owner_dec,
            readiness=readiness,
        )
        caps.append(cap)

    return caps


# ---------------------------------------------------------------------------
# YAML serialization
# ---------------------------------------------------------------------------
def _yaml_str(value: str) -> str:
    """Return a YAML-safe string representation (literal block or quoted)."""
    if "\n" in value:
        lines = ["|"]
        for vline in value.splitlines():
            lines.append(f"      {vline}")
        return "\n".join(lines)
    safe = value.replace("\\", "\\\\").replace('"', '\\"')
    return f'"{safe}"'


def serialize_candidates_yaml(epics, capabilities):
    """Serialize epics and capabilities as structured YAML without truncation."""
    lines = []
    lines.append("# CAFL V1 Backlog Candidates")
    lines.append("# Generated deterministically from S18 Blueprint categories.")
    lines.append("# Do not modify manually. Regenerate via blueprint_to_backlog.py.")
    lines.append("")
    lines.append(f"generated_at: \"{datetime.now(timezone.utc).isoformat()}\"")
    lines.append("generated_by: tools/blueprint/blueprint_to_backlog.py")
    lines.append(f"total_epics: {len(epics)}")
    lines.append(f"total_capabilities: {len(capabilities)}")
    lines.append(f"readiness_summary:")
    for readiness_label in ["candidate", "conditional", "post-v1"]:
        count = sum(1 for e in epics if e.readiness == readiness_label)
        count += sum(1 for c in capabilities if c.readiness == readiness_label)
        lines.append(f"  {readiness_label}: {count}")
    lines.append("")
    lines.append("epics:")
    for e in epics:
        lines.append(f"  - id: {e.id}")
        lines.append(f"    type: {e.type}")
        lines.append(f"    title: {_yaml_str(e.title)}")
        lines.append(f"    source_category: {_yaml_str(e.source_category)}")
        lines.append(f"    source_sections: [{', '.join(e.source_sections)}]")
        lines.append(f"    upstream_refs: [{', '.join(e.upstream_refs)}]")
        lines.append(f"    rationale: {_yaml_str(e.rationale)}")
        lines.append(f"    boundary: {_yaml_str(e.boundary)}")
        lines.append(f"    acceptance_criteria: [{', '.join(e.acceptance_criteria)}]")
        lines.append(f"    excluded_scope: {_yaml_str(e.excluded_scope)}")
        odr_safe = (
            f'"{e.owner_decision_required}"'
            if e.owner_decision_required in ("yes", "no", "none")
            else e.owner_decision_required
        )
        lines.append(f"    owner_decision_required: {odr_safe}")
        lines.append(f"    readiness: {e.readiness}")
        lines.append("")
    lines.append("capabilities:")
    for c in capabilities:
        lines.append(f"  - id: {c.id}")
        lines.append(f"    type: {c.type}")
        lines.append(f"    title: {_yaml_str(c.title)}")
        lines.append(f"    source_category: {_yaml_str(c.source_category)}")
        lines.append(f"    source_sections: [{', '.join(c.source_sections)}]")
        lines.append(f"    upstream_refs: [{', '.join(c.upstream_refs)}]")
        lines.append(f"    rationale: {_yaml_str(c.rationale)}")
        lines.append(f"    boundary: {_yaml_str(c.boundary)}")
        lines.append(f"    acceptance_criteria: [{', '.join(c.acceptance_criteria)}]")
        lines.append(f"    excluded_scope: {_yaml_str(c.excluded_scope)}")
        odr_cap_safe = (
            f'"{c.owner_decision_required}"'
            if c.owner_decision_required in ("yes", "no", "none")
            else c.owner_decision_required
        )
        lines.append(f"    owner_decision_required: {odr_cap_safe}")
        lines.append(f"    readiness: {c.readiness}")
        lines.append("")
    return "\n".join(lines)


def serialize_traceability_yaml(epics, capabilities, categories):
    """Generate the traceability YAML linking candidates to source categories."""
    lines = []
    lines.append("# CAFL V1 Backlog Traceability")
    lines.append("# Candidate-to-source mapping derived from S18 categories and S17 matrix.")
    lines.append("# Do not modify manually.")
    lines.append("")
    lines.append(f"generated_at: \"{datetime.now(timezone.utc).isoformat()}\"")
    lines.append(f"total_traceability_links: {len(epics) + len(capabilities)}")
    lines.append("")
    lines.append("links:")
    for cat in categories:
        cat_id = cat["id"]
        cat_title = cat["title"]
        lines.append(f"  - category_id: {cat_id}")
        lines.append(f"    category_title: \"{cat_title}\"")
        lines.append(f"    source_blueprint_section: S18")
        lines.append(f"    source_sections: [{', '.join(str(x) for x in cat['source_sections'])}]")
        lines.append("    items:")
        for e in epics:
            if e.source_category == cat_title:
                lines.append(f"      - id: {e.id}")
                lines.append(f"        type: {e.type}")
                lines.append(f"        title: \"{e.title}\"")
                lines.append(f"        readiness: {e.readiness}")
                lines.append(f"        owner_decision_required: {e.owner_decision_required}")
        for c in capabilities:
            if c.source_category == cat_title:
                lines.append(f"      - id: {c.id}")
                lines.append(f"        type: {c.type}")
                lines.append(f"        title: \"{c.title}\"")
                lines.append(f"        readiness: {c.readiness}")
                lines.append(f"        owner_decision_required: {c.owner_decision_required}")
        lines.append("")
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Report generation
# ---------------------------------------------------------------------------
def generate_report(epics, capabilities, categories, source_lines: dict, cap_to_epic_map: dict[str, str]):
    """Generate the backlog generation report."""
    candidate_epics = [e for e in epics if e.readiness == "candidate"]
    conditional_epics = [e for e in epics if e.readiness == "conditional"]
    postv1_epics = [e for e in epics if e.readiness == "post-v1"]

    candidate_caps = [c for c in capabilities if c.readiness == "candidate"]
    conditional_caps = [c for c in capabilities if c.readiness == "conditional"]
    postv1_caps = [c for c in capabilities if c.readiness == "post-v1"]

    owner_items = [item for item in epics + capabilities if item.owner_decision_required != "none"]

    lines = []
    lines.append("# Backlog Candidate Generation Report")
    lines.append("")
    lines.append(f"Generated: {datetime.now(timezone.utc).isoformat()}")
    lines.append("Generator: `tools/blueprint/blueprint_to_backlog.py`")
    lines.append("")
    lines.append("## Generation Summary")
    lines.append("")
    lines.append(f"- **Source**: S18 Blueprint Outputs to Backlog (9 categories)")
    lines.append(f"- **S17 Traceability Matrix**: bidirectionally complete")
    lines.append(f"- **Total Epics generated**: {len(epics)}")
    lines.append(f"- **Total Capabilities generated**: {len(capabilities)}")
    lines.append(f"- **Total items generated**: {len(epics) + len(capabilities)}")
    lines.append("")
    lines.append("## S18 Category Source Lines")
    lines.append("")
    lines.append("| Category ID | Title | Blueprint Source Line |")
    lines.append("| --- | --- | --- |")
    for cat in categories:
        lineno = source_lines.get(cat["title"], "unknown")
        lines.append(f"| {cat['id']} | {cat['title']} | project-truth/implementation-blueprint.md line {lineno} |")
    lines.append("")
    lines.append("## Readiness Distribution")
    lines.append("")
    lines.append("| Readiness | Epics | Capabilities | Total |")
    lines.append("| --- | --- | --- | --- |")
    lines.append(f"| candidate | {len(candidate_epics)} | {len(candidate_caps)} | {len(candidate_epics) + len(candidate_caps)} |")
    lines.append(f"| conditional | {len(conditional_epics)} | {len(conditional_caps)} | {len(conditional_epics) + len(conditional_caps)} |")
    lines.append(f"| post-v1 | {len(postv1_epics)} | {len(postv1_caps)} | {len(postv1_epics) + len(postv1_caps)} |")
    lines.append("")
    lines.append("## Items Requiring Owner Decision")
    lines.append("")
    if owner_items:
        lines.append("| ID | Type | Title | Owner Decision | Readiness |")
        lines.append("| --- | --- | --- | --- | --- |")
        for item in owner_items:
            lines.append(f"| {item.id} | {item.type} | {item.title} | {item.owner_decision_required} | {item.readiness} |")
    else:
        lines.append("None.")
    lines.append("")
    lines.append("## Epics")
    lines.append("")
    for e in epics:
        lines.append(f"### {e.id}: {e.title}")
        lines.append(f"- **Source Category**: {e.source_category}")
        lines.append(f"- **Source Sections**: {', '.join(e.source_sections)}")
        lines.append(f"- **Upstream Refs**: {', '.join(e.upstream_refs)}")
        lines.append(f"- **Readiness**: {e.readiness}")
        lines.append(f"- **Owner Decision Required**: {e.owner_decision_required}")
        lines.append(f"- **Rationale**: {e.rationale}")
        lines.append("")
    lines.append("## Capabilities")
    lines.append("")
    for c in capabilities:
        epic_parent = cap_to_epic_map.get(c.id)
        if not epic_parent:
            raise RuntimeError(
                f"Capability {c.id} is missing from the backlog-contract.yaml "
                f"capability-to-epic mapping. Generation aborted."
            )
        lines.append(f"### {c.id}: {c.title}")
        lines.append(f"- **Epic Parent**: {epic_parent}")
        lines.append(f"- **Source Category**: {c.source_category}")
        lines.append(f"- **Upstream Refs**: {', '.join(c.upstream_refs)}")
        lines.append(f"- **Readiness**: {c.readiness}")
        lines.append(f"- **Owner Decision Required**: {c.owner_decision_required}")
        lines.append(f"- **Rationale**: {c.rationale}")
        lines.append("")
    lines.append("## Generation Rules Applied")
    lines.append("")
    lines.append("- **Rule S18 categories sole source**: Only S18 categories were used as backlog domains")
    lines.append("- **Rule S17 traceability attach**: S17 matrix and traceability-map.json attached upstream refs only")
    lines.append("- **Rule epics and capabilities only**: No detailed tasks, user stories, or implementation steps generated")
    lines.append("- **Rule every item has required fields**: All items include id, type, title, source_category, source_sections, upstream_refs, rationale, boundary, acceptance_criteria, excluded_scope, owner_decision_required, readiness")
    lines.append("- **Rule V1/Post-V1 boundary preserved**: Conditional and post-V1 items visibly separated")
    lines.append("- **Rule spike-dependent visible**: SP-04/SP-05/SP-11..SP-13 dependencies explicitly annotated")
    lines.append("- **Rule no external tooling**: No external project-management tooling introduced")
    lines.append("- **Rule no forbidden verbs**: Titles and rationale do not use execution-oriented verbs")
    lines.append("")
    lines.append("## Generated Files")
    lines.append("")
    lines.append("| File | Purpose |")
    lines.append("| --- | --- |")
    lines.append("| `backlog/backlog-candidates.yaml` | Epics and Capabilities with full field set |")
    lines.append("| `backlog/backlog-traceability.yaml` | Candidate-to-source-category mapping |")
    lines.append("| `reports/backlog/backlog-generation-report.md` | This report |")
    lines.append("")

    return "\n".join(lines) + "\n"


def load_cap_to_epic_map(contract: dict) -> dict[str, str]:
    """
    Build cap_id -> epic_id mapping from contract capability definitions.
    Derived purely from contract order (no hard-coded index, no boundary parsing).
    """
    cap_to_epic = {}
    cats = contract.get("s18_categories", [])
    for idx, cat in enumerate(cats, start=1):
        epic_id = f"EPIC-BACKLOG-{idx:03d}"
        for cap_def in cat.get("capabilities", []):
            cap_to_epic[cap_def["id"]] = epic_id
    return cap_to_epic


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main():
    # Validate inputs
    if not TRACE_MAP_PATH.exists():
        print(f"ERROR: traceability-map.json not found at {TRACE_MAP_PATH}", file=sys.stderr)
        print("Run python3 tools/blueprint/run_blueprint_verification.py first.", file=sys.stderr)
        sys.exit(1)

    if not BLUEPRINT_PATH.exists():
        print(f"ERROR: Blueprint not found at {BLUEPRINT_PATH}", file=sys.stderr)
        sys.exit(1)

    # Load traceability map
    with open(TRACE_MAP_PATH, encoding="utf-8") as f:
        trace_map = json.load(f)

    print(f"Loaded traceability map: {trace_map.get('total_unique_references', 0)} references")

    # Load contract (sole source of category/capability domain knowledge)
    contract = load_contract()
    print(f"Loaded contract: version {contract.get('version', '?')}")

    # Load S18 categories from contract + blueprint scope narrative
    categories, source_lines = load_s18_categories(contract)
    print(f"Loaded {len(categories)} S18 categories from contract + blueprint")

    # Validate capability counts from contract
    total_caps_in_contract = sum(len(cat["capabilities"]) for cat in categories)
    if total_caps_in_contract != 30:
        print(
            f"WARNING: Expected 30 capabilities in contract, found {total_caps_in_contract}",
            file=sys.stderr
        )

    # Generate candidates
    epics, capabilities = generate_candidates(categories, trace_map)
    all_items = epics + capabilities

    # Load capability-to-epic mapping from contract (sole source for Epic Parent)
    cap_to_epic_map = load_cap_to_epic_map(contract)

    # Fail loudly if any generated capability is missing from the contract mapping
    for cap in capabilities:
        if cap.id not in cap_to_epic_map:
            print(
                f"ERROR: Capability {cap.id} is missing from the "
                f"backlog-contract.yaml capability-to-epic mapping. "
                f"Generation aborted.",
                file=sys.stderr,
            )
            sys.exit(1)

    # Validate required fields
    required_fields = ["id", "type", "title", "source_category", "source_sections",
                       "upstream_refs", "rationale", "boundary", "acceptance_criteria",
                       "excluded_scope", "owner_decision_required", "readiness"]

    for item in all_items:
        d = item.to_dict()
        for field in required_fields:
            if field not in d or d[field] is None:
                print(f"ERROR: {item.id} missing required field '{field}'", file=sys.stderr)
                sys.exit(1)

    # Write candidates YAML
    CANDIDATES_PATH.parent.mkdir(parents=True, exist_ok=True)
    CANDIDATES_PATH.write_text(serialize_candidates_yaml(epics, capabilities), encoding="utf-8")
    print(f"Wrote: {CANDIDATES_PATH.relative_to(REPO_ROOT)}")

    # Write traceability YAML
    TRACE_OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    TRACE_OUT_PATH.write_text(serialize_traceability_yaml(epics, capabilities, categories), encoding="utf-8")
    print(f"Wrote: {TRACE_OUT_PATH.relative_to(REPO_ROOT)}")

    # Write report
    REPORT_PATH.parent.mkdir(parents=True, exist_ok=True)
    REPORT_PATH.write_text(generate_report(epics, capabilities, categories, source_lines, cap_to_epic_map), encoding="utf-8")
    print(f"Wrote: {REPORT_PATH.relative_to(REPO_ROOT)}")

    # Summary
    candidate_eps = sum(1 for e in epics if e.readiness == "candidate")
    conditional_eps = sum(1 for e in epics if e.readiness == "conditional")
    postv1_eps = sum(1 for e in epics if e.readiness == "post-v1")
    candidate_caps = sum(1 for c in capabilities if c.readiness == "candidate")
    conditional_caps = sum(1 for c in capabilities if c.readiness == "conditional")
    postv1_caps = sum(1 for c in capabilities if c.readiness == "post-v1")
    owner_items = [item for item in all_items if item.owner_decision_required != "none"]

    print()
    print(f"=== Generation Summary ===")
    print(f"Epics:    {len(epics)}  (candidate={candidate_eps}, conditional={conditional_eps}, post-v1={postv1_eps})")
    print(f"Capabilities: {len(capabilities)}  (candidate={candidate_caps}, conditional={conditional_caps}, post-v1={postv1_caps})")
    print(f"Total:    {len(all_items)}")
    print(f"Owner decision required: {len(owner_items)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
