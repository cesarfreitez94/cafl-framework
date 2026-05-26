# CRIT-04: Contracts

Status: approved

## Session Objective

- [accepted] Definir la estructura contractual minima para coordinar fases, entregables y mecanismos del modelo mixto, sin crear contratos finales.
- [accepted] CRIT-04 aprueba un modelo contractual conceptual; no aprueba contratos finales, schemas finales, gates, commands, agents ejecutables ni implementacion runtime.

## Context

- [accepted] CRIT-01 Intent and Scope esta approved.
- [accepted] CRIT-02 Operating Flow esta approved.
- [accepted] CRIT-03 Agent Responsibilities esta approved.
- [accepted] CRIT-03 aprobo modelo mixto: agents, commands, SDK/server/scripts/control deterministico, rules/config, skills/playbooks y owner/human segun responsabilidad.
- [accepted] PRD ligero, SDD ligero, task/context packet, Definition of Ready, context routing, token budget y rework acotado son obligatorios por CRIT-02/CRIT-03.
- [superseded] `framework/CONTRACT_CATALOG.md`, `framework/AGENT_CONTRACTS.md` y `framework/agents/*.agent.md` fueron evidencia secundaria historica durante CRIT-04; CRIT-07 supersedio su uso: `framework/` fue eliminado como artefacto contaminado y no es evidencia secundaria utilizable ni input de TOM/Blueprint.
- [accepted] CRIT-04 define estructura contractual; CRIT-05 ya aprobo gates conceptuales, CRIT-06 ya aprobo estado/evidencia/trazabilidad logica y CRIT-07 ya aprobo direccion candidata de implementacion/runtime.

## Owner Approval

- [accepted] El owner aprobo las recomendaciones de CRIT-04 Contracts Technical Elicitation con ajustes menores obligatorios.
- [accepted] Ajuste obligatorio 1: los contratos V1 se separan entre `always-required` y `conditional-required`.
- [accepted] Ajuste obligatorio 2: el campo `blockers` del task/context packet es `conditional`; si existen blockers conocidos deben declararse, y si no existen debe declararse explicitamente `none`.

## Approved Decisions

- [accepted] DEC-CRIT04-01: CAFL usara modelo contractual hibrido: contrato base comun mas extensiones por fase, mecanismo y riesgo.
- [accepted] DEC-CRIT04-02: El inventario minimo V1 se organiza por transiciones criticas y responsabilidades transversales, no por agentes finales.
- [accepted] DEC-CRIT04-03: Todo contrato conceptual debe tener contrato base comun con proposito, unidad de control, producer, consumer, validator, inputs, outputs, contexto, token budget, restricciones, criterios de suficiencia, rechazo, evidencia, blockers, handoff, version y trazabilidad.
- [accepted] DEC-CRIT04-04: El task/context packet es la unidad central obligatoria para toda unidad operativa verificable.
- [accepted] DEC-CRIT04-05: La Definition of Ready minima debe ser validada por receptor o validador; no puede autoaprobarse solo por el productor.
- [accepted] DEC-CRIT04-06: Todo contrato debe declarar producer, consumer y validator; el consumidor/receptor puede rechazar contratos insuficientes.
- [accepted] DEC-CRIT04-07: Cuando exista riesgo relevante, el validador no debe ser el mismo ejecutor.
- [accepted] DEC-CRIT04-08: La suficiencia contractual se evalua desde el consumidor/receptor.
- [accepted] DEC-CRIT04-09: Context routing es obligatorio por contrato y debe distinguir fuentes autorizadas, aplicables, secundarias, prohibidas/no relevantes y excepciones.
- [accepted] DEC-CRIT04-10: Token budget se declara mediante budget class, politica de expansion y registro de excepciones; los numeros finales y enforcement quedan fuera de CRIT-04.
- [accepted] DEC-CRIT04-11: La evidencia esperada no puede ser solo narrativa LLM; debe declarar outputs, artefactos, fuentes, decisiones, riesgos, blockers, pruebas/comandos/logs aplicables y handoff.
- [accepted] DEC-CRIT04-12: El contrato base se adapta mediante perfiles por mecanismo candidato: human, agent, command, SDK/server/script, rule/config/skill o mixed.
- [accepted] DEC-CRIT04-13: Versionado y trazabilidad contractual quedan aprobados a nivel conceptual, conectando modulo, capability/feature, tarea, decision, riesgo, evidencia, rework y handoff.
- [accepted] DEC-CRIT04-14: Rework, blockers y escalamiento deben estar representados en contratos como campos obligatorios o condicionales, sin definir todavia gates ni acciones finales.
- [accepted] DEC-CRIT04-15: CRIT-04 define estructura contractual, campos, handoffs y suficiencia; nota posterior: CRIT-05 fue aprobado como modelo conceptual de gates/verificacion, CRIT-06 como modelo logico/conceptual de estado/evidencia/trazabilidad/knowledge governance y CRIT-07 como direccion de viabilidad/runtime candidato y cierre de elicitacion critica, sin crear decision de implementacion.

