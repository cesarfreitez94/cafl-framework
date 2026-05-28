# S10 Context Packet — Validators V1 Minimum Set

**Section ID:** S10  
**Mode:** normal  
**Generated from:** `project-truth/blueprint-state.yaml`, `project-truth/implementation-blueprint.md` (S10 excerpt + S08/S09 handoffs), approved context summaries (S07, S08, S09)

---

## Section Objective

Define the conceptual minimum validator set (V1) for CAFL, derived from SCH-01..SCH-10 as deterministic control candidates. Validators serve gates, evidence, and execution checks without creating real validators, executable toolchains, or scripts, and without substituting technical judgment or owner approval.

---

## Selected Section Excerpt (from working contract)

**Section:** 10. Validators V1 Minimum Set  
**Status:** not-started  
**Iteration:** I3

**Inputs esperados:**
- S09 (Schemas V1 Minimum Set).
- Accepted decisions on minimum validators and deterministic control.

**Outputs esperados:**
- Minimum conceptual set of validators to feed gates, evidence, and execution checks.

**Restricciones especificas:**
- No crear validators reales, toolchain ejecutable ni scripts.

**Acceptance criteria minimos:**
- Cada validator esperado queda trazable a un control requerido y no sustituye juicio tecnico ni owner approval.

---

## Dependency Context Summaries

### S09 — Schemas V1 Minimum Set (approved)
Defines conceptual minimum schema set SCH-01..SCH-10: Authority Source, Traceability Link, Work State, Gate/Approval, Evidence Record, Deterministic Control, Runtime Output/Candidate Evidence, Context Packet, Source Policy/Knowledge Gap, Odoo Pilot Artifact. All schemas are logical categories only; physical schemas, JSON Schema, YAML schema, DDL, tables, ORM models and final formats are excluded. Each traces to CRIT-06/CRIT-07, TOM, APs, BR-01, S04/S05/S07/S08, and accepted decisions. Handoff to S10: derive validators from SCH-01..SCH-10 as deterministic control candidates; no validator future may close gates, grant owner approval, or convert runtime outputs into authority. *(source: blueprint-state.yaml S09.context_summary)*

### S08 — Agents / Commands / Scripts / Validators Split (approved)
Defines conceptual mechanism split: agents (reasoning), command candidates (repeatable inputs), script/CLI/validator candidates (deterministic control), rules/config (invariants), skills/playbooks (procedural), human/owner (decisions/gate closure). Handoff to S10: validators belong to deterministic control mechanism, not agents or commands; their result does not replace owner approval or governed evidence. OpenCode remains primary runtime but not authoritative state, gate, storage, source policy, or policy engine. *(source: blueprint-state.yaml S08.context_summary)*

### S07 — OpenCode Operating Design (approved)
Defines conceptual OpenCode operating design as primary runtime/coordination hub within hybrid progressive model. Differentiates agents, command candidates, script/CLI/validator candidates, rules/config, skills/playbooks, and human/owner roles. OpenCode coordinates handoffs but must not decide approvals, close gates, change state, or treat chat/output as sufficient evidence. *(source: blueprint-state.yaml S07.context_summary)*

---

## Hard Inherited Constraints

1. **RULE-04:** Every Blueprint component must trace to TOM, approved CRIT, or accepted decision. Untraceable components must be eliminated, marked post-V1, or registered as owner-decision-required.
2. **RULE-09:** Blueprint must not create runtime, executable agents, real commands, physical schemas, real validators, scripts, RAG/vector base, technical backlog, or implementation.
3. **AP-04:** Deterministic control must be separated from LLM reasoning and reserved for script/CLI/validator candidates.
4. **AP-05:** Progress is contract/gate/evidence driven; no self-closure. Owner approval is required for all gates and closures.
5. **AP-09:** Evidence must be simple, auditable, Git-compatible; runtime evidence is candidate until governed registration.
6. **S05:** `project-truth/` is sole authority; runtime outputs are candidate evidence only.
7. **S08 mechanism split:** Validators are script/CLI/validator candidates under deterministic control; results do not replace owner approval or governed evidence.
8. **S09 handoff:** Validators must derive from SCH-01..SCH-10 as deterministic control candidates only; no gate closure, no owner approval substitution, no conversion of runtime outputs into authority.
9. **V1 boundaries:** Odoo-only, Odoo 18, internal requests/simple approvals pilot. No RAG/vector, SDK/server, dashboard, CI/CD, advanced storage, multiuser, plugins/MCP.
10. **framework/** excluded as input or reference.

---

## Required Traceability Anchors

| Anchor | Purpose |
|--------|---------|
| CRIT-06 | State, logs, evidence, IDs, traceability |
| CRIT-07 | Minimum schemas (non-permanent) |
| AP-04 | Deterministic control separation |
| AP-05 | Gate/evidence-driven progress |
| AP-09 | Auditable evidence |
| S04 | Runtime layout candidate (deterministic control zone) |
| S05 | Source-vs-runtime separation |
| S08 | Mechanism split (validators = deterministic control) |
| S09 | SCH-01..SCH-10 conceptual base |
| DEC-ACCEPTED-138 | Validators/control decisions |
| DEC-ACCEPTED-140 | Evidence decisions |
| DEC-ACCEPTED-145 | Evidence decisions |
| TOM | Control, evidence, handoff anchors |
| BR-01 | V1 Odoo boundary |

---

## Forbidden Moves / Non-Goals

- Do NOT create real validators, executable toolchain, or scripts.
- Do NOT create physical schemas, JSON Schema, YAML schema, DDL, ORM models.
- Do NOT close gates, grant owner approval, or convert runtime outputs into authority.
- Do NOT introduce RAG/vector base, SDK/server core, MCP/plugins, CI/CD.
- Do NOT expand V1 beyond Odoo-only, Odoo 18, internal requests/simple approvals.
- Do NOT use `framework/` as input or reference.
- Do NOT create backlog, PRD, SDD, or implementation.
- Do NOT change acceptance criteria, governance rules, status semantics, or source policy.

---

## Acceptance Checklist

- [ ] Minimum conceptual validator set defined (logical categories, not executables).
- [ ] Validators derived from SCH-01..SCH-10 as deterministic control candidates.
- [ ] Each validator traces to a required control (CRIT-06, CRIT-07, AP-04, AP-09).
- [ ] No validator replaces technical judgment or owner approval.
- [ ] No validator closes gates or converts runtime outputs into authority.
- [ ] Validators preserve source-vs-runtime separation (S05).
- [ ] All components traceable to TOM, approved CRIT, or accepted decision (RULE-04).
- [ ] Handoffs defined to S11 (storage/evidence), S12 (source policy), S13-S15 (Odoo 18 pilot).
- [ ] No runtime, real validators, scripts, toolchain, or implementation created.
- [ ] `framework/` excluded; V1 boundaries preserved.

---

## Fallback-to-Strict Triggers

- Packet cannot prove required traceability for any validator.
- Validator design conflicts with S09 schemas or S08 mechanism split.
- Owner-decision blocker appears (untraceable validator, scope ambiguity).
- Author introduces claims not covered by this packet.
- Forbidden artifact ambiguity (approaching real validators/toolchain).
- Retroactive blocker affecting prior approved sections.
- Governance rule, source policy, status semantics, or owner approval semantics change required.
