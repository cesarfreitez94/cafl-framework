# Target Operating Model

Status: approved

Aprobado explicitamente por el owner (2026-05-27). Esta aprobacion habilita el Implementation Blueprint sin aprobarlo, ni al backlog, ni a la implementacion.

## Regla De Uso

- [accepted] Este Target Operating Model define como opera CAFL V1 de punta a punta a nivel conceptual/operativo.
- [accepted] Este documento usa `project-truth/` como unica fuente de verdad aprobada.
- [accepted] En caso de conflicto, prevalece este orden de autoridad: `decisions/accepted.md`, `decisions/rejected.md`, `decisions/superseded.md`, `critical-map.md`, `decisions/pending.md`, archivos individuales de elicitacion, `risks.md` y `glossary.md` como soporte.
- [accepted] Este TOM no crea runtime, commands reales, schemas fisicos finales, validators reales, scripts, backlog tecnico, Blueprint, RAG/base vectorial ni configuracion OpenCode.
- [accepted] Este TOM no implementa nada y no convierte recomendaciones en artefactos ejecutables.
- [accepted] Este TOM es input directo para el Implementation Blueprint; no lo reemplaza.
- [accepted] El TOM queda aprobado solo cuando todos sus acceptance criteria estan satisfechos y el owner lo marca explicitamente como `approved`.
- [accepted] El contenido operativo queda elaborado desde CRIT-01..CRIT-07 y aprobado explicitamente por el owner.
- [accepted] No se registran conflictos de autoridad que obliguen a resolver por criterio propio durante esta elaboracion.

## Proposito

- [accepted] Responder como opera CAFL V1 de punta a punta sin ambiguedad operativa critica, de modo que el Implementation Blueprint pueda arrancar desde una base validada.
- [accepted] Definir el modelo operativo generico aplicable a todos los modulos CAFL V1 dentro del dominio Odoo.
- [accepted] Instanciar el modelo sobre el piloto V1 confirmado de solicitudes internas / aprobaciones simples sin convertirlo en PRD final, SDD final ni backlog.
- [accepted] Separar claramente lo operativo del TOM de lo fisico/tecnico que queda para Blueprint o technical validation/spike.

## Fuentes Autoritativas Usadas

- [accepted] `project-truth/TOM.md` como specification / working contract inicial del TOM.
- [accepted] `project-truth/README.md`.
- [accepted] `project-truth/critical-map.md`.
- [accepted] `project-truth/decisions/accepted.md`.
- [accepted] `project-truth/decisions/pending.md`.
- [accepted] `project-truth/decisions/rejected.md`.
- [accepted] `project-truth/decisions/superseded.md`.
- [accepted] `project-truth/risks.md`.
- [accepted] `project-truth/glossary.md`.
- [accepted] `project-truth/elicitation/critical-01-intent-and-scope.md`.
- [accepted] `project-truth/elicitation/critical-02-operating-flow.md`.
- [accepted] `project-truth/elicitation/critical-03-agent-responsibilities.md`.
- [accepted] `project-truth/elicitation/critical-04-contracts.md`.
- [accepted] `project-truth/elicitation/critical-05-gates-and-verification.md`.
- [accepted] `project-truth/elicitation/critical-06-state-evidence-traceability.md`.
- [accepted] `project-truth/elicitation/critical-07-implementation-risks-resources.md`.
- [accepted] No se usaron fuentes fuera de `project-truth/` para crear contenido operativo del TOM.

## Alcance Operativo V1

- [accepted] CAFL es un framework/plataforma operativo sobre OpenCode para desarrollar soluciones empresariales Odoo con asistencia de IA durante el ciclo de vida.
- [accepted] El usuario inicial de CAFL es el owner.
- [accepted] Odoo es el unico dominio objetivo de V1 y el target aprobado es Odoo 18.
- [accepted] V1 debe demostrar un flujo end-to-end verificable desde idea del owner hasta modulo Odoo 18 listo para produccion tecnica.
- [accepted] `Listo para produccion tecnica` significa funcional, instalable/cargable en Odoo, testeado, documentado, seguro segun alcance, auditable, revisable y con evidencia suficiente; no significa despliegue real en servidor productivo.
- [accepted] CAFL V1 usa modelo hibrido progresivo sobre OpenCode: agents para razonamiento, commands candidatos para entradas repetibles, scripts/CLI/validators locales candidatos para control deterministico, rules/config para invariantes y skills/playbooks para conocimiento on-demand.
- [accepted] V1 no es agents-only y no puede ser puramente manual o solo narrativa.
- [accepted] La automatizacion minima suficiente V1 debe cubrir o semi-cubrir validacion estructural de packets/contratos/gates/evidencia, DoR, trazabilidad minima, logs/estado/evidencia, install/update/test execution de Odoo 18, captura de evidencia y source policy / Knowledge Gap basico.
- [accepted] La unidad de control operativa es jerarquica: `module -> capability/feature -> task`.
- [accepted] Toda fase/tarea debe tener objetivo, alcance, salida, criterio de aceptacion, evidencia minima, condicion de bloqueo y cierre verificable.

## Roles Y Capacidades

### Principios De Responsabilidad

- [accepted] Las responsabilidades son capacidades operativas consolidadas, no agentes finales separados.
- [accepted] Un mecanismo puede ser human, agent, command, SDK/server/script, rule/config/skill o mixed.
- [accepted] Agents son adecuados para juicio, razonamiento, analisis, diseno, generacion, diagnostico, revision y redaccion.
- [accepted] Commands son entradas repetibles candidatas para estructurar fases y tareas; no son autoridad final de gate, estado ni cierre.
- [accepted] Scripts/CLI/validators/control deterministico son candidatos para validar estructura, ejecutar checks, registrar evidencia, controlar permisos, token budget, DoR/DoD estructural y rework counters; su implementacion queda para Blueprint/spikes.
- [accepted] Para core V1, SDK/server queda fuera; Blueprint debe priorizar OpenCode + commands + scripts/CLI + validators y solo considerar SDK/server con spike favorable posterior y decision owner explicita.
- [accepted] Rules/config son candidatos para invariantes minimos.
- [accepted] Skills/playbooks son candidatos para conocimiento operativo on-demand.
- [accepted] El owner interviene solo en decisiones criticas, no en microgestion operativa.
- [accepted] La narrativa LLM puede explicar, recomendar o resumir, pero nunca constituye estado autoritativo.

### Matriz Operativa De Capacidades

