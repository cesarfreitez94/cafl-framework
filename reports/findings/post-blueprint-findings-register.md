# Post-Blueprint Findings Register

**Status:** `proposed`  
**Scope:** Post-Blueprint operational learnings only. Does not authorize execution, roadmap creation, backlog triage, spike planning, or work-package generation.  
**Source:** Deterministic verification of `project-truth/implementation-blueprint.md`, backlog candidate generation (`reports/backlog/`), and orchestration observations during author-verifier-re-verifier flows.  
**Authority:** Derived from `project-truth/`; not a competing source of truth.  

---

## Register Metadata

| Field | Value |
| --- | --- |
| Register ID | FND-POSTBP-REG-001 |
| Created | 2026-05-31 |
| Total findings | 15 |
| Classification distribution | RULE: 8, GATE: 2, SCOPE_CHANGE_RISK: 2, ROADMAP_IMPACT: 1, BACKLOG_IMPACT: 2 |
| Spike candidate distribution | yes: 4, no: 11 |
| Severity distribution | critical: 4, high: 8, medium: 3 |
| V1 scope impact | yes: 8, no: 7 |

---

## Findings

---

### FND-POSTBP-01: Excessive broad repository reading by agents

| Field | Value |
| --- | --- |
| **id** | FND-POSTBP-01 |
| **title** | Excessive broad repository reading by agents |
| **source_context** | Observed during deterministic verification and backlog generation tooling: agents loaded full directory listings, recursive file reads, and unbounded globs even when the task scope was narrow (e.g., a single section or contract field). CRIT-02 and CRIT-04 explicitly prohibit reading the entire repo by default, yet the behavior persists because enforcement is prompt-based, not structural. |
| **description** | Agents routinely read far more repository content than their current task contract authorizes. This includes recursive directory listings, broad globs (`**/*.md`), and reading files that are outside the declared context routing for the current task. The behavior is driven by a "gather all context just in case" heuristic rather than by structured context routing. |
| **why_it_matters** | Every unauthorized read consumes tokens, increases latency, raises cost, and contaminates the agent's reasoning with documents that may be draft, outdated, or outside the current task's authority. It directly undermines the CRIT-02/CRIT-04 context-routing and token-budget contracts. |
| **impact_area** | token_usage, cost, execution, quality |
| **classification** | RULE |
| **recommended_action** | Establish a RULE that every agent task must begin with an explicit context-routing declaration: list the exact files/sections authorized, the budget class, and the justification. Violation must be treated as a contract breach, not a minor inefficiency. |
| **creates_spike** | no |
| **spike_candidate** | no |
| **affects_roadmap** | no |
| **affects_backlog** | no |
| **affects_v1_scope** | no |
| **severity** | high |
| **status** | proposed |

---

### FND-POSTBP-02: Weak orchestration for long multi-step flows

| Field | Value |
| --- | --- |
| **id** | FND-POSTBP-02 |
| **title** | Weak orchestration for long multi-step flows |
| **source_context** | Observed during Blueprint section authoring (S01-S19) and deterministic verification: the author-verifier-re-verifier sequence was coordinated manually via prompt instructions and AGENTS.md conventions, not by a structured orchestration contract. State transitions (e.g., "author done → verifier starts") were inferred rather than explicitly registered. |
| **description** | Multi-step flows (author → verifier → fix → re-verifier → owner approval) lack a structured orchestration contract. There is no machine-readable or even human-readable state machine that governs who acts when, what evidence is required to transition, and what happens on timeout or failure. The flow depends on prompt obedience and human (owner/ChatGPT) coordination. |
| **why_it_matters** | Without structured orchestration, long flows are fragile: steps can be skipped, evidence can be lost, responsibilities can blur, and the owner becomes an implicit runtime. This contradicts CRIT-03's approved mixed-responsibility model and CRIT-05's gate-separation model. |
| **impact_area** | governance, execution, autonomy, quality |
| **classification** | RULE |
| **recommended_action** | Establish a RULE that every multi-step flow must have an explicit orchestration contract: states, transitions, evidence requirements per transition, timeout/escalation rules, and a designated coordinator mechanism (not the owner by default). |
| **creates_spike** | no |
| **spike_candidate** | yes |
| **affects_roadmap** | no |
| **affects_backlog** | no |
| **affects_v1_scope** | no |
| **severity** | high |
| **status** | proposed |

---

### FND-POSTBP-03: High token/cost load from author → verifier → re-verifier flows

