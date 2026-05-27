# CAFL V1 Implementation Blueprint Working Contract

Status: working-contract-created__iteration-01-not-started

Metodologia: Contract-Driven + ADRs ligeros + Ordered Spike-Driven Validation + Walking Skeleton + Risk-Based V1 Scoping + Bidirectional Traceability Matrix

Piloto V1: solicitudes internas / aprobaciones simples (DEC-ACCEPTED-162)

Source policy minima pre-autorizada: docs.odoo.com + github.com/odoo/odoo (DEC-ACCEPTED-163)

SDK/server: fuera de core V1 (DEC-ACCEPTED-164)

TOM aprobado: DEC-ACCEPTED-161

## Proposito Del Working Contract

- [accepted] Este archivo crea el working contract oficial para elaborar el Implementation Blueprint de CAFL V1.
- [accepted] Este archivo no elabora el Blueprint.
- [accepted] Este archivo no disena componentes tecnicos.
- [accepted] Este archivo no crea schemas, validators, commands, agents, runtime, backlog, RAG/base vectorial ni implementacion.
- [accepted] Este archivo establece estructura aprobada, modelo iterativo, reglas entre iteraciones, non-goals y acceptance criteria globales.

## Fuentes Obligatorias

- [accepted] `project-truth/TOM.md`.
- [accepted] `project-truth/decisions/accepted.md`.
- [accepted] `project-truth/decisions/pending.md`.
- [accepted] `project-truth/critical-map.md`.
- [accepted] `project-truth/risks.md`.
- [accepted] `project-truth/decisions/rejected.md`.
- [accepted] `project-truth/decisions/superseded.md`.

## Orden De Autoridad Para El Blueprint

1. `project-truth/decisions/accepted.md`
2. `project-truth/TOM.md`
3. `project-truth/decisions/rejected.md`
4. `project-truth/decisions/superseded.md`
5. `project-truth/critical-map.md`
6. `project-truth/decisions/pending.md`
7. `project-truth/risks.md` como soporte

## Conflict And Owner Decision Register

- [accepted] Si una iteracion o agente futuro detecta conflicto entre fuentes, debe registrarlo en este Conflict And Owner Decision Register.
- [accepted] Si el conflicto bloquea avance, debe marcarlo como `needs-owner-decision`.
- [accepted] Si el conflicto no bloquea avance pero requiere seguimiento, debe marcarlo como `open-question`.
- [accepted] El agente no debe resolver conflictos por criterio propio.

| ID | Tipo | Descripcion | Status | Accion requerida |
| --- | --- | --- | --- | --- |
| none | none | No se detectaron conflictos entre fuentes obligatorias al crear este working contract. | not-applicable | none |

## Iteration Model

- [accepted] El Implementation Blueprint se elabora en 5 iteraciones secuenciales.
- [accepted] Cada iteracion trabaja solo las secciones asignadas a esa iteracion.
- [accepted] Cada iteracion termina en `Status: pending-owner-approval`.
- [accepted] La siguiente iteracion solo puede arrancar con aprobacion explicita del owner.
- [accepted] Si una iteracion detecta un blocker que afecta una iteracion anterior, se detiene y pide revision owner; no corrige silenciosamente contenido anterior.
- [accepted] Ninguna iteracion puede implementar, crear backlog, crear runtime ni avanzar secciones futuras.

### Patron Obligatorio Por Iteracion

- Status: `pending-owner-approval` al cierre de la iteracion.
- Scope: solo secciones de esa iteracion.
- Non-goals: no implementar, no crear backlog y no avanzar a secciones futuras.
- Outputs: decisiones de diseno, trade-offs, riesgos, spikes e inputs para la siguiente iteracion.

### Iteraciones Y Secciones

