# Backlog Candidate Generation Report

Generated: 2026-05-30T06:45:47.273476+00:00
Generator: `tools/blueprint/blueprint_to_backlog.py`

## Generation Summary

- **Source**: S18 Blueprint Outputs to Backlog (9 categories)
- **S17 Traceability Matrix**: bidirectionally complete
- **Total Epics generated**: 9
- **Total Capabilities generated**: 30
- **Total items generated**: 39

## S18 Category Source Lines

| Category ID | Title | Blueprint Source Line |
| --- | --- | --- |
| CAT-01 | Runtime / OpenCode coordination setup | project-truth/implementation-blueprint.md line 2809 |
| CAT-02 | Mechanism implementation boundaries | project-truth/implementation-blueprint.md line 2810 |
| CAT-03 | Control and evidence infrastructure | project-truth/implementation-blueprint.md line 2811 |
| CAT-04 | Source policy and Knowledge Governance | project-truth/implementation-blueprint.md line 2812 |
| CAT-05 | Odoo 18 pilot environment and module | project-truth/implementation-blueprint.md line 2813 |
| CAT-06 | Security and secrets | project-truth/implementation-blueprint.md line 2814 |
| CAT-07 | Spike execution and technical validations | project-truth/implementation-blueprint.md line 2815 |
| CAT-08 | Traceability and quality gates | project-truth/implementation-blueprint.md line 2816 |
| CAT-09 | Owner / governance workflows | project-truth/implementation-blueprint.md line 2817 |

## Readiness Distribution

| Readiness | Epics | Capabilities | Total |
| --- | --- | --- | --- |
| candidate | 5 | 22 | 27 |
| conditional | 3 | 7 | 10 |
| post-v1 | 1 | 1 | 2 |

## Items Requiring Owner Decision

| ID | Type | Title | Owner Decision | Readiness |
| --- | --- | --- | --- | --- |
| EPIC-BACKLOG-002 | epic | Mechanism implementation boundaries | pending-spike-result | conditional |
| EPIC-BACKLOG-005 | epic | Odoo 18 pilot environment and module | pending-spike-result | conditional |
| EPIC-BACKLOG-006 | epic | Security and secrets | pending-spike-result | conditional |
| EPIC-BACKLOG-007 | epic | Spike execution and technical validations | yes | post-v1 |
| CAP-BACKLOG-005 | capability | Command candidate standardisation | pending-spike-result | conditional |
| CAP-BACKLOG-006 | capability | Script/CLI/validator boundary definition | pending-spike-result | conditional |
| CAP-BACKLOG-015 | capability | Odoo 18 environment readiness specification | pending-spike-result | conditional |
| CAP-BACKLOG-016 | capability | Pilot module candidate boundary definition | pending-spike-result | conditional |
| CAP-BACKLOG-018 | capability | Secrets handling posture specification | pending-spike-result | conditional |
| CAP-BACKLOG-019 | capability | Permissions boundary model specification | pending-spike-result | conditional |
| CAP-BACKLOG-023 | capability | Open uncertainty tracking (SP-04/SP-05) | pending-spike-result | conditional |
| CAP-BACKLOG-024 | capability | Post-V1 gated spike separation (SP-11..SP-13) | yes | post-v1 |
| CAP-BACKLOG-030 | capability | Deferred/post-V1 owner decision registry | yes | candidate |

## Epics

### EPIC-BACKLOG-001: Runtime / OpenCode coordination setup
- **Source Category**: Runtime / OpenCode coordination setup
- **Source Sections**: S01, S02, S04, S05, S07, S17
- **Upstream Refs**: AP-02, AP-03, AP-04, AP-05, BR-01, BR-02, CRIT-02, CRIT-03, CRIT-07, DEC-ACCEPTED-028, DEC-ACCEPTED-136, DEC-ACCEPTED-137, DEC-ACCEPTED-138, DEC-ACCEPTED-140, RISK-020, RISK-023, RISK-024, RISK-055, S01, S02, S04, S05, S07, S17, SP-04, SP-05, TOM-01, TOM-04, TOM-07
- **Readiness**: candidate
- **Owner Decision Required**: none
- **Rationale**: Derived from S18 category 'Runtime / OpenCode coordination setup'. Work domain for representing the CAFL V1 operating arrangement around OpenCode coordination, contract-driven progression, gate discipline, and non-authoritative runtime support.

### EPIC-BACKLOG-002: Mechanism implementation boundaries
- **Source Category**: Mechanism implementation boundaries
- **Source Sections**: S07, S08, S10, S16, S17
- **Upstream Refs**: AP-02, AP-03, AP-04, AP-05, CRIT-03, CRIT-07, DEC-ACCEPTED-056, DEC-ACCEPTED-069, DEC-ACCEPTED-136, DEC-ACCEPTED-137, DEC-ACCEPTED-138, DEC-ACCEPTED-140, DEC-ACCEPTED-145, S07, S08, S10, S16, S17, SCH-01, SCH-02, SCH-03, SCH-04, SCH-05, SCH-06, SCH-07, SP-04, SP-05, SP-07, SP-08, TOM-04, TOM-05, TOM-12, VAL-01, VAL-02, VAL-03, VAL-04, VAL-05, VAL-06, VAL-07
- **Readiness**: conditional
- **Owner Decision Required**: pending-spike-result
- **Rationale**: Derived from S18 category 'Mechanism implementation boundaries'. Work domain for later elaboration of the conceptual split between agents, commands, scripts/CLI, validators, deterministic controls, and LLM reasoning boundaries.