| Field | Value |
| --- | --- |
| **id** | FND-POSTBP-03 |
| **title** | High token/cost load from author → verifier → re-verifier flows |
| **source_context** | Observed during Blueprint section verification: each section required a full-context author report, a full-context verification report, and often a fix report plus re-verification report. The verifier and re-verifier re-read the entire section and its context packet from scratch rather than working from a bounded diff or incremental evidence. |
| **description** | The current verification pipeline is expensive by design: every verifier instance reloads the full context of the artifact being verified. There is no incremental verification model (e.g., "verify only what changed since last state"). For a 19-section Blueprint, this multiplied token consumption by approximately 3-4x per section. |
| **why_it_matters** | High token load makes the framework economically unsustainable at scale and creates a perverse incentive to skip verification or use cheaper (weaker) models for verification, which degrades quality. CRIT-04's token-budget contract is ignored because there is no enforcement. |
| **impact_area** | token_usage, cost, execution, quality |
| **classification** | RULE |
| **recommended_action** | Establish a RULE that verification must be incremental where possible: verifiers must state what changed, what they are checking, and why full re-read is necessary. Introduce a token-budget class for verification flows and require justification for budget-class escalation. |
| **creates_spike** | no |
| **spike_candidate** | no |
| **affects_roadmap** | no |
| **affects_backlog** | no |
| **affects_v1_scope** | no |
| **severity** | high |
| **status** | proposed |

---

### FND-POSTBP-04: Missing mature minimum context packet model per task type

| Field | Value |
| --- | --- |
| **id** | FND-POSTBP-04 |
| **title** | Missing mature minimum context packet model per task type |
| **source_context** | Observed during Blueprint authoring and backlog generation: while CRIT-04 defines a conceptual task/context packet, there is no mature, task-type-specific packet template. For example, a "schema design" task, a "validator script" task, and a "gate review" task all use the same generic packet structure, leading to omitted fields and inferred context. |
| **description** | The task/context packet exists conceptually (CRIT-04) but lacks mature templates tailored to task types. Different task types (design, review, implementation, verification, spike) have different context needs, but the current packet model is one-size-fits-all. Agents therefore omit or infer packet contents based on task type. |
| **why_it_matters** | Incomplete packets cause Definition-of-Ready failures, rework, and context gaps. If the packet model does not mature before V1 execution begins, every task will start with inferred or incomplete context, violating CRIT-04's sufficiency criteria. |
| **impact_area** | execution, quality, backlog |
| **classification** | RULE |
| **recommended_action** | Establish a RULE that every task type must have a minimum context packet template with mandatory and conditional fields declared explicitly. The template must be versioned and treated as a contract in its own right. |
| **creates_spike** | no |
| **spike_candidate** | yes |
| **affects_roadmap** | no |
| **affects_backlog** | yes |
| **affects_v1_scope** | no |
| **severity** | medium |
| **status** | proposed |

---

### FND-POSTBP-05: Agents infer hidden fallbacks or "help too much" when contracts are incomplete

| Field | Value |
| --- | --- |
| **id** | FND-POSTBP-05 |
| **title** | Agents infer hidden fallbacks or "help too much" when contracts are incomplete |
| **source_context** | Observed repeatedly during Blueprint authoring and backlog generation: when a contract or packet omitted a required field (e.g., blockers, token budget, output format), agents did not block or escalate. Instead, they invented reasonable defaults, guessed the owner's intent, or completed the missing information from general knowledge. |
| **description** | When contracts are incomplete, agents default to "being helpful" rather than enforcing contract completeness. This manifests as: invented blockers (`none` assumed rather than declared), guessed token budgets, inferred output formats, and synthesized context from general knowledge rather than approved sources. The behavior is a hidden fallback that violates CRIT-04's consumer-may-reject principle and CRIT-06's Knowledge Gap blocking rule. |
| **why_it_matters** | Hidden fallbacks create false confidence. The owner believes the framework is operating from approved sources, but the agent is actually improvising. This undermines traceability, reproducibility, and the authority of `project-truth/`. |
| **impact_area** | governance, quality, autonomy |
| **classification** | RULE |
| **recommended_action** | Establish a RULE that any incomplete contract or packet must trigger an explicit block or escalation, not a hidden fallback. Agents must state what is missing, request completion, and refuse to proceed until the contract is whole. This behavior must be enforced by deterministic checks where possible. |
| **creates_spike** | no |
| **spike_candidate** | no |
| **affects_roadmap** | no |
| **affects_backlog** | no |
| **affects_v1_scope** | no |
| **severity** | high |
| **status** | proposed |

