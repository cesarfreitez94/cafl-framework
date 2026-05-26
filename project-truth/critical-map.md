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
- [draft] Evidencia, fuentes, storage logico, logs, IDs conceptuales, gate log y trazabilidad contract -> gate -> evidence pertenecen a CRIT-06, aunque alimenten gates y contratos.
- [draft] Schemas finales, validators, commands, SDK/server/scripts, permissions, runtime, rutas/ubicaciones runtime y materializacion tecnica de CRIT-04/05/06 pertenecen a CRIT-07.
- [accepted] CRIT-04 queda approved como modelo contractual conceptual; CRIT-05 queda approved como modelo conceptual de gates y verificacion; CRIT-06 y CRIT-07 permanecen not-started.

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
| Open questions | [accepted] No quedan preguntas abiertas para aprobar CRIT-01; las sesiones posteriores mantienen su propio estado de aprobacion. |
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
| Open questions | [accepted] No quedan preguntas abiertas para aprobar CRIT-02; implementacion concreta queda derivada a las sesiones posteriores segun su estado. |
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
| Open questions | [accepted] No quedan preguntas abiertas para aprobar CRIT-03; CRIT-04 ya resolvio modelo contractual conceptual y la implementacion concreta queda derivada a CRIT-05, CRIT-06 y CRIT-07 segun corresponda. |
| Dependencies | [accepted] Depende de CRIT-01 y CRIT-02; alimenta CRIT-04, CRIT-05, CRIT-06 y CRIT-07. |

## CRIT-04: Contracts

Status: approved

| Campo | Contenido |
| --- | --- |
| Purpose | [accepted] Definir la estructura contractual conceptual para coordinar fases, entregables y mecanismos mixtos. |
| Why it is critical | [accepted] Contratos incompletos permiten avanzar con entradas ambiguas, contexto no controlado y salidas no verificables. |
| What was answered | [accepted] CAFL usara modelo hibrido: contrato base comun mas extensiones por fase, mecanismo y riesgo; task/context packet obligatorio; DoR validada por receptor o validador; producer, consumer y validator explicitos; consumer puede rechazar; context routing y token budget por contrato; evidencia no solo narrativa; contratos V1 clasificados como `always-required` y `conditional-required`; `blockers` en task/context packet es conditional con `none` explicito si no hay blockers conocidos. |
| What must NOT be decided yet | [accepted] Contenido final de cada contrato, gates finales, severidades, acciones por fallo, schemas definitivos, estado persistente, runtime, commands, agents ejecutables, validators y tooling de validacion. |
| Inputs reviewed | [accepted] CRIT-01/02/03 approved, CRIT-04 Contracts Technical Elicitation, aprobacion del owner y `project-truth/spikes/spike-oc-crit03-opencode-responsibility-mapping.md`; `framework/CONTRACT_CATALOG.md`, `framework/AGENT_CONTRACTS.md`, `framework/agents/*.agent.md` y otros documentos del repo solo como evidencia secundaria. |
| Expected outputs | [accepted] Modelo contractual conceptual, inventario V1 `always-required` y `conditional-required`, matriz contractual conceptual, campos candidatos del task/context packet y handoff a CRIT-05/06/07. |
| Acceptance criteria | [accepted] Cada contrato candidato tiene proposito, producer, consumer, validator, entrada, salida, contexto, token budget, evidencia, criterio de suficiencia y criterio de rechazo; el modelo cubre human, agent, command, SDK/server/script, rule/config/skill y mixed sin implementar runtime. |
| Open questions | [accepted] No quedan preguntas abiertas para aprobar CRIT-04 como modelo contractual conceptual; CRIT-05 ya aprobo gates conceptuales y los detalles finales de estado/runtime quedan derivados a CRIT-06 y CRIT-07. |
| Dependencies | [accepted] Depende de CRIT-01, CRIT-02 y CRIT-03; alimenta CRIT-05, CRIT-06 y CRIT-07. |

## CRIT-05: Gates And Verification

Status: approved

| Campo | Contenido |
| --- | --- |
| Purpose | [accepted] Definir modelo conceptual de gates verificables para avanzar, bloquear, replanificar, aceptar deuda o escalar. |
| Why it is critical | [accepted] Gates debiles o no verificables crean confianza falsa y no controlan riesgo. |
| What was answered | [accepted] CAFL V1 usara modelo hibrido: gates minimos independientes, checks transversales obligatorios dentro de gates y gates condicionales por riesgo/evento; separa gate recommendation, gate verification y gate decision; severidades `blocker`, `critical`, `high`, `medium`, `low`, `warning/info`; acciones por fallo; DoD verificable por task/capability-feature/module; testing suficiente/aplicable risk-based; shift-left verification; evidencia reproducible conceptual; seguridad/riesgo/compliance transversal; deuda tecnica menor aceptable condicionada; deuda funcional no aceptable para produccion tecnica; rework default 2 ciclos y tercer ciclo significativo con escalamiento. |
| What must NOT be decided yet | [accepted] Arquitectura OpenCode final, implementacion automatizada, scripts CI finales, commands locales, gates finales ejecutables, schemas finales, validators finales, storage/logs finales y cobertura tecnica no soportada por recursos. |
| Inputs reviewed | [accepted] CRIT-01/02/03/04 approved, CRIT-05 Gates and Verification Technical Elicitation, aprobacion del owner y fuentes primarias en `project-truth/`; `framework/` y documentos raiz solo como evidencia secundaria. |
| Expected outputs | [accepted] Modelo conceptual de gates con recommendation source, verification method, decision owner, evidencias reproducibles y consecuencias operativas. |
| Acceptance criteria | [accepted] Cada gate conceptual puede responder que recomienda, que verifica, con que evidencia reproducible, quien decide y que pasa si falla; CRIT-05 no crea gates finales ejecutables. |
| Open questions | [accepted] No quedan preguntas abiertas para aprobar CRIT-05 como modelo conceptual; CRIT-06 y CRIT-07 conservan sus decisiones pendientes. |
| Dependencies | [accepted] Depende de CRIT-01, CRIT-02, CRIT-03 y CRIT-04; alimenta CRIT-06 y CRIT-07. |