### EPIC-BACKLOG-003: Control and evidence infrastructure
- **Source Category**: Control and evidence infrastructure
- **Source Sections**: S02, S09, S10, S11, S17
- **Upstream Refs**: AP-01, AP-04, AP-05, AP-09, CRIT-06, CRIT-07, DEC-ACCEPTED-107, DEC-ACCEPTED-146, RISK-006, RISK-010, S02, S09, S10, S11, S17, SCH-01, SCH-02, SCH-03, SCH-04, SCH-05, SCH-06, SCH-07, SP-09, SP-10, TOM-01, TOM-06, TOM-07, TOM-12, VAL-01, VAL-02, VAL-03, VAL-04, VAL-05, VAL-06, VAL-07
- **Readiness**: candidate
- **Owner Decision Required**: none
- **Rationale**: Derived from S18 category 'Control and evidence infrastructure'. Work domain for later planning around state, logs, evidence capture, evidence lifecycle, storage posture, gate evidence, and auditability.

### EPIC-BACKLOG-004: Source policy and Knowledge Governance
- **Source Category**: Source policy and Knowledge Governance
- **Source Sections**: S01, S02, S03, S12, S16, S17
- **Upstream Refs**: AP-01, AP-06, AP-12, BR-01, BR-02, CRIT-06, CRIT-07, DEC-ACCEPTED-126, DEC-ACCEPTED-148, DEC-ACCEPTED-163, RISK-006, RISK-043, RISK-044, RISK-052, RISK-062, S01, S02, S03, S12, S16, S17, SCH-01, SCH-08, SCH-09, SP-01, SP-03, TOM-01, TOM-08, TOM-13, VAL-01, VAL-09
- **Readiness**: candidate
- **Owner Decision Required**: none
- **Rationale**: Derived from S18 category 'Source policy and Knowledge Governance'. Work domain for preserving source policy minima, Knowledge Gap handling, Curation Request handling, routing of source evidence, and governance of accepted knowledge boundaries.

### EPIC-BACKLOG-005: Odoo 18 pilot environment and module
- **Source Category**: Odoo 18 pilot environment and module
- **Source Sections**: S03, S13, S15, S16, S17
- **Upstream Refs**: AP-07, AP-08, AP-09, BR-01, CRIT-01, CRIT-06, CRIT-07, DEC-ACCEPTED-135, DEC-ACCEPTED-153, DEC-ACCEPTED-162, DEC-ACCEPTED-163, RISK-010, RISK-039, RISK-059, S03, S13, S15, S16, S17, SCH-05, SCH-06, SCH-10, SP-06, SP-10, SPK-S13-DB, SPK-S13-ENV, SPK-S13-EVIDENCE, SPK-S13-RUNNER, SPK-S13-TRACE, SPK-S15-ACCESS, SPK-S15-INSTALL, SPK-S15-TEST, TOM-02, TOM-03, TOM-11, TOM-12, VAL-05, VAL-06, VAL-10
- **Readiness**: conditional
- **Owner Decision Required**: pending-spike-result
- **Rationale**: Derived from S18 category 'Odoo 18 pilot environment and module'. Work domain for later planning around the Odoo-only, Odoo 18 pilot environment and internal requests / simple approvals pilot module boundary.

### EPIC-BACKLOG-006: Security and secrets
- **Source Category**: Security and secrets
- **Source Sections**: S02, S08, S11, S14, S16, S17
- **Upstream Refs**: AP-10, AP-11, AP-12, CRIT-02, CRIT-03, CRIT-04, CRIT-05, DEC-ACCEPTED-045, DEC-ACCEPTED-064, DEC-ACCEPTED-076, DEC-ACCEPTED-092, DEC-ACCEPTED-101, RISK-021, RISK-027, RISK-040, RISK-061, RISK-063, S02, S08, S11, S14, S16, S17, SCH-04, SCH-05, SCH-10, SP-02, SPK-S14-01, SPK-S14-02, SPK-S14-03, SPK-S14-04, TOM-09, TOM-10, VAL-04, VAL-10
- **Readiness**: conditional
- **Owner Decision Required**: pending-spike-result
- **Rationale**: Derived from S18 category 'Security and secrets'. Work domain for later planning around security posture, secrets handling, permissions boundaries, credential exposure risks, and security-related validation needs.

### EPIC-BACKLOG-007: Spike execution and technical validations
- **Source Category**: Spike execution and technical validations
- **Source Sections**: S06, S13, S14, S15, S16, S17
- **Upstream Refs**: AP-11, BR-01, BR-02, CRIT-01, CRIT-02, CRIT-03, CRIT-07, DEC-ACCEPTED-049, DEC-ACCEPTED-050, DEC-ACCEPTED-142, DEC-ACCEPTED-143, DEC-ACCEPTED-149, DEC-ACCEPTED-153, DEC-ACCEPTED-158, DEC-ACCEPTED-164, RISK-059, RISK-061, RISK-063, RISK-065, S06, S13, S14, S15, S16, S17, SP-01, SP-02, SP-03, SP-04, SP-05, SP-06, SP-07, SP-08, SP-09, SP-10, SP-11, SP-12, SP-13, SPK-S13, SPK-S13-DB, SPK-S13-ENV, SPK-S13-EVIDENCE, SPK-S13-RUNNER, SPK-S13-TRACE, SPK-S14, SPK-S14-01, SPK-S14-02, SPK-S14-03, SPK-S14-04, SPK-S15, SPK-S15-ACCESS, SPK-S15-INSTALL, SPK-S15-TEST, TOM-08, TOM-09, TOM-13, TOM-14
- **Readiness**: post-v1
- **Owner Decision Required**: yes
- **Rationale**: Derived from S18 category 'Spike execution and technical validations'. Work domain for later planning around the ordered spike catalogue, open technical uncertainties, and validation dependency families.