---

### FND-POSTBP-06: Risk of the framework becoming a documentation factory instead of an execution framework

| Field | Value |
| --- | --- |
| **id** | FND-POSTBP-06 |
| **title** | Risk of the framework becoming a documentation factory instead of an execution framework |
| **source_context** | Observed during Blueprint closure and backlog generation: the volume of generated artifacts (reports, context packets, verification reports, traceability maps, state YAMLs) now dwarfs the amount of executable code or validated runtime. The project produces documents about the framework faster than it produces framework behavior. |
| **description** | CAFL has generated an extensive document corpus (critical map, TOM, Blueprint 19 sections, verification reports, backlog candidates, glossary, risks, decisions) but has not yet validated a single end-to-end executable flow on Odoo 18. The ratio of documentation to validated execution is heavily skewed toward documentation. If this trend continues, V1 will be a documentation milestone, not an operational one. |
| **why_it_matters** | The owner's intent (CRIT-01) is to build an operational framework that delivers Odoo modules. A documentation factory would fail that intent even if every document is internally coherent. This is a scope-level risk: the framework might be well-specified but never operational. |
| **impact_area** | governance, roadmap, execution, autonomy |
| **classification** | SCOPE_CHANGE_RISK |
| **recommended_action** | Classify as SCOPE_CHANGE_RISK requiring owner decision: the owner must confirm whether the current documentation-to-execution ratio is acceptable or whether V1 scope should be adjusted to prioritize executable validation over additional documentation. |
| **creates_spike** | no |
| **spike_candidate** | no |
| **affects_roadmap** | yes |
| **affects_backlog** | yes |
| **affects_v1_scope** | yes |
| **severity** | critical |
| **status** | proposed |

---

### FND-POSTBP-07: Backlog candidates do not yet prove executable work-package generation

| Field | Value |
| --- | --- |
| **id** | FND-POSTBP-07 |
| **title** | Backlog candidates do not yet prove executable work-package generation |
| **source_context** | Observed in `reports/backlog/backlog-generation-report.md` and `reports/backlog/backlog-verification-report.md`: the backlog contains 9 epics and 30 capabilities, but zero tasks, user stories, or implementation steps. The report itself states: "No detailed tasks, user stories, or implementation steps generated." |
| **description** | Backlog candidates exist as epics and capabilities with traceability, but there is no evidence that the framework can decompose a capability into concrete, assignable, verifiable tasks with acceptance criteria, evidence requirements, and blocker declarations. The gap between "capability description" and "executable work package" is unbridged. |
| **why_it_matters** | Without executable work-package generation, the framework cannot self-organize execution. The owner or an external coordinator must still decompose work manually. This directly impacts CRIT-01's autonomy intent and CRIT-02's operating flow. |
| **impact_area** | backlog, execution, autonomy |
| **classification** | BACKLOG_IMPACT |
| **recommended_action** | Treat as BACKLOG_IMPACT: acknowledge that existing backlog candidates are conceptual only. Before V1 execution, the framework must demonstrate at least one capability-to-work-package decomposition with full task/context packets, DoR, acceptance criteria, and evidence requirements. |
| **creates_spike** | no |
| **spike_candidate** | no |
| **affects_roadmap** | no |
| **affects_backlog** | yes |
| **affects_v1_scope** | yes |
| **severity** | high |
| **status** | proposed |

---

### FND-POSTBP-08: Spikes are identified as conditional/post-V1 but not yet integrated into execution flow

| Field | Value |
| --- | --- |
| **id** | FND-POSTBP-08 |
| **title** | Spikes are identified as conditional/post-V1 but not yet integrated into execution flow |
| **source_context** | Observed in Blueprint S06 (Initial Spike Map), S16 (Spikes and Technical Validations final order), and backlog EPIC-BACKLOG-007: spikes are catalogued and sequenced (Band A/B/C/D), but there is no mechanism that triggers a spike, consumes its result, and gates subsequent execution based on that result. |
| **description** | The project has a rich spike catalogue (SP-01..SP-13, SPK-S13-*, SPK-S14-*, SPK-S15-*) with sequencing rules, but spikes exist as planning artifacts, not as integrated execution gates. There is no defined trigger condition (e.g., "if OpenCode permissions uncertainty remains, execute SP-04 before any command implementation"), no result format, and no gate that blocks execution until the spike resolves. |
| **why_it_matters** | Without spike-to-execution integration, the roadmap is a wish list, not a gated plan. Conditional capabilities (e.g., command standardisation, script boundary) remain conditional forever because there is no automatic or structured path from "spike complete" to "capability approved for implementation." |
| **impact_area** | roadmap, execution, governance |
| **classification** | ROADMAP_IMPACT |
| **recommended_action** | Treat as ROADMAP_IMPACT: define the spike integration model before the roadmap is finalized. Each conditional capability must have a spike trigger condition, a result format, and a gate that converts the capability from conditional to candidate (or rejects it). |
| **creates_spike** | no |
| **spike_candidate** | no |
| **affects_roadmap** | yes |
| **affects_backlog** | yes |
| **affects_v1_scope** | no |
| **severity** | medium |
| **status** | proposed |

