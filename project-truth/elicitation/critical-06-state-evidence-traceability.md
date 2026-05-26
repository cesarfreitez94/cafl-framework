# CRIT-06: State, Evidence, Traceability And Knowledge Governance

Status: approved

## Session Objective

- [accepted] Definir a nivel logico/conceptual el storage logico, estado autoritativo, evidencia, fuentes, contexto, decisiones, logs, IDs, trazabilidad, persistencia conceptual y knowledge/source governance de CAFL.
- [accepted] CRIT-06 define como CAFL sabe, registra, audita y gobierna que se decidio, que se ejecuto, que evidencia existe, que fuentes se usaron, que contexto se excluyo, que gate paso/fallo, que rework ocurrio, que estado es autoritativo y que conocimiento tecnico esta autorizado.
- [accepted] CRIT-06 no define schemas finales, validators finales, commands, scripts, RAG final, base vectorial, base de datos final, runtime OpenCode, rutas runtime, storage fisico ni implementacion.

## Context

- [accepted] CRIT-01 Intent and Scope esta approved.
- [accepted] CRIT-02 Operating Flow esta approved.
- [accepted] CRIT-03 Agent Responsibilities esta approved.
- [accepted] CRIT-04 Contracts esta approved como modelo contractual conceptual.
- [accepted] CRIT-05 Gates And Verification esta approved como modelo conceptual de gates y verificacion.
- [accepted] La unidad de control aprobada es modulo -> capability/feature -> tarea verificable.
- [accepted] Context routing, token budget, contexto excluido/prohibido, evidencia, testing y rework acotado son obligatorios por CRIT-02/CRIT-03/CRIT-04/CRIT-05.
- [accepted] `project-truth/` mantiene autoridad sobre verdad del proyecto; `framework/` y documentos raiz siguen siendo evidencia secundaria hasta validacion explicita.
- [accepted] CRIT-07 definira la materializacion fisica/runtime de CRIT-06.

## Owner Approval

- [accepted] El owner aprobo las recomendaciones de CRIT-06 State, Evidence, Traceability and Knowledge Governance Technical Elicitation con ajustes obligatorios.
- [accepted] Ajuste obligatorio 1: IDs obligatorios siempre y IDs obligatorios cuando aplique quedan diferenciados.
- [accepted] Ajuste obligatorio 2: logs minimos V1 obligatorios y logs minimos V1 condicionales quedan diferenciados.
- [accepted] Ajuste obligatorio 3: Curation Mode requiere fuente aprobada por owner o source policy antes de busqueda externa.
- [accepted] Ajuste obligatorio 4: busqueda web libre queda prohibida como fuente directa de implementacion.
- [accepted] Ajuste obligatorio 5: bootstrap incremental permite construir source registry y artifacts bajo demanda, pero no permite implementar sin conocimiento autorizado suficiente.
- [accepted] Ajuste obligatorio 6: CRIT-06 no crea ni propone CRIT-08.

## Approved Decisions