| Iteracion | Nombre | Secciones |
| --- | --- | --- |
| Iteration 1 | Marco arquitectonico base | 1. Blueprint Scope and Non-Goals; 2. Architecture Principles; 3. V1 / Post-V1 Boundary; 4. Runtime Layout Candidate; 5. Source-vs-Runtime Structure; 6. Initial Spike Map |
| Iteration 2 | Diseno operativo de mecanismos | 7. OpenCode Operating Design; 8. Agents / Commands / Scripts / Validators Split |
| Iteration 3 | Artefactos tecnicos de control | 9. Schemas V1 Minimum Set; 10. Validators V1 Minimum Set; 11. State / Logs / Evidence Storage; 12. Knowledge Base and Source Policy Implementation |
| Iteration 4 | Ejecucion Odoo y piloto | 13. Odoo 18 Execution Environment; 14. Security and Secrets; 15. Pilot Module Blueprint |
| Iteration 5 | Cierre del Blueprint | 16. Spikes and Technical Validations final order; 17. Bidirectional Traceability Matrix; 18. Blueprint Outputs to Backlog; 19. Acceptance Criteria |

## Rules

- RULE-01: Cada iteracion termina en `Status: pending-owner-approval`.
- RULE-02: La siguiente iteracion solo arranca con aprobacion owner explicita.
- RULE-03: Si una iteracion detecta un blocker que afecta una iteracion anterior, se detiene y pide revision owner; no corrige silenciosamente.
- RULE-04: Todo componente del Blueprint debe tener respaldo en TOM, CRIT aprobado o decision aceptada. Si no tiene respaldo, debe eliminarse, marcarse como post-V1 o registrarse como `owner decision required`.
- RULE-05: La Traceability Matrix debe ser bidireccional: TOM requirement -> Blueprint component y Blueprint component -> TOM requirement.
- RULE-06: Spikes deben tener orden de ejecucion explicito y justificado con dependencias. No pueden quedar como lista plana.
- RULE-07: Pilot Module Blueprint disena como el framework soportara el piloto a nivel de componentes, no PRD final, SDD final ni backlog funcional del piloto.
- RULE-08: Blueprint Outputs to Backlog solo puede listar categorias de trabajo, no tareas detalladas.
- RULE-09: El Blueprint no crea runtime, agents ejecutables, commands reales, schemas fisicos, validators reales, scripts, RAG/base vectorial, backlog tecnico ni implementacion.
- RULE-10: El Blueprint no usa `framework/` como input ni referencia.

## Non-Goals Globales Del Blueprint

- No implementa runtime.
- No crea agents ejecutables finales.
- No crea commands reales.
- No crea schemas fisicos finales.
- No crea validators reales.
- No crea scripts.
- No crea RAG/base vectorial.
- No crea backlog tecnico detallado.
- No crea PRD final del piloto.
- No crea SDD final del piloto.
- No reabre decisiones aprobadas en CRIT-01..07 ni en TOM.
- No crea CRIT-08.
- No recrea `framework/`.

## Acceptance Criteria Globales Del Blueprint

El Blueprint completo queda approved si y solo si:

- Las 5 iteraciones estan elaboradas y aprobadas por el owner.
- Cada componente tiene respaldo trazable en TOM o decisiones aceptadas.
- La Traceability Matrix bidireccional esta completa sin gaps.
- No existen componentes sin respaldo ni decisiones tecnicas ocultas.
- El Spike Execution Order esta definido con dependencias justificadas.
- Pilot Module Blueprint no contiene PRD/SDD/backlog funcional.
- Blueprint Outputs to Backlog lista solo categorias, no tareas.
- No se creo runtime, agents ejecutables, commands reales, schemas fisicos, validators reales, scripts, RAG/base vectorial, backlog tecnico ni implementacion.
- El owner aprueba explicitamente el Blueprint completo.

## Secciones Placeholder Por Iteracion

### Iteration 1 - Marco arquitectonico base

#### 1. Blueprint Scope and Non-Goals

Status: not-started

Inputs esperados:

- TOM aprobado y decisiones aceptadas relacionadas con alcance y limites.
- Reglas globales de este working contract.

Outputs esperados:

- Alcance y non-goals del Blueprint para alimentar secciones posteriores.

Restricciones especificas:

- No reabrir CRIT-01..07, TOM ni piloto V1.
- No crear backlog ni implementacion.

Acceptance criteria minimos:

- La seccion queda trazable a fuentes autorizadas y no introduce componentes sin respaldo.

