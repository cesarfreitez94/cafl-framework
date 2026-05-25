# Critical Map

Status: draft

## Regla De Uso

- [accepted] Este mapa organiza sesiones criticas de elicitacion antes de implementar.
- [accepted] Ningun punto critico produce contratos finales, gates finales, comandos ejecutables o agentes ejecutables por si solo.
- [draft] Si un tema aparece como critico pero es subpunto de otro, se clasifica dentro del punto que decide su autoridad y consecuencias.

## Clasificacion De Subpuntos

- [accepted] OpenCode ya esta aceptado como runtime principal por CRIT-01; CRIT-07 solo debe definir restricciones de entorno de desarrollo y setup operativo del runtime.
- [accepted] OpenSpec y OpenProject no son dependencias funcionales del producto CAFL; si se evaluan, sera como herramientas auxiliares fuera del producto.
- [draft] Instalacion local/global, permisos y herramientas auxiliares pertenecen a CRIT-07.
- [draft] Aprobaciones automaticas pertenecen a CRIT-02 si afectan flujo operativo y a CRIT-05 si dependen de gates.
- [draft] Granularidad de agentes pertenece a CRIT-03, no a implementacion.
- [draft] Formato de contratos pertenece a CRIT-04, no a tooling.
- [draft] Evidencia, fuentes y trazabilidad pertenecen a CRIT-06, aunque alimenten gates y contratos.
- [draft] CRIT-04, CRIT-05, CRIT-06 y CRIT-07 permanecen not-started y sus plantillas quedan alineadas al modelo mixto aprobado por CRIT-03.

## CRIT-01: Intent And Scope

Status: approved

| Campo | Contenido |
| --- | --- |
| Purpose | [accepted] Reconstruir la intencion real del owner y delimitar el alcance minimo antes de cualquier implementacion. |
| Why it is critical | [accepted] Sin intencion y alcance claros, el repo puede seguir expandiendo una interpretacion incorrecta. |
| What was answered | [accepted] CAFL es un framework/plataforma operativo sobre OpenCode para soluciones empresariales Odoo; usuario inicial owner; Odoo unico dominio; autonomia completa con control humano en decisiones criticas; V1 end-to-end con modulo real y acotado; testing/documentacion/evidencia obligatorios; despliegue productivo fuera de alcance inicial. |
| What must NOT be decided yet | [accepted] Arquitectura interna detallada, flujo operativo final, lista final de agentes, contratos finales, gates finales, modelo de trazabilidad detallado y backlog de implementacion. |
| Inputs reviewed | [accepted] Respuestas y aclaraciones CRIT-01 del owner como fuente primaria; `project-truth/` como bootstrap; repo previo solo como evidencia secundaria. |
| Expected outputs | [accepted] Declaracion de intencion, decisiones aceptadas/rechazadas, pendientes derivados, riesgos y glosario actualizados. |
| Acceptance criteria | [accepted] Verificacion independiente CRIT-01: APPROVED; CRIT-01 queda approved para intencion y alcance del producto. |
| Open questions | [accepted] No quedan preguntas abiertas para aprobar CRIT-01; CRIT-03 a CRIT-07 siguen sin resolverse. |
| Dependencies | [accepted] CRIT-01 alimenta CRIT-02, CRIT-03, CRIT-04, CRIT-05, CRIT-06 y CRIT-07, pero no los resuelve. |

## CRIT-02: Operating Flow

Status: approved

| Campo | Contenido |
| --- | --- |
| Purpose | [accepted] Definir el flujo operativo desde idea del owner hasta modulo Odoo listo para produccion tecnica, sin asumir el pipeline actual. |
| Why it is critical | [accepted] El flujo determina que artefactos, roles funcionales, decisiones humanas, gates y evidencias seran necesarios en sesiones posteriores. |
| What was answered | [accepted] CAFL usara flujo hibrido controlado; jerarquia modulo -> capability/feature -> tarea verificable; PRD y SDD ligeros obligatorios; task/context packet y DoR obligatorios; context routing y token budget; bloqueo selectivo por contexto critico; funciones minimas; shift-left verification; risk-based testing; rework acotado; cierre verificable; OpenCode spikes derivados a CRIT-07. |
| What must NOT be decided yet | [accepted] Agentes finales, contratos finales, gates finales, trazabilidad final, arquitectura OpenCode, planificacion detallada, comandos ejecutables, CI/CD final y formatos finales. |
| Inputs reviewed | [accepted] CRIT-01 approved, `project-truth/` y respuesta del owner a CRIT-02 como fuente primaria; repo previo solo como evidencia secundaria. |
| Expected outputs | [accepted] Mapa operativo aprobado, con decisiones de flujo y derivaciones explicitas a CRIT-03, CRIT-04, CRIT-05, CRIT-06 y CRIT-07. |
| Acceptance criteria | [accepted] Cada fase/tarea debe tener salida esperada, evidencia minima, criterios de aceptacion, condicion de bloqueo, rework acotado y cierre verificable. |
| Open questions | [accepted] No quedan preguntas abiertas para aprobar CRIT-02; implementacion concreta queda derivada a CRIT-03 a CRIT-07. |
| Dependencies | [accepted] Depende de CRIT-01 approved y alimenta CRIT-03, CRIT-04, CRIT-05, CRIT-06 y CRIT-07. |