- [accepted] DEC-CRIT06-01: El estado autoritativo de CAFL vive en registros logicos autoritativos, versionables y trazables; la narrativa LLM puede explicar, recomendar o resumir, pero nunca constituye estado autoritativo por si sola.
- [accepted] DEC-CRIT06-02: Deben persistirse conceptualmente estado, decisiones, contratos/packets, gates, evidencia, fuentes, contexto usado/excluido/prohibido, token/context usage, rework, deuda, aprobaciones, knowledge artifacts, source snapshots, source usage, integration knowledge packs y cambios de estado.
- [accepted] DEC-CRIT06-03: CAFL usara IDs conceptuales para todos los elementos necesarios de trazabilidad, diferenciando IDs obligatorios siempre e IDs obligatorios cuando aplique; formato fisico, nomenclatura final y schemas quedan para CRIT-07.
- [accepted] DEC-CRIT06-04: CAFL usara logs minimos V1 obligatorios y condicionales; todos forman parte del modelo logico, pero no todos deben generar entrada independiente en cada tarea.
- [accepted] DEC-CRIT06-05: La trazabilidad jerarquica modulo -> capability/feature -> tarea verificable es la columna vertebral del estado operativo.
- [accepted] DEC-CRIT06-06: Todo gate result debe enlazar contrato/packet aplicable, verificacion, decision, evidencia y consecuencia operativa; un contrato completo no aprueba por si solo un gate.
- [accepted] DEC-CRIT06-07: La evidencia auditable debe registrar tipo, origen, accion/comando/test si aplica, resultado, timestamp logico, relacion con tarea/gate/contrato, fuentes usadas, limitaciones y narrativa explicativa secundaria.
- [accepted] DEC-CRIT06-08: Deben registrarse fuentes usadas, autorizadas, secundarias, excluidas, prohibidas/no relevantes, excepciones, aplicabilidad, vigencia/freshness y trust level.
- [accepted] DEC-CRIT06-09: Token/context usage debe registrarse a nivel conceptual con budget class, contexto asignado, contexto usado, excepciones, razon de expansion e impacto estimado; medicion runtime final queda para CRIT-07.
- [accepted] DEC-CRIT06-10: Rework, deuda aceptada y aprobaciones del owner deben registrarse como logs enlazados a tarea, gate, evidencia previa, evidencia nueva, causa, severidad, aprobacion, condicion de pago y escalamiento.
- [accepted] DEC-CRIT06-11: El modelo de conocimiento debe usar knowledge domain, subdomain, sources, artifacts, applicability, patterns, anti-patterns, examples, recommendations y policies; V1 es Odoo, pero el modelo debe permitir dominios futuros sin redisenar el framework.
- [accepted] DEC-CRIT06-12: Debe existir un modelo logico de source registry con official source, curated source, secondary source, prohibited source, source snapshot/version, trust level, freshness/vigencia, applicability y stewardship.
- [accepted] DEC-CRIT06-13: La base de conocimiento debe transformar fuentes en knowledge artifacts curados con regla/recomendacion, fuente, aplicabilidad, warnings, patterns, anti-patterns, examples y evidencia.
- [accepted] DEC-CRIT06-14: V1 debe cubrir conocimiento Odoo, Odoo ORM, security/access, views/actions/menus, models/fields/constraints, data XML/CSV, testing, performance, module structure, OWL/frontend Odoo, Playwright/testing frontend aplicable, buenas practicas, anti-patrones y ejemplos tecnicos validados; Python entra solo como Python aplicado a Odoo.
- [accepted] DEC-CRIT06-15: Las integraciones externas deben modelarse como integration knowledge packs con proveedor, tipo, fuentes oficiales, snapshots/versiones, ambientes, autenticacion/autorizacion, certificados/tokens/firmas si aplica, endpoints, payloads, errores, rate limits si aplica, datos sensibles, seguridad, compliance, ejemplos oficiales, pruebas recomendadas, vigencia, riesgos y trazabilidad hacia PRD/SDD/task/test/gate/evidence.
- [accepted] DEC-CRIT06-16: Deben existir politicas logicas de update, validation, deprecation y stewardship para knowledge/source governance.
- [accepted] DEC-CRIT06-17: La ausencia de conocimiento autorizado suficiente debe generar Knowledge Gap, Curation Request y bloqueo de implementacion hasta que exista fuente/artifact/pack autorizado suficiente; busqueda externa solo puede ocurrir en Curation Mode controlado.
- [accepted] DEC-CRIT06-18: CRIT-06 define modelo logico/conceptual; CRIT-07 define schemas finales, validators, commands, SDK/server/scripts, permissions, OpenCode runtime setup, rutas, storage fisico, RAG o no RAG, base vectorial o no, archivos curados o base de datos, ingesta/actualizacion, procesamiento Swagger/OpenAPI/PDFs y ejecucion reproducible real.

## Mandatory ID Classification

### Always Required IDs

