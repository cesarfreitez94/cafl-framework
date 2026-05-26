# Critical Map

Status: READY_FOR_TARGET_OPERATING_MODEL

## Regla De Uso

- [accepted] Este mapa organiza sesiones criticas de elicitacion antes de implementar.
- [accepted] Ningun punto critico produce contratos finales, gates finales, comandos ejecutables o agentes ejecutables por si solo.
- [accepted] La elicitacion critica queda completa con CRIT-01..CRIT-07 approved.
- [accepted] No existe CRIT-08.
- [accepted] Si un tema aparece como critico pero es subpunto de otro, se clasifica dentro del punto que decide su autoridad y consecuencias.

## Clasificacion De Subpuntos

- [accepted] OpenCode ya esta aceptado como runtime principal por CRIT-01; CRIT-07 solo debe definir restricciones de entorno de desarrollo y setup operativo del runtime.
- [accepted] OpenSpec y OpenProject no son dependencias funcionales del producto CAFL; si se evaluan, sera como herramientas auxiliares fuera del producto.
- [accepted] Instalacion local/global, permisos y herramientas auxiliares quedaron tratados por CRIT-07 como direccion candidata y validaciones posteriores, no como implementacion cerrada.
- [accepted] Aprobaciones automaticas pertenecen a CRIT-02 si afectan flujo operativo y a CRIT-05 si dependen de gates; CRIT-07 no crea automatizacion final de aprobaciones.
- [accepted] Granularidad de agentes pertenece a CRIT-03; CRIT-07 aprobo capacidades consolidadas y modelo hibrido progresivo sin crear agents ejecutables.
- [accepted] Formato de contratos pertenece a CRIT-04; CRIT-07 aprobo schemas V1 minimos versionados y validators minimos como direccion, no contratos finales.
- [accepted] Evidencia, fuentes, storage logico, logs, IDs conceptuales, gate log y trazabilidad contract -> gate -> evidence pertenecen a CRIT-06, aunque alimenten gates y contratos.
- [accepted] Schemas V1 minimos versionados, validators minimos, commands candidatos, SDK/server fuera de core V1 salvo spike, scripts/CLI por spike, permissions, runtime candidate y materializacion tecnica de CRIT-04/05/06 fueron tratados por CRIT-07 como direccion aprobada, no como implementacion.
- [accepted] Knowledge/source governance logico, source registry, curated documentation registry, source snapshots/versiones, trust/freshness/applicability, source usage, Curation Mode, Knowledge Gap y bloqueo por falta de fuente autorizada suficiente pertenecen a CRIT-06.
- [accepted] Implementacion fisica/runtime candidata de knowledge base fue tratada por CRIT-07: curated files + lightweight source registry + knowledge artifacts + skills/playbooks para V1; RAG/base vectorial queda diferido.
- [accepted] CRIT-04 queda approved como modelo contractual conceptual; CRIT-05 queda approved como modelo conceptual de gates y verificacion; CRIT-06 queda approved como modelo logico/conceptual de estado/evidencia/trazabilidad/knowledge governance; CRIT-07 queda approved como viabilidad/direccion candidata de runtime y cierre de elicitacion critica.
- [accepted] `framework/` queda descartado como input de diseno y aprobado para eliminacion por CRIT-07; no debe usarse para layout, agents, commands, contracts, gates, schemas, validators, runtime ni knowledge base.

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
| Inputs reviewed | [accepted] `project-truth/spikes/spike-oc-crit03-opencode-responsibility-mapping.md` como input tecnico y fuentes primarias de `project-truth/`; cualquier referencia historica a legacy no tiene autoridad futura por CRIT-07. |
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
| Inputs reviewed | [accepted] CRIT-01/02/03 approved, CRIT-04 Contracts Technical Elicitation, aprobacion del owner y `project-truth/spikes/spike-oc-crit03-opencode-responsibility-mapping.md`; cualquier referencia historica a legacy no tiene autoridad futura por CRIT-07. |
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
| Inputs reviewed | [accepted] CRIT-01/02/03/04 approved, CRIT-05 Gates and Verification Technical Elicitation, aprobacion del owner y fuentes primarias en `project-truth/`; cualquier referencia historica a legacy no tiene autoridad futura por CRIT-07. |
| Expected outputs | [accepted] Modelo conceptual de gates con recommendation source, verification method, decision owner, evidencias reproducibles y consecuencias operativas. |
| Acceptance criteria | [accepted] Cada gate conceptual puede responder que recomienda, que verifica, con que evidencia reproducible, quien decide y que pasa si falla; CRIT-05 no crea gates finales ejecutables. |
| Open questions | [accepted] No quedan preguntas abiertas para aprobar CRIT-05 como modelo conceptual; CRIT-06 ya resolvio estado/evidencia/trazabilidad logica y CRIT-07 conserva decisiones de implementacion pendientes. |
| Dependencies | [accepted] Depende de CRIT-01, CRIT-02, CRIT-03 y CRIT-04; alimenta CRIT-06 y CRIT-07. |

## CRIT-06: State, Evidence, Traceability And Knowledge Governance

Status: approved

