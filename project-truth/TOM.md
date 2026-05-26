# Target Operating Model

Status: ready

## Regla De Uso

- [accepted] El TOM define cómo opera CAFL V1 de punta a punta a nivel conceptual/operativo.
- [accepted] El TOM no crea runtime, commands reales, schemas físicos, validators reales, scripts ni backlog técnico.
- [accepted] El TOM no implementa nada.
- [accepted] El TOM es input directo para el Implementation Blueprint; no lo reemplaza.
- [accepted] `project-truth/` tiene autoridad sobre cualquier documento paralelo.
- [accepted] El TOM queda aprobado solo cuando todos sus acceptance criteria están satisfechos
  y el owner lo marca explícitamente como approved.


## Propósito

- [accepted] Responder cómo opera CAFL V1 de punta a punta sin ambigüedad operativa,
  de modo que el Implementation Blueprint pueda arrancar desde una base validada.
- [accepted] El TOM define el modelo operativo genérico aplicable a todos los módulos.
- [accepted] El piloto aprobado en CRIT-07 (solicitudes internas / aprobaciones simples)
  se instancia como sección concreta dentro del TOM para validar el modelo genérico
  con un caso real acotado.


## Qué Debe Responder El TOM

### Roles Y Capacidades

- [draft] Qué roles/capacidades participan en CAFL V1.
- [draft] Qué hace OpenCode dentro del modelo operativo.
- [draft] Qué hacen los agents (responsabilidades, límites, handoffs).
- [draft] Qué hacen los commands (cuándo, quién los invoca, qué producen).
- [draft] Qué hacen scripts/validators (rol en el flujo, no implementación).
- [draft] Qué hace el owner (decisiones críticas, aprobaciones, escalamiento).
- [draft] Qué es automático vs asistido vs exclusivamente humano.

### Flujo Operativo Punta A Punta

- [draft] Cómo entra una idea al sistema.
- [draft] Cómo se convierte en PRD (quién, qué produce, qué valida).
- [draft] Cómo pasa de PRD a SDD.
- [draft] Cómo se crea el task/context packet.
- [draft] Cómo se valida DoR (quién valida, qué bloquea si no pasa).
- [draft] Cómo se ejecuta una tarea.
- [draft] Cómo se ejecutan los gates (quién recomienda, quién verifica, quién decide).
- [draft] Cómo se registra evidencia (qué queda, dónde lógicamente, quién la produce).
- [draft] Cómo opera knowledge governance en el flujo V1
  (source registry, knowledge artifacts, Curation Mode activado por Knowledge Gap,
  modo mínimo por defecto).
- [draft] Cómo se maneja rework (ciclos, contadores, condiciones).
- [draft] Qué pasa cuando un módulo no cierra después del rework máximo
  (¿se descarta, se replantea scope, se escala con qué consecuencias?).
- [draft] Cómo se escala al owner (qué eventos lo activan, qué decide el owner, qué sigue).
- [draft] Cómo se cierra un módulo (DoD, evidencia final, estado autoritativo).

### Control Y Bloqueos

- [draft] Qué se bloquea y bajo qué condición.
- [draft] Qué se escala y bajo qué condición.
- [draft] Qué evidencia se genera en cada fase/transición relevante.

### Knowledge Governance En El Flujo V1

- [accepted] Knowledge Governance arranca en modo mínimo en V1.
- [accepted] Curation Mode se activa por Knowledge Gap, no desde el inicio.
- [draft] Cómo opera el source registry dentro del flujo operativo.
- [draft] Cómo se crean y usan knowledge artifacts durante el desarrollo de un módulo.
- [draft] Cómo se detecta y gestiona un Knowledge Gap (quién lo detecta, qué bloquea, cómo se resuelve).
- [draft] Qué condiciones activan Curation Mode y qué cambia en el flujo cuando está activo.

### Instancia En El Piloto

- [accepted] El TOM cubre el modelo operativo genérico para todos los módulos.
- [accepted] El piloto (solicitudes internas / aprobaciones simples) se instancia
  como sección concreta dentro del TOM para validar el modelo genérico
  con un caso real acotado.
