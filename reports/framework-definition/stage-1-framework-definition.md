# Stage 1: Current Framework Definition Extraction

**Status:** proposed  
**Scope:** Factual extraction of the current CAFL V1 framework definition from existing repo evidence.  
**Authority:** Derived, non-authoritative until approved. Does not replace `project-truth/`.  
**Stage:** 1 of the Framework Definition & Alignment Review. Stage 2 (owner alignment) is out of scope here.

---

## 1. Status And Scope

This document extracts the current definition of the CAFL V1 framework exclusively from approved and generated repository evidence. It does not:
- Evaluate owner alignment.
- Create a roadmap.
- Triage or classify the backlog.
- Create a spike execution plan.
- Produce executable work packages.
- Promote findings into rules, gates, or spikes.
- Authorize implementation.
- Modify any existing file.

---

## 2. Source Hierarchy

Authoritative sources in descending priority:

| Priority | Source | Role |
| --- | --- | --- |
| 1 | `project-truth/decisions/accepted.md` | All approved decisions (DEC-ACCEPTED-001 through DEC-ACCEPTED-164) |
| 2 | `project-truth/TOM.md` | Target Operating Model, owner-approved 2026-05-27 |
| 3 | `project-truth/decisions/rejected.md` | Explicitly rejected decisions (boundary enforcement) |
| 4 | `project-truth/decisions/superseded.md` | Superseded decisions (historical reference) |
| 5 | `project-truth/critical-map.md` | CRIT-01..CRIT-07 session map |
| 6 | `project-truth/decisions/pending.md` | Pending work items, not yet approved |
| 7 | `project-truth/risks.md` | Risk catalogue (supporting) |

Supporting sources:

| Source | Role |
| --- | --- |
| `project-truth/glossary.md` | Terminology definitions |
| `project-truth/implementation-blueprint.md` | Blueprint content (19 sections, all closed/approved) |
| `project-truth/blueprint-state.yaml` | Operational Blueprint state |
| `project-truth/blueprint-contract.yaml` | Blueprint agent governance contract |
| `reports/blueprint/deterministic-verification-report.md` | Verification results |
| `backlog/backlog-candidates.yaml` | Generated backlog candidates |
| `backlog/backlog-traceability.yaml` | Candidate-to-source mapping |
| `backlog/backlog-contract.yaml` | Backlog generation contract |
| `reports/backlog/backlog-generation-report.md` | Generation report |
| `reports/backlog/backlog-verification-report.md` | Verification report |
| `generated/blueprint/blueprint-index.json` | Machine-readable section index |

Context-only sources (proposed, not authority):

| Source | Role |
| --- | --- |
| `reports/findings/post-blueprint-findings-register.md` | 15 proposed operational learnings |
| `reports/findings/post-blueprint-findings-executive-summary.md` | Summary of proposed findings |

Explicitly excluded as authority:

| Area | Reason |
| --- | --- |
| `framework/` | Discarded as contaminated input (CRIT-07, DEC-ACCEPTED-133). Not present in repo. |
| Root `README.md` | Status mirror only; `project-truth/` wins on conflict. |
| `.opencode/` | Blueprint automation governance evidence only, not final CAFL agents/commands. |
| `docs/coordination/` | Coordination reference only, not source of truth. |

---

## 3. Compact Framework Definition

CAFL is an **operational framework/platform on OpenCode** for developing **enterprise Odoo solutions** with AI assistance throughout the development lifecycle.

- **Domain:** Odoo-only for V1.
- **Target version:** Odoo 18.
- **Runtime principal:** OpenCode.
- **Operating model:** Hybrid progressive (agents + commands + scripts/CLI/validators + rules/config + skills/playbooks). V1 is not agents-only and cannot be purely manual or narrative.
- **Pilot:** Internal requests / simple approvals. Confirmed by owner (DEC-ACCEPTED-162). Closed selection.
- **V1 goal:** Demonstrate an end-to-end verifiable flow from owner idea to an Odoo 18 module technically ready for production.
- **Readiness definition:** Functional, installable/loadable in Odoo, tested, documented, secure within scope, auditable, reviewable, with sufficient evidence. Does not mean deployed on a production server.
- **Planning horizon:** 2 months as a scope constraint.

_Source: DEC-ACCEPTED-013 through DEC-ACCEPTED-033, TOM Alcance Operativo V1._

---

## 4. Problem Statement

