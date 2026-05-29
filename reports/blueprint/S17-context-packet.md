# S17 Context Packet

## Metadata
- `section_id`: S17
- `section_title`: Bidirectional Traceability Matrix
- `iteration`: I5
- `depends_on`: [S16]
- `dependency_context_summaries_complete`: yes
- `mode`: normal

## Section Objective
Construct the bidirectional traceability matrix for CAFL V1 Blueprint:
- **TOM → Blueprint**: every relevant TOM requirement traces to ≥1 Blueprint component
- **Blueprint → TOM**: every Blueprint component traces to ≥1 TOM requirement, approved CRIT, or accepted decision
Must be complete, bidirectional, and gap-free per RULE-04 / RULE-05.

## Section Excerpt (Blueprint Working Contract)
- **Inputs**: Secciones 1 a 16 elaboradas y aprobadas. TOM aprobado y decisiones aceptadas aplicables.
- **Outputs**: Matriz bidireccional TOM→Blueprint y Blueprint→TOM.
- **Restricciones**: No aprobar componentes sin respaldo trazable.
- **Acceptance criteria**: La matriz queda completa, bidireccional y sin gaps.

## Dependency Context Summary

### S16 — Spikes and Technical Validations final order (approved)
Consolidates all CAFL V1 spikes: S06 SP-01..SP-13 (bands A→B→C, band D conditional), S13 environment spikes (5, RISK-059 critical), S14 security spikes (SPK-S14-01..04), S15 pilot module spikes (6). Execution order in Tiers 1–8 with explicit dependencies. SP-04/SP-05 open uncertainties. Band D conditional/separated. Knowledge Gaps and Curation Requests from S12 are spike inputs.

**S16→S17 handoff**: Consolidated catalogue (SP-01..SP-13 + SPK-Snn) with traceability anchors (TOM, CRIT-01..07, accepted decisions, risks), dependency chain (Tiers 1–8), SP-04/SP-05 flagged conditional. S17 must use S16 catalogue; must not reconstruct spike identifiers independently.

## Key Handoff Inputs from Prior Sections
- **S11**: L2 registered evidence model → base for traceability matrix
- **S12**: Approved Curation Requests + resolved Knowledge Gaps → L2 eligible evidence
- **S13**: Logical component map (7 components, 3 env categories) → Odoo 18 environment traceability
- **S15**: Pilot module component map (models, views, workflow, security, evidence, tests) → pilot traceability
- **S16**: Consolidated spike catalogue → spike-side traceability input
- S17 cannot close matrix alone; requires owner approval.

## Hard Inherited Constraints
- **RULE-04**: Every Blueprint component must have backing in TOM, approved CRIT, or accepted decision. Unbacked → eliminate, mark post-V1, or register `owner decision required`.
- **RULE-05**: Bidirectional: TOM→Blueprint AND Blueprint→TOM.
- **RULE-09**: No runtime, agents, commands, schemas, validators, scripts, RAG, vector base, backlog, or implementation.
- **RULE-10**: Do not use `framework/` as input.
- SCH-02 defines link structure: identifier, origin, destination, relationship type, mandatory, state, evidence, gaps/conflicts, consuming section.
- SP-04/SP-05 entries must be marked conditional/open uncertainty; not resolved.
- Band D spikes (SP-11..SP-13) traced as conditional/post-V1.
- Matrix closure requires explicit owner approval.

## Required Traceability Scope
Matrix must cover: CRIT-01..07, TOM, AP-01..12, BR-01..04, accepted decisions referenced by S01-S16, all sections S01-S16, SCH-01..10, VAL-01..10, SP-01..13 + SPK-Snn, relevant RISK items, S13 logical components (7), S14 control areas CA-1..4, S15 pilot module components.

## Forbidden Moves
- Do not approve/close sections, resolve SP-04/SP-05, close Knowledge Gaps or approve Curation Requests, expand V1 scope or source policy, create implementation artifacts, use `framework/`, commit or push.

## Acceptance Checklist
- [ ] Bidirectional coverage (TOM↔Blueprint) per RULE-04/05
- [ ] All S01-S16 sections covered as components
- [ ] All spikes SP-01..13 + SPK-Snn covered; identifiers from S16 catalogue only
- [ ] All SCH-01..10 and VAL-01..10 covered
- [ ] CRIT-01..07, AP-01..12, BR-01..04 referenced
- [ ] Accepted decisions referenced by S01-S16 covered
- [ ] Relevant RISK items covered
- [ ] SP-04/SP-05 marked conditional
- [ ] Band D (SP-11..13) marked conditional/post-V1
- [ ] Link structure follows SCH-02
- [ ] No gaps: every component has ≥1 backing anchor
- [ ] Matrix does not close or approve anything
- [ ] No forbidden artifacts (RULE-09/10)
- [ ] V1 boundaries preserved

## Fallback-to-Strict Triggers
- Traceability gap without owner-decision registration
- Ambiguous TOM requirement mapping
- Missing anchor for a Blueprint component
- Source-policy conflict with traceability requirement
- SP-04/SP-05 or Band D scope question requiring owner decision