| Capacidad | Mecanismo operativo V1 | Responsabilidades | Limites / no-responsabilidades | Automatico, asistido o humano | Handoff principal |
| --- | --- | --- | --- | --- | --- |
| Owner | Human | Define intencion, responde decisiones criticas, aprueba cambios de alcance, excepciones relevantes, deuda significativa, recortes por plazo y aceptacion final del modulo. | No microgestiona tareas normales ni reemplaza QA, gates o evidencia. | Exclusivamente humano en decisiones criticas. | Recibe decision packs desde orquestacion y devuelve decision registrada. |
| OpenCode | Runtime principal | Entorno de interaccion/ejecucion para asistencia IA, coordinacion operativa, agents y commands candidatos. | No es por si solo estado autoritativo, gate decision, storage final, policy final ni evidencia suficiente. | Asistido; operacion concreta queda para Blueprint/runtime. | Entrega sesiones/salidas a registros, gates y evidencia logica. |
| Coordinacion/orquestacion | Mixed | Coordina flujo, handoffs, estado conceptual, bloqueos, rework, escalamiento y decision de gates normales segun evidencia. | No convierte narrativa LLM en estado real; no decide decisiones criticas ni cierre final del modulo. | Asistido con control deterministico futuro. | Hacia todas las capacidades; escala al owner cuando corresponde. |
| Context routing / token budget | Rule/config/skill + agent + validators futuros | Selecciona contexto minimo, clasifica fuentes autorizadas/secundarias/prohibidas/no relevantes, define budget class y excepciones. | No permite leer todo el repo por defecto ni dejar contexto al criterio libre del ejecutor. | Asistido y semi-automatico cuando exista validator. | Alimenta contratos, packets, gates y context logs. |
| Analisis funcional | Agent + command candidato + owner puntual | Elicita idea, alcance, actores, reglas, criterios de aceptacion, riesgos y produce PRD ligero. | No disena arquitectura tecnica, no escribe codigo, no cierra gates y no inventa decisiones de negocio criticas. | Asistido; owner solo ante decision critica. | PRD ligero hacia PRD Sufficiency Gate y diseno tecnico. |
| Diseno tecnico Odoo | Agent + skills/fuentes oficiales + review | Traduce PRD aprobado en SDD ligero, ADR minimo si aplica, riesgos tecnicos, estrategia de tests y criterios para descomposicion. | No implementa como responsabilidad primaria, no cierra gates finales y no inventa comportamiento Odoo sin fuente suficiente. | Asistido; bloquea por fuente insuficiente o riesgo critico. | SDD hacia SDD Sufficiency Gate, task/context packets, QA/riesgo. |
| Task/context packet / DoR | Mixed | Genera y valida packet obligatorio por unidad verificable; declara objetivo, scope, fuentes, criterios, evidencia, blockers o `none`, handoff y escalation conditions. | El productor no puede autoaprobar DoR; el receptor puede rechazar si no puede ejecutar sin inventar. | Asistido con check estructural futuro. | Packet ready hacia ejecucion; rechazo hacia productor/orquestacion. |
| Construccion Odoo backend | Agent + command candidato + permisos futuros | Implementa backend segun PRD, SDD y packet ready; reporta cambios, riesgos y evidencia local aplicable. | No cambia alcance, no omite SDD/packet, no autocierra y no decide gate. | Asistido; acciones reales quedan para implementacion posterior. | Salida tecnica hacia QA/testing y evidencia. |
| Construccion frontend/OWL condicional | Agent condicional | Implementa OWL/JS/assets/tours solo si PRD/SDD/piloto lo justifican. | No crea frontend avanzado por defecto ni fuera del SDD. | Asistido y condicional. | Hacia QA/testing y evidencia cuando aplique. |
| Verificacion/testing | Mixed | Planifica, diagnostica, ejecuta/verifica pruebas aplicables, revisa resultados y recomienda rework/cierre. | No acepta evidencia solo narrativa; el builder no puede autocerrar. | Asistido para juicio; automatico/semi-automatico para ejecucion/captura cuando exista tooling. | Hacia rework, Evidence/Closure Gate o owner si excepcion critica. |
| Seguridad/riesgo/compliance | Mixed | Mantiene triage transversal, revisa datos/accesos/permisos/compliance, activa review especializado por riesgo y escala riesgo critico. | No se diluye en QA generico; V1 no es motor legal completo. | Asistido; humano exclusivo ante riesgo legal/compliance critico. | Hacia gates, rework, block o owner. |
| Evidence/closure | Mixed | Consolida evidencia, trazabilidad, logs, documentacion, deuda aceptada o `none`, y prepara paquetes de cierre. | No cierra sin tests/evidencia/DoD ni reemplaza aceptacion owner del modulo. | Asistido con captura automatica futura. | Hacia gates de cierre, Module Technical Readiness y owner. |
| Rework/escalamiento | Mixed + control deterministico futuro | Cuenta ciclos, registra causa/evidencia, limita loops, dispara Rework Limit Gate y decision owner cuando corresponde. | No reintenta indefinidamente ni oculta cambio de alcance. | Automatico para contador cuando exista runtime; asistido para diagnostico; humano para excepciones criticas. | Hacia correccion, replan/reduce scope, reject/stop u owner. |
| Commands candidatos | Command + agent | Estandarizan entradas repetibles para elicitar modulo, generar PRD, generar SDD, preparar packet, desarrollar tarea, ejecutar/verificar pruebas, validar gate, registrar evidencia y preparar cierre. | No son commands reales aprobados, no son autoridad final y no sustituyen validators/gates. | Asistido; invocados por owner/orquestacion segun fase futura. | Producen salidas estructuradas para contratos/gates/logs. |
| Scripts/CLI/validators candidatos | Script/control deterministico candidato | Validan estructura, referencias, estados, IDs, trazabilidad minima, evidencia, source policy, Knowledge Gap basico, rework/debt/approval y Odoo 18 execution minima. | No se implementan en TOM; no sustituyen juicio tecnico, gate decision ni aceptacion owner. | Automatico/semi-automatico despues de Blueprint. | Producen resultados reproducibles para gates/evidence logs. |
| Knowledge governance / curation | Mixed + source policy + skills/playbooks | Mantiene source registry logico, knowledge artifacts, Knowledge Gap, Curation Request, Curation Mode y source usage. | No habilita busqueda web libre ni RAG/base vectorial V1. | Asistido; owner/source policy requerido para fuentes externas no autorizadas. | Hacia PRD/SDD/tasks/gates/evidence con source usage trazado. |

### Automatico, Asistido Y Exclusivamente Humano

- [accepted] Automatico o semi-automatico en V1, cuando Blueprint lo materialice: validacion estructural de packets/contratos/gates/evidencia, IDs/referencias/estados, DoR estructural, rework counters, source policy checks, Knowledge Gap basico, logs, captura de evidencia e install/update/test execution Odoo 18 minimo.
- [accepted] Asistido por LLM/agent: elicitacion funcional, PRD, SDD, division de tareas, construccion, diagnostico QA, revision de riesgos, redaccion de documentacion y recomendaciones de gate.
- [accepted] Exclusivamente humano: aprobacion de TOM final, cambios de alcance, falta de contexto critico no resoluble por fuentes autorizadas, riesgo legal/compliance critico, contradiccion normativa, riesgo alto de seguridad/datos, decision arquitectonica irreversible, excepcion a testing/DoD, tercer ciclo significativo de rework, deuda significativa, recorte por plazo y aceptacion final del modulo.

