# Pending Decisions

Status: bootstrap + CRIT-06 approved / CRIT-07 pending

## CRIT-01: Intent And Scope

- [accepted] No quedan decisiones pendientes para aprobar CRIT-01; CRIT-01 esta approved para intencion y alcance.

## CRIT-02: Operating Flow

- [accepted] No quedan decisiones pendientes para aprobar CRIT-02; CRIT-02 esta approved como operating flow.
- [accepted] CRIT-03 ya aprobo responsabilidades conceptuales y mecanismos candidatos.
- [accepted] CRIT-04 ya aprobo el modelo contractual conceptual.
- [accepted] CRIT-05 ya aprobo el modelo conceptual de gates y verificacion.
- [accepted] Las decisiones de implementacion concreta restantes se derivan a CRIT-07.

## CRIT-03: Agent Responsibilities

- [accepted] CRIT-03 fue resuelto y aprobado como decision de responsabilidades, autoridad conceptual, limites, handoffs y mecanismos candidatos.
- [accepted] La trazabilidad de CRIT-03 queda en `project-truth/decisions/accepted.md` y `project-truth/elicitation/critical-03-agent-responsibilities.md`.
- [accepted] CRIT-03 no aprobo implementacion runtime; CRIT-06 ya resolvio estado/evidencia/trazabilidad logica y los pendientes vivos de runtime continuan en CRIT-07.

## CRIT-04: Contracts

- [accepted] CRIT-04 fue resuelto y aprobado como modelo contractual conceptual.
- [accepted] La trazabilidad de CRIT-04 queda en `project-truth/decisions/accepted.md` y `project-truth/elicitation/critical-04-contracts.md`.
- [accepted] CRIT-04 no aprobo contratos finales, schemas finales, gates finales, commands, agents ejecutables ni runtime; CRIT-06 ya resolvio trazabilidad/logs conceptuales y los pendientes vivos de implementacion quedan derivados a CRIT-07.

## CRIT-05: Gates And Verification

- [accepted] CRIT-05 fue resuelto y aprobado como modelo conceptual de gates y verificacion.
- [accepted] La trazabilidad de CRIT-05 queda en `project-truth/decisions/accepted.md` y `project-truth/elicitation/critical-05-gates-and-verification.md`.
- [accepted] CRIT-05 no aprobo gates finales ejecutables, schemas finales, validators, commands, scripts, agents ejecutables, storage fisico ni runtime; CRIT-06 ya resolvio logs/trazabilidad conceptuales y los pendientes vivos de implementacion quedan derivados a CRIT-07.
- [accepted] No quedan decisiones CRIT-05 activas como pendientes.

## CRIT-06: State, Evidence And Traceability

- [accepted] CRIT-06 fue resuelto y aprobado como modelo logico/conceptual de estado, evidencia, logs, IDs, trazabilidad, storage logico, persistencia conceptual y knowledge/source governance.
- [accepted] La trazabilidad de CRIT-06 queda en `project-truth/decisions/accepted.md` y `project-truth/elicitation/critical-06-state-evidence-traceability.md`.
- [accepted] CRIT-06 no aprobo schemas finales, validators finales, commands, scripts, RAG final, base vectorial, base de datos final, runtime OpenCode, rutas runtime, storage fisico ni implementacion.
- [accepted] No quedan decisiones CRIT-06 activas como pendientes; los pendientes vivos derivados continuan en CRIT-07.

## CRIT-07: Implementation Risks And Resources

