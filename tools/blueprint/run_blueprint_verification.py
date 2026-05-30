#!/usr/bin/env python3
"""
run_blueprint_verification.py

Orchestrator for deterministic Blueprint verification.

Runs all checks in order:
  1. blueprint_indexer.py      -> generated/blueprint/blueprint-index.json
  2. blueprint_state_check.py  -> generated/blueprint/state-check.json
  3. blueprint_rule_check.py   -> generated/blueprint/rule-check.json
  4. blueprint_traceability_index.py -> generated/blueprint/traceability-map.json

Produces:
  - reports/blueprint/deterministic-verification-report.md
  - reports/blueprint/deterministic-verification-findings.json

Exits non-zero if critical findings exist.
"""

import json
import sys
import importlib.util
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
TOOLS_DIR = Path(__file__).resolve().parent
REPORTS_DIR = REPO_ROOT / "reports" / "blueprint"
GENERATED_DIR = REPO_ROOT / "generated" / "blueprint"

REPORT_PATH = REPORTS_DIR / "deterministic-verification-report.md"
FINDINGS_PATH = REPORTS_DIR / "deterministic-verification-findings.json"

# Script modules to run in order
SCRIPTS = [
    ("blueprint_indexer",            "generated/blueprint/blueprint-index.json"),
    ("blueprint_state_check",        "generated/blueprint/state-check.json"),
    ("blueprint_rule_check",         "generated/blueprint/rule-check.json"),
    ("blueprint_traceability_index", "generated/blueprint/traceability-map.json"),
]


def run_module(module_name: str) -> tuple[bool, str]:
    """Import and run a verification module's main(). Returns (success, error_msg)."""
    script_path = TOOLS_DIR / f"{module_name}.py"
    spec = importlib.util.spec_from_file_location(module_name, script_path)
    mod = importlib.util.module_from_spec(spec)
    try:
        spec.loader.exec_module(mod)
        mod.main()
        return True, ""
    except SystemExit as e:
        return e.code == 0, f"SystemExit({e.code})"
    except Exception as e:
        return False, str(e)


def collect_findings() -> dict:
    """Collect findings from all generated check files."""
    all_findings = []
    check_summaries = {}

    check_files = {
        "state_check":        GENERATED_DIR / "state-check.json",
        "rule_check":         GENERATED_DIR / "rule-check.json",
    }

    for check_name, path in check_files.items():
        if not path.exists():
            check_summaries[check_name] = {"result": "MISSING", "detail": f"{path.name} not generated"}
            all_findings.append({
                "severity": "critical",
                "check": check_name,
                "detail": f"Output file not generated: {path.name}",
            })
            continue

        data = json.loads(path.read_text(encoding="utf-8"))
        summary = data.get("summary", {})
        check_summaries[check_name] = summary

        for finding in data.get("findings", []):
            finding["_source_check"] = check_name
            all_findings.append(finding)

    return {
        "check_summaries": check_summaries,
        "all_findings": all_findings,
    }


def collect_index_stats() -> dict:
    """Collect stats from generated index files."""
    stats = {}

    index_path = GENERATED_DIR / "blueprint-index.json"
    if index_path.exists():
        data = json.loads(index_path.read_text(encoding="utf-8"))
        stats["blueprint_status"] = data.get("blueprint_status")
        stats["total_sections"] = data.get("total_sections_detected")
        stats["sections"] = [
            {
                "id": s["section_id"],
                "title": s["title"],
                "status": s["status"],
                "owner_approval": s["owner_approval"],
            }
            for s in data.get("sections", [])
        ]

    trace_path = GENERATED_DIR / "traceability-map.json"
    if trace_path.exists():
        data = json.loads(trace_path.read_text(encoding="utf-8"))
        stats["traceability"] = {
            "total_unique_references": data.get("total_unique_references"),
            "categories": {cat: info["count"] for cat, info in data.get("categories", {}).items()},
        }

    return stats


