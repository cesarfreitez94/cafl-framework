# S03 Context Packet - V1 / Post-V1 Boundary

Agent: cafl-blueprint-orchestrator  
Mode: normal  
Source status: bounded execution context for this section run; not a new source of truth.

## Selected Section

- section_id: S03
- title: V1 / Post-V1 Boundary
- iteration: I1 - Marco arquitectonico base
- current status: not-started
- owner approval: not-requested
- dependencies: S01, S02
- fix iterations: 0 / 2
- open issues: none

## Operational Eligibility

- `project-truth/blueprint-state.yaml` current iteration: I1, status `in-progress`, owner_gate `not-reached`.
- S01 and S02 are `approved` with owner approval recorded and non-empty `context_summary` values.
- S03 is the next not-started section in I1 whose dependencies are approved.
- Owner approval remains required after verification; agents cannot approve or close this section.

## Prior Approved Context Summaries

### S01 - Blueprint Scope and Non-Goals

Defines what the Blueprint is within CAFL V1 and what it must not cross. Fixed decisions: CRIT-01..07 approved and not reopened; TOM approved by DEC-ACCEPTED-161; `project-truth/` remains source of truth; CAFL V1 is Odoo-only targeting Odoo 18; OpenCode is primary runtime; pilot V1 is internal requests / simple approvals (DEC-ACCEPTED-162); minimal source policy is official Odoo docs + github.com/odoo/odoo (DEC-ACCEPTED-163); SDK/server out of V1 core (DEC-ACCEPTED-164); RAG/vector base deferred to V2. Blueprint must not create runtime, executable agents, real commands, physical schemas, real validators, scripts, RAG, detailed backlog, final PRD or SDD. `framework/` is excluded as input. Guardrails: every Blueprint component must be traceable to TOM, approved CRIT or accepted decision; conflicts must be registered, not resolved by agent criteria.

### S02 - Architecture Principles

Defines architecture principles AP-01..AP-12 for all later Blueprint sections. Invariants: single `project-truth/` authority and bidirectional traceability; OpenCode is primary runtime but not authoritative state, gate decision or evidence by itself; CAFL V1 uses a hybrid progressive model, not agents-only; LLM reasoning stays separated from verifiable deterministic control; progress is contract/gate/evidence driven with no self-closure; context routing and minimal source policy are mandatory; V1 remains Odoo-only on Odoo 18 and aligned to the confirmed internal requests / simple approvals pilot; V1 stays minimal with RAG/base vectorial, SDK/server core, dashboard/UI, CI/CD completo, DB avanzada, multiusuario/equipo, plugins/MCP, curation avanzada and broad post-V1 capabilities deferred unless future explicit owner decision allows them; storage/logs/evidence should remain simple, auditable and Git-compatible; security/risk/compliance and secrets are cross-cutting criteria; uncertain physical/runtime choices require Blueprint/spikes; design remains greenfield from `project-truth/` with `framework/` excluded. S02 does not decide runtime layout, physical paths, final schemas/validators, commands, permissions, exact Odoo environment, definitive storage, executable secrets policy or final spike order.

## Inherited Constraints For S03

- Preserve the S01 boundary: Blueprint design only; no runtime, executable agents, real commands, physical schemas, validators, scripts, RAG/vector base, detailed backlog, final PRD or SDD.
- Preserve S02 principles: single source of truth, traceability, hybrid progressive model, deterministic control separated from LLM reasoning, owner-gated progress, minimal source policy, and greenfield design from `project-truth/` only.
- Treat V1 as Odoo-only, Odoo 18-targeted, and instantiated around the confirmed pilot of internal requests / simple approvals.
- Do not move deferred/post-V1 capabilities into V1 without explicit owner decision.
- Register conflicts or untraceable limits as owner-decision issues instead of resolving them by agent judgment.

## Selected Section Excerpt From Working Contract

From `project-truth/implementation-blueprint.md` lines 304-323:

```md
#### 3. V1 / Post-V1 Boundary

Status: not-started

Inputs esperados:
- Secciones 1 y 2 de la iteracion correspondiente.
- Decisiones aceptadas, rechazadas y superseded sobre scope V1 y post-V1.

Outputs esperados:
- Limite V1 / post-V1 para guiar secciones posteriores.

Restricciones especificas:
- No mover capacidades post-V1 a V1 sin decision owner explicita.

Acceptance criteria minimos:
- Cada limite queda trazable y no reabre decisiones aprobadas.
```

## Compact Authority Anchors

### Accepted decisions

- DEC-ACCEPTED-013: CAFL is an operational framework/platform over OpenCode for enterprise Odoo solutions.
- DEC-ACCEPTED-028: OpenCode is CAFL's primary runtime.
- DEC-ACCEPTED-133/134: `framework/` is contaminated/discarded as design input and not migrated by default.
- DEC-ACCEPTED-135: Odoo target V1 is Odoo 18.
- DEC-ACCEPTED-136: CAFL V1 uses a hybrid progressive operating model over OpenCode.
- DEC-ACCEPTED-138: runtime candidate direction is OpenCode + commands + scripts/CLI/validators + simple auditable storage; not definitive architecture.
- DEC-ACCEPTED-140/145: V1 minimum automation/validators must cover structure, traceability, evidence, source policy/Knowledge Gap basics, rework/debt/approval when applicable, and minimal Odoo execution.
- DEC-ACCEPTED-148: RAG/vector base is not approved for V1; deferred to V2/post-V1 unless justified later.
- DEC-ACCEPTED-149 and DEC-ACCEPTED-164: SDK/server is outside V1 core by default; later inclusion requires favorable spike and explicit owner decision.
- DEC-ACCEPTED-151/152: broad automated documentation ingestion and real external integrations are not default V1 scope.
- DEC-ACCEPTED-153/156: V1 must execute/evidence a minimal real Odoo 18 end-to-end cycle, not just narrative recommendations.
- DEC-ACCEPTED-157: non-V1 capabilities are deferred to V2/post-V1, not rejected.
- DEC-ACCEPTED-161: TOM is approved; does not approve Blueprint, backlog, or implementation.
- DEC-ACCEPTED-162: pilot V1 is confirmed as internal requests / simple approvals; do not reopen or turn into final PRD/SDD/backlog here.
- DEC-ACCEPTED-163: minimal pre-authorized sources are official Odoo documentation and official GitHub `odoo/odoo`; other sources require Curation Request and approval.

### TOM anchors

- TOM `Alcance Operativo V1`: V1 is OpenCode-based, Odoo-only, Odoo 18-targeted, hybrid progressive, not agents-only, and must demonstrate an end-to-end verifiable Odoo 18 flow.
- TOM mechanism constraints: OpenCode is not by itself authoritative state, gate decision, final storage, final policy, or sufficient evidence; SDK/server is outside core V1.
- TOM Knowledge Governance: V1 starts with minimal source registry/source policy/knowledge artifacts/Knowledge Gap/Curation Request; no free web search and no V1 RAG/vector base.
- TOM pilot instance: internal requests / simple approvals is confirmed, real, scoped, Odoo 18, no complex external integration by default; UI/OWL/Playwright only if pilot justifies it.
- TOM open items for Blueprint/spikes: physical runtime layout, final mapping to agents/commands/scripts/validators/rules/skills, exact Odoo 18 environment, permissions, commands/skills, and Knowledge Governance without RAG/vector base.

### Rejected / superseded anchors

- DEC-REJECTED-016 and DEC-REJECTED-034: RAG/base vectorial is not approved/required for V1.
- DEC-REJECTED-035: SDK/server is not a mandatory V1 core component.
- DEC-REJECTED-038: real external integrations are not default V1 scope.
- Targeted search found no relevant superseded anchor for S03 beyond the accepted/rejected boundary above.

### Critical-map anchors

