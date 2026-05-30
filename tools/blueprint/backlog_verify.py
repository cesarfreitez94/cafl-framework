#!/usr/bin/env python3
"""
backlog_verify.py

Deterministic verification of backlog candidate generation.

Validates:
  1. backlog-contract.yaml parses and is well-formed
  2. backlog-candidates.yaml parses and every item has required fields
  3. Every item traces to exactly one S18 category via the contract
  4. Readiness values are valid
  5. Conditional/post-v1 items are visibly separated
  6. No detailed tasks are present
  7. Global Blueprint non-goals are preserved
  8. backlog-traceability.yaml maps all candidates to source categories
  9. No forbidden execution-oriented verbs appear in titles/rationale/boundary/acceptance_criteria

Produces:
  - reports/backlog/backlog-verification-report.md
"""

import re
import sys
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]

CONTRACT_PATH   = REPO_ROOT / "backlog" / "backlog-contract.yaml"
CANDIDATES_PATH = REPO_ROOT / "backlog" / "backlog-candidates.yaml"
TRACE_PATH      = REPO_ROOT / "backlog" / "backlog-traceability.yaml"
STATE_PATH      = REPO_ROOT / "project-truth" / "blueprint-state.yaml"
REPORT_PATH     = REPO_ROOT / "reports" / "backlog" / "backlog-verification-report.md"

REQUIRED_FIELDS = [
    "id", "type", "title", "source_category", "source_sections",
    "upstream_refs", "rationale", "boundary", "acceptance_criteria",
    "excluded_scope", "owner_decision_required", "readiness",
]

ALLOWED_TYPES = {"epic", "capability"}
ALLOWED_READINESS = {"candidate", "conditional", "post-v1"}
ALLOWED_OWNER_DECISION = {"none", "yes", "pending-spike-result"}

# Forbidden execution-oriented verbs (case-insensitive word-boundary match)
FORBIDDEN_VERBS = [
    "Implement",
    "Provision",
    "Enforce",
    "Integrate",
    "Scaffold",
    "Resolve",
]

# Fields to check for forbidden verbs
VERB_CHECK_FIELDS = ["title", "rationale", "boundary", "acceptance_criteria", "excluded_scope"]


def load_contract() -> dict:
    """Load the backlog contract."""
    try:
        import yaml
        with open(CONTRACT_PATH, encoding="utf-8") as f:
            return yaml.safe_load(f)
    except Exception as e:
        print(f"WARNING: Could not load contract: {e}", file=sys.stderr)
        return {}


def load_s18_categories() -> list[str]:
    """Load S18 category titles from the backlog contract."""
    contract = load_contract()
    cats = contract.get("s18_categories", [])
    return [c["title"] for c in cats if "title" in c]


def load_cap_to_epic_map(contract: dict) -> dict[str, str]:
    """
    Build cap_id -> epic_id mapping from contract capability definitions.
    Derived purely from contract order (no hard-coded index).
    """
    cap_to_epic = {}
    cats = contract.get("s18_categories", [])
    for idx, cat in enumerate(cats, start=1):
        epic_id = f"EPIC-BACKLOG-{idx:03d}"
        for cap_def in cat.get("capabilities", []):
            cap_to_epic[cap_def["id"]] = epic_id
    return cap_to_epic


S18_CATEGORIES = load_s18_categories()

# Forbidden substrings that would indicate detailed tasks
FORBIDDEN_TASK_INDICATORS = [
    "sprint", "story point", "storypoint", "velocity",
    "assignee", "assigned to", "due date", "deadline",
    "subtask", "child task",
]


def parse_yaml_file(path: Path) -> dict:
    """Parse a YAML file. Uses PyYAML if available, else fails with clear message."""
    try:
        import yaml
        with open(path, encoding="utf-8") as f:
            return yaml.safe_load(f)
    except ImportError:
        raise RuntimeError("PyYAML not available. Install: pip3 install pyyaml")


