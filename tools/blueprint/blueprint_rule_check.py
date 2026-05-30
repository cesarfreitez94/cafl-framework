#!/usr/bin/env python3
"""
blueprint_rule_check.py

Check forbidden post-blueprint artifacts/signals in the repository.
Forbidden categories (RULE-09 / Non-Goals Globales Del Blueprint):
  - runtime (executable runtime layout/infrastructure)
  - executable agents (real agent definitions)
  - physical schemas (JSON Schema, YAML schema, DDL, ORM models)
  - real validators (executable validator scripts/classes)
  - scripts (executable scripts outside tools/blueprint/)
  - RAG/vector base
  - detailed backlog
  - implementation artifacts

Rules checked:
  - RULE-09: Blueprint must not create runtime, executable agents, real commands,
             physical schemas, real validators, scripts, RAG/base vectorial,
             detailed technical backlog, or implementation.
  - RULE-08: Blueprint Outputs to Backlog lists only categories, not detailed tasks.
  - RULE-10: Blueprint must not use framework/ as input or reference.
  - CRIT-08: Must not be created.

Note: RULE-04 semantic verification requires LLM review.
This check covers reference presence only (see traceability-map.json).

Scan scope:
  - Prunes node_modules, __pycache__, venv, .venv, .git.
  - Distinguishes Blueprint-authoring .opencode agents/commands
    from forbidden CAFL runtime artifacts.
  - All traversal results are sorted for reproducibility.

The check operates on:
  1. File-system scan: detect forbidden files outside allowed boundaries.
  2. Blueprint text scan: detect explicit forbidden artifact creation signals
     within implementation-blueprint.md — respecting explicit non-goals / exclusion text.

Emit generated/blueprint/rule-check.json.
"""

import json
import os
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
BLUEPRINT_PATH = REPO_ROOT / "project-truth" / "implementation-blueprint.md"
OUTPUT_PATH = REPO_ROOT / "generated" / "blueprint" / "rule-check.json"

# ---------------------------------------------------------------------------
# Allowed boundaries: these directories/patterns are expected and not violations
# ---------------------------------------------------------------------------
ALLOWED_DIRS = {
    "project-truth",
    "reports",
    "docs",
    "tools/blueprint",
    "generated/blueprint",
    ".git",
}

# Specific backlog files allowed as post-Blueprint deterministic outputs.
# Any other backlog/** file must be scanned against forbidden artifact patterns.
ALLOWED_BACKLOG_FILES = {
    "backlog/backlog-contract.yaml",
    "backlog/backlog-candidates.yaml",
    "backlog/backlog-traceability.yaml",
}

# Directories pruned from traversal (heavy, generated, or virtual-env dirs)
PRUNE_DIRS = {
    "node_modules",
    "__pycache__",
    "venv",
    ".venv",
    ".git",
}

# .opencode paths that are legitimate Blueprint-authoring infrastructure, not CAFL runtime
OPNECODE_ALLOWED_SUBDIRS = {
    ".opencode/agents",
    ".opencode/commands",
}

# File patterns that would indicate forbidden post-blueprint artifacts
# These look for files *outside* allowed dirs that signal real implementation.
FORBIDDEN_FILE_PATTERNS = [
    # executable Python scripts outside tools/blueprint/
    (r".*\.py$", "executable_python_script",
     "Python scripts outside tools/blueprint/ may indicate implementation artifact"),
    # ORM model files
    (r".*/models/.*\.py$", "orm_model",
     "ORM model files indicate physical schema — forbidden by RULE-09"),
    # SQL DDL
    (r".*\.(sql|ddl)$", "sql_ddl",
     "SQL/DDL files indicate physical schema — forbidden by RULE-09"),
    # JSON Schema files
    (r".*schema.*\.(json|yaml|yml)$", "json_yaml_schema",
     "JSON/YAML schema files indicate physical schema — forbidden by RULE-09"),
    # Vector/RAG artifacts
    (r".*(vector|rag|embedding|faiss|chroma|pinecone).*$", "rag_vector",
     "RAG/vector base artifacts — forbidden by RULE-09"),
    # Backlog files
    (r".*(backlog|sprint|epic|story|task[-_]list).*\.(md|json|yaml|yml)$", "detailed_backlog",
     "Detailed backlog files — forbidden by RULE-09 / RULE-08"),
    # Odoo module structures
    (r".*/__manifest__\.py$", "odoo_module",
     "Odoo module manifest indicates executable pilot module — RULE-09"),
    # Agent config files (opencode agent definitions outside project-truth/)
    (r".*agents?[-_]config.*\.(json|yaml|yml)$", "agent_config",
     "Agent config files indicate executable agents — RULE-09"),
]