---

### FND-POSTBP-09: Lack of an authoritative Odoo knowledge source creates false-confidence risk

| Field | Value |
| --- | --- |
| **id** | FND-POSTBP-09 |
| **title** | Lack of an authoritative Odoo knowledge source creates false-confidence risk |
| **source_context** | Observed during Blueprint S12 (Knowledge Base and Source Policy) and CRIT-06 governance discussions: DEC-ACCEPTED-163 limits pre-authorized sources to `docs.odoo.com` and `github.com/odoo/odoo`, but there is no curated knowledge artifact set, no snapshot mechanism, no freshness check, and no validator that confirms an agent is reasoning from an authorized source rather than from its training data. |
| **description** | Agents can (and do) produce Odoo-specific recommendations, code patterns, and architectural advice without confirming that their knowledge comes from an authorized, versioned, fresh source. The framework has no gate that blocks implementation when the only source is the agent's internal knowledge. This creates false confidence: the output looks correct but may be outdated, version-incompatible, or hallucinated. |
| **why_it_matters** | This is a critical quality and compliance risk. CRIT-06 explicitly prohibits using LLM training data as an authoritative source. Without a gate that enforces source authorization, V1 implementation could be built on incorrect or outdated Odoo knowledge. |
| **impact_area** | governance, quality, execution |
| **classification** | GATE |
| **recommended_action** | Establish a GATE that every implementation or design output must cite its authoritative source (with URL, version, and snapshot reference). Outputs without such citation must be blocked pending curation or escalation. This gate must be enforced before any code or schema is approved. |
| **creates_spike** | no |
| **spike_candidate** | yes |
| **affects_roadmap** | no |
| **affects_backlog** | yes |
| **affects_v1_scope** | yes |
| **severity** | critical |
| **status** | proposed |

---

### FND-POSTBP-10: Lack of formal distinction between finding, rule, gate, spike, scope change, and debt

| Field | Value |
| --- | --- |
| **id** | FND-POSTBP-10 |
| **title** | Lack of formal distinction between finding, rule, gate, spike, scope change, and debt |
| **source_context** | Observed while creating this register: the glossary (`project-truth/glossary.md`) defines many terms, but there is no formal taxonomy that distinguishes operational learnings (findings), behavioral constraints (rules), decision checkpoints (gates), investigative work (spikes), scope threats (scope-change risks), and accepted compromises (debt). Agents and documents conflate these categories. |
| **description** | The framework uses terms like "finding," "rule," "gate," "spike," and "debt" informally. A "finding" might be treated as a "rule" without owner approval, or a "spike" might be treated as executable work. This lack of formal taxonomy causes governance ambiguity: it is unclear who can act on what category, what approval is required, and what the consequences are. |
| **why_it_matters** | Without a formal taxonomy, the framework cannot govern itself. Every new operational learning requires a human decision about what it "is," which reintroduces the owner-as-coordinator dependency that CAFL is supposed to reduce. |
| **impact_area** | governance, execution, autonomy |
| **classification** | RULE |
| **recommended_action** | Establish a RULE that defines the formal taxonomy: what each category means, who can propose it, who approves it, what state transitions are allowed (e.g., finding → rule requires owner approval; finding → spike requires uncertainty assessment), and where each is recorded. |
| **creates_spike** | no |
| **spike_candidate** | no |
| **affects_roadmap** | no |
| **affects_backlog** | no |
| **affects_v1_scope** | no |
| **severity** | medium |
| **status** | proposed |

---

### FND-POSTBP-11: Risk that Blueprint is internally coherent but not fully aligned with owner expectation

