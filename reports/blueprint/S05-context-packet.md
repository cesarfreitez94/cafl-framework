# S05 Context Packet — Source-vs-Runtime Structure

Source status: bounded execution context for this section run only; not a new source of truth.

## Section Objective

Elaborate S05 as the conceptual source-vs-runtime separation for CAFL V1. It must use the approved S04 runtime layout candidate and prior approved boundaries to define how source-of-truth authority, runtime assistance, candidate mechanisms, deterministic control, evidence/state/logs, source policy, Odoo 18 pilot concerns, security/secrets and spikes remain separated without creating a physical runtime structure.

## Selected Section Excerpt

From `project-truth/implementation-blueprint.md` lines 494-515:

> #### 5. Source-vs-Runtime Structure
>
> Status: not-started
>
> Inputs esperados:
> - Seccion 4 de la iteracion correspondiente.
> - Reglas aprobadas sobre fuente de verdad, estado autoritativo y runtime.
>
> Outputs esperados:
> - Separacion source-vs-runtime para alimentar secciones posteriores.
>
> Restricciones especificas:
> - No recrear `framework/` ni usarlo como referencia.
> - No crear estructura fisica runtime.
>
> Acceptance criteria minimos:
> - La separacion queda trazable y no duplica fuentes de verdad.

## Dependency Context Summaries

- S01 approved: Blueprint is bounded to CAFL V1 and must not cross into runtime, executable agents, real commands, physical schemas, real validators, scripts, RAG/vector base, detailed backlog, PRD/SDD or implementation. `project-truth/` remains source of truth; CAFL V1 is Odoo-only on Odoo 18; OpenCode is primary runtime; pilot is internal requests / simple approvals; minimal source policy is official Odoo docs + `github.com/odoo/odoo`; SDK/server is out of V1 core; `framework/` is excluded.
- S02 approved: Later sections inherit AP-01..AP-12: single `project-truth/` authority, bidirectional traceability, OpenCode as runtime but not authoritative state/gate/evidence by itself, hybrid progressive model, separation of LLM reasoning from deterministic control, contract/gate/evidence-driven progress, mandatory context routing/minimal source policy, simple auditable Git-compatible storage posture, security/risk/compliance as cross-cutting, and physical/runtime details left for Blueprint/spikes.
- S03 approved: V1 core stays Odoo-only/Odoo 18/OpenCode-based for the internal requests / simple approvals pilot, with minimum evidence/control automation, source policy/Knowledge Gap basics, `project-truth/` traceability and simple auditable evidence/storage. Runtime layout, mechanism split, exact Odoo environment, permissions/commands/skills/secrets and Knowledge Governance remain conceptual/conditional. RAG/vector, SDK/server core, broad ingestion/integrations, dashboards/UI productization, full CI/CD, advanced DB/storage, multiuser/team, plugins/MCP, advanced curation and broad post-V1 capabilities remain deferred unless future owner decision changes scope.
- S04 approved: Provides a conceptual runtime layout candidate only. Candidate zones: source of truth / decision record, OpenCode coordination, repeatable inputs / command candidates, deterministic control candidates, auditable state/logs/evidence, source policy / Knowledge Gap, Odoo 18 pilot integration, security / permissions / secrets, and spikes / technical validations. S04 does not approve physical structure, final paths, implementation, executable agents, real commands, schemas, validators, scripts, backlog, PRD or SDD.

## Hard Inherited Constraints

- All S05 components must be traceable to TOM, approved CRIT, accepted decisions, and/or approved S01-S04 summaries; unsupported items must be eliminated, marked post-V1, or registered as owner-decision required.
- Do not reopen CRIT-01..CRIT-07, TOM approval, DEC-ACCEPTED-161..164, or approved S01-S04 boundaries.
- S05 may define conceptual separation rules and interfaces between source and runtime concerns, but must not create final physical paths, runtime skeleton, executable files, real OpenCode agents, real commands, final schemas, real validators, scripts, RAG/vector base, SDK/server core, backlog, PRD, SDD, or implementation.
- Do not use or reference `framework/` as an input or migration source.
- `project-truth/` remains authoritative source; runtime outputs, session notes, command outputs or evidence candidates do not become authoritative without defined traceable registration.
- OpenCode is primary runtime/coordination support, not authoritative state, gate decision, final storage, final policy, or sufficient evidence by itself.
- V1 core prioritizes OpenCode + command candidates + scripts/CLI/validator candidates + simple auditable storage; SDK/server is outside core V1 unless later spike plus explicit owner decision.
- RAG/vector base, advanced DB/storage, dashboard/productized UI, full CI/CD, MCP/plugins, broad integrations and advanced curation are outside V1 core.
- Source policy base remains official Odoo documentation + official GitHub `odoo/odoo`; other sources require Curation Request / owner approval.
- Pilot selection is fixed: internal requests / simple approvals in Odoo 18; S05 must not turn it into final PRD, SDD, backlog or implementation design.

