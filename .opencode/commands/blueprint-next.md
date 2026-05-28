---
description: Execute the next eligible CAFL Blueprint section.
agent: cafl-blueprint-orchestrator
---

Execute the next eligible Blueprint section using the CAFL Blueprint Automation Loop.

Owner usage:
- `/blueprint-next` runs in normal mode.
- `/blueprint-next strict` or `STRICT S03` requests strict mode for the selected section.
- If OpenCode command arguments are unreliable, treat any owner message containing `strict` or `STRICT {section_id}` with the command invocation as an explicit strict request.

Required constraints:
- Read `project-truth/blueprint-state.yaml` to select the next eligible section.
- Use `project-truth/implementation-blueprint.md` as the Blueprint working contract and `project-truth/blueprint-contract.yaml` as the automation contract.
- Treat `docs/coordination/blueprint-automation-loop.md` as reference coordination guidance only; author and verifier must not read it in normal mode.
- Default to normal mode for ordinary section authoring and verification.
- Use strict mode only when explicitly requested by the owner or when a fallback-to-strict trigger fires.
- Normal mode budgets: context packet <=15000 chars, author estimated source chars <=30000, verifier estimated source chars <=40000.
- In normal mode, generate a compact `reports/blueprint/{section_id}-context-packet.md` before routing `cafl-blueprint-author`.
- Treat the context packet as bounded execution context for one section run, not as a new source of truth.
- Compact packets include only section objective, selected section excerpt, dependency context summaries, hard inherited constraints, required traceability anchors, forbidden moves / non-goals, acceptance checklist, and fallback-to-strict triggers.
- Compact packets must avoid long decision lists, long risk catalogs, broad TOM excerpts, repeated coordination rules, and excessive prose.
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
- Mode: normal|strict.
- Context packet path and whether it was generated.
- Context packet chars.
- Full authority fallback count.
- Large repeated reads avoided.
- Estimated source chars read, if practical.
- `budget_exceeded: yes|no`, `budget_exceeded_by_chars`, `largest_read_source`, and `optimization_recommendation`.
- Next handoff.
