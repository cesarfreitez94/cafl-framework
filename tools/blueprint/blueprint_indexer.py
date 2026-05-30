#!/usr/bin/env python3
"""
blueprint_indexer.py

Parse project-truth/implementation-blueprint.md.
Detect S01-S19 sections.
Extract section id, title, status, owner approval, start/end lines.
Emit generated/blueprint/blueprint-index.json.
"""

import json
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
BLUEPRINT_PATH = REPO_ROOT / "project-truth" / "implementation-blueprint.md"
OUTPUT_PATH = REPO_ROOT / "generated" / "blueprint" / "blueprint-index.json"

# Maps numeric section position (1-19) to section id (S01-S19)
def section_id(pos: int) -> str:
    return f"S{pos:02d}"

# Section header pattern: #### N. Title
SECTION_HEADER_RE = re.compile(r"^#### (\d+)\. (.+)$")
STATUS_RE = re.compile(r"^Status:\s*(.+)$")
OWNER_APPROVAL_RE = re.compile(r"^Owner approval:\s*(.+)$")

# Top-level blueprint status
BLUEPRINT_TOP_STATUS_RE = re.compile(r"^Status:\s*(blueprint-closed|blueprint-open)$")


def parse_blueprint(path: Path) -> dict:
    lines = path.read_text(encoding="utf-8").splitlines()

    blueprint_status = None
    sections = {}
    current_section = None
    current_start = None

    for lineno, line in enumerate(lines, start=1):
        # Detect top-level blueprint status (line 3 in current file)
        if lineno <= 10 and blueprint_status is None:
            m = BLUEPRINT_TOP_STATUS_RE.match(line.strip())
            if m:
                blueprint_status = m.group(1)

        # Detect section header
        m = SECTION_HEADER_RE.match(line)
        if m:
            pos = int(m.group(1))
            title = m.group(2).strip()
            sid = section_id(pos)

            # Close previous section
            if current_section is not None:
                sections[current_section]["end_line"] = lineno - 1

            current_section = sid
            current_start = lineno
            sections[sid] = {
                "section_id": sid,
                "position": pos,
                "title": title,
                "status": None,
                "owner_approval": None,
                "start_line": current_start,
                "end_line": None,
            }
            continue

        # Inside a section, extract status and owner approval
        if current_section is not None:
            sec = sections[current_section]

            if sec["status"] is None:
                m_s = STATUS_RE.match(line.strip())
                if m_s:
                    sec["status"] = m_s.group(1).strip()

            if sec["owner_approval"] is None:
                m_o = OWNER_APPROVAL_RE.match(line.strip())
                if m_o:
                    sec["owner_approval"] = m_o.group(1).strip()

    # Close the last section
    if current_section is not None:
        sections[current_section]["end_line"] = len(lines)

    # Sort sections by position
    ordered_sections = [sections[section_id(p)] for p in range(1, 20) if section_id(p) in sections]

    return {
        "source": str(BLUEPRINT_PATH.relative_to(REPO_ROOT)),
        "blueprint_status": blueprint_status,
        "total_sections_detected": len(ordered_sections),
        "sections": ordered_sections,
    }


def main():
    if not BLUEPRINT_PATH.exists():
        print(f"ERROR: Blueprint not found at {BLUEPRINT_PATH}", file=sys.stderr)
        sys.exit(1)

    index = parse_blueprint(BLUEPRINT_PATH)

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(json.dumps(index, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    print(f"blueprint-index.json written: {len(index['sections'])} sections detected")
    print(f"Blueprint status: {index['blueprint_status']}")
    return index


if __name__ == "__main__":
    main()