### EPIC-BACKLOG-008: Traceability and quality gates
- **Source Category**: Traceability and quality gates
- **Source Sections**: S01, S02, S09, S10, S11, S17
- **Upstream Refs**: AP-01, AP-05, CRIT-06, CRIT-07, RISK-006, RULE-04, RULE-05, S01, S02, S09, S10, S11, S17, SCH-01, SCH-02, SCH-03, SCH-04, SCH-05, SCH-06, SCH-07, TOM-01, TOM-05, TOM-06, TOM-07, TOM-10, VAL-01, VAL-02, VAL-03, VAL-04, VAL-05, VAL-06, VAL-07, VAL-08
- **Readiness**: candidate
- **Owner Decision Required**: none
- **Rationale**: Derived from S18 category 'Traceability and quality gates'. Work domain for preserving bidirectional traceability, acceptance-gate evidence, non-self-closure, validation coverage, and quality-control boundaries.

### EPIC-BACKLOG-009: Owner / governance workflows
- **Source Category**: Owner / governance workflows
- **Source Sections**: S01, S02, S03, S12, S16, S17
- **Upstream Refs**: AP-05, BR-03, BR-04, CRIT-05, DEC-ACCEPTED-059, DEC-ACCEPTED-148, DEC-ACCEPTED-149, DEC-ACCEPTED-157, RISK-004, RISK-005, RISK-013, RULE-01, RULE-02, S01, S02, S03, S12, S16, S17, SCH-03, SCH-04, SP-11, SP-12, SP-13, TOM-07, TOM-10, TOM-13, VAL-03, VAL-04
- **Readiness**: candidate
- **Owner Decision Required**: none
- **Rationale**: Derived from S18 category 'Owner / governance workflows'. Work domain for later planning around owner approvals, blocker registration, conflict handling, deferred/post-V1 owner decisions, and governance handoffs.

## Capabilities

### CAP-BACKLOG-001: OpenCode coordination model specification
- **Epic Parent**: EPIC-BACKLOG-001
- **Source Category**: Runtime / OpenCode coordination setup
- **Upstream Refs**: AP-02, AP-03, AP-04, AP-05, BR-01, BR-02, CRIT-02, CRIT-03, CRIT-07, DEC-ACCEPTED-028, DEC-ACCEPTED-136, DEC-ACCEPTED-137, DEC-ACCEPTED-138, DEC-ACCEPTED-140, RISK-020, RISK-023, RISK-024, RISK-055, S01, S02, S04, S05, S07, S17, SP-04, SP-05, TOM-01, TOM-04, TOM-07
- **Readiness**: candidate
- **Owner Decision Required**: none
- **Rationale**: Specify the OpenCode coordination model preserving AP-02/AP-03/AP-05: OpenCode as primary runtime and coordination hub, not as authoritative state, gate owner, storage, source policy engine, or sufficient evidence by itself.

### CAP-BACKLOG-002: Contract-driven progression discipline
- **Epic Parent**: EPIC-BACKLOG-001
- **Source Category**: Runtime / OpenCode coordination setup
- **Upstream Refs**: AP-02, AP-03, AP-04, AP-05, BR-01, BR-02, CRIT-02, CRIT-03, CRIT-07, DEC-ACCEPTED-028, DEC-ACCEPTED-136, DEC-ACCEPTED-137, DEC-ACCEPTED-138, DEC-ACCEPTED-140, RISK-020, RISK-023, RISK-024, RISK-055, S01, S02, S04, S05, S07, S17, SP-04, SP-05, TOM-01, TOM-04, TOM-07
- **Readiness**: candidate
- **Owner Decision Required**: none
- **Rationale**: Define the contract-driven progression mechanism: section-level contracts, gates, handoffs, and non-self-closure discipline per S05 source-vs-runtime separation.

### CAP-BACKLOG-003: Gate discipline and non-authoritative runtime boundary
- **Epic Parent**: EPIC-BACKLOG-001
- **Source Category**: Runtime / OpenCode coordination setup
- **Upstream Refs**: AP-02, AP-03, AP-04, AP-05, BR-01, BR-02, CRIT-02, CRIT-03, CRIT-07, DEC-ACCEPTED-028, DEC-ACCEPTED-136, DEC-ACCEPTED-137, DEC-ACCEPTED-138, DEC-ACCEPTED-140, RISK-020, RISK-023, RISK-024, RISK-055, S01, S02, S04, S05, S07, S17, SP-04, SP-05, TOM-01, TOM-04, TOM-07
- **Readiness**: candidate
- **Owner Decision Required**: none
- **Rationale**: Bound gate discipline: OpenCode coordinates but does not close gates, approve sections, change owner approval, or replace project-truth/ as source of truth.

### CAP-BACKLOG-004: Agent conceptual elaboration boundaries
- **Epic Parent**: EPIC-BACKLOG-002
- **Source Category**: Mechanism implementation boundaries
- **Upstream Refs**: AP-02, AP-03, AP-04, AP-05, CRIT-03, CRIT-07, DEC-ACCEPTED-056, DEC-ACCEPTED-069, DEC-ACCEPTED-136, DEC-ACCEPTED-137, DEC-ACCEPTED-138, DEC-ACCEPTED-140, DEC-ACCEPTED-145, S07, S08, S10, S16, S17, SCH-01, SCH-02, SCH-03, SCH-04, SCH-05, SCH-06, SCH-07, SP-04, SP-05, SP-07, SP-08, TOM-04, TOM-05, TOM-12, VAL-01, VAL-02, VAL-03, VAL-04, VAL-05, VAL-06, VAL-07
- **Readiness**: candidate
- **Owner Decision Required**: none
- **Rationale**: Describe the conceptual agent split from S08: reasoning/analysis agents that are not executable, not self-verifying, and not self-approving.

