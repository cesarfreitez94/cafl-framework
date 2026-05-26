# CRIT-06: State, Evidence And Traceability

Status: not-started

## Session Objective

- [draft] Definir a nivel logico/conceptual el storage, estado autoritativo, evidencia, fuentes, contexto, decisiones, logs y trazabilidad sin depender de memoria, chats externos o narrativa LLM.

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

## Risks If Unresolved

- [draft] Perdida de trazabilidad entre intencion y artefactos.
- [draft] Decisiones tomadas en chats o memoria sin registro verificable.
- [draft] Narrativa LLM confundida con estado autoritativo.
- [draft] Contexto usado, excluido o prohibido sin registro auditable.
- [draft] Evidencia secundaria usada sin advertencias ni trazabilidad.
- [draft] Rework, token budget y excepciones sin historial.
- [draft] Fuentes no oficiales tratadas como autoridad.
- [draft] Dificultad para auditar por que se avanzo o bloqueo una fase.

## Output Format

- [draft] Politica minima de estado autoritativo, storage logico, persistencia conceptual, evidencia, fuentes, contexto, rework y token budget.
- [draft] Convencion de IDs conceptuales.
- [draft] Modelo candidato de decision log, evidence log, source log, context log, excluded/prohibited context log, gate log y rework history.
- [draft] Matriz candidata modulo -> capability/feature -> tarea verificable -> contrato/gate/evidencia/fuente/decision.
- [draft] Relacion conceptual contract -> gate -> evidence, sin schemas finales, validators finales, commands ni runtime.
- [draft] Reglas para actualizar decisiones, riesgos y preguntas abiertas.

## Acceptance Criteria

- [draft] Cada decision aceptada puede rastrearse a fuente y razon.
- [draft] Cada evidencia tiene ubicacion, estado y relacion con un punto critico o entrega.
- [draft] Estado autoritativo, narrativa LLM y evidencia secundaria quedan diferenciados.
- [draft] Context routing decisions, contexto excluido/prohibido/no relevante y token budget usage quedan contemplados.
- [draft] Storage logico, persistencia conceptual, IDs conceptuales, gate log y relacion contract -> gate -> evidence quedan contemplados.
- [draft] Evidencia producida por commands, scripts, tests, capturas y reportes puede registrarse sin implementar tooling.
- [draft] Rework history queda trazable a tarea, gate, decision y owner cuando corresponda.
- [draft] Las conversaciones no registradas quedan excluidas como autoridad.
