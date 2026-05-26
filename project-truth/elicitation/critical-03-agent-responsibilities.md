# CRIT-03: Agent Responsibilities

Status: approved

## Session Objective

- [accepted] Definir responsabilidades, autoridad conceptual, limites, handoffs y mecanismo candidato por responsabilidad antes de crear o ajustar agentes.
- [accepted] CRIT-03 decide responsabilidades reales de CAFL, no una lista final de agentes OpenCode.
- [accepted] CRIT-03 usa `project-truth/spikes/spike-oc-crit03-opencode-responsibility-mapping.md` como evidencia tecnica e input, sin convertirlo en arquitectura final.

## Scope Of Approval

- [accepted] Se aprueba el modelo de responsabilidades y mecanismos candidatos.
- [accepted] Se aprueba que CAFL no sea agents-only.
- [accepted] Se aprueba un modelo mixto con agents, commands, control deterministico futuro, rules/config/skills y owner para decisiones criticas.
- [accepted] Se aprueba autoridad conceptual para avanzar, bloquear, replanificar, escalar y cerrar segun responsabilidad.
- [superseded] La clasificacion preliminar de agentes existentes se conserva solo como registro historico de CRIT-03; CRIT-07 elimino `framework/` y supersedio cualquier uso de esos agentes como evidencia secundaria utilizable o candidatos por supervivencia.

## Non-Approvals

- [accepted] CRIT-03 no aprueba agentes ejecutables finales.
- [accepted] CRIT-03 no aprueba prompts finales.
- [accepted] CRIT-03 no aprueba commands finales.
- [accepted] CRIT-03 no aprueba SDK/server/scripts implementados.
- [accepted] CRIT-03 no aprueba permisos tecnicos finales.
- [accepted] CRIT-03 no aprueba contratos finales.
- [accepted] CRIT-03 no aprueba gates finales.
- [accepted] CRIT-03 no aprueba arquitectura OpenCode final.
- [accepted] CRIT-03 no aprueba archivos runtime definitivos.
- [superseded] En CRIT-03, `framework/agents/*.agent.md` se trato solo como evidencia secundaria; CRIT-07 supersedio esa lectura: `framework/` fue eliminado como artefacto contaminado y no es evidencia secundaria utilizable ni input de TOM/Blueprint.

## Sources Reviewed

- [accepted] `project-truth/elicitation/critical-03-agent-responsibilities.md` como plantilla de sesion.
- [accepted] `project-truth/spikes/spike-oc-crit03-opencode-responsibility-mapping.md` como evidencia tecnica principal.
- [accepted] `project-truth/critical-map.md`.
- [accepted] `project-truth/decisions/accepted.md`.
- [accepted] `project-truth/decisions/pending.md`.
- [accepted] `project-truth/risks.md`.
- [accepted] `project-truth/glossary.md`.
- [superseded] `framework/agents/*.agent.md` y `framework/AGENT_CONTRACTS.md` fueron revisados solo como evidencia historica durante CRIT-03; CRIT-07 supersedio su uso y prohibe usarlos como input de TOM/Blueprint.
- [accepted] Documentos raiz del repo solo como evidencia secundaria.

## Accepted Decisions

### DEC-CRIT03-01: Modelo De Responsabilidad CAFL

- [accepted] CAFL no sera agents-only.
- [accepted] CAFL usara modelo mixto.
- [accepted] El modelo mixto combina agents, commands, control deterministico futuro, rules/config/skills y owner solo en decisiones criticas.
- [accepted] Agents son candidatos fuertes para razonamiento, analisis, diseno, generacion, diagnostico, revision y redaccion.
- [accepted] Control deterministico futuro es candidato para estado, evidencia, permisos, token budget, validaciones estructurales, ejecucion de tests y rework counters.

### DEC-CRIT03-02: Lista Minima De Roles/Capacidades

- [accepted] Se aprueban capacidades minimas consolidadas, no agentes finales separados.
- [accepted] Lista minima: owner; coordinacion/orquestacion; analisis funcional; diseno tecnico Odoo; construccion Odoo; verificacion/testing; seguridad/riesgo/compliance; evidencia/cierre; context routing/token budget; task/context packet/DoR; DoD/cierre; rework/escalamiento.
- [accepted] Esta lista no implica que cada capacidad sea un agente separado.

### DEC-CRIT03-03: Orquestacion, Estado Y Autoridad Operativa