Enable a **single owner** to operate with capabilities equivalent to a **specialized engineering team** for building enterprise Odoo solutions. The owner operates as a single-worker enterprise and CAFL should close the gap between a solo owner and a full team.

_Source: DEC-ACCEPTED-014._

---

## 5. Intended User

The **initial user** of CAFL is the **owner**. V1 is not defined for external clients, external teams, or external developers.

_Source: DEC-ACCEPTED-015._

---

## 6. Owner Role

| Aspect | Detail |
| --- | --- |
| Mechanism | Exclusively human for critical decisions |
| Responsibilities | Define intent, respond to critical decisions, approve scope changes, significant exceptions, significant debt, deadline-driven reductions, and final module acceptance |
| Limits | Does not micro-manage normal tasks, does not replace QA, gates, or evidence |
| Approvals required for | Scope change, unresolvable critical context lack, legal/compliance critical risk, normative contradiction, high security/data risk, irreversible architectural decision, testing/DoD exception, repeated rework beyond limit, final module acceptance, deadline-based scope reduction |

_Sources: DEC-ACCEPTED-019, DEC-ACCEPTED-059, TOM Roles Y Capacidades._

---

## 7. Agent And Mechanism Roles

### 7.1 Agents (LLM-assisted reasoning)

| Aspect | Detail |
| --- | --- |
| Suitable for | Judgment, reasoning, analysis, design, generation, diagnosis, review, drafting |
| Responsibilities | Functional analysis (PRD), Odoo technical design (SDD), backend construction, QA planning/diagnosis, risk review, documentation drafting |
| Limits | Cannot approve gates, cannot self-close, cannot convert narrative into authoritative state, cannot replace deterministic evidence |

### 7.2 Orchestration

| Aspect | Detail |
| --- | --- |
| Mechanism | Mixed (assisted + future deterministic control) |
| Responsibilities | Coordinate flow, handoffs, conceptual state, manage blocking/rework/escalation, decide normal gates based on evidence |
| Limits | Cannot convert LLM narrative into real state, cannot decide critical decisions or final module closure |

### 7.3 Deterministic Controls

| Aspect | Detail |
| --- | --- |
| Mechanism | Scripts/CLI/validators candidates, rules/config, skills/playbooks |
| Expected V1 scope | Structural validation of packets/contracts/gates/evidence, DoR checks, minimum traceability, logs/state/evidence recording, Odoo 18 install/update/test execution, evidence capture, source policy/Knowledge Gap basics |
| Limits | Do not replace technical judgment, gate decision, or owner acceptance |

### 7.4 Mechanism Split (from Blueprint S08)

| Mechanism | Responsibility | Constraints |
| --- | --- | --- |
| Conceptual agents | Reasoning, analysis, design, generation, review | Not executable, not self-closing, not self-approving |
| Command candidates | Repeatable inputs to structure phases/tasks | Not real commands, not final gate authority |
| Script/CLI/validator candidates | Deterministic structural validation and evidence capture | Not implemented; language/toolchain spike-dependent |
| Rules/config | Minimum invariants | Conceptual only |
| Skills/playbooks | On-demand operational knowledge | Conceptual only |
| Human/owner | Critical decisions and gate closure | Exclusively human; no agent delegation |

_Sources: DEC-ACCEPTED-055 through DEC-ACCEPTED-069, TOM Matriz Operativa De Capacidades, Blueprint S08._

---

## 8. Contract Role

Contracts are **formal internal agreements** between phases, responsibilities, mechanisms, or artifacts. They define:

- Producer, consumer, validator
- Inputs, outputs, context, token budget
- Sufficiency criteria, rejection criteria
- Evidence, blockers (`none` declared if absent)
- Handoff, version, traceability

**Always-required contracts (9):** Base Contract Envelope, Idea → PRD, PRD → SDD, SDD → Task/Context Packet, Task/Context Packet + DoR, Task Execution, QA/Testing, Evidence/Closure, Context Routing / Token Budget.

**Conditional-required contracts (4):** Security/Risk/Compliance Review, Rework, Escalation/Owner Decision, Mechanism Execution Profile.

Consumer may reject insufficient contracts. Producer cannot self-approve DoR.

_Sources: CRIT-04, DEC-ACCEPTED-072 through DEC-ACCEPTED-087._

---

## 9. Gates, Evidence, State, And Traceability

### 9.1 Gates

**6 independent gates:** PRD Sufficiency, SDD Sufficiency, Task Packet/DoR, QA/Testing, Evidence/Closure, Module Technical Readiness.

