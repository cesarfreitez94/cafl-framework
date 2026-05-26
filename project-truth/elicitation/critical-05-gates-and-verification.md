# CRIT-05: Gates And Verification

Status: approved

## Session Objective

- [accepted] Definir el modelo conceptual de gates verificables para avance, bloqueo, replanificacion, deuda, rework, escalamiento y cierre tecnico, sin crear gates finales ejecutables, schemas finales, commands, scripts ni runtime OpenCode.
- [accepted] CRIT-05 aprueba un modelo conceptual de gates y verificacion; no aprueba implementacion fisica, validators, storage, commands, agents ejecutables ni configuracion OpenCode.

## Context

- [accepted] CRIT-01 Intent and Scope esta approved.
- [accepted] CRIT-02 Operating Flow esta approved.
- [accepted] CRIT-03 Agent Responsibilities esta approved.
- [accepted] CRIT-04 Contracts esta approved como modelo contractual conceptual.
- [accepted] `framework/GATE_CATALOG.md` existe como catalogo preliminar y evidencia secundaria; no es autoridad oficial.
- [accepted] CRIT-02/CRIT-03 aprobaron shift-left verification, risk-based testing, testing aplicable, rework acotado y seguridad/riesgo/compliance como responsabilidad explicita.
- [accepted] CRIT-04 aprobo que contratos no equivalen a gates; CRIT-05 define verificacion, severidad y acciones por fallo.
- [accepted] El rework default es 2 ciclos; excepciones y tercer ciclo significativo requieren justificacion y escalamiento.

## Owner Approval

- [accepted] El owner aprobo las recomendaciones de CRIT-05 Gates and Verification Technical Elicitation con ajustes obligatorios.
- [accepted] Ajuste obligatorio 1: la escala principal de severidades sera `blocker`, `critical`, `high`, `medium`, `low` y `warning/info`.
- [accepted] Ajuste obligatorio 2: los gates V1 se separan entre gates minimos independientes, checks transversales obligatorios dentro de gates y gates condicionales por riesgo o evento.
- [accepted] Ajuste obligatorio 3: deuda tecnica menor puede aceptarse si es documentada, acotada, con impacto conocido y aceptacion explicita; deuda funcional sobre alcance comprometido no permite declarar produccion tecnica.
- [accepted] Ajuste obligatorio 4: CRIT-06 define modelo logico de estado/evidencia/logs/trazabilidad y CRIT-07 define implementacion fisica/runtime/schemas/validators/commands/SDK/server/scripts/permissions/OpenCode/Odoo.

## Approved Decisions

- [accepted] DEC-CRIT05-01: CAFL V1 usara modelo hibrido de gates: gates minimos por transicion critica, checks transversales obligatorios dentro de gates y gates condicionales por riesgo o evento.
- [accepted] DEC-CRIT05-02: Gate recommendation, gate verification y gate decision quedan separados; una recomendacion LLM no equivale a decision de gate.
- [accepted] DEC-CRIT05-03: Los gates normales pueden ser decididos por orquestacion segun evidencia; owner decide decisiones criticas, excepciones relevantes, deuda significativa, replan/reduce scope critico y cierre final de modulo.
- [accepted] DEC-CRIT05-04: Las severidades aprobadas son `blocker`, `critical`, `high`, `medium`, `low` y `warning/info`.
- [accepted] DEC-CRIT05-05: Las acciones por fallo aprobadas son `continue`, `continue with warning`, `rework`, `block`, `escalate to owner`, `reject/stop`, `accept technical debt` y `replan/reduce scope`.
- [accepted] DEC-CRIT05-06: Los gates minimos independientes V1 son PRD Sufficiency Gate, SDD Sufficiency Gate, Task Packet / DoR Gate, QA/Testing Gate, Evidence/Closure Gate y Module Technical Readiness Gate.
- [accepted] DEC-CRIT05-07: Context Routing / Token Budget y Security/Risk/Compliance Triage son checks transversales obligatorios dentro de gates, no gates independientes formales V1.
- [accepted] DEC-CRIT05-08: Security/Data/Access Gate, Debt Acceptance Gate y Rework Limit Gate son gates condicionales activados por riesgo, fallo, deuda, seguridad/datos/compliance o evento de rework.
- [accepted] DEC-CRIT05-09: DoD verificable se define por nivel: task, capability/feature y module; ningun nivel puede cerrarse solo por opinion del ejecutor.
- [accepted] DEC-CRIT05-10: Testing suficiente/aplicable se define bajo risk-based testing, con minimo obligatorio y pruebas condicionales segun tipo de modulo, alcance, riesgo, entorno Odoo y cambio realizado.
- [accepted] DEC-CRIT05-11: Shift-left verification se aplicara en transiciones criticas antes de llegar al cierre final.
- [accepted] DEC-CRIT05-12: Evidencia reproducible es requisito conceptual para gates; narrativa LLM puede explicar, pero no sustituye evidencia verificable.
- [accepted] DEC-CRIT05-13: Seguridad/riesgo/compliance queda como criterio transversal obligatorio; review especializado se activa por triggers de riesgo, datos, seguridad, normativa, compliance o severidad.
- [accepted] DEC-CRIT05-14: Deuda tecnica menor puede aceptarse condicionalmente; deuda funcional sobre alcance comprometido, omision de testing minimo, evidencia, documentacion minima, instalacion/carga o riesgo critico no son deuda aceptable para produccion tecnica.
- [accepted] DEC-CRIT05-15: Rework default queda limitado a 2 ciclos bajo el mismo alcance; tercer ciclo significativo requiere justificacion, evidencia y escalamiento.
- [accepted] DEC-CRIT05-16: CRIT-05 no define storage, IDs finales, evidence log, gate log, schemas finales, validators finales, commands, scripts, runtime OpenCode ni entorno Odoo.