- [accepted] La orquestacion sera mixta.
- [accepted] Un orquestador puede usar razonamiento LLM para coordinar, proponer avance, bloqueo, replanificacion y handoffs.
- [accepted] Estado real, evidencia, rework counters y gates son candidatos a control deterministico posterior.
- [accepted] La orquestacion puede avanzar tareas solo con DoR/DoD y evidencia suficiente.
- [accepted] La orquestacion puede bloquear por contexto critico.
- [accepted] La orquestacion puede replanificar dentro de limites.
- [accepted] La orquestacion debe escalar decisiones criticas al owner.
- [accepted] La orquestacion no puede autocerrar sin evidencia, reemplazar gates finales ni convertir narrativa LLM en estado real sin trazabilidad.

### DEC-CRIT03-04: Trabajo Humano Y Escalamiento Obligatorio

- [accepted] El owner interviene solo en decisiones criticas predefinidas, no en microgestion operativa.
- [accepted] Escalan siempre al owner: cambio de alcance; falta de contexto critico; riesgo legal/compliance critico; contradiccion normativa; riesgo alto de seguridad o datos; decision arquitectonica irreversible; excepcion a testing o DoD; rework repetido fuera del limite; aceptacion final del modulo; recorte de alcance por plazo.

### DEC-CRIT03-05: Analisis Funcional Y PRD Minimo

- [accepted] Analisis funcional usara functional analyst LLM, command repetible candidato y decisiones puntuales del owner.
- [accepted] Debe producir PRD ligero, alcance in/out, actores, reglas, criterios de aceptacion y dudas bloqueantes.
- [accepted] No debe disenar arquitectura tecnica, escribir codigo, cerrar gates ni inventar decisiones de negocio criticas.

### DEC-CRIT03-06: Diseno Tecnico Odoo

- [accepted] Diseno tecnico Odoo usara arquitecto Odoo LLM, skills/fuentes oficiales y validacion posterior por QA/riesgo.
- [accepted] El arquitecto Odoo debe traducir PRD aprobado en SDD ligero antes de escribir codigo.
- [accepted] El arquitecto puede bloquear por fuentes insuficientes, ambiguedad tecnica critica, riesgo de seguridad/datos o impacto arquitectonico relevante.
- [accepted] El arquitecto no debe implementar como responsabilidad primaria, cerrar gates finales ni inventar comportamiento Odoo sin fuente suficiente.

### DEC-CRIT03-07: Granularidad De Construccion Odoo

- [accepted] La construccion Odoo usara division dinamica por riesgo.
- [accepted] Para V1 se acepta backend builder como capacidad base.
- [accepted] Frontend/OWL sera condicional solo si aplica.
- [accepted] Especialistas por artefacto solo se activan cuando el SDD, riesgo o complejidad lo justifique.
- [accepted] No se aprueba crear especialistas permanentes por cada artefacto Odoo desde el inicio.

### DEC-CRIT03-08: Verificacion, Testing Y DoD

- [accepted] Verificacion/testing sera mixta.
- [accepted] QA LLM puede planificar, diagnosticar y reportar.
- [accepted] Ejecucion de pruebas, captura de evidencia y validaciones reproducibles son candidatas a commands/scripts/control deterministico.
- [accepted] El builder no puede autocerrar.
- [accepted] QA puede rechazar y enviar a rework.
- [accepted] El cierre de modulo requiere evidencia de tests aplicables y aceptacion del owner o mecanismo aprobado posteriormente.

### DEC-CRIT03-09: Seguridad, Riesgo Y Compliance

- [accepted] Seguridad/riesgo/compliance existe como responsabilidad explicita.
- [accepted] El modelo aprobado es mixto: checklist transversal, reviewer especializado cuando exista riesgo alto o critico y escalamiento humano para riesgo legal/compliance critico.
- [accepted] Compliance no debe diluirse dentro de QA generico ni fusionarse prematuramente de forma que pierda visibilidad.
- [accepted] CAFL V1 no debe convertirse en motor legal completo.
- [accepted] La responsabilidad explicita de compliance debe preservarse aunque se decida despues si queda como agente, skill, checklist, reviewer o capacidad combinada.

### DEC-CRIT03-10: Context Routing Y Token Budget

