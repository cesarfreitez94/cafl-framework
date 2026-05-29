# S16 Context Packet
dependency_context_summaries_complete: yes
section: S16
title: Spikes and Technical Validations final order
iteration: I5
packet_generated_by: cafl-blueprint-orchestrator
mode: normal
budget: 15000

## Section Objective
Produce the final ordered spike and technical validation list for CAFL V1 with justified dependencies. All spikes must trace to risks, decisions, and earlier section handoffs. No spikes are executed; no validation results are closed. RULE-06: no flat list without dependencies.

## Selected Section Excerpt (Blueprint Placeholder)
Inputs: Iteration 4 approved (✓), S01-S15 approved (✓), S06 Initial Spike Map, applicable risks.
Outputs: final spike order with justified dependencies.
Restrictions: do not execute spikes; do not close validation results; do not produce a flat list.
Acceptance: each spike ordered, justified, connected to dependencies/risks/decisions.

## Dependency Context Summaries (Compact)

**S01 Blueprint Scope**: CRIT-01..07 fixed; TOM approved DEC-ACCEPTED-161; project-truth/ sole authority; CAFL V1 Odoo-only Odoo 18; pilot internal requests/simple approvals DEC-ACCEPTED-162; source policy docs.odoo.com + github.com/odoo/odoo DEC-ACCEPTED-163; SDK/server out V1 DEC-ACCEPTED-164; RAG/vector deferred. Blueprint must not create runtime, agents, commands, schemas, validators, scripts, RAG, backlog, PRD, SDD. framework/ excluded.

**S02 Architecture Principles**: AP-01..AP-12. Key: project-truth/ sole authority (AP-01), hybrid progressive model not agents-only (AP-02), LLM/deterministic separation (AP-04), gate/evidence-driven no self-closure (AP-05), context routing + source policy mandatory (AP-06), Odoo-only Odoo 18 (AP-08), Git-compatible evidence (AP-09), security/secrets cross-cutting (AP-10/11), minimal source policy (AP-12).

**S03 V1/Post-V1 Boundary**: BR-01 V1 core = Odoo-only Odoo 18 hybrid OpenCode pilot. BR-02 conditional/spike areas. Deferred: RAG/vector, SDK/server, broad ingestion, dashboard/UI, CI/CD, multiuser, plugins/MCP, advanced curation.

**S04 Runtime Layout**: 9 conceptual zones (source of truth, OpenCode, repeatable inputs, deterministic controls, state/logs/evidence, source policy, Odoo 18 pilot, security/secrets, spikes). Handoffs to S05/S06 conceptual only.

**S05 Source-vs-Runtime**: project-truth/ = sole authority; OpenCode = runtime coordination only, not authoritative state/gate/storage/policy. V1 boundaries preserved.

**S06 Initial Spike Map**: 13 spikes SP-01..SP-13 in 4 bands:
- Band A (scope/source/security guardrails): SP-01 source policy enforcement, SP-02 secrets posture, SP-03 V1/post-V1 boundary
- Band B (OpenCode/Odoo 18 base): SP-04 OpenCode permissions/capabilities, SP-05 commands/skills design, SP-06 Odoo 18 minimal environment
- Band C (control/evidence toolchain): SP-07 language/toolchain scripts, SP-08 schemas/validators toolchain, SP-09 storage/logs convention, SP-10 evidence capture Odoo 18
- Band D (conditional anti-scope-creep): SP-11 SDK/server, SP-12 OpenAPI/PDF, SP-13 Frontend/OWL/Playwright
Precedence A→B→C; D separated from core. Serves as initial input for S16.

**S07 OpenCode Design**: OpenCode = primary runtime & coordination hub; must not decide approvals, close gates, change state, treat chat as evidence. SP-04/SP-05 preserved as open uncertainties for S16.

**S08 Mechanism Split**: 6 categories (agents, commands, scripts/CLI/validators, rules/config, skills/playbooks, human/owner). SP-04/SP-05 preserved as open uncertainties. Language/toolchain left as future validation.

**S09 Schemas**: SCH-01..SCH-10 logical categories. Conceptual only — no physical schemas, JSON Schema, DDL.

**S10 Validators**: VAL-01..VAL-10 conceptual set, 1:1 with SCH-01..SCH-10. Delivers full VAL set to S16 for spike ordering.

**S11 Storage**: L1-L4 authority hierarchy. 6-step evidence lifecycle. Delivers validator results/alertas to S16 for spike ordering.