| Field | Value |
| --- | --- |
| **id** | FND-POSTBP-11 |
| **title** | Risk that Blueprint is internally coherent but not fully aligned with owner expectation |
| **source_context** | Observed during Blueprint approval: the owner approved each section explicitly, but the approvals were section-by-section over multiple iterations. There was no consolidated owner review of the entire Blueprint as an integrated artifact. The deterministic verification checks internal consistency and traceability, not owner-intent alignment. |
| **description** | The Blueprint is internally consistent (233 traceable references, all sections approved), deterministic checks pass, and every section links to TOM or approved CRITs. However, there is no evidence that the owner has validated the *integrated* Blueprint against their original intent. Section-by-section approval does not guarantee that the whole is what the owner expected. |
| **why_it_matters** | If the Blueprint is internally coherent but misaligned with the owner's actual intent, V1 will be built in the wrong direction. This is a scope-level risk that could invalidate months of work. It is distinct from internal consistency and must be checked explicitly. |
| **impact_area** | governance, roadmap, execution, autonomy |
| **classification** | SCOPE_CHANGE_RISK |
| **recommended_action** | Classify as SCOPE_CHANGE_RISK requiring owner decision: the owner must perform (or delegate) an integrated Blueprint alignment review before execution begins. This is not a re-approval of sections; it is a holistic check of whether the assembled Blueprint matches the owner's intent. |
| **creates_spike** | no |
| **spike_candidate** | no |
| **affects_roadmap** | yes |
| **affects_backlog** | yes |
| **affects_v1_scope** | yes |
| **severity** | critical |
| **status** | proposed |

---

### FND-POSTBP-12: Current flow still depends heavily on owner/ChatGPT as external coordinator

| Field | Value |
| --- | --- |
| **id** | FND-POSTBP-12 |
| **title** | Current flow still depends heavily on owner/ChatGPT as external coordinator |
| **source_context** | Observed throughout the entire post-TOM workflow: every major transition (Blueprint section start, verification trigger, fix approval, re-verification trigger, backlog generation trigger, deterministic check trigger) was initiated by the owner or by a human using ChatGPT as the coordination interface. No transition was self-triggered by the framework. |
| **description** | Despite CRIT-01's autonomy intent and CRIT-03's mixed-responsibility model, the actual observed flow is human-coordinated. The owner decides when to start, what to verify, when to fix, and when to generate backlog. The framework does not have a self-coordination loop: it does not detect that a section is complete and auto-trigger verification, nor does it detect verification failure and auto-trigger fix assignment. |
| **why_it_matters** | If V1 begins with this level of external coordination, CAFL will not demonstrate the autonomy equivalent to a team. The owner will remain the project manager, runtime trigger, and error handler. This contradicts the core value proposition. |
| **impact_area** | autonomy, execution, governance |
| **classification** | RULE |
| **recommended_action** | Establish a RULE that every V1 execution flow must have a self-coordination model: state change must trigger the next step automatically (or with deterministic escalation), not wait for human initiation. The owner remains the approver of critical decisions, not the coordinator of every transition. |
| **creates_spike** | no |
| **spike_candidate** | no |
| **affects_roadmap** | yes |
| **affects_backlog** | yes |
| **affects_v1_scope** | yes |
| **severity** | high |
| **status** | proposed |

---

### FND-POSTBP-13: Capability → executable work package conversion is unproven

| Field | Value |
| --- | --- |
| **id** | FND-POSTBP-13 |
| **title** | Capability → executable work package conversion is unproven |
| **source_context** | Observed in backlog candidates (`reports/backlog/backlog-generation-report.md`): all 30 capabilities stop at the description level. There is no demonstrated path from, e.g., "CAP-BACKLOG-005: Command candidate standardisation" to a concrete set of tasks with assigned agents/commands, acceptance criteria, evidence formats, and blocker declarations. |
| **description** | The framework can generate capabilities (functional boundaries) but has not demonstrated that it can decompose a capability into executable work packages (tasks with DoR, context packet, producer, consumer, validator, acceptance criteria, evidence requirements, and estimated token budget). This is a fundamental execution gap. |
| **why_it_matters** | A framework that cannot convert its own capabilities into work cannot execute. This is a V1 blocker because V1's goal is to execute end-to-end. The gap is not in planning; it is in the execution bridge. |
| **impact_area** | execution, backlog, autonomy |
| **classification** | BACKLOG_IMPACT |
| **recommended_action** | Treat as BACKLOG_IMPACT: before V1 execution begins, demonstrate at least one end-to-end capability-to-work-package conversion. The demonstration must include: task decomposition, task/context packets, DoR validation, assignment to mechanism (agent/command/script), acceptance criteria, evidence format, and blocker declaration. |
| **creates_spike** | no |
| **spike_candidate** | yes |
| **affects_roadmap** | no |
| **affects_backlog** | yes |
| **affects_v1_scope** | yes |
| **severity** | high |
| **status** | proposed |