## Flujo Operativo Punta A Punta

### Invariantes Del Flujo

- [accepted] El flujo minimo es: idea/entrada -> elicitacion -> PRD ligero -> SDD ligero -> planificacion de capabilities/tareas -> task/context packet + DoR -> construccion -> verificacion/testing -> documentacion/evidencia -> cierre tecnico.
- [accepted] PRD y SDD son obligatorios en version ligera.
- [accepted] Ninguna unidad operativa inicia sin task/context packet y DoR minimo.
- [accepted] Context routing y token budget son obligatorios por contrato y packet.
- [accepted] Todo contrato debe declarar producer, consumer, validator, inputs, outputs, contexto, token budget, restricciones, criterios de suficiencia, rechazo, evidencia, blockers, handoff, version y trazabilidad.
- [accepted] Contratos V1 always-required: Base Contract Envelope, Idea -> PRD, PRD -> SDD, SDD -> Task/Context Packet, Task/Context Packet + DoR, Task Execution, QA/Testing, Evidence/Closure y Context Routing / Token Budget.
- [accepted] Contratos V1 conditional-required: Security/Risk/Compliance Review, Rework, Escalation/Owner Decision y Mechanism Execution Profile.
- [accepted] Gates minimos independientes V1: PRD Sufficiency Gate, SDD Sufficiency Gate, Task Packet / DoR Gate, QA/Testing Gate, Evidence/Closure Gate y Module Technical Readiness Gate.
- [accepted] Checks transversales obligatorios dentro de gates: Context Routing / Token Budget y Security/Risk/Compliance Triage.
- [accepted] Gates condicionales: Security/Data/Access Gate, Debt Acceptance Gate y Rework Limit Gate.
- [accepted] Gate recommendation, gate verification y gate decision estan separados.
- [accepted] Orquestacion decide gates normales segun evidencia; owner decide decisiones criticas y cierre final del modulo.

### Fases, Evidencia Y Handoffs

| Fase | Entrada | Ejecuta | Valida | Salida | Evidencia minima | Bloquea si | Condicion de avance | Handoff siguiente |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1. Idea intake | Idea breve del owner, objetivo inicial, restricciones conocidas. | Owner + analisis funcional + orquestacion. | Orquestacion. | Intake trazado, objetivo inicial, dudas, contexto requerido. | Registro de idea, preguntas iniciales, decision/context log si aplica. | Objetivo ambiguo critico, alcance imposible, falta de contexto que impide elicitar. | Existe base suficiente para elicitar PRD sin inventar. | Elicitacion funcional / PRD. |
| 2. PRD ligero | Intake, respuestas owner, contexto autorizado y criterios de alcance. | Analisis funcional asistido. | Receptor tecnico/orquestacion; owner si alcance critico. | PRD ligero con scope in/out, actores, reglas, criterios de aceptacion, riesgos y dudas bloqueantes. | PRD, decisiones owner, supuestos permitidos, riesgos, source/context usage. | Falta alcance, regla critica, aceptacion, riesgo legal/compliance/seguridad/datos o decision owner. | PRD Sufficiency Gate puede verificar suficiencia. | PRD Sufficiency Gate. |
| 3. PRD Sufficiency Gate | PRD ligero y evidencia de elicitacion. | Recomendacion de analisis funcional. | Orquestacion/receptor tecnico; owner si decision critica. | Gate decision: continue, rework, block o escalate. | Gate log, PRD, riesgos, blockers o `none`, decisiones owner si aplica. | PRD no permite disenar sin inventar o contiene blocker critico. | Gate decide `continue`. | SDD ligero. |
| 4. SDD ligero | PRD suficiente, fuentes Odoo/knowledge artifacts autorizados, restricciones. | Diseno tecnico Odoo asistido. | QA/riesgo/receptor tecnico. | SDD ligero, ADR minimo si aplica, estrategia tecnica y tests, riesgos. | SDD, source usage, decisiones tecnicas, riesgos, contexto excluido si aplica. | Fuente Odoo insuficiente, ambiguedad tecnica critica, riesgo de seguridad/datos/compliance, decision arquitectonica irreversible sin owner. | SDD Sufficiency Gate puede verificar. | SDD Sufficiency Gate. |
| 5. SDD Sufficiency Gate | SDD, PRD, fuentes usadas, riesgos y estrategia de tests. | Recomendacion de arquitecto. | QA/riesgo/receptor; orquestacion decide normal, owner si irreversible. | Gate decision: continue, rework, block, escalate o replan. | Gate log, SDD, ADR si aplica, source usage, risk flags. | Diseno no implementable, fuentes insuficientes, riesgos criticos o testing no planificable. | Gate decide `continue`. | Descomposicion en capabilities/tasks. |
| 6. Capabilities/tasks y task/context packets | PRD, SDD, gates previos, riesgos, constraints. | Arquitecto + orquestacion + context routing. | Receptor/validator de cada packet. | Jerarquia module -> capability/feature -> task y packets candidatos. | Contract/packet registry, context log, razon de division, dependencias, blockers o `none`. | Tareas no verificables, alcance mezclado, contexto insuficiente, blockers no declarados. | Cada tarea tiene packet validable. | Task Packet / DoR Gate. |
| 7. Task Packet / DoR Gate | Packet con objetivo, scope, fuentes, criterios, evidencia, blockers o `none`, escalation conditions. | Productor/orquestacion recomienda. | Receptor o validator; orquestacion decide. | Packet ready o rechazo DoR. | DoR decision, packet versionado conceptualmente, fuentes autorizadas/prohibidas, budget class. | Campos minimos ausentes, consumidor no puede ejecutar sin inventar, evidencia esperada no verificable. | Gate decide `continue` y packet queda ready. | Ejecucion de tarea. |
| 8. Ejecucion de tarea | Packet ready, SDD, restricciones, fuentes autorizadas y permisos aplicables. | Builder/capacidad ejecutora. | QA, arquitecto o reviewer aplicable. | Cambio tecnico/documental esperado y reporte de ejecucion. | Artefactos tocados, razon de cambio, riesgos, pruebas locales si aplica, source/context usage. | Scope creep, fuente insuficiente, permisos ambiguos, Knowledge Gap, riesgo critico o cambio de alcance. | Salida cumple packet y puede ser testeada. | QA/Testing Gate o rework si falla temprano. |
| 9. QA/Testing Gate | Salida de tarea/capability, criterios, test strategy, entorno disponible. | QA + ejecucion/captura reproducible futura. | QA independiente/orquestacion; owner si excepcion critica. | Resultado QA, fallas, recomendaciones, rework o avance. | Plan/resultados/logs/reportes, justificacion de no aplica, evidencia de install/update/test cuando aplique. | Testing minimo no ejecutado, evidencia ausente, falla critica, autocierre del builder. | Gate decide `continue`, `continue with warning` permitido o rework controlado. | Evidence/Closure o Rework. |
| 10. Evidence/Closure Gate por task/capability | Resultados QA, cambios, docs, riesgos, decisiones, deuda o `none`. | Evidence/closure + orquestacion. | QA/orquestacion; owner condicional. | Paquete de cierre operativo de task/capability. | Evidence log, gate log, docs minimas, riesgos/deuda, rework history si aplica. | DoD no demostrado, evidencia/documentacion minima ausente, deuda funcional, blocker abierto. | Gate decide cierre o warning no bloqueante permitido. | Siguiente task/capability o cierre de modulo. |
| 11. Rework controlado | Falla de gate/QA/evidencia, criterio incumplido, ciclo actual. | Orquestacion + QA/reviewer + ejecutor. | QA/reviewer y orquestacion; owner en tercer ciclo significativo o cambio de alcance. | Correccion, nueva evidencia, rework log o escalation. | Causa, severidad, ciclo, cambios, evidencia previa/nueva. | Tercer ciclo significativo sin owner, cambio de alcance oculto, causa no diagnosticada. | Falla corregida dentro de limite o owner decide excepcion/replan. | QA/Testing Gate, replan/reduce scope o owner. |
| 12. Module Technical Readiness Gate | Capabilities cerradas, evidencia agregada, docs, tests, riesgos/deuda. | QA/orquestacion/evidence closure recomiendan. | QA, seguridad/riesgo/compliance y owner. | Decision final de produccion tecnica: ready, block, rework, reject/stop o replan/reduce scope. | Reporte final, tests aplicables, install/update/test Odoo 18, docs, evidencia, deuda aceptada o `none`, approvals. | Testing/evidencia/documentacion minima ausente, deuda funcional, riesgo critico, instalacion/carga aplicable no validada. | Owner acepta modulo final como listo para produccion tecnica. | Cierre tecnico del modulo o replan/rework. |
| 13. Knowledge governance transversal | Necesidad de fuente/conocimiento en PRD, SDD, task, gate, test o evidence. | Knowledge governance/curation + owner/source policy si aplica. | Source policy, steward, owner cuando no hay fuente aprobada. | Source usage, artifact autorizado o Knowledge Gap + Curation Request. | Source registry entry, snapshot/version, artifact/pack, source usage log, Knowledge Gap si aplica. | Conocimiento autorizado insuficiente, fuente prohibida necesaria, source policy insuficiente. | Conocimiento autorizado suficiente o owner/source policy aprueba curacion. | Fase solicitante retoma con fuente/artifact trazado. |