def render_markdown_report(
    run_results: list[dict],
    findings_data: dict,
    index_stats: dict,
    overall_result: str,
) -> str:
    lines = []
    lines.append("# Deterministic Blueprint Verification Report")
    lines.append("")
    lines.append("Source: `project-truth/implementation-blueprint.md`")
    lines.append("State: `project-truth/blueprint-state.yaml`")
    lines.append("")
    lines.append(f"## Overall Result: {overall_result}")
    lines.append("")
    lines.append("**Deterministic scope**: This report covers deterministic checks only. RULE-04 semantic verification (tracing every Blueprint component to TOM, approved CRIT, or accepted decision) requires LLM review; the deterministic traceability index checks reference presence, not semantic sufficiency.")
    lines.append("")

    # Section index summary
    lines.append("## Blueprint Section Index")
    lines.append("")
    bp_status = index_stats.get("blueprint_status", "unknown")
    total_sec = index_stats.get("total_sections", 0)
    lines.append(f"- Blueprint status: `{bp_status}`")
    lines.append(f"- Sections detected: {total_sec}")
    lines.append("")

    sections = index_stats.get("sections", [])
    if sections:
        lines.append("| Section | Title | Status | Owner Approval |")
        lines.append("| --- | --- | --- | --- |")
        for s in sections:
            lines.append(f"| {s['id']} | {s['title']} | {s['status']} | {s['owner_approval']} |")
        lines.append("")

    # Traceability summary
    trace = index_stats.get("traceability", {})
    if trace:
        lines.append("## Traceability Reference Summary")
        lines.append("")
        lines.append(f"Total unique references: **{trace.get('total_unique_references', 0)}**")
        lines.append("")
        lines.append("| Category | Count |")
        lines.append("| --- | --- |")
        for cat, count in trace.get("categories", {}).items():
            lines.append(f"| {cat} | {count} |")
        lines.append("")

    # Check run results
    lines.append("## Check Execution Results")
    lines.append("")
    lines.append("| Script | Output File | Result |")
    lines.append("| --- | --- | --- |")
    for r in run_results:
        status_icon = "PASS" if r["success"] else "FAIL"
        lines.append(f"| `{r['script']}` | `{r['output']}` | {status_icon} |")
    lines.append("")

    # Check summaries
    lines.append("## Check Summaries")
    lines.append("")
    for check_name, summary in findings_data.get("check_summaries", {}).items():
        result = summary.get("result", "UNKNOWN")
        passed = summary.get("total_passed", "?")
        total_findings = summary.get("total_findings", "?")
        critical = summary.get("critical", "?")
        warning = summary.get("warning", "?")
        lines.append(f"### {check_name}: {result}")
        lines.append(f"- Passed checks: {passed}")
        lines.append(f"- Findings: {total_findings} ({critical} critical, {warning} warning)")
        lines.append("")

    # Findings
    all_findings = findings_data.get("all_findings", [])
    critical_findings = [f for f in all_findings if f.get("severity") == "critical"]
    warning_findings = [f for f in all_findings if f.get("severity") == "warning"]
    info_findings = [f for f in all_findings if f.get("severity") == "info"]

    lines.append("## Findings")
    lines.append("")

    if not all_findings:
        lines.append("No findings. All checks passed.")
        lines.append("")
    else:
        if critical_findings:
            lines.append(f"### Critical ({len(critical_findings)})")
            lines.append("")
            for f in critical_findings:
                check = f.get("_source_check", "")
                section = f.get("section", f.get("iteration", ""))
                detail = f.get("detail", "")
                rule = f.get("rule", "")
                path = f.get("path", "")
                lines.append(f"- **[{check}]** {rule} {section} {path}: {detail}")
            lines.append("")

        if warning_findings:
            lines.append(f"### Warning ({len(warning_findings)})")
            lines.append("")
            for f in warning_findings:
                check = f.get("_source_check", "")
                section = f.get("section", f.get("iteration", ""))
                detail = f.get("detail", "")
                lines.append(f"- **[{check}]** {section}: {detail}")
            lines.append("")

        if info_findings:
            lines.append(f"### Info ({len(info_findings)})")
            lines.append("")
            for f in info_findings:
                check = f.get("_source_check", "")
                detail = f.get("detail", "")
                lines.append(f"- **[{check}]** {detail}")
            lines.append("")

    lines.append("## Generated Files")
    lines.append("")
    lines.append("| File | Purpose |")
    lines.append("| --- | --- |")
    lines.append("| `generated/blueprint/blueprint-index.json` | Section index with status and line ranges |")
    lines.append("| `generated/blueprint/state-check.json` | State YAML vs blueprint-index comparison |")
    lines.append("| `generated/blueprint/rule-check.json` | Forbidden artifact and rule checks |")
    lines.append("| `generated/blueprint/traceability-map.json` | Reference extraction map |")
    lines.append("| `reports/blueprint/deterministic-verification-report.md` | This report |")
    lines.append("| `reports/blueprint/deterministic-verification-findings.json` | Machine-readable findings |")
    lines.append("")

    return "\n".join(lines) + "\n"


def main():
    GENERATED_DIR.mkdir(parents=True, exist_ok=True)
    REPORTS_DIR.mkdir(parents=True, exist_ok=True)

    print("=== Blueprint Deterministic Verification ===")
    print()

    # Run all scripts
    run_results = []
    any_script_failed = False

    for module_name, output_rel in SCRIPTS:
        print(f"Running {module_name}.py ...", end=" ", flush=True)
        success, error = run_module(module_name)
        if not success:
            print(f"FAILED: {error}")
            any_script_failed = True
        run_results.append({
            "script": f"{module_name}.py",
            "output": output_rel,
            "success": success,
            "error": error,
        })

    print()

    # Collect findings
    findings_data = collect_findings()
    index_stats = collect_index_stats()

    all_findings = findings_data.get("all_findings", [])
    critical_count = sum(1 for f in all_findings if f.get("severity") == "critical")
    warning_count = sum(1 for f in all_findings if f.get("severity") == "warning")
    info_count = sum(1 for f in all_findings if f.get("severity") == "info")

    overall_result = "PASS" if (critical_count == 0 and not any_script_failed) else "FAIL"

    # Render report
    report_md = render_markdown_report(
        run_results=run_results,
        findings_data=findings_data,
        index_stats=index_stats,
        overall_result=overall_result,
    )

    REPORT_PATH.write_text(report_md, encoding="utf-8")

    # Write findings JSON
    findings_json = {
        "overall_result": overall_result,
        "run_results": run_results,
        "check_summaries": findings_data.get("check_summaries", {}),
        "findings": all_findings,
        "summary": {
            "critical": critical_count,
            "warning": warning_count,
            "info": info_count,
            "total": len(all_findings),
        },
    }
    FINDINGS_PATH.write_text(json.dumps(findings_json, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    print(f"Report: {REPORT_PATH.relative_to(REPO_ROOT)}")
    print(f"Findings JSON: {FINDINGS_PATH.relative_to(REPO_ROOT)}")
    print()
    print(f"Summary: {critical_count} critical, {warning_count} warning, {info_count} info")
    print(f"Overall result: {overall_result}")

    if overall_result != "PASS":
        print("\nCritical findings:")
        for f in all_findings:
            if f.get("severity") == "critical":
                print(f"  [{f.get('_source_check','')}] {f.get('detail','')}")
        sys.exit(1)


if __name__ == "__main__":
    main()