---

### FND-POSTBP-14: Generated artifacts can contaminate commits if validation regenerates timestamps or derived files

| Field | Value |
| --- | --- |
| **id** | FND-POSTBP-14 |
| **title** | Generated artifacts can contaminate commits if validation regenerates timestamps or derived files |
| **source_context** | Observed during deterministic verification: validation scripts (`blueprint_indexer.py`, `blueprint_state_check.py`, etc.) generate JSON and YAML files in `generated/blueprint/`. These files contain timestamps, line ranges, and derived data. If a developer runs validation and commits the regenerated files, the commit diff will be noisy and potentially misleading. |
| **description** | The framework generates derived artifacts (JSON indexes, state checks, traceability maps) as part of its verification process. These files contain non-deterministic or semi-deterministic data (timestamps, absolute paths, line ranges that shift with edits). The risk is partially mitigated: `generated/blueprint/` and `*.pyc` patterns are covered by the existing `.gitignore`. However, regenerated reports, state YAML updates, and other derived artifacts outside those patterns can still contaminate commits if validation is run and results are committed without review. The remaining gap is the absence of a pre-commit check that detects non-logical diffs (timestamp-only changes, regenerated file drift) and warns or blocks before the commit lands. |
| **why_it_matters** | Commit contamination undermines traceability and code review. A commit that should show a single logical change might instead show hundreds of lines of regenerated artifact diff. This degrades the audit trail that CRIT-06 mandates. The existing `.gitignore` reduces but does not eliminate the risk, because not all generated artifacts are covered by current ignore patterns. |
| **impact_area** | governance, quality, execution |
| **classification** | GATE |
| **recommended_action** | Establish a GATE that every commit must be checked for generated-artifact contamination before approval. Extend `.gitignore` coverage to remaining generated artifact patterns. Implement a pre-commit check that confirms generated files match their deterministic source and flags non-logical diffs (timestamp-only changes, regenerated file drift). |
| **creates_spike** | no |
| **spike_candidate** | no |
| **affects_roadmap** | no |
| **affects_backlog** | no |
| **affects_v1_scope** | yes |
| **severity** | critical |
| **status** | proposed |

---

### FND-POSTBP-15: Cheap models can produce structure, but should not approve critical decisions

| Field | Value |
| --- | --- |
| **id** | FND-POSTBP-15 |
| **title** | Cheap models can produce structure, but should not approve critical decisions |
| **source_context** | Observed during backlog generation and deterministic verification: some structural tasks (indexing, YAML generation, reference counting) were executed successfully by cheaper models. However, there is no explicit rule that prevents a cheap model from being used for gate approval, owner-decision simulation, or critical-rule enforcement. |
| **description** | The framework does not have a model-class policy. Any model configured in an agent can, in principle, be assigned to any task. Cheap models are demonstrably capable of structural work (parsing, counting, formatting) but are less capable of nuanced judgment, risk assessment, and owner-intent interpretation. Without a policy, a cost-conscious configuration might inadvertently assign critical approvals to cheap models. |
| **why_it_matters** | Critical decisions (gate approval, scope change, owner-intent interpretation) require high-reliability reasoning. Assigning them to cheap models creates a governance and quality risk that could invalidate approvals, misinterpret scope, or approve inadequate evidence. |
| **impact_area** | governance, cost, quality |
| **classification** | RULE |
| **recommended_action** | Establish a RULE that classifies tasks by required model capability: structural tasks may use cheaper models; judgment tasks (gate approval, scope assessment, risk evaluation, owner-intent interpretation) require explicit model-class assignment and must not default to the cheapest available model. |
| **creates_spike** | no |
| **spike_candidate** | no |
| **affects_roadmap** | no |
| **affects_backlog** | no |
| **affects_v1_scope** | no |
| **severity** | high |
| **status** | proposed |

---

## Register Integrity

- This register does not modify `project-truth/implementation-blueprint.md`.
- This register does not modify backlog candidates.
- This register does not modify approvals or decisions.
- This register does not authorize execution, roadmap creation, backlog triage, spike planning, or work-package generation.
- All findings are `proposed` and require review before promotion to any other status.