- [accepted] Context routing y token budget son responsabilidad separada mixta.
- [accepted] No deben depender del criterio libre del ejecutor.
- [accepted] El task/context packet debe declarar fuentes aplicables, fuentes secundarias, fuentes prohibidas/no relevantes, presupuesto de contexto/token budget y justificacion para excepciones.
- [accepted] Ningun rol ejecutor debe cargar contexto masivo sin justificacion trazable.

### DEC-CRIT03-11: Task/Context Packet Y Definition Of Ready

- [accepted] El packet lo genera la fase productora.
- [accepted] Orquestacion y/o receptor validan el packet.
- [accepted] Futuros checks deterministicos deben validar estructura minima.
- [accepted] Ninguna tarea inicia sin task/context packet y DoR.
- [accepted] El receptor puede rechazar el packet por objetivo incompleto, alcance incompleto, fuentes insuficientes, restricciones faltantes, criterios de aceptacion insuficientes, evidencia esperada incompleta o blockers no resueltos.

### DEC-CRIT03-12: Rework Y Replanificacion

- [accepted] El rework queda acotado por defecto a 2 ciclos por tarea bajo el mismo alcance.
- [accepted] El limite de 2 ciclos es default, no regla absoluta.
- [accepted] Excepciones requieren justificacion, trazabilidad y escalamiento.
- [accepted] Orquestacion controla el contador de rework.
- [accepted] QA y arquitecto pueden disparar rework.
- [accepted] Owner decide excepciones relevantes, cambio de alcance o tercer ciclo significativo.

### DEC-CRIT03-13: Commands Candidatos

- [accepted] Commands quedan aprobados solo como entradas repetibles de fase y tareas, no como autoridad final.
- [accepted] Commands candidatos: elicitar modulo; generar PRD; generar SDD; preparar task/context packet; desarrollar tarea; ejecutar/verificar pruebas; validar gate; registrar evidencia; preparar cierre.
- [accepted] Esta decision no aprueba la creacion de commands runtime.

### DEC-CRIT03-14: Control Deterministico, Rules/Config/Skills

- [accepted] LLM se usara para juicio, razonamiento, analisis, diseno, generacion, diagnostico y redaccion.
- [accepted] Scripts/SDK/server/control deterministico son candidatos para validacion, estado, ejecucion reproducible, evidencia, permisos, token budget, DoR/DoD estructural, rework counters y triggers de escalamiento.
- [accepted] Rules/config son candidatos para invariantes globales minimos.
- [accepted] Skills/playbooks son candidatos para conocimiento operativo on-demand.
- [accepted] No se aprueba implementar todavia SDK/server/scripts ni arquitectura OpenCode final.

## Responsibility Matrix