## Severity Model

| Severity | Meaning | Typical consequence |
| --- | --- | --- |
| blocker | Impide avanzar sin violar alcance, contexto, seguridad, compliance, DoD o evidencia minima. | block, rework, escalate to owner, reject/stop |
| critical | Riesgo grave legal/compliance/seguridad/datos/arquitectura o contradiccion normativa/fuente insuficiente que puede invalidar produccion tecnica. | block, escalate to owner, reject/stop, replan/reduce scope |
| high | Falla relevante que afecta funcionalidad, tests aplicables, calidad tecnica o trazabilidad, pero puede corregirse sin reabrir decision critica. | rework, block si persiste, escalate si supera limite |
| medium | Falla corregible o deuda tecnica menor potencial que requiere registro, rework focalizado o warning controlado. | rework, continue with warning, accept technical debt si aplica |
| low | Observacion menor sin impacto inmediato en DoD, seguridad, testing minimo o alcance comprometido. | continue, continue with warning, registrar pendiente menor |
| warning/info | Informacion, advertencia o mejora no bloqueante. | continue, registrar como informacion o mejora futura |

## V1 Gate Model

### Minimum Independent Gates

- [accepted] PRD Sufficiency Gate.
- [accepted] SDD Sufficiency Gate.
- [accepted] Task Packet / DoR Gate.
- [accepted] QA/Testing Gate.
- [accepted] Evidence/Closure Gate.
- [accepted] Module Technical Readiness Gate.

### Mandatory Transversal Checks Inside Gates

- [accepted] Context Routing / Token Budget.
- [accepted] Security/Risk/Compliance Triage.

### Conditional Gates By Risk Or Event

- [accepted] Security/Data/Access Gate.
- [accepted] Debt Acceptance Gate.
- [accepted] Rework Limit Gate.

## Gate Recommendation, Verification And Decision

| Concept | Definition | Authority rule |
| --- | --- | --- |
| Gate recommendation | Juicio o propuesta de un agent/reviewer/QA sobre si avanzar, bloquear, retrabajar, escalar o aceptar deuda. | No decide por si sola; debe declarar evidencia y riesgos. |
| Gate verification | Comprobacion conceptual o reproducible de criterios, pruebas, artefactos, fuentes, logs, reportes o evidencias. | Debe ser independiente del ejecutor cuando exista riesgo relevante. |
| Gate decision | Resultado autorizado del gate: continue, warning, rework, block, escalate, reject/stop, accept debt o replan. | Orquestacion decide gates normales; owner decide decisiones criticas y cierre final del modulo. |

## Action Model

