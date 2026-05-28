# S04 Context Packet — Runtime Layout Candidate

Source status: bounded execution context for this section run only; not a new source of truth.

## Section Objective

Elaborate S04 as a conceptual Runtime Layout Candidate for CAFL V1. It must feed later sections on source-vs-runtime structure, mechanisms, storage, OpenCode operating design, schemas, validators, Odoo execution, security/secrets, pilot blueprint and spikes.

## Selected Section Excerpt

From `project-truth/implementation-blueprint.md` lines 400-420:

> #### 4. Runtime Layout Candidate
>
> Status: not-started
>
> Inputs esperados:
> - Secciones 1, 2 y 3 de la iteracion correspondiente.
> - Handoff del TOM al Blueprint y decisiones CRIT-07 aplicables.
>
> Outputs esperados:
> - Candidato conceptual de layout para alimentar secciones de estructura, mecanismos y storage.
>
> Restricciones especificas:
> - No crear runtime, rutas fisicas finales ni archivos ejecutables.
> - No usar `framework/` como input.
>
> Acceptance criteria minimos:
> - El candidato queda conceptual, trazable y sin implementacion.

## Dependency Context Summaries

- S01 approved: Blueprint remains within CAFL V1; `project-truth/` is source of truth; Odoo-only/Odoo 18/OpenCode runtime direction; pilot is internal requests/simple approvals; official Odoo docs + `github.com/odoo/odoo` are the pre-authorized source base; SDK/server out of V1 core; RAG/vector base deferred; no runtime, executable agents, real commands, physical schemas, real validators, scripts, backlog, PRD/SDD, or implementation; `framework/` excluded.
- S02 approved: Architecture principles AP-01..AP-12 require single authority, bidirectional traceability, OpenCode as primary runtime but not authoritative state/gate/evidence by itself, hybrid progressive model, LLM reasoning separated from deterministic control, evidence/gate driven progress, minimal source policy, V1 Odoo 18 internal-request pilot, simple auditable Git-compatible storage posture, security/risk/compliance as cross-cutting, and physical/runtime details left for Blueprint/spikes.
- S03 approved: V1 core is limited to the Odoo-only, Odoo 18, OpenCode-based hybrid operating model for internal requests/simple approvals with minimum evidence/control automation, source policy/Knowledge Gap basics, `project-truth/` traceability and simple auditable evidence/storage. Runtime layout, mechanism split, Odoo execution environment, permissions/commands/skills/secrets and Knowledge Governance are conditional/conceptual and must not imply implementation approval. RAG/vector, SDK/server core, broad ingestion, dashboards/UI productization, full CI/CD, advanced DB/storage, multiuser/team, plugins/MCP, advanced curation and broad integrations remain post-V1 unless future owner decision changes scope.

## Hard Inherited Constraints

- All Blueprint components must be traceable to TOM, approved CRIT, or accepted decision; unsupported items must be eliminated, marked post-V1, or registered as owner-decision required.
- Do not reopen CRIT-01..CRIT-07, TOM, DEC-ACCEPTED-161..164, or the approved S01-S03 boundaries.
- S04 may propose a conceptual layout candidate, but must not create runtime, final physical paths, executable files, real commands, final schemas, real validators, scripts, RAG/vector base, detailed backlog, PRD, SDD, or implementation.
- Do not use or reference `framework/` as an input.
- OpenCode is primary runtime, but not authoritative state, gate decision, final storage, final policy, or sufficient evidence by itself.
- V1 core must prioritize OpenCode + commands candidates + scripts/CLI/validators candidates + simple auditable storage; SDK/server is outside core V1 unless later spike + explicit owner decision.
- RAG/vector base is outside V1.
- Source policy base is official Odoo documentation + official GitHub `odoo/odoo`; any other source requires Curation Request/owner approval.
- Pilot selection is fixed: internal requests / simple approvals in Odoo 18; S04 must not turn it into final PRD/SDD/backlog.

## Required Traceability Anchors