**S12 Source Policy**: Operationalizes docs.odoo.com + github.com/odoo/odoo. Knowledge Gap mechanism (VAL-01/VAL-09 triggers). Curation Request flow (owner-gated). Delivers unresolved Knowledge Gaps and pending Curation Requests to S16 as spike inputs.

**S13 Odoo 18 Environment**: 3 environment categories, 7 logical components. 5 spike dependencies for S16: exact environment form (Docker/venv/local), DB compatibility, Odoo 18 test runner, evidence capture for minimum cycle, code source traceability. RISK-059 (critical) positions environment spike as blocking.

**S14 Security**: 4 control areas CA-1..CA-4. 4 spike dependencies for S16: SPK-S14-01 secrets handling, SPK-S14-02 permissions model, SPK-S14-03 security validation approach, SPK-S14-04 compliance assessment. Ordering: SPK-S14-01 blocks SPK-S14-02 and SPK-S14-03; both depend on S13 environment form spike.

**S15 Pilot Module**: conceptual module blueprint (InternalRequest, ApprovalRecord, 4-state workflow). 4 technical spike dependencies + 2 inherited: module installation (depends SPK-S14-01), test execution (depends SPK-S14-02), access model executable (depends SPK-S14-02), code source traceability. RISK-059 positions environment spike as precondition for all module spikes.

## Hard Inherited Constraints
- RULE-06: explicit justified execution order with dependencies; no flat list
- RULE-04: every component traceable to TOM, CRIT, or accepted decision
- RULE-09: no runtime, agents, commands, schemas, validators, scripts, RAG, backlog, PRD, SDD, implementation
- RULE-10: framework/ excluded
- V1 boundaries: Odoo-only, Odoo 18, internal requests/simple approvals pilot
- Source policy minima: docs.odoo.com + github.com/odoo/odoo
- All sources traceable to TOM/CRIT/decisions; no self-resolution of conflicts
- SP-04/SP-05 remain open uncertainties (S06, S07, S08)
- Band D (SP-11..SP-13) must remain conditional/separated from core V1
- SPK-S14-01 blocks SPK-S14-02 and SPK-S14-03 (S14 ordering constraint)
- S13 environment spike is precondition for all module spikes (RISK-059 critical)
- Knowledge Gaps and Curation Requests from S12 are spike inputs; S16 does not close gaps
- No spike is executed; no validation result is closed

## Required Traceability Anchors
- S06: SP-01..SP-13 and band structure A→B→C, D separated
- S13: 5 environment spike dependencies with RISK-059
- S14: SPK-S14-01..SPK-S14-04 with ordering constraints and risk anchors
- S15: 4+2 technical spike dependencies
- S08: SP-04/SP-05 as open uncertainties
- S11: validator results/alerts as spike inputs
- S12: Knowledge Gaps and Curation Requests as spike inputs
- TOM, CRIT-01..07 references
- Applicable decisions: DEC-ACCEPTED-045/059/064/076/092/101/135/136/137/138/140/145/146/149/153/158/162/163/164

## Forbidden Moves / Non-Goals
- Do not execute spikes or close validation results
- Do not produce a flat list without dependencies
- Do not resolve SP-04/SP-05 (they remain open uncertainties)
- Do not close Knowledge Gaps or approve Curation Requests
- Do not create runtime, agents, commands, schemas, validators, scripts, RAG, backlog, PRD, SDD, implementation
- Do not use or reference framework/
- Do not expand V1 scope, source policy, or pilot definition
- Do not re-open CRIT-01..07 or TOM
- Do not approve, close, or change owner_approval status

## Acceptance Checklist
- [ ] Each spike ordered, justified, connected to dependencies/risks/decisions
- [ ] SP-01..SP-13 incorporated with band structure A→B→C preserved, D separated
- [ ] S13 5 environment spike dependencies integrated with RISK-059 priority
- [ ] S14 4 security spikes (SPK-S14-01..04) integrated with ordering constraints
- [ ] S15 4+2 technical spike dependencies integrated
- [ ] SP-04/SP-05 preserved as open uncertainties
- [ ] SPK-S14-01 blocks SPK-S14-02 and SPK-S14-03 respected
- [ ] S13 environment spike = precondition for pilot module spikes
- [ ] Knowledge Gaps and Curation Requests included as potential spike inputs
- [ ] No flat list; RULE-06 satisfied
- [ ] V1 boundaries, source policy, framework/ exclusion preserved
- [ ] No forbidden artifacts created

## Fallback-To-Strict Triggers
- Packet cannot prove required traceability → strict
- Packet conflicts with section content or operational state → strict
- Owner-decision blocker appears → strict
- Author introduces claims not covered by packet → strict
- Section requires governance rule changes → strict