### Reglas Para Evitar Trabajo Doble Documental

- [accepted] Cada artefacto existe para controlar ejecucion, validacion, trazabilidad o cierre; no para duplicar manualmente informacion.
- [accepted] Si un dato aparece en narrativa y en registro estructurado, una representacion debe ser autoritativa y la otra derivada o referenciada.
- [accepted] PRD, SDD y packets contienen la definicion operativa minima; logs registran eventos, decisiones, evidencia y cambios de estado, no reescriben todo el artefacto.
- [accepted] Los reportes narrativos LLM son explicacion secundaria y deben apuntar a IDs, gates, evidencia, decisiones y fuentes.
- [accepted] La evidencia se genera como subproducto del flujo: ejecucion, gates, rework, curacion, source usage y cierre producen registros/evidencias al ocurrir, no como reconstruccion manual posterior.

### Estado Autoritativo Y Narrativa LLM

- [accepted] Estado autoritativo vive en registros logicos versionables y trazables: status changes, decisions, contracts/packets, gates, evidence, sources, context, rework, debt, approvals, knowledge artifacts y source usage.
- [accepted] Una recomendacion LLM no aprueba un gate.
- [accepted] Una respuesta narrativa no reemplaza evidence log, gate log, contract/packet registry, source usage ni approval log.
- [accepted] El cierre no puede depender solo de opinion del ejecutor.

## Control Y Bloqueos

### Severidades Y Acciones

- [accepted] La escala principal de severidad es `blocker`, `critical`, `high`, `medium`, `low` y `warning/info`.
- [accepted] Acciones permitidas: `continue`, `continue with warning`, `rework`, `block`, `escalate to owner`, `reject/stop`, `accept technical debt` y `replan/reduce scope`.
- [accepted] `continue` solo aplica cuando criterios y evidencia suficiente estan cumplidos.
- [accepted] `continue with warning` solo aplica a impacto bajo, informativo o no bloqueante; no permite omitir DoD, testing minimo, evidencia, documentacion minima, instalacion/carga aplicable, seguridad critica ni compliance critico.
- [accepted] `rework` aplica a fallas corregibles con evidencia y criterio claro bajo el mismo alcance.
- [accepted] `block` aplica cuando avanzar implicaria inventar, violar alcance, omitir evidencia minima, ignorar riesgo critico o cerrar sin DoD.
- [accepted] `escalate to owner` aplica solo a decisiones criticas, no a microgestion operativa.
- [accepted] `reject/stop` aplica cuando la tarea/entrega no es viable, viola restricciones, excede rework o carece de base suficiente.
- [accepted] `accept technical debt` solo aplica a deuda tecnica menor, documentada, acotada, con impacto conocido, responsable, condicion de pago y aceptacion explicita.
- [accepted] `replan/reduce scope` requiere decision explicita y trazable cuando el alcance comprometido no puede completarse.

### Matriz De Bloqueo, Escalamiento Y Rework