## CRIT-06: State, Evidence And Traceability

Status: not-started

| Campo | Contenido |
| --- | --- |
| Purpose | [draft] Definir modelo logico/conceptual persistente y auditable de storage, estado autoritativo, evidencia, fuentes, contexto, decisiones, logs y trazabilidad sin depender de memoria, conversaciones externas o narrativa LLM. |
| Why it is critical | [draft] Sin trazabilidad se pierden causas de decisiones, fuentes, riesgos, aprobaciones y cambios. |
| What must be decided | [open-question] Storage logico, persistencia conceptual, estado autoritativo, IDs conceptuales, decision log, evidence log, source log, context log, excluded/prohibited context log, gate log, rework history, token/context usage, fuentes, evidencia minima, matriz modulo -> capability/feature -> tarea y relacion contract -> gate -> evidence. |
| What must NOT be decided yet | [draft] Schemas finales, validators finales, commands finales, storage fisico, configuracion runtime, tooling, automatizacion RAG, dashboards o resolucion de CRIT-07. |
| Inputs to review | [draft] `DECISIONS.md`, `ELICITATION_RECORD.md`, `PROJECT_CONTROL.md`, templates de trazabilidad, RAG y CI. |
| Expected outputs | [draft] Modelo minimo de storage logico, estado autoritativo, IDs conceptuales, decision/evidence/source/context/excluded-prohibited/gate logs, rework, token/context usage y trazabilidad contract -> gate -> evidence con reglas de actualizacion y auditoria. |
| Acceptance criteria | [draft] Una decision o entrega puede rastrearse a fuente, contexto usado/excluido/prohibido, evidence log, gate log, contract relacionado, fecha, estado, impacto, riesgos y artefactos afectados; narrativa LLM y estado autoritativo quedan diferenciados. |
| Open questions | [open-question] Que evidencia es obligatoria para aceptar una decision o entrega? |
| Dependencies | [draft] Depende de CRIT-01, CRIT-02, CRIT-04 y CRIT-05; alimenta CRIT-07. |

## CRIT-07: Implementation Risks And Resources

Status: not-started

| Campo | Contenido |
| --- | --- |
| Purpose | [draft] Validar setup operativo, schemas finales, validators, commands, SDK/server/scripts, permissions, runtime, rutas, recursos, restricciones, riesgos, secuencia y recortes para implementar el modelo mixto aprobado sin reabrir OpenCode como runtime principal. |
| Why it is critical | [draft] Integrar herramientas o prometer automatizacion sin recursos disponibles puede consumir la V1 sin validar valor. |
| What must be decided | [open-question] Schemas finales, validators, commands, SDK/server/scripts, permissions, OpenCode runtime setup, rutas/ubicaciones runtime, entorno Odoo real, instalacion/carga/actualizacion de modulo, tests aplicables, ejecucion reproducible, tooling operativo, source-vs-runtime, materializacion tecnica de CRIT-04 contracts, CRIT-05 gates y CRIT-06 state/evidence/traceability, evidencia ejecutable, RAG, CI/CD, Playwright, recursos, riesgos, plan, secuencia, recortes de alcance, modulo piloto exacto y plazo de 2 meses como restriccion. |
| What must NOT be decided yet | [draft] Codigo, implementacion efectiva, archivos runtime activos, instaladores finales, infraestructura productiva, optimizaciones, reapertura de OpenCode como runtime principal o propuesta de CRIT-08. |
| Inputs to review | [draft] `framework/INSTALLATION_MODEL.md`, `framework/rag/`, `framework/ci/`, `framework/examples/`, `RISKS.md`. |
| Expected outputs | [draft] Mapa de recursos, setup operativo candidato, schemas finales, validators, commands, SDK/server/scripts, permissions, rutas/ubicaciones runtime, restricciones, riesgos bloqueantes, recortes y secuencia candidata de implementacion compatible con 2 meses. |
| Acceptance criteria | [draft] Cada mecanismo/herramienta candidata tiene justificacion, prerequisito, costo, riesgo, evidencia esperada y decision futura de incluir/excluir/postergar; la materializacion tecnica de CRIT-04/05/06 queda definida sin crear implementacion, cerrando la elicitacion critica antes del Consolidated Truth Review y sin proponer CRIT-08. |
| Open questions | [open-question] Que setup operativo, recursos, restricciones, recortes y herramientas auxiliares son necesarios para construir V1 en 2 meses sin convertirlas en dependencias funcionales del producto CAFL? |
| Dependencies | [draft] Depende de CRIT-01, CRIT-02, CRIT-05 y CRIT-06; desbloquea planificacion tecnica. |