| ID | Critical area | Decision needed | Why it matters | Current status | Truth status | Blocking level |
| --- | --- | --- | --- | --- | --- | --- |
| DEC-PENDING-023 | CRIT-07 | Confirmar recursos y entorno Odoo disponibles. | Sin entorno Odoo no se puede verificar modulo funcional, instalacion/carga ni ejecucion reproducible. | pending | open-question | blocker |
| DEC-PENDING-024 | CRIT-07 | Decidir herramientas auxiliares para construir, verificar o coordinar el desarrollo del framework. | Herramientas como OpenSpec u OpenProject pueden evaluarse fuera del producto CAFL, sin ser dependencias funcionales. | pending | open-question | medium |
| DEC-PENDING-025 | CRIT-07 | Definir restricciones de entorno de desarrollo y setup operativo del runtime OpenCode sin reabrir OpenCode como runtime principal. | OpenCode ya es runtime principal; falta precisar prerequisitos, perfiles, permisos, rutas, source-vs-runtime y operacion local/global. | pending | open-question | high |
| DEC-PENDING-026 | CRIT-07 | Definir secuencia de implementacion y recortes de alcance compatibles con el plazo objetivo de 2 meses. | Evita planificacion basada en tiempos no realistas o capacidades que no caben en V1. | pending | open-question | high |
| DEC-PENDING-028 | CRIT-07 | Definir el modulo Odoo real y acotado que validara el flujo end-to-end. | CRIT-01 acepto el tipo de piloto, pero no el modulo exacto. | pending | open-question | high |
| DEC-PENDING-032 | CRIT-07 | Validar setup operativo OpenCode sobre subagentes, comandos, contexto, permisos, aprobaciones, estado, archivos fuente vs runtime, limites de tokens y ejecucion verificable. | CRIT-02/CRIT-03 lo requieren para operar correctamente el flujo sin reabrir OpenCode como runtime principal. | pending | open-question | blocker |
| DEC-PENDING-035 | CRIT-07 | Decidir implementacion concreta de mecanismos candidatos CRIT-03: agents, commands, permissions, SDK/server/scripts, config, rules/AGENTS.md, skills, ejecucion no interactiva y control deterministico. | CRIT-03 aprobo mecanismos candidatos conceptuales, pero no setup operativo final ni archivos runtime definitivos. | pending | open-question | blocker |
| DEC-PENDING-036 | CRIT-07 | Decidir alcance de RAG V1 y si RAG completo se justifica dentro del plan de 2 meses. | CRIT-03 aclaro que RAG completo no queda aprobado para V1 salvo justificacion posterior. | pending | open-question | high |
| DEC-PENDING-039 | CRIT-07 | Definir schemas finales, validators, commands, SDK/server/scripts, permissions y runtime que implementarian o validarian los modelos CRIT-04 y CRIT-05. | CRIT-04 no crea schemas finales ni implementacion runtime; CRIT-05 no crea gates ejecutables ni validators. La viabilidad y forma tecnica pertenecen a CRIT-07. | pending | open-question | blocker |
| DEC-PENDING-041 | CRIT-07 | Definir ejecucion reproducible y tooling operativo para testing, evidencia, gates, instalacion/carga Odoo y reportes. | CRIT-05 aprobo evidencia reproducible y testing suficiente, pero no define commands, scripts, CI/local tooling ni entorno real. | pending | open-question | blocker |
| DEC-PENDING-046 | CRIT-07 | Decidir implementacion fisica/runtime de la knowledge base curada. | CRIT-06 debe definir el modelo logico, pero CRIT-07 debe decidir como operarlo fisicamente. | pending | open-question | blocker |
| DEC-PENDING-047 | CRIT-07 | Decidir si se usara RAG, base vectorial, archivos curados, JSON/YAML/JSONL/Markdown, SQLite, PostgreSQL, pgvector u otro mecanismo. | La forma de storage/recuperacion afecta recursos, costo, permisos, source-vs-runtime y plazo de 2 meses. | pending | open-question | high |
| DEC-PENDING-048 | CRIT-07 | Decidir schemas, validators, commands y scripts de ingesta, actualizacion, validacion, snapshots/versiones, Swagger/OpenAPI, PDFs tecnicos y knowledge packs. | Sin tooling definido no se puede transformar fuentes oficiales en conocimiento utilizable por agents, commands, context packets, gates y evidencia. | pending | open-question | blocker |
| DEC-PENDING-049 | CRIT-07 | Decidir integracion de la knowledge base con OpenCode agents, commands, skills/playbooks, SDK/server/scripts, permissions, context routing y bloqueo por falta de conocimiento autorizado. | El conocimiento autorizado debe ser consultable y enforceable desde el runtime principal sin reabrir OpenCode. | pending | open-question | blocker |
| DEC-PENDING-050 | CRIT-07 | Decidir implementacion fisica/runtime de Knowledge Gap, Curation Request y Curation Mode con aprobacion de owner/source policy. | CRIT-06 aprobo bloqueo conceptual y curacion controlada; falta decidir schemas, validators, permissions, commands/scripts y enforcement real. | pending | open-question | blocker |
| DEC-PENDING-051 | CRIT-07 | Decidir alcance fisico del bootstrap incremental de knowledge base para el modulo piloto. | CRIT-06 aprobo source registry minimo inicial, artifacts curados bajo demanda y no asumir RAG/base vectorial; falta decidir mecanismo operativo compatible con 2 meses. | pending | open-question | high |