**2 transversal checks** (always applied within gates): Context Routing / Token Budget, Security/Risk/Compliance Triage.

**3 conditional gates:** Security/Data/Access, Debt Acceptance, Rework Limit.

Severities: `blocker`, `critical`, `high`, `medium`, `low`, `warning/info`.
Actions: `continue`, `continue with warning`, `rework`, `block`, `escalate to owner`, `reject/stop`, `accept technical debt`, `replan/reduce scope`.

Gate recommendation, verification, and decision are separated. Orchestration decides normal gates; owner decides critical decisions and final module closure. Rework is bounded to 2 cycles per task under the same scope; third significant cycle escalates.

_Sources: CRIT-05, DEC-ACCEPTED-090 through DEC-ACCEPTED-105._

### 9.2 Evidence

Evidence must be **reproducible**. LLM narrative alone is not sufficient evidence. Minimum V1 evidence includes traceable PRD/SDD, contract/packet registry, context/source usage logs, gate logs, evidence logs, rework history, debt log, and approval log.

_Sources: DEC-ACCEPTED-100, DEC-ACCEPTED-115, TOM Evidencia Minima Del Piloto._

### 9.3 State

Authoritative state lives in **traceable, versionable, logical records**. LLM narrative is never authoritative state.

**L1-L4 authority hierarchy:**
- **L1:** `project-truth/` — authoritative governed records
- **L2:** Governed registered evidence
- **L3:** Candidate evidence
- **L4:** Ephemeral

**9 always-required logs:** State/Status Change Log, Decision Log, Contract/Packet Registry, Gate Log, Evidence Log, Source Registry/Source Log, Context Log, Rework History, Approval Log.

**7 conditional logs:** Source Snapshot Log, Source Usage Log, Excluded/Prohibited Context Log, Token/Context Usage Log, Debt Log, Knowledge Registry Log, Integration Source Log.

Storage direction: simple, auditable, Git-compatible (Markdown, JSON/YAML, JSONL append-only).

_Sources: CRIT-06, DEC-ACCEPTED-107 through DEC-ACCEPTED-118, DEC-ACCEPTED-146._

### 9.4 Traceability

**Bidirectional:** TOM requirement → Blueprint component, and Blueprint component → TOM requirement.

Control unit hierarchy: `module → capability/feature → task`.
Required paths: `contract → gate → evidence`, `module → capability/feature → task`, TOM anchors → Blueprint components → backlog categories.

12 always-required IDs and 12 conditional IDs defined in DEC-ACCEPTED-109 and DEC-ACCEPTED-110.

_Sources: DEC-ACCEPTED-109 through DEC-ACCEPTED-114, RULE-04, RULE-05._

---

## 10. Knowledge Governance

| Aspect | Detail |
| --- | --- |
| Mode | Minimum by default in V1 |
| Pre-authorized sources | `docs.odoo.com` + `github.com/odoo/odoo` (DEC-ACCEPTED-163) |
| Expansion path | Curation Request → owner gate → approve/reject → L1 registration |
| Knowledge Gap | Blocks implementation until sufficient authorized source/artifact exists |
| Curation Mode | Activated by Knowledge Gap; requires owner approval or prior source policy |
| Prohibited | Free web search, Wikipedia, unauthorized blogs, StackOverflow as authority, copying unvalidated third-party solutions |
| Deferred from V1 | RAG / vector base, broad automated documentation ingestion |

_Sources: DEC-ACCEPTED-163, DEC-ACCEPTED-126 through DEC-ACCEPTED-129, DEC-ACCEPTED-148, DEC-ACCEPTED-150._

---

## 11. Expected Operating Flow

```
Idea intake → PRD light → PRD Sufficiency Gate
  → SDD light → SDD Sufficiency Gate
  → Capabilities/tasks + task/context packets → Task Packet / DoR Gate
  → Task execution → QA/Testing Gate
  → Evidence/Closure Gate → Module Technical Readiness Gate
  + Controlled rework (max 2 cycles)
  + Knowledge governance transversal
```

**Invariants:**
- PRD and SDD are mandatory in light version.
- No unit starts without task/context packet + DoR.
- Context routing and token budget are mandatory per contract/packet.
- Gate recommendation, verification, and decision are separated.
- Owner decides critical decisions and final module closure.

Each of the 13 phases has a defined executor, validator, output, blocking condition, advance condition, evidence minimum, and handoff.

_Sources: CRIT-02, TOM Flujo Operativo Punta A Punta._

---