| Responsibility / role capability | Recommended mechanism | Main responsibilities | Non-responsibilities | Inputs | Outputs | Authority | Handoffs | Open questions |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Owner | human | Decidir alcance critico, riesgos criticos, excepciones, aceptacion final | Microgestionar tareas operativas | Preguntas bloqueantes, reportes, riesgos, evidencia | Decisiones, aceptaciones, rechazos, cambios | Acepta, rechaza o modifica decisiones criticas | Orquestacion | Severidades exactas quedan para CRIT-05 |
| Coordinacion/orquestacion | mixed | Coordinar flujo, handoffs, bloqueos, rework y escalamiento | Reemplazar estado/gates finales por narrativa LLM | PRD, SDD, packets, riesgos, evidencia | Handoffs, bloqueo, replanificacion, decision request | Avanza con DoR/DoD; bloquea; escala; propone cierre | Todos los roles | Estado autoritativo queda para CRIT-06 |
| Analisis funcional | agent + command + human | Elicitar negocio, alcance, actores, reglas y PRD minimo | Disenar arquitectura o escribir codigo | Idea owner, contexto de negocio | PRD ligero, scope in/out, criterios, dudas | Bloquea por falta de contexto funcional critico | Arquitectura, owner | Formato PRD queda para CRIT-04 |
| Diseno tecnico Odoo | agent + rule-config-skill | Producir SDD, decisiones tecnicas y riesgos | Implementar como responsabilidad primaria o cerrar gates finales | PRD aprobado, fuentes oficiales, restricciones | SDD ligero, ADR minimo, riesgos | Bloquea por fuente insuficiente o riesgo tecnico critico | Builders, QA, riesgo | Politica de fuentes queda para CRIT-06 |
| Construccion Odoo backend | agent + command + permissions later | Implementar backend segun SDD y packet | Cambiar alcance, autocerrar u omitir SDD | SDD, packet, DoR | Codigo, notas, evidencia local | Edita solo con packet ready | QA, orquestacion | Permissions tecnicos quedan para validations/spikes post-CRIT-07 |
| Construccion frontend/OWL condicional | agent conditional | Implementar OWL/JS/assets/tours cuando aplique | Crear frontend sin necesidad funcional/SDD | SDD frontend, packet | Codigo frontend y pruebas aplicables | Puede rechazar packet frontend insuficiente | QA, backend, arquitectura | Criterio OWL queda para Blueprint/piloto posterior |
| Verificacion/testing | mixed | Planificar, diagnosticar, ejecutar/verificar pruebas y reportar evidencia | Confiar solo en opinion LLM o autocerrar modulo | PRD, SDD, codigo, entorno, criterios | Plan, resultados, reporte QA, rework | Rechaza entrega y exige rework | Builder, orquestacion, evidencia | Commands reales quedan para Blueprint/spikes post-CRIT-07 |
| Seguridad/riesgo/compliance | mixed | Revisar seguridad, datos, riesgo operativo y compliance | Reemplazar asesoria legal humana o motor legal completo V1 | PRD, SDD, fuentes, evidencia | Riesgos, blockers, advertencias | Bloquea/escalada riesgo legal/compliance critico | Owner, orquestacion, arquitectura, QA | Severidades finales quedan para CRIT-05 |
| Evidencia/cierre | mixed | Consolidar evidencia, trazabilidad y reporte | Cerrar sin tests o sin aceptacion requerida | Resultados QA, decisiones, riesgos | Paquete de cierre, gaps, decision request | Propone cierre; no reemplaza owner en modulo final | Owner, orquestacion | Modelo de evidencia queda para CRIT-06 |
| Context routing/token budget | rule-config-skill + SDK-server-script + agent | Seleccionar contexto minimo y clasificar fuentes | Leer todo el repo por defecto | Objetivo, fase, fuente de verdad, packet | Contexto permitido/excluido y budget | Rechaza contexto excesivo o insuficiente | Todos los roles | Enforcement queda para Blueprint/spikes post-CRIT-07 |
| Task/context packet / DoR | mixed | Generar y validar readiness | Iniciar trabajo con packet generico | PRD/SDD, objetivo, restricciones, fuentes | Packet ready o rechazo DoR | Receptor rechaza; orquestacion arbitra | Builders, QA, riesgo | Campos finales quedan para CRIT-04 |
| DoD y cierre | mixed + human | Validar tarea, feature y modulo con evidencia | Cierre por opinion del ejecutor | Evidencia, tests, criterios, riesgos | Cierre o rework | QA/orquestacion cierran niveles operativos; owner acepta modulo final | Owner, evidencia | DoD verificable queda para CRIT-05 |
| Rework/escalamiento | mixed + SDK-server-script later | Contar ciclos, limitar loops y escalar | Reintentar indefinidamente | Fallas QA, blockers, cambios | Rework plan, escalamiento | 2 ciclos default; owner excepciones | Builder, QA, owner | Politica final queda para CRIT-05 |
| Commands de fase | command + agent | Estandarizar entrada de fases y tareas | Ser gate final o validacion deterministica | Argumentos, paths, packet | Sesion estructurada, salida esperada | Invoca flujo; no decide verdad final | Orquestacion, roles | Catalogo final queda para Blueprint post-CRIT-07 |
| Control deterministico futuro | SDK-server-script | Estado, checks estructurales, tests, evidencia, permisos, rework counters | Juicio funcional o tecnico ambiguo | Artefactos, repo, entorno | Resultados reproducibles, logs, evidencias | Enforcement tecnico posterior | Orquestacion, QA, CRIT-07 | Viabilidad base aprobada en CRIT-07; implementacion queda para Blueprint/spikes |
| Rules/config/skills | rule-config-skill | Invariantes globales, playbooks on-demand y fuentes | Cargar toda la metodologia siempre | Politicas aceptadas, fase, tarea | Instrucciones minimas, skills activables | Condicionan comportamiento; no cierran gates finales | Todos los roles | Contenido final queda para TOM/Blueprint post-CRIT-07 |

## Current Agent Review