- [accepted] `module_id`.
- [accepted] `capability_feature_id`.
- [accepted] `task_id`.
- [accepted] `contract_id`.
- [accepted] `packet_id`.
- [accepted] `gate_result_id`.
- [accepted] `evidence_id`.
- [accepted] `decision_id`.
- [accepted] `risk_id`.
- [accepted] `source_id`.
- [accepted] `context_event_id`.
- [accepted] `status_change_id`.

### Conditional Required IDs

- [accepted] `source_snapshot_id`.
- [accepted] `source_usage_id`.
- [accepted] `knowledge_artifact_id`.
- [accepted] `integration_pack_id`.
- [accepted] `pattern_id`.
- [accepted] `anti_pattern_id`.
- [accepted] `example_id`.
- [accepted] `token_usage_id`.
- [accepted] `rework_cycle_id`.
- [accepted] `debt_id`.
- [accepted] `owner_approval_id`.
- [accepted] `blocker_id`.

## Mandatory Log Classification

### Always Required Minimum V1 Logs

- [accepted] State / Status Change Log.
- [accepted] Decision Log.
- [accepted] Contract / Packet Registry.
- [accepted] Gate Log.
- [accepted] Evidence Log.
- [accepted] Source Registry / Source Log.
- [accepted] Context Log.
- [accepted] Rework History.
- [accepted] Approval Log.

### Conditional Minimum V1 Logs

- [accepted] Source Snapshot Log.
- [accepted] Source Usage Log.
- [accepted] Excluded/Prohibited Context Log.
- [accepted] Token/Context Usage Log.
- [accepted] Debt Log.
- [accepted] Knowledge Registry Log.
- [accepted] Integration Source Log.

## Logical State Model

| Logical component | Purpose | Producer | Consumer | Authority level | Required relationships | Related CRIT | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Authoritative State Ledger | Registrar estado aceptado, bloqueado, rechazado, superado o cerrado | Orquestacion, validators, owner | Todos | Autoritativo primario | decision, gate, evidence, approval, status change | CRIT-06, CRIT-07 | Narrativa LLM no es estado |
| Module/Capability/Task Registry | Mantener jerarquia operativa | Orquestacion | Agents, QA, owner | Autoritativo para unidad de control | module -> capability/feature -> task | CRIT-02, CRIT-06 | Columna vertebral del estado |
| Decision Log | Registrar decisiones y autoridad | Owner, orquestacion | Todos | Autoritativo si accepted | source, evidence, risk, approval | CRIT-01, CRIT-06 | Diferencia decision de recomendacion |
| Contract/Packet Registry | Registrar contratos y task/context packets | Productor de fase | Receptor, validator | Autoritativo para handoff | producer, consumer, validator, context, evidence expected | CRIT-04, CRIT-06 | No equivale a gate aprobado |
| Gate Log | Registrar recommendation, verification y decision | QA, reviewer, orquestacion, owner | Orquestacion, owner | Autoritativo para avance/bloqueo | contract -> gate -> evidence -> action | CRIT-05, CRIT-06 | Incluye severidad y accion |
| Evidence Log | Registrar evidencia auditable | QA, scripts futuros, agents, owner | Gates, closure, owner | Autoritativo como soporte | task, gate, contract, source, limitation | CRIT-05, CRIT-06 | Narrativa es secundaria |
| Source Registry | Clasificar fuentes | Knowledge steward, curator | Agents, architect, QA | Autoritativo para fuente permitida | source, domain, trust, freshness, applicability | CRIT-06, CRIT-07 | Incluye official/curated/secondary/prohibited |
| Source Snapshot Registry | Registrar version/captura de fuente | Curator, tooling futuro | Knowledge artifacts, evidence | Autoritativo para version usada | source -> snapshot -> artifact | CRIT-06, CRIT-07 | Fisico queda CRIT-07 |
| Source Usage Log | Registrar uso de fuente/artifact | Agents, curator, orquestacion | Gates, evidence, audit | Autoritativo para trazabilidad | source/artifact -> decision/output | CRIT-06 | Evita fuente invisible |
| Context Log | Registrar contexto asignado/usado | Context routing capability | Receptor, gate | Autoritativo para contexto usado | packet, sources, files, reason | CRIT-04, CRIT-06 | No leer todo el repo por defecto |
| Excluded/Prohibited Context Log | Registrar contexto excluido/prohibido | Context routing, curator | Receptor, QA | Autoritativo para exclusion | packet, source, reason, risk | CRIT-04, CRIT-06 | Condicional segun existencia de exclusion relevante |
| Token/Context Usage Log | Registrar budget class y excepciones | Context routing, runtime futuro | Orquestacion, owner | Autoritativo conceptual | packet, budget, expansion reason | CRIT-04, CRIT-06, CRIT-07 | Medicion exacta queda CRIT-07 |
| Rework History | Registrar ciclos y causas | QA, orquestacion | Builder, owner | Autoritativo para limite de rework | gate failure -> rework -> new evidence | CRIT-05, CRIT-06 | Default 2 ciclos |
| Debt Log | Registrar deuda tecnica aceptada | QA, orquestacion, owner | Closure, owner | Autoritativo si aprobada | debt -> impact -> approval -> pay condition | CRIT-05, CRIT-06 | Condicional; no deuda funcional |
| Approval Log | Registrar aprobaciones owner/autoridad | Owner, orquestacion | Gates, closure | Autoritativo para decisiones criticas | approval -> decision/gate/debt/replan | CRIT-05, CRIT-06 | Evita aprobaciones en memoria |
| Knowledge Registry | Registrar domains, artifacts, patterns, anti-patterns | Curator, architect | Agents, packets, gates | Autoritativo para conocimiento curado | domain -> artifact -> source snapshot | CRIT-06, CRIT-07 | No implica RAG final |
| Integration Pack Registry | Registrar knowledge packs de integracion | Curator, architect | SDD, tasks, QA | Autoritativo si pack aprobado | provider -> sources -> endpoints -> tests | CRIT-06, CRIT-07 | Condicional si hay integracion |