## V1 Contract Classification

### Always-Required

- [accepted] Base Contract Envelope.
- [accepted] Idea -> PRD Contract.
- [accepted] PRD -> SDD Contract.
- [accepted] SDD -> Task/Context Packet Contract.
- [accepted] Task/Context Packet + DoR Contract.
- [accepted] Task Execution Contract.
- [accepted] QA/Testing Contract.
- [accepted] Evidence/Closure Contract.
- [accepted] Context Routing / Token Budget Contract.

### Conditional-Required

- [accepted] Security/Risk/Compliance Review Contract.
- [accepted] Rework Contract.
- [accepted] Escalation/Owner Decision Contract.
- [accepted] Mechanism Execution Profile Contract.

### Compliance Visibility Rule

- [accepted] Seguridad/riesgo/compliance siempre debe estar visible como criterio contractual transversal.
- [accepted] El contrato/review especializado de seguridad/riesgo/compliance se activa de forma condicional por riesgo, severidad, compliance, seguridad, datos, normativa o tipo de modulo.
- [accepted] La clasificacion condicional del review especializado no autoriza diluir compliance dentro de QA generico o seguridad tecnica.

## Conceptual Contract Matrix

| Contract | Required class | Purpose | Producer | Consumer | Validator | Required inputs | Required outputs | Context rules | Token budget rule | Evidence expected | Blockers | Handoff | Related future CRIT |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Base Contract Envelope | always-required | Campos comunes para todo contrato interno | Orquestacion o fase productora | Cualquier receptor | Receptor y orquestacion | Unidad, objetivo, alcance, roles, fuentes, restricciones | Contrato completo o rechazo | Clasificar autorizado, aplicable, secundario y prohibido/no relevante | Budget class obligatorio | Razon de contrato, fuentes, decisiones, blockers si existen | Roles ausentes, contexto critico faltante | Extension por fase/mecanismo | CRIT-06, CRIT-07 |
| Idea -> PRD Contract | always-required | Convertir idea breve en PRD ligero suficiente | Owner y analisis funcional | Diseno tecnico Odoo | Owner para alcance critico, orquestacion | Idea, problema, objetivo, modulo/capability, restricciones | PRD ligero, scope in/out, criterios funcionales, dudas bloqueantes | `project-truth/` e input owner mandan; repo previo solo secundario | Bajo/medio; sin lectura total de repo | Preguntas, decisiones, supuestos, riesgos | Objetivo ambiguo, alcance imposible, decision critica sin owner | PRD -> SDD | CRIT-05, CRIT-06 |
| PRD -> SDD Contract | always-required | Traducir PRD aprobado a diseno tecnico ligero | Analisis funcional | Arquitecto Odoo | Arquitecto, QA/riesgo segun impacto | PRD suficiente, criterios, restricciones, riesgos | SDD ligero, ADR minimo si aplica, estrategia tecnica | Fuentes Odoo oficiales y contexto aplicable | Medio/alto segun riesgo | Decisiones tecnicas, fuentes usadas/excluidas, riesgos | PRD incompleto, fuente Odoo insuficiente, contradiccion critica | SDD -> task/context packet | CRIT-05, CRIT-06, CRIT-07 |
| SDD -> Task/Context Packet Contract | always-required | Descomponer diseno en tareas verificables | Arquitecto y orquestacion | Builder, QA, reviewer | Receptor y orquestacion | SDD, PRD, riesgos, constraints | Lista de tareas verificables y packets candidatos | Solo artefactos necesarios por tarea | Medio; por tarea no por repo completo | Razon de division, dependencias, riesgos | Tareas no verificables, alcance mezclado | Task/context packet | CRIT-06 |
| Task/Context Packet + DoR Contract | always-required | Declarar unidad minima ejecutable y readiness | Fase productora u orquestacion | Ejecutor | Receptor, futuro check deterministico | Objetivo, alcance, fuentes, inputs, outputs, criterios | Packet ready o rechazo DoR | Contexto autorizado y prohibido explicito | Budget class y expansion policy | DoR decision, faltantes, excepciones | Campos minimos ausentes, consumidor no puede ejecutar | Task execution | CRIT-05, CRIT-06, CRIT-07 |
| Task Execution Contract | always-required | Ejecutar una tarea verificable sin inventar | Builder o capacidad ejecutora | QA/testing, evidence/closure | QA, arquitecto o reviewer aplicable | Packet ready, SDD, restricciones, archivos objetivo | Cambio realizado, reporte, evidencia primaria | Solo archivos/fuentes autorizadas y relacionadas | Ajustado a tarea; excepciones registradas | Archivos tocados, razonamiento, riesgos, tests aplicables | Scope creep, fuente insuficiente, permisos no claros | QA/testing o rework | CRIT-05, CRIT-07 |
| QA/Testing Contract | always-required | Planificar, ejecutar o revisar verificacion aplicable | QA y mecanismo de ejecucion | Rework, closure, owner si critico | QA independiente, futuro script/control | Outputs de ejecucion, criterios, test scope | Resultado QA, fallas, evidencia de tests/logs | Contexto de cambios, tests, logs y requisitos | Medio/alto; centrado en evidencias | Plan, comandos/logs aplicables, diagnostico | Tests no ejecutables, evidencia ausente, autocierre | Rework o closure | CRIT-05, CRIT-07 |
| Evidence/Closure Contract | always-required | Preparar cierre verificable de fase/tarea/modulo | Evidence/closure y orquestacion | Owner o siguiente fase | QA, orquestacion, owner final | Outputs, tests, docs, riesgos, decisiones | Paquete de cierre, resumen, handoff, pendientes | Solo evidencia y fuentes trazadas | Medio; orientado a sintesis | Artefactos, logs, fuentes, riesgos, decisiones | Evidencia faltante, DoD no demostrable | Siguiente fase o aceptacion final | CRIT-05, CRIT-06 |
| Context Routing / Token Budget Contract | always-required | Gobernar lectura de fuentes y presupuesto | Context routing capability | Todos los contratos | Orquestacion, futuro control deterministico | Unidad, objetivo, fuentes candidatas | Context map, budget class, excepciones | Autoridad documental explicita | Budget por fase/tarea; no repo completo | Fuentes usadas/excluidas, excepciones | Fuente prohibida necesaria, budget insuficiente para riesgo | Packet o escalation | CRIT-06, CRIT-07 |
| Security/Risk/Compliance Review Contract | conditional-required | Mantener seguridad, riesgo y compliance visibles | Reviewer o checklist transversal | Arquitecto, builder, QA, owner | Reviewer especializado u owner si critico | PRD/SDD/task, datos, permisos, impacto legal | Riesgos, blockers, recomendaciones, escalamiento | Fuentes oficiales aplicables; no inventar normativa | Medio; expansion justificada | Riesgos, fuentes, limites, decision requerida | Riesgo legal/compliance critico, contradiccion normativa | Rework, escalation o closure | CRIT-05, CRIT-06 |
| Rework Contract | conditional-required | Controlar retrabajo acotado bajo mismo alcance | QA, reviewer u orquestacion | Ejecutor original o alternativo | QA/reviewer y orquestacion | Falla, evidencia, criterio incumplido, ciclo actual | Correccion, analisis, evidencia actualizada | Contexto de falla y tarea original | Bajo/medio; no reabrir todo | Causa, cambios, pruebas, ciclo | Tercer ciclo significativo, cambio de alcance oculto | QA/testing o escalation | CRIT-05, CRIT-06 |
| Escalation/Owner Decision Contract | conditional-required | Elevar solo decisiones criticas al owner | Cualquier capacidad via orquestacion | Owner | Owner y orquestacion para registro | Pregunta, opciones, recomendacion, riesgos | Decision owner o pendiente explicito | Contexto minimo suficiente para decidir | Bajo; decision pack breve | Decision, motivo, impacto, pendientes | Falta contexto critico, riesgo alto, decision irreversible | Replan, rework o avance | CRIT-05, CRIT-06 |
| Mechanism Execution Profile Contract | conditional-required | Adaptar contrato al mecanismo consumidor | Orquestacion o disenador de flujo | Human, agent, command, script, skill, mixed | Receptor y futuro runtime/control | Contrato base y mecanismo objetivo | Perfil de consumo, restricciones, evidencia | Segun mecanismo y permisos conceptuales | Segun mecanismo; scripts con logs, agents con contexto limitado | Inputs, outputs, logs o respuesta esperada | Mecanismo no apto, permisos ambiguos | Ejecucion o CRIT-07 | CRIT-07 |

