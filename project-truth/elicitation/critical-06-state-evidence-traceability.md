# CRIT-06: State, Evidence And Traceability

Status: not-started

## Session Objective

- [draft] Definir a nivel logico/conceptual el storage, estado autoritativo, evidencia, fuentes, contexto, decisiones, logs y trazabilidad sin depender de memoria, chats externos o narrativa LLM.
- [draft] Definir tambien a nivel logico/conceptual el modelo de knowledge governance, source governance, base de conocimiento curada, registros de fuentes oficiales/documentacion curada y relacion source -> decision -> contract -> gate -> evidence, sin decidir implementacion fisica.

## Context

- [accepted] El owner prohibio usar informacion de conversaciones externas.
- [accepted] La unidad de control aprobada es modulo -> capability/feature -> tarea verificable.
- [accepted] Context routing, token budget, contexto excluido/prohibido, evidencia, testing y rework acotado son obligatorios por CRIT-02/CRIT-03.
- [draft] El repo actual contiene Markdown de control, pero su autoridad debe reconstruirse.
- [draft] La trazabilidad debe conectar intencion, decisiones, requerimientos, diseno, implementacion, pruebas y entrega si esos elementos son aceptados.
- [draft] CRIT-06 define modelo de estado/evidencia/trazabilidad; no define schemas finales ni crea tooling.
- [draft] CRIT-06 debe definir storage logico, persistencia conceptual, estado autoritativo e IDs conceptuales para registrar y auditar cambios sin elegir storage fisico.
- [draft] CRIT-06 debe separar narrativa LLM de estado autoritativo y registrar uso de contexto/tokens, contexto excluido/prohibido y evidencia usada.
- [draft] CRIT-06 debe explicitar la relacion conceptual contract -> gate -> evidence, incluido gate log, sin crear gates finales ni resolver la implementacion de CRIT-07.
- [draft] CAFL no debe resolver dudas tecnicas, integraciones o decisiones de implementacion mediante busqueda web libre por defecto ni usar busqueda web libre como fuente directa de implementacion.
- [draft] La base de conocimiento no debe ser solo documentacion guardada: debe modelar source oficial -> snapshot/version -> knowledge artifact curado -> reglas/patrones/anti-patrones/ejemplos -> uso en PRD/SDD/task/context packet/gate/test/evidencia.
- [draft] CRIT-06 debe definir el modelo logico de source registry, curated documentation registry, source snapshot/version, trust level, freshness/vigencia, applicability, source usage log y excluded/prohibited source log.
- [draft] CRIT-06 debe contemplar dominios iniciales Odoo, OWL, Playwright/testing, Python aplicado a Odoo, Odoo ORM, seguridad/accesos Odoo, performance Odoo, patrones y anti-patrones Odoo, integraciones externas, APIs oficiales y de terceros, Swagger/OpenAPI, PDFs tecnicos y documentacion oficial de servicios externos.
- [draft] SII, FirmaGob, ClaveUnica y DocDigital deben tratarse como ejemplos de dominios/integraciones modelables, no como implementaciones aprobadas en esta sesion.
- [draft] El modelo debe ser extensible a dominios futuros como legal-compliance, tax-regulation, public-sector-processes, accounting, industry-specific-rules y regulatory-reporting.

## Questions For The Owner