## Required Traceability Anchors

- TOM lines 48-55: CAFL is an OpenCode-based framework/platform for Odoo; V1 is Odoo-only/Odoo 18; V1 must demonstrate an end-to-end verifiable flow; hybrid progressive model; minimum automation includes structure validation, DoR, traceability, logs/state/evidence, Odoo 18 execution evidence and source policy / Knowledge Gap basics.
- TOM lines 79-93: OpenCode assists coordination/runtime but is not state/gate/storage/policy/evidence by itself; scripts/CLI/validators are deterministic-control candidates; knowledge governance forbids free web/RAG assumptions.
- TOM lines 206-246 and DEC-ACCEPTED-163/164: minimal source policy, Knowledge Gap, source usage, no RAG/vector V1 and no SDK/server core V1.
- TOM lines 351-366: Blueprint must resolve runtime layout, mechanism mapping, storage/log/evidence conventions, OpenCode setup, Odoo 18 environment, evidence capture, source policy enforcement, secrets handling and pilot instantiation without reopening pilot choice.
- Critical-map CRIT-06/CRIT-07: state/evidence/traceability/source governance are logical authority concerns; runtime candidate direction is OpenCode + commands + scripts/CLI/validators + simple storage, with no final physical implementation and no `framework/` input.
- Accepted decisions: DEC-ACCEPTED-001 (`project-truth/` source), 028 (OpenCode runtime), 133/134 (`framework/` discarded), 135 (Odoo 18), 136 (hybrid OpenCode model), 138 (runtime candidate direction), 145 (minimum deterministic validators as direction, not implementation), 161 (TOM approved), 162 (pilot fixed), 163 (minimal source policy), 164 (SDK/server outside core V1).
- Risks to control: RISK-006 traceability loss, RISK-011 fragmented truth, RISK-019 packet insufficiency, RISK-020 OpenCode assumptions without spikes, RISK-022/023/024 agents-only or prompt-only control, RISK-025 token/context overuse, RISK-043/052/054/062 source policy gaps, RISK-048/058 RAG/server/overautomation creep, RISK-064 `framework/` reintroduction, RISK-065 deferred capabilities advanced.

## Forbidden Moves / Non-Goals

- Do not create or approve final directory trees, file paths, package layout, schemas, validators, scripts, commands, permission rules, OpenCode config, agents, skills, MCP/plugins, RAG/vector DB, SDK/server, CI/CD, dashboard/UI product, advanced DB/storage, backlog, PRD, SDD, or implementation artifacts.
- Do not make runtime logs, command outputs, OpenCode sessions, author reports or verifier reports authoritative sources unless S05 explicitly keeps them as candidate/evidence inputs requiring traceable registration under `project-truth/` governance.
- Do not duplicate `project-truth/` with a second source of truth or define a competing status/approval record.
- Do not use external web sources or unauthorized examples.
- Do not close S05, approve S05, alter owner approval semantics, or advance S06+ content.
- Do not resolve conflicts by agent judgment; register blocking conflicts as owner-decision required.

## Acceptance Checklist For S05

- Status becomes `in-verification` after authoring, with owner approval still not requested/approved.
- S05 defines a conceptual source-vs-runtime separation that feeds later sections without creating physical runtime structure.
- The separation clearly distinguishes authoritative sources/decisions/state from runtime assistance, candidate mechanism outputs, evidence candidates, logs and reports.
- Every proposed category, rule or boundary is traceable to at least one anchor above or marked out-of-scope / owner-decision required.
- No duplicated source of truth, competing approval record, `framework/` reference, forbidden artifact or implementation detail is introduced.
- Deferred/post-V1 items remain deferred unless marked owner-decision required.
- Any ambiguity that cannot be resolved from this packet is recorded as an open issue or owner-decision blocker; do not invent.

## Fallback-To-Strict Triggers

- Packet cannot prove required traceability for a proposed source/runtime boundary.
- Packet conflicts with S05 excerpt, approved S01-S04 summaries, state, or contract.
- Owner-decision blocker appears.
- Need to change governance rule, source policy, status semantics, owner approval semantics, or iteration gate closure.
- Forbidden artifact ambiguity appears, especially around whether a path/schema/log/store/command is conceptual or final.
- Retroactive blocker against S01-S04 appears.
- Author or verifier needs to introduce claims not covered by this packet.