## CRIT-03: Agent Responsibilities

Status: approved

| Campo | Contenido |
| --- | --- |
| Purpose | [accepted] Definir responsabilidades, autoridad conceptual, limites, handoffs y mecanismo candidato por responsabilidad antes de crear o modificar agentes. |
| Why it is critical | [accepted] Evita agents-only, duplicacion, brechas, decisiones opacas, handoffs debiles y uso de prompts como control operativo. |
| What was answered | [accepted] CAFL usara modelo mixto; capacidades minimas consolidadas; owner solo en decisiones criticas; orquestacion mixta; backend base y frontend condicional; QA mixto; seguridad/riesgo/compliance explicito; context routing/token budget separados; task/context packet y DoR obligatorios; rework default 2 ciclos con excepciones escaladas; commands como entradas repetibles; control deterministico futuro para estado, evidencia, tests, permisos, token budget, DoR/DoD estructural y rework counters. |
| What must NOT be decided yet | [accepted] Agentes ejecutables finales, prompts finales, commands finales, SDK/server/scripts implementados, permisos tecnicos finales, contratos finales, gates finales, arquitectura OpenCode final y archivos runtime definitivos. |
| Inputs reviewed | [accepted] `project-truth/spikes/spike-oc-crit03-opencode-responsibility-mapping.md` como input tecnico; `framework/AGENT_CONTRACTS.md` y `framework/agents/*.agent.md` solo como evidencia secundaria; documentos raiz solo como evidencia secundaria. |
| Expected outputs | [accepted] Matriz de responsabilidades conceptuales, mecanismos candidatos, autoridad, handoffs, limites y revision preliminar de agentes actuales. |
| Acceptance criteria | [accepted] CRIT-03 queda aprobado como decision de responsabilidades y mecanismo candidato; no eleva `framework/agents` a verdad oficial ni crea implementacion runtime. |
| Open questions | [accepted] No quedan preguntas abiertas para aprobar CRIT-03; implementacion concreta y criterios finales quedan derivados a CRIT-04, CRIT-05, CRIT-06 y CRIT-07. |
| Dependencies | [accepted] Depende de CRIT-01 y CRIT-02; alimenta CRIT-04, CRIT-05, CRIT-06 y CRIT-07. |

## CRIT-04: Contracts

Status: not-started

| Campo | Contenido |
| --- | --- |
| Purpose | [draft] Definir la estructura contractual para coordinar fases, entregables y mecanismos mixtos. |
| Why it is critical | [draft] Contratos incompletos permiten avanzar con entradas ambiguas y salidas no verificables. |
| What must be decided | [open-question] Tipos de contratos, task/context packet, Definition of Ready, producer/consumer/validator, contexto autorizado/excluido, token budget, campos minimos, formato, versionado y relacion con trazabilidad. |
| What must NOT be decided yet | [draft] Contenido final de cada contrato, gates finales, schemas definitivos, estado persistente, runtime y tooling de validacion. |
| Inputs to review | [draft] CRIT-01/02/03 approved, `project-truth/spikes/spike-oc-crit03-opencode-responsibility-mapping.md`, `framework/CONTRACT_CATALOG.md`, plantillas en `framework/templates/contracts/`, `framework/PRE_PLANNING_ELICITATION.md` como evidencia secundaria. |
| Expected outputs | [draft] Inventario de contratos candidatos y estructura contractual para agent, command, SDK/server/script, rule/config, skill/playbook, human/owner y mixed. |
| Acceptance criteria | [draft] Cada contrato candidato tiene proposito, producer, consumer, validator, entrada, salida, contexto, token budget, evidencia, criterio de suficiencia y criterio de rechazo. |
| Open questions | [open-question] Que contrato minimo evita perder control del modelo mixto sin crear burocracia excesiva? |
| Dependencies | [draft] Depende de CRIT-01, CRIT-02 y CRIT-03; alimenta CRIT-05 y CRIT-06. |

## CRIT-05: Gates And Verification

Status: not-started