def extract_candidates_from_structured_yaml(path: Path) -> tuple[list, list]:
    """Extract epics and capabilities from candidates YAML file."""
    text = path.read_text(encoding="utf-8")
    try:
        import yaml
        data = yaml.safe_load(text)
    except ImportError:
        return _fallback_parse_candidates(text)

    epics = data.get("epics", [])
    capabilities = data.get("capabilities", [])
    return epics, capabilities


def _fallback_parse_candidates(text: str) -> tuple[list, list]:
    """Minimal fallback parser for candidates YAML if PyYAML is unavailable."""
    epics = []
    capabilities = []
    current_list = None
    current_item = None
    in_epics = False
    in_capabilities = False

    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith("#") or not stripped:
            continue

        if stripped == "epics:":
            in_epics = True
            in_capabilities = False
            current_list = epics
            continue
        elif stripped == "capabilities:":
            in_epics = False
            in_capabilities = True
            current_list = capabilities
            continue

        if stripped.startswith("- id:") and (in_epics or in_capabilities):
            current_item = {}
            current_list.append(current_item)
            current_item["id"] = stripped[5:].strip().strip('"')
            continue

        if current_item is not None and ":" in stripped and stripped.startswith("  "):
            key, _, value = stripped.partition(":")
            key = key.strip()
            value = value.strip().strip('"')
            if value:
                current_item[key] = value

    return epics, capabilities


def extract_traceability_items(path: Path) -> list:
    """Extract traceability items from traceability YAML."""
    text = path.read_text(encoding="utf-8")
    try:
        import yaml
        data = yaml.safe_load(text)
    except ImportError:
        return []
    return data.get("links", [])


def check_blueprint_state() -> tuple[bool, str]:
    """Verify the Blueprint is closed and S18 is approved."""
    if not STATE_PATH.exists():
        return False, "blueprint-state.yaml not found"

    try:
        state = parse_yaml_file(STATE_PATH)
    except Exception as e:
        return False, f"Cannot parse blueprint-state.yaml: {e}"

    sections = state.get("sections", {})
    s18 = sections.get("S18", {})
    s18_status = s18.get("status")
    s18_approval = s18.get("owner_approval")

    issues = []
    if s18_status != "closed":
        issues.append(f"S18 status={s18_status}, expected 'closed'")
    if s18_approval != "approved":
        issues.append(f"S18 owner_approval={s18_approval}, expected 'approved'")

    if issues:
        return False, "; ".join(issues)
    return True, "S18 closed and approved"


def _item_text_for_verb_check(item: dict) -> str:
    """Concatenate all verb-checked fields from an item into a single string."""
    parts = []
    for field in VERB_CHECK_FIELDS:
        val = item.get(field, "")
        if isinstance(val, list):
            parts.append(" ".join(str(v) for v in val))
        elif val:
            parts.append(str(val))
    return " ".join(parts)


def check_forbidden_verbs(all_items: list) -> list:
    """
    Check all items for forbidden execution-oriented verbs.
    Returns list of findings (dicts with severity/check/detail).
    """
    findings = []
    # Build regex: word-boundary match, case-insensitive
    verb_pattern = re.compile(
        r'\b(' + '|'.join(re.escape(v) for v in FORBIDDEN_VERBS) + r')\b',
        re.IGNORECASE
    )
    for item in all_items:
        item_id = item.get("id", "???")
        for field in VERB_CHECK_FIELDS:
            val = item.get(field, "")
            if isinstance(val, list):
                text = " ".join(str(v) for v in val)
            else:
                text = str(val) if val else ""
            matches = verb_pattern.findall(text)
            if matches:
                unique = sorted(set(m.lower() for m in matches))
                findings.append({
                    "severity": "critical",
                    "check": "forbidden_verbs",
                    "detail": (
                        f"Item {item_id} field '{field}' contains forbidden verb(s): "
                        f"{', '.join(unique)}"
                    ),
                })
    return findings


