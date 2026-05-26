# Project Truth

Status: bootstrap + CRIT-04 approved / CRIT-05 to CRIT-07 pending

## Proposito

- [accepted] `project-truth/` es la primera capa de fuente de verdad del proyecto CAFL Framework.
- [accepted] Existe porque el owner indico que el repo actual puede contener material util, pero no representa necesariamente su intencion real.
- [accepted] Su objetivo inicial es ordenar la elicitacion critica antes de implementar, no cerrar diseno tecnico final.

## Autoridad

- [accepted] En caso de conflicto, `project-truth/` tiene prioridad sobre `README.md`, `framework/`, agentes, comandos, contratos, gates, backlog, roadmap y documentos previos del repo.
- [accepted] El contenido actual del repo es evidencia secundaria hasta que el owner lo valide explicitamente.
- [accepted] `framework/` no es autoridad de verdad del proyecto en esta etapa.
- [accepted] Las conversaciones externas no son fuente valida para completar decisiones.

## Que No Representa Todavia

- [accepted] No es un PRD aprobado.
- [accepted] No es un SDD aprobado.
- [accepted] No contiene contratos finales.
- [accepted] No contiene gates finales.
- [accepted] No contiene agentes ejecutables.
- [accepted] No instala ni configura OpenSpec u otra herramienta.
- [accepted] No define todavia el alcance V1 real, salvo restricciones explicitas aceptadas en CRIT-01, decisiones de flujo aceptadas en CRIT-02, responsabilidades conceptuales aprobadas en CRIT-03 y modelo contractual conceptual aprobado en CRIT-04.

## Uso Antes De Implementar

- [accepted] Antes de implementar en `framework/`, se deben resolver los puntos criticos minimos definidos en `critical-map.md`.
- [accepted] Cada afirmacion relevante debe usar uno de estos estados: `accepted`, `draft`, `assumption`, `open-question`, `rejected`, `superseded`.
- [accepted] Las decisiones firmes deben registrarse en `decisions/accepted.md`.
- [accepted] Las decisiones no resueltas deben registrarse en `decisions/pending.md`.
- [accepted] Los riesgos deben mantenerse en `risks.md` hasta que exista mitigacion aceptada o cierre documentado.
- [draft] Las plantillas de `elicitation/` deben ejecutarse como sesiones separadas antes de revisar temas generales o planificar desarrollo.

## Regla De Implementacion

- [accepted] No se implementa en `framework/` hasta resolver los puntos criticos minimos con el owner.
- [accepted] No se crean agentes ejecutables, comandos, contratos finales ni gates finales durante este bootstrap.
- [accepted] Este bootstrap solo crea archivos bajo `project-truth/`.

## Estado Actual

- [accepted] CRIT-01 Intent And Scope esta approved.
- [accepted] CRIT-02 Operating Flow esta approved.
- [accepted] CRIT-03 Agent Responsibilities esta approved como decision de responsabilidades y mecanismos candidatos, no como implementacion runtime.
- [accepted] CRIT-04 Contracts esta approved como modelo contractual conceptual, no como contratos finales, schemas finales, gates, commands ni runtime.
- [accepted] CRIT-05, CRIT-06 y CRIT-07 siguen pendientes.
- [accepted] No se debe implementar en `framework/` hasta resolver los puntos criticos minimos restantes con el owner.
