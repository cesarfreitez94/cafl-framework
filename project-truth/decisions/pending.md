# Pending Decisions

Status: bootstrap + CRIT-03 approved / downstream decisions pending

## CRIT-01: Intent And Scope

- [accepted] No quedan decisiones pendientes para aprobar CRIT-01; CRIT-01 esta approved para intencion y alcance.

## CRIT-02: Operating Flow

- [accepted] No quedan decisiones pendientes para aprobar CRIT-02; CRIT-02 esta approved como operating flow.
- [accepted] CRIT-03 ya aprobo responsabilidades conceptuales y mecanismos candidatos.
- [accepted] Las decisiones de implementacion concreta restantes se derivan a CRIT-04, CRIT-05, CRIT-06 y CRIT-07.

## CRIT-03: Agent Responsibilities

| ID | Critical area | Decision needed | Why it matters | Current status | Truth status | Blocking level |
| --- | --- | --- | --- | --- | --- | --- |
| DEC-PENDING-009 | CRIT-03 | Definir si las funciones minimas aprobadas por CRIT-02 se implementan como agentes separados, roles combinados, capacidades de orquestacion u otros mecanismos candidatos: human, agent, command, SDK-server-script, rule-config o mixed. | Evita crear agentes innecesarios, forzar responsabilidades no aptas para LLM y dejar brechas en capacidades equivalentes a equipo especializado. | resolved in CRIT-03 | accepted | none |
| DEC-PENDING-010 | CRIT-03 | Definir responsabilidades y no-responsabilidades por rol/agente, incluyendo seguridad/riesgo/compliance. | Evita solapamiento, brechas, handoffs debiles y tareas operativas manuales. | resolved in CRIT-03 | accepted | none |
| DEC-PENDING-011 | CRIT-03 | Definir autoridad conceptual de roles/agentes para bloquear, avanzar, pedir contexto, escalar o cerrar una unidad de trabajo. | Afecta autonomia, seguridad, compliance y control humano en decisiones criticas. | resolved in CRIT-03 | accepted | none |
| DEC-PENDING-012 | CRIT-03 | Definir como los roles/agentes interactuan con la jerarquia modulo -> capability/feature -> tarea verificable. | Impacta handoffs, contexto, evidencia y validacion del modulo acotado. | resolved in CRIT-03 | accepted | none |

- [accepted] CRIT-03 queda aprobado como decision de responsabilidades y mecanismo candidato, no como implementacion runtime.
- [accepted] Las decisiones de implementacion concreta quedan derivadas a CRIT-04, CRIT-05, CRIT-06 y CRIT-07.

## CRIT-04: Contracts

| ID | Critical area | Decision needed | Why it matters | Current status | Truth status | Blocking level |
| --- | --- | --- | --- | --- | --- | --- |
| DEC-PENDING-013 | CRIT-04 | Definir contratos internos minimos obligatorios, incluyendo relacion con PRD, SDD, CDD, TDD y handoffs. | Sin contratos claros no hay handoffs verificables ni control de alcance. | pending | open-question | blocker |
| DEC-PENDING-014 | CRIT-04 | Definir formato de contratos internos y task/context packet. | Afecta legibilidad, validacion, versionado, tokens y mantenimiento. | pending | open-question | high |
| DEC-PENDING-015 | CRIT-04 | Definir campos minimos, producer/consumer/validator, versionado, Definition of Ready, criterios de suficiencia y criterio de rechazo por consumidor o receptor. | Permite trazabilidad y evita avanzar con entradas incompletas o salidas rechazadas tardiamente. | pending | open-question | high |
| DEC-PENDING-029 | CRIT-04 | Definir contenido minimo del task/context packet por tipo de tarea, incluyendo fuentes aplicables, fuentes secundarias, fuentes prohibidas/no relevantes, token budget, evidencia esperada y excepciones justificadas. | CRIT-02 lo hizo obligatorio y CRIT-03 aprobo la responsabilidad, pero no definio campos finales ni formatos. | pending | open-question | high |

## CRIT-05: Gates And Verification

| ID | Critical area | Decision needed | Why it matters | Current status | Truth status | Blocking level |
| --- | --- | --- | --- | --- | --- | --- |
| DEC-PENDING-016 | CRIT-05 | Definir gates minimos por fase/transicion. | Sin gates no hay control verificable de avance hacia produccion tecnica. | pending | open-question | blocker |
| DEC-PENDING-017 | CRIT-05 | Definir severidades, categorias, acciones por fallo y separacion entre gate recommendation, gate verification y gate decision. | Determina bloqueo, deuda, escalamiento, re-trabajo o avance sin confundir recomendacion LLM con decision autorizada. | pending | open-question | blocker |
| DEC-PENDING-018 | CRIT-05 | Definir evidencia minima reproducible por gate, por verificacion shift-left y por aceptacion final: logs, comandos, scripts, tests, capturas, reportes u otros artefactos. | Evita gates ceremoniales o no verificables. | pending | open-question | high |
| DEC-PENDING-019 | CRIT-05 | Definir que significa `tests suficientes` y `tests aplicables` bajo risk-based testing. | Testing es obligatorio, pero falta convertirlo en criterio verificable. | pending | open-question | high |
| DEC-PENDING-027 | CRIT-05 | Definir DoD verificable para modulo listo para produccion tecnica. | CRIT-01 acepto la intencion del DoD y CRIT-02 el principio operativo, pero falta operacionalizar evidencia y criterios. | pending | open-question | high |
| DEC-PENDING-030 | CRIT-05 | Definir cuando aplicar BDD formal, ATDD parcial, TDD estricto o solo planificacion de pruebas. | CRIT-02 diferio BDD formal y no aprobo TDD estricto universal. | pending | open-question | medium |
| DEC-PENDING-033 | CRIT-05 | Definir politica concreta para rework default de 2 ciclos, excepciones, tercer ciclo significativo, bloqueo y escalamiento. | CRIT-03 aprobo el limite default y la autoridad conceptual, pero no definio gate final, severidad ni evidencia requerida para excepciones. | pending | open-question | high |

