# S11 Context Packet — State / Logs / Evidence Storage

## Section Objective

Diseno de storage conceptual para alimentar evidence, traceability y backlog categories. Debe definir como almacenar estado, logs y evidencia de forma simple, auditable y Git-compatible, sin crear storage fisico ni rutas finales.

## Selected Section Excerpt (from Blueprint)

- **Inputs:** Secciones 9 y 10 de la iteracion correspondiente. Modelo logico de estado, logs, evidencia e IDs aprobado en CRIT-06.
- **Outputs:** Diseno de storage conceptual para alimentar evidence, traceability y backlog categories.
- **Restricciones:** No crear storage fisico, rutas finales, logs reales ni artifacts.
- **Acceptance criteria:** La seccion preserva estado autoritativo, evidencia reproducible y no double work sin implementar storage.

## Dependency Context Summaries

### S09 — Schemas V1 Minimum Set (approved)

Define 10 schemas logicos (SCH-01..SCH-10). Relevant to S11: SCH-03 Work State, SCH-05 Evidence Record, SCH-07 Runtime Output / Candidate Evidence. S09 handoff: "S11 debe usar SCH-03, SCH-05 y SCH-07 como base para almacenamiento logico simple y auditable, manteniendo `project-truth/` como autoridad y tratando evidencia runtime como candidata hasta registro gobernado."

### S10 — Validators V1 Minimum Set (approved)

Define 10 validators (VAL-01..VAL-10), one per schema. Relevant to S11: VAL-03 Work State Transition, VAL-04 Gate Prerequisites, VAL-05 Evidence Record, VAL-06 Deterministic Control. S10 handoff: "S11 debe recibir de S10 los resultados candidatos de VAL-01..VAL-10 como evidencia candidata a registrar. S11 debe definir como almacenar logs de transiciones de estado (VAL-03), resultados de prerequisitos de gate (VAL-04), confirmaciones de evidencia bien formada (VAL-05) y resultados de control deterministico (VAL-06) de forma simple, auditable y Git-compatible, sin crear storage fisico ni rutas finales. Ningun resultado de validator es autoridad por si mismo; requiere registro gobernado para ser evidencia formal."

### S08 — Agents/Commands/Scripts/Validators Split (closed, I2)

S08 handoff to S11: "logs, reportes, outputs de agents/commands y resultados de validators son evidencia candidata hasta registro trazable bajo la separacion source-vs-runtime de S05."

## Hard Inherited Constraints

- **AP-09:** Storage, logs y evidencia deben ser simples, auditables y compatibles con Git.
- **AP-04:** Control deterministico separado del razonamiento LLM.
- **AP-05:** Progreso por contratos, gates, evidencia y cierre verificable; no autocierre.
- **AP-01:** `project-truth/` como fuente unica de verdad; trazabilidad bidireccional.
- **AP-06:** Context routing y source policy minima obligatorios.
- **S05 source-vs-runtime:** Evidencia runtime es candidata hasta registro gobernado; `project-truth/` mantiene autoridad.
- **DEC-ACCEPTED-146:** State/evidence storage candidate V1 simple, auditable, Git-compatible (Markdown, JSON/YAML, JSONL append-only, artifacts; rutas finales para blueprint).
- **DEC-ACCEPTED-138:** Runtime candidate: OpenCode + commands + scripts/CLI/validators + storage fisico simple y auditable (direccion, no implementacion).
- **DEC-ACCEPTED-140:** Automatizacion minima cubre validacion estructural y logs/estado/evidencia.
- **CRIT-06:** Modelo logico de estado, storage logico, persistencia conceptual, IDs, logs, evidencia, fuentes, contexto, rework, deuda, approvals, trazabilidad.
- **RULE-09:** No crear runtime, agents ejecutables, commands reales, schemas fisicos, validators reales, scripts, RAG/vector base, backlog ni implementacion.
- **RULE-10:** No usar `framework/` como input.

## Required Traceability Anchors