| Condicion | Resultado operativo | Evidencia requerida | Owner approval requerido | Siguiente paso |
| --- | --- | --- | --- | --- |
| Falta de contexto critico sobre alcance, compliance, seguridad, arquitectura, datos, pruebas, aceptacion o riesgo relevante. | `block` y, si no puede resolverse con fuente autorizada, `escalate to owner`. | Blocker/context gap, pregunta concreta, impacto y decision requerida. | Si afecta decision critica o falta dato del owner. | Owner decide, se cura fuente o se replanifica. |
| Duda menor sin impacto en DoD, riesgo critico ni alcance. | `continue with warning` o registrar open question no bloqueante. | Warning/info con razon y limitacion. | No. | Avanzar manteniendo trazabilidad. |
| DoR insuficiente. | `block` ejecucion y `rework` del packet. | DoR rejection, campos faltantes, fuente/contexto insuficiente o evidencia no verificable. | Solo si se repite fuera de limite o expone decision critica. | Productor corrige packet; receptor revalida. |
| Contrato/packet invalido. | `block` o `rework`; no inicia tarea. | Contract/packet registry con rechazo y criterio incumplido. | Condicional por riesgo/tercer ciclo/cambio de alcance. | Corregir contrato/packet o escalar. |
| Gate fallido. | Accion segun severidad: warning, rework, block, escalate, reject/stop, debt o replan. | Gate log con recommendation, verification, decision, severidad, evidencia y consecuencia. | Si es critico, irreversible, tercer ciclo, deuda significativa, replan critico o cierre final. | Ejecutar accion decidida. |
| Evidencia insuficiente. | `block` cierre o `rework`; no se acepta gate. | Evidence gap, evidencia esperada faltante, limitacion y relacion con gate/contract. | Si requiere excepcion a DoD/testing o afecta modulo final. | Generar evidencia o escalar excepcion. |
| Knowledge Gap. | `block` implementacion/diseno afectado y crear Curation Request. | Knowledge Gap, Curation Request, fuente faltante, tarea/decision afectada, budget class. | Si no existe source policy/fuente aprobada. | Activar Curation Mode aprobado o esperar decision owner. |
| Source policy insuficiente o fuente prohibida necesaria. | `block` y `escalate to owner`; busqueda web libre sigue prohibida. | Source policy gap, fuente propuesta, dominio/URL base, riesgo y aplicabilidad. | Si. | Owner/source policy aprueba o rechaza fuente; luego curacion o replan. |
| Deuda funcional sobre alcance comprometido. | No es aceptable para produccion tecnica; `rework`, `block`, `escalate` o `replan/reduce scope`. | Functional gap, alcance afectado, impacto, opcion de replan. | Si afecta scope o readiness del modulo. | Completar, reducir alcance explicitamente o rechazar. |
| Deuda tecnica menor. | Puede `accept technical debt` solo si cumple condiciones. | Debt log con descripcion, impacto, severidad, responsable, condicion de pago y aceptacion. | Si es high/modulo/significativa; orquestacion si menor y permitido. | Avanzar con deuda trazada o rework si no aceptable. |
| Riesgo critico de seguridad/datos/compliance o contradiccion normativa. | `block` y `escalate to owner`; no warning para produccion tecnica. | Risk log, fuentes, severidad, impacto y decision requerida. | Si. | Mitigar, replan, reject/stop o owner decision. |
| Testing minimo no ejecutado o instalacion/carga aplicable no validada. | `block` produccion tecnica; no puede registrarse como deuda aceptable. | QA/testing evidence gap, entorno disponible/no disponible, tests afectados. | Si se pide excepcion. | Ejecutar tests, resolver entorno, o owner decide replan/excepcion no apta para ready. |
| Rework default agotado: 2 ciclos bajo mismo alcance. | Activar Rework Limit Gate; tercer ciclo significativo requiere justificacion y escalamiento. | Rework history, causa, ciclos, evidencia previa/nueva, diagnostico. | Si tercer ciclo significativo, cambio de alcance o excepcion. | Owner/orquestacion decide rework adicional, replan/reduce scope, reject/stop o cambio de enfoque. |
| Token budget excedido sin justificacion. | `rework` de context routing o `continue with warning` solo si no afecta riesgo/DoD. | Token/context usage exception, razon, impacto estimado. | Si la expansion requiere fuente prohibida, scope o fuente no aprobada. | Registrar excepcion, ajustar packet o escalar. |
| Entorno Odoo 18 exacto no definido en Blueprint/spike. | No bloquea TOM; en implementacion bloquea declarar produccion tecnica real. | Technical validation/spike requirement y evidencia de entorno faltante. | Owner/Blueprint para priorizacion si afecta V1. | Blueprint/spike define entorno y ejecucion. |

### Rework Maximo Agotado

- [accepted] El rework default es 2 ciclos por tarea bajo el mismo alcance.
- [accepted] Un tercer ciclo significativo requiere justificacion, evidencia, diagnostico de causa y escalamiento.
- [accepted] Si el rework maximo se agota, la tarea no sigue indefinidamente: se activa Rework Limit Gate.
- [accepted] Las salidas permitidas tras Rework Limit Gate son replan/reduce scope explicito, reject/stop, decision owner para excepcion justificada, cambio de enfoque tecnico o bloqueo hasta resolver contexto/fuente/entorno.
- [accepted] El agotamiento de rework debe quedar registrado en Rework History y Gate Log con causa, severidad, evidencia y consecuencia.

### Owner Approval Obligatorio

- [accepted] Escalan siempre al owner: cambio de alcance, falta de contexto critico no resoluble, riesgo legal/compliance critico, contradiccion normativa, riesgo alto de seguridad o datos, decision arquitectonica irreversible, excepcion a testing/DoD, rework repetido fuera de limite, aceptacion final del modulo y recorte por plazo.
- [accepted] Tambien escala al owner cualquier fuente externa no aprobada cuando no exista source policy suficiente para Curation Mode.
- [accepted] Owner approval debe registrarse en Approval Log y enlazarse a decision/gate/deuda/replan/evidencia.

## Knowledge Governance En El Flujo V1

### Modo Minimo Por Defecto

- [accepted] Knowledge Governance arranca en modo minimo en V1.
- [accepted] Modo minimo significa source registry inicial ligero, source policy basica, knowledge artifacts minimos bajo demanda, source usage trazado y Knowledge Gap/Curation Request basicos.
- [accepted] La source policy minima pre-autorizada sin Curation Mode es documentacion oficial Odoo y repositorio oficial GitHub `odoo/odoo`; otras fuentes requieren Curation Request y aprobacion segun DEC-ACCEPTED-163.
- [accepted] Bootstrap incremental no autoriza implementar sin conocimiento autorizado suficiente.
- [accepted] Curation Mode no inicia por defecto; se activa por Knowledge Gap.
- [accepted] V1 no carga toda la documentacion desde el dia 1 y no asume RAG/base vectorial.

### Source Registry Minimo

- [accepted] El source registry logico debe clasificar official source, curated source, secondary source y prohibited source.
- [accepted] Cada fuente debe poder registrar source id conceptual, dominio/subdominio, snapshot/version, trust level, freshness/vigencia, applicability, stewardship y policy aplicable.
- [accepted] Una fuente oficial no queda automaticamente convertida en conocimiento aplicable; debe tener vigencia, aplicabilidad y, cuando corresponda, artifact curado.
- [accepted] Fuentes secundarias pueden informar contexto con warning, pero no son autoridad sin validacion.
- [accepted] Fuentes prohibidas/no relevantes deben quedar excluidas y registradas cuando su exclusion sea relevante para el packet/gate.
- [queda para Blueprint] Rutas, formatos, schemas fisicos y validators reales del source registry.

### Knowledge Artifacts Minimos

- [accepted] Knowledge artifact es la unidad logica que transforma fuente/snapshot en regla, recomendacion, pattern, anti-pattern, example, warning, aplicabilidad y evidencia utilizable.
- [accepted] V1 debe cubrir bajo demanda conocimiento Odoo, ORM, security/access, views/actions/menus, models/fields/constraints, data XML/CSV, testing, performance, module structure, OWL/frontend Odoo si aplica, Playwright/testing frontend si aplica, buenas practicas, anti-patrones y ejemplos tecnicos validados.
- [accepted] Python entra solo como Python aplicado a Odoo; quedan fuera Python generico, Django, FastAPI, Flask y patrones Python que contradigan Odoo.
- [accepted] Integration knowledge packs son logicos y condicionales; integraciones externas reales no entran por defecto en V1.
- [queda para Blueprint] Formato fisico, schema final, validator real y storage de knowledge artifacts.