- [superseded] Esta revision de nombres existentes se conserva solo como registro historico de CRIT-03. Por CRIT-07, `framework/` fue eliminado como artefacto contaminado y no debe usarse para layout, agents, commands, contracts, gates, schemas, validators, runtime ni knowledge base; no es input de TOM/Blueprint ni candidato de supervivencia.

| Existing agent | Observed purpose | Candidate action | Reason | Risk |
| --- | --- | --- | --- | --- |
| `odoo-pm-orchestrator.agent.md` | Coordinar flujo, alcance, estado, riesgos, gates y handoffs | conserve as candidate | La capacidad de orquestacion es necesaria | Peligroso si pretende mantener estado/gates solo por prompt |
| `odoo-functional-analyst.agent.md` | Elicitar procesos, reglas, usuarios, criterios y PRD base | conserve as candidate | Encaja con LLM y CRIT-02 | Puede generar entrevistas infinitas o invadir diseno tecnico |
| `odoo-architect.agent.md` | Traducir PRD en SDD Odoo v18 con modelos, vistas, seguridad y riesgos | conserve as candidate | SDD ligero obligatorio antes de codigo | Riesgo de decisiones Odoo alucinadas sin fuentes oficiales |
| `odoo-backend-dev.agent.md` | Implementar backend Odoo, modelos, constraints, seguridad, datos y migraciones | conserve as candidate | Builder backend base es util para V1 | Alcance demasiado amplio si no recibe packet y limites claros |
| `odoo-frontend-owl-dev.agent.md` | Implementar OWL/JS/assets/tours y UX frontend | analyze later | Frontend/OWL sera condicional | Puede sobredisenar frontend o existir sin necesidad V1 |
| `odoo-qa-engineer.agent.md` | Disenar, ejecutar y reportar pruebas | split conceptually | Separar QA planning/review de test execution/evidence capture | Falsa confianza si reporta tests no ejecutados |
| `odoo-legal-risk-reviewer.agent.md` | Identificar riesgo legal critico, contradicciones y fuentes insuficientes | analyze later / maybe merge as capability | Preservar responsabilidad explicita de compliance sin fusion prematura | Compliance puede diluirse si se absorbe en QA generico |
| `odoo-knowledge-curator.agent.md` | Mantener fuentes oficiales, snapshots, RAG e ingesta | split/analyze later | Separar source policy, skills/playbooks, referencias oficiales Odoo y RAG | RAG completo puede exceder V1 salvo justificacion CRIT-07 |

## Derived Work

- [accepted] CRIT-04 debe definir contratos internos, task/context packet, campos, formatos, DoR y criterios de suficiencia.
- [accepted] CRIT-05 debe definir gates, severidades, evidencia, DoD verificable, testing suficiente y politica concreta de avance/bloqueo/rework.
- [accepted] CRIT-06 debe definir estado, fuentes, evidencia, trazabilidad, auditoria y registro de decisiones.
- [accepted] CRIT-07 aprobo direccion candidata de runtime y viabilidad; arquitectura exacta, runtime config, permissions, commands reales, SDK/server/scripts si aplican, entorno Odoo y ejecucion verificable quedan para TOM/Blueprint/technical validations post-CRIT-07.
- [accepted] RAG completo no queda aprobado para V1; CRIT-07 lo difirio a V2/post-V1 salvo decision futura explicita.

## Acceptance Criteria Result

- [accepted] CRIT-03 documenta responsabilidades y autoridad conceptual aprobadas.
- [accepted] Queda explicito que CAFL no es agents-only.
- [accepted] Queda aprobado el modelo mixto.
- [accepted] Queda claro que responsabilidades son candidatas a LLM/agent.
- [accepted] Queda claro que responsabilidades son candidatas a commands.
- [accepted] Queda claro que responsabilidades son candidatas a control deterministico futuro.
- [accepted] Queda claro que responsabilidades pertenecen al owner.
- [accepted] Queda claro que no se crean agentes, commands, scripts, permisos finales ni arquitectura OpenCode final.
- [accepted] Se conservan limites hacia CRIT-04, CRIT-05, CRIT-06 y CRIT-07.
- [accepted] Queda explicita la responsabilidad de seguridad/riesgo/compliance.
- [accepted] Queda explicito que compliance no debe diluirse.
- [accepted] Queda explicito que RAG completo no se aprueba para V1 salvo justificacion posterior.
- [accepted] Queda explicito que el limite de 2 ciclos de rework es default, con excepciones justificadas y escaladas.
