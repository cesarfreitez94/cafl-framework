#!/usr/bin/env python3
"""
blueprint_traceability_index.py

Extract deterministic references from project-truth/implementation-blueprint.md.
Reference types extracted:
  - DEC-ACCEPTED-NNN, DEC-REJECTED-NNN, DEC-SUPERSEDED-NNN, DEC-PENDING-NNN
  - RISK-NNN
  - TOM (TOM-NN anchor references)
  - RULE-NN
  - SPK-* / SP-NN
  - VAL-NN
  - S01-S19 (section cross-references)
  - CRIT-NN
  - AP-NN (Architecture Principles)
  - BR-NN (Boundary Rules)
  - SCH-NN (Schemas)
  - AC-G* / FAC-*  (Acceptance Criteria)

Emit generated/blueprint/traceability-map.json with:
  - counts per reference type
  - sorted unique list per reference type
  - per-reference line numbers (first 20 occurrences)
"""

import json
import re
import sys
from collections import defaultdict
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
BLUEPRINT_PATH = REPO_ROOT / "project-truth" / "implementation-blueprint.md"
OUTPUT_PATH = REPO_ROOT / "generated" / "blueprint" / "traceability-map.json"

# Reference patterns: (category, regex)
REFERENCE_PATTERNS = [
    ("DEC-ACCEPTED",    r"\bDEC-ACCEPTED-(\d+)\b"),
    ("DEC-REJECTED",    r"\bDEC-REJECTED-(\d+)\b"),
    ("DEC-SUPERSEDED",  r"\bDEC-SUPERSEDED-(\d+)\b"),
    ("DEC-PENDING",     r"\bDEC-PENDING-(\d+)\b"),
    ("RISK",            r"\bRISK-(\d+)\b"),
    ("TOM",             r"\bTOM(?:-(\d+))?\b"),
    ("RULE",            r"\bRULE-(\d+)\b"),
    ("SP",              r"\bSP-(\d+)\b"),
    ("SPK",             r"\bSPK-([A-Z0-9_\-]+)\b"),
    ("VAL",             r"\bVAL-(\d+)\b"),
    ("SECTION",         r"\bS(0[1-9]|1[0-9])\b"),
    ("CRIT",            r"\bCRIT-(\d+)\b"),
    ("AP",              r"\bAP-(\d+)\b"),
    ("BR",              r"\bBR-(\d+)\b"),
    ("SCH",             r"\bSCH-(\d+)\b"),
    ("AC-G",            r"\bAC-G(\d+)\b"),
    ("FAC",             r"\bFAC-(\d+)\b"),
]

MAX_LINE_REFS = 20  # max line numbers stored per reference


def extract_references(path: Path) -> dict:
    lines = path.read_text(encoding="utf-8").splitlines()

    # category -> ref_id -> list of line numbers
    ref_map: dict[str, dict[str, list[int]]] = {cat: defaultdict(list) for cat, _ in REFERENCE_PATTERNS}

    for lineno, line in enumerate(lines, start=1):
        for category, pattern in REFERENCE_PATTERNS:
            for m in re.finditer(pattern, line):
                suffix = m.group(1) if m.lastindex and m.group(1) else ""
                if category == "TOM":
                    ref_id = f"TOM-{suffix}" if suffix else "TOM"
                elif category == "SPK":
                    # SPK-S14-01 style — keep full suffix
                    ref_id = f"SPK-{suffix}"
                else:
                    ref_id = f"{category}-{suffix}" if suffix else category
                if len(ref_map[category][ref_id]) < MAX_LINE_REFS:
                    ref_map[category][ref_id].append(lineno)

    return ref_map


def build_output(ref_map: dict) -> dict:
    categories = {}
    total_unique = 0

    for category, refs in ref_map.items():
        if not refs:
            continue
        sorted_refs = {}
        for ref_id in sorted(refs.keys(), key=lambda x: (
            # Sort numerically where possible
            int(re.search(r"\d+$", x).group()) if re.search(r"\d+$", x) else 0,
            x
        )):
            sorted_refs[ref_id] = refs[ref_id]

        categories[category] = {
            "count": len(sorted_refs),
            "references": sorted_refs,
        }
        total_unique += len(sorted_refs)

    return {
        "source": str(BLUEPRINT_PATH.relative_to(REPO_ROOT)),
        "total_unique_references": total_unique,
        "categories": categories,
    }


def main():
    if not BLUEPRINT_PATH.exists():
        print(f"ERROR: Blueprint not found at {BLUEPRINT_PATH}", file=sys.stderr)
        sys.exit(1)

    ref_map = extract_references(BLUEPRINT_PATH)
    output = build_output(ref_map)

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(json.dumps(output, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    print(f"traceability-map.json written: {output['total_unique_references']} unique references across {len(output['categories'])} categories")
    for cat, data in output["categories"].items():
        print(f"  {cat}: {data['count']} unique")

    return output


if __name__ == "__main__":
    main()