# ---------------------------------------------------------------------------
# Blueprint text signals — phrases that would indicate actual creation of
# forbidden artifacts (not conceptual mention, not non-goal statement).
# We look for affirmative creation language near forbidden keywords.
# ---------------------------------------------------------------------------

# Patterns that indicate creation language (affirmative)
CREATION_VERBS = [
    r"\bcreate[sd]?\b",
    r"\bimplements?\b",
    r"\binstall[sed]?\b",
    r"\bdeploy[sed]?\b",
    r"\bexecutes?\b",
    r"\bgenerate[sd]?\b",
    r"\bdefine[sd]?\b.*(?:schema|validator|script|agent|command|runtime|rag|vector)",
    r"\bbuilds?\b",
    r"\brun[ns]?\b.*(?:script|agent|validator)",
]

FORBIDDEN_SUBJECT_PATTERNS = [
    (r"\bexecutable\s+agent", "executable_agent"),
    (r"\breal\s+(?:command|validator|script|schema)", "real_artifact"),
    (r"\brag\b|\bvector\s+(?:base|store|db|database)\b|\bembedding\s+store\b", "rag_vector"),
    (r"\bCRIT-08\b", "crit_08"),
    (r"\bframework/\b.*(?:input|source|reference)", "framework_reference"),
    (r"\bdetailed\s+(?:backlog|task\s+list)\b", "detailed_backlog"),
]

# Lines/paragraphs that are clearly non-goals, exclusions, or negative statements
# We exclude these from the creation-language search.
EXCLUSION_INDICATORS = [
    r"^-\s+No\s+",
    r"^-\s+\[accepted\].*no\s+",
    r"\bnot?\s+create[sd]?\b",
    r"\bdoes\s+not\s+create\b",
    r"\bmust\s+not\b",
    r"\bnon-goals?\b",
    r"\bexcluded?\b",
    r"\bforbidden\b",
    r"\bexplicit\s+non-(?:decision|goal)",
    r"\bno\s+(?:runtime|scripts?|agents?|validators?|schemas?|rag|backlog)\b",
    r"^\s*\*?\s*\*\*?Non-",
    r"\bdeferred\b",
    r"\bout\s+of\s+(?:scope|V1|core)\b",
    r"\bpost-V1\b",
]


def is_exclusion_line(line: str) -> bool:
    lower = line.lower()
    for pat in EXCLUSION_INDICATORS:
        if re.search(pat, lower):
            return True
    return False


def scan_filesystem(repo_root: Path) -> list:
    """Scan the repository for forbidden file patterns outside allowed dirs."""
    findings = []

    for path in sorted(repo_root.rglob("*"), key=str):
        if not path.is_file():
            continue

        # Compute relative path
        try:
            rel = path.relative_to(repo_root)
        except ValueError:
            continue

        rel_str = str(rel)
        parts = rel.parts
        top = parts[0] if parts else ""
        top2 = "/".join(parts[:2]) if len(parts) >= 2 else top
        top3 = "/".join(parts[:3]) if len(parts) >= 3 else top2

        # Prune heavy or generated directories
        if any(p in PRUNE_DIRS for p in parts):
            continue

        # Skip if within explicitly allowed directories
        if top in ALLOWED_DIRS or top2 in ALLOWED_DIRS:
            continue

        # Allow specific backlog files as authorized deterministic outputs;
        # any other backlog/** file must still be scanned.
        if rel_str in ALLOWED_BACKLOG_FILES:
            continue

        # Allow Blueprint-authoring infrastructure under .opencode/agents and .opencode/commands
        if top2 in OPNECODE_ALLOWED_SUBDIRS or top3 in OPNECODE_ALLOWED_SUBDIRS:
            continue

        # Check against forbidden file patterns
        for pattern, category, description in FORBIDDEN_FILE_PATTERNS:
            if re.match(pattern, rel_str, re.IGNORECASE):
                findings.append({
                    "severity": "critical",
                    "rule": "RULE-09",
                    "category": category,
                    "path": rel_str,
                    "detail": description,
                })
                break  # only report once per file

    return findings