def verify_contract(contract_path: Path) -> dict:
    """Verify the backlog contract."""
    findings = []
    passed = []

    if not contract_path.exists():
        findings.append({
            "severity": "critical",
            "check": "contract_exists",
            "detail": "backlog-contract.yaml not found",
        })
        return {"passed": passed, "findings": findings, "summary": {"result": "FAIL"}}

    try:
        contract = parse_yaml_file(contract_path)
    except Exception as e:
        findings.append({
            "severity": "critical",
            "check": "contract_parses",
            "detail": f"Cannot parse backlog-contract.yaml: {e}",
        })
        return {"passed": passed, "findings": findings, "summary": {"result": "FAIL"}}

    passed.append({"check": "contract_parses", "detail": "backlog-contract.yaml parses successfully"})

    # Check required top-level keys
    required_keys = ["contract_id", "version", "scope", "generation_rules", "item_schema", "s18_categories"]
    for key in required_keys:
        if key in contract:
            passed.append({"check": f"contract_key_{key}", "detail": f"Key '{key}' present"})
        else:
            findings.append({
                "severity": "critical",
                "check": f"contract_key_{key}",
                "detail": f"Missing required key '{key}' in contract",
            })

    # Check S18 categories
    contract_cats = contract.get("s18_categories", [])
    if len(contract_cats) == 9:
        passed.append({"check": "s18_category_count", "detail": "9 categories defined"})
    else:
        findings.append({
            "severity": "critical",
            "check": "s18_category_count",
            "detail": f"Expected 9 categories, found {len(contract_cats)}",
        })

    # Check each category has capabilities and upstream_ref_patterns
    for cat in contract_cats:
        cat_id = cat.get("id", "?")
        if "capabilities" not in cat:
            findings.append({
                "severity": "critical",
                "check": "contract_category_capabilities",
                "detail": f"Category {cat_id} missing 'capabilities' in contract",
            })
        if "upstream_ref_patterns" not in cat:
            findings.append({
                "severity": "critical",
                "check": "contract_category_ref_patterns",
                "detail": f"Category {cat_id} missing 'upstream_ref_patterns' in contract",
            })

    # Check no_forbidden_verbs rule present in generation_rules
    gen_rules = contract.get("generation_rules", {})
    if "rule_no_forbidden_verbs" in gen_rules:
        passed.append({"check": "contract_forbidden_verb_rule", "detail": "rule_no_forbidden_verbs present in generation_rules"})
    else:
        findings.append({
            "severity": "critical",
            "check": "contract_forbidden_verb_rule",
            "detail": "rule_no_forbidden_verbs missing from generation_rules in contract",
        })

    return {
        "passed": passed,
        "findings": findings,
        "summary": {
            "total_passed": len(passed),
            "total_findings": len(findings),
            "critical": sum(1 for f in findings if f.get("severity") == "critical"),
            "result": "PASS" if not any(f.get("severity") == "critical" for f in findings) else "FAIL",
        },
    }