### CAP-BACKLOG-005: Command candidate standardisation
- **Epic Parent**: EPIC-BACKLOG-002
- **Source Category**: Mechanism implementation boundaries
- **Upstream Refs**: AP-02, AP-03, AP-04, AP-05, CRIT-03, CRIT-07, DEC-ACCEPTED-056, DEC-ACCEPTED-069, DEC-ACCEPTED-136, DEC-ACCEPTED-137, DEC-ACCEPTED-138, DEC-ACCEPTED-140, DEC-ACCEPTED-145, S07, S08, S10, S16, S17, SCH-01, SCH-02, SCH-03, SCH-04, SCH-05, SCH-06, SCH-07, SP-04, SP-05, SP-07, SP-08, TOM-04, TOM-05, TOM-12, VAL-01, VAL-02, VAL-03, VAL-04, VAL-05, VAL-06, VAL-07
- **Readiness**: conditional
- **Owner Decision Required**: pending-spike-result
- **Rationale**: Define command candidates as repeatable inputs per S08: parameters, expected outputs, and DoR context without creating real commands or permissions. SP-05 remains unresolved.

### CAP-BACKLOG-006: Script/CLI/validator boundary definition
- **Epic Parent**: EPIC-BACKLOG-002
- **Source Category**: Mechanism implementation boundaries
- **Upstream Refs**: AP-02, AP-03, AP-04, AP-05, CRIT-03, CRIT-07, DEC-ACCEPTED-056, DEC-ACCEPTED-069, DEC-ACCEPTED-136, DEC-ACCEPTED-137, DEC-ACCEPTED-138, DEC-ACCEPTED-140, DEC-ACCEPTED-145, S07, S08, S10, S16, S17, SCH-01, SCH-02, SCH-03, SCH-04, SCH-05, SCH-06, SCH-07, SP-04, SP-05, SP-07, SP-08, TOM-04, TOM-05, TOM-12, VAL-01, VAL-02, VAL-03, VAL-04, VAL-05, VAL-06, VAL-07
- **Readiness**: conditional
- **Owner Decision Required**: pending-spike-result
- **Rationale**: Bound the deterministic control boundary for script/CLI/validator candidates per S08 and S10: control structure, traceability, evidence, and source policy. SP-07/SP-08 remain unresolved.

### CAP-BACKLOG-007: LLM reasoning vs deterministic control separation
- **Epic Parent**: EPIC-BACKLOG-002
- **Source Category**: Mechanism implementation boundaries
- **Upstream Refs**: AP-02, AP-03, AP-04, AP-05, CRIT-03, CRIT-07, DEC-ACCEPTED-056, DEC-ACCEPTED-069, DEC-ACCEPTED-136, DEC-ACCEPTED-137, DEC-ACCEPTED-138, DEC-ACCEPTED-140, DEC-ACCEPTED-145, S07, S08, S10, S16, S17, SCH-01, SCH-02, SCH-03, SCH-04, SCH-05, SCH-06, SCH-07, SP-04, SP-05, SP-07, SP-08, TOM-04, TOM-05, TOM-12, VAL-01, VAL-02, VAL-03, VAL-04, VAL-05, VAL-06, VAL-07
- **Readiness**: candidate
- **Owner Decision Required**: none
- **Rationale**: Classify the separation of LLM reasoning from deterministic control per AP-04: agents reason, validators verify, owner approves.

### CAP-BACKLOG-008: State management specification
- **Epic Parent**: EPIC-BACKLOG-003
- **Source Category**: Control and evidence infrastructure
- **Upstream Refs**: AP-01, AP-04, AP-05, AP-09, CRIT-06, CRIT-07, DEC-ACCEPTED-107, DEC-ACCEPTED-146, RISK-006, RISK-010, S02, S09, S10, S11, S17, SCH-01, SCH-02, SCH-03, SCH-04, SCH-05, SCH-06, SCH-07, SP-09, SP-10, TOM-01, TOM-06, TOM-07, TOM-12, VAL-01, VAL-02, VAL-03, VAL-04, VAL-05, VAL-06, VAL-07
- **Readiness**: candidate
- **Owner Decision Required**: none
- **Rationale**: Specify state management per S11/SCH-03/VAL-03: state transitions, status lifecycle, and the L1-L4 authority hierarchy.

### CAP-BACKLOG-009: Logs capture and append-only audit trail
- **Epic Parent**: EPIC-BACKLOG-003
- **Source Category**: Control and evidence infrastructure
- **Upstream Refs**: AP-01, AP-04, AP-05, AP-09, CRIT-06, CRIT-07, DEC-ACCEPTED-107, DEC-ACCEPTED-146, RISK-006, RISK-010, S02, S09, S10, S11, S17, SCH-01, SCH-02, SCH-03, SCH-04, SCH-05, SCH-06, SCH-07, SP-09, SP-10, TOM-01, TOM-06, TOM-07, TOM-12, VAL-01, VAL-02, VAL-03, VAL-04, VAL-05, VAL-06, VAL-07
- **Readiness**: candidate
- **Owner Decision Required**: none
- **Rationale**: Describe append-only logs per S11: state transition logs, gate prerequisite logs, validator result logs, and execution context logs.

### CAP-BACKLOG-010: Evidence lifecycle and storage posture
- **Epic Parent**: EPIC-BACKLOG-003
- **Source Category**: Control and evidence infrastructure
- **Upstream Refs**: AP-01, AP-04, AP-05, AP-09, CRIT-06, CRIT-07, DEC-ACCEPTED-107, DEC-ACCEPTED-146, RISK-006, RISK-010, S02, S09, S10, S11, S17, SCH-01, SCH-02, SCH-03, SCH-04, SCH-05, SCH-06, SCH-07, SP-09, SP-10, TOM-01, TOM-06, TOM-07, TOM-12, VAL-01, VAL-02, VAL-03, VAL-04, VAL-05, VAL-06, VAL-07
- **Readiness**: candidate
- **Owner Decision Required**: none
- **Rationale**: Describe the S11 6-step evidence lifecycle: origin, capture, validation, eligibility evaluation, governed registration, authoritative reference. All storage Git-compatible per AP-09.