| Action | Meaning | Allowed when |
| --- | --- | --- |
| continue | Avanzar sin observaciones bloqueantes. | Criterios y evidencia suficiente estan cumplidos. |
| continue with warning | Avanzar con advertencia no bloqueante. | El impacto es bajo o informativo y no afecta DoD ni riesgo critico. |
| rework | Retornar a correccion bajo el mismo alcance. | Existe falla corregible con evidencia y criterio claro. |
| block | Detener avance hasta resolver causa. | Falta contexto critico, evidencia minima, testing minimo, seguridad/compliance o DoD. |
| escalate to owner | Elevar decision critica al owner. | Riesgo critico, tercer ciclo significativo, deuda relevante, cambio de alcance o cierre final. |
| reject/stop | Rechazar o cortar una tarea/entrega. | La tarea no es viable, viola restricciones, excede rework o carece de base suficiente. |
| accept technical debt | Aceptar deuda tecnica menor documentada. | Impacto conocido, no critica, con aceptacion explicita y condicion de pago. |
| replan/reduce scope | Cambiar plan o reducir alcance. | Funcionalidad comprometida no puede completarse sin decision explicita y trazable. |

## Conceptual Gate Matrix

| Gate | Type | Purpose | Applies to | Trigger | Recommended by | Verified by | Decided by | Evidence required | Possible severity | Possible actions | Related contract | Related future CRIT |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| PRD Sufficiency Gate | minimum independent | Validar PRD ligero suficiente antes de diseno tecnico. | module, capability/feature | Fin de elicitacion funcional. | Analisis funcional | Receptor tecnico/orquestacion | Orquestacion; owner si alcance critico | PRD, scope in/out, criterios, dudas, riesgos, decisiones owner si aplica | blocker, critical, high, medium | rework, block, escalate to owner, continue | Idea -> PRD | CRIT-06 |
| SDD Sufficiency Gate | minimum independent | Validar diseno tecnico antes de codigo. | capability/feature, module | PRD suficiente/aprobado. | Arquitecto Odoo | QA/riesgo/receptor | Orquestacion; owner si decision irreversible | SDD, ADR si aplica, fuentes Odoo, riesgos, estrategia de tests | blocker, critical, high, medium | rework, block, escalate to owner, replan/reduce scope | PRD -> SDD | CRIT-06, CRIT-07 |
| Task Packet / DoR Gate | minimum independent | Confirmar tarea ejecutable sin inventar. | task | Antes de ejecucion. | Productor/orquestacion | Receptor/validator | Orquestacion | Packet, fuentes, outputs, acceptance criteria, evidence expected, blockers o `none` | blocker, high, medium, low | rework, block, continue | Task/Context Packet + DoR | CRIT-06, CRIT-07 |
| QA/Testing Gate | minimum independent | Confirmar testing suficiente/aplicable. | task, capability/feature, module | Despues de implementacion o antes de cierre. | QA | QA independiente y ejecucion reproducible futura | QA/orquestacion; owner si excepcion critica | Plan, resultados, logs/reportes, fallas, justificacion de no aplica | blocker, critical, high, medium, low | rework, block, accept technical debt, escalate to owner, continue | QA/Testing | CRIT-07 |
| Evidence/Closure Gate | minimum independent | Validar cierre verificable de unidad. | task, capability/feature | Antes de handoff o cierre parcial. | Evidence/closure | QA/orquestacion | Orquestacion | Evidencia, docs, pruebas, riesgos, pendientes, deuda aceptada o `none` | blocker, high, medium, low, warning/info | block, rework, continue with warning, continue | Evidence/Closure | CRIT-06 |
| Module Technical Readiness Gate | minimum independent | Decidir si el modulo esta listo para produccion tecnica. | module | Cierre final del modulo. | QA/orquestacion | QA, risk/compliance, evidence | Owner | Reporte final, tests aplicables, instalacion/carga, docs, evidencia, deuda aceptada o `none` | blocker, critical, high, medium, low | continue, block, rework, reject/stop, replan/reduce scope | Evidence/Closure, Escalation/Owner Decision | CRIT-06, CRIT-07 |
| Context Routing / Token Budget | mandatory transversal check | Evitar contexto indebido, fuente no autorizada o exceso de tokens. | all gates/contracts | Cada gate o packet relevante. | Context routing capability | Orquestacion/control futuro | Gate decision owner segun gate contenedor | Fuentes usadas/excluidas, budget class, excepciones | high, medium, low, warning/info | continue, continue with warning, rework, block, escalate to owner | Context Routing / Token Budget | CRIT-06, CRIT-07 |
| Security/Risk/Compliance Triage | mandatory transversal check | Mantener seguridad, riesgo y compliance visibles. | all gates/contracts | PRD, SDD, task, QA y closure. | Reviewer/checklist | Reviewer especializado si aplica | Gate decision owner segun gate contenedor; owner si critico | Risk flags, fuentes, limites, decision requerida si aplica | blocker, critical, high, medium | block, rework, escalate to owner, reject/stop | Security/Risk/Compliance Review | CRIT-06, CRIT-07 |
| Security/Data/Access Gate | conditional | Validar permisos, datos, accesos, exposicion o compliance especifico. | conditional task/capability/module | Modelos, ACL, record rules, datos sensibles, portal, API, normativa. | Security/risk reviewer | QA/reviewer especializado | Orquestacion; owner si high/critical | ACL/rules review, pruebas de acceso, riesgos datos/compliance | blocker, critical, high | block, rework, escalate to owner, reject/stop | Security/Risk/Compliance Review | CRIT-06, CRIT-07 |
| Debt Acceptance Gate | conditional | Decidir si una falla puede registrarse como deuda tecnica aceptable. | task, capability/feature, module | Falla no critica o recorte propuesto. | QA/orquestacion | Reviewer/orquestacion | Owner si high o modulo; orquestacion si menor | Descripcion, impacto, severidad, responsable, condicion de pago, aceptacion | high, medium, low, warning/info | accept technical debt, replan/reduce scope, block | Evidence/Closure, Escalation/Owner Decision | CRIT-06 |
| Rework Limit Gate | conditional | Evitar loops infinitos y detectar tercer ciclo significativo. | task | Falla tras ciclos de rework o cambio de alcance oculto. | QA/orquestacion | Orquestacion/control futuro | Orquestacion; owner para tercer ciclo significativo | Causa, ciclos, cambios, evidencia actualizada, recomendacion | blocker, high, medium | rework, replan/reduce scope, escalate to owner, reject/stop | Rework, Escalation/Owner Decision | CRIT-06 |