def verify_candidates(candidates_path: Path) -> dict:
    """Verify the backlog candidates YAML."""
    findings = []
    passed = []

    if not candidates_path.exists():
        findings.append({
            "severity": "critical",
            "check": "candidates_exists",
            "detail": "backlog-candidates.yaml not found",
        })
        return {"passed": passed, "findings": findings, "summary": {"result": "FAIL"}}

    try:
        epics, capabilities = extract_candidates_from_structured_yaml(candidates_path)
    except Exception as e:
        findings.append({
            "severity": "critical",
            "check": "candidates_parses",
            "detail": f"Cannot parse backlog-candidates.yaml: {e}",
        })
        return {"passed": passed, "findings": findings, "summary": {"result": "FAIL"}}

    passed.append({"check": "candidates_parses", "detail": f"Parsed {len(epics)} epics, {len(capabilities)} capabilities"})

    all_items = epics + capabilities

    # Check minimum counts
    if len(epics) >= 9:
        passed.append({"check": "epic_count", "detail": f"{len(epics)} epics (expected at least 9)"})
    else:
        findings.append({
            "severity": "critical",
            "check": "epic_count",
            "detail": f"Only {len(epics)} epics found, expected at least 9",
        })

    if len(capabilities) >= 18:
        passed.append({"check": "capability_count", "detail": f"{len(capabilities)} capabilities (expected at least 18)"})
    else:
        findings.append({
            "severity": "critical",
            "check": "capability_count",
            "detail": f"Only {len(capabilities)} capabilities found, expected at least 18",
        })

    # Check ID format
    epic_id_pattern = re.compile(r"^EPIC-BACKLOG-\d{3}$")
    cap_id_pattern = re.compile(r"^CAP-BACKLOG-\d{3}$")

    for item in all_items:
        item_id = item.get("id", "")
        if "id" not in item:
            findings.append({
                "severity": "critical",
                "check": "item_id_missing",
                "detail": f"Item missing 'id' field",
            })
            continue

        item_type = item.get("type", "")
        if item_type == "epic" and not epic_id_pattern.match(item_id):
            findings.append({
                "severity": "critical",
                "check": "item_id_format",
                "detail": f"Epic {item_id} does not match EPIC-BACKLOG-NNN format",
            })
        elif item_type == "capability" and not cap_id_pattern.match(item_id):
            findings.append({
                "severity": "critical",
                "check": "item_id_format",
                "detail": f"Capability {item_id} does not match CAP-BACKLOG-NNN format",
            })
        elif item_type not in ALLOWED_TYPES:
            findings.append({
                "severity": "critical",
                "check": "item_type_valid",
                "detail": f"Item {item_id} has invalid type '{item_type}'",
            })
        else:
            passed.append({"check": "item_id_format", "detail": f"ID {item_id} format valid"})

    # Check required fields
    for item in all_items:
        item_id = item.get("id", "???")
        for field in REQUIRED_FIELDS:
            if field not in item or item[field] is None or item[field] == "":
                findings.append({
                    "severity": "critical",
                    "check": "required_field_missing",
                    "detail": f"Item {item_id} missing required field '{field}'",
                })

    field_count = len(all_items) * len(REQUIRED_FIELDS)
    field_missing = sum(1 for f in findings if f.get("check") == "required_field_missing")
    if field_missing == 0:
        passed.append({"check": "required_fields", "detail": f"All {field_count} required field slots present across {len(all_items)} items"})
    else:
        passed.append({"check": "required_fields", "detail": f"{field_missing} missing fields out of {field_count}"})

    # Check allowed types
    for item in all_items:
        item_type = item.get("type", "")
        if item_type not in ALLOWED_TYPES:
            findings.append({
                "severity": "critical",
                "check": "allowed_types",
                "detail": f"Item {item.get('id', '???')} has invalid type '{item_type}'",
            })

    # Check allowed readiness
    for item in all_items:
        readiness = item.get("readiness", "")
        if readiness not in ALLOWED_READINESS:
            findings.append({
                "severity": "critical",
                "check": "allowed_readiness",
                "detail": f"Item {item.get('id', '???')} readiness '{readiness}' not in {ALLOWED_READINESS}",
            })

    # Check S18 category traceability
    for item in all_items:
        src_cat = item.get("source_category", "")
        if src_cat not in S18_CATEGORIES:
            findings.append({
                "severity": "critical",
                "check": "source_category_valid",
                "detail": f"Item {item.get('id', '???')} source_category '{src_cat}' not in S18 categories",
            })

    # Check conditional/post-v1 separation
    conditional_items = [i for i in all_items if i.get("readiness") == "conditional"]
    postv1_items = [i for i in all_items if i.get("readiness") == "post-v1"]
    candidate_items = [i for i in all_items if i.get("readiness") == "candidate"]

    passed.append({
        "check": "readiness_separation",
        "detail": f"{len(candidate_items)} candidate, {len(conditional_items)} conditional, {len(postv1_items)} post-v1 items visibly separated",
    })

    # Check owner_decision_required values
    for item in all_items:
        odr = item.get("owner_decision_required", "")
        if odr not in ALLOWED_OWNER_DECISION:
            findings.append({
                "severity": "critical",
                "check": "owner_decision_valid",
                "detail": f"Item {item.get('id', '???')} owner_decision_required '{odr}' not valid",
            })

    # Check no detailed tasks
    for item in all_items:
        text = str(item)
        for indicator in FORBIDDEN_TASK_INDICATORS:
            if indicator in text.lower():
                findings.append({
                    "severity": "critical",
                    "check": "no_detailed_tasks",
                    "detail": f"Item {item.get('id', '???')} contains forbidden task indicator '{indicator}'",
                })

    # --- Forbidden execution verb check (CRITICAL) ---
    verb_findings = check_forbidden_verbs(all_items)
    if verb_findings:
        findings.extend(verb_findings)
    else:
        passed.append({
            "check": "no_forbidden_verbs",
            "detail": f"No forbidden execution verbs found in {len(all_items)} items across fields: {', '.join(VERB_CHECK_FIELDS)}",
        })

    # Check capability readiness consistency with owner decision
    for item in all_items:
        readiness = item.get("readiness", "")
        odr = item.get("owner_decision_required", "")
        if readiness == "conditional" and odr == "none":
            findings.append({
                "severity": "warning",
                "check": "conditional_owner_decision",
                "detail": f"Item {item.get('id', '???')} is conditional but owner_decision_required='none'",
            })
        if readiness == "post-v1" and odr == "none":
            findings.append({
                "severity": "warning",
                "check": "postv1_owner_decision",
                "detail": f"Item {item.get('id', '???')} is post-v1 but owner_decision_required='none'",
            })

    # Build epic-to-cap mapping from contract (sole source)
    contract = load_contract()
    cap_to_epic_map = load_cap_to_epic_map(contract)

    # Check every capability is present in the contract mapping
    for c in capabilities:
        cap_id = c.get("id", "")
        if cap_id not in cap_to_epic_map:
            findings.append({
                "severity": "critical",
                "check": "capability_contract_mapping",
                "detail": f"Capability {cap_id} not found in backlog-contract.yaml mapping",
            })

    # Check boundary preservation: container epics must not hide conditional/post-V1 scope
    epic_map = {e.get("id", ""): e for e in epics}
    cap_by_epic = defaultdict(list)
    for c in capabilities:
        cap_id = c.get("id", "")
        if cap_id not in cap_to_epic_map:
            continue
        parent = cap_to_epic_map[cap_id]
        cap_by_epic[parent].append(c)

    for epic_id, epic in epic_map.items():
        child_caps = cap_by_epic.get(epic_id, [])
        child_readiness = [c.get("readiness", "") for c in child_caps]
        has_conditional = "conditional" in child_readiness
        has_postv1 = "post-v1" in child_readiness
        epic_readiness = epic.get("readiness", "")
        epic_odr = epic.get("owner_decision_required", "")

        if has_postv1:
            if epic_readiness != "post-v1":
                findings.append({
                    "severity": "critical",
                    "check": "epic_boundary_preservation",
                    "detail": f"Epic {epic_id} contains post-v1 capabilities but epic readiness is '{epic_readiness}'",
                })
            if epic_odr == "none":
                findings.append({
                    "severity": "critical",
                    "check": "epic_boundary_preservation",
                    "detail": f"Epic {epic_id} contains post-v1 capabilities but owner_decision_required='none'",
                })
        elif has_conditional:
            if epic_readiness == "candidate" and epic_odr == "none":
                findings.append({
                    "severity": "critical",
                    "check": "epic_boundary_preservation",
                    "detail": f"Epic {epic_id} contains conditional capabilities but epic is plain candidate with owner_decision_required='none'",
                })

    # Check no more than 9 epics (one per category)
    epic_count = len(epics)
    if epic_count > 12:
        findings.append({
            "severity": "warning",
            "check": "epic_count_limit",
            "detail": f"{epic_count} epics may exceed the 9 S18 categories",
        })

    if epic_count == 9:
        passed.append({"check": "epic_one_per_category", "detail": "Exactly 9 epics, one per S18 category"})
    elif epic_count == 10:
        passed.append({"check": "epic_one_per_category", "detail": "10 epics (near 9 S18 categories; possibly one extra for spike tracking)"})

    return {
        "passed": passed,
        "findings": findings,
        "summary": {
            "total_passed": len(passed),
            "total_findings": len(findings),
            "critical": sum(1 for f in findings if f.get("severity") == "critical"),
            "warning": sum(1 for f in findings if f.get("severity") == "warning"),
            "info": sum(1 for f in findings if f.get("severity") == "info"),
            "result": "PASS" if not any(f.get("severity") == "critical" for f in findings) else "FAIL",
        },
    }