| Anchor | Source | Relevance |
|--------|--------|-----------|
| CRIT-06 | critical-map.md | State/evidence/traceability logical model |
| CRIT-07 | critical-map.md | V1 runtime candidate direction |
| AP-01, AP-04, AP-05, AP-06, AP-09 | S02 Architecture Principles | Authority, deterministic control, gates/evidence, context, simple storage |
| S04 | Runtime Layout Candidate | Zone: estado, logs y evidencia auditable |
| S05 | Source-vs-Runtime Structure | Evidence candidata hasta registro gobernado |
| S07 | OpenCode Operating Design | OpenCode como runtime no autoritativo para storage |
| S08 | Mechanism Split | Logs/outputs/validator results = evidencia candidata |
| S09 SCH-03, SCH-05, SCH-07 | Schemas V1 | Logical schemas for storage |
| S10 VAL-03, VAL-04, VAL-05, VAL-06 | Validators V1 | Validator results as candidate evidence to store |
| DEC-ACCEPTED-146 | accepted.md | Git-compatible simple storage candidate |
| DEC-ACCEPTED-138 | accepted.md | Runtime candidate with simple storage |
| DEC-ACCEPTED-140 | accepted.md | Minimum automation covering logs/evidence |
| DEC-ACCEPTED-162 | accepted.md | Pilot: internal requests / simple approvals |
| DEC-ACCEPTED-163 | accepted.md | Source policy minima |
| TOM | TOM.md | Handoff al Blueprint para schemas, logs, evidence, storage |

## Forbidden Moves / Non-Goals

- No crear storage fisico, rutas finales, archivos reales ni artifacts.
- No crear logs reales ni implementacion de logging.
- No decidir toolchain, lenguaje, librerias, CI/CD ni estructura runtime final.
- No convertir OpenCode en storage final o autoridad de evidencia.
- No convertir outputs runtime en evidencia formal sin registro gobernado.
- No crear schemas fisicos, validators reales, scripts, commands, agents ejecutables.
- No crear RAG/vector base, SDK/server, backlog, PRD, SDD, implementacion.
- No usar `framework/` como input o referencia.
- No expandir V1 fuera de Odoo-only, Odoo 18, piloto internal requests / simple approvals.
- No cambiar source policy, owner approval semantics, status semantics ni reglas de governance.

## Acceptance Checklist

- [ ] Define modelo conceptual de storage para estado, logs, evidencia y outputs candidatos.
- [ ] Usa SCH-03, SCH-05, SCH-07 como base logica.
- [ ] Integra VAL-03, VAL-04, VAL-05, VAL-06 como fuentes de evidencia candidata.
- [ ] Preserva `project-truth/` como autoridad; evidencia runtime es candidata hasta registro gobernado.
- [ ] Diseno simple, auditable, Git-compatible (AP-09, DEC-ACCEPTED-146).
- [ ] Trazabilidad bidireccional a TOM, CRIT-06, decisiones aceptadas.
- [ ] No double work: no duplica estado ya cubierto por `blueprint-state.yaml`.
- [ ] Handoffs claros a S12 (source policy/Knowledge Gap) y S13-S15 (Odoo 18 pilot evidence).
- [ ] No implementa storage fisico, rutas, scripts ni artifacts.
- [ ] Respeta S05 source-vs-runtime separation.
- [ ] Explicit non-decisions listed for forbidden artifacts.

## Fallback-To-Strict Triggers

- Packet cannot prove required traceability (any anchor missing or ambiguous).
- Packet conflicts with S11 section content or operational state.
- Owner-decision blocker appears.
- Approved dependency (S09, S10) context_summary missing or inconsistent.
- Governance rule, source policy, status semantics, or owner approval semantics change needed.
- Forbidden artifact ambiguity: unclear whether a proposed concept crosses into physical storage.
- Retroactive blocker detected affecting I1 or I2 sections.
- Author introduces claims not covered by this packet.