## Candidate Task/Context Packet Fields

| Field | Required | Purpose | Producer | Validator | Failure if missing | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| packet_id | yes | Identificar instancia del packet | Orquestacion | Orquestacion | No hay trazabilidad | ID final queda para CRIT-06 |
| contract_type | yes | Indicar contrato aplicable | Orquestacion | Receptor | No se sabe como validar | Candidato, no schema final |
| contract_version | yes | Controlar version conceptual | Orquestacion | Receptor | Cambios no auditables | Versionado final CRIT-06 |
| status | yes | Distinguir draft, ready, rejected, blocked, done | Productor | Receptor | DoR ambiguo | Estados finales CRIT-06 |
| control_unit | yes | Ubicar modulo, capability/feature o tarea | Productor | Orquestacion | No hay alcance operativo | Debe seguir jerarquia aprobada |
| objective | yes | Definir resultado buscado | Productor | Receptor | Ejecucion inventada o desviada | Debe ser verificable |
| scope_in | yes | Limitar lo incluido | Productor | Receptor | Scope creep | Debe ser breve |
| scope_out | yes | Limitar lo excluido | Productor | Receptor | Cambios fuera de alcance | Importante para autonomia |
| producer | yes | Declarar quien genera el packet | Productor | Orquestacion | No hay responsabilidad | Puede ser human, agent o mixed |
| consumer | yes | Declarar quien ejecuta o recibe | Productor | Orquestacion | No hay receptor claro | Consumidor puede rechazar |
| validator | yes | Declarar quien valida suficiencia o salida | Productor | Orquestacion | Riesgo de autocierre | Puede ser conceptual en CRIT-04 |
| authorized_sources | yes | Definir fuentes permitidas/prioritarias | Context routing/productor | Receptor | Contexto insuficiente o contaminado | `project-truth/` manda en el framework |
| secondary_sources | conditional | Permitir evidencia secundaria controlada | Context routing/productor | Receptor | Uso secundario no trazado | No autoriza usar `framework/`; por CRIT-07 no es fuente secundaria utilizable |
| prohibited_or_not_relevant_sources | yes | Evitar lectura innecesaria o fuente invalida | Context routing/productor | Receptor | Se puede leer contexto indebido | Incluye no leer todo el repo |
| context_applicability | yes | Explicar por que una fuente aplica | Context routing/productor | Receptor | Fuente usada sin justificacion | Campo breve |
| token_budget_class | yes | Limitar costo/contexto | Context routing/productor | Receptor | Bloat de tokens | Numeros finales CRIT-07 |
| token_budget_exception_policy | yes | Definir cuando expandir contexto | Context routing/productor | Orquestacion | Excepciones invisibles | Excepciones criticas escalan |
| constraints | yes | Declarar limites tecnicos, funcionales y operativos | Productor | Receptor | Implementacion insegura o fuera de alcance | Incluye restricciones de no modificar si aplican |
| required_inputs | yes | Listar artefactos necesarios | Productor | Receptor | Consumidor no puede ejecutar | Deben tener autoridad clara |
| expected_outputs | yes | Definir entregables | Productor | Receptor | Salida no verificable | Puede incluir texto, codigo, docs |
| acceptance_criteria | yes | Definir exito verificable | Productor | Validator | No se puede aceptar/rechazar | Gates finales CRIT-05 |
| expected_evidence | yes | Declarar pruebas o evidencia esperada | Productor | Validator | Cierre narrativo | Formato persistente CRIT-06 |
| risk_flags | conditional | Senalar seguridad, datos, compliance, arquitectura | Productor/reviewer | Reviewer | Riesgo critico oculto | Obligatorio si aplica |
| blockers | conditional | Declarar blockers conocidos o `none` | Productor | Receptor | DoR ambiguo: no se sabe si no hay blockers o si no fueron evaluados | Si existen blockers conocidos, declararlos; si no existen, declarar `none` |
| escalation_conditions | yes | Definir cuando va al owner | Productor | Orquestacion | Microgestion o no escalamiento | Owner solo decisiones criticas |
| rework_context | conditional | Indicar ciclo y causa de retrabajo | QA/orquestacion | Orquestacion | Loops invisibles | Politica final CRIT-05 |
| handoff_next | yes | Declarar receptor siguiente | Productor | Orquestacion | Se pierde continuidad | Conecta contratos |
| open_questions | conditional | Registrar dudas no bloqueantes o bloqueantes | Productor | Receptor | Supuestos ocultos | Bloqueantes deben resolverse |
| assumptions | conditional | Declarar supuestos permitidos | Productor | Receptor | Se inventa contexto | Supuestos criticos escalan |

