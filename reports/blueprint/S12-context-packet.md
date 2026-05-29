# S12 Context Packet — Normal Mode

## Section Objective
Define conceptual source policy implementation and knowledge governance for CAFL V1, feeding Odoo execution (S13-S15) and pilot support without creating RAG/vector base, physical source registry, artifacts, validators, scripts, or implementation.

## Selected Section Excerpt (from working contract)

**Inputs**: S09, S10, S11; DEC-ACCEPTED-163; TOM Knowledge Governance rules.
**Outputs**: Implementacion conceptual de source policy y knowledge governance para alimentar Odoo execution y pilot support.
**Restricciones especificas**: No crear RAG/base vectorial. No ampliar fuentes sin Curation Request y aprobacion owner. No implementar source registry, artifacts, validators ni scripts.
**Acceptance criteria**: La seccion respeta source policy minima, Knowledge Gap y Curation Request sin implementacion.

## Dependency Context Summaries

### S09 — Schemas V1 Minimum Set (approved)
SCH-09 Source Policy / Knowledge Gap: logical category defining how source policy and knowledge governance metadata is structured. Serves deterministic controls, evidence, traceability, source policy. Handoff to S12: source policy/Knowledge Gap via VAL-01/VAL-09 as triggers. Traces to CRIT-06, CRIT-07, TOM, AP-01/AP-04/AP-06/AP-09, BR-01, accepted decisions.

### S10 — Validators V1 Minimum Set (approved)
VAL-01 (Authority Source validation) and VAL-09 (Source Policy validation) deliver Knowledge Gap triggers to S12 via validator candidate evidence. VAL-01 checks source freshness and authority compliance; VAL-09 validates eligibility and completeness. Both trace to CRIT-06, CRIT-07, AP-04/AP-05/AP-09, S04/S05/S08, TOM, BR-01, and decisions DEC-ACCEPTED-138/140/145/162/163. Conceptual only; no real validators created.

### S11 — State / Logs / Evidence Storage (approved)
4-level authority hierarchy: L1 project-truth/, L2 governed registered evidence, L3 candidate evidence, L4 ephemeral. 6-step evidence lifecycle: origin, capture, validation, eligibility evaluation, governed registration, authoritative reference. Handoffs to S12: evidence lifecycle and execution context log for source policy evidence. Storage types all Git-compatible per AP-09 and DEC-ACCEPTED-146. Traces to S05, S07, S08.

## Hard Inherited Constraints

1. **Source policy minima** (DEC-ACCEPTED-163): Only official Odoo docs + github.com/odoo/odoo are pre-authorized. Any other source requires Curation Request + owner approval.
2. **No RAG/vector base** (DEC-ACCEPTED-164): RAG deferred to V2/post-V1.
3. **project-truth/ is sole authority**: Runtime outputs never become authority.
4. **V1 scope**: Odoo-only, Odoo 18, internal requests / simple approvals pilot.
5. **framework/ excluded** as input/reference (RULE-10).
6. **No implementation artifacts**: No runtime, real validators, scripts, executables, backlog, PRD, SDD.
7. **Max fix iterations**: 2 (contract RULE).
8. **Source-vs-runtime separation** (S05): Source (project-truth/) is authority; runtime (OpenCode, candidates) is assistance only.

## Required Traceability Anchors

- **TOM Knowledge Governance**: Knowledge Gap triggers, Curation Request flow, source policy enforcement.
- **DEC-ACCEPTED-163**: Source policy minima.
- **DEC-ACCEPTED-164**: SDK/server and RAG deferral decisions.
- **CRIT-06, CRIT-07**: Traceability and control requirements.
- **AP-01, AP-04, AP-06, AP-09**: Architecture principles (authority, deterministic control, context routing, storage/evidence).
- **BR-01 (S03)**: V1/Post-V1 boundary.
- **S09 SCH-09, S10 VAL-01/VAL-09, S11 evidence lifecycle**: Direct handoff anchors.

## Forbidden Moves / Non-Goals

- NO RAG/vector base creation or design.
- NO source registry, source artifacts, physical schemas, or source database.
- NO validators or scripts (VAL-01/VAL-09 are conceptual handoffs only, do not instantiate).
- NO source policy expansion without Curation Request + owner approval.
- NO implementation of Knowledge Governance tooling.
- NO web search as direct design/implement source.
- NO `framework/` reference.
- NO creation of executable agents, real commands, physical schemas.

## Acceptance Checklist

- [ ] Section respects source policy minima (DEC-ACCEPTED-163).
- [ ] Knowledge Gap mechanism is conceptual, not implemented.
- [ ] Curation Request flow is defined conceptually, not as executable workflow.
- [ ] Handoffs from S09 SCH-09, S10 VAL-01/VAL-09, S11 evidence lifecycle are addressed.
- [ ] No RAG/vector base, source registry, artifacts, validators, or scripts created.
- [ ] All components traceable to TOM, CRIT, or accepted decision.
- [ ] V1 boundaries preserved (Odoo-only, Odoo 18, pilot scope, framework/ excluded).
- [ ] Outputs prepare for S13-S15 (Odoo execution, security, pilot module) and S16-S19 (spike order, traceability matrix, backlog categories, acceptance criteria).

## Fallback-to-Strict Triggers

- Packet conflicts with section content or operational state.
- Section requires governance rule, source policy, or status semantics changes.
- Author introduces claims not covered by this packet.
- Owner-decision blocker appears.
- Retroactive blocker detected.
- Forbidden artifact ambiguity (e.g., borderline RAG-like design).
- Author or verifier budget exceeded without owner override.

additional anchors available on fallback