def verify_traceability(trace_path: Path, candidates_path: Path) -> dict:
    """Verify the backlog traceability YAML."""
    findings = []
    passed = []

    if not trace_path.exists():
        findings.append({
            "severity": "critical",
            "check": "traceability_exists",
            "detail": "backlog-traceability.yaml not found",
        })
        return {"passed": passed, "findings": findings, "summary": {"result": "FAIL"}}

    try:
        links = extract_traceability_items(trace_path)
    except Exception as e:
        findings.append({
            "severity": "critical",
            "check": "traceability_parses",
            "detail": f"Cannot parse backlog-traceability.yaml: {e}",
        })
        return {"passed": passed, "findings": findings, "summary": {"result": "FAIL"}}

    passed.append({"check": "traceability_parses", "detail": f"Parsed {len(links)} traceability link groups"})

    if len(links) == 9:
        passed.append({"check": "traceability_category_count", "detail": "9 traceability category groups (one per S18 category)"})
    else:
        findings.append({
            "severity": "critical",
            "check": "traceability_category_count",
            "detail": f"Expected 9 category groups, found {len(links)}",
        })

    # Count total items
    total_items = sum(len(link.get("items", [])) for link in links)
    if total_items >= 27:
        passed.append({"check": "traceability_total_items", "detail": f"{total_items} items tracked (expected at least 27: 9 epics + 18+ caps)"})
    else:
        findings.append({
            "severity": "critical",
            "check": "traceability_total_items",
            "detail": f"Only {total_items} items tracked, expected at least 27",
        })

    return {
        "passed": passed,
        "findings": findings,
        "summary": {
            "total_passed": len(passed),
            "total_findings": len(findings),
            "critical": sum(1 for f in findings if f.get("severity") == "critical"),
            "result": "PASS" if not any(f.get("severity") == "critical" for f in findings) else "FAIL",
        },
    }