- CRIT-01: CAFL is OpenCode + Odoo, owner-controlled, V1 end-to-end with real scoped module; production deployment is out of initial scope.
- CRIT-02: hybrid controlled flow, PRD/SDD/task packets/DoR, context routing, risk-based testing; no final agents/contracts/gates/commands yet.
- CRIT-03: responsibilities and candidate mechanisms approved; no executable agents/prompts/commands/runtime.
- CRIT-04/05/06: conceptual contracts, gates, evidence, state, traceability, and knowledge governance approved; no final schemas, validators, commands, scripts, storage, runtime, RAG, or DB.
- CRIT-07: runtime candidate direction, Odoo 18 target, V1 cuts, RAG/vector deferred, SDK/server out of core, `framework/` excluded.

### Risk anchors

- RISK-008 / RISK-065 / RISK-066: avoid V1 scope creep and overly broad pilot.
- RISK-010 / RISK-057 / RISK-059: V1 needs reproducible verification, minimum automation, and Odoo 18 execution path later.
- RISK-028 / RISK-048 / RISK-053: avoid RAG/KB scope creep; keep knowledge governance incremental.
- RISK-058: avoid premature server/RAG/dashboard/CI/CD/advanced ingestion.
- RISK-062: enforce source policy; external sources need owner approval.
- RISK-064: do not reintroduce `framework/`.

## Non-Goals And Forbidden Artifacts

- Do not implement runtime or source code.
- Do not create executable/final agents, commands, schemas, validators, scripts, RAG/vector base, backlog, final PRD, or final SDD.
- Do not configure OpenCode or create final permissions.
- Do not use or reference `framework/`.
- Do not reopen CRIT-01..07, TOM, accepted decisions, pilot selection, source policy, or SDK/server exclusion.
- Do not advance S04+ content except by noting how S03 boundaries will guide later sections.

## Traceability Checklist For Author And Verifier

- Each V1 item must cite TOM, approved CRIT, or accepted decision support.
- Each post-V1/deferred item must cite accepted/rejected decision, TOM non-goal/deferred item, critical-map, or risk anchor.
- Boundary must include at least: core V1 operating model, Odoo 18 target, pilot constraint, minimum automation/evidence, knowledge/source policy minimum, deferred RAG/vector, SDK/server outside core, deferred dashboard/UI/CI/CD/DB/multiuser/plugins/MCP/curation advanced/integrations unless conditionally justified.
- Boundary must distinguish `V1 core`, `V1 conditional/spike`, and `post-V1/deferred` where helpful without creating backlog tasks.
- No boundary may move a deferred capability into V1 core without explicit owner decision.
- Any untraceable or conflicting limit must be marked as owner-decision blocker/open question, not solved by the agent.
- Section status after authoring/verification is not owner approval.

## Fallback-To-Strict Triggers

- Packet cannot prove traceability for a required S03 boundary.
- Packet conflicts with selected section content or `blueprint-state.yaml`.
- Owner-decision blocker appears.
- Approved dependency lacks `context_summary`.
- S03 work requires governance rule, source policy, status semantics, owner approval semantics, iteration gate closure, final traceability matrix, or acceptance criteria closure.
- Retroactive blocker or forbidden artifact ambiguity appears.
- Author or verifier introduces claims not covered by this packet.

## Sources Read Directly By Orchestrator For Packet

- `project-truth/blueprint-state.yaml` full operational state.
- `project-truth/blueprint-contract.yaml` automation contract.
- `project-truth/implementation-blueprint.md` targeted global rules, S03 excerpt, status summary.
- `docs/coordination/blueprint-automation-loop.md` coordination guidance only.
- Targeted excerpts/searches from `project-truth/TOM.md`, `project-truth/decisions/accepted.md`, `project-truth/decisions/rejected.md`, `project-truth/decisions/superseded.md`, `project-truth/decisions/pending.md`, `project-truth/critical-map.md`, and `project-truth/risks.md`.

Full authority fallback count: 0.
