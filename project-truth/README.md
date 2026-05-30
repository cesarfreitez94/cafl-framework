# Project Truth

TOM_APPROVED_BY_OWNER

## Proposito

- [accepted] `project-truth/` es la primera capa de fuente de verdad del proyecto CAFL Framework.
- [accepted] Existe porque el owner indico que el repo actual puede contener material util, pero no representa necesariamente su intencion real.
- [accepted] Su objetivo inicial es ordenar la elicitacion critica antes de implementar, no cerrar diseno tecnico final.

## Autoridad

- [accepted] En caso de conflicto, `project-truth/` tiene prioridad sobre `README.md`, agentes, comandos, contratos, gates, backlog, roadmap y documentos previos del repo.
- [accepted] El contenido actual del repo no debe tratarse como verdad oficial salvo validacion explicita del owner.
- [accepted] `framework/` queda descartado como input de diseno y aprobado para eliminacion por CRIT-07.
- [accepted] Las conversaciones externas no son fuente valida para completar decisiones.

## Que No Representa Todavia

- [accepted] No es un PRD aprobado.
- [accepted] No es un SDD aprobado.
- [accepted] No contiene contratos finales.
- [accepted] No contiene gates finales.
- [accepted] No contiene agentes ejecutables.
- [accepted] No instala ni configura OpenSpec u otra herramienta.
- [accepted] No es Implementation Blueprint, backlog tecnico ni runtime implementado; CRIT-07 aprobo viabilidad, runtime candidate direction, recortes V1, riesgos, recursos y criterios para implementacion posterior.
- [accepted] `project-truth/TOM.md` fue elaborado como Target Operating Model operativo y aprobado explicitamente por el owner; estado actual: `approved`.

## Uso Antes De Implementar

- [accepted] La elicitacion critica CRIT-01..CRIT-07 esta completa; los trabajos posteriores deben definirse formalmente sin crear CRIT-08.
- [accepted] Cada afirmacion relevante debe usar uno de estos estados: `accepted`, `draft`, `assumption`, `open-question`, `rejected`, `superseded`.
- [accepted] Las decisiones firmes deben registrarse en `decisions/accepted.md`.
- [accepted] Las decisiones no resueltas deben registrarse en `decisions/pending.md`.
- [accepted] Los riesgos deben mantenerse en `risks.md` hasta que exista mitigacion aceptada o cierre documentado.
- [accepted] Las sesiones criticas CRIT-01..CRIT-07 ya fueron ejecutadas y aprobadas; no existe CRIT-08.

## Regla De Implementacion

- [accepted] No se implementa runtime hasta que los trabajos posteriores correspondientes definan formalmente blueprint, backlog y validaciones necesarias.
- [accepted] No se crean agentes ejecutables, comandos, contratos finales ni gates finales durante este bootstrap.
- [accepted] CRIT-07 no creo runtime, agents ejecutables, commands, schemas fisicos finales, validators reales, scripts, RAG, base vectorial ni configuracion OpenCode.

## Estado Actual

- [accepted] CRIT-01 Intent And Scope esta approved.
- [accepted] CRIT-02 Operating Flow esta approved.
- [accepted] CRIT-03 Agent Responsibilities esta approved como decision de responsabilidades y mecanismos candidatos, no como implementacion runtime.
- [accepted] CRIT-04 Contracts esta approved como modelo contractual conceptual, no como contratos finales, schemas finales, gates, commands ni runtime.
- [accepted] CRIT-05 Gates And Verification esta approved como modelo conceptual, no como gates finales ejecutables, schemas finales, validators, commands, scripts ni runtime.
- [accepted] CRIT-06 State, Evidence, Traceability And Knowledge Governance esta approved como modelo logico/conceptual, no como schemas finales, validators, commands, scripts, RAG final, base vectorial, storage fisico, runtime ni implementacion.
- [accepted] CRIT-07 Implementation Risks, Resources, Runtime And Feasibility esta approved como cierre de elicitacion critica, viabilidad, runtime candidate direction, riesgos, recursos, recortes V1 y criterios para implementacion posterior.
- [accepted] CRIT-01..CRIT-07 quedan completos.
- [accepted] CRIT-08 no existe.
- [accepted] Consolidated Truth Review esta completado.
- [accepted] Estado actual: TOM operativo elaborado y aprobado explicitamente por el owner (2026-05-27).
- [accepted] `project-truth/TOM.md` es el Target Operating Model approved de CAFL V1.
- [accepted] Implementation Blueprint esta closed y approved (5 iteraciones, 19 secciones, todas approved).
- [accepted] Verificacion deterministica del Blueprint completada: PASS sin findings.
- [accepted] Backlog candidates generados deterministicamente y verificados (PASS). No son paquetes de trabajo ejecutables, no autorizan implementacion.
- [accepted] Roadmap, hallazgos post-Blueprint, triage, spikes y planificacion de ejecucion estan pendientes.