## 12. Designed Theory

### 12.1 Target Operating Model (approved)
- **Status:** Owner-approved 2026-05-27 (DEC-ACCEPTED-161).
- **Content:** Complete operational model: roles/capabilities, 13-phase flow, control/blocking matrix, evidence model, knowledge governance, pilot instantiation, Blueprint handoff.

### 12.2 Implementation Blueprint (closed)
- **Status:** 5 iterations, 19 sections, all closed/approved.
- **Iteration 1 (I1):** S01-S06 — Architectural framework: scope, principles, V1/post-V1 boundary, runtime layout candidate, source-vs-runtime structure, initial spike map.
- **Iteration 2 (I2):** S07-S08 — Operational mechanism design: OpenCode operating design, mechanism split.
- **Iteration 3 (I3):** S09-S12 — Technical control artifacts: 10 minimum schemas, 10 minimum validators, state/logs/evidence storage, source policy/KB implementation.
- **Iteration 4 (I4):** S13-S15 — Odoo execution and pilot: Odoo 18 environment, security/secrets, pilot module blueprint.
- **Iteration 5 (I5):** S16-S19 — Blueprint closure: final spike order, bidirectional traceability matrix, outputs to backlog, acceptance criteria.
- **Architecture principles:** 12 (AP-01 through AP-12).
- **Boundary rules:** 4 (BR-01 through BR-04).
- **Conceptual schemas:** 10 (SCH-01 through SCH-10).
- **Conceptual validators:** 10 (VAL-01 through VAL-10).
- **Spikes catalogued:** 13 primary spikes (SP-01 through SP-13), plus additional section-specific spike families for environment, security, and pilot validation where applicable.
- **Pilot logical models:** InternalRequest, ApprovalRecord with 4-state workflow (draft → submitted → approved/rejected).
- **Traceability:** 233 unique references across all sections.

---

## 13. Generated Artifacts

| Artifact | File |
| --- | --- |
| Blueprint section index | `generated/blueprint/blueprint-index.json` |
| State consistency check | `generated/blueprint/state-check.json` |
| Rule compliance check | `generated/blueprint/rule-check.json` |
| Traceability reference map | `generated/blueprint/traceability-map.json` |
| Backlog candidates (9 epics, 30 capabilities) | `backlog/backlog-candidates.yaml` |
| Backlog traceability | `backlog/backlog-traceability.yaml` |

Total backlog items: 39
Epics: 9
Capabilities: 30
Readiness distribution across total backlog items:
  - candidate: 27
  - conditional: 10
  - post-V1: 2

---

## 14. Validated Artifacts

### Blueprint deterministic verification: PASS
- State check: 53 checks passed, 0 findings.
- Rule check: 5 checks passed, 0 findings.
- Traceability index: PASS.
- Section index: PASS.

### Backlog verification: PASS
- Contract checks: 9 passed.
- Candidate checks: 46 passed (all IDs valid, all required fields present, no forbidden verbs).
- Traceability checks: 3 passed.

---

## 15. Pending Areas

| Area | Status |
| --- | --- |
| Roadmap | Not started |
| Backlog triage | Not started |
| Spike execution | Not started (13 primary spikes SP-01..SP-13, plus section-specific spike families for environment, security, and pilot validation where applicable, catalogued but not executed) |
| Work-package generation | Not demonstrated (backlog candidates are conceptual only) |
| Implementation | Not authorized |
| Findings review | 15 proposed findings in `reports/findings/` require owner review |

The post-Blueprint findings register is proposed only and contains 4 critical, 8 high, and 3 medium severity findings. It does not modify Blueprint content or authorize execution.

---

## 16. Explicitly Not Authorized

The following are **explicitly not authorized** by the current approved theory:

| Category | Not Authorized |
| --- | --- |
| Runtime | Creating runtime skeleton, installing Odoo 18, executing pilot |
| Agents/commands | Final executable agents, real commands, final prompts, permissions config |
| Schemas/validators/scripts | Physical schemas, real validators, executable scripts, language choice |
| RAG/vector | RAG infrastructure, vector database, automated ingestion |
| SDK/server | As V1 core (DEC-ACCEPTED-164) |
| Pilot deliverables | Final PRD, final SDD, executed pilot module |
| Planning | Detailed technical backlog, CI/CD pipeline, dashboard/UI |
| Governance | Reopening CRIT-01..CRIT-07, TOM, or accepted decisions |
| Repository | Using `framework/` as input, recreating `framework/`, committing, pushing |
| Scope | Expanding source policy, adding integrations, making V1 multi-user |