## CRIT-06: State, Evidence And Traceability

| ID | Critical area | Decision needed | Why it matters | Current status | Truth status | Blocking level |
| --- | --- | --- | --- | --- | --- | --- |
| DEC-PENDING-020 | CRIT-06 | Definir modelo de estado autoritativo. | Evita depender de memoria, chats o documentos secundarios. | pending | open-question | blocker |
| DEC-PENDING-021 | CRIT-06 | Definir politica de fuentes, evidencia y context routing por autoridad documental. | Protege contra fuentes no oficiales, no trazables, antiguas, preliminares o insuficientes. | pending | open-question | high |
| DEC-PENDING-022 | CRIT-06 | Definir matriz de trazabilidad minima alineada a modulo -> capability/feature -> tarea verificable. | Conecta idea, alcance, decisiones, tareas, implementacion, pruebas, evidencia y resultado. | pending | open-question | high |
| DEC-PENDING-031 | CRIT-06 | Definir como registrar context routing decisions, token budget usage, context log, excluded/prohibited context log, documentos no relevantes y uso de evidencia secundaria. | CRIT-02 lo aprobo como principio, pero falta modelo de estado y auditoria. | pending | open-question | medium |
| DEC-PENDING-034 | CRIT-06 | Definir como registrar decisiones CRIT-03 en estado autoritativo, incluyendo autoridad conceptual, rework counters, fuentes usadas/excluidas y clasificacion de mecanismos candidatos. | CRIT-03 aprobo responsabilidades y limites, pero el modelo de persistencia, auditoria y decision log pertenece a CRIT-06. | pending | open-question | medium |

## CRIT-07: Implementation Risks And Resources

| ID | Critical area | Decision needed | Why it matters | Current status | Truth status | Blocking level |
| --- | --- | --- | --- | --- | --- | --- |
| DEC-PENDING-023 | CRIT-07 | Confirmar recursos y entorno Odoo disponibles. | Sin entorno Odoo no se puede verificar modulo funcional ni instalacion/carga. | pending | open-question | blocker |
| DEC-PENDING-024 | CRIT-07 | Decidir herramientas auxiliares para construir, verificar o coordinar el desarrollo del framework. | Herramientas como OpenSpec u OpenProject pueden evaluarse fuera del producto CAFL, sin ser dependencias funcionales. | pending | open-question | medium |
| DEC-PENDING-025 | CRIT-07 | Definir restricciones de entorno de desarrollo y setup operativo del runtime OpenCode sin reabrir OpenCode como runtime principal. | OpenCode ya es runtime principal; falta precisar prerequisitos, perfiles, permisos, rutas, source-vs-runtime y operacion local/global. | pending | open-question | high |
| DEC-PENDING-026 | CRIT-07 | Definir secuencia de implementacion y recortes de alcance compatibles con el plazo objetivo de 2 meses. | Evita planificacion basada en tiempos no realistas o capacidades que no caben en V1. | pending | open-question | high |
| DEC-PENDING-028 | CRIT-07 | Definir el modulo Odoo real y acotado que validara el flujo end-to-end. | CRIT-01 acepto el tipo de piloto, pero no el modulo exacto. | pending | open-question | high |
| DEC-PENDING-032 | CRIT-07 | Validar setup operativo OpenCode sobre subagentes, comandos, contexto, permisos, aprobaciones, estado, archivos fuente vs runtime, limites de tokens y ejecucion verificable. | CRIT-02/CRIT-03 lo requieren para operar correctamente el flujo sin reabrir OpenCode como runtime principal. | pending | open-question | blocker |
| DEC-PENDING-035 | CRIT-07 | Decidir implementacion concreta de mecanismos candidatos CRIT-03: agents, commands, permissions, SDK/server/scripts, config, rules/AGENTS.md, skills, ejecucion no interactiva y control deterministico. | CRIT-03 aprobo mecanismos candidatos conceptuales, pero no setup operativo final ni archivos runtime definitivos. | pending | open-question | blocker |
| DEC-PENDING-036 | CRIT-07 | Decidir alcance de RAG V1 y si RAG completo se justifica dentro del plan de 2 meses. | CRIT-03 aclaro que RAG completo no queda aprobado para V1 salvo justificacion posterior. | pending | open-question | high |