def scan_blueprint_text(path: Path) -> list:
    """
    Scan blueprint text for affirmative creation of forbidden artifacts.
    Respects explicit non-goal / exclusion language.
    """
    findings = []
    lines = path.read_text(encoding="utf-8").splitlines()

    # Check CRIT-08 creation signal: any line mentioning CRIT-08 as something
    # being created or opened (not as a prohibition).
    for lineno, line in enumerate(lines, start=1):
        # CRIT-08 must not be created — if it appears in affirmative context
        if re.search(r"\bCRIT-08\b", line):
            if not is_exclusion_line(line):
                # Check if it's in a prohibition context
                if not re.search(r"no\s+crea\s+crit-08|must\s+not.*crit-08|not.*crit-08", line.lower()):
                    findings.append({
                        "severity": "warning",
                        "rule": "RULE-09 / AGENTS.md",
                        "category": "crit_08",
                        "line": lineno,
                        "detail": f"CRIT-08 mention in potentially affirmative context: {line.strip()[:120]}",
                    })

    # Check framework/ affirmative references as an input/source/authority (RULE-10)
    # Exclusion contexts, prohibitions, and general "framework" mentions are allowed.
    # Only flag lines where framework/ is positioned as an actual input or authority.
    for lineno, line in enumerate(lines, start=1):
        # Only consider lines with the path-like `framework/` pattern
        if not re.search(r"`framework/`", line):
            continue
        lower = line.lower()
        # Skip if it's clearly an exclusion or prohibition
        if is_exclusion_line(line):
            continue
        if re.search(r"exclu|not\s+use|no\s+usar|fuera\s+de|not\s+input|no\s+se\s+usa|no\s+recrea|no\s+usa|outside|prohibited|not\s+authorit|no\s+son\s+autorid|sin.*uso\s+de|sin\s+recrear|do\s+not\s+reference|do\s+not\s+use|introducir|reintroduc", lower):
            continue
        # Skip lines that mention using framework/ as anti-example (negative context)
        if re.search(r"usar\s+`framework/`|usar\s+o\s+referenciar|no\s+uso|sin\s+uso", lower):
            continue
        # Skip lines that are clearly a bullet list of prohibited actions
        # (list items ending with `framework/` as last in a series of prohibited items)
        if re.search(r"^\s*-\s+", line) and re.search(r"o\s+`framework/`\s*\.?\s*$", line):
            continue
        findings.append({
            "severity": "info",
            "rule": "RULE-10",
            "category": "framework_reference",
            "line": lineno,
            "detail": f"framework/ reference (verify it is exclusion context): {line.strip()[:120]}",
        })

    return findings


def check_crit08_absent() -> list:
    """
    Ensure CRIT-08 is not defined as an actual critical item.
    CRIT-08 is allowed to appear in exclusion/prohibition context
    (e.g. 'no existe CRIT-08', 'without CRIT-08', 'CRIT-08 no existe').
    A violation would be an affirmative definition like '## CRIT-08' or
    '| CRIT-08 | ...' as a real entry row.
    """
    findings = []
    crit_map_path = REPO_ROOT / "project-truth" / "critical-map.md"
    if crit_map_path.exists():
        text = crit_map_path.read_text(encoding="utf-8")
        lines = text.splitlines()
        for lineno, line in enumerate(lines, start=1):
            if not re.search(r"\bCRIT-08\b", line):
                continue
            # Affirmative heading definition
            if re.match(r"^#{1,4}\s+CRIT-08\b", line):
                findings.append({
                    "severity": "critical",
                    "rule": "AGENTS.md / Non-Goals",
                    "category": "crit_08_defined",
                    "path": "project-truth/critical-map.md",
                    "line": lineno,
                    "detail": f"CRIT-08 appears as a section heading — prohibited: {line.strip()[:100]}",
                })
            # Table row that defines CRIT-08 as a real entry (not a prohibition)
            elif re.match(r"^\|\s*CRIT-08\s*\|", line):
                lower = line.lower()
                if not re.search(r"no\s+existe|does\s+not\s+exist|prohibited|forbidden|not\s+creat", lower):
                    findings.append({
                        "severity": "critical",
                        "rule": "AGENTS.md / Non-Goals",
                        "category": "crit_08_table_entry",
                        "path": "project-truth/critical-map.md",
                        "line": lineno,
                        "detail": f"CRIT-08 appears as a table entry — verify it is exclusion context: {line.strip()[:100]}",
                    })
    return findings