### Uso En PRD, SDD, Tasks, Gates Y Evidence

- [accepted] PRD debe registrar fuentes/contexto usados cuando afecten reglas, alcance, compliance, datos o aceptacion.
- [accepted] SDD debe basarse en fuentes Odoo/knowledge artifacts autorizados y registrar source usage para decisiones tecnicas.
- [accepted] Task/context packet debe declarar fuentes autorizadas, secundarias, prohibidas/no relevantes, aplicabilidad, budget class y excepciones.
- [accepted] Gates deben verificar que las fuentes usadas son autorizadas/aplicables y que no existe Knowledge Gap bloqueante.
- [accepted] Evidence debe enlazar fuentes usadas, limitaciones, contexto y knowledge artifacts cuando influyan en decision, test, implementacion o cierre.

### Knowledge Gap, Curation Request Y Curation Mode

- [accepted] Un Knowledge Gap existe cuando falta conocimiento autorizado suficiente para decidir, disenar, implementar, verificar o cerrar sin inventar.
- [accepted] Knowledge Gap bloquea la implementacion o decision afectada hasta que exista fuente/artifact/pack autorizado suficiente.
- [accepted] Una Curation Request debe indicar conocimiento faltante, decision/tarea afectada, fuente oficial propuesta, dominio/URL base a autorizar, artifact esperado, alcance, limitacion de contexto y budget class.
- [accepted] Curation Mode solo permite consultar fuentes externas aprobadas por owner, source policy previa, documentos especificos entregados por owner, repositorios oficiales autorizados o Swagger/OpenAPI/PDFs tecnicos aprobados como candidatos.
- [accepted] Si no existe source policy aprobada o fuente autorizada, debe escalar al owner antes de buscar.
- [accepted] El resultado de Curation Mode debe convertirse en source registry entry, snapshot/version, trust/freshness/applicability, knowledge artifact o integration knowledge pack, y validarse/aprobarse antes de usarlo para implementar.
- [accepted] La busqueda web libre no es fuente directa de implementacion.
- [accepted] Queda prohibido usar Wikipedia como fuente tecnica directa, blogs no autorizados, StackOverflow como fuente autoritativa, copiar soluciones de terceros sin validacion o ampliar fuentes sin aprobacion.
- [accepted] RAG/base vectorial no forma parte de V1 salvo decision futura post-V1.

## Instancia En El Piloto V1 Confirmado

### Estado Del Piloto

- [accepted] El piloto V1 confirmado por el owner es solicitudes internas / aprobaciones simples.
- [accepted] Esta seleccion queda cerrada para el Blueprint; no debe reabrirse salvo nueva decision explicita del owner.
- [accepted] Esta seccion instancia el modelo operativo sobre el piloto confirmado sin crear PRD final, SDD final ni backlog del piloto.
- [accepted] El piloto debe ser real, acotado, Odoo 18, con modelos, vistas, ACL/record rules, workflow, reglas de negocio, datos minimos, tests backend, tests de acceso, documentacion, evidencia y sin integracion externa compleja por defecto.

### Como Entra La Idea Piloto

- [accepted] El owner puede ingresar una idea breve equivalente a: necesidad de gestionar solicitudes internas con aprobaciones simples en Odoo 18.
- [accepted] Analisis funcional no debe asumir PRD completo desde esa frase; debe elicitar objetivo, usuarios/roles de negocio, reglas, estados/transiciones, datos minimos, criterios de aceptacion, restricciones y fuera de alcance.
- [accepted] Si la idea requiere integracion externa, compliance avanzado, frontend custom avanzado o workflow complejo, se registra como riesgo/scope impact y se escala antes de incluirlo en V1.

### PRD Minimo Esperado Del Piloto

- [accepted] Debe declarar problema, objetivo funcional y alcance acotado del modulo.
- [accepted] Debe declarar scope in/out, incluyendo que no hay integracion externa compleja por defecto salvo decision posterior.
- [accepted] Debe definir actores/roles de negocio necesarios para solicitar, revisar/aprobar y administrar segun la decision del owner; no se fijan aqui actores finales.
- [accepted] Debe definir campos funcionales minimos de la solicitud, reglas de negocio, estados/transiciones, criterios de aprobacion/rechazo y excepciones relevantes; no se fijan aqui campos finales.
- [accepted] Debe declarar criterios de aceptacion testeables para flujo, permisos/accesos, datos minimos, documentacion y cierre.
- [accepted] Debe identificar riesgos de seguridad/datos/compliance y dudas bloqueantes.

### SDD Minimo Esperado Del Piloto

- [accepted] Debe traducir el PRD aprobado a diseno Odoo 18 ligero.
- [accepted] Debe definir conceptualmente estructura de modulo, modelos/fields/constraints, workflow, views/actions/menus, ACL/record rules, datos minimos, tests backend, tests de acceso y documentacion/evidencia esperada.
- [accepted] Debe registrar fuentes Odoo/knowledge artifacts usados para ORM, security/access, views, module structure y testing.
- [accepted] Debe incluir ADR minimo solo si existe decision tecnica relevante.
- [accepted] Debe declarar estrategia de pruebas suficiente/aplicable y condiciones de no aplica.
- [queda para Blueprint] Detalle fisico de archivos Odoo, rutas, manifests, nombres tecnicos finales, commands, validators y entorno de ejecucion.

### Task/Context Packets Esperados Del Piloto

- [accepted] Se esperan packets verificables para las unidades que el SDD apruebe; no se crea aqui backlog ni secuencia cerrada.
- [accepted] Como categorias operativas esperadas, el piloto normalmente necesitara packets para modelo/datos, seguridad/accesos, workflow/reglas de negocio, vistas/actions/menus, datos minimos, pruebas backend, pruebas de acceso, documentacion y evidencia/cierre.
- [accepted] Cada packet debe incluir objetivo, scope in/out, fuentes autorizadas, fuentes prohibidas/no relevantes, criterios de aceptacion, evidencia esperada, risk flags, blockers o `none`, budget class, escalation conditions y handoff.
- [accepted] Si el SDD no justifica frontend/OWL custom, no se crea packet OWL avanzado por defecto.
- [accepted] Si no hay integracion externa, no se crea integration knowledge pack ni task de integracion.

### Gates Aplicables Al Piloto

- [accepted] Aplican todos los gates minimos independientes: PRD Sufficiency, SDD Sufficiency, Task Packet / DoR, QA/Testing, Evidence/Closure y Module Technical Readiness.
- [accepted] Aplican siempre los checks transversales Context Routing / Token Budget y Security/Risk/Compliance Triage.
- [accepted] Security/Data/Access Gate se activa por ACL/record rules, permisos, datos o accesos del modulo.
- [accepted] Debt Acceptance Gate solo aplica si se propone deuda tecnica menor; deuda funcional sobre alcance comprometido no puede aceptarse para readiness tecnica.
- [accepted] Rework Limit Gate aplica si una tarea falla repetidamente o llega al limite de rework.