## Traceability Rules

- [accepted] La trazabilidad minima debe cubrir modulo -> capability/feature -> tarea.
- [accepted] La trazabilidad minima debe cubrir idea -> PRD -> SDD -> task/context packet.
- [accepted] La trazabilidad minima debe cubrir contract -> gate -> evidence.
- [accepted] La trazabilidad minima debe cubrir gate failure -> rework -> new evidence.
- [accepted] La trazabilidad minima debe cubrir risk/compliance issue -> escalation -> owner decision.
- [accepted] La trazabilidad minima debe cubrir source/context -> decision/output.
- [accepted] La trazabilidad minima debe cubrir source snapshot -> knowledge artifact -> recommendation.
- [accepted] La trazabilidad minima debe cubrir knowledge artifact -> task/context packet -> implementation decision.
- [accepted] La trazabilidad minima debe cubrir pattern/anti-pattern -> SDD/task/gate cuando aplique.
- [accepted] La trazabilidad minima debe cubrir integration knowledge pack -> SDD/task/test/gate/evidence cuando aplique.
- [accepted] La trazabilidad minima debe cubrir debt -> approval -> payment condition cuando aplique.

## Evidence Policy

- [accepted] Evidencia reproducible no puede ser solo narrativa LLM.
- [accepted] La evidencia auditable debe registrar tipo, origen, accion/comando/test si aplica, resultado, timestamp logico, relacion con tarea/gate/contrato, fuentes usadas, limitaciones y narrativa explicativa secundaria.
- [accepted] La evidencia puede ser manual, documental o producida por commands/scripts/tests futuros, pero CRIT-06 no crea esos mecanismos.
- [accepted] Si una evidencia minima falta, el gate aplicable debe bloquear, rework, escalar o rechazar segun CRIT-05.

## Knowledge And Source Governance Model