### CAP-BACKLOG-011: Gate evidence and auditability boundary
- **Epic Parent**: EPIC-BACKLOG-003
- **Source Category**: Control and evidence infrastructure
- **Upstream Refs**: AP-01, AP-04, AP-05, AP-09, CRIT-06, CRIT-07, DEC-ACCEPTED-107, DEC-ACCEPTED-146, RISK-006, RISK-010, S02, S09, S10, S11, S17, SCH-01, SCH-02, SCH-03, SCH-04, SCH-05, SCH-06, SCH-07, SP-09, SP-10, TOM-01, TOM-06, TOM-07, TOM-12, VAL-01, VAL-02, VAL-03, VAL-04, VAL-05, VAL-06, VAL-07
- **Readiness**: candidate
- **Owner Decision Required**: none
- **Rationale**: Bound gate evidence with storage: VAL-04 gate prerequisite checking, VAL-05 evidence record validation, and governed L2 registration.

### CAP-BACKLOG-012: Source policy minima boundary
- **Epic Parent**: EPIC-BACKLOG-004
- **Source Category**: Source policy and Knowledge Governance
- **Upstream Refs**: AP-01, AP-06, AP-12, BR-01, BR-02, CRIT-06, CRIT-07, DEC-ACCEPTED-126, DEC-ACCEPTED-148, DEC-ACCEPTED-163, RISK-006, RISK-043, RISK-044, RISK-052, RISK-062, S01, S02, S03, S12, S16, S17, SCH-01, SCH-08, SCH-09, SP-01, SP-03, TOM-01, TOM-08, TOM-13, VAL-01, VAL-09
- **Readiness**: candidate
- **Owner Decision Required**: none
- **Rationale**: Bound source policy minima: docs.odoo.com + github.com/odoo/odoo only, per DEC-ACCEPTED-163, AP-06, AP-12. No auto-expansion.

### CAP-BACKLOG-013: Knowledge Gap detection and handling
- **Epic Parent**: EPIC-BACKLOG-004
- **Source Category**: Source policy and Knowledge Governance
- **Upstream Refs**: AP-01, AP-06, AP-12, BR-01, BR-02, CRIT-06, CRIT-07, DEC-ACCEPTED-126, DEC-ACCEPTED-148, DEC-ACCEPTED-163, RISK-006, RISK-043, RISK-044, RISK-052, RISK-062, S01, S02, S03, S12, S16, S17, SCH-01, SCH-08, SCH-09, SP-01, SP-03, TOM-01, TOM-08, TOM-13, VAL-01, VAL-09
- **Readiness**: candidate
- **Owner Decision Required**: none
- **Rationale**: Describe Knowledge Gap mechanism per S12: VAL-01/VAL-09 triggers, gap-open/gap-resolved/gap-discarded states, and owner-gated resolution.

### CAP-BACKLOG-014: Curation Request governance flow
- **Epic Parent**: EPIC-BACKLOG-004
- **Source Category**: Source policy and Knowledge Governance
- **Upstream Refs**: AP-01, AP-06, AP-12, BR-01, BR-02, CRIT-06, CRIT-07, DEC-ACCEPTED-126, DEC-ACCEPTED-148, DEC-ACCEPTED-163, RISK-006, RISK-043, RISK-044, RISK-052, RISK-062, S01, S02, S03, S12, S16, S17, SCH-01, SCH-08, SCH-09, SP-01, SP-03, TOM-01, TOM-08, TOM-13, VAL-01, VAL-09
- **Readiness**: candidate
- **Owner Decision Required**: none
- **Rationale**: Define Curation Request flow per S12: request, owner gate, approve/reject, L1 registration. Only path for source policy expansion.

### CAP-BACKLOG-015: Odoo 18 environment readiness specification
- **Epic Parent**: EPIC-BACKLOG-005
- **Source Category**: Odoo 18 pilot environment and module
- **Upstream Refs**: AP-07, AP-08, AP-09, BR-01, CRIT-01, CRIT-06, CRIT-07, DEC-ACCEPTED-135, DEC-ACCEPTED-153, DEC-ACCEPTED-162, DEC-ACCEPTED-163, RISK-010, RISK-039, RISK-059, S03, S13, S15, S16, S17, SCH-05, SCH-06, SCH-10, SP-06, SP-10, SPK-S13-DB, SPK-S13-ENV, SPK-S13-EVIDENCE, SPK-S13-RUNNER, SPK-S13-TRACE, SPK-S15-ACCESS, SPK-S15-INSTALL, SPK-S15-TEST, TOM-02, TOM-03, TOM-11, TOM-12, VAL-05, VAL-06, VAL-10
- **Readiness**: conditional
- **Owner Decision Required**: pending-spike-result
- **Rationale**: Specify the Odoo 18 execution environment per S13: three logical environment categories (development, validation, authority reference) and seven logical components. Physical form remains spike-dependent.

### CAP-BACKLOG-016: Pilot module candidate boundary definition
- **Epic Parent**: EPIC-BACKLOG-005
- **Source Category**: Odoo 18 pilot environment and module
- **Upstream Refs**: AP-07, AP-08, AP-09, BR-01, CRIT-01, CRIT-06, CRIT-07, DEC-ACCEPTED-135, DEC-ACCEPTED-153, DEC-ACCEPTED-162, DEC-ACCEPTED-163, RISK-010, RISK-039, RISK-059, S03, S13, S15, S16, S17, SCH-05, SCH-06, SCH-10, SP-06, SP-10, SPK-S13-DB, SPK-S13-ENV, SPK-S13-EVIDENCE, SPK-S13-RUNNER, SPK-S13-TRACE, SPK-S15-ACCESS, SPK-S15-INSTALL, SPK-S15-TEST, TOM-02, TOM-03, TOM-11, TOM-12, VAL-05, VAL-06, VAL-10
- **Readiness**: conditional
- **Owner Decision Required**: pending-spike-result
- **Rationale**: Define candidate boundary for the pilot module per S15: InternalRequest, ApprovalRecord, form/list/search views, four-state workflow. No PRD, SDD, or final module.