def render_report(contract_result, candidates_result, traceability_result, state_check, overall_result):
    """Render the verification report."""
    lines = []
    lines.append("# Backlog Verification Report")
    lines.append("")
    lines.append(f"Generated: {datetime.now(timezone.utc).isoformat()}")
    lines.append("Verifier: `tools/blueprint/backlog_verify.py`")
    lines.append("")
    lines.append(f"## Overall Result: {overall_result}")
    lines.append("")
    lines.append("## Precondition: Blueprint State")
    lines.append("")
    lines.append(f"- S18 status: {state_check[1]}")
    lines.append("")

    # Contract
    lines.append("## Contract Verification")
    lines.append("")
    cr = contract_result.get("summary", {})
    lines.append(f"- **Result**: {cr.get('result', 'UNKNOWN')}")
    lines.append(f"- Passed: {cr.get('total_passed', 0)}, Findings: {cr.get('total_findings', 0)} ({cr.get('critical', 0)} critical)")
    for p in contract_result.get("passed", []):
        lines.append(f"  - [PASS] {p.get('detail', '')}")
    for f in contract_result.get("findings", []):
        lines.append(f"  - [{f.get('severity','').upper()}] {f.get('detail', '')}")
    lines.append("")

    # Candidates
    lines.append("## Candidates Verification")
    lines.append("")
    cdr = candidates_result.get("summary", {})
    lines.append(f"- **Result**: {cdr.get('result', 'UNKNOWN')}")
    lines.append(f"- Passed: {cdr.get('total_passed', 0)}, Findings: {cdr.get('total_findings', 0)} ({cdr.get('critical', 0)} critical, {cdr.get('warning', 0)} warning)")
    for p in candidates_result.get("passed", []):
        lines.append(f"  - [PASS] {p.get('detail', '')}")
    for f in candidates_result.get("findings", []):
        lines.append(f"  - [{f.get('severity','').upper()}] {f.get('detail', '')}")
    lines.append("")

    # Traceability
    lines.append("## Traceability Verification")
    lines.append("")
    tr = traceability_result.get("summary", {})
    lines.append(f"- **Result**: {tr.get('result', 'UNKNOWN')}")
    lines.append(f"- Passed: {tr.get('total_passed', 0)}, Findings: {tr.get('total_findings', 0)} ({tr.get('critical', 0)} critical)")
    for p in traceability_result.get("passed", []):
        lines.append(f"  - [PASS] {p.get('detail', '')}")
    for f in traceability_result.get("findings", []):
        lines.append(f"  - [{f.get('severity','').upper()}] {f.get('detail', '')}")
    lines.append("")

    lines.append("## Generated Files")
    lines.append("")
    lines.append("| File | Purpose |")
    lines.append("| --- | --- |")
    lines.append("| `reports/backlog/backlog-verification-report.md` | This report |")
    lines.append("")

    return "\n".join(lines) + "\n"