- TOM lines 48-55: CAFL is an OpenCode-based framework/platform for Odoo; V1 is Odoo-only/Odoo 18; V1 must demonstrate end-to-end verifiable flow; hybrid progressive model; minimum automation includes structure validation, DoR, traceability, logs/state/evidence, Odoo 18 execution evidence, source policy/Knowledge Gap basics.
- TOM lines 63-72 and 79-93: mechanisms are human, agent, command, SDK/server/script, rule/config/skill or mixed; agents reason, commands standardize repeatable entries, scripts/CLI/validators are candidates for deterministic controls, rules/config hold invariants, skills/playbooks support on-demand knowledge; OpenCode is not state/gate/storage/policy/evidence by itself.
- TOM lines 351-366: Blueprint must resolve runtime layout, mechanism mapping, storage/log/evidence conventions, OpenCode setup, Odoo 18 environment, evidence capture, source policy enforcement, secrets handling, and pilot instantiation without reopening pilot choice.
- TOM lines 368-383: S04 should preserve spike/technical-validation placeholders for script/CLI language, Odoo 18 environment, OpenCode permissions/commands/skills, schema/validator toolchain, storage/log convention, source policy/Knowledge Gap, knowledge governance without RAG/vector, evidence capture, secrets, and frontend only if pilot needs it.
- CRIT-07 / critical-map: approved candidate direction is OpenCode + commands + scripts/CLI/validators + simple storage, with no implementation, no final paths/schemas/validators/commands/scripts, no SDK/server core, no RAG/vector, and no `framework/` input.
- Accepted decisions: DEC-ACCEPTED-135 (Odoo 18), 136 (hybrid progressive OpenCode model), 138 (runtime candidate direction), 148 (RAG/vector not approved for V1), 149/164 (SDK/server outside V1 core), 161 (TOM approved), 162 (pilot fixed), 163 (minimal source policy), 133/134 (`framework/` discarded).
- Risks to control: RISK-006 traceability loss, RISK-010 non-reproducible verification, RISK-018/025/032 token/context overuse, RISK-020 OpenCode assumptions without spikes, RISK-022/023/024 agents-only or prompt-only control, RISK-048/058 overautomation/RAG/server creep, RISK-059 Odoo 18 environment unknown, RISK-061 permissions, RISK-063 secrets, RISK-064 `framework/` reintroduction, RISK-065 deferred capabilities advanced.

## Forbidden Moves / Non-Goals

- Do not name or create final directories/files as approved runtime paths; conceptual zones/categories are allowed if labeled non-final and spike-dependent.
- Do not define executable OpenCode agents, commands, skills, permission rules, schemas, validators, scripts, MCP/plugins, RAG, vector DB, SDK/server, CI/CD, dashboard/UI product, or advanced DB/storage as V1 core.
- Do not use external web sources or unauthorized examples.
- Do not close S04, approve S04, or alter owner approval semantics.
- Do not edit future sections except only the permitted status summary row if the author instructions allow it.

## Acceptance Checklist For S04

- Status becomes `in-verification` after authoring, with owner approval still not requested/approved.
- S04 provides a conceptual runtime layout candidate that can feed S05/S07/S11/S13/S14 without final physical implementation.
- Every proposed zone/component is traced to at least one TOM/CRIT/accepted-decision anchor above.
- The layout keeps OpenCode/hybrid model, deterministic control candidates, source policy, evidence/logs/state, and Odoo 18/pilot needs visibly separated.
- Deferred/post-V1 items remain deferred unless marked owner-decision required.
- No forbidden artifact or `framework/` reference is introduced.
- Any ambiguity that cannot be resolved from this packet is recorded as an open issue or owner-decision blocker; do not invent.

## Fallback-To-Strict Triggers

- Packet cannot prove required traceability for a proposed layout component.
- Packet conflicts with S04 excerpt, approved S01-S03 summaries, state, or contract.
- Owner-decision blocker appears.
- Need to change governance rule, source policy, status semantics, owner approval semantics, or iteration gate closure.
- Forbidden artifact ambiguity appears (e.g., whether a path/schema/command is conceptual vs final).
- Retroactive blocker against S01-S03 appears.
- Author or verifier needs to introduce claims not covered by this packet.