### Evidencia Minima Del Piloto

- [accepted] PRD ligero y SDD ligero trazables.
- [accepted] Contract/packet registry para tasks/capabilities ejecutadas.
- [accepted] Context/source usage de fuentes Odoo y knowledge artifacts usados.
- [accepted] Gate logs con recommendation, verification, decision, severidad, accion y evidencia.
- [accepted] Evidence logs de cambios, pruebas, install/update/test execution Odoo 18 cuando exista entorno, resultados QA, documentacion y cierre.
- [accepted] Rework history si aplica.
- [accepted] Debt log con deuda aceptada o declaracion `none` si no existe.
- [accepted] Approval log para decisiones owner, excepciones y aceptacion final.

### Pruebas Minimas Del Piloto

- [accepted] Install/update/test execution de Odoo 18 con captura de evidencia cuando el entorno este definido.
- [accepted] Tests backend aplicables.
- [accepted] Tests de acceso/ACL/record rules aplicables.
- [accepted] Validacion de reglas de negocio y workflow aprobatorio definido en PRD/SDD.
- [accepted] Validacion de carga de datos minimos si aplica.
- [accepted] UI/OWL/Playwright solo si el piloto incluye frontend custom que lo justifique.
- [accepted] Si una prueba minima no puede ejecutarse por falta de entorno, no se declara produccion tecnica sin excepcion explicita y trazable; el entorno exacto queda para Blueprint/spike.

### Simplificaciones Del Piloto Frente Al Modelo General

- [accepted] No incluye integracion externa compleja por defecto.
- [accepted] No usa RAG/base vectorial.
- [accepted] No requiere SDK/server como core V1.
- [accepted] No requiere dashboard/UI del framework ni CI/CD completo.
- [accepted] Knowledge governance opera en modo minimo con fuentes/artifacts Odoo necesarios para el piloto.
- [accepted] Legal-compliance avanzado queda fuera salvo que el PRD aprobado lo active explicitamente.
- [accepted] Frontend/OWL avanzado y Playwright quedan condicionales; no se asumen si las vistas Odoo estandar bastan.
- [accepted] Despliegue productivo real queda fuera.

### Fuera Del Piloto

- [accepted] PRD final del piloto.
- [accepted] SDD final del piloto.
- [accepted] Backlog del piloto.
- [accepted] Reapertura de la seleccion del piloto sin nueva decision explicita del owner.
- [accepted] Integraciones externas reales salvo decision posterior explicita.
- [accepted] RAG/base vectorial, SDK/server core, dashboard, CI/CD completo, DB avanzada, multiusuario/equipo, plugins/MCP/custom tools y curation avanzada.

## Handoff Al Blueprint

### Artefactos Operativos Que Entrega El TOM

- [accepted] Mapa operativo V1 de roles/capacidades, mecanismos, limites y handoffs.
- [accepted] Flujo punta a punta con entrada, salida, ejecutor, validador, evidencia minima, bloqueo, condicion de avance y handoff por fase.
- [accepted] Matriz de control con bloqueos, escalamiento, warnings, rework, owner approval y consecuencias ante rework maximo.
- [accepted] Modelo operativo de Knowledge Governance V1: source registry minimo, knowledge artifacts, Knowledge Gap, Curation Request, Curation Mode y reglas de fuente.
- [accepted] Instancia del flujo sobre el piloto V1 confirmado de solicitudes internas / aprobaciones simples sin cerrar PRD/SDD/backlog.
- [accepted] Lista de gates aplicables, checks transversales y gates condicionales.
- [accepted] Reglas de no double work y de separacion entre narrativa LLM y estado autoritativo.
- [accepted] Lista concreta de decisiones fisicas/tecnicas que quedan para Blueprint y spikes.

### Decisiones Que El Blueprint Debe Resolver

- [queda para Blueprint] Runtime layout fisico de CAFL V1.
- [queda para Blueprint] Mapping final de capacidades a agents, commands, scripts/validators, rules/config y skills/playbooks sin usar `framework/`.
- [queda para Blueprint] Agentes ejecutables finales, si se aprueban, incluyendo prompts, permisos y modos.
- [queda para Blueprint] Commands reales finales, argumentos, salidas esperadas y condiciones de invocacion.
- [queda para Blueprint] Schemas fisicos finales/minimos V1 para registros criticos, contracts, packets, gates, evidence, source policy, rework, debt y approvals.
- [queda para Blueprint] Validators reales y su toolchain.
- [queda para Blueprint] Storage fisico simple, auditable y compatible con Git, incluyendo convenciones de Markdown, JSON/YAML, JSONL append-only y artifacts.
- [queda para Blueprint] Rutas fisicas de registros, logs, evidencia, source registry y knowledge artifacts.
- [queda para Blueprint] OpenCode setup/runtime configuration, permissions y forma de operar agents/commands/skills.
- [queda para Blueprint] Entorno exacto Odoo 18 y forma de ejecutar install/update/test execution.
- [queda para Blueprint] Evidence capture fisico y convenciones de logs/resultados.
- [queda para Blueprint] Source policy enforcement basico y materializacion de Knowledge Gap/Curation Request.
- [queda para Blueprint] Secrets handling para Odoo, tokens, certificados o integraciones futuras.
- [queda para Blueprint] Instanciacion del flujo sobre el piloto V1 confirmado sin reabrir su seleccion.

### Technical Validations / Spikes Que Blueprint Debe Planificar

- [technical validation/spike] Lenguaje scripts/CLI: no se asume Python, Node ni otro lenguaje; decidir por facilidad local, JSON/YAML/JSONL, integracion Odoo, velocidad, mantenibilidad y friccion OpenCode.
- [technical validation/spike] Entorno Odoo 18 exacto: Docker, venv/local u otra alternativa.
- [technical validation/spike] OpenCode permissions.
- [technical validation/spike] OpenCode commands/skills.
- [technical validation/spike] SDK/server no se planifica como core V1; cualquier spike posterior requiere decision owner explicita y debe demostrar beneficio frente a commands/scripts/validators.
- [technical validation/spike] Schema/validator toolchain.
- [technical validation/spike] Storage/log convention.
- [technical validation/spike] Source policy enforcement y Knowledge Gap basico.
- [technical validation/spike] Knowledge governance sin RAG/base vectorial.
- [technical validation/spike] Odoo 18 install/update/test execution.
- [technical validation/spike] Evidence capture.
- [technical validation/spike] Secrets handling.
- [technical validation/spike] OpenAPI/PDF processing solo si una decision posterior de alcance lo requiere explicitamente.
- [technical validation/spike] Frontend/OWL/Playwright solo si el piloto aprobado lo requiere.

### Lo Que NO Debe Resolver El TOM