- [draft] Qué simplificaciones o restricciones aplican en el piloto vs el modelo general.
- [draft] Cómo el flujo genérico se recorre concretamente en el piloto paso a paso.

### Handoff Al Blueprint

- [draft] Lista explícita de artefactos que el TOM entrega al Implementation Blueprint
  (no en abstracto; lista concreta de outputs esperados).
- [draft] Qué decisiones de implementación física/técnica quedan deliberadamente
  fuera del TOM y deben resolverse en el Blueprint.


## Lo Que El TOM NO Hace

- [accepted] No crea runtime.
- [accepted] No crea commands reales.
- [accepted] No crea schemas físicos finales.
- [accepted] No crea validators reales.
- [accepted] No crea scripts.
- [accepted] No crea backlog técnico.
- [accepted] No implementa nada.
- [accepted] No reabre decisiones aprobadas en CRIT-01..CRIT-07.
- [accepted] No crea CRIT-08 ni sesiones críticas nuevas.


## Inputs

- [accepted] CRIT-01..CRIT-07 approved en `project-truth/critical-map.md`.
- [accepted] `project-truth/decisions/accepted.md`.
- [accepted] `project-truth/risks.md`.
- [accepted] Respuestas y aclaraciones del owner durante la sesión TOM como fuente primaria.
- [accepted] `framework/` queda descartado como input; no debe usarse.
- [accepted] Conversaciones externas no son fuente válida para completar decisiones.


## Outputs Esperados Del TOM

- [draft] Mapa operativo V1 aprobado: roles, capacidades, flujo, mecanismos, bloqueos,
  escalamientos y knowledge governance.
- [draft] Instancia del modelo operativo sobre el piloto aprobado con
  simplificaciones/restricciones explícitas.
- [draft] Lista explícita de artefactos y decisiones que el TOM pasa al Blueprint.
- [draft] Lista explícita de decisiones técnicas/físicas deliberadamente fuera del TOM.
- [draft] Actualizaciones a `decisions/accepted.md`, `decisions/pending.md` y `risks.md`
  según corresponda.


## Acceptance Criteria

El TOM queda aprobado si y solo si:

- [draft] Cada rol/capacidad tiene responsabilidades, límites y handoffs sin ambigüedad operativa.
- [draft] Cada fase del flujo tiene: entrada, salida esperada, evidencia mínima, quién ejecuta,
  quién valida, condición de bloqueo y condición de avance.
- [draft] Cada gate puede responder: qué recomienda, qué verifica, con qué evidencia,
  quién decide y qué pasa si falla (incluyendo el caso de rework máximo agotado).
- [draft] Knowledge governance tiene un lugar explícito en el flujo V1:
  modo mínimo por defecto, activación de Curation Mode por Knowledge Gap,
  sin quedar flotando entre TOM y Blueprint.
- [draft] El modelo operativo genérico cubre todos los módulos sin restricción a un dominio
  específico dentro de V1.
- [draft] El piloto queda instanciado concretamente con simplificaciones/restricciones
  explícitas respecto al modelo genérico.
- [draft] Los outputs del TOM al Blueprint están listados concretamente,
  no como categorías abiertas.
- [draft] Lo que queda fuera del TOM está listado explícitamente para el Blueprint.
- [draft] El owner aprueba explícitamente el TOM.
- [draft] No se creó runtime, commands reales, schemas físicos, validators reales,
  scripts ni backlog técnico durante la sesión.


## Open Questions

- [accepted] El TOM cubre el modelo operativo genérico para todos los módulos;
  el piloto (solicitudes internas / aprobaciones simples) se instancia como ejemplo
  concreto dentro del mismo documento, no como scope separado.
- [accepted] Knowledge Governance arranca en modo mínimo en V1;
  Curation Mode se activa por Knowledge Gap, no desde el inicio.


## Dependencies

- [accepted] Depende de CRIT-01..CRIT-07 todos approved.
- [accepted] Alimenta directamente el Implementation Blueprint.
- [accepted] Alimenta `decisions/accepted.md`, `decisions/pending.md` y `risks.md`.