#### 2. Architecture Principles

Status: not-started

Inputs esperados:

- Seccion 1 aprobada dentro de la iteracion correspondiente.
- TOM aprobado y decisiones aceptadas aplicables a principios operativos.

Outputs esperados:

- Principios de arquitectura para guiar secciones posteriores.

Restricciones especificas:

- No introducir principios sin respaldo en TOM, CRIT aprobado o decision aceptada.

Acceptance criteria minimos:

- Cada principio queda trazable y no contradice decisiones aceptadas o rechazadas.

#### 3. V1 / Post-V1 Boundary

Status: not-started

Inputs esperados:

- Secciones 1 y 2 de la iteracion correspondiente.
- Decisiones aceptadas, rechazadas y superseded sobre scope V1 y post-V1.

Outputs esperados:

- Limite V1 / post-V1 para guiar secciones posteriores.

Restricciones especificas:

- No mover capacidades post-V1 a V1 sin decision owner explicita.

Acceptance criteria minimos:

- Cada limite queda trazable y no reabre decisiones aprobadas.

#### 4. Runtime Layout Candidate

Status: not-started

Inputs esperados:

- Secciones 1, 2 y 3 de la iteracion correspondiente.
- Handoff del TOM al Blueprint y decisiones CRIT-07 aplicables.

Outputs esperados:

- Candidato conceptual de layout para alimentar secciones de estructura, mecanismos y storage.

Restricciones especificas:

- No crear runtime, rutas fisicas finales ni archivos ejecutables.
- No usar `framework/` como input.

Acceptance criteria minimos:

- El candidato queda conceptual, trazable y sin implementacion.

#### 5. Source-vs-Runtime Structure

Status: not-started

Inputs esperados:

- Seccion 4 de la iteracion correspondiente.
- Reglas aprobadas sobre fuente de verdad, estado autoritativo y runtime.

Outputs esperados:

- Separacion source-vs-runtime para alimentar secciones posteriores.

Restricciones especificas:

- No recrear `framework/` ni usarlo como referencia.
- No crear estructura fisica runtime.

Acceptance criteria minimos:

- La separacion queda trazable y no duplica fuentes de verdad.

#### 6. Initial Spike Map

Status: not-started

Inputs esperados:

- Secciones 1 a 5 de la iteracion correspondiente.
- Riesgos aceptados y technical validations/spikes registrados en TOM.

Outputs esperados:

- Mapa inicial de spikes para alimentar orden final de validaciones.

Restricciones especificas:

- No ejecutar spikes.
- No dejar spikes como lista plana cuando la seccion sea elaborada.

Acceptance criteria minimos:

- Cada spike esperado queda vinculado a riesgo, decision o dependencia sin ejecutarse.

### Iteration 2 - Diseno operativo de mecanismos

#### 7. OpenCode Operating Design

Status: not-started

Inputs esperados:

- Iteration 1 aprobada por owner.
- Secciones 1 a 6 elaboradas y aprobadas.

Outputs esperados:

- Diseno operativo OpenCode para alimentar el split de mecanismos.

Restricciones especificas:

- No configurar OpenCode.
- No crear agents, commands, skills, plugins, permissions ni runtime ejecutable.

Acceptance criteria minimos:

- La seccion queda trazable y no implementa configuracion.

#### 8. Agents / Commands / Scripts / Validators Split

Status: not-started

Inputs esperados:

- Seccion 7 de la iteracion correspondiente.
- Capacidades operativas del TOM y decisiones aceptadas sobre modelo mixto.

Outputs esperados:

- Split de responsabilidades por mecanismo para alimentar artefactos de control.

Restricciones especificas:

- No crear agents ejecutables, commands reales, scripts ni validators reales.
- No tratar commands como autoridad final de gates, estado o cierre.

Acceptance criteria minimos:

- Cada asignacion esperada queda respaldada y sin artefactos ejecutables.

### Iteration 3 - Artefactos tecnicos de control

#### 9. Schemas V1 Minimum Set

Status: not-started

Inputs esperados:

- Iteration 2 aprobada por owner.
- Secciones 7 y 8 elaboradas y aprobadas.
- Modelo logico CRIT-06 y direccion CRIT-07 aplicables.

Outputs esperados:

- Set minimo conceptual de schemas V1 para alimentar validators y storage.

Restricciones especificas:

- No crear schemas fisicos finales ni archivos de schema.

Acceptance criteria minimos:

- Cada schema esperado queda justificado por control, trazabilidad o evidencia.

#### 10. Validators V1 Minimum Set

Status: not-started

Inputs esperados:

- Seccion 9 de la iteracion correspondiente.
- Decisiones aceptadas sobre validators minimos y control deterministico.

Outputs esperados:

- Set minimo conceptual de validators para alimentar gates, evidence y execution checks.

Restricciones especificas:

- No crear validators reales, toolchain ejecutable ni scripts.

Acceptance criteria minimos:

- Cada validator esperado queda trazable a un control requerido y no sustituye juicio tecnico ni owner approval.

#### 11. State / Logs / Evidence Storage

Status: not-started

Inputs esperados:

- Secciones 9 y 10 de la iteracion correspondiente.
- Modelo logico de estado, logs, evidencia e IDs aprobado en CRIT-06.

Outputs esperados:

- Diseno de storage conceptual para alimentar evidence, traceability y backlog categories.

Restricciones especificas:

- No crear storage fisico, rutas finales, logs reales ni artifacts.

Acceptance criteria minimos:

- La seccion preserva estado autoritativo, evidencia reproducible y no double work sin implementar storage.

#### 12. Knowledge Base and Source Policy Implementation

Status: not-started

Inputs esperados:

- Secciones 9, 10 y 11 de la iteracion correspondiente.
- DEC-ACCEPTED-163 y reglas TOM de Knowledge Governance.

Outputs esperados:

- Implementacion conceptual de source policy y knowledge governance para alimentar Odoo execution y pilot support.

Restricciones especificas:

- No crear RAG/base vectorial.
- No ampliar fuentes sin Curation Request y aprobacion owner.
- No implementar source registry, artifacts, validators ni scripts.

Acceptance criteria minimos:

- La seccion respeta source policy minima, Knowledge Gap y Curation Request sin implementacion.

### Iteration 4 - Ejecucion Odoo y piloto

#### 13. Odoo 18 Execution Environment

Status: not-started

Inputs esperados:

- Iteration 3 aprobada por owner.
- Secciones 9 a 12 elaboradas y aprobadas.
- DEC-ACCEPTED-135 y DEC-ACCEPTED-153.

Outputs esperados:

- Definicion conceptual del entorno Odoo 18 para alimentar security, pilot y spikes finales.

Restricciones especificas:

- No instalar Odoo, crear entorno real, ejecutar tests ni crear scripts.

Acceptance criteria minimos:

- La seccion identifica dependencias de validacion sin ejecutar entorno.

#### 14. Security and Secrets

Status: not-started

Inputs esperados:

- Seccion 13 de la iteracion correspondiente.
- Reglas TOM sobre seguridad, riesgo, compliance, datos y owner approval.

Outputs esperados:

- Modelo conceptual de seguridad y secrets para alimentar pilot support y spikes finales.

Restricciones especificas:

- No crear secretos, tokens, certificados, configuraciones reales ni policies ejecutables.

Acceptance criteria minimos:

- La seccion cubre controles esperados sin exponer ni generar secretos.

#### 15. Pilot Module Blueprint

Status: not-started

Inputs esperados:

- Secciones 13 y 14 de la iteracion correspondiente.
- Piloto V1 confirmado por DEC-ACCEPTED-162 y restricciones TOM del piloto.

Outputs esperados:

- Blueprint del soporte del framework para el piloto a nivel de componentes.

Restricciones especificas:

- No crear PRD final del piloto.
- No crear SDD final del piloto.
- No crear backlog funcional del piloto.
- No reabrir seleccion del piloto.

Acceptance criteria minimos:

- La seccion explica soporte del framework al piloto sin convertirse en PRD, SDD o backlog.

### Iteration 5 - Cierre del Blueprint