## Definition Of Ready Conceptual

- [accepted] Una unidad operativa puede iniciar solo si tiene task/context packet suficiente.
- [accepted] La DoR debe validar campos minimos, alcance ejecutable, contexto suficiente, fuentes autorizadas, fuentes prohibidas/no relevantes, token budget class, politica de excepcion, inputs, outputs, criterios de aceptacion, evidencia esperada, blockers declarados o `none`, condiciones de escalamiento y handoff.
- [accepted] El productor no puede autoaprobar DoR por si solo.
- [accepted] El receptor puede rechazar el packet si no puede ejecutar sin inventar, si el contexto critico falta o si los criterios/evidencia no son verificables.
- [accepted] CRIT-04 no define gates finales, severidades ni acciones por fallo; eso pertenece a CRIT-05.

## Mechanism Profiles Conceptual Rule

- [accepted] Human: requiere decision pack breve, opciones, recomendacion, riesgos y decision requerida.
- [accepted] Agent: requiere objetivo, contexto autorizado limitado, restricciones, outputs esperados y criterio de rechazo.
- [accepted] Command: requiere entrada repetible, argumentos, contexto minimo declarado y salida esperada; no es autoridad final.
- [accepted] SDK/server/script: requiere inputs estructurados, salida reproducible, logs/evidencia y reglas de error; CRIT-07 aprobo direccion candidata y la implementacion concreta queda para Blueprint/spikes post-CRIT-07.
- [accepted] Rule/config/skill: requiere alcance de aplicacion, invariantes o playbook, y condiciones de uso; no reemplaza estado ni gates.
- [accepted] Mixed: requiere separar que parte razona, que parte valida, que parte ejecuta y que parte registra evidencia.