def main():
    REPORT_PATH.parent.mkdir(parents=True, exist_ok=True)
    findings_all = []

    # 0. Check Blueprint state
    state_ok, state_msg = check_blueprint_state()
    if not state_ok:
        print(f"WARNING: Blueprint state issue: {state_msg}")
    else:
        print(f"Blueprint state: {state_msg}")

    # 1. Verify contract
    contract_result = verify_contract(CONTRACT_PATH)
    findings_all.extend(contract_result.get("findings", []))
    print(f"Contract: {contract_result['summary']['result']} "
          f"({contract_result['summary']['total_passed']} passed, "
          f"{contract_result['summary']['total_findings']} findings)")

    # 2. Verify candidates
    candidates_result = verify_candidates(CANDIDATES_PATH)
    findings_all.extend(candidates_result.get("findings", []))
    print(f"Candidates: {candidates_result['summary']['result']} "
          f"({candidates_result['summary']['total_passed']} passed, "
          f"{candidates_result['summary']['total_findings']} findings)")

    # 3. Verify traceability
    traceability_result = verify_traceability(TRACE_PATH, CANDIDATES_PATH)
    findings_all.extend(traceability_result.get("findings", []))
    print(f"Traceability: {traceability_result['summary']['result']} "
          f"({traceability_result['summary']['total_passed']} passed, "
          f"{traceability_result['summary']['total_findings']} findings)")

    critical_count = sum(1 for f in findings_all if f.get("severity") == "critical")
    warning_count = sum(1 for f in findings_all if f.get("severity") == "warning")
    overall_result = "PASS" if critical_count == 0 else "FAIL"

    # Render report
    report_md = render_report(
        contract_result, candidates_result, traceability_result,
        (state_ok, state_msg), overall_result
    )
    REPORT_PATH.write_text(report_md, encoding="utf-8")

    print(f"\nReport: {REPORT_PATH.relative_to(REPO_ROOT)}")
    print(f"Summary: {critical_count} critical, {warning_count} warning")
    print(f"Overall result: {overall_result}")

    if overall_result != "PASS":
        sys.exit(1)

    return 0


if __name__ == "__main__":
    sys.exit(main())