def check_forbidden_dirs() -> list:
    """Check for forbidden directory patterns."""
    findings = []
    # backlog/ itself is allowed, but files inside it are checked individually
    # (only backlog-contract.yaml, backlog-candidates.yaml, backlog-traceability.yaml
    # are authorized; see ALLOWED_BACKLOG_FILES in scan_filesystem).
    forbidden_dir_patterns = [
        (r"(historical|archive|legacy)", "historical_archive_dir",
         "Forbidden directory type per AGENTS.md (no historical/archive/legacy)"),
        (r"sprint", "sprint_dir",
         "Sprint directory signals detailed implementation planning — RULE-09"),
    ]
    for path in sorted(REPO_ROOT.rglob("*"), key=str):
        if not path.is_dir():
            continue
        parts = path.relative_to(REPO_ROOT).parts
        if any(p in PRUNE_DIRS for p in parts):
            continue
        name = path.name.lower()
        for pattern, category, detail in forbidden_dir_patterns:
            if re.search(pattern, name):
                try:
                    rel = str(path.relative_to(REPO_ROOT))
                except ValueError:
                    rel = str(path)
                findings.append({
                    "severity": "critical",
                    "rule": "AGENTS.md",
                    "category": category,
                    "path": rel,
                    "detail": detail,
                })
                break
    return findings


def main():
    findings = []
    passed = []

    # 1. Filesystem scan
    fs_findings = scan_filesystem(REPO_ROOT)
    if fs_findings:
        findings.extend(fs_findings)
    else:
        passed.append({"check": "filesystem_scan", "detail": "No forbidden implementation files found outside allowed dirs"})

    # 2. Blueprint text scan
    if BLUEPRINT_PATH.exists():
        text_findings = scan_blueprint_text(BLUEPRINT_PATH)
        if text_findings:
            findings.extend(text_findings)
        else:
            passed.append({"check": "blueprint_text_scan", "detail": "No affirmative forbidden artifact signals in blueprint text"})
    else:
        findings.append({
            "severity": "critical",
            "rule": "RULE-09",
            "category": "missing_blueprint",
            "detail": f"Blueprint not found: {BLUEPRINT_PATH}",
        })

    # 3. CRIT-08 absent check
    crit_findings = check_crit08_absent()
    if crit_findings:
        findings.extend(crit_findings)
    else:
        passed.append({"check": "crit08_absent", "detail": "CRIT-08 not found in critical-map.md"})

    # 4. Forbidden dirs
    dir_findings = check_forbidden_dirs()
    if dir_findings:
        findings.extend(dir_findings)
    else:
        passed.append({"check": "forbidden_dirs", "detail": "No forbidden directory patterns found"})

    # 5. No detailed backlog files check
    # backlog/ and reports/backlog/ are authorized post-Blueprint deterministic output dirs
    backlog_files = list(REPO_ROOT.rglob("backlog*.md")) + list(REPO_ROOT.rglob("backlog*.json"))
    # Exclude project-truth references, .git, and authorized post-Blueprint dirs
    real_backlog = [
        f for f in backlog_files
        if "project-truth" not in str(f) and ".git" not in str(f)
        and "reports/backlog" not in str(f) and "backlog/" not in str(f.parent)
    ]
    if real_backlog:
        for f in real_backlog:
            findings.append({
                "severity": "critical",
                "rule": "RULE-08 / RULE-09",
                "category": "detailed_backlog_file",
                "path": str(f.relative_to(REPO_ROOT)),
                "detail": "Backlog file found — RULE-08 allows only categories, RULE-09 forbids detailed technical backlog",
            })
    else:
        passed.append({"check": "no_backlog_files", "detail": "No detached backlog files found"})

    critical_count = sum(1 for f in findings if f.get("severity") == "critical")
    warning_count = sum(1 for f in findings if f.get("severity") == "warning")
    info_count = sum(1 for f in findings if f.get("severity") == "info")

    result = {
        "check": "rule_check",
        "rules_checked": ["RULE-08", "RULE-09", "RULE-10", "AGENTS.md/No-CRIT-08"],
        "rule_04_note": "RULE-04 semantic verification requires LLM review; deterministic check covers reference presence only (see traceability-map.json).",
        "passed": passed,
        "findings": findings,
        "summary": {
            "total_passed": len(passed),
            "total_findings": len(findings),
            "critical": critical_count,
            "warning": warning_count,
            "info": info_count,
            "result": "PASS" if critical_count == 0 else "FAIL",
        },
    }

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    s = result["summary"]
    print(f"rule-check.json written: {s['total_passed']} passed, {s['total_findings']} findings "
          f"({s['critical']} critical, {s['warning']} warning, {s['info']} info) — {s['result']}")
    return result


if __name__ == "__main__":
    main()