| Campo | Contenido |
| --- | --- |
| Purpose | [draft] Definir modelo de gates verificables para avanzar, bloquear, replanificar, aceptar deuda o escalar. |
| Why it is critical | [draft] Gates debiles o no verificables crean confianza falsa y no controlan riesgo. |
| What must be decided | [open-question] Gates minimos, recommendation vs verification vs decision, severidades, categorias, evidencia reproducible, testing suficiente/aplicable, rework default 2 ciclos, deuda, escalamiento y acciones por fallo. |
| What must NOT be decided yet | [draft] Arquitectura OpenCode final, implementacion automatizada, scripts CI finales, commands locales, gates finales y cobertura tecnica no soportada por recursos. |
| Inputs to review | [draft] `framework/GATE_CATALOG.md`, `framework/ci/contract/PIPELINE_CONTRACT.md`, `RISKS.md`, `PROJECT_CONTROL.md`. |
| Expected outputs | [draft] Mapa de gates candidatos con recommendation source, verification method, decision owner, evidencias reproducibles y consecuencias operativas. |
| Acceptance criteria | [draft] Cada gate candidato puede responder que recomienda, que verifica, con que evidencia reproducible, quien decide y que pasa si falla. |
| Open questions | [open-question] Que fallas bloquean siempre y cuales pueden registrarse como deuda aceptada? |
| Dependencies | [draft] Depende de CRIT-01, CRIT-02, CRIT-04 y CRIT-06; alimenta CRIT-07. |

## CRIT-06: State, Evidence And Traceability

Status: not-started

| Campo | Contenido |
| --- | --- |
| Purpose | [draft] Definir modelo persistente y auditable de estado, evidencia, fuentes, contexto, decisiones y trazabilidad sin depender de memoria, conversaciones externas o narrativa LLM. |
| Why it is critical | [draft] Sin trazabilidad se pierden causas de decisiones, fuentes, riesgos, aprobaciones y cambios. |
| What must be decided | [open-question] Estado autoritativo, IDs, decision log, evidence log, source log, context log, excluded/prohibited context log, rework history, token budget usage, fuentes, evidencia minima, matriz de trazabilidad y politica de cambios. |
| What must NOT be decided yet | [draft] Herramientas finales de almacenamiento, schemas definitivos, tooling, automatizacion RAG o dashboards. |
| Inputs to review | [draft] `DECISIONS.md`, `ELICITATION_RECORD.md`, `PROJECT_CONTROL.md`, templates de trazabilidad, RAG y CI. |
| Expected outputs | [draft] Modelo minimo de estado, evidencia, fuentes, contexto, rework y token budget con reglas de actualizacion y auditoria. |
| Acceptance criteria | [draft] Una decision o entrega puede rastrearse a fuente, contexto usado/excluido, evidencia, fecha, estado, impacto, riesgos y artefactos afectados. |
| Open questions | [open-question] Que evidencia es obligatoria para aceptar una decision o entrega? |
| Dependencies | [draft] Depende de CRIT-01 y CRIT-02; alimenta CRIT-04, CRIT-05 y CRIT-07. |

## CRIT-07: Implementation Risks And Resources

Status: not-started

| Campo | Contenido |
| --- | --- |
| Purpose | [draft] Validar setup operativo, recursos, restricciones, riesgos, secuencia y recortes para implementar el modelo mixto aprobado sin reabrir OpenCode como runtime principal. |
| Why it is critical | [draft] Integrar herramientas o prometer automatizacion sin recursos disponibles puede consumir la V1 sin validar valor. |
| What must be decided | [open-question] Entorno Odoo real, instalacion/carga/actualizacion de modulo, tests aplicables, setup operativo OpenCode, agents, commands, SDK/server/scripts, permissions, config, skills, rules/AGENTS.md, operacion local/global, source-vs-runtime, evidencia ejecutable, RAG, CI/CD, Playwright, esfuerzo, secuencia, recortes de alcance y modulo piloto exacto. |
| What must NOT be decided yet | [draft] Codigo, implementacion antes de CRIT-04/05/06, instaladores finales, configuracion activa, runtime files, infraestructura productiva y optimizaciones. |
| Inputs to review | [draft] `framework/INSTALLATION_MODEL.md`, `framework/rag/`, `framework/ci/`, `framework/examples/`, `RISKS.md`. |
| Expected outputs | [draft] Mapa de recursos, setup operativo candidato, restricciones, riesgos bloqueantes, recortes y secuencia candidata de implementacion. |
| Acceptance criteria | [draft] Cada mecanismo/herramienta candidata tiene justificacion, prerequisito, costo, riesgo, evidencia esperada y decision futura de incluir/excluir/postergar. |
| Open questions | [open-question] Que setup operativo, recursos, restricciones, recortes y herramientas auxiliares son necesarios para construir V1 en 2 meses sin convertirlas en dependencias funcionales del producto CAFL? |
| Dependencies | [draft] Depende de CRIT-01, CRIT-02, CRIT-05 y CRIT-06; desbloquea planificacion tecnica. |