- [accepted] Lenguaje scripts/CLI final.
- [accepted] Entorno Odoo 18 exacto.
- [accepted] Schemas fisicos finales.
- [accepted] Validators reales.
- [accepted] Commands reales.
- [accepted] Agents ejecutables finales.
- [accepted] Runtime layout.
- [accepted] Rutas fisicas de storage/logs/evidence.
- [accepted] RAG/base vectorial, que queda post-V1 salvo decision posterior explicita.
- [accepted] PRD final del piloto V1 confirmado.
- [accepted] Backlog tecnico ni secuencia de implementacion.

## Lo Que El TOM NO Hace

- [accepted] No crea runtime.
- [accepted] No crea commands reales.
- [accepted] No crea agents ejecutables.
- [accepted] No crea prompts finales.
- [accepted] No crea schemas fisicos finales.
- [accepted] No crea validators reales.
- [accepted] No crea scripts.
- [accepted] No crea RAG.
- [accepted] No crea base vectorial.
- [accepted] No crea backlog tecnico.
- [accepted] No crea Implementation Blueprint.
- [accepted] No implementa nada.
- [accepted] No configura OpenCode.
- [accepted] No recrea ni usa `framework/` como input.
- [accepted] No crea CRIT-08 ni sesiones criticas nuevas.
- [accepted] No reabre decisiones aprobadas en CRIT-01..CRIT-07.

## Outputs Esperados Del TOM

- [accepted] Mapa operativo V1 elaborado: roles, capacidades, flujo, mecanismos, bloqueos, escalamientos, rework y knowledge governance.
- [accepted] Instancia del modelo operativo sobre el piloto V1 confirmado con simplificaciones/restricciones explicitas.
- [accepted] Lista concreta de artefactos, decisiones y validations/spikes que pasan al Blueprint.
- [accepted] Lista explicita de decisiones tecnicas/fisicas fuera del TOM.
- [accepted] La decision de aprobacion del TOM por el owner queda registrada en `decisions/accepted.md` como DEC-ACCEPTED-161.
- [accepted] No se identifican nuevos riesgos que requieran actualizar `risks.md` durante esta elaboracion.

## Owner Decisions Pendientes

- [accepted] Aprobacion explicita del TOM final otorgada por el owner (2026-05-27). Estado cambiado a `approved`.
- [accepted] Seleccion final del piloto V1 confirmada por owner como solicitudes internas / aprobaciones simples. Decision registrada en DEC-ACCEPTED-162; Blueprint instancia el flujo sin reabrir seleccion.
- [accepted] Source policy minima base aprobada por owner: documentacion oficial Odoo y repositorio oficial GitHub `odoo/odoo`. Decision registrada en DEC-ACCEPTED-163; enforcement fisico queda para Blueprint.
- [queda para Blueprint] Aprobaciones puntuales de fuentes externas durante Curation Mode cuando no exista source policy suficiente.
- [queda para Blueprint] Decisiones de excepcion sobre testing/DoD, deuda significativa, tercer ciclo de rework o recorte de alcance si aparecen durante implementacion.

## Conflictos Y Open Questions

- [accepted] No se detectaron conflictos entre fuentes obligatorias que afecten aprobacion, flujo, responsabilidades, gates, evidencia, knowledge governance, runtime candidate o scope V1.
- [accepted] No se registran `needs-owner-decision` por conflicto de autoridad dentro del TOM.
- [accepted] No se registran `open-question` que bloquee el TOM; las decisiones tecnicas fisicas quedan clasificadas como `queda para Blueprint` o `technical validation/spike`.
- [accepted] La seleccion final del piloto quedo cerrada por owner en DEC-ACCEPTED-162; Blueprint no debe reabrirla salvo nueva decision explicita.

## Dependencies

- [accepted] Depende de CRIT-01..CRIT-07 todos approved.
- [accepted] Depende de Consolidated Truth Review en estado `READY_FOR_TARGET_OPERATING_MODEL`.
- [accepted] Cuenta con aprobacion explicita del owner, registrada como DEC-ACCEPTED-161, para mantener `Status: approved`.
- [accepted] Alimenta directamente el Implementation Blueprint.
- [accepted] Blueprint debe definir formalmente validations/spikes, backlog tecnico e implementacion controlada sin crear CRIT-08.

## Acceptance Criteria

| Criterio | Estado | Nota |
| --- | --- | --- |
| Cada rol/capacidad tiene responsabilidades, limites y handoffs sin ambiguedad operativa. | [accepted] Cumplido operativamente | Cubierto en `Roles Y Capacidades`. |
| Cada fase del flujo tiene entrada, salida esperada, evidencia minima, ejecutor, validador, condicion de bloqueo, condicion de avance y handoff. | [accepted] Cumplido operativamente | Cubierto en `Fases, Evidencia Y Handoffs`. |
| Cada gate puede responder que recomienda, que verifica, con que evidencia, quien decide y que pasa si falla, incluyendo rework maximo agotado. | [accepted] Cumplido operativamente | Cubierto en `Flujo Operativo Punta A Punta` y `Control Y Bloqueos`. |
| Knowledge governance tiene lugar explicito en V1: modo minimo por defecto, Curation Mode por Knowledge Gap y bloqueo por fuente insuficiente. | [accepted] Cumplido operativamente | Cubierto en `Knowledge Governance En El Flujo V1`. |
| El modelo operativo generico cubre todos los modulos V1 sin restringirse al piloto. | [accepted] Cumplido operativamente | Cubierto por flujo generico y unidad module -> capability/feature -> task. |
| El piloto queda instanciado con simplificaciones/restricciones explicitas. | [accepted] Cumplido operativamente | Cubierto en `Instancia En El Piloto V1 Confirmado`. |
| Outputs del TOM al Blueprint estan listados concretamente. | [accepted] Cumplido operativamente | Cubierto en `Handoff Al Blueprint`. |
| Lo que queda fuera del TOM esta listado explicitamente para Blueprint/spikes/post-V1. | [accepted] Cumplido operativamente | Cubierto en `Lo Que NO Debe Resolver El TOM` y `Lo Que El TOM NO Hace`. |
| El owner aprueba explicitamente el TOM. | [accepted] Cumplido | Aprobacion owner otorgada explicitamente el 2026-05-27 y registrada en DEC-ACCEPTED-161. |
| No se creo runtime, commands reales, schemas fisicos, validators reales, scripts ni backlog tecnico durante la sesion. | [accepted] Cumplido | El TOM solo documenta modelo operativo. |

## Estado Final Del TOM

- [accepted] El TOM operativo completo queda elaborado desde `project-truth/` y aprobado explicitamente por el owner (2026-05-27).
- [accepted] La aprobacion owner requerida esta satisfecha y el documento mantiene `Status: approved`.
- [accepted] El siguiente trabajo habilitado es Implementation Blueprint; no queda aprobado Blueprint, backlog ni implementacion.
- [accepted] No se detecto informacion critica imposible de resolver desde `project-truth/` que obligue a usar `Status: needs-owner-decision` para el documento completo.