---

## 17. Theoretical Implemented Behavior

If implemented from the current definition, the framework would:

1. Accept a brief owner idea for an Odoo 18 module.
2. Elicit scope, actors, rules, and acceptance criteria into a light PRD.
3. Gate the PRD through PRD Sufficiency Gate with evidence.
4. Translate the approved PRD into a light SDD with Odoo-specific design.
5. Gate the SDD through SDD Sufficiency Gate.
6. Decompose the module into capabilities and verifiable tasks.
7. Produce task/context packets with DoR validated by the consumer.
8. Use OpenCode to coordinate agent-based construction of backend, views, security, and data.
9. Verify outputs through QA/Testing Gate with reproducible evidence.
10. Consolidate evidence per task through Evidence/Closure Gate.
11. Validate aggregated evidence, tests, and pilot execution through Module Technical Readiness Gate.
12. Require owner acceptance for final module readiness.
13. Enforce source policy, block on Knowledge Gaps, gate Curation Requests through owner approval.
14. Log all state, decisions, evidence, gates, sources, rework, and approvals in Git-compatible append-only records.
15. Bound rework to 2 cycles per task; escalate third cycles.
16. Resolve 13 primary spikes (SP-01..SP-13) plus additional section-specific spike families where applicable before committing to physical implementations.
17. Keep SDK/server, RAG/vector base, dashboard/UI, CI/CD, and broad integrations as post-V1.

---

## 18. Non-Authoritative Areas

These repo areas should not be treated as framework authority during Stage 1 or subsequent work:

- `framework/` — absent, explicitly discarded (CRIT-07, DEC-ACCEPTED-133).
- Root `README.md` — status mirror only.
- `.opencode/` — Blueprint automation governance evidence only, not final CAFL agents/commands/skills.
- `docs/coordination/` — coordination reference only.
- `reports/findings/` — proposed findings; do not promote into rules/gates/spikes without owner review.
- `backlog/` — generated candidates only, not executable backlog or implementation authorization.
- `generated/blueprint/` — derived deterministic artifacts only.

---

## 19. Extraction Risks

| Risk | Mitigation |
| --- | --- |
| Treating proposed findings as approved rules | Findings remain `proposed`; Stage 1 extracts definition, not findings |
| Turning backlog candidates into executable tasks | Candidates are conceptual only; Stage 1 does not decompose |
| Treating Blueprint design as implemented runtime | All design is conceptual; Stage 1 notes what is designed vs. implemented |
| Overweighting `.opencode/` Blueprint agents as final CAFL agents | Noted as governance evidence only |
| Creating a parallel source of truth outside `project-truth/` | This document is `proposed` and derived; authority remains with `project-truth/` |

---

## 20. Source References

| Source File | Lines/Scope Used |
| --- | --- |
| `project-truth/README.md` | Full |
| `project-truth/critical-map.md` | Full |
| `project-truth/TOM.md` | Full (470 lines) |
| `project-truth/decisions/accepted.md` | Full (170 lines) |
| `project-truth/decisions/pending.md` | Full |
| `project-truth/decisions/rejected.md` | Full |
| `project-truth/decisions/superseded.md` | Full |
| `project-truth/risks.md` | Full |
| `project-truth/glossary.md` | Full |
| `project-truth/implementation-blueprint.md` | S01-S19 (sampled via blueprint-state.yaml summaries + section index) |
| `project-truth/blueprint-state.yaml` | Full |
| `project-truth/blueprint-contract.yaml` | Full |
| `reports/blueprint/deterministic-verification-report.md` | Full |
| `reports/backlog/backlog-generation-report.md` | Full |
| `reports/backlog/backlog-verification-report.md` | Full |
| `backlog/backlog-candidates.yaml` | Full |
| `backlog/backlog-traceability.yaml` | Full |
| `backlog/backlog-contract.yaml` | Full |
| `generated/blueprint/blueprint-index.json` | Full |
| `reports/findings/post-blueprint-findings-register.md` | Full (context only) |
| `reports/findings/post-blueprint-findings-executive-summary.md` | Full (context only) |
| `docs/coordination/blueprint-automation-loop.md` | Full (governance reference only) |
| `.opencode/agents/cafl-blueprint-orchestrator.md` | Full (governance reference only) |
| `.opencode/commands/blueprint-next.md` | Full (governance reference only) |
| Root `README.md` | Full (status mirror only) |
