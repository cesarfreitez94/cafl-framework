# Pending Decisions

Status: CRIT-01 answered / pending verification

## CRIT-01: Intent And Scope

| ID | Critical area | Decision needed | Why it matters | Current status | Truth status | Blocking level |
| --- | --- | --- | --- | --- | --- | --- |
| DEC-PENDING-001 | CRIT-01 | Verificar que el owner acepta el registro documental de CRIT-01. | CRIT-01 no debe marcarse como approved sin confirmacion explicita del owner. | pending verification | open-question | high |

## CRIT-02: Operating Flow

| ID | Critical area | Decision needed | Why it matters | Current status | Truth status | Blocking level |
| --- | --- | --- | --- | --- | --- | --- |
| DEC-PENDING-005 | CRIT-02 | Definir fases operativas minimas desde idea hasta modulo Odoo listo para produccion tecnica. | Agentes, contratos y gates dependen del flujo real. | pending | open-question | blocker |
| DEC-PENDING-006 | CRIT-02 | Definir reglas de avance, bloqueo, re-trabajo y cierre por fase. | Evita avances automaticos sin criterio y tareas interminables. | pending | open-question | blocker |
| DEC-PENDING-007 | CRIT-02 | Definir el mecanismo operativo para escalar decisiones criticas al owner. | La intencion de autonomia completa ya esta aceptada, pero falta operacionalizar cuando preguntar y cuando continuar. | pending | open-question | high |
| DEC-PENDING-008 | CRIT-02 | Definir la unidad de control del flujo. | Cambia granularidad de backlog, evidencia, tareas, aprobaciones y validaciones. | pending | open-question | high |

## CRIT-03: Agent Responsibilities

| ID | Critical area | Decision needed | Why it matters | Current status | Truth status | Blocking level |
| --- | --- | --- | --- | --- | --- | --- |
| DEC-PENDING-009 | CRIT-03 | Definir lista minima de roles/agentes necesarios para cubrir el ciclo Odoo. | Evita crear agentes innecesarios o dejar brechas en capacidades equivalentes a equipo especializado. | pending | open-question | blocker |
| DEC-PENDING-010 | CRIT-03 | Definir responsabilidades y no-responsabilidades por rol. | Evita solapamiento, brechas, handoffs debiles y tareas operativas manuales. | pending | open-question | blocker |
| DEC-PENDING-011 | CRIT-03 | Definir autoridad de roles/agentes para bloquear, avanzar, pedir contexto o escalar. | Afecta autonomia, seguridad y control humano en decisiones criticas. | pending | open-question | high |
| DEC-PENDING-012 | CRIT-03 | Definir granularidad del desarrollo Odoo. | Impacta arquitectura de roles, handoffs y validacion del modulo acotado. | pending | open-question | high |

## CRIT-04: Contracts

| ID | Critical area | Decision needed | Why it matters | Current status | Truth status | Blocking level |
| --- | --- | --- | --- | --- | --- | --- |
| DEC-PENDING-013 | CRIT-04 | Definir contratos internos minimos obligatorios. | Sin contratos claros no hay handoffs verificables ni control de alcance. | pending | open-question | blocker |
| DEC-PENDING-014 | CRIT-04 | Definir formato de contratos internos. | Afecta legibilidad, validacion, versionado y mantenimiento. | pending | open-question | high |
| DEC-PENDING-015 | CRIT-04 | Definir campos minimos, versionado y criterios de suficiencia. | Permite trazabilidad y evita avanzar con entradas incompletas. | pending | open-question | high |

## CRIT-05: Gates And Verification

| ID | Critical area | Decision needed | Why it matters | Current status | Truth status | Blocking level |
| --- | --- | --- | --- | --- | --- | --- |
| DEC-PENDING-016 | CRIT-05 | Definir gates minimos por fase. | Sin gates no hay control verificable de avance hacia produccion tecnica. | pending | open-question | blocker |
| DEC-PENDING-017 | CRIT-05 | Definir severidades, categorias y acciones por fallo. | Determina bloqueo, deuda, escalamiento, re-trabajo o avance. | pending | open-question | blocker |
| DEC-PENDING-018 | CRIT-05 | Definir evidencia minima por gate y por aceptacion final. | Evita gates ceremoniales o no verificables. | pending | open-question | high |
| DEC-PENDING-019 | CRIT-05 | Definir que significa `tests suficientes` y `tests aplicables` por alcance de modulo. | Testing es obligatorio, pero falta convertirlo en criterio verificable. | pending | open-question | high |
| DEC-PENDING-027 | CRIT-05 | Definir DoD verificable para modulo listo para produccion tecnica. | CRIT-01 acepto la intencion del DoD, pero falta operacionalizar evidencia y criterios. | pending | open-question | high |

## CRIT-06: State, Evidence And Traceability

| ID | Critical area | Decision needed | Why it matters | Current status | Truth status | Blocking level |
| --- | --- | --- | --- | --- | --- | --- |
| DEC-PENDING-020 | CRIT-06 | Definir modelo de estado autoritativo. | Evita depender de memoria, chats o documentos secundarios. | pending | open-question | blocker |
| DEC-PENDING-021 | CRIT-06 | Definir politica de fuentes y evidencia. | Protege contra fuentes no oficiales, no trazables o insuficientes. | pending | open-question | high |
| DEC-PENDING-022 | CRIT-06 | Definir matriz de trazabilidad minima. | Conecta idea, alcance, decisiones, tareas, implementacion, pruebas, evidencia y resultado. | pending | open-question | high |

## CRIT-07: Implementation Risks And Resources

| ID | Critical area | Decision needed | Why it matters | Current status | Truth status | Blocking level |
| --- | --- | --- | --- | --- | --- | --- |
| DEC-PENDING-023 | CRIT-07 | Confirmar recursos y entorno Odoo disponibles. | Sin entorno Odoo no se puede verificar modulo funcional ni instalacion/carga. | pending | open-question | blocker |
| DEC-PENDING-024 | CRIT-07 | Decidir herramientas auxiliares para construir, verificar o coordinar el desarrollo del framework. | Herramientas como OpenSpec u OpenProject pueden evaluarse fuera del producto CAFL, sin ser dependencias funcionales. | pending | open-question | medium |
| DEC-PENDING-025 | CRIT-07 | Definir restricciones de entorno de desarrollo y setup operativo del runtime OpenCode. | OpenCode ya es runtime principal; falta precisar prerequisitos, perfiles, permisos, rutas y operacion local/global. | pending | open-question | high |
| DEC-PENDING-026 | CRIT-07 | Definir secuencia de implementacion y recortes de alcance compatibles con el plazo objetivo de 2 meses. | Evita planificacion basada en tiempos no realistas o capacidades que no caben en V1. | pending | open-question | high |
| DEC-PENDING-028 | CRIT-07 | Definir el modulo Odoo real y acotado que validara el flujo end-to-end. | CRIT-01 acepto el tipo de piloto, pero no el modulo exacto. | pending | open-question | high |
