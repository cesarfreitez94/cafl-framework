# Pending Decisions

TOM_APPROVED_BY_OWNER

## CRIT-01: Intent And Scope

- [accepted] No quedan decisiones pendientes para aprobar CRIT-01; CRIT-01 esta approved para intencion y alcance.

## CRIT-02: Operating Flow

- [accepted] No quedan decisiones pendientes para aprobar CRIT-02; CRIT-02 esta approved como operating flow.
- [accepted] CRIT-03 ya aprobo responsabilidades conceptuales y mecanismos candidatos.
- [accepted] CRIT-04 ya aprobo el modelo contractual conceptual.
- [accepted] CRIT-05 ya aprobo el modelo conceptual de gates y verificacion.
- [accepted] CRIT-07 ya aprobo la direccion candidata de implementacion y viabilidad; los trabajos posteriores deben definirse formalmente sin crear CRIT-08.

## CRIT-03: Agent Responsibilities

- [accepted] CRIT-03 fue resuelto y aprobado como decision de responsabilidades, autoridad conceptual, limites, handoffs y mecanismos candidatos.
- [accepted] La trazabilidad de CRIT-03 queda en `project-truth/decisions/accepted.md` y `project-truth/elicitation/critical-03-agent-responsibilities.md`.
- [accepted] CRIT-03 no aprobo implementacion runtime; CRIT-07 ya aprobo direccion candidata de runtime sin crear implementacion.

## CRIT-04: Contracts

- [accepted] CRIT-04 fue resuelto y aprobado como modelo contractual conceptual.
- [accepted] La trazabilidad de CRIT-04 queda en `project-truth/decisions/accepted.md` y `project-truth/elicitation/critical-04-contracts.md`.
- [accepted] CRIT-04 no aprobo contratos finales, schemas finales, gates finales, commands, agents ejecutables ni runtime; CRIT-07 aprobo schemas V1 minimos versionados y validators minimos como direccion, sin crearlos.

## CRIT-05: Gates And Verification

- [accepted] CRIT-05 fue resuelto y aprobado como modelo conceptual de gates y verificacion.
- [accepted] La trazabilidad de CRIT-05 queda en `project-truth/decisions/accepted.md` y `project-truth/elicitation/critical-05-gates-and-verification.md`.
- [accepted] CRIT-05 no aprobo gates finales ejecutables, schemas finales, validators, commands, scripts, agents ejecutables, storage fisico ni runtime; CRIT-07 aprobo automatizacion minima suficiente y validators minimos como direccion, sin implementarlos.
- [accepted] No quedan decisiones CRIT-05 activas como pendientes.

## CRIT-06: State, Evidence And Traceability

- [accepted] CRIT-06 fue resuelto y aprobado como modelo logico/conceptual de estado, evidencia, logs, IDs, trazabilidad, storage logico, persistencia conceptual y knowledge/source governance.
- [accepted] La trazabilidad de CRIT-06 queda en `project-truth/decisions/accepted.md` y `project-truth/elicitation/critical-06-state-evidence-traceability.md`.
- [accepted] CRIT-06 no aprobo schemas finales, validators finales, commands, scripts, RAG final, base vectorial, base de datos final, runtime OpenCode, rutas runtime, storage fisico ni implementacion.
- [accepted] No quedan decisiones CRIT-06 activas como pendientes; CRIT-07 ya aprobo direccion de implementacion fisica/runtime sin crear implementacion.

## CRIT-07: Implementation Risks, Resources, Runtime And Feasibility

- [accepted] CRIT-07 fue resuelto y aprobado como cierre de elicitacion critica, definicion de viabilidad, direccion candidata de runtime, riesgos, recursos, recortes V1 y criterios para implementacion posterior.
- [accepted] No quedan decisiones CRIT-07 activas como pendientes.
- [accepted] CRIT-07 no implemento runtime, no creo artifacts ejecutables, no cerro Implementation Blueprint, no cerro backlog tecnico y no impuso planificacion detallada posterior.
- [accepted] No existe CRIT-08.

## Post-CRIT-07 Work To Define

- [accepted] Consolidated Truth Review esta completado con resultado READY_FOR_TARGET_OPERATING_MODEL.
- [accepted] `project-truth/TOM.md` existe como especificacion/working contract para elaborar el Target Operating Model.
- [accepted] TOM approval completada. El contenido operativo completo del Target Operating Model fue elaborado en `project-truth/TOM.md` y aprobado explicitamente por el owner (2026-05-27). Decision registrada en DEC-ACCEPTED-161.
- [accepted] Piloto V1 confirmado por owner como solicitudes internas / aprobaciones simples. Decision registrada en DEC-ACCEPTED-162; Blueprint debe instanciar el flujo sin reabrir seleccion ni crear PRD/SDD/backlog aqui.
- [accepted] Source policy minima base pre-autorizada por owner: documentacion oficial Odoo y repositorio oficial GitHub `odoo/odoo`. Decision registrada en DEC-ACCEPTED-163; enforcement fisico queda pendiente para Blueprint/technical validation.
- [accepted] SDK/server queda fuera de core V1. Decision registrada en DEC-ACCEPTED-164; cualquier inclusion posterior requiere spike favorable y decision explicita del owner.
- [pending] Implementation Blueprint debe definirse formalmente sin usar `framework/` como input, tomando como entradas el piloto V1 confirmado, la source policy minima pre-autorizada y SDK/server fuera de core V1, sin convertir recomendaciones en implementacion prematura.
- [pending] Diseno fisico de source policy enforcement, Knowledge Gap y Curation Request queda para Implementation Blueprint/technical validation; no esta implementado aqui.
- [pending] Technical validations/spikes deben definirse formalmente.
- [pending] Backlog tecnico debe definirse formalmente.
- [pending] Implementacion controlada debe ejecutarse solo despues de los pasos formales que correspondan y con scope V1 aprobado.
- [accepted] Esta lista no impone una secuencia detallada post-CRIT-07 ni crea CRIT-08.