### CAP-BACKLOG-017: Internal requests / approvals evidence boundary
- **Epic Parent**: EPIC-BACKLOG-005
- **Source Category**: Odoo 18 pilot environment and module
- **Upstream Refs**: AP-07, AP-08, AP-09, BR-01, CRIT-01, CRIT-06, CRIT-07, DEC-ACCEPTED-135, DEC-ACCEPTED-153, DEC-ACCEPTED-162, DEC-ACCEPTED-163, RISK-010, RISK-039, RISK-059, S03, S13, S15, S16, S17, SCH-05, SCH-06, SCH-10, SP-06, SP-10, SPK-S13-DB, SPK-S13-ENV, SPK-S13-EVIDENCE, SPK-S13-RUNNER, SPK-S13-TRACE, SPK-S15-ACCESS, SPK-S15-INSTALL, SPK-S15-TEST, TOM-02, TOM-03, TOM-11, TOM-12, VAL-05, VAL-06, VAL-10
- **Readiness**: candidate
- **Owner Decision Required**: none
- **Rationale**: Bound pilot evidence with the S11 evidence lifecycle: classify Odoo 18 pilot execution evidence as candidate evidence (L3), identify promotion path to governed evidence (L2) on validation.

### CAP-BACKLOG-018: Secrets handling posture specification
- **Epic Parent**: EPIC-BACKLOG-006
- **Source Category**: Security and secrets
- **Upstream Refs**: AP-10, AP-11, AP-12, CRIT-02, CRIT-03, CRIT-04, CRIT-05, DEC-ACCEPTED-045, DEC-ACCEPTED-064, DEC-ACCEPTED-076, DEC-ACCEPTED-092, DEC-ACCEPTED-101, RISK-021, RISK-027, RISK-040, RISK-061, RISK-063, S02, S08, S11, S14, S16, S17, SCH-04, SCH-05, SCH-10, SP-02, SPK-S14-01, SPK-S14-02, SPK-S14-03, SPK-S14-04, TOM-09, TOM-10, VAL-04, VAL-10
- **Readiness**: conditional
- **Owner Decision Required**: pending-spike-result
- **Rationale**: Specify secrets handling posture per S14 CA-1: identify controls to prevent tokens, credentials, and Odoo secrets from entering repo, logs, or evidence. SP-02 remains unresolved.

### CAP-BACKLOG-019: Permissions boundary model specification
- **Epic Parent**: EPIC-BACKLOG-006
- **Source Category**: Security and secrets
- **Upstream Refs**: AP-10, AP-11, AP-12, CRIT-02, CRIT-03, CRIT-04, CRIT-05, DEC-ACCEPTED-045, DEC-ACCEPTED-064, DEC-ACCEPTED-076, DEC-ACCEPTED-092, DEC-ACCEPTED-101, RISK-021, RISK-027, RISK-040, RISK-061, RISK-063, S02, S08, S11, S14, S16, S17, SCH-04, SCH-05, SCH-10, SP-02, SPK-S14-01, SPK-S14-02, SPK-S14-03, SPK-S14-04, TOM-09, TOM-10, VAL-04, VAL-10
- **Readiness**: conditional
- **Owner Decision Required**: pending-spike-result
- **Rationale**: Define the permissions boundary model per S14 CA-2/SP-04: minimum-access, OpenCode permissions that do not convert OpenCode into authority or policy engine.

### CAP-BACKLOG-020: Security/risk triage boundary in gates
- **Epic Parent**: EPIC-BACKLOG-006
- **Source Category**: Security and secrets
- **Upstream Refs**: AP-10, AP-11, AP-12, CRIT-02, CRIT-03, CRIT-04, CRIT-05, DEC-ACCEPTED-045, DEC-ACCEPTED-064, DEC-ACCEPTED-076, DEC-ACCEPTED-092, DEC-ACCEPTED-101, RISK-021, RISK-027, RISK-040, RISK-061, RISK-063, S02, S08, S11, S14, S16, S17, SCH-04, SCH-05, SCH-10, SP-02, SPK-S14-01, SPK-S14-02, SPK-S14-03, SPK-S14-04, TOM-09, TOM-10, VAL-04, VAL-10
- **Readiness**: candidate
- **Owner Decision Required**: none
- **Rationale**: Describe security/risk triage per S14 CA-4: security criteria in gates, risk escalation, and compliance cross-checking.

### CAP-BACKLOG-021: Spike sequencing readiness specification
- **Epic Parent**: EPIC-BACKLOG-007
- **Source Category**: Spike execution and technical validations
- **Upstream Refs**: AP-11, BR-01, BR-02, CRIT-01, CRIT-02, CRIT-03, CRIT-07, DEC-ACCEPTED-049, DEC-ACCEPTED-050, DEC-ACCEPTED-142, DEC-ACCEPTED-143, DEC-ACCEPTED-149, DEC-ACCEPTED-153, DEC-ACCEPTED-158, DEC-ACCEPTED-164, RISK-059, RISK-061, RISK-063, RISK-065, S06, S13, S14, S15, S16, S17, SP-01, SP-02, SP-03, SP-04, SP-05, SP-06, SP-07, SP-08, SP-09, SP-10, SP-11, SP-12, SP-13, SPK-S13, SPK-S13-DB, SPK-S13-ENV, SPK-S13-EVIDENCE, SPK-S13-RUNNER, SPK-S13-TRACE, SPK-S14, SPK-S14-01, SPK-S14-02, SPK-S14-03, SPK-S14-04, SPK-S15, SPK-S15-ACCESS, SPK-S15-INSTALL, SPK-S15-TEST, TOM-08, TOM-09, TOM-13, TOM-14
- **Readiness**: candidate
- **Owner Decision Required**: none
- **Rationale**: Specify spike sequencing readiness per S16: Band A before Band B before Band C with justified dependencies. No spike is executed at this level.

