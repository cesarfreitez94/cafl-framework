# S06 Context Packet — Initial Spike Map

## Section Objective
Define the initial spike map for CAFL V1. Each spike must derive from technical uncertainties registered in TOM (lines 368-383), accepted risks, and limitations recognized in S01-S05. Output feeds S16 for final ordering. Section must produce a dependency-ordered map, not a flat list (RULE-06).

## Section Excerpt (implementation-blueprint.md, L573-593)
- **Inputs esperados:** Secciones 1 a 5; Riesgos aceptados y technical validations/spikes registrados en TOM.
- **Outputs esperados:** Mapa inicial de spikes para alimentar orden final de validaciones.
- **Restricciones específicas:** No ejecutar spikes. No dejar spikes como lista plana.
- **Acceptance criteria mínimos:** Cada spike esperado queda vinculado a riesgo, decisión o dependencia sin ejecutarse.

## Dependency Context Summaries (from blueprint-state.yaml)
- **S01:** Blueprint scope is Odoo-only V1 (Odoo 18), OpenCode primary runtime, pilot=internal requests/simple approvals. RAG/vector, SDK/server, dashboard/UI, CI/CD, DB avanzada, multiuser, plugins/MCP deferred. No runtime, no executable artifacts, no backlog. `framework/` excluded.
- **S02:** AP-11 mandates spike-driven validation before closing uncertain physical decisions. AP-08 enforces minimal V1 / anti-scope-creep. AP-01 requires bidirectional traceability. AP-12 excludes `framework/`.
- **S03:** BR-02 classifies conditional/spike areas: runtime layout/mechanism split, Odoo 18 environment, UI/OWL/Playwright (pilot-justified only), permissions/commands/skills/secrets, Knowledge Governance without RAG.
- **S04:** "Spikes y validaciones técnicas" zone reserved for S06/S16 to order validations for: language/toolchain, Odoo 18 environment, OpenCode permissions, schemas/validators, storage/log convention, source policy/Knowledge Gap, evidence capture, secrets.
- **S05:** Spikes/uncertainties remain governed; S05 does not execute spikes. Handoff to S06/S16: order spikes to validate uncertainties without implementing.

## Hard Inherited Constraints
- **RULE-04:** Every component traceable to TOM, approved CRIT, or accepted decision.
- **RULE-06:** Spikes must have explicit justified execution order with dependencies; not a flat list.
- **RULE-09:** No runtime, executable agents, real commands, physical schemas, validators, scripts, RAG/vector, backlog, or implementation.
- **RULE-10:** No use of `framework/` as input or reference.
- **AP-11:** Technical validation by spikes before closing uncertain physical decisions.
- **AP-08:** V1 minimal; anti-scope-creep.
- **S05 handoff:** Order spikes for S06/S16 without executing implementation.

## Required Traceability Anchors

### TOM Spike Candidates (TOM §Technical Validations / Spikes, L368-383)
| ID | Spike Area | Constraint |
|---|---|---|
| TOM-S01 | Scripts/CLI language | No Python/Node assumed; decide by local ease, JSON/YAML/JSONL, Odoo integration, speed, maintainability, OpenCode friction |
| TOM-S02 | Odoo 18 environment | Docker/venv/local; exact form undecided |
| TOM-S03 | OpenCode permissions | Validation needed before runtime |
| TOM-S04 | OpenCode commands/skills | Design candidate; no execution |
| TOM-S05 | SDK/server evaluation | NOT core V1; conditional only with favorable spike + owner decision (DEC-ACCEPTED-149/164) |
| TOM-S06 | Schema/validator toolchain | Toolchain selection pending |
| TOM-S07 | Storage/log convention | Simple, auditable, Git-compatible |
| TOM-S08 | Source policy enforcement + Knowledge Gap basics | Minimal; no RAG/vector |
| TOM-S09 | Knowledge governance without RAG | Source registry, K-Gap, Curation Request basics |
| TOM-S10 | Odoo 18 install/update/test execution | Minimal end-to-end cycle evidence |
| TOM-S11 | Evidence capture | Reproducible, separable from chat/prompts |
| TOM-S12 | Secrets handling | Tokens, credentials, Odoo secrets; must not enter repo/logs |
| TOM-S13 | OpenAPI/PDF processing | Conditional: only if future scope decision requires |
| TOM-S14 | Frontend/OWL/Playwright | Conditional: only if pilot-approved requirement exists |

