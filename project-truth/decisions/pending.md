# Pending Decisions

Status: bootstrap + CRIT-05 approved / CRIT-06 to CRIT-07 pending

## CRIT-01: Intent And Scope

- [accepted] No quedan decisiones pendientes para aprobar CRIT-01; CRIT-01 esta approved para intencion y alcance.

## CRIT-02: Operating Flow

- [accepted] No quedan decisiones pendientes para aprobar CRIT-02; CRIT-02 esta approved como operating flow.
- [accepted] CRIT-03 ya aprobo responsabilidades conceptuales y mecanismos candidatos.
- [accepted] CRIT-04 ya aprobo el modelo contractual conceptual.
- [accepted] CRIT-05 ya aprobo el modelo conceptual de gates y verificacion.
- [accepted] Las decisiones de implementacion concreta restantes se derivan a CRIT-06 y CRIT-07.

## CRIT-03: Agent Responsibilities

- [accepted] CRIT-03 fue resuelto y aprobado como decision de responsabilidades, autoridad conceptual, limites, handoffs y mecanismos candidatos.
- [accepted] La trazabilidad de CRIT-03 queda en `project-truth/decisions/accepted.md` y `project-truth/elicitation/critical-03-agent-responsibilities.md`.
- [accepted] CRIT-03 no aprobo implementacion runtime; los pendientes vivos derivados continuan en CRIT-06 y CRIT-07 donde aplique.

## CRIT-04: Contracts

- [accepted] CRIT-04 fue resuelto y aprobado como modelo contractual conceptual.
- [accepted] La trazabilidad de CRIT-04 queda en `project-truth/decisions/accepted.md` y `project-truth/elicitation/critical-04-contracts.md`.
- [accepted] CRIT-04 no aprobo contratos finales, schemas finales, gates finales, commands, agents ejecutables ni runtime; los pendientes vivos quedan derivados a CRIT-06 y CRIT-07.

## CRIT-05: Gates And Verification

- [accepted] CRIT-05 fue resuelto y aprobado como modelo conceptual de gates y verificacion.
- [accepted] La trazabilidad de CRIT-05 queda en `project-truth/decisions/accepted.md` y `project-truth/elicitation/critical-05-gates-and-verification.md`.
- [accepted] CRIT-05 no aprobo gates finales ejecutables, schemas finales, validators, commands, scripts, agents ejecutables, storage, logs persistentes ni runtime; los pendientes vivos quedan derivados a CRIT-06 y CRIT-07.
- [accepted] No quedan decisiones CRIT-05 activas como pendientes.

## CRIT-06: State, Evidence And Traceability

| ID | Critical area | Decision needed | Why it matters | Current status | Truth status | Blocking level |
| --- | --- | --- | --- | --- | --- | --- |
| DEC-PENDING-020 | CRIT-06 | Definir modelo de estado autoritativo. | Evita depender de memoria, chats o documentos secundarios. | pending | open-question | blocker |
| DEC-PENDING-021 | CRIT-06 | Definir politica de fuentes, evidencia y context routing por autoridad documental. | Protege contra fuentes no oficiales, no trazables, antiguas, preliminares o insuficientes. | pending | open-question | high |
| DEC-PENDING-022 | CRIT-06 | Definir matriz de trazabilidad minima alineada a modulo -> capability/feature -> tarea verificable. | Conecta idea, alcance, decisiones, tareas, implementacion, pruebas, evidencia y resultado. | pending | open-question | high |
| DEC-PENDING-031 | CRIT-06 | Definir como registrar context routing decisions, token budget usage, context log, excluded/prohibited context log, documentos no relevantes y uso de evidencia secundaria. | CRIT-02/CRIT-04/CRIT-05 lo aprobaron como principio/check, pero falta modelo de estado y auditoria. | pending | open-question | medium |
| DEC-PENDING-034 | CRIT-06 | Definir como registrar decisiones CRIT-03 y CRIT-05 en estado autoritativo, incluyendo autoridad conceptual, rework counters, fuentes usadas/excluidas, gates y clasificacion de mecanismos candidatos. | CRIT-03 y CRIT-05 aprobaron responsabilidades y gates conceptuales, pero el modelo de persistencia, auditoria y decision log pertenece a CRIT-06. | pending | open-question | medium |
| DEC-PENDING-038 | CRIT-06 | Definir IDs finales, registros de instancias contractuales, evidence log, source log, context log, gate log y trazabilidad persistente para los modelos CRIT-04 y CRIT-05. | CRIT-04 y CRIT-05 aprobaron trazabilidad conceptual, pero no definen storage, logs ni esquema persistente. | pending | open-question | high |
| DEC-PENDING-040 | CRIT-06 | Definir rework history, gate decision history, debt log y relacion entre decision log, evidence log y gate log. | CRIT-05 aprobo rework acotado, deuda aceptable y gate decisions, pero no define persistencia ni logs finales. | pending | open-question | high |

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