### CAP-BACKLOG-022: Technical validation dependency tracking
- **Epic Parent**: EPIC-BACKLOG-007
- **Source Category**: Spike execution and technical validations
- **Upstream Refs**: AP-11, BR-01, BR-02, CRIT-01, CRIT-02, CRIT-03, CRIT-07, DEC-ACCEPTED-049, DEC-ACCEPTED-050, DEC-ACCEPTED-142, DEC-ACCEPTED-143, DEC-ACCEPTED-149, DEC-ACCEPTED-153, DEC-ACCEPTED-158, DEC-ACCEPTED-164, RISK-059, RISK-061, RISK-063, RISK-065, S06, S13, S14, S15, S16, S17, SP-01, SP-02, SP-03, SP-04, SP-05, SP-06, SP-07, SP-08, SP-09, SP-10, SP-11, SP-12, SP-13, SPK-S13, SPK-S13-DB, SPK-S13-ENV, SPK-S13-EVIDENCE, SPK-S13-RUNNER, SPK-S13-TRACE, SPK-S14, SPK-S14-01, SPK-S14-02, SPK-S14-03, SPK-S14-04, SPK-S15, SPK-S15-ACCESS, SPK-S15-INSTALL, SPK-S15-TEST, TOM-08, TOM-09, TOM-13, TOM-14
- **Readiness**: candidate
- **Owner Decision Required**: none
- **Rationale**: Track technical validation dependencies across S13/S14/S15 spike families: environment, security, and pilot module spike ordering.

### CAP-BACKLOG-023: Open uncertainty tracking (SP-04/SP-05)
- **Epic Parent**: EPIC-BACKLOG-007
- **Source Category**: Spike execution and technical validations
- **Upstream Refs**: AP-11, BR-01, BR-02, CRIT-01, CRIT-02, CRIT-03, CRIT-07, DEC-ACCEPTED-049, DEC-ACCEPTED-050, DEC-ACCEPTED-142, DEC-ACCEPTED-143, DEC-ACCEPTED-149, DEC-ACCEPTED-153, DEC-ACCEPTED-158, DEC-ACCEPTED-164, RISK-059, RISK-061, RISK-063, RISK-065, S06, S13, S14, S15, S16, S17, SP-01, SP-02, SP-03, SP-04, SP-05, SP-06, SP-07, SP-08, SP-09, SP-10, SP-11, SP-12, SP-13, SPK-S13, SPK-S13-DB, SPK-S13-ENV, SPK-S13-EVIDENCE, SPK-S13-RUNNER, SPK-S13-TRACE, SPK-S14, SPK-S14-01, SPK-S14-02, SPK-S14-03, SPK-S14-04, SPK-S15, SPK-S15-ACCESS, SPK-S15-INSTALL, SPK-S15-TEST, TOM-08, TOM-09, TOM-13, TOM-14
- **Readiness**: conditional
- **Owner Decision Required**: pending-spike-result
- **Rationale**: Track open uncertainties SP-04 (OpenCode permissions) and SP-05 (commands/skills design). These remain conditional-open-uncertainty; resolution requires owner decision.

### CAP-BACKLOG-024: Post-V1 gated spike separation (SP-11..SP-13)
- **Epic Parent**: EPIC-BACKLOG-007
- **Source Category**: Spike execution and technical validations
- **Upstream Refs**: AP-11, BR-01, BR-02, CRIT-01, CRIT-02, CRIT-03, CRIT-07, DEC-ACCEPTED-049, DEC-ACCEPTED-050, DEC-ACCEPTED-142, DEC-ACCEPTED-143, DEC-ACCEPTED-149, DEC-ACCEPTED-153, DEC-ACCEPTED-158, DEC-ACCEPTED-164, RISK-059, RISK-061, RISK-063, RISK-065, S06, S13, S14, S15, S16, S17, SP-01, SP-02, SP-03, SP-04, SP-05, SP-06, SP-07, SP-08, SP-09, SP-10, SP-11, SP-12, SP-13, SPK-S13, SPK-S13-DB, SPK-S13-ENV, SPK-S13-EVIDENCE, SPK-S13-RUNNER, SPK-S13-TRACE, SPK-S14, SPK-S14-01, SPK-S14-02, SPK-S14-03, SPK-S14-04, SPK-S15, SPK-S15-ACCESS, SPK-S15-INSTALL, SPK-S15-TEST, TOM-08, TOM-09, TOM-13, TOM-14
- **Readiness**: post-v1
- **Owner Decision Required**: yes
- **Rationale**: Classify Band D / post-V1-gated spikes: SP-11 (SDK/server), SP-12 (OpenAPI/PDF), SP-13 (Frontend/OWL/Playwright). Not V1 core. Activation requires explicit future owner decision.

### CAP-BACKLOG-025: Bidirectional traceability preservation
- **Epic Parent**: EPIC-BACKLOG-008
- **Source Category**: Traceability and quality gates
- **Upstream Refs**: AP-01, AP-05, CRIT-06, CRIT-07, RISK-006, RULE-04, RULE-05, S01, S02, S09, S10, S11, S17, SCH-01, SCH-02, SCH-03, SCH-04, SCH-05, SCH-06, SCH-07, TOM-01, TOM-05, TOM-06, TOM-07, TOM-10, VAL-01, VAL-02, VAL-03, VAL-04, VAL-05, VAL-06, VAL-07, VAL-08
- **Readiness**: candidate
- **Owner Decision Required**: none
- **Rationale**: Describe bidirectional traceability per S17/RULE-05: TOM-to-Blueprint and Blueprint-to-authority links must remain complete without gaps.

