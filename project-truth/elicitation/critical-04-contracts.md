# CRIT-04: Contracts

Status: not-started

## Session Objective

- [draft] Definir la estructura contractual minima para coordinar fases, entregables y mecanismos del modelo mixto, sin crear contratos finales.

## Context

- [accepted] `framework/CONTRACT_CATALOG.md` existe como catalogo preliminar y evidencia secundaria.
- [accepted] CRIT-03 aprobo modelo mixto: agents, commands, SDK/server/scripts/control deterministico, rules/config, skills/playbooks y owner/human segun responsabilidad.
- [accepted] PRD ligero, SDD ligero, task/context packet, Definition of Ready, context routing, token budget y rework acotado son obligatorios por CRIT-02/CRIT-03.
- [draft] Los contratos deben reducir ambiguedad, no crear documentacion innecesaria.
- [draft] CRIT-04 define estructura contractual; CRIT-05 decidira gates y acciones por fallo; CRIT-06 decidira estado/evidencia/trazabilidad persistente; CRIT-07 decidira implementacion/runtime.

## Questions For The Owner

- [open-question] Que tipo de informacion debe estar obligatoriamente acordada antes de avanzar de fase?
- [open-question] Que contratos son indispensables para evitar trabajo ambiguo?
- [open-question] Que contratos minimos requiere cada mecanismo candidato: agent, command, SDK/server/script, rule/config, skill/playbook, human/owner o mixed?
- [open-question] Que campos obligatorios debe tener el task/context packet por tipo de tarea verificable?
- [open-question] Que condiciones componen la Definition of Ready antes de iniciar una fase o tarea?
- [open-question] Como se declaran producer, consumer y validator para cada contrato?
- [open-question] Con que criterio puede rechazar un contrato el consumidor, receptor o validator?
- [open-question] Como se declara contexto autorizado, contexto excluido/prohibido y contexto no relevante?
- [open-question] Como se declara token budget esperado, usado y excepciones?
- [open-question] Que inputs, outputs, evidencia esperada, blockers y criterio de suficiencia son obligatorios?
- [open-question] Que contratos serian exceso documental para V1?
- [open-question] Los contratos deben ser legibles por humanos, validables por maquina o ambos?
- [open-question] Que nivel de formalidad necesita cada contrato?
- [open-question] Como se versionan cambios de contrato y como se trazan a decisiones, fuentes, tareas y evidencias?
- [open-question] Que contrato conecta requerimientos con pruebas?
- [open-question] Que contrato conecta diseno con implementacion?

## Decisions To Make

- [open-question] Inventario minimo de contratos.
- [open-question] Formato preferido: Markdown, YAML, JSON, frontmatter, schema u otro.
- [open-question] Campos minimos para task/context packet, DoR, inputs, outputs, evidencia, blockers, contexto autorizado/excluido y token budget.
- [open-question] Reglas de producer/consumer/validator y rechazo por consumidor o receptor.
- [open-question] Reglas de versionado, cambios y trazabilidad contractual.
- [open-question] Relacion con gates, evidencias y trazabilidad.

## Non-Goals For This Session

- [accepted] No redactar contratos finales.
- [accepted] No crear gates finales ni acciones por fallo; eso pertenece a CRIT-05.
- [accepted] No definir estado persistente, evidence log ni decision log finales; eso pertenece a CRIT-06.
- [accepted] No definir arquitectura runtime, commands, scripts, agentes ejecutables ni configuracion OpenCode; eso pertenece a CRIT-07.
- [accepted] No crear JSON Schema final.
- [accepted] No implementar validadores.
- [accepted] No convertir plantillas candidatas en implementacion.

## Risks If Unresolved

- [draft] Avance con entradas incompletas.
- [draft] Handoffs agents-only que ignoran commands, SDK/server/scripts, rules/config, skills o decision humana.
- [draft] Rechazos tardios por falta de consumer, validator, criterio de suficiencia o contexto autorizado.
- [draft] Contratos extensos sin uso operativo.
- [draft] Diferencias no detectadas entre requerimiento, diseno, codigo y prueba.

## Output Format

- [draft] Tabla de contrato candidato, proposito, mecanismo candidato, producer, consumer, validator, inputs, outputs, contexto autorizado, contexto excluido/prohibido/no relevante, token budget, evidencia esperada, blockers, criterio de suficiencia, criterio de rechazo, versionado, trazabilidad y estado.
- [draft] Definicion candidata de estructura para task/context packet y Definition of Ready.
- [draft] Lista de contratos rechazados o postergados.

## Acceptance Criteria

- [draft] Cada contrato candidato tiene consumidor claro.
- [draft] Cada contrato candidato identifica producer, consumer, validator y criterio de rechazo por consumidor o receptor.
- [draft] El modelo cubre agent, command, SDK/server/script, rule/config, skill/playbook, human/owner y mixed sin asumir implementacion final.
- [draft] Task/context packet y Definition of Ready quedan modelados como estructura contractual candidata.
- [draft] Contexto autorizado, excluido/prohibido/no relevante, token budget, inputs, outputs, evidencia, blockers y criterio de suficiencia quedan contemplados.
- [draft] Cada contrato candidato justifica su costo documental.
- [draft] Los formatos y reglas de versionado/trazabilidad quedan aceptados o registrados como decision pendiente.