## Candidate DoD By Level

| Level | Required evidence | Required testing | Required documentation | Security/compliance requirement | Who can close | Owner approval required |
| --- | --- | --- | --- | --- | --- | --- |
| task | Packet ready, cambios realizados, criterios cumplidos, evidencia de ejecucion o revision, blockers resueltos o `none`. | Tests aplicables al cambio; al menos validacion focalizada y evidencia si no hay test automatizado. | Nota breve de que cambio, por que y limites si aplica. | Risk flags revisados; review si toca seguridad, datos, permisos o compliance. | QA/orquestacion, no builder. | conditional |
| capability/feature | Tareas cerradas, criterios funcionales cumplidos, evidencia agregada, riesgos/deuda visibles. | Tests de reglas de negocio, integracion funcional y UI si aplica. | Descripcion funcional/tecnica breve, uso, limites y validacion. | Review proporcional si afecta datos, permisos, normativa o procesos criticos. | QA/orquestacion con receptor funcional/tecnico. | conditional |
| module | PRD/SDD trazables, capacidades cerradas, reporte final, evidencia reproducible, deuda aceptada o `none`. | Instalacion/carga/update, backend, seguridad/accesos, reglas de negocio, UI/OWL/Playwright/migracion/performance si aplica. | Documentacion de modulo, uso, validacion, limites, riesgos y operacion tecnica. | Seguridad/riesgo/compliance sin blockers criticos; excepciones aprobadas. | Owner con recomendacion QA/orquestacion. | yes |

## Testing Sufficient / Applicable

- [accepted] Testing es obligatorio y no debe omitirse ni minimizarse.
- [accepted] `Todos los tests aplicables` significa minimo obligatorio mas pruebas condicionales segun alcance, riesgo, tipo de cambio y entorno Odoo disponible.
- [accepted] El minimo conceptual incluye instalacion/carga o actualizacion del modulo cuando exista entorno Odoo, tests backend aplicables, validacion de reglas de negocio, validacion de seguridad/accesos cuando aplique, evidencia de ejecucion y documentacion de pruebas.
- [accepted] Tests UI/OWL, tours, Playwright, migracion/update, performance basica o pruebas manuales documentadas son condicionales segun alcance y riesgo.
- [accepted] Si una prueba no aplica, debe justificarse; si una prueba minima no puede ejecutarse por falta de entorno, no se debe declarar produccion tecnica sin excepcion explicita y trazable.
- [accepted] BDD formal, ATDD parcial, TDD estricto o planificacion ligera de pruebas se aplican por valor, riesgo y complejidad; TDD estricto universal sigue rechazado.

## Shift-Left Verification

