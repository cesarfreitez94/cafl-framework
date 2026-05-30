#!/usr/bin/env python3
"""
blueprint_state_check.py

Validate project-truth/blueprint-state.yaml parses.
Compare section count, statuses, approvals, and iteration closure
against generated/blueprint/blueprint-index.json.
Emit generated/blueprint/state-check.json.
"""

import json
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
STATE_PATH = REPO_ROOT / "project-truth" / "blueprint-state.yaml"
INDEX_PATH = REPO_ROOT / "generated" / "blueprint" / "blueprint-index.json"
OUTPUT_PATH = REPO_ROOT / "generated" / "blueprint" / "state-check.json"

# We avoid third-party deps; parse YAML using stdlib where possible.
# blueprint-state.yaml is simple enough for a targeted parse.
try:
    import yaml
    _HAS_YAML = True
except ImportError:
    _HAS_YAML = False


def load_state_yaml(path: Path) -> dict:
    """Load blueprint-state.yaml. Uses PyYAML if available, else minimal parser."""
    text = path.read_text(encoding="utf-8")
    if _HAS_YAML:
        return yaml.safe_load(text)
    # Minimal fallback: just confirm the file reads without error.
    # Return a sentinel indicating it parsed (structural checks still run via yaml).
    raise RuntimeError(
        "PyYAML not available. Install pyyaml: pip3 install pyyaml"
    )


def load_index(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def normalize_approval(val: str) -> str:
    """Normalize owner_approval values from blueprint text to state yaml values."""
    if val is None:
        return None
    v = val.strip().lower()
    if v.startswith("approved"):
        return "approved"
    return v


def run_checks(state: dict, index: dict) -> dict:
    findings = []
    passed = []

    # ---- 1. YAML parses ----
    passed.append({"check": "yaml_parses", "detail": "blueprint-state.yaml parsed successfully"})

    # ---- 2. Section count ----
    state_sections = state.get("sections", {})
    state_count = len(state_sections)
    blueprint_total = state.get("blueprint", {}).get("total_sections", None)
    index_count = index.get("total_sections_detected", 0)

    if state_count != index_count:
        findings.append({
            "severity": "critical",
            "check": "section_count",
            "detail": f"state.yaml has {state_count} sections; blueprint-index has {index_count}",
        })
    else:
        passed.append({"check": "section_count", "detail": f"{state_count} sections match"})

    if blueprint_total is not None and blueprint_total != index_count:
        findings.append({
            "severity": "critical",
            "check": "total_sections_declared",
            "detail": f"blueprint-state.yaml declares total_sections={blueprint_total} but index detected {index_count}",
        })
    else:
        passed.append({"check": "total_sections_declared", "detail": f"total_sections={blueprint_total} matches index"})

    # ---- 3. Section statuses ----
    index_by_id = {s["section_id"]: s for s in index.get("sections", [])}

    for sid, sec_state in state_sections.items():
        state_status = sec_state.get("status")
        state_approval = sec_state.get("owner_approval")

        if sid not in index_by_id:
            findings.append({
                "severity": "critical",
                "check": "section_in_index",
                "section": sid,
                "detail": f"{sid} in state.yaml but not found in blueprint-index",
            })
            continue

        idx_sec = index_by_id[sid]
        idx_status = idx_sec.get("status")
        idx_approval_raw = idx_sec.get("owner_approval")
        idx_approval = normalize_approval(idx_approval_raw)

        # Status comparison
        if state_status != idx_status:
            findings.append({
                "severity": "critical",
                "check": "section_status",
                "section": sid,
                "detail": f"state={state_status!r} vs blueprint-text={idx_status!r}",
            })
        else:
            passed.append({"check": "section_status", "section": sid, "detail": f"status={state_status!r} matches"})

        # Approval comparison
        if state_approval != idx_approval:
            findings.append({
                "severity": "critical",
                "check": "section_approval",
                "section": sid,
                "detail": f"state={state_approval!r} vs blueprint-text-normalized={idx_approval!r} (raw: {idx_approval_raw!r})",
            })
        else:
            passed.append({"check": "section_approval", "section": sid, "detail": f"owner_approval={state_approval!r} matches"})

    # ---- 4. Iteration closure ----
    state_iterations = state.get("iterations", {})
    for iid, it in state_iterations.items():
        it_status = it.get("status")
        it_gate = it.get("owner_gate")
        if it_status != "closed":
            findings.append({
                "severity": "critical",
                "check": "iteration_closed",
                "iteration": iid,
                "detail": f"iteration {iid} status={it_status!r} (expected 'closed')",
            })
        else:
            passed.append({"check": "iteration_closed", "iteration": iid, "detail": f"{iid} status=closed"})

        if it_gate != "approved":
            findings.append({
                "severity": "critical",
                "check": "iteration_gate",
                "iteration": iid,
                "detail": f"iteration {iid} owner_gate={it_gate!r} (expected 'approved')",
            })
        else:
            passed.append({"check": "iteration_gate", "iteration": iid, "detail": f"{iid} owner_gate=approved"})

    # ---- 5. Blueprint-level closure ----
    bp_status = index.get("blueprint_status")
    if bp_status != "blueprint-closed":
        findings.append({
            "severity": "critical",
            "check": "blueprint_closed",
            "detail": f"blueprint top-level status={bp_status!r} (expected 'blueprint-closed')",
        })
    else:
        passed.append({"check": "blueprint_closed", "detail": "blueprint status=blueprint-closed"})

    total_iterations = state.get("blueprint", {}).get("total_iterations", None)
    if total_iterations != 5:
        findings.append({
            "severity": "critical",
            "check": "total_iterations",
            "detail": f"expected 5 iterations, state declares {total_iterations}",
        })
    else:
        passed.append({"check": "total_iterations", "detail": "total_iterations=5"})

    critical_count = sum(1 for f in findings if f.get("severity") == "critical")
    warning_count = sum(1 for f in findings if f.get("severity") == "warning")

    return {
        "check": "state_check",
        "state_yaml_path": str(STATE_PATH.relative_to(REPO_ROOT)),
        "index_path": str(INDEX_PATH.relative_to(REPO_ROOT)),
        "passed": passed,
        "findings": findings,
        "summary": {
            "total_passed": len(passed),
            "total_findings": len(findings),
            "critical": critical_count,
            "warning": warning_count,
            "result": "PASS" if critical_count == 0 else "FAIL",
        },
    }


def main():
    if not STATE_PATH.exists():
        print(f"ERROR: State file not found: {STATE_PATH}", file=sys.stderr)
        sys.exit(1)
    if not INDEX_PATH.exists():
        print(f"ERROR: blueprint-index.json not found. Run blueprint_indexer.py first.", file=sys.stderr)
        sys.exit(1)

    state = load_state_yaml(STATE_PATH)
    index = load_index(INDEX_PATH)

    result = run_checks(state, index)

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    s = result["summary"]
    print(f"state-check.json written: {s['total_passed']} passed, {s['total_findings']} findings "
          f"({s['critical']} critical, {s['warning']} warning) — {s['result']}")
    return result


if __name__ == "__main__":
    main()