- [accepted] CAFL debe consultar primero base de conocimiento curada, documentacion oficial registrada, snapshots/versiones autorizadas, source registry, skills/playbooks aprobados, patrones/anti-patrones validados, ejemplos internos autorizados e integration knowledge packs aprobados.
- [accepted] El modelo de conocimiento debe ser replicable y extensible mediante knowledge domains y subdomains.
- [accepted] V1 debe cubrir inicialmente Odoo, Odoo ORM, Odoo security/access rules, Odoo views/actions/menus, Odoo models/fields/constraints, Odoo data/XML/CSV, Odoo testing, Odoo performance, Odoo module structure, Odoo backend Python aplicado a Odoo, OWL/frontend Odoo, Playwright/testing frontend aplicable, buenas practicas Odoo, anti-patrones Odoo, ejemplos tecnicos validados e integraciones externas.
- [accepted] Python queda incluido solo como conocimiento aplicado a Odoo: ORM, recordsets, create/write/search/read_group, decorators Odoo, constraints, computed fields, batch operations, performance, testing Odoo y anti-patrones Python/Odoo.
- [accepted] Quedan fuera Python generico como framework independiente, Django, FastAPI, Flask, patrones Python que contradigan Odoo y soluciones Python externas no aplicables a Odoo.
- [accepted] El modelo debe permitir dominios futuros como legal-compliance, tax-regulation, public-sector-processes, accounting, industry-specific-rules y regulatory-reporting sin redisenar el framework.

## Source Registry And Knowledge Artifact Rules

- [accepted] Source registry debe clasificar official source, curated source, secondary source y prohibited source.
- [accepted] Source registry debe registrar source snapshot/version, trust level, freshness/vigencia, applicability y stewardship.
- [accepted] Una fuente oficial no queda automaticamente convertida en conocimiento aplicable; debe tener vigencia, aplicabilidad y, cuando corresponda, artifact curado.
- [accepted] Knowledge artifact es la unidad logica que transforma fuente/snapshot en regla, recomendacion, pattern, anti-pattern, example, warning y evidencia utilizable.
- [accepted] Source usage debe registrar cuando una fuente o artifact se usa en PRD, SDD, task/context packet, decision, contract, gate, test o evidence.
- [accepted] Fuentes secundarias pueden informar contexto con warning, pero no deben convertirse en autoridad sin validacion.

## Integration Knowledge Pack Rules

- [accepted] Las integraciones externas se modelan como integration knowledge packs condicionales.
- [accepted] Un integration knowledge pack debe poder representar proveedor, tipo de integracion, fuentes oficiales, snapshots/versiones, Swagger/OpenAPI si aplica, PDFs tecnicos si aplica, ambientes sandbox/certificacion/produccion, autenticacion/autorizacion, certificados/tokens/firmas si aplica, endpoints, payloads, errores, rate limits si aplica, datos sensibles, seguridad, compliance, ejemplos oficiales, pruebas recomendadas, vigencia, riesgos y trazabilidad.
- [accepted] SII, FirmaGob, ClaveUnica, DocDigital, APIs publicas y APIs privadas de terceros quedan como ejemplos modelables, no como implementaciones aprobadas.

## Curation Mode And Knowledge Gap Policy

- [accepted] CAFL no puede usar busqueda web libre como fuente directa de implementacion.
- [accepted] Bootstrap incremental no significa trabajar sin conocimiento; significa construir la base bajo demanda mediante curaduria controlada.
- [accepted] Si falta conocimiento autorizado suficiente, CAFL debe bloquear implementacion y registrar Knowledge Gap + Curation Request.
- [accepted] Una Curation Request debe indicar que conocimiento falta, para que decision/tarea se necesita, que fuente oficial se propone consultar, que dominio o URL base se solicita autorizar, que tipo de artifact se espera producir, limite de alcance/contexto y token budget o budget class esperado.
- [accepted] La busqueda externa solo puede ocurrir en Curation Mode, no en modo implementacion.
- [accepted] Una Curation Task solo puede consultar fuentes oficiales explicitamente indicadas por el owner, dominios oficiales aprobados en una source policy previa, documentos especificos entregados por el owner, repositorios oficiales previamente autorizados o Swagger/OpenAPI/PDFs tecnicos aprobados como candidatos.
- [accepted] Si no existe source policy aprobada o fuente autorizada, debe escalar al owner antes de buscar.
- [accepted] Queda prohibido usar busqueda web general, Wikipedia como fuente tecnica directa, blogs no autorizados, StackOverflow como fuente autoritativa, copiar soluciones de terceros sin validacion o ampliar fuentes sin aprobacion.
- [accepted] El resultado de una Curation Task debe convertirse en source registry entry, snapshot/version, trust/freshness/applicability, knowledge artifact o integration knowledge pack y validacion/aprobacion correspondiente antes de disenar o implementar.