- [open-question] Que storage logico y persistencia conceptual necesita el estado autoritativo del proyecto?
- [open-question] Donde debe vivir logicamente el estado autoritativo del proyecto?
- [open-question] Que debe registrarse como decision?
- [open-question] Que debe contener el decision log y que diferencia una decision autoritativa de una recomendacion o narrativa LLM?
- [open-question] Que debe contener el evidence log para evidencia manual y evidencia producida por commands, scripts o tests?
- [open-question] Que debe contener el source log para fuentes oficiales, secundarias, antiguas, insuficientes o descartadas?
- [open-question] Que debe contener el context log para registrar context routing, documentos usados y razon de seleccion?
- [open-question] Que debe contener el excluded/prohibited context log para registrar contexto excluido, prohibido o no relevante?
- [open-question] Que debe contener el gate log para registrar recommendation, verification, decision, bloqueo, excepcion y resultado?
- [open-question] Como se registra rework history, ciclos usados, excepciones y escalamiento?
- [open-question] Como se relaciona estado con modulo -> capability/feature -> tarea verificable?
- [open-question] Como se relacionan contract -> gate -> evidence y como se trazan a modulo -> capability/feature -> tarea?
- [open-question] Como se registra token budget usage y excepciones de presupuesto?
- [open-question] Como se registra context usage para diferenciar contexto usado, excluido, prohibido y no relevante?
- [open-question] Como se registra el uso de evidencia secundaria sin convertirla en autoridad?
- [open-question] Que evidencia minima requiere una decision aceptada?
- [open-question] Que evidencia minima requiere una entrega aceptada?
- [open-question] Como se trazan cambios de alcance?
- [open-question] Como se marcan fuentes oficiales, secundarias y descartadas?
- [open-question] Que conversacion o decision no registrada debe considerarse inexistente?
- [open-question] Que nivel de auditoria necesita CAFL en V1?
- [open-question] Que modelo logico de knowledge governance necesita CAFL para convertir fuentes oficiales versionadas en conocimiento utilizable?
- [open-question] Que debe contener el official source registry y como se diferencia de curated documentation registry?
- [open-question] Que debe contener un source snapshot/version y como se registra vigencia, version, fecha, hash o referencia verificable?
- [open-question] Como se clasifica source trust level, source freshness/vigencia, applicability, ownership/stewardship y warnings de uso?
- [open-question] Que debe contener un knowledge artifact curado y como se relaciona con pattern, anti-pattern, example, recommendation y applicability?
- [open-question] Como se registra source usage log para PRD, SDD, task/context packet, decision, contract, gate, test y evidence?
- [open-question] Como se registra excluded/prohibited source log para fuentes no oficiales, insuficientes, obsoletas, contradictorias o prohibidas?
- [open-question] Como se traza source -> decision -> contract -> gate -> evidence sin crear schemas finales?
- [open-question] Como se traza knowledge artifact -> task/context packet -> implementation decision sin crear runtime?
- [open-question] Que politica debe bloquear avance cuando no exista fuente autorizada suficiente?
- [open-question] Que politica impide usar busqueda web libre como fuente directa de implementacion?
- [open-question] Como se modelan dominios iniciales de Odoo, OWL, Playwright/testing, Python aplicado a Odoo, ORM, seguridad/accesos, performance, patrones/anti-patrones e integraciones externas?
- [open-question] Como se modelan fuentes para APIs oficiales, APIs de terceros, Swagger/OpenAPI, PDFs tecnicos, autenticacion, ambientes sandbox/certificacion/produccion, endpoints, payloads, errores, seguridad, datos sensibles, compliance, ejemplos oficiales y pruebas recomendadas?
- [open-question] Como se modelan SII, FirmaGob, ClaveUnica y DocDigital como ejemplos de integraciones/dominios sin resolver su implementacion?
- [open-question] Como se habilita extensibilidad futura para legal-compliance, tax-regulation, public-sector-processes, accounting, industry-specific-rules y regulatory-reporting?

## Decisions To Make

- [open-question] Modelo de estado autoritativo, storage logico y persistencia conceptual.
- [open-question] IDs conceptuales y convenciones.
- [open-question] Estructura candidata de decision log, evidence log, source log, context log, excluded/prohibited context log, gate log y rework history.
- [open-question] Politica de evidencia.
- [open-question] Politica de fuentes.
- [open-question] Politica de estado autoritativo vs narrativa LLM.
- [open-question] Registro de token budget usage y context routing decisions.
- [open-question] Registro de evidencia producida por commands, scripts, tests, capturas y reportes.
- [open-question] Matriz de trazabilidad minima modulo -> capability/feature -> tarea -> contract -> gate -> evidence.
- [open-question] Politica de actualizacion y cambio.
- [open-question] Modelo logico de knowledge governance, source governance y curated knowledge base.
- [open-question] Official source registry, curated documentation registry, source snapshots/versions y excluded/prohibited source log.
- [open-question] Clasificacion conceptual de source trust level, source freshness/vigencia, applicability, ownership/stewardship, update policy, validation policy y deprecation policy.
- [open-question] Modelo conceptual de knowledge artifact, pattern, anti-pattern, example, recommendation y applicability.
- [open-question] Relacion source -> decision -> contract -> gate -> evidence y knowledge artifact -> task/context packet -> implementation decision.
- [open-question] Politica de bloqueo cuando no exista conocimiento autorizado suficiente.
- [open-question] Politica contra busqueda web libre como fuente directa de implementacion.
- [open-question] Dominios iniciales y extensibilidad futura para integraciones externas y dominios legales/regulatorios sin crear nuevas sesiones criticas.

## Non-Goals For This Session

- [accepted] No implementar base de datos, RAG ni dashboards.
- [accepted] No definir schemas finales.
- [accepted] No definir validators finales.
- [accepted] No definir commands finales.
- [accepted] No crear tooling, commands, scripts ni automatizaciones.
- [accepted] No implementar storage fisico.
- [accepted] No configurar runtime.
- [accepted] No resolver CRIT-07.
- [accepted] No aprobar herramienta de gestion externa.
- [accepted] No convertir documentos actuales en verdad oficial.
- [accepted] No definir RAG final ni base vectorial final.
- [accepted] No definir base de datos final para knowledge base.
- [accepted] No crear schemas finales de knowledge artifacts ni source registry.
- [accepted] No crear validators finales de fuentes o knowledge packs.
- [accepted] No crear commands, scripts, ingesta, snapshots fisicos ni tooling de actualizacion.
- [accepted] No implementar curated knowledge base ni integraciones externas.