| Campo | Contenido |
| --- | --- |
| Purpose | [accepted] Definir modelo logico/conceptual persistente y auditable de storage logico, estado autoritativo, evidencia, fuentes, contexto, decisiones, logs, IDs, trazabilidad y knowledge/source governance sin depender de memoria, conversaciones externas, busqueda web libre o narrativa LLM. |
| Why it is critical | [accepted] Sin trazabilidad y governance de fuentes se pierden causas de decisiones, fuentes, vigencia, riesgos, aprobaciones, cambios y autoridad del conocimiento usado por CAFL. |
| What was answered | [accepted] Estado autoritativo en registros logicos versionables y trazables; narrativa LLM no es estado; persistencia conceptual de estado, decisiones, contratos/packets, gates, evidencia, fuentes, contexto, token/context usage, rework, deuda, approvals, knowledge artifacts, snapshots, source usage, integration packs y cambios de estado; IDs obligatorios y condicionales; logs obligatorios y condicionales; trazabilidad modulo -> capability/feature -> tarea y contract -> gate -> evidence; evidencia reproducible; source registry; knowledge artifacts; integration knowledge packs; Curation Mode; Knowledge Gap; bootstrap incremental; Python solo aplicado a Odoo; extensibilidad a dominios futuros. |
| What must NOT be decided yet | [accepted] Schemas finales, validators finales, commands finales, scripts, storage fisico, configuracion runtime, tooling, automatizacion RAG, RAG final, base vectorial final, base de datos final, ingesta, dashboards, ejecucion reproducible real o resolucion de CRIT-07. |
| Inputs reviewed | [accepted] CRIT-01/02/03/04/05 approved, CRIT-06 Technical Elicitation y aprobacion del owner; fuentes primarias en `project-truth/`; cualquier referencia historica a legacy no tiene autoridad futura por CRIT-07. |
| Expected outputs | [accepted] Modelo logico de estado, storage logico, persistencia conceptual, IDs, logs, evidencia, fuentes, contexto, rework, deuda, approvals, trazabilidad y knowledge/source governance; handoff explicito a CRIT-07 para implementacion fisica/runtime. |
| Acceptance criteria | [accepted] Una decision o entrega puede rastrearse a fuente, contexto usado/excluido/prohibido, evidence log, gate log, contract relacionado, fecha, estado, impacto, riesgos, knowledge artifact y artefactos afectados; narrativa LLM, busqueda web libre y estado autoritativo quedan diferenciados. |
| Open questions | [accepted] No quedan preguntas abiertas para aprobar CRIT-06 como modelo logico/conceptual; implementacion fisica/runtime queda derivada a CRIT-07. |
| Dependencies | [accepted] Depende de CRIT-01, CRIT-02, CRIT-03, CRIT-04 y CRIT-05; alimenta CRIT-07. |

## CRIT-07: Implementation Risks, Resources, Runtime And Feasibility

Status: approved

| Campo | Contenido |
| --- | --- |
| Purpose | [accepted] Definir viabilidad, direccion candidata de runtime, recursos, riesgos, recortes V1 y criterios para implementacion posterior del modelo mixto aprobado, sin reabrir OpenCode como runtime principal y sin crear implementacion. |
| Why it is critical | [accepted] Sin CRIT-07 V1 podia quedar como agents-only, automatizacion debil, scope creep de RAG/SDK/server/dashboard/CI/CD o sin entorno Odoo 18 verificable. |
| What was answered | [accepted] Operating model hibrido progresivo; runtime candidate OpenCode + commands + scripts/CLI/validators locales + storage simple; `framework/` descartado y aprobado para eliminacion; Odoo 18 target; V1 con automatizacion minima suficiente; scripts/CLI language por spike; schemas V1 minimos no permanentes; SDK/server fuera de core V1 salvo spike favorable; KB V1 con curated files/source registry/artifacts/skills; RAG/base vectorial diferido; piloto preferido solicitudes internas/aprobaciones simples; capacidades no V1 diferidas a V2/post-V1, no rechazadas. |
| What must NOT be decided yet | [accepted] Implementation Blueprint, backlog tecnico, runtime skeleton, rutas finales, schemas fisicos finales, validators reales, commands reales, scripts, SDK/server core, RAG, base vectorial, DB avanzada, entorno Odoo exacto, piloto final y secuencia detallada post-CRIT-07. |
| Inputs reviewed | [accepted] CRIT-01/02/03/04/05/06 approved, CRIT-07 Technical Elicitation y aprobacion del owner; `project-truth/` como fuente de verdad. `framework/` no fue input y queda descartado. |
| Expected outputs | [accepted] Decisiones CRIT-07 aprobadas, runtime candidate direction, recortes V1, riesgos, recursos, criterios de automatizacion minima suficiente, capacidades diferidas y handoff a trabajos posteriores sin CRIT-08. |
| Acceptance criteria | [accepted] CRIT-07 queda approved; CRIT-01..07 completos; no existe CRIT-08; no se implementa runtime; no se crean artefactos ejecutables; no se impone planificacion detallada posterior. |
| Open questions | [accepted] No quedan preguntas abiertas para aprobar CRIT-07; los detalles fisicos y tecnicos quedan para Consolidated Truth Review, Target Operating Model, Implementation Blueprint, technical validations/spikes, backlog tecnico e implementacion controlada segun corresponda. |
| Dependencies | [accepted] Depende de CRIT-01, CRIT-02, CRIT-03, CRIT-04, CRIT-05 y CRIT-06; cierra la elicitacion critica y habilita trabajos posteriores definidos formalmente. |

## Elicitacion Critica Completa

- [accepted] CRIT-01..CRIT-07 quedan completos.
- [accepted] Consolidated Truth Review quedo `READY_FOR_TARGET_OPERATING_MODEL`.
- [accepted] `project-truth/TOM.md` existe como especificacion/working contract para elaborar el Target Operating Model.
- [pending] El Target Operating Model operativo completo sigue pendiente de elaboracion y aprobacion explicita del owner.
- [accepted] El siguiente trabajo sigue siendo Target Operating Model.
- [accepted] CRIT-08 no existe.
- [accepted] El siguiente paso debe definirse formalmente a partir de las decisiones aprobadas, sin imponer en este mapa una secuencia detallada post-CRIT-07.