## Bootstrap Incremental Rule

- [accepted] CRIT-06 aprueba el modelo logico completo, pero V1 debe permitir un modo bootstrap incremental.
- [accepted] Bootstrap incremental implica source registry minimo inicial, artifacts curados minimos para Odoo/ORM/security/testing segun necesidad del modulo piloto, integration knowledge packs solo cuando la solucion requiera integracion, snapshots/versiones obligatorios para fuentes criticas y curacion incremental guiada por necesidades reales del modulo piloto.
- [accepted] Bootstrap incremental no asume RAG/base vectorial ni cargar toda la documentacion Odoo/OWL/Playwright/integraciones desde el dia 1.
- [accepted] Bootstrap incremental no autoriza implementacion sin fuente; si falta conocimiento autorizado, se bloquea y se activa Knowledge Gap + Curation Request.

## Boundaries With CRIT-07

- [accepted] CRIT-06 define modelo logico/conceptual.
- [accepted] CRIT-07 fue aprobado posteriormente como direccion candidata de viabilidad/runtime y cierre de la elicitacion critica CRIT-01..07.
- [accepted] CRIT-07 resolvio direccion candidata para runtime, storage fisico, schemas/validators/commands/scripts y knowledge base V1, pero no implemento runtime ni artefactos fisicos finales.
- [accepted] No se crea ni propone CRIT-08.

## Non-Goals Confirmed

- [accepted] No crear schemas finales.
- [accepted] No crear validators finales.
- [accepted] No crear commands finales.
- [accepted] No crear scripts.
- [accepted] No implementar storage fisico.
- [accepted] No implementar RAG.
- [accepted] No crear base vectorial.
- [accepted] No crear base de datos final.
- [accepted] No configurar OpenCode.
- [accepted] No configurar OpenSpec.
- [accepted] No modificar `framework/`.
- [accepted] No modificar codigo.
- [accepted] No resolver CRIT-07.
- [accepted] No crear CRIT-08.
- [accepted] No elevar `framework/` a verdad oficial.

## Acceptance Criteria Result

- [accepted] CRIT-06 queda documentado como modelo logico/conceptual aprobado.
- [accepted] Estado autoritativo no vive en narrativa LLM.
- [accepted] Logs obligatorios y condicionales quedan diferenciados.
- [accepted] IDs obligatorios y condicionales quedan diferenciados.
- [accepted] El modelo logico de knowledge/source governance queda aprobado.
- [accepted] Source registry, snapshots/versiones, trust/freshness/applicability y stewardship quedan aprobados conceptualmente.
- [accepted] Knowledge artifact queda aprobado como unidad logica.
- [accepted] Integration knowledge pack queda aprobado como unidad logica condicional.
- [accepted] Python queda limitado a Python aplicado a Odoo.
- [accepted] Busqueda web libre queda prohibida como fuente directa de implementacion.
- [accepted] Curation Mode requiere fuentes aprobadas por owner o source policy.
- [accepted] Knowledge Gap bloquea implementacion hasta curaduria/aprobacion suficiente.
- [accepted] Bootstrap incremental queda aprobado sin autorizar implementacion sin fuente.
- [accepted] CRIT-07 fue aprobado posteriormente como direccion candidata de viabilidad/runtime; no implemento schemas, validators, commands, scripts, storage fisico, runtime, RAG ni base vectorial.
- [accepted] CRIT-08 no existe.