### Key Risks (accepted, from risks.md)
- **RISK-020:** Assuming OpenCode capabilities without spikes → TOM-S01..S04
- **RISK-025:** Token excess from poor responsibility allocation → TOM-S03, S04
- **RISK-059:** Missing Odoo 18 environment → TOM-S02, S10
- **RISK-060:** Wrong script/CLI language → TOM-S01
- **RISK-061:** Unvalidated OpenCode permissions → TOM-S03
- **RISK-063:** Insecure secrets → TOM-S12
- **RISK-058:** Early over-automation → TOM-S05, S09
- **RISK-018:** Excess tokens from weak context routing → TOM-S03
- **RISK-006:** Loss of traceability → TOM-S07, S08
- **RISK-010:** Non-reproducible verification → TOM-S10, S11
- **RISK-065:** Deferred capabilities advanced → TOM-S05, S13, S14 (anti-scope-creep)
- **RISK-032:** Token budget without traceable exception → TOM-S03
- **RISK-039:** Minimal testing omitted as acceptable debt → TOM-S10
- **RISK-043:** Free web search as direct source → TOM-S08
- **RISK-044:** Insufficient/outdated Odoo knowledge → TOM-S08
- **RISK-045:** Unversioned official documentation → TOM-S08
- **RISK-047:** Misinterpreted Swagger/PDF/API → TOM-S13
- **RISK-050:** Legal/compliance without official source → TOM-S08

### Key Accepted Decisions
- **DEC-ACCEPTED-049/050:** Spikes mandated for OpenCode validation; do not reopen OpenCode as primary runtime.
- **DEC-ACCEPTED-135:** Odoo 18 target V1; environment form = spike.
- **DEC-ACCEPTED-142/143:** Script/CLI language decided by spike with criteria (local ease, JSON/YAML/JSONL, Odoo integration, speed, maintainability, OpenCode friction).
- **DEC-ACCEPTED-149/164:** SDK/server outside core V1; only with favorable spike + owner decision.
- **DEC-ACCEPTED-153:** V1 must execute and evidence minimal Odoo 18 cycle.
- **DEC-ACCEPTED-158:** Spikes formally defined; CRIT-07 records need, does not execute/close results.

## Forbidden Moves / Non-Goals
- **NO** ejecutar spikes (no implementation, execution, or closure of technical uncertainties).
- **NO** lista plana sin dependencias justificadas (RULE-06).
- **NO** runtime, agents ejecutables, commands reales, schemas físicos, validators reales, scripts, RAG/vector, backlog, PRD, SDD.
- **NO** usar `framework/` como input o referencia.
- **NO** reabrir CRIT-01..07, TOM, pilot selection, source policy.
- **NO** ampliar source policy sin Curation Request + owner approval.
- **NO** introducir capacidades post-V1 (RAG, SDK/server core, dashboard/UI, CI/CD, DB avanzada, MCP/plugins, broad ingestion) como V1.

## Acceptance Checklist
- [ ] Cada spike vinculado a riesgo, decisión o dependencia trazable (RULE-04).
- [ ] Spikes ordenados con dependencias justificadas (RULE-06); no lista plana.
- [ ] Ningún spike ejecutado.
- [ ] Trazabilidad bidireccional: TOM/riesgo/decisión → spike.
- [ ] S06 es conceptual; no crea artefactos ejecutables (RULE-09).
- [ ] `framework/` excluido (RULE-10).
- [ ] Sección queda en `Status: in-verification`.

## Fallback-to-Strict Triggers
- Packet cannot prove traceability for any spike.
- Spike conflicts with S01-S05 approved context.
- Owner-decision blocker appears (e.g., spike covers post-V1 capability without owner decision).
- Forbidden artifact ambiguity (spike looks like implementation artifact).
- Retroactive blocker in S01-S05 detected.
- Author/verifier introduces claims not covered by this packet.
- Governance, source policy, or status semantics change attempted.

---
*Generated by cafl-blueprint-orchestrator / Normal mode / Target: S06 Initial Spike Map*
