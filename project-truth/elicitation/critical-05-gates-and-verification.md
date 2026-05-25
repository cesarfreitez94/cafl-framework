# CRIT-05: Gates And Verification

Status: not-started

## Session Objective

- [draft] Definir el modelo de gates verificables para avance, bloqueo, replanificacion, deuda y escalamiento, sin crear gates finales, commands ni scripts.

## Context

- [accepted] `framework/GATE_CATALOG.md` existe como catalogo preliminar y evidencia secundaria.
- [accepted] CRIT-02/CRIT-03 aprobaron shift-left verification, risk-based testing, testing aplicable, rework acotado y seguridad/riesgo/compliance como responsabilidad explicita.
- [accepted] El rework default es 2 ciclos; excepciones y tercer ciclo significativo requieren justificacion y escalamiento.
- [draft] Un gate solo aporta valor si es verificable y tiene consecuencias claras.
- [draft] CRIT-05 define modelo de gates; no define arquitectura OpenCode final, no crea commands/scripts y no implementa gates.

## Questions For The Owner

- [open-question] Que condiciones deben bloquear siempre el avance?
- [open-question] Que condiciones pueden aceptarse como deuda documentada?
- [open-question] Como se diferencia gate recommendation, gate verification y gate decision?
- [open-question] Que evidencias reproducibles son necesarias para aprobar una fase: logs, comandos ejecutados, scripts, tests, capturas, reportes u otros artefactos?
- [open-question] Que significa `todos los tests aplicables` en un contexto V1 realista?
- [open-question] Como se define testing suficiente/aplicable segun riesgo, alcance, tipo de cambio y entorno Odoo disponible?
- [open-question] Quien decide cuando un gate falla?
- [open-question] Que severidades y categorias son utiles?
- [open-question] Como se incorpora seguridad/riesgo/compliance como categoria obligatoria de gates?
- [open-question] Que acciones por fallo aplican por severidad: bloquear, rework, aceptar deuda, escalar al owner, rechazar, reducir alcance o replanificar?
- [open-question] Como se aplican 2 ciclos default de rework, excepciones justificadas y tercer ciclo significativo?
- [open-question] Que gates deben existir antes de codigo?
- [open-question] Que gates deben existir despues de codigo?

## Decisions To Make

- [open-question] Gates minimos por fase.
- [open-question] Modelo de recommendation, verification y decision por gate.
- [open-question] Severidades y categorias.
- [open-question] Accion por severidad.
- [open-question] Evidencia minima, reproducible y trazable por gate.
- [open-question] Politica de rework, excepciones, tercer ciclo significativo y escalamiento al owner.
- [open-question] Criterio de testing suficiente/aplicable bajo shift-left verification y risk-based testing.
- [open-question] Reglas de aprobacion automatica o humana.

## Non-Goals For This Session

- [accepted] No crear gates finales.
- [accepted] No definir arquitectura OpenCode final.
- [accepted] No crear commands, scripts ni herramientas de verificacion.
- [accepted] No implementar CI/CD.
- [accepted] No escribir scripts de validacion.
- [accepted] No implementar gates; solo definir el modelo de gates.
- [accepted] No prometer cobertura tecnica no soportada por recursos reales.

## Risks If Unresolved

- [draft] Gates ceremoniales sin capacidad de bloqueo.
- [draft] Avances automaticos sobre evidencia insuficiente.
- [draft] Confundir recomendacion LLM con verificacion reproducible o decision autorizada.
- [draft] Rework ilimitado, deuda no aceptada formalmente o escalamiento tardio al owner.
- [draft] Seguridad/riesgo/compliance tratado como revision opcional.
- [draft] Rechazo tardio de entregables por criterios no acordados.

## Output Format

- [draft] Tabla de gate candidato, fase, criterio, recommendation source, verification method, decision owner, evidencia reproducible, severidad, categoria, accion por fallo, regla de rework y estado.
- [draft] Lista de bloqueadores y condiciones de deuda aceptable.
- [draft] Politica candidata de testing suficiente/aplicable, shift-left verification, risk-based testing y escalamiento.

## Acceptance Criteria

- [draft] Cada gate candidato es verificable con evidencia definida.
- [draft] Cada gate separa recommendation, verification y decision.
- [draft] Cada gate define evidencia reproducible esperada y no depende solo de narrativa LLM.
- [draft] Cada falla tiene accion operativa clara.
- [draft] Rework default de 2 ciclos, excepciones justificadas, tercer ciclo significativo y escalamiento al owner quedan contemplados.
- [draft] Seguridad/riesgo/compliance queda como categoria obligatoria.
- [draft] Las aprobaciones automaticas quedan aceptadas o pendientes.
