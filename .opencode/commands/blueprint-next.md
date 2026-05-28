---
description: Execute the next eligible CAFL Blueprint section.
agent: cafl-blueprint-orchestrator
---

Execute the next eligible Blueprint section using the CAFL Blueprint Automation Loop.

Required constraints:
- Read `project-truth/blueprint-state.yaml` to select the next eligible section.
- Use `project-truth/implementation-blueprint.md` as the Blueprint working contract and `project-truth/blueprint-contract.yaml` as the automation contract.
- Use `docs/coordination/blueprint-automation-loop.md` as coordination guidance only.
- Max sections this run: 1.
- Route only through `cafl-blueprint-author` and `cafl-blueprint-verifier` as needed.
- Do not commit.
- Do not push.
- Stop when owner approval is required.

Report at the end:
- Selected section.
- Files changed.
- State changes.
- Reports created.
- Next handoff.
