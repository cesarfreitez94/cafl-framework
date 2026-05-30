# AGENTS.md

## Scope

Estas reglas aplican a cualquier agente que trabaje en este repo. Su objetivo es mantener el trabajo alineado con `project-truth/` sin introducir decisiones nuevas, fuentes paralelas ni implementacion prematura.

## Fuente De Verdad

- Antes de actuar, leer el contexto aplicable en `project-truth/`.
- Tratar `project-truth/` como la unica fuente de verdad aprobada.
- Usar como referencias de autoridad `project-truth/critical-map.md`, `project-truth/TOM.md`, `project-truth/risks.md`, `project-truth/decisions/accepted.md`, `project-truth/decisions/pending.md`, `project-truth/decisions/rejected.md` y `project-truth/decisions/superseded.md`.
- Mantener trazabilidad hacia decisiones, riesgos y pendientes en `project-truth/`.
- No duplicar decisiones que ya viven en `project-truth/`.
- No crear documentos raiz paralelos que compitan con `project-truth/`.

## Estado Aprobado

- CRIT-01..CRIT-07 estan completos y aprobados.
- Consolidated Truth Review esta completado.
- Target Operating Model esta approved (2026-05-27) en `project-truth/TOM.md`. Decision registrada en DEC-ACCEPTED-161.
- Implementation Blueprint esta closed y approved. No ejecutar trabajo de Blueprint salvo solicitud explicita para auditoria historica.
- Backlog candidates generados y verificados. No son paquetes de trabajo ejecutables ni autorizacion de implementacion.
- Roadmap, hallazgos, triage, spikes y planificacion de ejecucion estan pendientes. Ejecutar solo cuando el prompt lo solicite explicitamente.

## Modo De Trabajo

- Ejecutar solo el objetivo solicitado por el prompt vigente.
- No ampliar alcance por iniciativa propia.
- No crear ni modificar artefactos fuera del alcance autorizado.
- No convertir recomendaciones en implementacion sin autorizacion explicita.
- Si falta contexto suficiente para cumplir una tarea, reportar el gap y pedir autorizacion o decision; no inventar.
- Si una tarea corresponde a Implementation Blueprint, backlog o implementacion, ejecutarla solo cuando el prompt lo solicite explicitamente y con los limites definidos en `project-truth/`.

## Documentacion

- Todo documento fuera de `project-truth/` debe ser vigente, derivado de `project-truth/` y util para el estado actual del proyecto.
- Si un documento raiz necesita cambiar, reescribirlo completo desde `project-truth/`; no aplicar micro-ediciones que dejen documentos hibridos.
- No conservar documentos como evidencia secundaria fuera de `project-truth/`.
- No crear carpetas historical, archive o legacy.

## Limites

- No disenar Implementation Blueprint ni backlog salvo instruccion explicita.
- No implementar runtime salvo instruccion explicita posterior y trazable.
- No definir agentes finales, commands finales, schemas finales, validators finales, scripts, RAG, base vectorial ni configuracion OpenCode salvo instruccion explicita posterior y trazable.
- No introducir decisiones no trazadas a `project-truth/`.
- No crear CRIT-08.