#### 16. Spikes and Technical Validations final order

Status: not-started

Inputs esperados:

- Iteration 4 aprobada por owner.
- Secciones 1 a 15 elaboradas y aprobadas.
- Initial Spike Map y riesgos aplicables.

Outputs esperados:

- Orden final de spikes y technical validations con dependencias justificadas.

Restricciones especificas:

- No ejecutar spikes ni cerrar resultados de validacion.
- No dejar una lista plana sin dependencias.

Acceptance criteria minimos:

- Cada spike queda ordenado, justificado y conectado a dependencias, riesgos o decisiones.

#### 17. Bidirectional Traceability Matrix

Status: not-started

Inputs esperados:

- Secciones 1 a 16 elaboradas y aprobadas.
- TOM aprobado y decisiones aceptadas aplicables.

Outputs esperados:

- Matriz bidireccional TOM requirement -> Blueprint component y Blueprint component -> TOM requirement.

Restricciones especificas:

- No aprobar componentes sin respaldo trazable.

Acceptance criteria minimos:

- La matriz queda completa, bidireccional y sin gaps.

#### 18. Blueprint Outputs to Backlog

Status: not-started

Inputs esperados:

- Secciones 1 a 17 elaboradas y aprobadas.
- Traceability Matrix completa.

Outputs esperados:

- Categorias de trabajo para backlog posterior.

Restricciones especificas:

- No crear backlog tecnico detallado.
- No listar tareas detalladas ni secuencia de implementacion.

Acceptance criteria minimos:

- La seccion lista solo categorias y preserva el limite no-backlog.

#### 19. Acceptance Criteria

Status: not-started

Inputs esperados:

- Secciones 1 a 18 elaboradas y aprobadas.
- Acceptance criteria globales de este working contract.

Outputs esperados:

- Acceptance criteria finales del Blueprint completo para aprobacion owner.

Restricciones especificas:

- No declarar el Blueprint approved sin aprobacion owner explicita.

Acceptance criteria minimos:

- Los criterios finales cubren trazabilidad, respaldo, spikes, non-goals y aprobacion owner.

## Blueprint Status Summary

| Iteracion | Numero de seccion | Nombre de seccion | Status | Owner approval | Blocker retroactivo detectado |
| --- | --- | --- | --- | --- | --- |
| Iteration 1 | 1 | Blueprint Scope and Non-Goals | not-started | not-requested | none |
| Iteration 1 | 2 | Architecture Principles | not-started | not-requested | none |
| Iteration 1 | 3 | V1 / Post-V1 Boundary | not-started | not-requested | none |
| Iteration 1 | 4 | Runtime Layout Candidate | not-started | not-requested | none |
| Iteration 1 | 5 | Source-vs-Runtime Structure | not-started | not-requested | none |
| Iteration 1 | 6 | Initial Spike Map | not-started | not-requested | none |
| Iteration 2 | 7 | OpenCode Operating Design | not-started | not-requested | none |
| Iteration 2 | 8 | Agents / Commands / Scripts / Validators Split | not-started | not-requested | none |
| Iteration 3 | 9 | Schemas V1 Minimum Set | not-started | not-requested | none |
| Iteration 3 | 10 | Validators V1 Minimum Set | not-started | not-requested | none |
| Iteration 3 | 11 | State / Logs / Evidence Storage | not-started | not-requested | none |
| Iteration 3 | 12 | Knowledge Base and Source Policy Implementation | not-started | not-requested | none |
| Iteration 4 | 13 | Odoo 18 Execution Environment | not-started | not-requested | none |
| Iteration 4 | 14 | Security and Secrets | not-started | not-requested | none |
| Iteration 4 | 15 | Pilot Module Blueprint | not-started | not-requested | none |
| Iteration 5 | 16 | Spikes and Technical Validations final order | not-started | not-requested | none |
| Iteration 5 | 17 | Bidirectional Traceability Matrix | not-started | not-requested | none |
| Iteration 5 | 18 | Blueprint Outputs to Backlog | not-started | not-requested | none |
| Iteration 5 | 19 | Acceptance Criteria | not-started | not-requested | none |