## Risks If Unresolved

- [draft] Perdida de trazabilidad entre intencion y artefactos.
- [draft] Decisiones tomadas en chats o memoria sin registro verificable.
- [draft] Narrativa LLM confundida con estado autoritativo.
- [draft] Contexto usado, excluido o prohibido sin registro auditable.
- [draft] Evidencia secundaria usada sin advertencias ni trazabilidad.
- [draft] Rework, token budget y excepciones sin historial.
- [draft] Fuentes no oficiales tratadas como autoridad.
- [draft] Dificultad para auditar por que se avanzo o bloqueo una fase.
- [draft] Busqueda web libre usada como fuente directa de implementacion.
- [draft] Conocimiento Odoo, OWL, testing o integraciones desactualizado, no versionado o no aplicable.
- [draft] Agentes inventando comportamiento por falta de fuente curada autorizada.
- [draft] Integraciones externas modeladas desde fuentes no oficiales, Swagger/PDF/API docs mal interpretados o documentacion sin vigencia.
- [draft] Knowledge governance demasiado rigido para dominios futuros o demasiado laxo para bloquear fuentes insuficientes.

## Output Format

- [draft] Politica minima de estado autoritativo, storage logico, persistencia conceptual, evidencia, fuentes, contexto, rework y token budget.
- [draft] Convencion de IDs conceptuales.
- [draft] Modelo candidato de decision log, evidence log, source log, context log, excluded/prohibited context log, gate log y rework history.
- [draft] Matriz candidata modulo -> capability/feature -> tarea verificable -> contrato/gate/evidencia/fuente/decision.
- [draft] Relacion conceptual contract -> gate -> evidence, sin schemas finales, validators finales, commands ni runtime.
- [draft] Reglas para actualizar decisiones, riesgos y preguntas abiertas.
- [draft] Modelo logico candidato de knowledge governance, source governance, curated knowledge base, official source registry y curated documentation registry.
- [draft] Modelo conceptual de source snapshot/version, source trust level, source freshness/vigencia, applicability, source usage log y prohibited/excluded source log.
- [draft] Modelo conceptual de knowledge artifact, pattern, anti-pattern, example, recommendation, ownership/stewardship, update policy, validation policy y deprecation policy.
- [draft] Trazabilidad candidata source -> decision -> contract -> gate -> evidence y knowledge artifact -> task/context packet -> implementation decision.
- [draft] Politica candidata de bloqueo por falta de fuente autorizada suficiente y prohibicion de busqueda web libre como fuente directa de implementacion.

## Acceptance Criteria

- [draft] Cada decision aceptada puede rastrearse a fuente y razon.
- [draft] Cada evidencia tiene ubicacion, estado y relacion con un punto critico o entrega.
- [draft] Estado autoritativo, narrativa LLM y evidencia secundaria quedan diferenciados.
- [draft] Context routing decisions, contexto excluido/prohibido/no relevante y token budget usage quedan contemplados.
- [draft] Storage logico, persistencia conceptual, IDs conceptuales, gate log y relacion contract -> gate -> evidence quedan contemplados.
- [draft] Evidencia producida por commands, scripts, tests, capturas y reportes puede registrarse sin implementar tooling.
- [draft] Rework history queda trazable a tarea, gate, decision y owner cuando corresponda.
- [draft] Las conversaciones no registradas quedan excluidas como autoridad.
- [draft] Knowledge governance, source governance, source registry, curated knowledge artifacts, snapshots/versiones, trust/freshness/applicability y source usage quedan contemplados a nivel logico.
- [draft] La relacion source -> decision -> contract -> gate -> evidence y knowledge artifact -> task/context packet -> implementation decision queda contemplada sin crear runtime.
- [draft] Odoo, OWL, Playwright/testing, Python aplicado a Odoo, Odoo ORM, seguridad/accesos, performance, patrones/anti-patrones, integraciones externas, APIs, Swagger/OpenAPI, PDFs tecnicos y documentacion oficial externa quedan contemplados como dominios iniciales.
- [draft] SII, FirmaGob, ClaveUnica y DocDigital quedan contemplados como ejemplos de dominios/integraciones modelables.
- [draft] La extensibilidad a dominios legales, regulatorios, contables, publicos e industriales queda contemplada sin crear CRIT-08.
- [draft] Queda claro que CRIT-06 no define RAG final, base de datos final, schemas finales, validators finales, commands, scripts, ingesta ni runtime.