- [accepted] La verificacion se aplica temprano en PRD, SDD, Task Packet / DoR, QA/Testing y Evidence/Closure.
- [accepted] El objetivo es detectar defectos de alcance, contexto, fuentes, seguridad, compliance, diseno, testing y evidencia antes del cierre final.
- [accepted] Shift-left verification no significa microgate por cada microcambio; se aplica en transiciones criticas.

## Security, Risk And Compliance

- [accepted] Seguridad/riesgo/compliance es criterio transversal obligatorio en gates.
- [accepted] Review especializado se activa por datos sensibles, permisos/accesos, normativa, riesgo legal/compliance, contradiccion normativa, fuente oficial insuficiente, seguridad critica o severidad high/critical/blocker.
- [accepted] Riesgo critico legal/compliance, contradiccion normativa o fuente oficial insuficiente bloquea o escala; no puede tratarse como warning para produccion tecnica.
- [accepted] V1 no aprueba motor legal completo ni automatizacion legal autonoma.

## Acceptable Debt

- [accepted] Se permite deuda tecnica menor si es documentada, acotada, con impacto conocido, responsable, condicion de pago y aceptacion explicita.
- [accepted] No se permite deuda funcional sobre alcance comprometido para declarar produccion tecnica.
- [accepted] No se permite como deuda aceptable: omision de testing minimo, omision de evidencia, omision de documentacion minima, riesgo critico de seguridad/datos, riesgo critico legal/compliance, instalacion/carga no validada cuando es aplicable, o DoD falso/incompleto.
- [accepted] Si una funcionalidad comprometida no se completa, debe ir a rework, block, escalate to owner o replan/reduce scope aprobado.
- [accepted] Solo puede salir del alcance mediante replan/reduce scope explicito y trazable.

## Rework And Escalation

- [accepted] Rework default es 2 ciclos por tarea bajo el mismo alcance.
- [accepted] Tercer ciclo significativo requiere justificacion, evidencia, diagnostico de causa y escalamiento.
- [accepted] Se escala al owner por riesgo critico, cambio de alcance, deuda significativa, excepcion a testing/DoD, tercer ciclo significativo, decision irreversible, recorte por plazo y cierre final del modulo.
- [accepted] Una tarea puede cortarse o replanificarse si falla repetidamente, revela alcance incorrecto, carece de contexto suficiente o no tiene entorno verificable.

## Boundaries With CRIT-06 And CRIT-07

- [accepted] CRIT-06 debe definir modelo logico de estado, evidencia, logs, IDs, trazabilidad, persistencia conceptual, decision log, evidence log, source log, context log, gate log y rework history.
- [accepted] CRIT-07 debe definir implementacion fisica/runtime, schemas finales, validators, commands, SDK/server/scripts, permissions, OpenCode setup, rutas source-vs-runtime, entorno Odoo, ejecucion reproducible y tooling operativo.
- [accepted] CRIT-05 prepara CRIT-06 y CRIT-07, pero no los resuelve.

## Non-Goals Confirmed

- [accepted] No crear gates finales ejecutables.
- [accepted] No crear schemas finales.
- [accepted] No crear validators finales.
- [accepted] No crear commands.
- [accepted] No crear scripts.
- [accepted] No crear agents ejecutables.
- [accepted] No configurar OpenCode.
- [accepted] No configurar OpenSpec.
- [accepted] No implementar runtime.
- [accepted] No definir storage/evidence log/gate log final.
- [accepted] No elevar `framework/` a verdad oficial.

## Acceptance Criteria Result

- [accepted] CRIT-05 queda aprobado documentalmente como modelo conceptual de gates y verificacion.
- [accepted] La escala de severidades queda como `blocker`, `critical`, `high`, `medium`, `low` y `warning/info`.
- [accepted] Los gates V1 quedan separados en gates minimos independientes, checks transversales obligatorios y gates condicionales.
- [accepted] La deuda tecnica menor queda permitida condicionalmente.
- [accepted] La deuda funcional no queda permitida para produccion tecnica sobre alcance comprometido.
- [accepted] Testing minimo, evidencia, documentacion minima, instalacion/carga, seguridad critica y compliance critico no pueden omitirse como deuda aceptable.
- [accepted] CRIT-06 define modelo logico de estado/evidencia/logs/trazabilidad.
- [accepted] CRIT-07 define implementacion fisica/runtime/schemas/validators/commands/SDK/server/scripts/permissions/OpenCode/Odoo.
- [accepted] CRIT-06 y CRIT-07 quedan preparados, no resueltos.