### CAP-BACKLOG-026: Acceptance-gate evidence boundary
- **Epic Parent**: EPIC-BACKLOG-008
- **Source Category**: Traceability and quality gates
- **Upstream Refs**: AP-01, AP-05, CRIT-06, CRIT-07, RISK-006, RULE-04, RULE-05, S01, S02, S09, S10, S11, S17, SCH-01, SCH-02, SCH-03, SCH-04, SCH-05, SCH-06, SCH-07, TOM-01, TOM-05, TOM-06, TOM-07, TOM-10, VAL-01, VAL-02, VAL-03, VAL-04, VAL-05, VAL-06, VAL-07, VAL-08
- **Readiness**: candidate
- **Owner Decision Required**: none
- **Rationale**: Bound acceptance-gate evidence: FAC-01..FAC-08 traceability, gate prerequisite checking, and evidence registration for owner review.

### CAP-BACKLOG-027: Non-self-closure and validation coverage tracking
- **Epic Parent**: EPIC-BACKLOG-008
- **Source Category**: Traceability and quality gates
- **Upstream Refs**: AP-01, AP-05, CRIT-06, CRIT-07, RISK-006, RULE-04, RULE-05, S01, S02, S09, S10, S11, S17, SCH-01, SCH-02, SCH-03, SCH-04, SCH-05, SCH-06, SCH-07, TOM-01, TOM-05, TOM-06, TOM-07, TOM-10, VAL-01, VAL-02, VAL-03, VAL-04, VAL-05, VAL-06, VAL-07, VAL-08
- **Readiness**: candidate
- **Owner Decision Required**: none
- **Rationale**: Track non-self-closure: verify that no gate is self-closed, all approvals require explicit owner action, and validation coverage is complete.

### CAP-BACKLOG-028: Owner approval workflow boundary
- **Epic Parent**: EPIC-BACKLOG-009
- **Source Category**: Owner / governance workflows
- **Upstream Refs**: AP-05, BR-03, BR-04, CRIT-05, DEC-ACCEPTED-059, DEC-ACCEPTED-148, DEC-ACCEPTED-149, DEC-ACCEPTED-157, RISK-004, RISK-005, RISK-013, RULE-01, RULE-02, S01, S02, S03, S12, S16, S17, SCH-03, SCH-04, SP-11, SP-12, SP-13, TOM-07, TOM-10, TOM-13, VAL-03, VAL-04
- **Readiness**: candidate
- **Owner Decision Required**: none
- **Rationale**: Define owner approval workflow boundary: owner-gated section approval, iteration closure, and governance state tracking per S01/S02/blueprint-state.yaml.

### CAP-BACKLOG-029: Blocker registration and conflict classification
- **Epic Parent**: EPIC-BACKLOG-009
- **Source Category**: Owner / governance workflows
- **Upstream Refs**: AP-05, BR-03, BR-04, CRIT-05, DEC-ACCEPTED-059, DEC-ACCEPTED-148, DEC-ACCEPTED-149, DEC-ACCEPTED-157, RISK-004, RISK-005, RISK-013, RULE-01, RULE-02, S01, S02, S03, S12, S16, S17, SCH-03, SCH-04, SP-11, SP-12, SP-13, TOM-07, TOM-10, TOM-13, VAL-03, VAL-04
- **Readiness**: candidate
- **Owner Decision Required**: none
- **Rationale**: Classify blocker registration and conflict handling per S01: needs-owner-decision and open-question registration, conflict escalation, and retroactive blocker detection.

### CAP-BACKLOG-030: Deferred/post-V1 owner decision registry
- **Epic Parent**: EPIC-BACKLOG-009
- **Source Category**: Owner / governance workflows
- **Upstream Refs**: AP-05, BR-03, BR-04, CRIT-05, DEC-ACCEPTED-059, DEC-ACCEPTED-148, DEC-ACCEPTED-149, DEC-ACCEPTED-157, RISK-004, RISK-005, RISK-013, RULE-01, RULE-02, S01, S02, S03, S12, S16, S17, SCH-03, SCH-04, SP-11, SP-12, SP-13, TOM-07, TOM-10, TOM-13, VAL-03, VAL-04
- **Readiness**: candidate
- **Owner Decision Required**: yes
- **Rationale**: Track the deferred/post-V1 owner decision registry: identify conditional and post-V1-gated items that require explicit future owner decision before movement into V1 core.

## Generation Rules Applied

- **Rule S18 categories sole source**: Only S18 categories were used as backlog domains
- **Rule S17 traceability attach**: S17 matrix and traceability-map.json attached upstream refs only
- **Rule epics and capabilities only**: No detailed tasks, user stories, or implementation steps generated
- **Rule every item has required fields**: All items include id, type, title, source_category, source_sections, upstream_refs, rationale, boundary, acceptance_criteria, excluded_scope, owner_decision_required, readiness
- **Rule V1/Post-V1 boundary preserved**: Conditional and post-V1 items visibly separated
- **Rule spike-dependent visible**: SP-04/SP-05/SP-11..SP-13 dependencies explicitly annotated
- **Rule no external tooling**: No external project-management tooling introduced
- **Rule no forbidden verbs**: Titles and rationale do not use execution-oriented verbs

## Generated Files

| File | Purpose |
| --- | --- |
| `backlog/backlog-candidates.yaml` | Epics and Capabilities with full field set |
| `backlog/backlog-traceability.yaml` | Candidate-to-source-category mapping |
| `reports/backlog/backlog-generation-report.md` | This report |

