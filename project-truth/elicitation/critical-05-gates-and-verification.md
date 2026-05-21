# CRIT-05: Gates And Verification

Status: not-started

## Session Objective

- [draft] Definir criterios de avance, bloqueo, replanificacion y verificacion sin crear gates finales ni scripts.

## Context

- [accepted] `framework/GATE_CATALOG.md` existe como catalogo preliminar y evidencia secundaria.
- [draft] Un gate solo aporta valor si es verificable y tiene consecuencias claras.

## Questions For The Owner

- [open-question] Que condiciones deben bloquear siempre el avance?
- [open-question] Que condiciones pueden aceptarse como deuda documentada?
- [open-question] Que evidencias son necesarias para aprobar una fase?
- [open-question] Que significa `todos los tests aplicables` en un contexto V1 realista?
- [open-question] Quien decide cuando un gate falla?
- [open-question] Que severidades y categorias son utiles?
- [open-question] Que gates deben existir antes de codigo?
- [open-question] Que gates deben existir despues de codigo?

## Decisions To Make

- [open-question] Gates minimos por fase.
- [open-question] Severidades y categorias.
- [open-question] Accion por severidad.
- [open-question] Evidencia minima por gate.
- [open-question] Reglas de aprobacion automatica o humana.

## Non-Goals For This Session

- [accepted] No crear gates finales.
- [accepted] No implementar CI/CD.
- [accepted] No escribir scripts de validacion.
- [accepted] No prometer cobertura tecnica no soportada por recursos reales.

## Risks If Unresolved

- [draft] Gates ceremoniales sin capacidad de bloqueo.
- [draft] Avances automaticos sobre evidencia insuficiente.
- [draft] Rechazo tardio de entregables por criterios no acordados.

## Output Format

- [draft] Tabla de gate candidato, fase, criterio, evidencia, severidad, accion por fallo, responsable y estado.
- [draft] Lista de bloqueadores y condiciones de deuda aceptable.

## Acceptance Criteria

- [draft] Cada gate candidato es verificable con evidencia definida.
- [draft] Cada falla tiene accion operativa clara.
- [draft] Las aprobaciones automaticas quedan aceptadas o pendientes.