## Non-Goals Confirmed

- [accepted] No redactar contratos finales.
- [accepted] No crear gates finales ni acciones por fallo; eso pertenece a CRIT-05.
- [accepted] No definir estado persistente, evidence log ni decision log finales; eso pertenece a CRIT-06.
- [accepted] No definir arquitectura runtime, commands, scripts, agentes ejecutables ni configuracion OpenCode; eso pertenece a CRIT-07.
- [accepted] No crear JSON Schema final.
- [accepted] No implementar validadores.
- [accepted] No convertir plantillas candidatas en implementacion.
- [accepted] No elevar ni reutilizar `framework/AGENT_CONTRACTS.md`, `framework/CONTRACT_CATALOG.md` ni `framework/agents/*.agent.md`; por CRIT-07 no son evidencia secundaria utilizable ni input de TOM/Blueprint.

## Downstream Handoff

- [accepted] CRIT-05 debe definir gates, severidades, categorias, acciones por fallo, DoD verificable, testing suficiente/aplicable, deuda aceptable, consecuencias de rework y politica concreta de avance/bloqueo.
- [accepted] CRIT-06 debe definir estado autoritativo, IDs finales, decision log, evidence log, source log, context log, excluded/prohibited context log, trazabilidad persistente, historial de rework y registro real de token/context usage.
- [accepted] CRIT-07 aprobo direccion candidata de schemas V1 minimos, validators, runtime, OpenCode, agents/commands futuros, SDK/server condicional, permissions, rutas, entorno Odoo y ejecucion reproducible; su materializacion exacta queda para TOM/Blueprint/technical validations post-CRIT-07.

## Acceptance Criteria Result

- [accepted] Cada contrato candidato tiene consumidor claro.
- [accepted] Cada contrato candidato identifica producer, consumer, validator y criterio de rechazo por consumidor o receptor.
- [accepted] El modelo cubre agent, command, SDK/server/script, rule/config, skill/playbook, human/owner y mixed sin asumir implementacion final.
- [accepted] Task/context packet y Definition of Ready quedan modelados como estructura contractual conceptual.
- [accepted] Contexto autorizado, excluido/prohibido/no relevante, token budget, inputs, outputs, evidencia, blockers condicionales y criterio de suficiencia quedan contemplados.
- [accepted] Los contratos V1 quedan clasificados como `always-required` y `conditional-required`.
- [accepted] CRIT-05, CRIT-06 y CRIT-07 ya aprobaron los modelos conceptuales/direccion candidata correspondientes; formatos finales, schemas, estado persistente fisico, gates finales, validators y runtime quedan para TOM/Blueprint/technical validations post-CRIT-07 segun corresponda.
