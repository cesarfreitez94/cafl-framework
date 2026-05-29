# CAFL V1 Implementation Blueprint Working Contract

Status: blueprint-closed

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

##### 1. Status

Status: closed

Owner approval: approved explicitly by owner.

##### 2. Purpose

Esta seccion define el alcance externo y los non-goals del Implementation Blueprint V1. Su proposito es fijar que es el Blueprint dentro de CAFL V1, que debe transformar desde el TOM aprobado hacia diseno tecnico/conceptual y que limites no puede cruzar durante su elaboracion.

El Implementation Blueprint es el artefacto principal post-TOM para convertir el modelo operativo aprobado en decisiones de diseno tecnico trazables, validaciones tecnicas planificadas y salidas controladas hacia backlog posterior. No reemplaza `project-truth/`, no aprueba backlog y no autoriza implementacion.

Esta seccion funciona como guardrail para las secciones futuras. No disena runtime layout en detalle, source-vs-runtime structure, OpenCode operating design, split de agents/commands/scripts/validators, schemas, validators, storage, KB, source policy implementation, entorno Odoo, security, pilot module, spikes, traceability matrix ni backlog categories.

##### 3. Scope

- El Blueprint debe transformar el TOM aprobado, CRIT-01..07 approved y decisiones aceptadas en diseno tecnico/conceptual de CAFL V1 sin reabrirlos.
- El Blueprint debe mantener `project-truth/` como fuente de verdad aprobada y `project-truth/implementation-blueprint.md` como artefacto principal del Blueprint.
- El Blueprint debe preservar el scope V1 aprobado: CAFL opera sobre OpenCode, dominio Odoo, target V1 Odoo 18, flujo end-to-end verificable y piloto V1 confirmado de solicitudes internas / aprobaciones simples.
- El Blueprint debe disenar, solo en las secciones asignadas, la traduccion tecnica/conceptual del TOM hacia principios de arquitectura, limite V1/post-V1, runtime layout candidate, source-vs-runtime structure, mecanismos OpenCode, split de mecanismos, schemas/validators conceptuales, storage, source policy implementation, entorno Odoo 18, security/secrets, soporte del piloto, spikes, trazabilidad y acceptance criteria.
- El Blueprint debe planificar technical validations/spikes requeridos por TOM, decisiones aceptadas y riesgos, sin ejecutarlos.
- El Blueprint debe preparar salidas hacia backlog posterior solo como categorias de trabajo cuando llegue la seccion 18, no como tareas detalladas.
- El Blueprint debe mantener la source policy minima pre-autorizada: documentacion oficial Odoo y repositorio oficial GitHub `odoo/odoo`.
- El Blueprint debe reconocer que SDK/server queda fuera de core V1 y que RAG/base vectorial queda fuera de V1.
- El Blueprint debe instanciar el diseno sobre el piloto confirmado sin crear PRD final, SDD final ni backlog funcional del piloto.

##### 4. Non-Goals

- El Blueprint no reabre CRIT-01..07, el TOM approved, la seleccion del piloto V1, Odoo 18 como target V1, la source policy minima pre-autorizada ni SDK/server fuera de core V1.
- El Blueprint no crea runtime.
- El Blueprint no crea backlog tecnico detallado.
- El Blueprint no implementa modulo Odoo.
- El Blueprint no crea PRD final ni SDD final del piloto.
- El Blueprint no crea agents ejecutables, commands reales, schemas fisicos, validators reales ni scripts.
- El Blueprint no configura OpenCode ni crea permisos, plugins, MCP, skills ejecutables o tooling real.
- El Blueprint no crea RAG/base vectorial y no carga toda la documentacion desde el dia 1.
- El Blueprint no usa `framework/` como input, referencia, evidencia secundaria, layout base, fuente de agents, commands, contracts, gates, schemas, validators, runtime ni knowledge base.
- El Blueprint no crea CRIT-08, no recrea `framework/` y no crea documentos paralelos que compitan con `project-truth/`.
- Esta seccion no adelanta decisiones tecnicas fisicas que corresponden a secciones futuras del Blueprint.

##### 5. Fixed Decisions

- CRIT-01..07 estan completos y approved; no se reabren en el Blueprint.
- El TOM esta approved por DEC-ACCEPTED-161; el Blueprint lo usa como input directo y no lo reabre.
- `project-truth/` sigue siendo la fuente de verdad aprobada; el repo previo y `framework/` no son autoridad de diseno.
- CAFL V1 es Odoo-only y el target V1 es Odoo 18.
- OpenCode es runtime principal y CAFL V1 usa un modelo hibrido progresivo; V1 no es agents-only ni puramente manual o solo narrativa.
- El piloto V1 confirmado es solicitudes internas / aprobaciones simples por DEC-ACCEPTED-162; el Blueprint no reabre su seleccion.
- La source policy minima pre-autorizada por DEC-ACCEPTED-163 es documentacion oficial Odoo y repositorio oficial GitHub `odoo/odoo`; cualquier otra fuente requiere Curation Request y aprobacion antes de usarse para disenar o implementar.
- SDK/server queda fuera de core V1 por DEC-ACCEPTED-164; solo puede entrar con spike favorable posterior y decision explicita del owner.
- RAG/base vectorial no queda aprobado para V1 y se difiere a V2/post-V1 salvo decision futura explicita.
- Despliegue productivo real, integraciones externas reales por defecto, dashboard/UI del framework, CI/CD completo, DB avanzada, multiusuario/equipo, plugins/MCP y curation avanzada no forman parte del core V1.

##### 6. Deferred Areas

- Secciones 2 a 6: principios de arquitectura, limite V1/post-V1, runtime layout candidate, source-vs-runtime structure e Initial Spike Map quedan para elaboracion posterior dentro de Iteration 1, sin adelantarse en esta seccion.
- Secciones 7 a 15: OpenCode operating design, split de agents/commands/scripts/validators, schemas, validators, state/logs/evidence storage, source policy implementation, entorno Odoo 18, security/secrets y Pilot Module Blueprint quedan para sus secciones asignadas.
- Secciones 16 a 19: orden final de spikes, matriz de trazabilidad bidireccional, salidas a backlog y acceptance criteria finales quedan para el cierre del Blueprint.
- Backlog posterior: queda para despues del Blueprint aprobado; el Blueprint solo puede producir categorias de trabajo, no tareas detalladas ni secuencia de implementacion.
- Implementacion posterior: runtime real, modulo Odoo, agents ejecutables, commands reales, schemas fisicos, validators reales, scripts, configuracion OpenCode, storage fisico real, logs reales y evidence capture real quedan fuera del Blueprint.
- Post-V1: RAG/base vectorial, SDK/server core, dashboard/UI, CI/CD completo, integraciones reales por defecto, legal-compliance avanzado, KB amplia, OpenAPI/PDF automatico, DB avanzada, multiusuario/equipo, plugins/MCP, curation avanzada, OWL avanzado y Playwright quedan diferidos salvo condicion o decision futura explicita.

##### 7. Scope Guardrails

- Todo componente del Blueprint debe tener respaldo trazable en TOM, CRIT aprobado o decision aceptada; si no lo tiene, debe eliminarse, marcarse post-V1 o registrarse como `owner decision required`.
- El orden de autoridad del working contract aplica sin cambios: decisiones aceptadas, TOM, decisiones rechazadas, decisiones superseded, critical map, decisiones pendientes y riesgos como soporte.
- Si aparece un conflicto entre fuentes, esta seccion no lo resuelve por criterio propio; debe registrarlo como `open-question` o `needs-owner-decision` segun bloqueo.
- Ninguna seccion puede convertir recomendaciones en implementacion, crear backlog, crear runtime ni avanzar contenido asignado a secciones futuras.
- Esta seccion no puede crear nombres definitivos de archivos runtime, rutas fisicas finales, ADRs detallados, commands finales, schemas finales, validators finales, scripts ni decisiones fisicas que correspondan a secciones posteriores.
- La source policy no se amplia dentro del Blueprint sin Curation Request y aprobacion owner; la busqueda web libre no es fuente directa de diseno o implementacion.
- `framework/` permanece excluido como input y no puede ser auditado, migrado, recreado ni usado como referencia por conveniencia.
- Los documentos fuera de `project-truth/` no pueden convertirse en fuente paralela ni competir con `implementation-blueprint.md`.
- El avance a secciones futuras requiere instruccion y aprobacion correspondiente; esta ejecucion solo deja la seccion 1 en `pending-owner-approval`.

##### 8. Open Questions / Owner Decisions

- none

##### 9. Acceptance Criteria

- La seccion queda en `Status: pending-owner-approval`.
- La seccion define que es el Implementation Blueprint dentro de CAFL V1 y como transforma el TOM approved hacia diseno tecnico/conceptual.
- La seccion lista scope, non-goals, fixed decisions, deferred areas y guardrails sin crear componentes sin respaldo.
- La seccion reconoce explicitamente que CRIT-01..07 y TOM approved no se reabren.
- La seccion reconoce explicitamente el piloto V1 confirmado, Odoo 18 target V1, source policy minima pre-autorizada, SDK/server fuera de core V1 y RAG/base vectorial fuera de V1.
- La seccion confirma que el Blueprint no crea runtime, backlog tecnico detallado, implementacion Odoo, PRD final, SDD final, agents ejecutables, commands reales, schemas fisicos, validators reales ni scripts.
- La seccion no elabora secciones 2 a 19 ni modifica reglas globales del working contract.
- La seccion no introduce decisiones no trazadas a `project-truth/` ni documentos paralelos.

##### 10. Section Output

- Para la seccion 2, entrega limites de scope y non-goals que los principios de arquitectura no pueden violar.
- Para la seccion 3, entrega decisiones fijas y areas diferidas que deben guiar el limite V1/post-V1 sin reabrir CRIT-01..07 ni TOM.
- Para la seccion 4, entrega guardrails para mantener el runtime layout candidate conceptual, sin runtime real, rutas fisicas finales ni uso de `framework/`.
- Para la seccion 5, entrega guardrails para separar source-vs-runtime sin duplicar fuentes de verdad, sin documentos paralelos y sin recrear `framework/`.
- Para la seccion 6, entrega limites para mapear spikes desde decisiones y riesgos sin ejecutarlos ni convertirlos en backlog o implementacion.

#### 2. Architecture Principles

##### 1. Status

Status: closed

Owner approval: approved explicitly by owner.

##### 2. Purpose

Esta seccion define los principios arquitectonicos de CAFL V1 que deben guiar las secciones posteriores del Blueprint. Los principios traducen el TOM aprobado y las decisiones aceptadas a reglas de diseno conceptual, sin crear runtime, layout fisico final, agents ejecutables, commands reales, schemas fisicos, validators reales, scripts, backlog, PRD, SDD ni implementacion.

Los principios son vinculantes para el Blueprint: cualquier componente posterior debe respetarlos o registrar un conflicto/open question segun las reglas del working contract. Esta seccion no decide rutas fisicas, archivos finales, tooling concreto, permisos OpenCode finales, entorno Odoo exacto ni orden final de spikes.

##### 3. Inputs Used

- Seccion 1 aprobada: scope, non-goals, fixed decisions, deferred areas y guardrails del Blueprint.
- TOM aprobado por DEC-ACCEPTED-161.
- Decisiones aceptadas aplicables: DEC-ACCEPTED-013..033, 035..053, 055..069, 071..088, 089..105, 106..130, 131..158 y 162..164.
- Decisiones rechazadas aplicables: no agents-only, no repo/framework como verdad, no cierre por opinion, no evidencia solo narrativa, no busqueda web libre, no RAG/base vectorial obligatorio, no SDK/server core obligatorio, no V1 puramente manual.
- Riesgos aplicables: RISK-006, RISK-010, RISK-020, RISK-023, RISK-024, RISK-043, RISK-052, RISK-055, RISK-057, RISK-058, RISK-059, RISK-061, RISK-064 y RISK-065.

##### 4. Architecture Principles

| ID | Principio | Implicacion para secciones posteriores | Trazabilidad |
| --- | --- | --- | --- |
| AP-01 | Fuente de verdad unica y trazabilidad bidireccional. | Todo diseno posterior debe derivar de `project-truth/`, TOM o decision aceptada; ningun componente sin respaldo puede quedar como V1 salvo owner decision. La Traceability Matrix debe poder enlazar TOM/decision -> componente y componente -> TOM/decision. | S01; DEC-ACCEPTED-001, 002, 010, 042, 086, 107, 113, 116; TOM `Regla De Uso`, `Estado Autoritativo`; RISK-006, RISK-011. |
| AP-02 | OpenCode es runtime principal, pero no autoridad de estado, gate ni evidencia por si solo. | El operating design posterior debe usar OpenCode como entorno principal sin convertir salidas LLM, memoria de chat o commands candidatos en estado autoritativo o decision final. | DEC-ACCEPTED-028, 058, 094, 107, 136, 139; TOM `Roles Y Capacidades`, `Estado Autoritativo`; DEC-REJECTED-013, 021, 023; RISK-023, RISK-024, RISK-035. |
| AP-03 | Modelo hibrido progresivo, no agents-only. | Capacidades posteriores deben asignarse conceptualmente entre agents, commands candidatos, scripts/CLI/validators candidatos, rules/config, skills/playbooks y humano critico, sin crear mecanismos ejecutables en el Blueprint. | DEC-ACCEPTED-056, 068, 069, 136, 137, 140; TOM `Alcance Operativo V1`, `Principios De Responsabilidad`; DEC-REJECTED-011, 033, 036; RISK-022, RISK-055, RISK-057. |
| AP-04 | Separacion entre razonamiento asistido y control verificable. | LLM/agents pueden recomendar, disenar, diagnosticar y redactar; validaciones estructurales, estado, evidencia, rework counters, source policy y ejecucion Odoo deben quedar destinados a control deterministico conceptual cuando aplique. | DEC-ACCEPTED-063, 069, 084, 090, 100, 145; TOM `Automatico, Asistido Y Exclusivamente Humano`; DEC-REJECTED-013, 017, 021; RISK-010, RISK-024, RISK-026. |
| AP-05 | Avance por contratos, gates, evidencia y cierre verificable. | El diseno posterior debe preservar PRD/SDD ligeros, task/context packet + DoR, gates minimos, checks transversales, evidencia reproducible y separacion recommendation/verification/decision; no puede permitir autocierre. | DEC-ACCEPTED-033, 041, 047, 052, 074, 078, 079, 090, 091, 094, 097, 100; TOM `Flujo Operativo Punta A Punta`; DEC-REJECTED-010, 017, 018; RISK-004, RISK-005, RISK-013, RISK-033. |
| AP-06 | Contexto minimo autorizado y source policy por defecto. | Las secciones de KB/source policy y mecanismos deben preservar context routing, token budget, Knowledge Gap y Curation Request; la base pre-autorizada queda limitada a documentacion oficial Odoo y GitHub `odoo/odoo`. | DEC-ACCEPTED-042, 065, 082, 116, 126, 127, 128, 150, 163; TOM `Knowledge Governance En El Flujo V1`; DEC-REJECTED-025, 026, 027; RISK-018, RISK-043, RISK-052, RISK-062. |
| AP-07 | V1 Odoo-only con Odoo 18 y piloto confirmado. | El Blueprint debe optimizar decisiones para un flujo end-to-end verificable de modulo Odoo 18 y para el piloto de solicitudes internas / aprobaciones simples, sin convertir esta seccion en PRD/SDD/backlog del piloto. | DEC-ACCEPTED-016, 021, 024, 135, 153, 155, 156, 162; TOM `Alcance Operativo V1`, `Instancia En El Piloto V1 Confirmado`; DEC-REJECTED-002, 003; RISK-059, RISK-066. |
| AP-08 | V1 minimo suficiente y anti-scope-creep. | Capacidades como RAG/base vectorial, SDK/server core, dashboard/UI, CI/CD completo, DB avanzada, multiusuario/equipo, plugins/MCP, curation avanzada, integraciones reales por defecto y deployment productivo no deben entrar al core V1 sin decision explicita. | S01; DEC-ACCEPTED-023, 032, 148, 149, 151, 152, 157, 164; TOM `Simplificaciones Del Piloto`, `Lo Que El TOM NO Hace`; DEC-REJECTED-034, 035, 038; RISK-008, RISK-058, RISK-065. |
| AP-09 | Storage, logs y evidencia deben ser simples, auditables y compatibles con Git, hasta que el Blueprint detalle su forma. | Secciones posteriores pueden definir storage conceptual/fisico candidato solo dentro de su alcance; esta seccion fija que debe favorecer auditabilidad, versionado, trazabilidad y no double work. | DEC-ACCEPTED-107, 108, 111, 115, 141, 146; TOM `Reglas Para Evitar Trabajo Doble Documental`, `Handoff Al Blueprint`; RISK-006, RISK-056. |
| AP-10 | Seguridad, riesgo, compliance, secretos y datos son criterios transversales. | El diseno posterior debe mantener triage de seguridad/riesgo/compliance en gates y escalar riesgos criticos; secrets handling queda para seccion/spike posterior sin crear secretos ni policies ejecutables aqui. | DEC-ACCEPTED-045, 059, 064, 076, 092, 101; TOM `Control Y Bloqueos`, `Owner Approval Obligatorio`; RISK-021, RISK-027, RISK-040, RISK-063. |
| AP-11 | Validacion tecnica por spikes antes de cerrar decisiones fisicas inciertas. | Lenguaje scripts/CLI, entorno Odoo 18 exacto, permisos OpenCode, schema/validator toolchain, storage/log conventions, source policy enforcement, evidence capture y secrets handling deben resolverse mediante Blueprint/spikes, no por suposicion. | DEC-ACCEPTED-049, 142, 143, 158; TOM `Technical Validations / Spikes Que Blueprint Debe Planificar`; RISK-020, RISK-059, RISK-060, RISK-061. |
| AP-12 | Diseno greenfield desde `project-truth/`; `framework/` excluido. | Ninguna seccion posterior puede usar `framework/` como layout, evidencia, fuente de agents, commands, contracts, gates, schemas, validators, runtime o KB. | S01; DEC-ACCEPTED-003, 133, 134; DEC-SUPERSEDED-002, 003; DEC-REJECTED-032; TOM `Lo Que El TOM NO Hace`; RISK-064. |

##### 5. Cross-Section Guidance

- Seccion 3 debe usar AP-07 y AP-08 para separar V1/post-V1 sin mover capacidades diferidas al core V1.
- Seccion 4 debe usar AP-02, AP-03, AP-04, AP-09 y AP-12 para proponer solo un runtime layout candidate conceptual, sin rutas finales ni runtime real.
- Seccion 5 debe usar AP-01, AP-06, AP-09 y AP-12 para separar fuente, estado autoritativo y runtime sin duplicar fuentes de verdad.
- Seccion 6 debe usar AP-11 para mapear spikes desde riesgos, decisiones y dependencias, sin ejecutarlos.
- Secciones 7 y 8 deben usar AP-02, AP-03, AP-04 y AP-05 para disenar operacion OpenCode y split de mecanismos sin crear agents/commands/scripts/validators reales.
- Secciones 9 a 12 deben usar AP-01, AP-04, AP-06 y AP-09 para schemas/validators/storage/source policy conceptuales y trazables.
- Secciones 13 a 15 deben usar AP-07, AP-10 y AP-11 para entorno Odoo 18, security/secrets y soporte del piloto sin PRD/SDD/backlog.
- Secciones 16 a 19 deben usar todos los principios para cerrar orden de spikes, matriz de trazabilidad, categorias hacia backlog y acceptance criteria sin aprobar implementacion.

##### 6. Explicit Non-Decisions

- Esta seccion no decide runtime layout, rutas fisicas, nombres de archivos, formatos finales, schemas fisicos, validators reales, command interfaces, prompts finales, permissions OpenCode, entorno Odoo 18 exacto, storage definitivo, secrets policy ejecutable ni orden final de spikes.
- Esta seccion no crea agentes ejecutables, commands reales, scripts, validators, schemas, RAG/base vectorial, backlog, PRD, SDD ni implementacion.
- Esta seccion no amplia la source policy ni autoriza fuentes fuera de la base minima aprobada.
- Esta seccion no reabre CRIT-01..07, TOM approved, piloto V1 confirmado, Odoo 18 target, SDK/server fuera de core V1 ni RAG/base vectorial fuera de V1.

##### 7. Open Questions / Owner Decisions

- none

##### 8. Acceptance Criteria

- La seccion queda en `Status: in-verification` para auditoria del verifier, sin owner approval.
- Cada principio queda trazable a TOM, decision aceptada, CRIT aprobado o riesgo de soporte.
- Los principios no contradicen decisiones aceptadas, rechazadas o superseded.
- La seccion guia secciones posteriores sin avanzar su contenido especifico ni crear layout/runtime fisico final.
- La seccion mantiene el Blueprint conceptual y respeta los non-goals globales: no runtime, no agents ejecutables, no commands reales, no schemas fisicos, no validators reales, no scripts, no RAG/base vectorial, no backlog, no PRD, no SDD y no implementacion.
- La seccion preserva la exclusion de `framework/` como input o referencia.

##### 9. Section Output

- Para la seccion 3, entrega principios de alcance V1/post-V1 y anti-scope-creep.
- Para la seccion 4, entrega principios para un runtime layout candidate conceptual sobre OpenCode y modelo hibrido.
- Para la seccion 5, entrega principios para separar fuente de verdad, estado autoritativo, runtime y evidencia.
- Para la seccion 6, entrega principios para derivar spikes desde incertidumbres fisicas y riesgos.
- Para secciones posteriores, entrega invariantes arquitectonicas de trazabilidad, source policy, gates/evidencia, seguridad/riesgo/compliance, no double work y no uso de `framework/`.

#### 3. V1 / Post-V1 Boundary

Status: closed

Owner approval: approved explicitly by owner.

Inputs esperados:

- Secciones 1 y 2 de la iteracion correspondiente.
- Decisiones aceptadas, rechazadas y superseded sobre scope V1 y post-V1.

Outputs esperados:

- Limite V1 / post-V1 para guiar secciones posteriores.

Restricciones especificas:

- No mover capacidades post-V1 a V1 sin decision owner explicita.

Acceptance criteria minimos:

- Cada limite queda trazable y no reabre decisiones aprobadas.

##### 1. Purpose

- Establecer el limite conceptual entre V1 core, capacidades V1 condicionales/spike y post-V1/deferred, para evitar scope creep y guiar secciones posteriores sin convertir esta seccion en backlog, PRD, SDD ni implementacion.
- Mantener V1 alineado con el TOM aprobado, CRIT-01..07, DEC-ACCEPTED-161, DEC-ACCEPTED-162, DEC-ACCEPTED-163 y DEC-ACCEPTED-164.

##### 2. Boundary Rules

- BR-01 — Una capacidad entra en V1 core solo si esta respaldada por TOM, CRIT aprobado o decision aceptada y es necesaria para el flujo minimo Odoo 18 end-to-end del piloto confirmado. Trazabilidad: RULE-04; TOM `Alcance Operativo V1`; CRIT-01; DEC-ACCEPTED-153/156/162.
- BR-02 — Una capacidad queda V1 conditional/spike cuando esta permitida como incertidumbre o candidato conceptual, pero requiere validacion posterior antes de convertirse en diseno operativo. Trazabilidad: TOM open items for Blueprint/spikes; CRIT-02/03/07; DEC-ACCEPTED-138.
- BR-03 — Una capacidad queda post-V1/deferred cuando las decisiones aceptadas, rechazadas, TOM o riesgos la excluyen del core V1 o la marcan como expansion posterior. Trazabilidad: DEC-ACCEPTED-148/149/151/152/157/164; DEC-REJECTED-016/034/035/038; RISK-008/058/065/066.
- BR-04 — Ningun limite en esta seccion reabre CRIT-01..07, TOM aprobado, seleccion del piloto, target Odoo 18, source policy minima, exclusion de `framework/`, SDK/server fuera de core V1 ni RAG/base vectorial fuera de V1. Trazabilidad: DEC-ACCEPTED-133/134/135/161/162/163/164; DEC-ACCEPTED-148; RISK-064.

##### 3. V1 Core Boundary

| Area | V1 core boundary | Traceability |
| --- | --- | --- |
| Operating model | CAFL V1 opera como framework/plataforma sobre OpenCode con modelo hibrido progresivo; no es agents-only y OpenCode no es por si solo estado autoritativo, decision de gate ni evidencia suficiente. | DEC-ACCEPTED-013/028/136; TOM mechanism constraints; S02 context |
| Product/technical target | V1 es Odoo-only y apunta a Odoo 18. | DEC-ACCEPTED-135; TOM `Alcance Operativo V1`; CRIT-01/07 |
| Pilot scope | La instancia de piloto que acota V1 es solicitudes internas / aprobaciones simples; esta seccion no lo convierte en PRD, SDD ni backlog final. | DEC-ACCEPTED-162; TOM pilot instance; S01 non-goals |
| End-to-end evidence | V1 debe poder demostrar un ciclo minimo real Odoo 18 end-to-end con evidencia verificable; la definicion operativa queda para secciones posteriores. | DEC-ACCEPTED-153/156; CRIT-01; RISK-010/057/059 |
| Minimum control automation | V1 incluye control minimo conceptual sobre estructura, trazabilidad, evidencia, source policy/Knowledge Gap basics, rework/debt/approval cuando aplique y ejecucion Odoo minima; no define aqui commands, validators ni scripts reales. | DEC-ACCEPTED-140/145; CRIT-04/05/06; S01/S02 restrictions |
| Knowledge/source governance | V1 usa source policy minima pre-autorizada: documentacion oficial Odoo y GitHub oficial `odoo/odoo`; otras fuentes requieren Curation Request y aprobacion. No hay free web search ni RAG/base vectorial V1. | DEC-ACCEPTED-163; TOM Knowledge Governance; RISK-062 |
| Source of truth and traceability | `project-truth/` permanece como autoridad; todo componente posterior debe mantener trazabilidad bidireccional conceptual hacia TOM/CRIT/decisiones. | S01/S02 context; RULE-04/05; CRIT-04/05 |
| Evidence/storage posture | La orientacion de V1 es simple, auditable y compatible con Git para estado/logs/evidencia conceptual, sin cerrar almacenamiento fisico definitivo en esta seccion. | S02 context; TOM mechanism constraints; CRIT-04/05/06 |

##### 4. V1 Conditional / Spike Boundary

| Area | Conditional boundary | Traceability |
| --- | --- | --- |
| Runtime layout and mechanism split | OpenCode + commands + scripts/CLI/validators + almacenamiento simple auditable es direccion candidata, no arquitectura definitiva; su detalle pertenece a secciones posteriores y/o spikes. | DEC-ACCEPTED-138; TOM open items; CRIT-07 |
| Odoo 18 execution environment | La forma exacta de entorno Odoo 18 queda como incertidumbre de Blueprint/spike; no se fija infraestructura ni deployment final aqui. | TOM open items; CRIT-01; RISK-010/057/059 |
| UI/OWL/Playwright | UI, OWL o Playwright solo pueden considerarse si el piloto lo justifica y una decision posterior lo mantiene dentro de V1; por defecto no son V1 core. | TOM pilot instance; S02 context; RISK-008/065/066 |
| Permissions, commands, skills and secrets | Permisos, commands/skills y politica ejecutable de secretos requieren diseno posterior; esta seccion solo marca que no deben contradecir source policy, gates ni evidencia. | TOM open items; S02 context; CRIT-02/03/04 |
| Knowledge Governance without RAG | La implementacion minima de source registry, knowledge artifacts, Knowledge Gap y Curation Request se define despues sin introducir RAG/base vectorial. | TOM Knowledge Governance; DEC-ACCEPTED-163; DEC-ACCEPTED-148 |

##### 5. Post-V1 / Deferred Boundary

| Capability | Boundary decision | Traceability |
| --- | --- | --- |
| RAG / base vectorial | Deferred to V2/post-V1; not approved for V1 unless a future explicit owner decision changes the scope. | DEC-ACCEPTED-148; DEC-REJECTED-016/034; RISK-028/048/053 |
| SDK/server as core | Outside V1 core by default; later inclusion requires favorable spike and explicit owner decision. | DEC-ACCEPTED-149/164; DEC-REJECTED-035; TOM mechanism constraints |
| Broad automated documentation ingestion | Not default V1 scope; keep knowledge governance incremental. | DEC-ACCEPTED-151; TOM Knowledge Governance; RISK-058 |
| Real external integrations | Not default V1 scope for the pilot. | DEC-ACCEPTED-152; DEC-REJECTED-038; TOM pilot instance |
| Dashboard/UI productization | Deferred unless narrowly justified by the pilot; not V1 core. | TOM pilot instance; S02 context; RISK-058 |
| CI/CD completo | Deferred beyond the minimal V1 evidence/execution needs. | S02 context; RISK-058 |
| Advanced DB/storage | Deferred; V1 favors simple auditable storage until later sections decide conceptual posture and spikes. | S02 context; CRIT-04/05/06; RISK-058 |
| Multiuser/team operations | Deferred beyond internal pilot/minimum owner-controlled flow unless future decision expands scope. | S02 context; RISK-008/065/066 |
| Plugins/MCP | Deferred; not part of default V1 core. | S02 context; RISK-058 |
| Advanced curation | Deferred beyond the minimum source policy, Knowledge Gap and Curation Request baseline. | TOM Knowledge Governance; DEC-ACCEPTED-163; RISK-028/048/053 |
| Broad post-V1 capabilities | Deferred to V2/post-V1, not rejected. | DEC-ACCEPTED-157; S02 context |

##### 6. Anti-Scope-Creep Controls

- Any proposed V1 capability without TOM, CRIT or accepted-decision support must be eliminated, marked post-V1/deferred, or registered as owner decision required; it must not be silently accepted.
- Any attempt to expand source policy, add RAG/vector base, move SDK/server into core, broaden the pilot, add real external integrations by default, or reintroduce `framework/` is outside this section's authority and requires explicit owner decision.
- Conditional/spike classification is not approval to implement; it only preserves an uncertainty for later conceptual Blueprint sections.

##### 7. Open Questions / Owner Decisions

- none

##### 8. Acceptance Criteria

- La seccion queda en `Status: in-verification` para auditoria del verifier, sin owner approval.
- Cada limite V1 core, V1 conditional/spike y post-V1/deferred queda trazado a TOM, CRIT aprobado, decision aceptada/rechazada o riesgo de soporte incluido en el context packet.
- La seccion no reabre decisiones aprobadas ni mueve capacidades post-V1 a V1 core sin decision owner explicita.
- La seccion se mantiene conceptual y no crea runtime, agents ejecutables, commands reales, schemas fisicos, validators reales, scripts, RAG/base vectorial, backlog, PRD, SDD ni implementacion.
- La seccion no usa ni referencia `framework/` como input y mantiene su exclusion.

##### 9. Section Output / Handoff

- Para secciones posteriores, S03 entrega el limite conceptual que separa V1 core, V1 conditional/spike y post-V1/deferred; cualquier detalle operativo posterior debe permanecer dentro de estos limites o registrar owner decision required.

#### 4. Runtime Layout Candidate

Status: closed

Owner approval: approved explicitly by owner.

Inputs esperados:

- Secciones 1, 2 y 3 de la iteracion correspondiente.
- Handoff del TOM al Blueprint y decisiones CRIT-07 aplicables.

Outputs esperados:

- Candidato conceptual de layout para alimentar secciones de estructura, mecanismos y storage.

Restricciones especificas:

- No crear runtime, rutas fisicas finales ni archivos ejecutables.
- No usar ni reintroducir material legacy descartado como input o referencia.
- No convertir categorias conceptuales en directorios, archivos, comandos, schemas, validators, scripts, agentes ejecutables, MCP/plugins, RAG/base vectorial, backlog, PRD, SDD ni implementacion.

Acceptance criteria minimos:

- El candidato queda conceptual, trazable y sin implementacion.

##### 1. Proposito y alcance

S04 propone un candidato conceptual de layout runtime para CAFL V1. El candidato organiza responsabilidades y separaciones logicas que las secciones posteriores deben refinar, sin aprobar una estructura fisica ni autorizar artefactos ejecutables.

El layout se mantiene dentro de los limites aprobados por S01-S03: V1 es Odoo-only/Odoo 18, usa OpenCode como runtime primario en un modelo hibrido progresivo, conserva `project-truth/` como fuente de verdad, limita el piloto a internal requests / simple approvals y difiere RAG/vector, SDK/server core, UI/dashboard productizado, CI/CD amplio, integraciones amplias y storage avanzado salvo decision owner futura.

##### 2. Principios de layout conceptual

- **Separacion source-vs-runtime:** la autoridad conceptual permanece en la fuente de verdad; el runtime solo ejecuta, coordina o produce evidencia. Trazas: TOM 48-55, TOM 79-93, S01/S02 summaries, RISK-006.
- **OpenCode como runtime, no como autoridad:** OpenCode puede orquestar interacciones de trabajo, pero no sustituye estado, gates, storage, source policy ni evidencia verificable. Trazas: TOM 63-72, TOM 79-93, DEC-ACCEPTED-136, RISK-020.
- **Control hibrido progresivo:** agentes pueden razonar; comandos candidatos estandarizan entradas repetibles; scripts/CLI/validators candidatos cubren controles deterministicos; reglas/config sostienen invariantes; skills/playbooks apoyan conocimiento bajo demanda. Trazas: TOM 63-72, CRIT-07, DEC-ACCEPTED-138, RISK-022/023/024.
- **Evidencia auditable minima:** logs, estado y evidencia deben permanecer separables de prompts y conversaciones para soportar verificacion reproducible. Trazas: TOM 48-55, TOM 351-366, RISK-010.
- **Fuente y Knowledge Gap minimos:** la politica base de fuentes se limita a documentacion oficial de Odoo y `github.com/odoo/odoo`; cualquier otra fuente requiere curation/owner approval posterior. Trazas: DEC-ACCEPTED-163, S01/S03 summaries.
- **Spike-dependencia visible:** aspectos aun inciertos se preservan como placeholders conceptuales para validacion tecnica posterior; no implican permiso de implementacion. Trazas: TOM 368-383, RISK-059/061/063.

##### 3. Zonas conceptuales candidatas

Las siguientes zonas son categorias logicas no finales. No son rutas, paquetes, carpetas ni archivos aprobados.

| Zona conceptual | Responsabilidad V1 candidata | Excluye explicitamente | Trazabilidad |
| --- | --- | --- | --- |
| Fuente de verdad y decision record | Mantener autoridad humana y documental aprobada; alimentar trazabilidad hacia runtime y evidencia. | Estado operacional exclusivo en OpenCode; fuentes paralelas; cambios de decisiones sin owner approval. | TOM 48-55; S01; S02 AP-01/AP-02; RISK-006; DEC-ACCEPTED-161. |
| Coordinacion OpenCode | Servir como runtime primario para trabajo asistido, handoffs y uso de mecanismos candidatos. | Ser gate final, storage final, policy engine final o evidencia suficiente por si solo. | TOM 63-72, 79-93; DEC-ACCEPTED-136; RISK-020. |
| Entradas repetibles / comandos candidatos | Definir, a nivel conceptual, puntos de entrada repetibles para tareas recurrentes del flujo CAFL. | Comandos reales, nombres ejecutables, permisos finales o configuracion OpenCode final. | TOM 63-72; CRIT-07; DEC-ACCEPTED-138; RISK-022/023/024. |
| Control deterministico candidato | Reservar espacio conceptual para scripts/CLI/validators que validen estructura, DoR, trazabilidad, logs/state/evidence y evidencia Odoo cuando sean aprobados. | Implementar scripts, validators reales, schemas fisicos o toolchain final. | TOM 48-55, 351-366; CRIT-07; DEC-ACCEPTED-138; RISK-010. |
| Estado, logs y evidencia auditable | Separar lo producido por ejecuciones, controles y pruebas para que pueda auditarse y reproducirse. | Storage avanzado, DB compleja, dashboard/UI productizado o evidencia basada solo en chat/prompt. | TOM 48-55, 351-366; S02 AP-06/AP-09; RISK-010. |
| Politica de fuentes y Knowledge Gap | Registrar distincion conceptual entre fuentes autorizadas, brechas de conocimiento y solicitudes de curacion. | RAG/vector base, ingestion amplia, fuentes no autorizadas por defecto o knowledge governance avanzado. | DEC-ACCEPTED-163; DEC-ACCEPTED-148; TOM 368-383; RISK-048/058/065. |
| Integracion Odoo 18 / piloto | Reservar el area conceptual que recibira evidencia de ejecucion Odoo 18 para internal requests / simple approvals. | Cambiar el piloto, crear PRD/SDD/backlog, ejecutar entorno Odoo o ampliar integraciones. | TOM 48-55, 351-366; DEC-ACCEPTED-135; DEC-ACCEPTED-162; RISK-059. |
| Seguridad, permisos y secretos | Mantener los limites conceptuales de permisos OpenCode y tratamiento de secretos para validacion posterior. | Reglas de permisos finales, secrets reales, vault/configuracion o implementacion de seguridad. | TOM 351-366, 368-383; RISK-061; RISK-063. |
| Spikes y validaciones tecnicas | Conservar incertidumbres que S06/S16 ordenaran y validaran antes de convertirlas en diseno operacional. | Ejecutar spikes o cerrar incertidumbres tecnicas dentro de S04. | TOM 368-383; RISK-018/025/032; RISK-059/061/063. |

##### 4. Relaciones entre zonas

- La fuente de verdad alimenta coordinacion OpenCode, entradas repetibles, controles deterministicos candidatos, politica de fuentes y criterios de evidencia; ninguna zona runtime puede sobrescribirla.
- La coordinacion OpenCode puede invocar o guiar mecanismos candidatos, pero los resultados que importan para gates deben quedar respaldados por evidencia auditable y trazable.
- Los controles deterministicos candidatos deben operar sobre estructuras y evidencias aprobadas en secciones posteriores; S04 solo reserva la separacion conceptual.
- La zona Odoo 18 / piloto recibe necesidades del piloto fijo y devuelve evidencia de ejecucion; no define alcance funcional nuevo.
- Seguridad, permisos y secretos cruzan OpenCode, controles candidatos y Odoo 18, pero permanecen pendientes de diseno y spikes posteriores.
- Spikes y validaciones tecnicas gobiernan incertidumbres, no implementan runtime ni convierten placeholders en artefactos aprobados.

##### 5. Handoff a secciones posteriores

- **S05 Source-vs-Runtime Structure:** debe convertir estas zonas conceptuales en separacion source-vs-runtime sin aprobar estructura fisica final.
- **S06 / S16 Spikes:** deben ordenar validaciones para lenguaje/toolchain de scripts/CLI, entorno Odoo 18, permisos OpenCode, schemas/validators, storage/log convention, source policy/Knowledge Gap, evidence capture y secrets.
- **S07 / S08 Operating Design y Mechanism Split:** deben mapear agentes, comandos candidatos, scripts/CLI/validators candidatos, reglas/config y skills/playbooks sin crear artefactos ejecutables.
- **S09 / S10 / S11 / S12:** deben mantener schemas, validators, evidence/storage y source policy como minimos conceptuales hasta que exista decision de implementacion.
- **S13 / S14 / S15:** deben conservar Odoo 18, seguridad/secrets y piloto interno simple dentro de los limites V1 aprobados.

##### 6. Fuera de alcance y deferred/post-V1

- RAG/base vectorial, broad ingestion, SDK/server core, MCP/plugins, UI/dashboard productizado, CI/CD amplio, storage avanzado, integraciones amplias, multiuser/team avanzado y curation/knowledge governance avanzado permanecen post-V1 o requieren decision owner futura.
- Cualquier componente sin trazabilidad al context packet debe eliminarse, marcarse post-V1/deferred o registrarse como owner-decision required antes de avanzar.

##### 7. Open Questions / Owner Decisions

- none

##### 8. Acceptance Criteria

- La seccion queda en `Status: in-verification` para auditoria del verifier, sin owner approval.
- Todas las zonas propuestas son conceptuales, no finales, no fisicas y trazadas a anchors del context packet.
- El layout separa autoridad/source, runtime OpenCode, mecanismos candidatos, control deterministico candidato, evidencia/storage/logs, politica de fuentes, Odoo 18/piloto, seguridad/secrets y spikes.
- OpenCode no queda definido como estado autoritativo, gate final, storage final, politica final ni evidencia suficiente por si solo.
- No se crean runtime, rutas fisicas finales, archivos ejecutables, agentes ejecutables, comandos reales, schemas fisicos, validators reales, scripts, RAG/base vectorial, SDK/server, backlog, PRD, SDD ni implementacion.

##### 9. Section Output / Handoff

- S04 entrega un layout conceptual candidato para que S05 refine la separacion source-vs-runtime y para que S06+ identifiquen mecanismos, storage/evidence, OpenCode design, Odoo 18, seguridad/secrets y spikes sin convertir categorias en implementacion.

#### 5. Source-vs-Runtime Structure

Status: closed

Owner approval: approved explicitly by owner.

##### 1. Proposito y alcance

- Definir la separacion conceptual entre source autoritativo y runtime de asistencia para CAFL V1, usando el layout candidato de S04 sin convertirlo en estructura fisica.
- Mantener `project-truth/` como fuente de verdad unica para autoridad, decisiones, estado aprobado y trazabilidad; ningun resultado runtime puede reemplazarlo ni duplicarlo.
- Alimentar S06+ con limites claros para spikes, mecanismos, evidencia/storage, OpenCode, Odoo 18, seguridad/secrets y source policy sin crear artefactos ejecutables.

##### 2. Entradas trazables

| Entrada | Uso en S05 | Trazabilidad |
| --- | --- | --- |
| S04 Runtime Layout Candidate | Convertir zonas candidatas en responsabilidades source-vs-runtime conceptuales. | S04 handoff; TOM 351-366; CRIT-06/CRIT-07. |
| Reglas de autoridad `project-truth/` | Proteger fuente de verdad, decision record, estado operativo aprobado y trazabilidad. | DEC-ACCEPTED-001; S01; S02 AP-01/AP-02/AP-06. |
| Modelo OpenCode V1 | Ubicar OpenCode como asistencia de coordinacion/runtime, no como autoridad. | DEC-ACCEPTED-028/136; TOM 79-93; S02 AP-03/AP-04. |
| Politica minima de fuentes | Separar fuentes autorizadas, Knowledge Gap y solicitudes de curacion de outputs runtime. | DEC-ACCEPTED-163; TOM 206-246; S03. |
| Limites V1 y piloto | Restringir la separacion a Odoo 18, OpenCode y piloto internal requests / simple approvals. | DEC-ACCEPTED-135/162/164; TOM 48-55; S03. |

##### 3. Separacion source-vs-runtime

| Categoria conceptual | Lado source / autoridad | Lado runtime / asistencia | Regla de separacion | Trazabilidad |
| --- | --- | --- | --- | --- |
| Fuente de verdad y decisiones | `project-truth/` conserva decisiones aceptadas, pendientes, riesgos, TOM, blueprint/state aprobados y trazabilidad oficial. | OpenCode, comandos candidatos o sesiones pueden ayudar a leer, resumir o preparar cambios. | Todo cambio de autoridad requiere registro trazable en `project-truth/`; resumentes o chats no son autoridad. | DEC-ACCEPTED-001; RISK-011; S01/S02. |
| Estado operativo y gates | El estado aprobado, owner approval y cierre de gates viven solo en el estado/working contract gobernado. | Runtime puede producir reportes, logs o handoffs para revision. | Ningun agente, reporte o output runtime aprueba, cierra ni cambia semanticas de estado por si mismo. | TOM 79-93; approval rules; RISK-006. |
| Coordinacion OpenCode | Las reglas aprobadas definen que puede coordinarse y que requiere decision. | OpenCode coordina tareas, contexto y asistencia de razonamiento. | OpenCode es soporte primario de runtime, no final storage, policy, gate, evidence suficiente ni source of truth. | DEC-ACCEPTED-028/136; S02 AP-03/AP-04. |
| Inputs repetibles y comandos candidatos | La autoridad define criterios, alcance y trazabilidad esperada. | Prompts/commands candidatos pueden estructurar ejecuciones futuras. | S05 no aprueba comandos reales, agentes ejecutables, permission rules ni configuracion OpenCode. | DEC-ACCEPTED-138; TOM 351-366; S04. |
| Control deterministico candidato | La autoridad define necesidad de DoR, trazabilidad, estructura, logs/evidencia y fuente minima. | Scripts/CLI/validators candidatos podrian comprobar reglas en fases posteriores. | Los validadores siguen siendo direccion conceptual; no se crean schemas, scripts ni validadores reales. | DEC-ACCEPTED-145; TOM 48-55/79-93; RISK-022/023/024. |
| Evidencia candidata, logs y reportes | La evidencia solo se vuelve relevante para autoridad cuando queda trazada y registrada bajo gobierno aprobado. | Ejecuciones, reportes de agente, logs, outputs de comandos o evidencia Odoo pueden proponer evidencia. | La evidencia runtime es candidata hasta su registro trazable; chat/prompt por si solo no basta. | TOM 48-55/351-366; S02 AP-06/AP-09; RISK-006. |
| Source policy y Knowledge Gap | Fuentes base autorizadas: documentacion oficial Odoo y GitHub oficial `odoo/odoo`; excepciones requieren curacion/owner approval. | Runtime puede detectar brechas, preparar Curation Requests o citar fuentes autorizadas. | No hay free web, RAG/vector ni expansion de fuentes por default en V1. | DEC-ACCEPTED-163; TOM 206-246; RISK-043/052/054/062. |
| Odoo 18 y piloto | El alcance aprobado fija Odoo 18 e internal requests / simple approvals. | Runtime puede asistir pruebas, preparacion de evidencia y observaciones del piloto. | La separacion no crea PRD, SDD, backlog, entorno Odoo ni implementacion; no cambia el piloto. | DEC-ACCEPTED-135/162; TOM 48-55; S03/S04. |
| Seguridad, permisos y secretos | Las restricciones aprobadas definen que secretos/permisos requieren validacion posterior. | Runtime puede identificar necesidades y riesgos de permisos/secrets. | No se definen reglas finales de permisos, vault, secretos reales ni configuracion. | TOM 351-366; S04; RISK-061/063. |
| Spikes e incertidumbres | Los riesgos y decisiones aprobadas determinan que incertidumbres requieren validacion. | Runtime puede preparar propuestas de spike para S06/S16. | S05 no ejecuta spikes ni cierra incertidumbres tecnicas. | TOM 368-383; S04; RISK-020/025. |

##### 4. Reglas de flujo entre source y runtime

- **Source a runtime:** el source autorizado entrega alcance, decisiones, restricciones, criterios de evidencia, fuente minima y estado permitido; runtime solo opera dentro de esos limites.
- **Runtime a source:** los outputs runtime regresan como candidatos: evidencia candidata, hallazgos, logs, reportes, propuestas de cambios, Curation Requests o owner-decision blockers.
- **Registro autoritativo:** un output runtime solo impacta autoridad cuando una seccion, decision, riesgo, estado o reporte permitido lo incorpora con trazabilidad y aprobacion aplicable.
- **Conflictos:** si un output runtime contradice `project-truth/`, prevalece `project-truth/` hasta decision owner; el conflicto se registra, no se resuelve por juicio del agente.
- **Minimalidad:** la separacion usa categorias conceptuales, no rutas finales, arboles de carpetas, schemas, validators, scripts, comandos ni configuracion.

##### 5. Controles anti-duplicacion

- No crear un segundo registro de decisiones, estado, owner approval, gates, risks o source policy fuera de `project-truth/`.
- Los reportes de autor/verifier, logs y outputs de comandos son evidencia o trazas auxiliares; no son fuente de verdad paralela.
- La asistencia OpenCode no puede declarar una seccion aprobada, cerrar una iteracion, cambiar owner approval ni redefinir politicas.
- Si una categoria runtime necesita autoridad nueva, debe quedar como owner-decision required o deferred/post-V1, no como regla implicita de S05.

##### 6. Fuera de alcance y deferred/post-V1

- RAG/base vectorial, SDK/server core, advanced DB/storage, dashboard/UI productizado, CI/CD amplio, MCP/plugins, broad ingestion, broad integrations, multiuser/team avanzado y advanced curation permanecen fuera de V1 core o requieren decision owner futura.
- S05 no crea runtime, estructura fisica final, rutas, archivos, agentes ejecutables, commands reales, schemas, validators, scripts, PRD, SDD, backlog, Odoo environment, secretos ni implementacion.
- `framework/` no se usa ni se recrea como entrada, ejemplo o fuente de migracion.

##### 7. Handoff a secciones posteriores

- **S06 / S16:** ordenar spikes para validar incertidumbres sin ejecutar implementacion.
- **S07 / S08:** mapear mecanismos OpenCode, agentes, comandos candidatos, scripts/CLI/validators candidatos y reglas/playbooks manteniendo la separacion autoridad-runtime.
- **S09 / S10 / S11:** definir schemas, validators y state/log/evidence storage minimos como conceptos trazables antes de cualquier implementacion.
- **S12:** concretar source policy / Knowledge Gap sin RAG/vector ni fuentes libres por default.
- **S13 / S14 / S15:** mantener Odoo 18, seguridad/secrets y piloto interno simple dentro del alcance V1 aprobado.

##### 8. Open Questions / Owner Decisions

- none

##### 9. Acceptance Criteria

- La seccion queda en `Status: in-verification` para auditoria del verifier, sin owner approval.
- La separacion source-vs-runtime es conceptual, trazable y no crea estructura fisica runtime.
- Autoridad, decisiones, estado, owner approval, gates y source policy permanecen en `project-truth/` y no se duplican.
- Runtime assistance, mecanismos candidatos, evidencia candidata, logs y reportes quedan subordinados a registro trazable y aprobacion aplicable.
- OpenCode no queda definido como estado autoritativo, gate final, storage final, politica final ni evidencia suficiente por si solo.
- No se introducen runtime, rutas fisicas finales, agentes ejecutables, commands reales, schemas fisicos, validators reales, scripts, RAG/base vectorial, SDK/server, backlog, PRD, SDD, Odoo environment, secretos ni implementacion.

#### 6. Initial Spike Map

##### 1. Status

Status: closed

Owner approval: approved explicitly by owner.

##### 2. Purpose

Esta seccion define el mapa inicial de spikes tecnicos de CAFL V1 para que S16 pueda convertirlo en orden final de validaciones. El mapa no ejecuta spikes, no cierra incertidumbres fisicas y no autoriza implementacion; solo organiza dependencias, criterios de precedencia y trazabilidad minima hacia TOM, riesgos aceptados y decisiones aceptadas.

El objetivo es evitar que las incertidumbres registradas por S01-S05 se conviertan en diseno operacional prematuro. Cada spike queda ubicado dentro de una cadena de dependencia: primero se protegen alcance, seguridad y source policy; luego se validan capacidades del runtime OpenCode y el ciclo Odoo 18; despues se ordenan toolchains de control/evidencia; finalmente se dejan como condicionales las capacidades fuera del core V1.

##### 3. Scope / Inputs

Entradas usadas para este mapa:

- S01-S05 aprobadas: scope V1 Odoo-only sobre Odoo 18, OpenCode como runtime primario, piloto interno de solicitudes/aprobaciones simples, `project-truth/` como autoridad, `framework/` excluido y post-V1 diferido.
- TOM technical validations/spikes TOM-S01..TOM-S14.
- Riesgos aceptados vinculados a OpenCode, Odoo 18, source policy, evidencia, seguridad/secrets, testing minimo, token budget y anti-scope-creep.
- Decisiones aceptadas DEC-ACCEPTED-049/050, 135, 142/143, 149/164, 153 y 158.

Fuera de alcance:

- Ejecutar spikes, registrar resultados tecnicos o cerrar incertidumbres.
- Crear runtime, agents ejecutables, commands reales, schemas fisicos, validators reales, scripts, RAG/base vectorial, backlog, PRD, SDD o implementacion.
- Reabrir OpenCode como runtime primario, Odoo 18 como target V1, piloto confirmado, source policy minima o limites V1/post-V1.
- Usar `framework/` como input o referencia.

##### 4. Initial Spike Map

El mapa se organiza por bandas de dependencia. Las bandas expresan precedencia conceptual para S16; no son fases de ejecucion aprobada. Un spike posterior no debe cerrarse antes de que sus precondiciones hayan sido validadas o registradas como excepcion/owner decision.

| Banda | Razon de precedencia | Spikes incluidos | Dependencias hacia bandas posteriores |
| --- | --- | --- | --- |
| A. Guardrails de alcance, fuentes y seguridad | Evita validar capacidades sobre supuestos prohibidos o inseguros. | SP-01, SP-02, SP-03 | Condiciona OpenCode, evidence, Odoo y toolchains. |
| B. Capacidades base de OpenCode y Odoo 18 | Valida los dos ejes operativos de V1 antes de seleccionar mecanismos de control. | SP-04, SP-05, SP-06 | Alimenta schemas/validators, comandos/skills candidatos y ciclo evidenciable. |
| C. Toolchain conceptual de control y evidencia | Solo tiene sentido despues de saber que fuente, runtime y Odoo minimo son viables. | SP-07, SP-08, SP-09, SP-10 | Alimenta diseno operativo posterior y criterios de verificabilidad. |
| D. Condicionales anti-scope-creep | No bloquean el core V1 salvo decision futura; se mantienen separados para no contaminar el orden base. | SP-11, SP-12, SP-13 | Solo S16 puede ubicarlos como condicionales con decision owner si aplica. |

###### Banda A — Guardrails de alcance, fuentes y seguridad

| ID | Spike conceptual | Dependencias / orden | TOM anchors | Riesgos | Decisiones aceptadas |
| --- | --- | --- | --- | --- | --- |
| SP-01 | Validar enforcement minimo de source policy y Knowledge Gap sin RAG/vector: como detectar fuente faltante, version oficial o gap antes de usar informacion tecnica. | Primero: si la fuente no es gobernable, los demas spikes pueden producir conclusiones no trazables. | TOM-S08, TOM-S09 | RISK-006, RISK-043, RISK-044, RISK-045, RISK-050, RISK-058 | DEC-ACCEPTED-158; limites de source policy aprobados por S01-S05. |
| SP-02 | Validar postura minima de secrets: como impedir que tokens, credenciales y secretos Odoo entren en repo, logs o evidencia. | Antes de OpenCode/Odoo/evidence porque esos spikes pueden tocar credenciales o logs. | TOM-S12 | RISK-063 | DEC-ACCEPTED-158; guardrails S01-S05 sobre seguridad/secrets. |
| SP-03 | Validar frontera V1/post-V1 para capacidades condicionales antes de considerarlas en cualquier spike operacional. | Depende de SP-01 y SP-02; bloquea que SDK/server, OpenAPI/PDF, UI/OWL o Playwright entren como V1 por arrastre tecnico. | TOM-S05, TOM-S13, TOM-S14 | RISK-058, RISK-065, RISK-047 | DEC-ACCEPTED-149, DEC-ACCEPTED-164, DEC-ACCEPTED-158. |

###### Banda B — Capacidades base de OpenCode y Odoo 18

| ID | Spike conceptual | Dependencias / orden | TOM anchors | Riesgos | Decisiones aceptadas |
| --- | --- | --- | --- | --- | --- |
| SP-04 | Validar capacidades y limites de permisos OpenCode requeridos para operar V1 sin convertir OpenCode en autoridad, gate final o evidencia suficiente por si solo. | Depende de SP-01/SP-02; precede commands/skills y token-routing porque permisos condicionan que mecanismos pueden existir. | TOM-S03 | RISK-020, RISK-025, RISK-061, RISK-018, RISK-032 | DEC-ACCEPTED-049, DEC-ACCEPTED-050, DEC-ACCEPTED-158. |
| SP-05 | Validar diseno candidato de commands/skills OpenCode sin crearlos ni ejecutarlos: entradas, salidas y limites conceptuales. | Depende de SP-04; precede split agents/commands/scripts/validators de S08 y toolchain de control. | TOM-S04 | RISK-020, RISK-025, RISK-018 | DEC-ACCEPTED-049, DEC-ACCEPTED-050, DEC-ACCEPTED-158. |
| SP-06 | Validar forma minima del entorno Odoo 18 y ciclo install/update/test como incertidumbre tecnica, sin construir entorno. | Corre despues de secrets y source policy; precede evidencia end-to-end y cualquier seleccion de toolchain que dependa de Odoo. | TOM-S02, TOM-S10 | RISK-059, RISK-010, RISK-039 | DEC-ACCEPTED-135, DEC-ACCEPTED-153, DEC-ACCEPTED-158. |

###### Banda C — Toolchain conceptual de control y evidencia

| ID | Spike conceptual | Dependencias / orden | TOM anchors | Riesgos | Decisiones aceptadas |
| --- | --- | --- | --- | --- | --- |
| SP-07 | Validar criterios de lenguaje/toolchain para scripts/CLI candidatos, comparando facilidad local, JSON/YAML/JSONL, integracion Odoo, velocidad, mantenibilidad y friccion con OpenCode. | Depende de SP-04, SP-05 y SP-06; no selecciona lenguaje final antes de conocer runtime/permisos/Odoo. | TOM-S01 | RISK-060, RISK-020 | DEC-ACCEPTED-142, DEC-ACCEPTED-143, DEC-ACCEPTED-158. |
| SP-08 | Validar toolchain conceptual para schemas/validators sin crear schemas fisicos ni validators reales. | Depende de SP-07 y de las necesidades de evidencia/control derivadas de SP-04..SP-06. | TOM-S06 | RISK-010, RISK-006 | DEC-ACCEPTED-158; trazabilidad S01-S05. |
| SP-09 | Validar convencion simple, auditable y Git-compatible para storage/logs como criterio conceptual, separada de chat/prompts. | Depende de SP-01 y se coordina con SP-08; precede evidencia final porque define donde podria registrarse control verificable. | TOM-S07 | RISK-006, RISK-010 | DEC-ACCEPTED-158; S04/S05 source-vs-runtime. |
| SP-10 | Validar captura de evidencia reproducible y separable de prompts/chat para ciclo Odoo 18 minimo. | Depende de SP-06, SP-08 y SP-09; no puede cerrarse antes de conocer Odoo minimo y convencion de control/evidencia. | TOM-S10, TOM-S11 | RISK-010, RISK-039, RISK-006 | DEC-ACCEPTED-153, DEC-ACCEPTED-158. |

###### Banda D — Condicionales anti-scope-creep

| ID | Spike conceptual | Dependencias / orden | TOM anchors | Riesgos | Decisiones aceptadas |
| --- | --- | --- | --- | --- | --- |
| SP-11 | Evaluar SDK/server solo como capacidad no core V1 y solo si una decision owner futura lo solicita tras spike favorable. | Depende de SP-03; no bloquea core V1 ni se mezcla con OpenCode baseline. | TOM-S05 | RISK-058, RISK-065 | DEC-ACCEPTED-149, DEC-ACCEPTED-164, DEC-ACCEPTED-158. |
| SP-12 | Evaluar OpenAPI/PDF processing solo si una decision futura de alcance lo requiere. | Depende de SP-01/SP-03 para evitar fuente no oficial o interpretacion no trazable. | TOM-S13 | RISK-047, RISK-065, RISK-043 | DEC-ACCEPTED-158; limites V1/post-V1 de S01-S05. |
| SP-13 | Evaluar Frontend/OWL/Playwright solo si aparece requisito piloto aprobado que lo justifique. | Depende de SP-03 y de decision owner/piloto; no forma parte del core V1 por defecto. | TOM-S14 | RISK-065 | DEC-ACCEPTED-158; piloto V1 confirmado por S01-S05. |

##### 5. Ordering Rationale

- **A antes de B:** source policy, Knowledge Gap y secrets son precondiciones de seguridad/trazabilidad. Sin ellas, un resultado de OpenCode, Odoo o evidencia puede ser no reproducible, no versionado o inseguro.
- **B antes de C:** permisos y commands/skills candidatos de OpenCode, junto con la viabilidad del entorno Odoo 18, determinan que toolchain de scripts/CLI, schemas/validators, storage/logs y evidencia puede ser razonable validar despues.
- **C antes de cierre de orden final:** S16 necesitara saber que validaciones de control/evidencia dependen de lenguaje, schemas, storage y ciclo Odoo minimo para ordenar ejecucion real sin convertir este mapa en implementacion.
- **D separada del core:** SDK/server, OpenAPI/PDF y UI/OWL/Playwright son condicionales o post-V1. Mantenerlos fuera de la ruta base preserva AP-08/anti-scope-creep y evita que una validacion opcional bloquee el core V1.

##### 6. Handoff to S16

S16 debe tomar este mapa como input inicial y producir el orden final de validaciones tecnicas. Para cada spike, S16 debera conservar o ajustar:

- precondiciones y dependencias entre bandas;
- trazabilidad TOM/riesgo/decision;
- condicion V1 core versus condicional/post-V1;
- criterios para registrar resultado posterior sin crear implementacion dentro del Blueprint;
- cualquier owner decision requerida para capacidades condicionales.

S16 no debe interpretar esta seccion como ejecucion, resultado favorable, seleccion de toolchain, aprobacion de runtime fisico ni autorizacion para crear artefactos ejecutables.

##### 7. Open Questions

- Ningun blocker owner nuevo se detecta en esta seccion.
- Las capacidades SP-11, SP-12 y SP-13 quedan explicitamente condicionadas a decision futura o requisito piloto aprobado; no bloquean la ruta base de V1.
- El detalle exacto de criterios de exito/fallo de cada spike queda para S16 o secciones operativas posteriores, sin ejecutarlos aqui.

##### 8. Acceptance Criteria

- Cada spike esta vinculado a al menos un TOM anchor y a riesgos/decisiones aceptadas o dependencia explicita.
- El mapa no es una lista plana: contiene bandas, precedencias y dependencias justificadas.
- Ningun spike se ejecuta ni se marca como cerrado.
- Ningun artefacto prohibido es creado o especificado como implementacion.
- Las capacidades post-V1 o condicionales quedan separadas de la ruta core V1 y sujetas a owner decision cuando aplique.
- `framework/` permanece excluido como input y referencia.

##### 9. Section Output

La salida de S06 es un mapa inicial de 13 spikes conceptuales ordenados por dependencias en cuatro bandas: guardrails, capacidades base OpenCode/Odoo 18, toolchain conceptual de control/evidencia y condicionales anti-scope-creep. Este mapa queda listo para verificacion y para alimentar S16 sin ejecutar validaciones ni cerrar incertidumbres tecnicas.

### Iteration 2 - Diseno operativo de mecanismos

#### 7. OpenCode Operating Design

##### 1. Status

Status: closed

Owner approval: approved

##### 2. Purpose

Esta seccion define el diseno operativo conceptual de OpenCode para CAFL V1. Su proposito es explicar como OpenCode funciona como runtime primario y hub de coordinacion dentro del modelo hibrido progresivo, sin convertirlo en fuente de verdad, gate final, storage final, policy engine final ni evidencia suficiente por si solo.

S07 traduce las zonas conceptuales de S04 y la separacion source-vs-runtime de S05 en reglas de operacion para alimentar S08. No crea configuracion OpenCode, agentes ejecutables, commands reales, skills, plugins, permission rules, MCP, scripts, validators, schemas, runtime ni implementacion.

##### 3. Inputs / Scope

Entradas trazables usadas:

- S01: scope V1 Odoo-only, target Odoo 18, piloto internal requests / simple approvals, source policy minima y non-goals globales.
- S02: AP-02, AP-03, AP-04 y AP-05 sobre OpenCode, modelo hibrido, separacion reasoning/control y avance por gates/evidencia.
- S03: BR-01 y BR-02 para mantener V1 core y condicional/spike dentro de limites aprobados.
- S04: zona conceptual `Coordinacion OpenCode` y relaciones entre fuente de verdad, mecanismos candidatos, evidencia/storage, Odoo 18, seguridad/secrets y spikes.
- S05: separacion source-vs-runtime: OpenCode como soporte primario de coordinacion/runtime, no como autoridad ni evidencia suficiente.
- S06: SP-04 y SP-05 como incertidumbres conceptuales sobre permisos OpenCode y commands/skills candidatos, sin validarlos ni crearlos aqui.
- Decisiones aceptadas aplicables: DEC-ACCEPTED-028, 058, 094, 107, 136 y 139 para OpenCode como runtime; DEC-ACCEPTED-056, 068, 069, 136, 137 y 140 para el modelo hibrido progresivo; DEC-ACCEPTED-162 y DEC-ACCEPTED-163 para piloto y source policy minima.

Alcance de S07:

- Definir que coordina OpenCode en V1 a nivel conceptual.
- Definir que OpenCode no puede decidir ni cerrar.
- Ubicar agentes, commands candidatos, scripts/CLI/validators candidatos, reglas/config y skills/playbooks dentro del modelo hibrido sin crear artefactos.
- Describir handoffs conceptuales entre OpenCode, fuente de verdad, control deterministico candidato, evidencia/storage, source policy y Odoo 18.
- Mantener el diseno dentro del core V1: Odoo-only, Odoo 18, piloto de solicitudes internas / aprobaciones simples.

##### 4. Operating Role of OpenCode

OpenCode opera como el entorno principal donde el trabajo asistido se prepara, coordina y encamina. En V1, su rol conceptual es:

| Responsabilidad conceptual | Como opera en OpenCode | Limite obligatorio | Trazabilidad |
| --- | --- | --- | --- |
| Coordinacion de tareas | Organiza handoffs, context packets, instrucciones de ejecucion y retorno de reportes entre roles conceptuales. | No aprueba, no cierra gates, no cambia owner approval y no reemplaza `project-truth/`. | AP-02, AP-05; S04 Coordinacion OpenCode; S05 source-vs-runtime. |
| Context routing | Encauza contexto autorizado, source policy minima, Knowledge Gap y restricciones de seccion hacia el mecanismo conceptual correcto. | No amplia fuentes; no usa busqueda libre ni fuentes fuera de politica sin curacion/owner approval. | AP-06; DEC-ACCEPTED-163; S05 source policy. |
| Invocacion o guia de mecanismos candidatos | Puede guiar agentes conceptuales, commands candidatos, playbooks o futuros controles deterministicos cuando las secciones posteriores los definan. | No crea commands reales, agents ejecutables, skills, scripts, validators, permission rules ni configuracion. | AP-03, AP-04; S06 SP-04/SP-05. |
| Preparacion de evidencia candidata | Puede ayudar a recopilar reportes, logs, observaciones y resultados candidatos para revision posterior. | Chat, prompt o salida OpenCode no son evidencia suficiente por si solos hasta registro gobernado. | AP-02, AP-05; S05 evidencia candidata. |
| Coordinacion con Odoo 18 piloto | Encauza trabajo y evidencia hacia el ciclo Odoo 18 del piloto confirmado. | No cambia piloto, no crea PRD/SDD/backlog, no construye entorno Odoo ni implementa modulo. | AP-07; DEC-ACCEPTED-162; S03 BR-01. |

##### 5. What OpenCode Must Not Decide

OpenCode no es autoridad de decision. En S07 quedan prohibidas las siguientes funciones para OpenCode o cualquier mecanismo coordinado por OpenCode:

- Aprobar secciones, cerrar iteraciones, declarar owner approval, cambiar status semantico o cerrar gates.
- Reemplazar `project-truth/` como fuente de verdad, decision record, source policy, registro de riesgos o estado aprobado.
- Resolver conflictos entre fuentes por criterio del agente; los conflictos deben registrarse como `open-question` o `needs-owner-decision` segun corresponda.
- Convertir outputs de chat, memoria de sesion, reportes o resultados de commands candidatos en evidencia suficiente sin registro trazable y revision aplicable.
- Expandir el scope V1, reabrir CRIT-01..07, cambiar el piloto, usar fuentes no aprobadas, introducir RAG/vector, SDK/server core, plugins/MCP, integraciones amplias o `framework/`.
- Crear o activar configuracion OpenCode, agents, commands, skills, plugins, permissions, scripts, validators, schemas, storage fisico, runtime o implementacion.

##### 6. Hybrid Mechanism Relationships

El operating design usa el modelo hibrido progresivo: OpenCode coordina mecanismos diferenciados, pero no los fusiona ni los convierte en autoridad. S08 debe refinar el split; S07 solo fija relaciones conceptuales.

| Mecanismo conceptual | Relacion con OpenCode | Responsabilidad V1 candidata | No decide / no crea | Trazabilidad |
| --- | --- | --- | --- | --- |
| Agentes conceptuales | OpenCode puede enrutar instrucciones, contexto y reportes entre roles asistidos. | Razonamiento asistido, redaccion, diagnostico, preparacion de cambios conceptuales y reportes. | No son ejecutables finales, no verifican/aprueban su propio trabajo y no cierran gates. | AP-03, AP-04, AP-05; DEC-ACCEPTED-056/068/069. |
| Commands candidatos | OpenCode puede tratarlos como entradas repetibles futuras o interfaces conceptuales. | Estandarizar tareas recurrentes, parametros esperados y salidas candidatas en secciones posteriores. | No se nombran ni crean commands reales, permisos finales o configuracion. | S04 entradas repetibles; S06 SP-05. |
| Scripts/CLI/validators candidatos | OpenCode puede invocar o solicitar controles solo cuando futuras secciones/spikes los definan. | Control deterministico conceptual sobre estructura, trazabilidad, evidencia, source policy y Odoo cuando aplique. | No se implementan scripts, validators, schemas ni toolchain final en S07. | AP-04; S04 control deterministico; S06 Banda C. |
| Reglas/config conceptuales | OpenCode debe operar bajo reglas aprobadas del Blueprint y `project-truth/`. | Mantener invariantes de scope, source policy, gates, evidencia, seguridad y exclusion de `framework/`. | No se crean archivos de configuracion ni permission rules. | AP-01, AP-02, AP-06, AP-12; S05. |
| Skills/playbooks conceptuales | OpenCode puede usar playbooks como conocimiento procedimental futuro si son aprobados. | Guiar pasos repetibles sin sustituir determinismo, evidencia ni owner approval. | No se crean skills OpenCode, plugins ni MCP en S07. | AP-03; S06 SP-05; S03 BR-02. |
| Humano critico / owner | OpenCode prepara contexto y opciones para decision humana. | Owner approval, decisiones de alcance, conflictos bloqueantes y cierre de gates cuando aplique. | OpenCode no delega ni simula autoridad humana. | AP-05; S05 estado/gates. |

##### 7. Conceptual Handoff Flows

Los flujos siguientes son logicos, no secuencias ejecutables ni comandos.

1. **Source of truth -> OpenCode coordination:** `project-truth/`, context packets y estado permitido entregan alcance, restricciones, decisiones y criterios. OpenCode solo opera dentro de ese contexto autorizado.
2. **OpenCode coordination -> mechanism candidate:** OpenCode encamina la tarea hacia agente conceptual, command candidato, playbook o control deterministico candidato segun el tipo de trabajo. La seleccion no cambia autoridad ni crea artefactos.
3. **Mechanism candidate -> deterministic control candidate:** Cuando el trabajo requiera verificabilidad, el resultado debe poder pasar a controles deterministicos futuros. En S07 esto es solo una expectativa conceptual para S08-S11.
4. **Deterministic control candidate -> evidence/storage candidate:** Los resultados verificables deberan registrarse como evidencia/log/estado auditable en secciones posteriores. OpenCode puede transportar o resumir, pero no ser storage final.
5. **Evidence/storage candidate -> source of truth:** Solo mediante registro gobernado, revision y aprobacion aplicable un output runtime puede impactar decisiones, estado o trazabilidad oficial.
6. **OpenCode coordination -> source policy / Knowledge Gap:** Si falta fuente autorizada, OpenCode debe encaminar la brecha como Knowledge Gap o Curation Request futura; no debe inventar ni ampliar fuentes.
7. **OpenCode coordination -> Odoo 18 pilot zone:** Para el piloto, OpenCode puede coordinar preparacion, observaciones y evidencia candidata del ciclo Odoo 18. No define funcionalidad nueva, PRD, SDD, backlog ni entorno real.
8. **Security/secrets cross-flow:** Cualquier necesidad de permisos, secretos o acceso debe tratarse como restriccion transversal y/o spike posterior; no se materializa en configuracion.

##### 8. V1 Boundaries Preserved

- **Odoo-only / Odoo 18:** El operating design se limita al dominio Odoo y target Odoo 18; no introduce otros dominios ni integraciones por defecto.
- **Piloto confirmado:** Las referencias de operacion se acotan a solicitudes internas / aprobaciones simples; S07 no convierte el piloto en PRD, SDD ni backlog.
- **Minimalidad V1:** OpenCode coordina el minimo necesario para trazabilidad, gates, evidencia y source policy sin RAG/vector, SDK/server core, dashboard productizado, CI/CD completo, storage avanzado, multiuser/team avanzado, plugins/MCP ni curation avanzada.
- **No implementacion:** Toda capacidad queda conceptual hasta que secciones posteriores y spikes autorizados la detallen; S07 no valida, ejecuta ni cierra incertidumbres.
- **Greenfield desde `project-truth/`:** El diseno no usa fuentes legacy ni material externo no autorizado como base.

##### 9. Open Questions / Owner Decisions

- none

##### 10. Acceptance Criteria

- La seccion queda en `Status: in-verification` para auditoria del verifier, con `Owner approval: not-requested`.
- El diseno define OpenCode como runtime primario y hub de coordinacion dentro del modelo hibrido progresivo, sin convertirlo en autoridad de estado, gate, storage, source policy ni evidencia suficiente por si solo.
- La seccion especifica que coordina OpenCode: handoffs, context routing, guia o invocacion conceptual de mecanismos candidatos y preparacion de evidencia candidata.
- La seccion especifica que OpenCode no decide: approvals, gates, cambios de estado, source policy, cierre, conflictos ni expansion de scope.
- Agentes conceptuales, commands candidatos, scripts/CLI/validators candidatos, reglas/config y skills/playbooks quedan diferenciados sin crear artefactos ejecutables ni configuracion.
- Los handoff flows conectan fuente de verdad, OpenCode, control deterministico candidato, evidencia/storage, source policy/Knowledge Gap, seguridad/secrets y Odoo 18 piloto sin implementar runtime.
- El diseno respeta Odoo-only, Odoo 18, piloto internal requests / simple approvals, source policy minima y exclusion de `framework/`.
- Cada responsabilidad queda trazable a AP-02..AP-05, S04, S05, S06 SP-04/SP-05, BR-01/BR-02 o decisiones aceptadas citadas.

##### 11. Section Output / Handoff

- Para S08, S07 entrega los limites operativos que deben guiar el split entre agentes conceptuales, commands candidatos, scripts/CLI/validators candidatos, reglas/config, skills/playbooks y humano critico.
- Para S09-S12, S07 entrega expectativas conceptuales de control deterministico, evidencia/storage y source policy sin crear schemas, validators, storage fisico ni source tooling.
- Para S13-S15, S07 entrega el rol de OpenCode frente al ciclo Odoo 18 y piloto confirmado sin crear entorno, modulo, PRD, SDD ni backlog.
- Para S16, S07 conserva SP-04 y SP-05 como incertidumbres de permisos y commands/skills candidatos que deben validarse antes de convertir mecanismos en diseno operacional final.

#### 8. Agents / Commands / Scripts / Validators Split

##### 1. Status

Status: closed

Owner approval: approved

##### 2. Purpose

Esta seccion define el split conceptual de responsabilidades entre agentes, command candidates, script/CLI/validator candidates, rules/config, skills/playbooks y humano/owner para CAFL V1. El objetivo es convertir las relaciones hibridas de S07 en criterios de asignacion de mecanismos sin crear mecanismos ejecutables, configuracion, scripts, validators, schemas, runtime, backlog, PRD, SDD ni implementacion.

S08 preserva el modelo hibrido progresivo: OpenCode coordina y encamina, los agentes razonan, los commands candidatos estandarizan entradas, los controles deterministicos candidatos verifican cuando futuras secciones los definan, las reglas/config sostienen invariantes, los skills/playbooks contienen conocimiento procedimental y el owner conserva decisiones y cierres. Ningun mecanismo runtime sustituye `project-truth/`, owner approval, gates, evidencia gobernada ni source policy.

##### 3. Inputs / Scope

Entradas trazables usadas:

- S07: operating design de OpenCode, relaciones hibridas y handoff flows entre fuente de verdad, OpenCode, mecanismos candidatos, control deterministico candidato, evidencia/storage, source policy/Knowledge Gap, seguridad/secrets y Odoo 18 piloto.
- S02: AP-02, AP-03, AP-04 y AP-05 sobre OpenCode no autoritativo, modelo hibrido progresivo, separacion reasoning/control y avance por contratos, gates y evidencia.
- S03: BR-01 y BR-02 para mantener V1 core limitado y conservar incertidumbres condicionales/spike sin convertirlas en aprobacion de implementacion.
- S04: zonas conceptuales de coordinacion OpenCode, entradas repetibles, control deterministico candidato, rules/config, skills/playbooks, source policy, evidencia/storage, Odoo 18 piloto y seguridad/secrets.
- S05: separacion source-vs-runtime: autoridad en `project-truth/`; outputs runtime solo como evidencia candidata hasta registro gobernado.
- S06: SP-04 y SP-05 como incertidumbres sobre permisos OpenCode y commands/skills candidatos; S08 las referencia, no las cierra.
- Decisiones aceptadas aplicables: DEC-ACCEPTED-056, 068, 069, 136, 137 y 140 para modelo hibrido progresivo; DEC-ACCEPTED-138 para direccion conceptual de mecanismos; DEC-ACCEPTED-162 y DEC-ACCEPTED-163 para piloto y source policy minima.

Alcance de S08:

- Diferenciar responsabilidades conceptuales por tipo de mecanismo.
- Indicar que tipo de trabajo debe ir a razonamiento asistido, entrada repetible, control deterministico, regla/config, procedimiento reusable o decision humana.
- Preparar handoff para S09-S12 sobre schemas, validators, storage/evidence y source policy, sin definirlos fisicamente.
- Preparar handoff para S13-S15 sobre evidencia Odoo 18, seguridad/secrets y piloto, sin crear entorno ni modulo.

##### 4. Mechanism Split

Los mecanismos siguientes son categorias conceptuales, no artefactos aprobados. No son nombres finales, comandos ejecutables, agentes reales, scripts, validators, schemas, permission rules ni configuracion OpenCode.

| Mecanismo | Responsabilidad conceptual V1 | Asignar aqui cuando el trabajo sea | No debe asumir | Trazabilidad |
| --- | --- | --- | --- | --- |
| Agents conceptuales | Razonamiento asistido, analisis de contexto autorizado, redaccion conceptual, diagnostico, preparacion de propuestas, reportes y handoffs para revision. | La tarea requiere interpretar fuentes aprobadas, resumir contexto, proponer cambios conceptuales, detectar gaps, preparar evidencia candidata o explicar trade-offs. | No son ejecutables finales; no aprueban, verifican su propio trabajo, cierran gates, cambian estado, resuelven conflictos por criterio propio ni sustituyen controles deterministicos. | S07 hybrid relationships; AP-03/AP-04/AP-05; S04 coordinacion OpenCode; S05 source-vs-runtime; DEC-ACCEPTED-056/068/069/136/137/140. |
| Command candidates | Entradas repetibles futuras para iniciar trabajos recurrentes con parametros, restricciones y salidas esperadas de forma estandarizada. | La tarea necesita repetibilidad de input, encuadre consistente, DoR contextual o handoff predecible, pero no una verificacion deterministica ni autoridad de gate. | No son commands reales, interfaces finales, permission rules ni evidencia suficiente; no aprueban gates, no cambian estado y no reemplazan `project-truth/`. SP-05 sigue abierto. | S07 handoff flow OpenCode -> mechanism candidate; AP-03/AP-05; S04 entradas repetibles; S06 SP-05; S03 BR-02; DEC-ACCEPTED-138/140. |
| Script/CLI/validator candidates | Control deterministico conceptual para comprobaciones futuras de estructura, trazabilidad, DoR, evidencia, source policy, logs/state y resultados Odoo cuando S09-S12/S13 los definan. | La tarea requiere un resultado verificable, reproducible o bloqueante basado en reglas objetivas aprobadas, no en juicio LLM. | No se implementan scripts, CLIs, validators, schemas ni toolchains aqui; no sustituyen owner approval ni cierran gates por si solos; solo producirian evidencia candidata gobernable. | S07 deterministic control flow; AP-04/AP-05; S04 control deterministico; S05 evidencia candidata; S06 Banda C; DEC-ACCEPTED-069/138/140. |
| Rules/config conceptuales | Invariantes de alcance, autoridad, source policy, estado, evidencia, seguridad, exclusiones y limites V1 que todos los mecanismos deben respetar. | La tarea requiere una regla estable para impedir scope creep, preservar source policy minima, proteger gates/estado, excluir `framework/` o mantener seguridad/secrets como criterio transversal. | No se crean archivos de configuracion, schemas, permission rules ni policies ejecutables; OpenCode no se convierte en policy engine final. SP-04 sigue abierto. | AP-02/AP-05/AP-07/AP-10/AP-12; S04 rules/config y seguridad; S05 autoridad-runtime; S06 SP-04; DEC-ACCEPTED-136/137/140/163. |
| Skills/playbooks conceptuales | Conocimiento procedimental reusable: pasos, checklist narrativo, criterios de handoff y guias de actuacion bajo contexto autorizado. | La tarea requiere orientar una secuencia humana/asistida repetible sin convertirla en command, script o validator. | No son skills OpenCode reales, plugins, MCP, prompts finales ni automatizacion aprobada; no reemplazan controles deterministicos, evidencia ni owner approval. SP-05 sigue abierto. | S07 skills/playbooks relationship; AP-03/AP-04; S04 skills/playbooks; S06 SP-05; S03 BR-02; DEC-ACCEPTED-056/068/138. |
| Human / owner | Decisiones de alcance, owner approval, cierre de gates, resolucion de conflictos bloqueantes, aprobacion de fuentes fuera de minima, aceptacion de riesgos y cambios de estado autorizados. | La tarea afecta autoridad, aprobacion, cierre, excepciones de source policy, cambios de scope, conflictos entre fuentes, capacidades condicionales o incertidumbres que requieren decision. | No debe ser simulado por OpenCode, agente, command candidate, validator candidate o script; ningun output runtime equivale a owner approval. | S07 human/owner relationship; AP-02/AP-05; S05 estado/gates; S03 BR-01/BR-02; DEC-ACCEPTED-136/140/162/163. |

Reglas de asignacion por tipo de control:

- **Razonamiento y redaccion:** asignar a agents conceptuales cuando el valor dependa de interpretacion, sintesis o propuesta; cualquier resultado queda sujeto a revision y posible control deterministico futuro. Trazabilidad: AP-03/AP-04; S07 agents; DEC-ACCEPTED-056/068/069.
- **Repetibilidad de entrada:** asignar a command candidates cuando el problema sea estandarizar como se inicia un trabajo recurrente; no usar commands para aprobar, cerrar ni registrar autoridad. Trazabilidad: S04 entradas repetibles; S07 command candidates; S06 SP-05; AP-05.
- **Verificabilidad objetiva:** asignar a script/CLI/validator candidates cuando la necesidad sea comprobar reglas aprobadas de forma reproducible; el detalle corresponde a S09-S12/S13 y a spikes posteriores. Trazabilidad: AP-04/AP-05; S04 control deterministico; S05 runtime evidence candidate; DEC-ACCEPTED-138/140.
- **Invariantes:** asignar a rules/config conceptuales cuando la responsabilidad sea mantener limites obligatorios de scope, source policy, seguridad, gates, estado o exclusion de `framework/`. Trazabilidad: AP-02/AP-07/AP-10/AP-12; S05 authority separation; DEC-ACCEPTED-163.
- **Procedimiento reusable:** asignar a skills/playbooks conceptuales cuando se requiere guiar pasos o criterios sin formalizarlos como comando o validator. Trazabilidad: AP-03; S07 skills/playbooks; S06 SP-05; S03 BR-02.
- **Decision y cierre:** asignar a human/owner cuando haya approval, gate closure, conflicto, excepcion de fuentes, cambio de alcance o incertidumbre bloqueante. Trazabilidad: AP-05; S05 estado/gates; S07 human/owner.

##### 5. Cross-Section Guidance / Handoff Rules

- **Para S09 Schemas V1 Minimum Set:** S08 entrega que los schemas futuros deben servir a controles deterministicos, evidencia y trazabilidad; no deben modelar agentes, commands o playbooks como autoridad por si mismos.
- **Para S10 Validators V1 Minimum Set:** S08 entrega que validators futuros pertenecen al mecanismo de control deterministico candidato y no a agents ni commands; su resultado no sustituye owner approval ni evidencia gobernada.
- **Para S11 State / Logs / Evidence Storage:** S08 entrega que logs, reportes, outputs de agents/commands y resultados de validators son evidencia candidata hasta registro trazable bajo la separacion source-vs-runtime de S05.
- **Para S12 Knowledge Base and Source Policy Implementation:** S08 entrega que source policy minima, Knowledge Gap y Curation Request deben tratarse como reglas/config conceptuales y controles futuros, no como memoria libre de OpenCode, RAG/vector ni busqueda web libre.
- **Para S13 Odoo 18 Execution Environment:** S08 entrega que la evidencia Odoo 18 del piloto debe pasar por controles deterministicos candidatos cuando sean definidos, manteniendo Odoo-only, Odoo 18 e internal requests / simple approvals.
- **Para S14 Security and Secrets:** S08 entrega que permisos, secretos y accesos son invariantes/riesgos transversales; SP-04 permanece abierto y esta seccion no define permission rules, vault ni secrets policy ejecutable.
- **Para S15 Pilot Module Blueprint:** S08 entrega criterios para usar agents en razonamiento, commands en repetibilidad y validators en evidencia del piloto sin crear PRD, SDD, backlog funcional ni modulo.
- **Para S16 Spikes:** S08 preserva SP-04/SP-05 como incertidumbres sobre permisos y commands/skills; tambien deja language/toolchain de scripts/CLI/validators como validacion futura, no como eleccion cerrada.

##### 6. Explicit Non-Decisions

- Esta seccion no crea agents ejecutables, commands reales, scripts, CLIs, validators, schemas, OpenCode config, permission rules, skills reales, plugins, MCP, runtime, backlog, PRD, SDD ni implementacion.
- Esta seccion no nombra mecanismos finales, no define interfaces de command, no define prompts finales, no define toolchain, no decide lenguaje de scripts/CLI y no define storage fisico.
- Esta seccion no convierte OpenCode en autoridad de estado, gate, source policy, storage, decision, evidencia suficiente ni policy engine.
- Esta seccion no convierte commands o scripts en autoridad final de gates, estado, cierre u owner approval.
- Esta seccion no cierra SP-04 ni SP-05; solo ubica sus responsabilidades conceptuales dentro del split.
- Esta seccion no introduce RAG/vector, SDK/server core, MCP/plugins, CI/CD completo, storage avanzado, multiuser/team operation, integraciones amplias, dashboard productizado, curation avanzada ni capacidades post-V1.
- Esta seccion no usa ni referencia `framework/` como input, evidencia, layout, fuente de agents, commands, validators, schemas, runtime o conocimiento.

##### 7. Open Questions / Owner Decisions

- none

##### 8. Acceptance Criteria

- La seccion queda en `Status: in-verification` para auditoria del verifier, con `Owner approval: not-requested`.
- El split diferencia agents conceptuales, command candidates, script/CLI/validator candidates, rules/config, skills/playbooks y human/owner sin crear artefactos ejecutables.
- Cada mecanismo y regla de asignacion queda trazado a S07, AP-02..AP-05, AP-07/AP-10/AP-12, S04, S05, S03 BR-01/BR-02, S06 SP-04/SP-05 o decisiones aceptadas aplicables.
- OpenCode permanece como runtime primario y hub de coordinacion, no como autoridad de estado, gate, storage, source policy, policy engine ni evidencia suficiente.
- El control deterministico queda reservado para script/CLI/validator candidates futuros; agents y commands no sustituyen verificaciones reproducibles, gates ni owner approval.
- SP-04 y SP-05 quedan referenciados como incertidumbres abiertas, no cerradas.
- La seccion respeta Odoo-only, Odoo 18, piloto internal requests / simple approvals, source policy minima y exclusion de `framework/`.
- La seccion no introduce RAG/vector, SDK/server core, MCP/plugins, CI/CD completo, advanced storage, multiuser, post-V1 capabilities, runtime, backlog, PRD, SDD ni implementacion.

##### 9. Section Output / Handoff

- S08 entrega a S09-S12 el split conceptual que separa razonamiento, entrada repetible, control deterministico, invariantes, conocimiento procedimental y decision humana para que schemas, validators, storage/evidence y source policy se definan sin confundir mecanismos ni autoridad.
- S08 entrega a S13-S15 criterios para coordinar trabajo del piloto Odoo 18 sin ampliar scope ni crear artefactos ejecutables.
- S08 entrega a S16 incertidumbres preservadas sobre permisos OpenCode, commands/skills y toolchain de control para ordenarlas como validaciones futuras sin autocierre.

### Iteration 3 - Artefactos tecnicos de control

#### 9. Schemas V1 Minimum Set

Status: closed

Owner approval: approved explicitly by owner.

##### 1. Purpose

S09 define el set minimo conceptual de schemas V1 necesario para que CAFL pueda describir, controlar y auditar el flujo piloto Odoo-only / Odoo 18 / solicitudes internas y aprobaciones simples sin crear schemas fisicos, archivos de schema, runtime ni implementacion.

El objetivo es fijar categorias logicas compartidas para:

- alimentar S10 con controles deterministicos candidatos trazables;
- alimentar S11 con estado, logs y evidencia auditables;
- alimentar S12 con source policy minima, Knowledge Gap y Curation Request conceptuales;
- mantener separacion source-vs-runtime: la autoridad permanece en `project-truth/` y cualquier output runtime es evidencia candidata hasta registro gobernado;
- preservar que los schemas V1 son minimos y no permanentes.

##### 2. Inputs / Scope

Inputs trazables usados:

- S07: OpenCode como runtime primario y hub de coordinacion, no como autoridad de estado, gate, storage, source policy o decision.
- S08: los schemas futuros deben servir a controles deterministicos, evidencia y trazabilidad; no deben modelar agents, commands o playbooks como autoridad por si mismos.
- CRIT-06: modelo logico requerido para estado, evidencia, trazabilidad, IDs, logs y governance de fuentes.
- CRIT-07: direccion de schemas V1 minimos, versionados y no permanentes, con validators minimos como direccion posterior.
- S02 AP-01/AP-04/AP-06/AP-09: trazabilidad bidireccional, separacion LLM/control deterministico, minimo contexto/source policy y evidencia simple auditable Git-compatible.
- S03 BR-01: V1 core limitado a Odoo-only, Odoo 18 y piloto de solicitudes internas / aprobaciones simples.
- S04: zonas conceptuales de control deterministico candidato, estado/logs/evidencia auditable, source policy y Odoo 18 piloto.
- S05: source-vs-runtime; `project-truth/` conserva autoridad y outputs runtime son evidencia candidata.
- Decisiones aceptadas citadas para esta seccion: DEC-ACCEPTED-138, DEC-ACCEPTED-140, DEC-ACCEPTED-145, DEC-ACCEPTED-162 y DEC-ACCEPTED-163.
- TOM: handoff al Blueprint para schemas, logs, evidence y storage como trabajo conceptual posterior al TOM aprobado.

Alcance de S09:

- Nombrar categorias conceptuales minimas de schema para V1.
- Describir que modela cada schema a nivel logico.
- Indicar campos o elementos conceptuales, sin definir tipos fisicos, formatos finales, JSON Schema, DDL, rutas ni archivos.
- Trazar cada schema a CRIT, TOM, decision aceptada, AP, BR o seccion previa.
- Indicar a que seccion posterior alimenta cada schema.

Fuera de alcance:

- Crear schemas fisicos, finales o archivos de schema.
- Crear validators reales, scripts, CLIs, runtime, agents, commands, playbooks ejecutables, RAG/vector base, backlog, PRD, SDD o implementacion.
- Convertir agents, commands, playbooks u outputs runtime en autoridad.
- Cambiar source policy, owner approval, status semantics o reglas de governance.
- Expandir V1 fuera de Odoo 18 y del piloto interno de solicitudes/aprobaciones simples.
- Usar o referenciar `framework/` como input.

##### 3. Schemas V1 Minimum Set

Los schemas siguientes son categorias logicas minimas. No son archivos, no son contratos finales de API, no son tablas, no son JSON Schema/YAML schema, no son validators y no fijan formato fisico. Cada schema debe poder evolucionar o ser reemplazado tras V1 porque CRIT-07 exige schemas minimos no permanentes.

| ID | Schema conceptual | Proposito | Campos / elementos conceptuales minimos | Trazabilidad | Handoff |
| --- | --- | --- | --- | --- | --- |
| SCH-01 | Authority Source Schema | Modelar la identidad logica de una fuente autorizada o fuente candidata para preservar source-vs-runtime y evitar autoridad paralela. | Identificador de fuente; tipo de fuente; estado de autoridad; alcance permitido; version/referencia; relacion con decision/CRIT/TOM; restricciones de uso; motivo si es candidata o no autorizada. | CRIT-06 source governance; CRIT-07 schemas minimos; TOM handoff schemas/evidence; AP-01; AP-06; S05; DEC-ACCEPTED-163. | S10 valida source policy minima y uso de fuentes; S12 define Knowledge Gap/Curation Request conceptual; S11 conserva evidencia de fuente. |
| SCH-02 | Traceability Link Schema | Modelar enlaces bidireccionales entre componentes del Blueprint, decisiones, riesgos/pendientes autorizados, evidencia y controles. | Identificador de enlace; origen; destino; tipo de relacion; obligatoriedad; estado del enlace; evidencia asociada; gaps o conflicto registrado; seccion consumidora. | CRIT-06 trazabilidad/IDs; CRIT-07; TOM traceability handoff; AP-01; RULE-04; S02; S05. | S10 valida cobertura trazable; S11 registra links/evidencia; S17 consume la matriz final sin cerrarla aqui. |
| SCH-03 | Work State Schema | Modelar el estado logico de secciones, iteraciones, gates y handoffs sin sustituir `blueprint-state.yaml` ni owner approval. | Identificador de unidad de trabajo; tipo de unidad; status permitido; owner approval; dependencia; gate relacionado; open issues; reportes asociados; timestamps conceptuales o marcador temporal auditable; actor/rol responsable como metadato no autoritativo. | CRIT-06 estado/IDs/logs; CRIT-07; TOM state/storage handoff; AP-05; S05; Blueprint contract/state semantics. | S10 valida transiciones permitidas; S11 define storage/logs/evidence; S19 revisa acceptance criteria sin autocierre. |
| SCH-04 | Gate and Approval Schema | Modelar gates, aprobaciones owner y bloqueos de avance como entidades logicas trazables, sin permitir cierre automatico. | Identificador de gate; scope del gate; prerequisitos; estado del gate; owner approval esperado/obtenido; evidencia requerida; bloqueos retroactivos; decision asociada; resultado permitido. | CRIT-06 estado/evidencia; CRIT-07; TOM gate/evidence handoff; AP-05; RULE-01/RULE-02; S05. | S10 valida prerequisitos/gates; S11 conserva evidencia de aprobacion; S16-S19 consumen para orden, trazabilidad y cierre, sin decidir aqui. |
| SCH-05 | Evidence Record Schema | Modelar evidencia simple, auditable y Git-compatible para soportar controles, revisiones y handoffs. | Identificador de evidencia; tipo de evidencia; origen; seccion/control relacionado; resumen verificable; ubicacion logica; estado candidato/registrado; trazas a fuente/decision/control; limitaciones; resultado observado. | CRIT-06 evidencia/logs/IDs; CRIT-07; TOM evidence/storage handoff; AP-04; AP-09; S05; DEC-ACCEPTED-140/145. | S10 valida evidencia esperada por control; S11 define storage/logs; S13-S15 consumen evidencia Odoo 18 piloto. |
| SCH-06 | Deterministic Control Schema | Modelar controles deterministicos candidatos que S10 puede convertir en set conceptual de validators, sin crear validators reales. | Identificador de control; regla verificable; input conceptual; output conceptual; condicion de bloqueo/no bloqueo; evidencia requerida; trazabilidad a schema/fuente; limites; seccion responsable. | CRIT-06 control/log/evidencia; CRIT-07 validators minimos como direccion; TOM control handoff; AP-04; S04; S08; DEC-ACCEPTED-138/140/145. | S10 define validators V1 minimum set; S11 registra resultados; S13-S15 usan controles candidatos para evidencia piloto. |
| SCH-07 | Runtime Output / Candidate Evidence Schema | Modelar outputs de OpenCode, agents conceptuales, commands candidatos, scripts/validators candidatos o reportes como evidencia candidata no autoritativa. | Identificador de output; mecanismo conceptual origen; input/handoff relacionado; resumen; estado candidato; controles pendientes; fuente autorizada usada; evidencia derivada; restricciones; decision humana requerida si aplica. | CRIT-06 logs/evidencia/source governance; CRIT-07; AP-03/AP-04/AP-05; S05; S07; S08. | S10 valida que outputs no sustituyan gates; S11 almacena logs/evidencia; S12 controla fuente/contexto minimo. |
| SCH-08 | Context Packet Schema | Modelar paquetes compactos de contexto autorizado para trabajo seccional sin convertirlos en fuente de verdad. | Identificador de paquete; seccion objetivo; fuentes resumidas; anchors de trazabilidad; restricciones heredadas; fallback triggers; fecha/generador; estado de no-autoridad; gaps declarados. | CRIT-06 context/source governance; CRIT-07; AP-06; S05; S07; S08; TOM context handoff. | S10 valida completitud minima del contexto; S11 conserva evidencia de uso; S12 gobierna source policy y Knowledge Gap. |
| SCH-09 | Source Policy / Knowledge Gap Schema | Modelar source policy minima, gaps de conocimiento y solicitudes de curacion sin introducir RAG/vector ni busqueda libre. | Identificador de politica/gap; fuente esperada; fuente disponible; tipo de gap; impacto; estado; solicitud de curacion; decision owner requerida si aplica; relacion con Odoo official docs / github.com/odoo/odoo. | CRIT-06 source governance; CRIT-07; AP-06; AP-12; S03 BR-01/BR-02; S05; DEC-ACCEPTED-163. | S10 valida cumplimiento source policy; S12 desarrolla Knowledge Gap/Curation Request conceptual; S13-S15 usan solo fuentes permitidas para Odoo 18. |
| SCH-10 | Odoo Pilot Artifact Schema | Modelar artefactos conceptuales del piloto Odoo 18 necesarios para evidencia y controles, limitado a solicitudes internas / aprobaciones simples. | Identificador de artefacto piloto; tipo de artefacto; relacion con flujo internal request/simple approval; version/entorno conceptual Odoo 18; fuente Odoo autorizada; control/evidencia asociada; estado candidato/registrado; restricciones de alcance. | CRIT-06 evidence/IDs/logs; CRIT-07; TOM Odoo handoff; BR-01; AP-08; S03; S04; DEC-ACCEPTED-162/163. | S13 define entorno conceptual Odoo 18; S15 consume para modulo piloto; S10/S11 definen controles y evidencia asociados. |

##### 4. Cross-Section Guidance / Handoff Rules

- **Para S10 Validators V1 Minimum Set:** S10 debe derivar validators conceptuales desde SCH-01..SCH-10 solo como controles deterministicos candidatos. Ningun validator futuro puede cerrar gates, otorgar owner approval ni convertir outputs runtime en autoridad.
- **Para S11 State / Logs / Evidence Storage:** S11 debe usar SCH-03, SCH-05 y SCH-07 como base para almacenamiento logico simple y auditable, manteniendo `project-truth/` como autoridad y tratando evidencia runtime como candidata hasta registro gobernado.
- **Para S12 Knowledge Base and Source Policy Implementation:** S12 debe usar SCH-01, SCH-08 y SCH-09 para source policy minima, contexto autorizado, Knowledge Gap y Curation Request, sin RAG/vector base, busqueda libre ni expansion de fuentes.
- **Para S13 Odoo 18 Execution Environment:** S13 debe usar SCH-10 junto con SCH-01/SCH-05/SCH-06 para describir evidencia del entorno Odoo 18 sin crear entorno ni implementacion.
- **Para S14 Security and Secrets:** S14 debe consumir los elementos de fuente, evidencia, estado y control solo como categorias logicas; esta seccion no define permission rules, vault, secrets policy ejecutable ni accesos.
- **Para S15 Pilot Module Blueprint:** S15 debe limitar cualquier uso de schemas al piloto internal requests / simple approvals y registrar evidencia/control sin crear PRD, SDD, backlog funcional ni modulo.
- **Para S16-S19:** los schemas apoyan orden de spikes, trazabilidad final, categorias de output y acceptance criteria; no cierran aceptacion final ni reemplazan owner approval.

##### 5. Explicit Non-Decisions

- Esta seccion no crea schemas fisicos, archivos de schema, JSON Schema, DDL, YAML schema, contratos finales de API, tablas, modelos ORM ni formatos definitivos.
- Esta seccion no crea validators reales, scripts, CLIs, agents ejecutables, commands reales, skills/playbooks reales, plugins, MCP, runtime, RAG/vector base, backlog, PRD, SDD ni implementacion.
- Esta seccion no decide rutas, nombres de archivos, repositorios runtime, toolchain, lenguaje, librerias, storage fisico, base de datos, CI/CD ni estructura final.
- Esta seccion no modela agents, commands o playbooks como autoridad; solo permite registrar sus outputs como evidencia candidata cuando corresponda.
- Esta seccion no cambia source policy minima, owner approval, status semantics, iteration gates ni reglas de governance.
- Esta seccion no expande V1 fuera de Odoo-only, Odoo 18 y piloto de solicitudes internas / aprobaciones simples.
- Esta seccion no usa ni referencia `framework/` como input.

##### 6. Open Questions / Owner Decisions

- none

##### 7. Acceptance Criteria

- La seccion queda en `Status: in-verification` para auditoria del verifier, con `Owner approval: not-requested`.
- El set minimo SCH-01..SCH-10 queda definido solo a nivel conceptual y no crea schemas fisicos, archivos, formatos finales ni implementacion.
- Cada schema queda justificado por control, trazabilidad o evidencia y trazado a CRIT-06, CRIT-07, TOM, decision aceptada, AP, BR o seccion previa aplicable.
- Los schemas sirven a controles deterministicos, evidencia, trazabilidad, estado, source policy y piloto Odoo 18 sin convertir OpenCode, agents, commands, playbooks ni runtime outputs en autoridad.
- Los handoffs a S10, S11 y S12 son suficientes para validators conceptuales, storage/evidence logico y source policy/Knowledge Gap sin cerrar decisiones futuras.
- Los handoffs a S13-S15 preservan Odoo-only, Odoo 18 y piloto internal requests / simple approvals.
- La seccion respeta source-vs-runtime de S05, minima/no permanencia de CRIT-07, separacion control deterministico de AP-04 y evidencia auditable de AP-09.
- La seccion no introduce RAG/vector base, SDK/server core, dashboard productizado, CI/CD completo, advanced storage/DB, multiuser/team operation, plugins/MCP, broad integrations ni post-V1 capabilities.
- La seccion mantiene `framework/` excluido y no reabre CRIT-01..07, TOM ni decisiones aceptadas.

##### 8. Section Output / Handoff

- S09 entrega a S10 el set SCH-01..SCH-10 como base conceptual para seleccionar validators V1 minimos y controles deterministicos candidatos.
- S09 entrega a S11 categorias logicas para estado, gates, logs, evidencia, outputs runtime candidatos y trazabilidad auditable.
- S09 entrega a S12 categorias logicas para Authority Source, Context Packet, Source Policy, Knowledge Gap y Curation Request sin RAG/vector ni expansion de fuentes.
- S09 entrega a S13-S15 una base limitada para evidencia Odoo 18 del piloto internal requests / simple approvals, sin crear entorno, modulo, PRD, SDD, backlog ni implementacion.

#### 10. Validators V1 Minimum Set

Status: closed

Owner approval: approved

##### 1. Purpose

S10 define el set minimo conceptual de validators V1 para CAFL, derivado de SCH-01..SCH-10 como candidatos de control deterministico. Los validators conceptuales sirven a gates, evidencia y execution checks sin crear validators reales, toolchain ejecutable, scripts ni implementacion.

El objetivo es fijar categorias logicas de validacion compartidas para:

- derivar controles deterministicos candidatos desde los schemas conceptuales de S09;
- alimentar gates de avance con checks verificables pero sin sustituir owner approval ni juicio tecnico;
- alimentar S11 con el conjunto de resultados candidatos que el storage/evidence debera registrar;
- preservar la separacion source-vs-runtime: los resultados de validators son evidencia candidata hasta registro gobernado, nunca autoridad por si mismos;
- mantener V1 boundaries: Odoo-only, Odoo 18, piloto de solicitudes internas / aprobaciones simples.

##### 2. Inputs / Scope

Inputs trazables usados:

- S09 SCH-01..SCH-10: categorias logicas de schema de las que derivan los validators como controles deterministicos candidatos.
- S08: validators pertenecen al mecanismo de control deterministico (script/CLI/validator candidates); su resultado no reemplaza owner approval ni evidencia gobernada.
- S07: OpenCode coordina handoffs y puede invocar validator candidates; no es autoridad de estado, gate, storage ni source policy.
- CRIT-06: modelo logico de estado, evidencia, trazabilidad, IDs y logs que los validators deben soportar.
- CRIT-07: direction de validators minimos, no permanentes, como contraparte de schemas minimos.
- AP-04: control deterministico separado del razonamiento LLM y reservado para script/CLI/validator candidates.
- AP-05: progreso contract/gate/evidence-driven sin autocompletado; owner approval requerido para gates y cierres.
- AP-09: evidencia simple, auditable y Git-compatible; resultados runtime son evidencia candidata.
- S04: zona conceptual de control deterministico candidato y estado/logs/evidencia auditable.
- S05: `project-truth/` conserva autoridad; outputs runtime incluido resultados de validators son candidatos.
- DEC-ACCEPTED-138: decisiones sobre validators/control aceptadas.
- DEC-ACCEPTED-140: decisiones sobre evidencia aceptadas.
- DEC-ACCEPTED-145: decisiones sobre evidencia aceptadas.
- TOM: control, evidencia y handoff anchors.
- BR-01: V1 Odoo-only boundary.

Alcance de S10:

- Nombrar categorias conceptuales minimas de validator para V1.
- Describir que controla cada validator a nivel logico, sin implementarlo.
- Indicar el schema S09 del que deriva, el control requerido al que responde y a que seccion posterior alimenta.
- Trazar cada validator a CRIT, TOM, decision aceptada, AP, BR o seccion previa.
- Definir handoff rules a S11 (storage/evidencia de resultados), S12 (source policy), S13-S15 (piloto Odoo 18).

Fuera de alcance:

- Crear validators reales, scripts, CLIs, toolchain ejecutable ni implementacion.
- Crear schemas fisicos, JSON Schema, YAML schema, DDL, tablas, modelos ORM ni formatos definitivos.
- Cerrar gates, otorgar owner approval ni convertir outputs runtime en autoridad.
- Introducir RAG/vector base, SDK/server, MCP/plugins, CI/CD, advanced storage, multiuser, integraciones amplias ni capacidades post-V1.
- Expandir V1 fuera de Odoo-only, Odoo 18 y piloto de solicitudes internas / aprobaciones simples.
- Usar o referenciar `framework/` como input.

##### 3. Validators V1 Minimum Set

Los validators siguientes son categorias logicas minimas derivadas de SCH-01..SCH-10 como controles deterministicos candidatos. No son archivos ejecutables, no son scripts, no son CLIs finales, no son configuracion de toolchain y no fijan implementacion. Cada validator debe poder evolucionar o ser reemplazado tras V1 porque CRIT-07 exige schemas y validators minimos no permanentes.

| ID | Validator conceptual | Schema derivado | Control requerido al que responde | Input conceptual | Output / resultado conceptual | Condicion de bloqueo potencial | Trazabilidad | Handoff |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| VAL-01 | Authority Source Validator | SCH-01 | Verificar que toda fuente referenciada en un componente tiene estado de autoridad declarado y relacion trazable a decision/CRIT/TOM | Referencia a fuente en un componente Blueprint o output runtime | Confirmacion de autoridad declarada / alerta de fuente no autorizada o candidata sin registro | Componente rechazado si referencia fuente no registrada y no marcada como candidata | CRIT-06 source governance; AP-06; S05; DEC-ACCEPTED-163; SCH-01 | S10 informa a S11 resultado candidato; S12 gobierna gaps de fuente; S12 gestiona Curation Request si fuente no autorizada. |
| VAL-02 | Traceability Link Validator | SCH-02 | Verificar que cada componente del Blueprint tiene al menos un enlace trazable a CRIT, TOM, decision aceptada, AP, BR o seccion previa; detectar gaps de trazabilidad | Componente o seccion a auditar; registro de links trazables existentes | Mapa de cobertura trazable / lista de gaps; confirmacion o alerta por componente | Alerta de gap que bloquea avance a siguiente seccion si el componente no tiene traza minima requerida | CRIT-06 trazabilidad/IDs; RULE-04; AP-01; SCH-02 | S11 registra resultados de cobertura; S17 consume para trazabilidad final sin cerrarla aqui. |
| VAL-03 | Work State Transition Validator | SCH-03 | Verificar que las transiciones de estado de secciones, iteraciones y gates son legales segun blueprint-state.yaml y las semanticas de status aprobadas; detectar transiciones no permitidas | Estado actual de seccion/iteracion/gate en blueprint-state.yaml; transicion propuesta | Confirmacion de transicion valida / alerta de transicion ilegal; log candidato | Bloqueo de transicion si no cumple el grafo de estados aprobados o si falta owner approval para cierre/aprobacion | CRIT-06 estado/IDs/logs; AP-05; blueprint-state.yaml semantics; SCH-03 | S11 conserva log de transiciones validas; S19 audita acceptance criteria sin autocierre. |
| VAL-04 | Gate Prerequisite Validator | SCH-04 | Verificar que los prerequisitos de un gate estan documentados y que la evidencia requerida existe como candidata antes de solicitar owner approval; no sustituye la decision owner | Gate a validar; prerequisitos requeridos documentados; evidencia candidata disponible | Checklist de prerequisitos cubiertos / lista de prerequisitos faltantes; estado del gate | Alerta de gate bloqueado si prerequisito faltante; owner approval sigue siendo requerida para cierre | CRIT-06 evidencia/estado; AP-05; RULE-01/RULE-02; SCH-04 | S11 registra evidencia de prerequisitos; S19 audita aceptacion; S16 consume para orden final. |
| VAL-05 | Evidence Record Validator | SCH-05 | Verificar que cada evidencia candidata tiene origen trazable, tipo declarado, resumen verificable y estado candidato/registrado; detectar evidencia sin trazabilidad o sin estado | Registro de evidencia candidata | Confirmacion de evidencia bien formada / alerta de evidencia sin trazabilidad, origen o estado | Alerta si evidencia usada en gate no tiene trazabilidad; evidencia mal formada no puede usarse como soporte de gate sin correccion | CRIT-06 evidencia/IDs; AP-09; DEC-ACCEPTED-140/145; SCH-05 | S11 almacena evidencia registrada; S13-S15 consumen para evidencia Odoo 18 piloto. |
| VAL-06 | Deterministic Control Completeness Validator | SCH-06 | Verificar que cada control deterministico candidato tiene regla verificable, input/output conceptual, condicion de bloqueo y trazabilidad declarados; detectar controles vacios o sin trazabilidad | Control deterministico candidato definido en S10 u otra seccion | Confirmacion de control completo / alerta de campo faltante; log candidato | Alerta si control deterministico carece de condicion de bloqueo o trazabilidad definida | CRIT-06 control/evidencia; AP-04; DEC-ACCEPTED-138; SCH-06 | S11 registra resultados de controles; S13-S15 usan controles candidatos para evidencia piloto. |
| VAL-07 | Runtime Output Classification Validator | SCH-07 | Verificar que cada output de OpenCode, agent conceptual, command candidato, script/validator candidato o reporte es clasificado como evidencia candidata y no como autoridad; detectar outputs promovidos indebidamente a autoridad | Output runtime a clasificar; origen declarado; estado de candidatura | Confirmacion de clasificacion candidata / alerta de output tratado como autoridad sin registro gobernado | Alerta si output runtime es referenciado como autoridad en un componente sin pasar por registro gobernado | CRIT-06 logs/source governance; AP-03/AP-04/AP-05; S05; S07; S08; SCH-07 | S10 informa a S11 resultado; S11 almacena logs/evidencia candidata. |
| VAL-08 | Context Packet Completeness Validator | SCH-08 | Verificar que cada context packet tiene identificador, seccion objetivo, anchors de trazabilidad, restricciones heredadas, fallback triggers y declaracion de no-autoridad; detectar packets incompletos | Context packet de una seccion | Confirmacion de packet completo / lista de campos faltantes o mal formados | Alerta si packet carece de anchors de trazabilidad o fallback triggers requeridos para el trabajo seccional | CRIT-06 context/source governance; AP-06; S05; S07; S08; SCH-08 | S11 conserva evidencia de uso de packets; S12 gobierna source policy y Knowledge Gap. |
| VAL-09 | Source Policy Compliance Validator | SCH-09 | Verificar que solo fuentes declaradas en la source policy minima (Odoo official docs, github.com/odoo/odoo) son usadas en componentes V1; detectar uso de fuentes no autorizadas o gaps no registrados | Referencia de fuente en componente; source policy declarada | Confirmacion de cumplimiento source policy / lista de fuentes no autorizadas o gaps no registrados | Alerta si fuente no autorizada es usada sin Curation Request registrada y aprobacion owner | CRIT-06 source governance; AP-06/AP-12; DEC-ACCEPTED-163; SCH-09 | S12 gestiona Knowledge Gap y Curation Request; S13-S15 usan fuentes dentro de source policy. |
| VAL-10 | Odoo Pilot Artifact Scope Validator | SCH-10 | Verificar que artefactos conceptuales del piloto Odoo 18 estan dentro del scope de solicitudes internas / aprobaciones simples, usan fuentes Odoo autorizadas y tienen evidencia/control asociados; detectar expansion de scope o uso de fuentes no autorizadas | Artefacto conceptual del piloto Odoo 18 | Confirmacion de artefacto dentro de scope / alerta de expansion de scope o fuente no autorizada | Alerta si artefacto piloto referencia entorno, modulo, PRD, SDD, backlog funcional o implementacion fuera de V1 boundary | CRIT-06 evidence/IDs; AP-08; BR-01; DEC-ACCEPTED-162/163; SCH-10 | S13 define entorno conceptual Odoo 18; S15 consume para modulo piloto; S11 registra evidencia/control. |

##### 4. Cross-Section Guidance / Handoff Rules

- **Para S11 State / Logs / Evidence Storage:** S11 debe recibir de S10 los resultados candidatos de VAL-01..VAL-10 como evidencia candidata a registrar. S11 debe definir como almacenar logs de transiciones de estado (VAL-03), resultados de prerequisitos de gate (VAL-04), confirmaciones de evidencia bien formada (VAL-05) y resultados de control deterministico (VAL-06) de forma simple, auditable y Git-compatible, sin crear storage fisico ni rutas finales. Ningun resultado de validator es autoridad por si mismo; requiere registro gobernado para ser evidencia formal.
- **Para S12 Knowledge Base and Source Policy Implementation:** S12 debe usar los resultados de VAL-01 (authority source) y VAL-09 (source policy compliance) como triggers de Knowledge Gap y Curation Request. Cuando VAL-01 detecta fuente no autorizada o VAL-09 detecta gap de source policy, S12 es el mecanismo conceptual que gestiona la respuesta sin ampliar fuentes por cuenta propia.
- **Para S13 Odoo 18 Execution Environment:** S13 debe consumir VAL-10 (Odoo pilot artifact scope) y VAL-05 (evidence record) para definir los controles conceptuales del entorno Odoo 18 sin crear entorno ni implementacion. S13 debe verificar que artefactos conceptuales del entorno respetan BR-01 y DEC-ACCEPTED-162/163.
- **Para S14 Security and Secrets:** S14 puede consumir VAL-01 (authority source) y VAL-09 (source policy compliance) como categorias logicas de control; S14 no define permission rules ejecutables, vault ni secrets policy final a partir de este set.
- **Para S15 Pilot Module Blueprint:** S15 debe limitar el uso de validators al piloto internal requests / simple approvals; VAL-10 es el control principal para preservar V1 scope en S15 sin crear PRD, SDD, backlog funcional ni modulo ejecutable.
- **Para S16-S19:** los validators apoyan el orden de spikes (S16), trazabilidad final (S17), categorias de output de backlog (S18) y acceptance criteria (S19); no cierran aceptacion final ni reemplazan owner approval.
- **Restriccion general:** Ningun validator puede cerrar un gate, otorgar owner approval, convertir outputs runtime en autoridad ni expandir scope V1. Los resultados de validators son siempre evidencia candidata hasta registro gobernado.

##### 5. Explicit Non-Decisions

- Esta seccion no crea validators reales, scripts, CLIs, toolchain ejecutable, configuracion de framework de testing ni implementacion.
- Esta seccion no crea schemas fisicos, archivos de schema, JSON Schema, DDL, YAML schema, contratos finales de API, tablas, modelos ORM ni formatos definitivos.
- Esta seccion no decide lenguaje de implementacion de validators, librerias, frameworks, rutas, nombres de archivos, repositorios runtime, CI/CD ni estructura final.
- Esta seccion no cierra gates, no otorga owner approval, no convierte resultados de validators en autoridad y no cambia status semantics.
- Esta seccion no modela agents, commands o playbooks como autoridad; sus resultados son siempre candidatos.
- Esta seccion no cambia source policy minima, owner approval, status semantics, iteration gates ni reglas de governance.
- Esta seccion no expande V1 fuera de Odoo-only, Odoo 18 y piloto de solicitudes internas / aprobaciones simples.
- Esta seccion no usa ni referencia `framework/` como input.
- Esta seccion no genera el orden final de spikes, la matriz de trazabilidad final, los outputs de backlog ni los acceptance criteria finales; esos pertenecen a S16-S19.

##### 6. Open Questions / Owner Decisions

- none

##### 7. Acceptance Criteria

- La seccion queda en `Status: in-verification` para auditoria del verifier, con `Owner approval: not-requested`.
- El set minimo VAL-01..VAL-10 queda definido solo a nivel conceptual como candidatos de control deterministico derivados de SCH-01..SCH-10; no crea validators reales, scripts, CLIs ni implementacion.
- Cada validator queda justificado por un control requerido y trazado a CRIT-06, CRIT-07, TOM, AP, BR, decision aceptada o seccion previa aplicable.
- Cada validator preserva que su resultado es evidencia candidata y no sustituye juicio tecnico, owner approval ni evidencia gobernada.
- Ningun validator cierra gates, otorga owner approval ni convierte outputs runtime en autoridad.
- Los validators preservan la separacion source-vs-runtime de S05 y la separacion LLM/control deterministico de AP-04.
- Los handoffs a S11, S12, S13-S15 y S16-S19 son suficientes para storage/evidencia logica, source policy/Knowledge Gap, piloto Odoo 18 y cierre sin cerrar decisiones futuras.
- La seccion respeta Odoo-only, Odoo 18, piloto internal requests / simple approvals, source policy minima (DEC-ACCEPTED-163) y exclusion de `framework/`.
- La seccion no introduce RAG/vector base, SDK/server core, dashboard productizado, CI/CD completo, advanced storage/DB, multiuser/team operation, plugins/MCP, broad integrations ni post-V1 capabilities.
- Todos los componentes son trazables a TOM, CRIT aprobado o decision aceptada (RULE-04).

##### 8. Section Output / Handoff

- S10 entrega a S11 el set conceptual VAL-01..VAL-10 como controles deterministicos candidatos cuyos resultados deben ser almacenados como evidencia candidata de forma simple, auditable y Git-compatible.
- S10 entrega a S12 los validators VAL-01 (authority source) y VAL-09 (source policy compliance) como triggers conceptuales de Knowledge Gap y Curation Request sin ampliar fuentes.
- S10 entrega a S13-S15 los validators VAL-05, VAL-06 y VAL-10 como controles conceptuales para evidencia del entorno Odoo 18 y del modulo piloto limitados a BR-01 y DEC-ACCEPTED-162/163.
- S10 entrega a S16-S19 el set conceptual VAL-01..VAL-10 como base para orden de spikes, trazabilidad final, categorias de output y acceptance criteria sin autocierre ni autoaprobacion.
- S10 no cierra ninguna decision sobre toolchain, lenguaje, rutas, storage fisico, CI/CD ni implementacion; esos pertenecen a spikes y fases posteriores con autorizacion explicita del owner.

#### 11. State / Logs / Evidence Storage

Status: closed

Owner approval: approved

##### 1. Purpose

S11 define el diseno conceptual de storage para estado, logs y evidencia en CAFL V1. Su objetivo es establecer como se almacenan, retienen y rastrean los artefactos de trabajo del piloto Odoo-only / Odoo 18 / solicitudes internas y aprobaciones simples de forma simple, auditable y Git-compatible, sin crear storage fisico, rutas finales, logs reales ni implementacion.

El objetivo es fijar categorias logicas compartidas para:

- modelar donde y como vive el estado autoritativo de secciones, iteraciones y gates;
- definir el ciclo de vida de evidencia candidata desde su origen (outputs runtime, resultados de validators) hasta su eventual registro gobernado;
- describir como se capturan logs de transiciones de estado, resultados de prerequisitos de gate, confirmaciones de evidencia bien formada y resultados de control deterministico;
- establecer la jerarquia de autoridad de storage: `project-truth/` es la unica fuente de verdad aprobada; evidencia runtime es candidata hasta registro gobernado;
- no duplicar estado ya cubierto por `blueprint-state.yaml` ni por `blueprint-contract.yaml`.

##### 2. Inputs / Scope

Inputs trazables usados:

- S09 SCH-03 Work State Schema: modelo logico del estado de secciones, iteraciones, gates y handoffs.
- S09 SCH-05 Evidence Record Schema: modelo logico de evidencia simple, auditable y Git-compatible.
- S09 SCH-07 Runtime Output / Candidate Evidence Schema: modelo logico de outputs de OpenCode, agents conceptuales, commands candidatos y validators candidatos como evidencia candidata no autoritativa.
- S10 VAL-03 Work State Transition Validator: resultados candidatos de transiciones de estado a registrar en logs de estado.
- S10 VAL-04 Gate Prerequisite Validator: resultados candidatos de prerequisitos de gate a registrar como evidencia candidata.
- S10 VAL-05 Evidence Record Validator: confirmaciones candidatas de evidencia bien formada.
- S10 VAL-06 Deterministic Control Completeness Validator: resultados candidatos de controles deterministicos a registrar.
- S08: logs, reportes y outputs de agents/commands son evidencia candidata hasta registro trazable bajo la separacion source-vs-runtime de S05.
- S07: OpenCode como runtime primario y hub de coordinacion; no es autoridad de estado, gate, storage ni source policy.
- S05: separacion source-vs-runtime; `project-truth/` conserva autoridad; outputs runtime son candidatos.
- S04: zonas conceptuales de estado, logs y evidencia auditable.
- CRIT-06: modelo logico de estado, storage logico, persistencia conceptual, IDs, logs, evidencia, fuentes, contexto, rework, deuda, approvals y trazabilidad.
- CRIT-07: direccion de schemas y validators minimos, no permanentes.
- AP-01: `project-truth/` como fuente unica de verdad; trazabilidad bidireccional.
- AP-04: control deterministico separado del razonamiento LLM.
- AP-05: progreso contract/gate/evidence-driven; no autocierre.
- AP-09: evidencia simple, auditable y Git-compatible.
- DEC-ACCEPTED-146: storage candidato V1 simple, auditable, Git-compatible (Markdown, JSON/YAML, JSONL append-only, artifacts; rutas finales para Blueprint).
- DEC-ACCEPTED-138: runtime candidato con storage fisico simple y auditable como direccion.
- DEC-ACCEPTED-140: automatizacion minima cubre validacion estructural y logs/estado/evidencia.
- TOM: handoff al Blueprint para schemas, logs, evidence y storage como trabajo conceptual posterior al TOM aprobado.

Alcance de S11:

- Describir categorias logicas de storage conceptual para estado, logs, evidencia y outputs candidatos.
- Definir el ciclo de vida de evidencia candidata y las condiciones de registro gobernado.
- Describir tipos conceptuales de storage compatibles con Git y el modelo de autoridad de `project-truth/`.
- Definir handoffs a S12 (source policy / Knowledge Gap), S13-S15 (evidencia piloto Odoo 18) y S16-S19 (trazabilidad final, backlog, acceptance criteria).

Fuera de alcance:

- Crear storage fisico, rutas finales, archivos reales ni artifacts.
- Crear logs reales ni implementacion de logging.
- Decidir toolchain, lenguaje, librerias, CI/CD ni estructura runtime final.
- Convertir OpenCode en storage final o autoridad de evidencia.
- Crear schemas fisicos, validators reales, scripts, commands, agents ejecutables.
- Crear RAG/vector base, SDK/server, backlog, PRD, SDD ni implementacion.
- Usar o referenciar `framework/` como input.
- Expandir V1 fuera de Odoo-only, Odoo 18, piloto internal requests / simple approvals.

##### 3. Conceptual Storage Design

El diseno de storage que sigue es logico y conceptual. No define archivos fisicos, rutas finales, formatos definitivos, base de datos ni toolchain. Cada categoria puede evolucionar o ser reemplazada tras V1 porque CRIT-07 exige schemas y validators minimos no permanentes.

###### 3.1 Jerarquia de autoridad de storage

La jerarquia de autoridad define que nivel de storage puede ser tratado como fuente de verdad y bajo que condiciones:

| Nivel | Descripcion | Autoridad | Condicion de promocion |
| --- | --- | --- | --- |
| L1 — project-truth/ | Estado operacional, decisions, blueprint, contract, state | Autoritativo | No requiere promocion; es la fuente aprobada |
| L2 — Evidencia registrada gobernada | Outputs runtime que pasaron por registro gobernado y fueron aceptados explicitamente | Autoritativo (por registro) | Requiere decision owner o proceso gobernado documentado |
| L3 — Evidencia candidata | Resultados de validators, outputs de OpenCode, reportes, logs de transiciones | Candidata | Puede ser promovida a L2 con registro gobernado; no es autoridad por si misma |
| L4 — Evidencia efimera / transitoria | Outputs de sesion, logs de depuracion, contexto de ejecucion no retenido | No autoritativa | No es elegible para promocion sin retener y registrar |

Regla fundamental: ningun output runtime puede actuar como autoridad de estado, gate o evidencia formal sin haber pasado de L3 a L2. `project-truth/` (L1) nunca es reemplazada por outputs runtime.

###### 3.2 Tipos conceptuales de storage

Los tipos conceptuales de storage describen formas logicas compatibles con Git y con el modelo de autoridad. No son implementacion ni definen herramientas finales:

| Tipo conceptual | Descripcion logica | Compatibilidad Git | Nivel de autoridad aplicable | Trazabilidad requerida |
| --- | --- | --- | --- | --- |
| Estado autoritativo estructurado | Archivos YAML/JSON que capturan estado operacional de secciones, iteraciones, gates y approvals | Alta (diff claro) | L1 | Trazable a blueprint-state.yaml, blueprint-contract.yaml |
| Documentos Markdown de evidencia | Archivos Markdown que documentan evidencia registrada con origen, tipo, estado y trazas | Alta | L2, L3 | Trazable a CRIT-06, decision, seccion o AP |
| Logs de transicion append-only | Registros de transiciones de estado, resultados de gate y resultados de validator en formato JSONL o equivalente conceptual, solo escritura al final | Alta (no sobreescribe historial) | L3 (candidato a L2 con registro gobernado) | Cada entrada trazable a seccion, validator y timestamp conceptual |
| Outputs de sesion candidatos | Outputs de OpenCode, commands, scripts o validators de una sesion dada, marcados como candidatos | Media (requiere gestion) | L3 | Marcados con origen runtime, seccion y estado candidato |
| Artefactos de evidencia nombrados | Reportes, checklists, context packets y outputs estructurados que apoyan gates y handoffs | Alta | L2 (si registrados), L3 (si candidatos) | Trazables a seccion, gate, decision o CRIT |

###### 3.3 Ciclo de vida de evidencia candidata

El ciclo de vida describe las etapas desde que se genera un output runtime hasta que puede actuar como evidencia formal:

1. **Origen (L4/L3):** un mecanismo runtime (OpenCode, command candidato, validator candidato, agente conceptual) produce un output. El output nace como candidato con estado `candidate`.
2. **Captura candidata (L3):** el output se retiene con metadatos minimos: identificador logico, origen, seccion relacionada, timestamp conceptual y estado `candidate`. Corresponde a SCH-07.
3. **Validacion de forma (L3):** VAL-05 verifica que la evidencia candidata tiene origen trazable, tipo declarado, resumen verificable y estado `candidate`. Los resultados de esta validacion son a su vez candidatos (L3).
4. **Evaluacion de elegibilidad (L3 → L2):** el responsable o proceso gobernado determina si la evidencia candidata cubre el requisito de un gate, handoff o cierre de seccion. Esta evaluacion requiere decision explicita; no es automatica.
5. **Registro gobernado (L2):** la evidencia es aceptada, documentada con trazabilidad completa y promovida a L2. Solo en este punto puede actuar como soporte formal de gate o cierre.
6. **Referencia autoritativa (L1 actualizado):** si la evidencia registrada cambia el estado operacional (status de seccion, gate, approval), ese cambio se refleja en `project-truth/` (L1). L1 es siempre la vista autoritativa.

Ningun paso del ciclo puede ser automatizado hasta el punto de sustituir la evaluacion de elegibilidad ni el registro gobernado; ambos requieren actor humano o proceso explicito aprobado.

###### 3.4 Logs de estado y transiciones

Los logs de estado y transiciones capturan el historial auditab de cambios operacionales y resultados de validators. No son el estado autoritativo; ese vive en `project-truth/blueprint-state.yaml`:

- **Log de transiciones de estado:** registro append-only de cada transicion de status de seccion o iteracion. Cada entrada incluye: identificador de seccion, status previo, status nuevo, actor/rol conceptual, timestamp conceptual y referencia al validator candidato (VAL-03) que verifico la transicion. Fuente de este log: S09 SCH-03, S10 VAL-03.
- **Log de prerequisitos de gate:** registro append-only de cada evaluacion de prerequisitos de gate. Cada entrada incluye: identificador de gate, checklist de prerequisitos, estado de cada prerequisito (cubierto/faltante), referencia a evidencia candidata y resultado del validator (VAL-04). Fuente: S09 SCH-04, S10 VAL-04.
- **Log de resultados de validators:** registro append-only de resultados de VAL-01..VAL-10 producidos en una sesion o ciclo de trabajo. Cada entrada incluye: ID de validator, input conceptual evaluado, resultado (conforme/alerta), condicion de bloqueo activada si aplica y estado candidato. Fuente: S09 SCH-06/SCH-07, S10 VAL-01..VAL-10.
- **Log de contexto de ejecucion:** registro de context packets usados, secciones trabajadas y gaps detectados en una sesion. Permite auditoria retroactiva sin requerir reproduccion completa de sesion. Fuente: S09 SCH-08.

Todos estos logs son L3 por defecto. Su promocion a L2 requiere registro gobernado. Ningun log sustituye al estado en `blueprint-state.yaml` ni puede modificarlo sin actor humano o proceso aprobado.

###### 3.5 Storage de state autoritativo vs storage de evidencia candidata

Para evitar double work y confusion de autoridad, S11 define limites claros:

| Elemento | Donde vive | Quien lo actualiza | Que es |
| --- | --- | --- | --- |
| Status de seccion (status, owner_approval) | `project-truth/blueprint-state.yaml` | Agentes autorizados con permisos definidos; owner para approvals | Estado autoritativo (L1) |
| Blueprint contract rules | `project-truth/blueprint-contract.yaml` | Owner o proceso gobernado | Estado autoritativo (L1) |
| Historial de transiciones | Log de transiciones (L3, append-only) | Agente autor/fixer con registro candidato | Evidencia candidata (L3) |
| Resultados de validators | Log de resultados de validators (L3) | Validators candidatos | Evidencia candidata (L3) |
| Reportes de autor/fixer/verifier | `reports/blueprint/` (Markdown) | Agentes correspondientes | Evidencia candidata (L3) / registrada (L2 si gates la consumen) |
| Evidencia registrada para gates | Documentos de evidencia Markdown (L2) | Proceso gobernado con registro explicito | Evidencia registrada (L2) |

Regla de no double work: S11 no duplica ni reemplaza `blueprint-state.yaml` ni `blueprint-contract.yaml`. El storage conceptual de S11 cubre el historial auditab y la evidencia candidata, no el estado autoritativo.

###### 3.6 Compatibilidad Git y simplicidad

Todos los tipos de storage conceptuales definidos en S11 deben ser compatibles con Git como sistema de control de versiones, siguiendo AP-09 y DEC-ACCEPTED-146:

- **Texto plano preferido:** Markdown para evidencia legible por humanos; YAML/JSON para estado estructurado; JSONL append-only para logs de historial.
- **Sin binarios ni blobs:** el storage conceptual no incluye artefactos binarios, bases de datos embebidas ni formatos propietarios.
- **Diffs legibles:** cada cambio en el storage autoritativo debe producir un diff Git legible que permita auditoria de quien cambio que y cuando.
- **Sin sobreescritura de historial:** los logs append-only no pueden ser editados retroactivamente sin dejar traza explicita de la correccion y su motivo.
- **Tamanio manejable:** el storage candidato de sesion (L4/L3) no debe acumularse en `project-truth/`; solo evidencia registrada gobernada (L2) puede residir alli permanentemente.

###### 3.7 Integracion con validacion deterministica y source policy

S11 recibe los resultados candidatos de VAL-01..VAL-10 de S10 como insumos de storage. La integracion funciona asi:

- **VAL-03 (Work State Transition):** sus resultados candidatos alimentan el log de transiciones de estado. Un resultado de VAL-03 que detecte una transicion ilegal es una alerta candidata (L3); no bloquea por si sola sin evaluacion gobernada.
- **VAL-04 (Gate Prerequisite):** sus resultados candidatos alimentan el log de prerequisitos de gate. Un checklist de prerequisitos cubiertos de VAL-04 puede actuar como evidencia de soporte para solicitar owner approval, pero no sustituye la decision owner.
- **VAL-05 (Evidence Record):** sus resultados candidatos confirman que una evidencia esta bien formada. Una confirmacion de VAL-05 permite que la evidencia sea elegible para evaluacion de registro gobernado (paso 4 del ciclo de vida).
- **VAL-06 (Deterministic Control Completeness):** sus resultados candidatos confirman que un control deterministico esta completo. Alimentan el log de resultados de validators.
- **Source policy (S12):** S11 no gestiona source policy; delega a S12. Si VAL-01 o VAL-09 detectan fuente no autorizada, el log de resultados de validators registra la alerta candidata y S12 es el mecanismo que gestiona la respuesta.

##### 4. Cross-Section Guidance / Handoff Rules

- **Para S12 Knowledge Base and Source Policy Implementation:** S11 entrega a S12 el modelo de ciclo de vida de evidencia candidata y el log de contexto de ejecucion como insumos para source policy minima y Knowledge Gap. S12 debe usar SCH-08 y SCH-09 para gestionar gaps y Curation Requests sin ampliar fuentes por cuenta propia.
- **Para S13 Odoo 18 Execution Environment:** S11 entrega a S13 el ciclo de vida de evidencia candidata y los tipos de storage compatibles con Git como referencia para definir evidencia del entorno Odoo 18 sin crear entorno ni implementacion. S13 debe registrar evidencia conceptual del entorno bajo los niveles L2/L3 definidos en S11.
- **Para S14 Security and Secrets:** S11 entrega a S14 las categorias logicas de storage de evidencia y estado para que S14 defina controles de acceso y secrets policy a nivel conceptual sin crear vault, permission rules ejecutables ni secrets finales.
- **Para S15 Pilot Module Blueprint:** S11 entrega a S15 el modelo de evidencia candidata para que S15 registre evidencia conceptual del piloto internal requests / simple approvals sin crear PRD, SDD, backlog funcional ni modulo ejecutable.
- **Para S16 Spikes and Technical Validations:** S11 entrega a S16 el log de resultados de validators y las alertas candidatas de VAL-03..VAL-06 como insumos para ordenar validaciones tecnicas futuras sin autocierre.
- **Para S17 Bidirectional Traceability Matrix:** S11 entrega a S17 el modelo de storage de evidencia registrada (L2) como base para la matriz de trazabilidad final. S17 no puede cerrar la matriz por si solo; requiere owner approval.
- **Para S18 Blueprint Outputs to Backlog:** S11 entrega a S18 las categorias de evidencia candidata y registrada como base para las categorias de output de backlog sin crear backlog, PRD, SDD ni implementacion.
- **Para S19 Acceptance Criteria:** S11 entrega a S19 el ciclo de vida de evidencia y los niveles de autoridad como referencia para auditar acceptance criteria sin autocierre ni sustituir owner approval.
- **Restriccion general:** ningun tipo de storage conceptual definido en S11 puede actuar como autoridad de estado, gate o evidencia formal hasta que la evidencia sea promovida a L2 mediante registro gobernado. Los logs y resultados de validators son siempre L3 hasta ese momento.

##### 5. Explicit Non-Decisions

- Esta seccion no crea storage fisico, archivos reales, directorios, rutas finales ni artifacts.
- Esta seccion no crea logs reales, implementacion de logging, schemas de base de datos, tablas, DDL, ORMs ni formatos definitivos.
- Esta seccion no decide toolchain, lenguaje, librerias, sistema de archivos, base de datos, CI/CD ni estructura runtime final.
- Esta seccion no convierte OpenCode en storage final ni en autoridad de evidencia.
- Esta seccion no convierte outputs runtime en evidencia formal; el registro gobernado requiere decision explicita y actor humano o proceso aprobado.
- Esta seccion no crea schemas fisicos, validators reales, scripts, commands, agents ejecutables, skills/playbooks reales, plugins ni MCP.
- Esta seccion no crea RAG/vector base, SDK/server, backlog, PRD, SDD ni implementacion.
- Esta seccion no modifica `blueprint-state.yaml` ni `blueprint-contract.yaml` mas alla de los campos autorizados.
- Esta seccion no cambia source policy minima, owner approval semantics, status semantics ni reglas de governance.
- Esta seccion no expande V1 fuera de Odoo-only, Odoo 18 y piloto de solicitudes internas / aprobaciones simples.
- Esta seccion no usa ni referencia `framework/` como input.
- Esta seccion no decide el formato fisico final de los logs (JSONL, CSV, base de datos, etc.); solo define la categoria conceptual append-only compatible con Git.

##### 6. Open Questions / Owner Decisions

- none

##### 7. Acceptance Criteria

- La seccion queda en `Status: in-verification` para auditoria del verifier, con `Owner approval: not-requested`.
- El diseno conceptual de storage cubre estado autoritativo, logs de transiciones, evidencia candidata y evidencia registrada gobernada sin crear storage fisico, rutas, scripts ni artifacts.
- La jerarquia L1..L4 preserva `project-truth/` como autoridad y trata evidencia runtime como candidata hasta registro gobernado.
- SCH-03, SCH-05 y SCH-07 son usados como base logica del modelo de storage.
- VAL-03, VAL-04, VAL-05 y VAL-06 son integrados como fuentes de evidencia candidata a registrar.
- No hay double work con `blueprint-state.yaml` ni `blueprint-contract.yaml`; los limites entre estado autoritativo y storage de evidencia candidata estan definidos explicitamente.
- Todos los tipos de storage conceptuales son compatibles con Git (AP-09, DEC-ACCEPTED-146).
- Los handoffs a S12-S19 son suficientes para alimentar source policy, evidencia piloto Odoo 18, trazabilidad final, backlog y acceptance criteria.
- La seccion respeta source-vs-runtime de S05, autoridad unica de AP-01, control deterministico de AP-04, gates/evidence de AP-05 y evidencia simple de AP-09.
- La seccion no introduce RAG/vector base, SDK/server core, CI/CD completo, advanced storage, multiuser, post-V1 capabilities, backlog, PRD, SDD ni implementacion.
- La seccion mantiene `framework/` excluido y no reabre CRIT-01..07, TOM ni decisiones aceptadas.
- Explicit non-decisions cubren todos los artefactos prohibidos.

##### 8. Section Output / Handoff

- S11 entrega a S12 el modelo de ciclo de vida de evidencia candidata y el log de contexto de ejecucion como insumos para source policy minima y Knowledge Gap conceptual.
- S11 entrega a S13-S15 los niveles de autoridad de storage (L1..L4) y el ciclo de vida de evidencia como referencia para registrar evidencia conceptual del piloto Odoo 18 sin crear entorno, modulo ni implementacion.
- S11 entrega a S16 el log de resultados de validators y alertas candidatas para ordenar validaciones tecnicas futuras sin autocierre.
- S11 entrega a S17 el modelo de evidencia registrada (L2) como base para la matriz de trazabilidad final.
- S11 entrega a S18 las categorias de evidencia candidata y registrada como base para categorias de output de backlog.
- S11 entrega a S19 el ciclo de vida de evidencia y los niveles de autoridad como referencia para auditar acceptance criteria sin autocierre.

#### 12. Knowledge Base and Source Policy Implementation

Status: closed

Owner approval: approved explicitly by owner.

##### 1. Purpose

S12 define la implementacion conceptual de source policy y knowledge governance para CAFL V1. Su objetivo es operacionalizar la source policy minima establecida por DEC-ACCEPTED-163 (docs.odoo.com + github.com/odoo/odoo), definir el mecanismo conceptual de Knowledge Gap y el flujo de Curation Request, y establecer como la evidencia de source policy se integra con el ciclo de vida de evidencia de S11, todo sin crear RAG/base vectorial, source registry fisico, validators reales, scripts ni implementacion ejecutable.

S12 recibe los triggers de Knowledge Gap (VAL-01 / VAL-09) de S10, el modelo de evidencia candidata de S11 y la definicion logica de SCH-09 de S09, y entrega handoffs conceptuales a S13-S15 (Odoo execution, security, pilot module) y a S16-S19 (spike order, traceability matrix, backlog categories, acceptance criteria).

##### 2. Inputs / Scope

Inputs trazables usados:

- S09 SCH-09 Source Policy / Knowledge Gap Schema: categoria logica que define como se estructuran los metadatos de source policy y knowledge governance. Sirve como modelo logico para authority classification, gap detection y Curation Request metadata. Trazable a CRIT-06, CRIT-07, TOM, AP-01/AP-04/AP-06/AP-09, BR-01, DEC-ACCEPTED-163.
- S10 VAL-01 Authority Source Validator: trigger conceptual de Knowledge Gap cuando detecta fuente no autorizada o sin cumplir criterios de freshness y autoridad. Trazable a CRIT-06, AP-04/AP-06, DEC-ACCEPTED-138/163.
- S10 VAL-09 Source Policy Compliance Validator: trigger conceptual de Knowledge Gap cuando detecta uso de fuente no elegible o gap de source policy no registrado. Trazable a CRIT-06, AP-06/AP-12, DEC-ACCEPTED-163.
- S11 ciclo de vida de evidencia candidata (6 pasos: origen, captura, validacion, evaluacion de elegibilidad, registro gobernado, referencia autoritativa) y jerarquia L1..L4: base logica para almacenar evidencia de source policy bajo los mismos niveles de autoridad.
- S11 log de contexto de ejecucion (SCH-08): insumo para detectar gaps de fuentes en sesiones de trabajo.
- DEC-ACCEPTED-163: source policy minima — docs.odoo.com + github.com/odoo/odoo son las unicas fuentes pre-autorizadas para V1.
- DEC-ACCEPTED-164: RAG/base vectorial diferida a V2; prohibida en V1.
- TOM Knowledge Governance: define Knowledge Gap triggers, Curation Request flow y source policy enforcement como mecanismos gobernados.
- CRIT-06: trazabilidad, control, evidencia y fuentes gobernadas.
- CRIT-07: schemas y validators minimos, no permanentes.
- AP-01: `project-truth/` como fuente unica de verdad; trazabilidad bidireccional.
- AP-04: control deterministico separado del razonamiento LLM.
- AP-06: context routing y source policy enforcement son obligatorios.
- AP-09: evidencia simple, auditable y Git-compatible.
- AP-12: source policy minima y exclusion de fuentes no autorizadas.
- BR-01 (S03): V1 boundary — Odoo-only, Odoo 18, piloto internal requests / simple approvals.

Alcance de S12:

- Definir como la source policy minima se operacionaliza conceptualmente: elegibilidad de fuentes, clasificacion de autoridad, freshness conceptual, deteccion de gaps.
- Definir como funciona el mecanismo conceptual de Knowledge Gap con los triggers VAL-01/VAL-09 y SCH-09.
- Definir el flujo conceptual de Curation Request para adicion de fuentes no pre-autorizadas.
- Definir como la evidencia de source policy se integra con la jerarquia L1..L4 y el ciclo de vida de evidencia de S11.
- Definir handoffs conceptuales a S13-S15 y S16-S19.

Fuera de alcance:

- Crear RAG/base vectorial, embeddings, vector search ni recuperacion semantica.
- Crear source registry fisico, base de datos de fuentes, archivos de configuracion de fuentes ni artifacts reales.
- Crear validators reales, scripts, CLIs, toolchain ejecutable ni implementacion.
- Expandir source policy mas alla de docs.odoo.com + github.com/odoo/odoo sin Curation Request aprobada por owner.
- Implementar tooling de Knowledge Governance; solo disenar conceptualmente los flujos.
- Usar o referenciar el directorio legado excluido como input.
- Expandir V1 fuera de Odoo-only, Odoo 18, piloto internal requests / simple approvals.

##### 3. Conceptual Source Policy and Knowledge Governance Design

El diseno que sigue es logico y conceptual. No define archivos fisicos, rutas finales, formatos definitivos, herramientas ejecutables ni implementacion. Cada categoria puede evolucionar o ser reemplazada tras V1 dado que CRIT-07 exige schemas y validators minimos no permanentes.

###### 3.1 Source Policy Minima — Operacionalizacion conceptual

La source policy minima para CAFL V1 queda fijada por DEC-ACCEPTED-163 en dos fuentes pre-autorizadas:

| Fuente pre-autorizada | Clasificacion de autoridad | Tipo de contenido aplicable | Razon de pre-autorizacion |
| --- | --- | --- | --- |
| docs.odoo.com | Autoridad Odoo oficial — documentacion | Documentacion funcional, API, configuracion, guias Odoo 18 | Fuente oficial de Odoo para el piloto V1 |
| github.com/odoo/odoo | Autoridad Odoo oficial — codigo fuente | Codigo fuente, modulos, estructura de datos Odoo 18 | Repositorio oficial; permite trazabilidad tecnica a implementacion real |

Cualquier otra fuente (internas, terceras partes, community forks, blogs, documentacion externa) es no pre-autorizada. Su uso en componentes V1 requiere Curation Request y aprobacion owner explicita antes de ser utilizada.

Regla fundamental: la source policy minima es inmutable en V1. No puede ampliarse por criterio de agente ni por conveniencia de sesion. Toda expansion requiere el flujo de Curation Request descrito en 3.3.

Trazabilidad: DEC-ACCEPTED-163; AP-06; AP-12; TOM Knowledge Governance; CRIT-06.

###### 3.2 Clasificacion de autoridad de fuentes y freshness conceptual

Para operacionalizar source policy en V1, se definen las siguientes categorias de clasificacion de autoridad de fuentes:

| Categoria | Descripcion | Condicion de elegibilidad | Accion si no cumple |
| --- | --- | --- | --- |
| Pre-autorizada — vigente | Fuente dentro de source policy minima; contenido conceptualmente actual para Odoo 18 | Debe ser docs.odoo.com o github.com/odoo/odoo; referencia debe corresponder a Odoo 18 | Ninguna; fuente elegible |
| Pre-autorizada — version inconsistente | Fuente dentro de source policy minima pero referencia version distinta de Odoo 18 | Mismas fuentes pre-autorizadas pero version incongruente con V1 scope | Alerta de freshness; registrar gap; no bloquear automaticamente sin evaluacion gobernada |
| No pre-autorizada — sin Curation Request | Fuente fuera de source policy minima; sin proceso de Curation Request iniciado | Cualquier fuente distinta a las dos pre-autorizadas | Trigger de Knowledge Gap; iniciar Curation Request si se desea usar |
| No pre-autorizada — con Curation Request pendiente | Fuente fuera de source policy minima; Curation Request iniciada pero aun sin aprobacion owner | Curation Request registrada; decision owner pendiente | No usar fuente hasta aprobacion owner; mantener estado pendiente |
| No pre-autorizada — aprobada por owner | Fuente originalmente fuera de source policy minima; Curation Request aprobada explicitamente por owner | Aprobacion owner registrada en `project-truth/` | Fuente elegible post-aprobacion; trazabilidad requerida |

Concepto de freshness: en V1 el criterio de freshness es conceptual — una referencia es "fresca" si corresponde a Odoo 18 y a las fuentes pre-autorizadas. No hay mecanismo automatico de verificacion de timestamps ni web crawling; VAL-01 detecta inconsistencias de version o autoridad como alertas candidatas (L3), no como bloqueos automaticos.

Trazabilidad: S09 SCH-09; S10 VAL-01; DEC-ACCEPTED-163; AP-06; AP-12; TOM.

###### 3.3 Mecanismo conceptual de Knowledge Gap

El Knowledge Gap es el mecanismo mediante el cual CAFL V1 registra y gestiona situaciones donde una fuente requerida no esta pre-autorizada o donde se detecta un uso de fuente no conforme con source policy minima.

**Triggers de Knowledge Gap:**

- **VAL-01 alerta de fuente no autorizada:** cuando VAL-01 detecta que un componente referencia una fuente fuera de source policy minima o que la fuente pre-autorizada no corresponde a Odoo 18, emite una alerta candidata (L3). Esta alerta es el trigger primario de Knowledge Gap.
- **VAL-09 alerta de gap de source policy:** cuando VAL-09 detecta uso de fuente no elegible o gap de conformidad con source policy, emite una alerta candidata (L3). Esta alerta es el trigger secundario de Knowledge Gap.
- **Log de contexto de ejecucion (SCH-08 / S11):** gaps detectados en sesiones de trabajo donde no habia fuente pre-autorizada disponible para un requerimiento tecnico del piloto Odoo 18 pueden registrarse como Knowledge Gaps en el log de ejecucion.

**Respuesta conceptual al Knowledge Gap:**

1. El trigger (alerta VAL-01 o VAL-09, o gap en log de ejecucion) es capturado como evidencia candidata (L3) bajo SCH-09.
2. Se registra el gap con los metadatos minimos conceptuales: identificador logico, fuente requerida o detectada, tipo de gap (fuente no autorizada / version inconsistente / gap de contenido), referencia al componente V1 afectado, timestamp conceptual, estado `gap-open`.
3. Si el gap corresponde a una fuente no pre-autorizada que se desea utilizar, se inicia el flujo de Curation Request (3.3 → 3.4).
4. Si el gap corresponde a una version inconsistente de fuente pre-autorizada, se registra como alerta candidata y se resuelve mediante evaluacion gobernada (no automatica) que puede confirmar o desestimar el uso sin ampliar source policy.
5. El gap permanece en estado `gap-open` hasta que se resuelva mediante Curation Request aprobada, descarte gobernado o decision owner. La resolucion requiere actor humano o proceso aprobado; no es automatica.
6. La resolucion del gap se registra actualizando el metadato bajo SCH-09 a estado `gap-resolved` o `gap-discarded` con referencia a la decision o Curation Request que lo cerro.

Regla: ningun Knowledge Gap puede ser cerrado automaticamente por agente. La evaluacion de elegibilidad y el registro gobernado requieren decision explicita. Trazabilidad: S09 SCH-09; S10 VAL-01/VAL-09; S11 evidencia L3→L2; TOM Knowledge Governance; CRIT-06; AP-04; AP-06.

###### 3.4 Flujo conceptual de Curation Request

El flujo de Curation Request es el mecanismo gobernado para agregar fuentes no pre-autorizadas a la source policy de CAFL V1. Es un flujo de gobernanza conceptual, no un workflow ejecutable ni un script.

**Pasos conceptuales del flujo:**

1. **Solicitud de curation:** un actor (agente o humano) identifica que necesita usar una fuente fuera de source policy minima. Registra una solicitud con los metadatos conceptuales minimos: fuente candidata, justificacion tecnica (por que se necesita para el piloto V1), componente(s) afectados, tipo de uso previsto. Estado inicial: `curation-requested`.
2. **Gate de aprobacion owner:** la solicitud llega al owner para evaluacion. El owner es el unico actor autorizado para aprobar ampliaciones de source policy. Los criterios de evaluacion son: coherencia con V1 boundary (Odoo-only, Odoo 18, piloto), trazabilidad a CRIT/decision/TOM, ausencia de alternativa en source policy minima, riesgo de scope creep. Este gate no puede ser sustituido por criterio de agente.
3. **Resultado del gate:**
   - Si el owner aprueba: la fuente candidata pasa a estado `curation-approved`; se registra la decision en `project-truth/` con trazabilidad completa; la fuente queda elegible para uso en los componentes declarados.
   - Si el owner rechaza: la fuente candidata pasa a estado `curation-rejected`; el Knowledge Gap asociado pasa a `gap-discarded`; el componente afectado debe adaptarse para usar solo fuentes pre-autorizadas.
4. **Registro y trazabilidad:** toda Curation Request (aprobada o rechazada) queda registrada como evidencia gobernada (L2) bajo SCH-09 con referencia a la decision owner, el componente afectado y el estado final. La trazabilidad es obligatoria; una Curation Request sin registro completo no es valida.
5. **Actualizacion de source policy:** si la Curation Request es aprobada, la ampliacion de source policy se registra en `project-truth/` como estado autoritativo (L1). No se actualiza en runtime ni en artifacts; solo en la fuente de verdad gobernada.

Restriccion critica: este flujo no puede ser acortado ni eludido. Cualquier uso de fuente no pre-autorizada sin Curation Request aprobada es una violacion de source policy minima y debe ser reportada como Knowledge Gap con estado `gap-open` de alta prioridad.

Trazabilidad: DEC-ACCEPTED-163; TOM Knowledge Governance; CRIT-06; AP-01; AP-06; AP-12; S09 SCH-09; S10 VAL-09.

###### 3.5 Integracion con el ciclo de vida de evidencia de S11

La evidencia de source policy se integra con la jerarquia L1..L4 y el ciclo de vida de 6 pasos de S11 de la siguiente manera:

| Elemento de source policy | Nivel S11 inicial | Condicion de promocion | Nivel final posible |
| --- | --- | --- | --- |
| Alerta VAL-01 (fuente no autorizada) | L3 — evidencia candidata | Evaluacion gobernada; registro explicito | L2 si se registra como soporte de gate o Knowledge Gap formal |
| Alerta VAL-09 (gap de source policy) | L3 — evidencia candidata | Evaluacion gobernada; registro explicito | L2 si se registra como soporte de Curation Request |
| Metadato de Knowledge Gap (SCH-09) | L3 — candidato al registrarse el gap | Registro gobernado con decision explicita | L2 una vez resuelto y registrado formalmente |
| Curation Request aprobada | L2 — registrada en `project-truth/` | Ya es evidencia gobernada al aprobarse | L1 si la decision modifica estado autoritativo en `project-truth/` |
| Source policy autoritativa | L1 — `project-truth/` | No requiere promocion; es la fuente aprobada | L1 permanente |

Ciclo de vida de evidencia de source policy (mapeado a los 6 pasos de S11):

1. **Origen:** VAL-01 o VAL-09 producen alerta candidata; o log de ejecucion (SCH-08) detecta gap. Output nace en L3/L4.
2. **Captura candidata:** la alerta o gap se retiene con metadatos SCH-09 en estado `candidate` / `gap-open`.
3. **Validacion de forma:** VAL-05 verifica que el registro de gap tiene origen trazable, tipo declarado y estado `candidate`. Resultado de VAL-05 es a su vez candidato (L3).
4. **Evaluacion de elegibilidad:** el owner o proceso gobernado determina si el gap requiere Curation Request, descarte o aceptacion como riesgo controlado. Esta evaluacion no es automatica.
5. **Registro gobernado:** gap resuelto o Curation Request aprobada se registran como L2. Solo en este punto la evidencia apoya formalmente un gate o decision.
6. **Referencia autoritativa:** si la resolucion modifica source policy (Curation Request aprobada), se actualiza L1 (`project-truth/`). L1 es siempre la vista autoritativa.

Trazabilidad: S11 ciclo de vida 6 pasos; S11 jerarquia L1..L4; S09 SCH-09; S10 VAL-01/VAL-05/VAL-09; AP-01; AP-09; CRIT-06.

##### 4. Cross-Section Guidance / Handoff Rules

- **Para S13 Odoo 18 Execution Environment:** S12 entrega a S13 la source policy minima operacionalizada (docs.odoo.com + github.com/odoo/odoo) y la clasificacion de autoridad de fuentes como restriccion a aplicar en la definicion del entorno conceptual Odoo 18. S13 debe verificar que cualquier referencia a fuentes Odoo 18 cumple source policy antes de usarla como insumo. S13 no puede ampliar source policy por iniciativa propia; si detecta un gap, debe activar el flujo de Knowledge Gap definido en S12.
- **Para S14 Security and Secrets:** S12 entrega a S14 el modelo de Curation Request y Knowledge Gap como patron de gobernanza conceptual aplicable a la gestion de secrets y sources de seguridad. S14 puede modelar la aprobacion de secrets sources bajo el mismo patron de gate owner sin crear vault, permission rules ejecutables ni secrets policy final.
- **Para S15 Pilot Module Blueprint:** S12 entrega a S15 la restriccion explícita de source policy para el piloto internal requests / simple approvals: solo fuentes pre-autorizadas pueden fundamentar decisiones de diseno del modulo piloto. Si el piloto requiere una fuente adicional, debe pasar por Curation Request antes de usarla. S15 no crea PRD, SDD, backlog funcional ni modulo ejecutable.
- **Para S16 Spikes and Technical Validations:** S12 entrega a S16 los Knowledge Gaps sin resolver y las Curation Requests pendientes como insumos para el orden final de spikes. Gaps de fuentes no resueltos pueden generar spikes de validacion de source policy. S16 no cierra gaps por autoridad propia.
- **Para S17 Bidirectional Traceability Matrix:** S12 entrega a S17 los registros de Curation Requests aprobadas y los Knowledge Gaps resueltos como evidencia gobernada (L2) elegible para la matriz de trazabilidad final. S17 no puede cerrar la matriz sin owner approval.
- **Para S18 Blueprint Outputs to Backlog:** S12 entrega a S18 las categorias de Knowledge Gap y Curation Request como categorias de output de backlog para futuros ciclos de gobernanza de fuentes. S18 no crea backlog funcional ni implementacion.
- **Para S19 Acceptance Criteria:** S12 entrega a S19 los criterios de source policy operacionalizados (elegibilidad, freshness conceptual, Knowledge Gap resuelto, Curation Request trazada) como referencia para acceptance criteria de componentes que consumen fuentes externas. S19 no cierra aceptacion final ni sustituye owner approval.
- **Restriccion general:** ningun handoff de S12 autoriza uso de fuentes no pre-autorizadas. Todos los handoffs preservan source policy minima. Knowledge Gaps no resueltos no bloquean automaticamente el avance de secciones futuras, pero deben ser declarados como restriccion heredada en las secciones que los consumen.

##### 5. Explicit Non-Decisions

- Esta seccion no crea RAG, base vectorial, embeddings, vector search ni recuperacion semantica de ningun tipo.
- Esta seccion no crea source registry fisico, base de datos de fuentes, archivos de configuracion de fuentes, APIs de consulta de fuentes ni artifacts ejecutables.
- Esta seccion no crea validators reales, scripts, CLIs, toolchain ejecutable ni implementacion de Knowledge Governance.
- Esta seccion no crea schemas fisicos, JSON Schema, YAML schema, DDL, tablas ni modelos ORM.
- Esta seccion no amplía source policy minima. La adicion de nuevas fuentes queda pendiente de Curation Request y aprobacion owner en ciclos futuros.
- Esta seccion no decide el formato fisico de registros de Knowledge Gap o Curation Request; solo define las categorias logicas bajo SCH-09.
- Esta seccion no instancia VAL-01 ni VAL-09 como validators reales; los usa solo como triggers conceptuales de Knowledge Gap.
- Esta seccion no convierte Knowledge Gap ni Curation Request en workflows ejecutables, BPMN, scripts de aprobacion ni automatizacion.
- Esta seccion no crea web crawlers, scrapers, monitores de freshness automaticos ni mecanismos de ingestion de fuentes.
- Esta seccion no cierra gates, no otorga owner approval, no convierte outputs runtime en autoridad y no cambia status semantics.
- Esta seccion no cambia source policy minima, owner approval semantics, status semantics, iteration gates ni reglas de governance.
- Esta seccion no expande V1 fuera de Odoo-only, Odoo 18 y piloto de solicitudes internas / aprobaciones simples.
- Esta seccion no usa ni referencia el directorio legado excluido como input.
- Esta seccion no genera el orden final de spikes, la matriz de trazabilidad final, los outputs de backlog ni los acceptance criteria finales; esos pertenecen a S16-S19.

##### 6. Open Questions / Owner Decisions

- none

##### 7. Acceptance Criteria

- La seccion queda en `Status: in-verification` para auditoria del verifier, con `Owner approval: not-requested`.
- La source policy minima (DEC-ACCEPTED-163) es respetada: docs.odoo.com + github.com/odoo/odoo son las unicas fuentes pre-autorizadas; cualquier expansion requiere Curation Request y aprobacion owner.
- El mecanismo de Knowledge Gap es descrito conceptualmente (triggers VAL-01/VAL-09, pasos de respuesta, estados gap-open/gap-resolved/gap-discarded) sin implementacion ejecutable.
- El flujo de Curation Request es descrito conceptualmente (solicitud, gate owner, resultado, registro, actualizacion de source policy) sin workflow ejecutable, script ni BPMN.
- La evidencia de source policy se integra con la jerarquia L1..L4 y el ciclo de vida de 6 pasos de S11 de forma coherente y sin contradiccion.
- Ningun elemento de esta seccion crea RAG, base vectorial, source registry fisico, validators reales, scripts ni implementacion.
- Los handoffs a S13-S15 y S16-S19 son suficientes para alimentar Odoo execution, security, pilot module, spike ordering, traceability matrix, backlog categories y acceptance criteria sin cerrar decisiones futuras.
- Todos los componentes son trazables a TOM, CRIT aprobado o decision aceptada (RULE-04 del contrato).
- La seccion respeta la separacion source-vs-runtime de S05, la autoridad unica de AP-01, el control deterministico de AP-04, el context routing/source policy de AP-06, la evidencia simple de AP-09 y la source policy minima de AP-12.
- La seccion no introduce RAG/vector base, SDK/server core, CI/CD completo, advanced storage/DB, multiuser/team, plugins/MCP, broad integrations ni post-V1 capabilities.
- La seccion mantiene el directorio legado excluido y no reabre CRIT-01..07, TOM ni decisiones aceptadas.
- Las explicit non-decisions cubren todos los artefactos prohibidos.

##### 8. Section Output / Handoff

- S12 entrega a S13 la source policy minima operacionalizada y la clasificacion de autoridad de fuentes como restriccion a aplicar en la definicion del entorno conceptual Odoo 18.
- S12 entrega a S14 el patron de gobernanza conceptual de Curation Request / Knowledge Gap como modelo para la gestion de secrets sources.
- S12 entrega a S15 la restriccion de source policy para el piloto: solo fuentes pre-autorizadas pueden fundamentar decisiones de diseno del modulo piloto sin PRD, SDD, backlog funcional ni modulo ejecutable.
- S12 entrega a S16 los Knowledge Gaps sin resolver y las Curation Requests pendientes como insumos para el orden final de spikes de validacion de source policy.
- S12 entrega a S17 los registros de Curation Requests aprobadas y Knowledge Gaps resueltos como evidencia gobernada (L2) elegible para la matriz de trazabilidad final.
- S12 entrega a S18 las categorias de Knowledge Gap y Curation Request como categorias de output de backlog para futuros ciclos de gobernanza de fuentes.
- S12 entrega a S19 los criterios de source policy operacionalizados como referencia para acceptance criteria de componentes que consumen fuentes externas.
- S12 no cierra ninguna decision sobre toolchain, lenguaje, rutas, storage fisico, implementacion de Knowledge Governance ni ampliacion de source policy; esos pertenecen a Curation Requests futuras y fases posteriores con autorizacion explicita del owner.

### Iteration 4 - Ejecucion Odoo y piloto

#### 13. Odoo 18 Execution Environment

Status: closed

Owner approval: approved

##### 1. Purpose

S13 define conceptualmente el entorno de ejecucion Odoo 18 que CAFL V1 necesita para llevar a cabo su ciclo minimo real. Su objetivo es establecer, a nivel conceptual, que componentes, categorias de entorno y requisitos de evidencia son necesarios para que el framework opere sobre Odoo 18 en el contexto del piloto (solicitudes internas / aprobaciones simples), sin crear el entorno fisico, instalar Odoo, ejecutar tests ni crear scripts.

S13 recibe los handoffs conceptuales de S09 (SCH-10 Odoo Pilot Artifact Schema), S10 (VAL-05 Evidence Record Validator, VAL-10 Odoo Pilot Artifact Scope Validator), S11 (jerarquia L1-L4 y ciclo de vida de evidencia candidata) y S12 (source policy minima operacionalizada: docs.odoo.com + github.com/odoo/odoo), y entrega handoffs conceptuales a S14 (Security and Secrets), S15 (Pilot Module Blueprint) y S16 (Spikes and Technical Validations final order).

La razon de existencia de esta seccion en el Blueprint es que el entorno exacto de Odoo 18 (Docker vs venv vs local) no esta decidido — esa decision queda para un spike (conforme TOM-S06, DEC-ACCEPTED-135 y DEC-ACCEPTED-153). Sin embargo, el Blueprint debe definir conceptualmente que tipo de entorno se necesita, cuales son sus componentes logicos, como fluye la evidencia desde ese entorno hacia el modelo de storage de S11, y cuales son las restricciones de V1 que el entorno debe respetar. Esto permite que S14 y S15 avancen con restricciones de entorno bien definidas y que S16 tenga insumos suficientes para ordenar los spikes de validacion tecnica.

##### 2. Inputs / Scope

Inputs trazables usados:

- S09 SCH-10 Odoo Pilot Artifact Schema: modelo logico del artefacto del piloto Odoo 18, que incluye modelos de datos, vistas, ACL, record rules, flujos de trabajo, tests y evidencia asociada. Trazable a CRIT-06, CRIT-07, TOM, BR-01, AP-08, DEC-ACCEPTED-162, DEC-ACCEPTED-163.
- S09 SCH-01 Authority Source Schema: modelo logico para clasificacion de fuentes de autoridad, aplicable a referencias Odoo 18 del entorno. Trazable a CRIT-06, AP-01, AP-06, DEC-ACCEPTED-163.
- S09 SCH-05 Evidence Record Schema: modelo logico de evidencia simple, auditable y Git-compatible. Trazable a AP-09, DEC-ACCEPTED-146.
- S09 SCH-06 Deterministic Control Schema: modelo logico de control deterministico para evidencia de ejecucion del entorno. Trazable a AP-04, CRIT-07.
- S10 VAL-05 Evidence Record Validator: control conceptual que verifica que la evidencia producida en el entorno tiene origen trazable, tipo declarado, resumen verificable y estado candidato. Trazable a AP-09, CRIT-06.
- S10 VAL-10 Odoo Pilot Artifact Scope Validator: control conceptual que verifica que los artefactos del piloto estan dentro de solicitudes internas / aprobaciones simples, referencian fuentes Odoo pre-autorizadas y tienen evidencia y control asociados. Trazable a BR-01, DEC-ACCEPTED-162, DEC-ACCEPTED-163.
- S11 jerarquia L1-L4 y ciclo de vida de evidencia candidata (6 pasos): base logica para registrar evidencia del entorno Odoo 18 bajo los niveles de autoridad apropiados (L2/L3 como candidata, L1 si modifica estado autoritativo). Trazable a AP-09, DEC-ACCEPTED-146.
- S12 source policy minima operacionalizada (docs.odoo.com + github.com/odoo/odoo): restriccion de fuentes aplicable a todas las referencias del entorno conceptual. Trazable a DEC-ACCEPTED-163, AP-06, AP-12.
- DEC-ACCEPTED-135: Odoo target V1 es Odoo 18. La forma exacta del entorno queda para spike/blueprint.
- DEC-ACCEPTED-153: V1 debe ejecutar y evidenciar un ciclo minimo real en Odoo 18. Incluye install/update/test execution y captura de evidencia; entorno exacto para spike/blueprint.
- DEC-ACCEPTED-162: piloto V1 = solicitudes internas / aprobaciones simples. Restriccion de scope de la ejecucion en el entorno.
- DEC-ACCEPTED-163: source policy minima — docs.odoo.com + github.com/odoo/odoo son las unicas fuentes pre-autorizadas para V1.
- TOM (lineas 184, 248-255, 362, 371, 379, 388): entorno Odoo 18 exacto no definido; spike requirement. Piloto real, acotado, Odoo 18, con modelos/vistas/ACL/record rules/workflow/reglas/tests/docs/evidencia, sin integracion externa compleja por defecto.
- BR-01 (S03): V1 boundary — Odoo-only, Odoo 18, piloto internal requests / simple approvals. Restriccion fundamental que el entorno debe respetar.
- AP-08: V1 minimo suficiente y anti-scope-creep. RAG, SDK/server, dashboard/UI, CI/CD, DB avanzada, multiusuario, plugins/MCP, curacion avanzada, integraciones reales fuera de core V1.
- AP-09: evidencia simple, auditable y Git-compatible.
- RISK-059: falta de entorno Odoo 18 — critical. Entorno exacto (Docker/venv/local) debe decidirse en spike. Sin entorno no hay ejecucion ni evidencia real.
- RISK-010: verificacion no reproducible — high. Commands/logs/entorno Odoo por materializar en Blueprint/spikes.

Alcance de S13:

- Definir conceptualmente las categorias de entorno necesarias para CAFL V1 (sin instanciarlas).
- Describir los componentes logicos del entorno Odoo 18 para el piloto.
- Definir como la evidencia del entorno se integra con la jerarquia L1-L4 de S11.
- Describir la relacion conceptual del entorno con S14 (security y secrets) y S15 (piloto).
- Establecer que significan SCH-10, VAL-05 y VAL-10 para la evidencia del entorno.
- Declarar dependencias de validacion para el spike de entorno (S16).

Fuera de alcance:

- Instalar Odoo, crear entorno fisico, ejecutar tests ni crear scripts.
- Decidir el entorno exacto (Docker vs venv vs local); eso es decision de spike.
- Crear PRD, SDD ni backlog funcional del piloto.
- Reabrir la seleccion del piloto (DEC-ACCEPTED-162 cerrado).
- Ampliar source policy (docs.odoo.com + github.com/odoo/odoo solamente).
- Crear schemas fisicos, validators reales, agents ejecutables, runtime ni implementacion.
- Usar o referenciar `framework/` como input.
- Expandir V1 fuera de Odoo-only, Odoo 18, solicitudes internas / aprobaciones simples.

##### 3. Conceptual Odoo 18 Execution Environment Design

El diseno que sigue es logico y conceptual. No define un entorno fisico, no instala Odoo, no ejecuta comandos, no crea rutas finales ni determina herramientas. El entorno exacto (Docker, venv, local) queda abierto para el spike correspondiente, conforme DEC-ACCEPTED-135, DEC-ACCEPTED-153 y RISK-059.

###### 3.1 Categorias conceptuales de entorno

Para CAFL V1, el entorno Odoo 18 se clasifica en tres categorias conceptuales. Estas categorias son logicas, no fisicas; su realizacion exacta depende del spike de entorno (S16):

| Categoria conceptual | Proposito en V1 | Alcance del piloto | Relacion con evidencia | Condicion de avance |
| --- | --- | --- | --- | --- |
| Entorno de desarrollo conceptual | Permite la construccion iterativa del modulo piloto (solicitudes internas / aprobaciones simples) con Odoo 18 instalado y funcional | Solo piloto V1; sin integraciones externas complejas | Outputs de construccion son evidencia candidata (L3); no autoritativos hasta registro gobernado | Requiere decision de spike sobre forma exacta (Docker/venv/local) |
| Entorno de validacion conceptual | Permite ejecutar el ciclo minimo real de DEC-ACCEPTED-153: install, update, test execution y captura de evidencia | Solo piloto V1; resultados de tests y logs de ejecucion capturados como evidencia candidata | Resultados de tests y logs son evidencia candidata (L3); elegibles para L2 si pasan registro gobernado | Mismo requisito de spike; ejecucion real no puede ocurrir sin entorno decidido |
| Entorno de referencia de autoridad | Permite verificar trazabilidad tecnica del piloto hacia codigo fuente Odoo 18 oficial | Solo lectura de github.com/odoo/odoo; no ejecuta ni modifica codigo fuente Odoo | Registros de trazabilidad son evidencia candidata (L3) bajo SCH-01 y SCH-10 | Source policy minima (DEC-ACCEPTED-163) determina fuentes elegibles |

Estas tres categorias conceptuales son necesarias para cumplir DEC-ACCEPTED-153 (ciclo minimo real con evidencia) y BR-01 (Odoo-only, Odoo 18, piloto acotado). No se instancian en esta seccion; su materializacion depende del spike de entorno.

Trazabilidad: DEC-ACCEPTED-135; DEC-ACCEPTED-153; BR-01; TOM (lineas 248-255); RISK-059; AP-08.

###### 3.2 Componentes logicos del entorno Odoo 18

Los componentes logicos describen que elementos necesita el entorno Odoo 18 para que el ciclo minimo real sea posible. No son implementacion ni prescripcion de herramientas:

| Componente logico | Descripcion conceptual | Obligatorio para V1 | Restriccion aplicable | Referencia |
| --- | --- | --- | --- | --- |
| Instancia Odoo 18 | Una instalacion funcional de Odoo 18 en cualquier forma que el spike decida (Docker, venv, local). Debe soportar el modulo piloto. | Si — sin instancia no hay ejecucion real (DEC-ACCEPTED-153) | Solo Odoo 18; ninguna version anterior ni posterior en V1 | DEC-ACCEPTED-135; BR-01 |
| Base de datos PostgreSQL | Instancia de PostgreSQL compatible con Odoo 18 para persistencia del modulo piloto. Forma exacta (local, contenedor) queda para spike. | Si — Odoo requiere PostgreSQL | Solo para piloto V1; sin schemas de produccion ni datos reales de clientes | TOM linea 248-255; RISK-059 |
| Modulo piloto instalado | El modulo Odoo 18 del piloto (solicitudes internas / aprobaciones simples) instalado y funcional en la instancia. Diseñado en S15. | Si — es el artefacto ejecutable del piloto V1 | Scope limitado a DEC-ACCEPTED-162; sin integraciones externas complejas | DEC-ACCEPTED-162; SCH-10; VAL-10 |
| Mecanismo de ejecucion de tests | Forma conceptual de ejecutar los tests del modulo piloto (test runner de Odoo o equivalente). Herramienta exacta queda para spike. | Si — DEC-ACCEPTED-153 requiere test execution con evidencia | Solo tests del piloto; no suite completa de Odoo | DEC-ACCEPTED-153; VAL-10 |
| Mecanismo de captura de evidencia | Forma conceptual de capturar outputs de ejecucion (logs de tests, resultados de install/update, snapshots de estado) como evidencia candidata. | Si — DEC-ACCEPTED-153 requiere evidencia del ciclo minimo | Evidencia candidata (L3); requiere registro gobernado para ser L2 | S11 L3-L2; VAL-05; SCH-05 |
| Trigger de ejecucion conceptual | Mecanismo conceptual para iniciar el ciclo minimo (install, update, test execution). Forma exacta (CLI, script, comando Odoo) queda para spike. | Si — ciclo minimo no se ejecuta sin trigger | No crea scripts ni commands reales en esta seccion | DEC-ACCEPTED-153; RISK-010 |
| Referencia de codigo fuente Odoo 18 | Acceso conceptual a github.com/odoo/odoo para verificacion de trazabilidad tecnica del modulo piloto. Solo lectura. | Si — trazabilidad tecnica requerida por source policy | Solo github.com/odoo/odoo; no forks, community ni terceros | DEC-ACCEPTED-163; SCH-01; VAL-10 |

Ningun componente logico es implementado ni creado en esta seccion. Cada uno tiene una forma exacta que debe decidirse en el spike de entorno. Lo que S13 establece es que estos componentes son necesarios conceptualmente para que V1 sea viable.

Trazabilidad: DEC-ACCEPTED-135; DEC-ACCEPTED-153; DEC-ACCEPTED-162; DEC-ACCEPTED-163; BR-01; TOM; SCH-10; VAL-05; VAL-10; RISK-059; RISK-010.

###### 3.3 Flujo de evidencia desde el entorno hacia la jerarquia L1-L4 de S11

La evidencia que produce el entorno Odoo 18 durante el ciclo minimo real debe integrarse con la jerarquia L1-L4 y el ciclo de vida de 6 pasos definidos en S11. Esta integracion es conceptual; no crea mecanismos reales ni flujos ejecutables:

| Evento de entorno | Tipo de evidencia generada | Nivel S11 inicial | Condicion de promocion | Schema/Validator aplicable |
| --- | --- | --- | --- | --- |
| Instalacion del modulo piloto | Log de instalacion, resultado de install (exito/error, dependencias resueltas) | L3 — evidencia candidata | Evaluacion gobernada; registro explicito con trazabilidad | SCH-05 (Evidence Record); VAL-05 (Evidence Record Validator) |
| Actualizacion del modulo piloto | Log de actualizacion, resultado de update, estado de la instancia | L3 — evidencia candidata | Evaluacion gobernada; registro explicito | SCH-05; VAL-05 |
| Ejecucion de tests del piloto | Resultados de test runner (tests pasados/fallidos, cobertura conceptual, logs) | L3 — evidencia candidata | Evaluacion gobernada; registro explicito; puede apoyar gate si se promociona a L2 | SCH-05; SCH-06; SCH-10; VAL-05; VAL-10 |
| Verificacion de scope del piloto | Resultado de VAL-10 (piloto dentro de solicitudes internas / aprobaciones simples, fuentes pre-autorizadas, evidencia asociada) | L3 — evidencia candidata | Evaluacion gobernada | SCH-10; VAL-10 |
| Trazabilidad a codigo fuente | Referencia verificada a github.com/odoo/odoo para componente del modulo piloto | L3 — evidencia candidata | Evaluacion gobernada; puede apoyar acceptance criteria si se promociona a L2 | SCH-01; VAL-01 (Authority Source) |
| Snapshot de estado del entorno | Estado logico del entorno al momento de una ejecucion (version Odoo, modulos instalados, resultado general) | L3 — evidencia candidata | Evaluacion gobernada; solo si cubre requisito de gate o handoff | SCH-07 (Runtime Output/Candidate Evidence); VAL-05 |

Regla de autoridad aplicada al entorno: ningun output del entorno Odoo 18 puede actuar como evidencia formal de gate, handoff ni cierre de seccion sin haber pasado por el ciclo de vida de S11 (L3 → L2 mediante registro gobernado). `project-truth/` (L1) no es sustituida por outputs del entorno.

Trazabilidad: S11 jerarquia L1-L4; S11 ciclo de vida 6 pasos; SCH-05; SCH-06; SCH-07; SCH-10; VAL-05; VAL-10; AP-09; DEC-ACCEPTED-146.

###### 3.4 Restricciones de source policy aplicadas al entorno

El entorno Odoo 18 conceptual debe operar dentro de la source policy minima definida por DEC-ACCEPTED-163 y operacionalizada en S12. Las restricciones son:

- **Fuentes pre-autorizadas unicamente:** toda referencia tecnica usada para construir, configurar o validar el entorno debe tener como origen docs.odoo.com o github.com/odoo/odoo. Ninguna otra fuente es elegible sin Curation Request aprobada por owner.
- **Version Odoo 18 obligatoria:** toda referencia tecnica debe corresponder a Odoo 18. Referencias a versiones anteriores (Odoo 16, 17) o posteriores no son elegibles en V1. VAL-01 detectara inconsistencias de version como alertas candidatas (L3) bajo el mecanismo de S12.
- **Gaps de source policy en el entorno:** si durante el spike de entorno o la elaboracion de S15 (Pilot Module Blueprint) se detecta que se necesita una fuente no pre-autorizada para alguna decision tecnica del entorno, debe activarse el flujo de Knowledge Gap definido en S12 (VAL-09 trigger → Curation Request → aprobacion owner). S13 no puede ampliar source policy por iniciativa propia.
- **`framework/` excluido:** ninguna referencia al directorio legado excluido puede usarse como input para el entorno conceptual ni para el modulo piloto.

Trazabilidad: DEC-ACCEPTED-163; S12 source policy minima; S10 VAL-01; S10 VAL-09; AP-06; AP-12; RULE-10.

###### 3.5 Relacion entre el entorno y el piloto (S15)

El entorno Odoo 18 conceptual es el sustrato de ejecucion del piloto V1. La relacion entre S13 y S15 es:

- S13 define los componentes logicos del entorno que S15 asumira disponibles para el modulo piloto. S15 no debe redefinir el entorno; lo consume como restriccion heredada.
- S15 (Pilot Module Blueprint) diseñara los artefactos del modulo piloto (modelos de datos, vistas, ACL, record rules, flujo de trabajo, tests) dentro de los limites de DEC-ACCEPTED-162 (solicitudes internas / aprobaciones simples) y asumira que el entorno provee una instancia Odoo 18 funcional con PostgreSQL.
- SCH-10 (Odoo Pilot Artifact Schema de S09) es el modelo logico que conecta los artefactos de S15 con la evidencia del entorno de S13. VAL-10 verifica el scope del piloto; VAL-05 verifica la forma de la evidencia.
- S13 no diseña el modulo piloto ni crea PRD, SDD ni backlog funcional. Ese trabajo pertenece a S15.
- La forma exacta de como el entorno ejecuta el modulo piloto (comandos de instalacion, test runner, triggers) queda para el spike de entorno y para la implementacion real; S13 y S15 solo establecen restricciones y requisitos conceptuales.

Trazabilidad: DEC-ACCEPTED-162; SCH-10; VAL-05; VAL-10; BR-01; TOM (lineas 248-255); AP-08.

###### 3.6 Relacion entre el entorno y seguridad (S14)

El entorno Odoo 18 conceptual implica requisitos de seguridad y manejo de secrets que S14 debe abordar. La relacion entre S13 y S14 es:

- S13 identifica los componentes logicos del entorno que tienen implicaciones de seguridad: instancia Odoo 18 (credenciales de administrador), base de datos PostgreSQL (credenciales de acceso), mecanismo de ejecucion de tests (posible acceso a logs con datos sensibles), referencias a github.com/odoo/odoo (tokens de acceso si aplica).
- S13 no define controles de seguridad ni politicas de secrets. Ese trabajo pertenece a S14.
- S14 recibe de S13 la descripcion conceptual de los componentes del entorno para modelar los controles de acceso y secrets policy a nivel conceptual sin crear vault, permission rules ejecutables ni secrets finales.
- RISK-059 (falta de entorno Odoo 18) implica que los controles de seguridad de S14 deben diseñarse para ser aplicables a cualquier forma que el entorno tome (Docker, venv, local), no para una implementacion especifica.

Trazabilidad: RISK-059; TOM; AP-08; DEC-ACCEPTED-153.

###### 3.7 Dependencias de validacion para el spike de entorno

S13 identifica las dependencias de validacion tecnica que el spike de entorno (a ordenar en S16) debe resolver. Estas son las preguntas tecnicas abiertas que bloquean la materializacion real del entorno:

| Dependencia de validacion | Descripcion | Riesgo relacionado | Requisito de evidencia |
| --- | --- | --- | --- |
| Forma exacta del entorno | Decidir si el entorno Odoo 18 usa Docker, venv local, instalacion nativa u otra forma. Impacta reproducibilidad y portabilidad. | RISK-059 (critical) | El spike debe producir evidencia candidata (L3) de que la forma elegida permite install, update y test execution completos del piloto |
| Compatibilidad de la base de datos | Verificar que la instancia PostgreSQL elegida es compatible con los modulos del piloto Odoo 18. | RISK-059; RISK-010 | El spike debe producir evidencia candidata de install exitoso con base de datos |
| Test runner de Odoo 18 | Validar que el mecanismo de ejecucion de tests de Odoo 18 funciona en el entorno elegido y produce resultados capturables como evidencia. | RISK-010 (high) | El spike debe producir log de tests con al menos un test del piloto ejecutado y resultado candidato a L3 |
| Captura de evidencia del ciclo minimo | Verificar que los outputs del entorno (logs de install, update, test) pueden capturarse, retenerse y procesarse bajo el modelo de evidencia de S11 (L3, VAL-05, SCH-05). | RISK-010; AP-09 | El spike debe producir al menos un artefacto de evidencia candidata bien formada bajo VAL-05 |
| Trazabilidad de codigo fuente | Verificar que las referencias a github.com/odoo/odoo para el modulo piloto son alcanzables y corresponden a Odoo 18. | DEC-ACCEPTED-163; RISK-010 | El spike debe confirmar acceso a github.com/odoo/odoo y trazabilidad a la version correcta |

Ninguna de estas dependencias puede ser resuelta conceptualmente; requieren el spike de entorno con ejecucion real. S13 las declara para que S16 las incluya en el orden de spikes con la prioridad correspondiente.

Trazabilidad: RISK-059; RISK-010; DEC-ACCEPTED-135; DEC-ACCEPTED-153; DEC-ACCEPTED-163; AP-09; S11; VAL-05; SCH-05.

##### 4. Cross-Section Guidance / Handoff Rules

- **Para S14 Security and Secrets:** S13 entrega a S14 la descripcion conceptual de los componentes logicos del entorno (instancia Odoo 18, PostgreSQL, trigger de ejecucion, mecanismo de captura de evidencia) como insumo para definir controles de seguridad y secrets policy a nivel conceptual. S14 debe modelar controles aplicables a cualquier forma del entorno sin crear vault, permission rules ejecutables ni secrets finales.
- **Para S15 Pilot Module Blueprint:** S13 entrega a S15 las categorias conceptuales de entorno, los componentes logicos del entorno, las restricciones de source policy (docs.odoo.com + github.com/odoo/odoo), el modelo de evidencia del entorno (L1-L4, ciclo de vida de S11, SCH-10, VAL-05, VAL-10) y las restricciones del piloto (DEC-ACCEPTED-162: solicitudes internas / aprobaciones simples). S15 asume el entorno logico como disponible y diseña los artefactos del modulo piloto sin redefinir el entorno ni crear PRD, SDD, backlog funcional ni modulo ejecutable.
- **Para S16 Spikes and Technical Validations:** S13 entrega a S16 las cinco dependencias de validacion del spike de entorno (forma exacta, compatibilidad DB, test runner, captura de evidencia, trazabilidad de codigo fuente) como insumos prioritarios para el orden final de spikes. RISK-059 (critical) posiciona el spike de entorno como bloqueante de la ejecucion real del piloto. S16 no puede cerrar estas dependencias por autoridad propia; requiere spike de ejecucion real.
- **Para S17 Bidirectional Traceability Matrix:** S13 entrega a S17 el mapa de componentes logicos del entorno y su trazabilidad a DEC-ACCEPTED-135, DEC-ACCEPTED-153, DEC-ACCEPTED-162, DEC-ACCEPTED-163, BR-01, TOM, SCH-10, VAL-05 y VAL-10 como base para la matriz bidireccional del entorno Odoo 18.
- **Para S19 Acceptance Criteria:** S13 entrega a S19 las dependencias de validacion del spike de entorno como criterios de aceptacion candidatos para el componente de entorno Odoo 18 en V1. S19 no puede cerrar acceptance criteria del entorno sin evidencia gobernada del spike correspondiente (L2).
- **Restriccion general:** ningun handoff de S13 crea el entorno fisico, instala Odoo, ejecuta comandos ni crea scripts. Todo handoff es conceptual y su materializacion depende del spike de entorno y de los ciclos de implementacion con autorizacion explicita del owner.

##### 5. Explicit Non-Decisions

- Esta seccion no instala Odoo 18 ni crea ninguna instancia real de entorno Odoo.
- Esta seccion no decide si el entorno Odoo 18 usara Docker, venv, instalacion nativa u otra forma; esa decision pertenece al spike de entorno (S16).
- Esta seccion no crea schemas fisicos, JSON Schema, YAML schema, DDL, tablas ni modelos ORM para el entorno o el piloto.
- Esta seccion no crea validators reales, scripts, CLIs, commands, toolchain ejecutable ni implementacion de entorno.
- Esta seccion no crea el modulo piloto ni ninguno de sus artefactos ejecutables (modelos de datos Odoo, vistas, ACL, record rules, flujos de trabajo, tests, datos de prueba).
- Esta seccion no crea PRD final, SDD final ni backlog funcional del piloto.
- Esta seccion no reabre la seleccion del piloto; DEC-ACCEPTED-162 (solicitudes internas / aprobaciones simples) esta cerrado y es restriccion no negociable.
- Esta seccion no amplia source policy minima; docs.odoo.com + github.com/odoo/odoo son las unicas fuentes pre-autorizadas; cualquier ampliacion requiere Curation Request y aprobacion owner.
- Esta seccion no ejecuta tests del piloto ni captura evidencia real del ciclo minimo; eso requiere el entorno fisico materializado por el spike.
- Esta seccion no define controles de seguridad, secrets policy, vault, tokens, certificados ni configuraciones de seguridad; ese trabajo pertenece a S14.
- Esta seccion no crea RAG/base vectorial, SDK/server, dashboard/UI, CI/CD completo, base de datos avanzada, operacion multiusuario, plugins/MCP ni integraciones externas fuera de core V1.
- Esta seccion no convierte outputs runtime en evidencia formal; el registro gobernado (L3 → L2) requiere decision explicita y actor humano o proceso aprobado.
- Esta seccion no modifica `blueprint-state.yaml` ni `blueprint-contract.yaml` mas alla de los campos autorizados.
- Esta seccion no cambia source policy minima, owner approval semantics, status semantics ni reglas de governance.
- Esta seccion no usa ni referencia `framework/` como input.
- Esta seccion no genera el orden final de spikes, la matriz de trazabilidad final, los outputs de backlog ni los acceptance criteria finales; esos pertenecen a S16-S19.

##### 6. Open Questions / Owner Decisions

- none

##### 7. Acceptance Criteria

- La seccion queda en `Status: in-verification` para auditoria del verifier, con `Owner approval: not-requested`.
- El diseño conceptual del entorno Odoo 18 cubre las tres categorias logicas (desarrollo, validacion, referencia de autoridad) sin crear ninguna instancia fisica, script ni artefacto ejecutable.
- Los siete componentes logicos del entorno estan identificados y trazados a DEC-ACCEPTED-135, DEC-ACCEPTED-153, DEC-ACCEPTED-162, DEC-ACCEPTED-163, BR-01, SCH-10, VAL-05 y VAL-10.
- El flujo de evidencia desde el entorno hacia la jerarquia L1-L4 de S11 esta definido para todos los eventos relevantes del ciclo minimo (instalacion, actualizacion, tests, verificacion de scope, trazabilidad).
- Las restricciones de source policy de S12 estan aplicadas al entorno: solo docs.odoo.com + github.com/odoo/odoo, solo Odoo 18.
- Las dependencias de validacion del spike de entorno estan identificadas (cinco dependencias) con su riesgo relacionado y requisito de evidencia candidata.
- Los handoffs a S14 (seguridad/secrets), S15 (piloto), S16 (spikes), S17 (trazabilidad), S19 (acceptance criteria) son suficientes para alimentar esas secciones sin crear implementacion.
- La seccion respeta BR-01 (Odoo-only, Odoo 18, solicitudes internas / aprobaciones simples) y AP-08 (V1 minimo suficiente, anti-scope-creep).
- La seccion no introduce RAG/vector base, SDK/server core, dashboard productizado, CI/CD completo, advanced storage/DB, multiuser/team operation, plugins/MCP, broad integrations ni post-V1 capabilities.
- Todos los componentes son trazables a TOM, CRIT aprobado o decision aceptada (RULE-04).
- Las explicit non-decisions cubren todos los artefactos prohibidos.
- RISK-059 y RISK-010 estan declarados como riesgos activos que el spike de entorno debe resolver.

##### 8. Section Output / Handoff

- S13 entrega a S14 los componentes logicos del entorno (instancia Odoo 18, PostgreSQL, trigger de ejecucion, captura de evidencia) como insumo para definir conceptualmente controles de seguridad y secrets policy sin crear vault ni secretos reales.
- S13 entrega a S15 las categorias de entorno, componentes logicos, restricciones de source policy, modelo de evidencia (L1-L4, SCH-10, VAL-05, VAL-10) y restricciones del piloto (DEC-ACCEPTED-162) como base para el Blueprint del modulo piloto sin PRD, SDD, backlog ni modulo ejecutable.
- S13 entrega a S16 las cinco dependencias de validacion del spike de entorno — forma exacta (Docker/venv/local), compatibilidad DB, test runner Odoo 18, captura de evidencia ciclo minimo, trazabilidad de codigo fuente — como insumos prioritarios para el orden final de spikes con RISK-059 como bloqueante critico.
- S13 entrega a S17 el mapa de componentes logicos del entorno con su trazabilidad completa a decisiones, schemas y validators como base para la matriz bidireccional del entorno Odoo 18.
- S13 entrega a S19 las dependencias de validacion del spike de entorno como criterios de aceptacion candidatos para el componente de entorno Odoo 18 en V1.
- S13 no cierra ninguna decision sobre toolchain, forma del entorno, lenguaje, CI/CD, implementacion del entorno ni forma del piloto; esos pertenecen al spike de entorno y a fases posteriores con autorizacion explicita del owner.

#### 14. Security and Secrets

Status: closed

Owner approval: approved explicitly by owner.

##### 14.1 Purpose

This section establishes a **conceptual security and secrets model** for CAFL V1 in the context of the Odoo 18 execution environment defined in S13. It identifies the logical security control areas, secrets handling posture, permissions model, and evidence protection requirements needed by the minimum end-to-end Odoo 18 pilot flow — without creating real secrets, tokens, certificates, configurations, or executable policies.

This section feeds:
- **S15** — security constraints and secrets handling posture as inputs to the Pilot Module Blueprint.
- **S16** — security spike dependencies for final spike ordering.

**Explicit non-goals of this section:** No vault, no real secrets, no permission rules, no executable policies, no scripts, no runtime artifacts, no PRD, no SDD, no backlog, no implementation.

##### 14.2 Scope and Inherited Constraints

S14 applies to CAFL V1 boundary only: Odoo-only, Odoo 18, internal requests / simple approvals pilot, minimal source policy. The following inherited constraints govern the full section:

| Constraint | Source | Implication for S14 |
|---|---|---|
| RULE-04 | Blueprint contract | Every security component must trace to TOM, approved CRIT, or accepted decision. No unbacked component. |
| RULE-09 | Blueprint contract | No runtime, executable agents, real commands, physical schemas, real validators, scripts, RAG/vector base, or implementation. |
| RULE-10 | Blueprint contract | `framework/` excluded as input or reference. |
| AP-10 | Architecture Principles (S02) | Security, risk, compliance, secrets, and data are cross-cutting criteria; maintain triage in all gates; escalate critical risks. |
| AP-11 | Architecture Principles (S02) | Uncertain physical/runtime choices (secrets handling, permissions) require spikes, not assumptions. |
| AP-12 | Architecture Principles (S02) | Design is greenfield from `project-truth/`; `framework/` excluded. |
| BR-01 | V1 Boundary (S03) | V1 core only if backed by TOM/CRIT/accepted decision and necessary for minimum pilot flow. |
| S05 source-vs-runtime | S05 | Security and permissions restrictions define what requires later runtime validation; no final rules, vault, real secrets, or configuration here. |
| S11 L1-L4 hierarchy | S11 | Security evidence must follow L1=authoritative, L2=governed registered, L3=candidate, L4=ephemeral. |
| S11 6-step lifecycle | S11 | Security evidence follows: origin → capture → validation → eligibility → governed registration → authoritative reference. |
| S12 source policy | S12 | docs.odoo.com + github.com/odoo/odoo only; no auto-expansion; Curation Request for any expansion. |
| S13 logical components | S13 | Odoo 18 instance, PostgreSQL, installed pilot module, test execution mechanism, evidence capture mechanism, conceptual execution trigger, Odoo 18 source reference. Three environment categories: development, validation, authority reference. |

##### 14.3 Conceptual Security Control Areas

Security controls in CAFL V1 are organized into **four conceptual control areas**. These are logical categories only; no runtime implementation or executable policy is defined here.

###### 14.3.1 Control Area 1 — Secrets Handling Posture

**Definition:** The conceptual model for how secrets (credentials, tokens, API keys, database passwords, service accounts) are categorized and protected within the CAFL V1 Odoo 18 environment — without creating or storing any actual secrets.

**Conceptual posture elements:**

1. **Secret categories identified (conceptual):** Database credentials (PostgreSQL), Odoo administrative credentials, test execution credentials, evidence capture access credentials. These are category names only; no actual values, tokens, or credentials are defined here.

2. **Separation principle:** Secrets must be conceptually separated by environment category (development, validation, authority reference) as established in S13. A secret used in development must not cross into validation or authority reference categories without explicit owner approval.

3. **Non-embedding principle:** Secrets must not be embedded in source artifacts, evidence records, schemas, or validator definitions. This principle applies to `project-truth/` artifacts, pilot module source, and all evidence produced under S11's 6-step lifecycle.

4. **Spike dependency:** The concrete mechanism for secrets storage and injection (environment variables, secrets manager, vault, .env files) is a **spike dependency for S16** (Spike: Secrets Handling Mechanism). The choice depends on the environment form resolved by S13's spike on exact environment form (Docker/venv/local). No assumption is made here; see Section 14.7.

5. **Traceability:** RISK-021 (secrets leakage), RISK-061 (secrets in Odoo), AP-10, DEC-ACCEPTED-045, TOM security/risk section.

###### 14.3.2 Control Area 2 — Permissions and Access Model

**Definition:** The conceptual model for what permissions are needed by which logical components to execute the minimum Odoo 18 pilot flow, without defining actual permission rules, roles, or access control lists.

**Conceptual model elements:**

1. **Logical permission surfaces identified:** Odoo 18 instance administrative access, PostgreSQL connection access, pilot module installation access, test execution access, evidence capture write access. These are logical categories derived from S13's seven logical components.

2. **Principle of minimal surface:** Each logical component should require only the minimum access needed for its role in the pilot flow. This principle is conceptual and guides spike validation; it is not an executable policy here.

3. **Owner approval gate:** Permissions that cross environment boundaries or grant administrative-level access to production-equivalent data require explicit owner approval before implementation, consistent with CRIT-03 (owner approval for critical gates) and AP-10.

4. **Framework exclusion:** No permissions model derives from or references `framework/` artifacts (RULE-10, AP-12).

5. **Spike dependency:** The concrete permissions model — specific roles, ACL definitions, Odoo module-level access rights — is a **spike dependency for S16** (Spike: Permissions Model). See Section 14.7.

6. **Traceability:** RISK-027 (permissions), AP-10, AP-11, CRIT-02, CRIT-03, DEC-ACCEPTED-059, DEC-ACCEPTED-076, TOM security/owner-approval section.

###### 14.3.3 Control Area 3 — Evidence Protection

**Definition:** The conceptual model for protecting the integrity and authority of evidence produced by the Odoo 18 execution environment under S11's L1-L4 hierarchy and 6-step lifecycle.

**Conceptual model elements:**

1. **Evidence authority levels (from S11):** L1 = `project-truth/` authoritative; L2 = governed registered evidence; L3 = candidate evidence; L4 = ephemeral. Security controls must be calibrated to protect L1 and L2 evidence above all, as these feed authoritative reference decisions.

2. **Evidence integrity principle:** Evidence records produced by the evidence capture mechanism (S13 logical component) must not be modified after capture without producing a new governed registration event. Tampering with L2-registered evidence without a new lifecycle event is a security violation at the conceptual level.

3. **Non-embedding principle (evidence):** Evidence records must not contain embedded secrets, credentials, or personally identifiable information. This applies to all evidence flowing through SCH-05, SCH-06, SCH-10, VAL-05, and VAL-10 (S13 environment events).

4. **Source policy protection:** Evidence derived from Odoo 18 source (docs.odoo.com + github.com/odoo/odoo only, per S12) must maintain source attribution. Evidence that loses source attribution cannot be registered as L2 governed evidence.

5. **Curation Request as security gate:** Any proposed expansion of evidence sources beyond the S12 minimal source policy must pass through the Curation Request governance pattern established in S12. This applies to evidence sourced for security validations as well as functional validations.

6. **Traceability:** S11 (L1-L4, 6-step lifecycle), S12 (source policy, Curation Request), S13 (evidence capture mechanism, SCH-10, VAL-05, VAL-10), RISK-021, RISK-061, CRIT-04, DEC-ACCEPTED-163.

###### 14.3.4 Control Area 4 — Security and Risk Triage in Gates

**Definition:** The conceptual model for how security and risk concerns are evaluated at each Blueprint gate, including the escalation path for critical security risks and the owner approval trigger.

**Conceptual model elements:**

1. **Cross-cutting triage principle (AP-10):** Security, risk, compliance, secrets, and data are evaluated at every gate. A gate cannot be marked as passing if known critical security risks are unresolved.

2. **Risk triage categories:** Security risks in CAFL V1 are triaged as: (a) **resolved** — risk has an accepted decision and conceptual mitigation path; (b) **spike-dependent** — risk cannot be resolved without spike validation; (c) **owner-decision required** — risk involves a cross-boundary or architectural choice requiring owner approval. Categories (b) and (c) are not gate blockers at the Blueprint level but must be explicitly declared.

3. **Critical risk escalation:** Risks classified as RISK-059 (environment form), RISK-021 (secrets leakage), RISK-027 (permissions), RISK-040 (compliance), RISK-061 (secrets in Odoo), and RISK-063 (security runtime) are tracked as spike-dependent or owner-decision required. None are resolved here; they are passed to S16 for spike ordering.

4. **Owner approval trigger:** Any security component that crosses into executable policy, vault creation, real credentials, or cross-environment permission grants triggers an owner approval requirement before Blueprint advancement. This is consistent with CRIT-03 and AP-10.

5. **Compliance posture:** CAFL V1 is an internal framework for internal requests / simple approvals pilot only. No external compliance certifications are in scope for V1 (BR-01). Compliance obligations that arise from the Odoo 18 deployment context are spike-dependent (RISK-040).

6. **Traceability:** AP-10, CRIT-02, CRIT-03, CRIT-04, RISK-021, RISK-027, RISK-040, RISK-059, RISK-061, RISK-063, DEC-ACCEPTED-092, DEC-ACCEPTED-101, TOM security/risk/compliance/owner-approval sections.

##### 14.4 Security Model Applied to S13 Logical Components

The following table maps each S13 logical component to its conceptual security considerations in S14. No executable controls are defined; this is a traceability and scoping map.

| S13 Logical Component | Security concern | Control area | Spike needed |
|---|---|---|---|
| Odoo 18 instance | Administrative credentials, module install permissions | CA-1 (Secrets), CA-2 (Permissions) | Secrets Handling, Permissions Model |
| PostgreSQL | DB credentials, connection access | CA-1 (Secrets), CA-2 (Permissions) | Secrets Handling, Permissions Model |
| Installed pilot module | Module-level access rights, code source traceability | CA-2 (Permissions), CA-3 (Evidence) | Permissions Model |
| Test execution mechanism | Test runner credentials/access, result capture integrity | CA-1 (Secrets), CA-3 (Evidence) | Secrets Handling, Security Validation |
| Evidence capture mechanism | Write access to evidence store, non-embedding of secrets | CA-3 (Evidence) | Security Validation |
| Conceptual execution trigger | Trigger authentication concept | CA-2 (Permissions) | Permissions Model |
| Odoo 18 source reference | Source attribution for evidence, source policy compliance | CA-3 (Evidence), CA-4 (Triage) | None (governed by S12) |

**Environment category application:**

| S13 Environment Category | Security posture |
|---|---|
| Development | Lowest privilege boundary; secrets must not leak to validation or authority reference categories. |
| Validation | Isolated from development credentials; evidence captured here is candidate L3 until governed registration. |
| Authority reference | Highest protection; artifacts here are L1 or L2 per S11 hierarchy; no credentials from lower categories. |

##### 14.5 Non-Decisions (Explicit)

The following are explicitly **not decided** in S14. They are spike dependencies or owner decisions deferred to S16 or later:

1. **Concrete secrets storage mechanism:** environment variables, secrets manager, vault product, .env files, OS keyring — not chosen. Spike dependency.
2. **Concrete permissions model:** Odoo roles, ACL definitions, database user roles, network-level isolation — not defined. Spike dependency.
3. **Security validation tooling:** static analysis tools, security scanners, compliance frameworks — not chosen. Spike dependency.
4. **Cross-environment isolation implementation:** Docker network isolation, process isolation, OS-level permissions — not defined. Depends on S13 environment form spike.
5. **Compliance certification scope:** any external or regulatory compliance requirements — not evaluated. V1 internal only (BR-01); spike-dependent if obligations arise.
6. **Security for post-V1 components:** no security model for post-V1 agents, multi-tenant, external integrations, or production deployment. Out of V1 scope.

##### 14.6 Traceability

| S14 component | Primary anchors |
|---|---|
| CA-1 Secrets Handling | AP-10, AP-11, RISK-021, RISK-061, DEC-ACCEPTED-045, TOM security section |
| CA-2 Permissions | AP-10, AP-11, CRIT-02, CRIT-03, RISK-027, DEC-ACCEPTED-059, DEC-ACCEPTED-076, TOM owner-approval |
| CA-3 Evidence Protection | S11 (L1-L4, 6-step), S12 (source policy, Curation Request), S13 (SCH-10, VAL-05, VAL-10), RISK-021, CRIT-04, DEC-ACCEPTED-163 |
| CA-4 Security Triage in Gates | AP-10, CRIT-02, CRIT-03, CRIT-04, RISK-040, RISK-059, RISK-063, DEC-ACCEPTED-092, DEC-ACCEPTED-101, TOM risk/compliance |
| Logical component map | S13 handoff (all 7 components), S11 L1-L4, S12 source policy |
| Non-decisions / spike list | AP-11, BR-01, BR-02, RISK-021, RISK-027, RISK-040, RISK-059, RISK-061, RISK-063 |
| V1 boundary enforcement | BR-01, BR-04, DEC-ACCEPTED-162 (pilot), DEC-ACCEPTED-064 |

##### 14.7 Spike Dependencies for S16

S14 identifies the following spike dependencies to be included in S16 final spike ordering:

| Spike ID (candidate) | Description | Blocking dependency | Risk anchor |
|---|---|---|---|
| SPK-S14-01 | Secrets Handling Mechanism | Must resolve before any environment credentials are defined; depends on S13 environment form spike | RISK-021, RISK-061 |
| SPK-S14-02 | Permissions Model | Must resolve before pilot module installation or test execution is authorized; depends on S13 environment form spike | RISK-027 |
| SPK-S14-03 | Security Validation Approach | Must resolve before evidence from test execution can be registered as L2 governed; depends on SPK-S14-01 and SPK-S14-02 | RISK-063 |
| SPK-S14-04 | Compliance Obligations Assessment | Must resolve if any regulatory or external obligation arises from Odoo 18 deployment context; currently V1 internal only | RISK-040 |

**Ordering constraint:** SPK-S14-01 and S13's environment form spike must be resolved before SPK-S14-02 and SPK-S14-03. SPK-S14-04 is conditional on deployment context clarification.

##### 14.8 Handoffs

- **S14 → S15 (Pilot Module Blueprint):** S14 delivers the four conceptual control areas (secrets handling posture, permissions model, evidence protection, security triage in gates), the logical component security map, and the non-embedding and separation principles as security constraints that S15 must respect when defining the pilot module blueprint. S15 must not embed secrets, must not define executable permission rules, and must treat pilot module installation and test execution as spike-dependent on SPK-S14-01 and SPK-S14-02.

- **S14 → S16 (Spikes and Technical Validations final order):** S14 delivers four candidate spikes (SPK-S14-01 through SPK-S14-04) with their ordering constraints and risk anchors. S16 must include these spikes in the final ordering, respecting that SPK-S14-01 blocks SPK-S14-02 and SPK-S14-03, and that both depend on S13's environment form spike.

##### 14.9 Inputs Consumed

- **S13 (approved):** Logical component descriptions (Odoo 18 instance, PostgreSQL, installed pilot module, test execution mechanism, evidence capture mechanism, conceptual execution trigger, Odoo 18 source reference), three environment categories (development, validation, authority reference), S13 spike dependencies (environment form, DB compatibility, test runner, evidence capture, code source traceability), S12 source policy constraints as applied in S13.
- **S11 (via S13 context):** L1-L4 authority hierarchy, 6-step evidence lifecycle.
- **S12 (via S13 context):** Minimal source policy (docs.odoo.com + github.com/odoo/odoo), Curation Request mechanism as governance pattern for source expansion.
- **TOM:** Security, risk, compliance, data, and owner approval sections (conceptual anchors only; no full TOM read required per normal mode budget).
- **Architecture Principles (S02):** AP-10 (cross-cutting), AP-11 (spike validation), AP-12 (greenfield, no framework/).
- **Prior handoffs:** S08 → S14 (permissions, secrets, accesses are cross-cutting invariants and risks; SP-04 open; no permission rules, vault, or executable secrets policy); S09 → S14 (security elements are logical categories only; no permission rules or executable secrets policy); S10 → S14 (VAL-01 and VAL-09 as logical control categories; no executable permission rules or vault); S11 → S14 (logical storage categories for access controls and secrets policy at conceptual level); S12 → S14 (Curation Request and Knowledge Gap as governance patterns applicable to secrets source management).

##### 14.10 Acceptance Criteria

1. Section covers all four conceptual control areas: secrets handling posture, permissions model, evidence protection, and security/risk triage in gates.
2. Security model is conceptual only: no real secrets, tokens, certificates, configurations, or executable policies exposed or generated anywhere in this section.
3. Every security component traces to at least one required traceability anchor (AP-10, CRIT-02/03/04, accepted decisions, risks, TOM) as listed in Section 14.6.
4. Section integrates with all seven S13 logical components and three environment categories via the logical component security map (Section 14.4).
5. Section respects S11 L1-L4 authority hierarchy for security evidence (Section 14.3.3).
6. Section respects S12 source policy: docs.odoo.com + github.com/odoo/odoo only; no auto-expansion; Curation Request for any expansion (Sections 14.2, 14.3.3).
7. Section identifies four spike dependencies for S16 with ordering constraints and risk anchors (Section 14.7).
8. Section delivers handoffs to S15 (security constraints for pilot module) and S16 (security spike ordering) (Section 14.8).
9. No unbacked (non-traceable) security components present.
10. V1 boundaries preserved: Odoo-only, Odoo 18, internal requests/simple approvals, minimal source policy, `framework/` excluded.
11. No PRD, SDD, backlog, runtime, implementation, or executable artifacts present.

#### 15. Pilot Module Blueprint

Status: closed

Owner approval: approved explicitly by owner.

##### 1. Purpose

S15 define conceptualmente el Blueprint del modulo piloto de CAFL V1 a nivel de componentes. Su objetivo es describir los artefactos logicos que el modulo piloto necesita — modelos de datos (Python classes), vistas, seguridad (ACL, record rules), flujo de estados y tests — para ejecutar el caso de uso de solicitudes internas / aprobaciones simples (DEC-ACCEPTED-162) sobre Odoo 18, sin crear un modulo ejecutable, sin instalar Odoo, sin generar PRD, SDD, backlog funcional ni implementacion real.

S15 recibe los handoffs de S13 (categorias de entorno conceptual, componentes logicos, restricciones de source policy, modelo de evidencia L1-L4) y S14 (cuatro areas de control de seguridad, mapa de seguridad de componentes logicos, principio de no-embedding, dependencias de spike SPK-S14-01/02) como restricciones heredadas. S15 no redefine ni el entorno ni los controles de seguridad; los asume y los aplica al diseño conceptual del modulo.

La razon de existencia de esta seccion en el Blueprint es que el piloto V1 requiere un Blueprint claro a nivel de componentes para que S16 pueda ordenar los spikes tecnicos relacionados con el modulo, S17 pueda incluirlo en la matriz de trazabilidad, y S19 pueda derivar criterios de aceptacion verificables. El diseño conceptual aqui definido establece que componentes necesita el modulo, como fluye el estado de las solicitudes, que evidencia debe registrarse y cuales decisiones tecnicas quedan abiertas para los spikes.

##### 2. Inputs / Scope

Inputs trazables usados:

- S13 handoff a S15: categorias conceptuales de entorno (desarrollo, validacion, referencia de autoridad), siete componentes logicos del entorno (instancia Odoo 18, PostgreSQL, modulo piloto instalado, mecanismo de ejecucion de tests, captura de evidencia, trigger de ejecucion conceptual, referencia de codigo fuente Odoo 18), restricciones de source policy (docs.odoo.com + github.com/odoo/odoo), modelo de evidencia (L1-L4, SCH-10, VAL-05, VAL-10), restricciones del piloto (DEC-ACCEPTED-162). Trazable a DEC-ACCEPTED-135; DEC-ACCEPTED-153; DEC-ACCEPTED-162; DEC-ACCEPTED-163; BR-01.
- S14 handoff a S15: cuatro areas de control (CA-1 secrets handling posture, CA-2 permissions/access model, CA-3 evidence protection, CA-4 security/risk triage in gates), mapa logico de seguridad de componentes, principios de no-embedding y separacion. Restricciones: no embeber secrets, no crear permission rules ejecutables, tratar instalacion y ejecucion de tests como spike-dependiente sobre SPK-S14-01 y SPK-S14-02. Trazable a AP-10; CRIT-02; CRIT-03; CRIT-04.
- S09 SCH-10 Odoo Pilot Artifact Schema: modelo logico del artefacto del piloto Odoo 18 — modelos de datos, vistas, ACL, record rules, flujos de trabajo, tests y evidencia asociada. Trazable a CRIT-06; CRIT-07; TOM; BR-01; AP-08; DEC-ACCEPTED-162; DEC-ACCEPTED-163.
- S10 VAL-10 Odoo Pilot Artifact Scope Validator: control conceptual que verifica que los artefactos del piloto estan dentro de solicitudes internas / aprobaciones simples, referencian fuentes Odoo pre-autorizadas y tienen evidencia y control asociados. Trazable a BR-01; DEC-ACCEPTED-162; DEC-ACCEPTED-163.
- S10 VAL-05 Evidence Record Validator: verifica que la evidencia producida tiene origen trazable, tipo declarado, resumen verificable y estado candidato. Trazable a AP-09; CRIT-06.
- S11 jerarquia L1-L4 y ciclo de vida de evidencia candidata: modelo logico para registrar evidencia del modulo piloto bajo los niveles de autoridad apropiados. L3 es el nivel inicial para outputs del modulo; requiere registro gobernado para ascender a L2. Trazable a AP-09; DEC-ACCEPTED-146.
- S12 source policy minima operacionalizada (docs.odoo.com + github.com/odoo/odoo): restriccion de fuentes aplicable a todas las referencias tecnicas del modulo piloto. Trazable a DEC-ACCEPTED-163; AP-06; AP-12.
- S08 handoff: agent reasoning, command repeatability, validator evidence criteria aplicables al diseño del piloto (trazabilidad de razonamiento del agente, repetibilidad de operaciones del modulo). Trazable a CRIT-07; AP-04.
- DEC-ACCEPTED-162: piloto V1 = solicitudes internas / aprobaciones simples. Restriccion de scope no reabrble.
- DEC-ACCEPTED-163: source policy minima — docs.odoo.com + github.com/odoo/odoo son las unicas fuentes pre-autorizadas para V1.
- BR-01 (S03): V1 boundary — Odoo-only, Odoo 18, piloto internal requests / simple approvals. Sin RAG, SDK/server, dashboard/UI, CI/CD, multiusuario, plugins/MCP.
- AP-08: V1 minimo suficiente y anti-scope-creep. CRIT-06 (evidence/IDs/logs); CRIT-07 (minimum validators).
- AP-09: evidencia simple, auditable y Git-compatible.
- RISK-059: falta de entorno Odoo 18 — critical. Impacta instalacion y ejecucion del modulo piloto.
- RISK-010: verificacion no reproducible — high. Impacta tests y captura de evidencia del modulo.

Alcance de S15:

- Definir conceptualmente los artefactos del modulo piloto (modelos de datos, vistas, seguridad, flujo de estados, evidencia, tests) a nivel de componentes.
- Describir como el modulo se integra con el modelo de evidencia L1-L4 de S11.
- Describir restricciones de seguridad heredadas de S14 aplicadas al modulo piloto.
- Describir restricciones de source policy heredadas de S12 y S13 aplicadas al modulo piloto.
- Declarar dependencias de spike tecnicas del modulo para S16.
- Entregar handoffs a S16 (spikes del modulo), S17 (trazabilidad), S19 (acceptance criteria).

Fuera de alcance:

- Crear el modulo Odoo 18 ejecutable ni ningun artefacto de implementacion.
- Instalar el modulo, ejecutar tests ni capturar evidencia real.
- Crear PRD final, SDD final ni backlog funcional del piloto.
- Reabrir la seleccion del piloto (DEC-ACCEPTED-162 cerrado).
- Ampliar source policy (docs.odoo.com + github.com/odoo/odoo solamente).
- Redefinir el entorno Odoo 18 (S13) ni los controles de seguridad (S14).
- Crear schemas fisicos, validators reales, scripts, commands, toolchain ejecutable ni runtime.
- Usar o referenciar `framework/` como input.
- Expandir V1 fuera de Odoo-only, Odoo 18, solicitudes internas / aprobaciones simples.
- Embeber secrets ni crear permission rules ejecutables (restriccion directa de S14 CA-1 y CA-2).

##### 3. Conceptual Pilot Module Blueprint Design

El diseño que sigue es logico y conceptual. No crea el modulo Odoo 18, no instala artefactos, no genera codigo fuente ejecutable, no define paths ni toolchain. El modulo piloto exacto (estructura de archivos Python, XML, CSV) queda abierto para los spikes correspondientes, conforme DEC-ACCEPTED-162, S13 y S14.

###### 3.1 Proposito y scope del modulo piloto

El modulo piloto es el artefacto de software Odoo 18 que realiza el ciclo minimo real de CAFL V1. Su proposito conceptual es demostrar que el framework puede producir un modulo Odoo 18 funcional, dentro del scope de solicitudes internas / aprobaciones simples, con evidencia verificable y trazabilidad completa a las decisiones y schemas del Blueprint.

| Atributo | Valor conceptual | Fundamento |
| --- | --- | --- |
| Plataforma objetivo | Odoo 18 unicamente | DEC-ACCEPTED-135; BR-01 |
| Scope funcional | Solicitudes internas / aprobaciones simples | DEC-ACCEPTED-162 |
| Nombre logico del modulo | cafl_pilot (nombre logico conceptual; nombre exacto queda para spike) | DEC-ACCEPTED-162; SCH-10 |
| Dependencias Odoo | Solo modulos del core de Odoo 18 pre-autorizados | DEC-ACCEPTED-163; VAL-10 |
| Fuentes tecnicas elegibles | docs.odoo.com + github.com/odoo/odoo unicamente | DEC-ACCEPTED-163; S12 |
| Integraciones externas | Ninguna en V1 core | BR-01; AP-08 |
| Evidencia minima requerida | Evidencia candidata (L3) de instalacion, tests y scope bajo VAL-05 y VAL-10 | S11; S13 3.3 |

Trazabilidad: DEC-ACCEPTED-162; DEC-ACCEPTED-163; DEC-ACCEPTED-135; BR-01; SCH-10; VAL-10; AP-08.

###### 3.2 Modelos de datos conceptuales (Python classes en Odoo ORM)

El modulo piloto requiere dos modelos principales de datos que soporten el caso de uso de solicitudes internas / aprobaciones simples. Estos modelos son conceptuales; sus campos exactos, relaciones completas y metodos se definen en la implementacion real, guiada por docs.odoo.com y github.com/odoo/odoo.

**Modelo conceptual 1 — Solicitud interna (InternalRequest):**

| Elemento conceptual | Descripcion | Tipo conceptual Odoo | Restriccion |
| --- | --- | --- | --- |
| Nombre/descripcion de la solicitud | Identificacion legible de la solicitud | Char / Text | Requerido; origen en docs.odoo.com |
| Solicitante | Usuario Odoo que crea la solicitud | Many2one → res.users | Requerido; ligado al modelo de acceso CA-2 S14 |
| Estado de la solicitud | Estado actual en el flujo (draft, submitted, approved, rejected) | Selection / statusbar | Controlado por flujo de estados; ver 3.4 |
| Fecha de solicitud | Timestamp de creacion | Datetime | Auto-generado conceptualmente |
| Notas / justificacion | Texto libre de justificacion | Text | Opcional |
| Aprobador asignado | Usuario Odoo responsable de aprobar | Many2one → res.users | Requerido si estado llega a submitted; ligado a CA-2 |

**Modelo conceptual 2 — Registro de aprobacion (ApprovalRecord):**

| Elemento conceptual | Descripcion | Tipo conceptual Odoo | Restriccion |
| --- | --- | --- | --- |
| Solicitud relacionada | Referencia a la solicitud interna | Many2one → InternalRequest | Requerido; integridad referencial |
| Aprobador | Usuario Odoo que aprueba o rechaza | Many2one → res.users | Requerido; ligado a CA-2 S14 |
| Decision | Aprobado o rechazado | Selection | Requerido; no extension de decisiones fuera de scope |
| Fecha de decision | Timestamp de la decision | Datetime | Auto-generado conceptualmente |
| Comentario del aprobador | Texto libre de decision | Text | Opcional |

Ningun campo de estos modelos contiene secrets, tokens ni credenciales (CA-1 S14). La forma exacta de estos modelos (nombres de clase Python, nombres de campos, herencia Odoo, metodos ORM) se determina en la implementacion, respaldada por docs.odoo.com y github.com/odoo/odoo.

Trazabilidad: DEC-ACCEPTED-162; SCH-10; VAL-10; S14 CA-1; S14 CA-2; DEC-ACCEPTED-163.

###### 3.3 Vistas conceptuales (form, list, search)

El modulo piloto requiere tres tipos de vistas conceptuales para cada modelo principal. Las vistas son conceptuales; sus definiciones XML exactas se determinan en la implementacion guiada por docs.odoo.com.

| Tipo de vista | Modelo | Proposito conceptual | Restriction de scope |
| --- | --- | --- | --- |
| Vista de formulario (form) | InternalRequest | Permite crear y editar una solicitud interna con todos sus campos | Solo campos del modelo conceptual 3.2; sin integraciones externas |
| Vista de lista (list/tree) | InternalRequest | Permite ver solicitudes con estado, solicitante y fecha en columnas | Solo piloto V1; sin columnas de datos externos |
| Vista de busqueda (search) | InternalRequest | Permite filtrar por estado, solicitante, fecha | Filtros conceptuales dentro del scope del modelo |
| Vista de formulario (form) | ApprovalRecord | Permite registrar la decision del aprobador con comentario | Solo campos del modelo conceptual 3.2; decision binaria (approved/rejected) |
| Vista de lista (list/tree) | ApprovalRecord | Permite ver historial de decisiones por solicitud | Solo piloto V1 |

Restricciones de vistas heredadas de S14: las vistas no exponen ni transmiten credenciales, tokens ni datos de configuracion de seguridad (CA-1). Los campos visibles deben estar alineados con el modelo de acceso ACL definido conceptualmente en 3.4.

Trazabilidad: DEC-ACCEPTED-162; SCH-10; S14 CA-1; S14 CA-2; DEC-ACCEPTED-163.

###### 3.4 Flujo de estados (workflow)

El modulo piloto implementa un flujo de estados simple para las solicitudes internas. Este flujo es conceptual; la forma exacta (metodos Python, botones XML, transiciones de estado) se determina en la implementacion.

**Estados conceptuales del flujo:**

| Estado | Descripcion | Transicion entrante | Transicion saliente | Actor conceptual |
| --- | --- | --- | --- | --- |
| draft | Solicitud creada pero no enviada al aprobador | Estado inicial (creacion) | → submitted (accion del solicitante) | Solicitante |
| submitted | Solicitud enviada; pendiente de decision del aprobador | draft → submitted | → approved o → rejected (accion del aprobador) | Sistema (automatico al enviar) |
| approved | Solicitud aprobada por el aprobador | submitted → approved | Terminal (no hay transicion saliente en V1) | Aprobador |
| rejected | Solicitud rechazada por el aprobador | submitted → rejected | Terminal (no hay transicion saliente en V1) | Aprobador |

**Reglas conceptuales del flujo:**

- Solo el solicitante puede mover de draft a submitted.
- Solo el aprobador asignado puede mover de submitted a approved o rejected.
- Los estados approved y rejected son terminales en V1; no hay reabrir ni ciclos multietapa (scope limitation per DEC-ACCEPTED-162).
- El flujo no admite escalaciones, delegaciones ni roles multiples en V1 (BR-01 anti-scope-creep AP-08).

Trazabilidad: DEC-ACCEPTED-162; BR-01; AP-08; SCH-10; VAL-10; S14 CA-2.

###### 3.5 Seguridad conceptual (ACL y record rules)

La seguridad del modulo piloto se diseña en el marco de los cuatro areas de control de S14. Este diseño es conceptual; no crea archivos CSV de ACL ejecutables, no crea record rules XML ejecutables ni define politicas de permisos implementadas.

**Area CA-1 — Secrets handling posture aplicada al modulo:**

El modulo piloto no debe contener secrets embebidos en ningun artefacto (modelos Python, vistas XML, datos CSV, tests). Credenciales de base de datos, tokens de API, claves de cifrado o cualquier otro secret deben ser manejados por el entorno de ejecucion (S13), no por el modulo. Esta restriccion es absoluta y no tiene excepcion en V1. La forma exacta de como el entorno inyecta configuracion al modulo sin embeber secrets queda para SPK-S14-01.

**Area CA-2 — Permissions/access model aplicado al modulo (conceptual):**

| Rol conceptual | Permisos conceptuales sobre InternalRequest | Permisos conceptuales sobre ApprovalRecord | Principio |
| --- | --- | --- | --- |
| Usuario solicitante | Crear, leer sus propias solicitudes, enviar (draft→submitted) | Solo leer los registros de sus solicitudes | Principio de minimo acceso; acceso a sus propios registros |
| Usuario aprobador | Leer solicitudes submitted asignadas, aprobar/rechazar | Crear registro de decision, leer sus propias decisiones | Acceso restringido a solicitudes que le corresponden |
| Administrador del modulo | Lectura completa, gestion de configuracion | Lectura completa | Solo para operacion del piloto; sin acceso a otros modulos por este rol |

Ninguna de estas definiciones es una ACL CSV ejecutable ni un record rule XML. Son principios conceptuales que guian la implementacion. La forma exacta del modelo de permisos Odoo (grupos de seguridad, ir.rule, ir.model.access.csv) se determina en la implementacion guiada por docs.odoo.com y SPK-S14-02.

**Area CA-3 — Evidence protection aplicada al modulo:**

Los registros de evidencia producidos por el modulo (logs de instalacion, resultados de tests, snapshots de estado) son L3 candidatos conforme S11. No pueden ser modificados retroactivamente ni eliminados una vez registrados conceptualmente. La integridad de la evidencia es responsabilidad del ciclo de vida de S11, no del modulo en si.

**Area CA-4 — Security/risk triage in gates aplicado al modulo:**

Antes de que el modulo piloto pueda ser instalado en el entorno de validacion (S13), debe pasar revision de seguridad conceptual: confirmacion de que no hay secrets embebidos (CA-1), confirmacion de que el modelo de acceso es coherente con CA-2, confirmacion de que la evidencia de instalacion es candidata L3 elegible. Esta revision es un gate conceptual; su forma exacta (checklist, script, proceso manual) queda para spike y para la implementacion con autorizacion explicita.

Trazabilidad: S14 CA-1; S14 CA-2; S14 CA-3; S14 CA-4; SPK-S14-01; SPK-S14-02; DEC-ACCEPTED-162; S11 L1-L4; AP-10; CRIT-02; CRIT-03; CRIT-04.

###### 3.6 Registro de evidencia del modulo piloto (candidato L3)

Conforme al modelo de evidencia de S11 y los eventos de entorno definidos en S13 3.3, el modulo piloto genera evidencia candidata (L3) en los siguientes puntos de ejecucion. Este mapa es conceptual; no crea mecanismos de captura reales.

| Evento del modulo | Tipo de evidencia candidata | Nivel S11 inicial | Schema/Validator aplicable | Condicion de promocion |
| --- | --- | --- | --- | --- |
| Instalacion del modulo cafl_pilot | Log de instalacion: exito/error, dependencias resueltas, version Odoo 18 | L3 candidata | SCH-05 (Evidence Record); VAL-05 | Evaluacion gobernada; registro explicito con trazabilidad |
| Ejecucion de test unitario de InternalRequest | Resultado de test runner: tests pasados/fallidos, nombre del test, timestamp | L3 candidata | SCH-05; SCH-06; SCH-10; VAL-05; VAL-10 | Evaluacion gobernada; puede apoyar gate si se promociona a L2 |
| Ejecucion de test del flujo de estados | Resultado de test de transicion draft→submitted→approved/rejected | L3 candidata | SCH-05; SCH-06; SCH-10; VAL-05; VAL-10 | Evaluacion gobernada; trazabilidad al flujo 3.4 |
| Verificacion de scope VAL-10 | Resultado de VAL-10: artefactos dentro de solicitudes internas/aprobaciones simples, fuentes pre-autorizadas | L3 candidata | SCH-10; VAL-10 | Evaluacion gobernada |
| Verificacion de source policy | Confirmacion de que todas las referencias tecnicas del modulo son docs.odoo.com o github.com/odoo/odoo | L3 candidata | SCH-01; VAL-01 | Evaluacion gobernada; confirma DEC-ACCEPTED-163 |
| Snapshot de estado del modulo instalado | Estado del modulo en instancia Odoo 18: version, modulos activos, resultado general de tests | L3 candidata | SCH-07; VAL-05 | Evaluacion gobernada; solo si cubre requisito de gate o handoff |

Regla de autoridad: ningun output del modulo piloto puede actuar como evidencia formal de gate, handoff ni cierre de seccion sin haber pasado por el ciclo de vida de S11 (L3 → L2 mediante registro gobernado). `project-truth/` (L1) no es sustituida por outputs del modulo.

Trazabilidad: S11 jerarquia L1-L4; S11 ciclo de vida 6 pasos; SCH-05; SCH-06; SCH-07; SCH-10; VAL-05; VAL-10; AP-09; DEC-ACCEPTED-146; CRIT-06; AP-09.

###### 3.7 Enfoque de tests conceptual

El modulo piloto requiere un enfoque de tests que permita verificar el comportamiento del caso de uso (solicitudes internas / aprobaciones simples) y producir evidencia candidata. El enfoque es conceptual; la herramienta exacta, el test runner y los archivos de test se determinan en la implementacion, guiada por docs.odoo.com y el spike de entorno.

**Tipos de tests conceptuales requeridos:**

| Tipo de test | Descripcion conceptual | Cobertura minima conceptual | Requisito de evidencia |
| --- | --- | --- | --- |
| Test unitario de modelos | Verifica que los modelos InternalRequest y ApprovalRecord pueden crearse, leerse y modificarse conforme a sus campos conceptuales | Creacion valida, campo requerido, tipo de campo | Resultado L3 bajo VAL-05; SCH-05 |
| Test de flujo de estados | Verifica las cuatro transiciones del flujo (draft→submitted, submitted→approved, submitted→rejected) y que los estados terminales son terminales | Las cuatro transiciones declaradas en 3.4; rechazo de transicion invalida | Resultado L3 bajo VAL-05; SCH-06; SCH-10 |
| Test de scope (VAL-10) | Verifica que el modulo no sale del scope de solicitudes internas / aprobaciones simples | Ninguna entidad, vista ni logica fuera del scope DEC-ACCEPTED-162 | Resultado L3 bajo VAL-10 |
| Test de source policy | Verifica que todas las referencias tecnicas del modulo apuntan a fuentes pre-autorizadas | Ninguna referencia fuera de docs.odoo.com o github.com/odoo/odoo | Resultado L3 bajo VAL-01 |

**Restricciones del enfoque de tests heredadas de S14:**

- La ejecucion real de tests sobre el entorno de validacion (S13) esta bloqueada hasta que SPK-S14-02 (pilot module installation test as spike) sea ejecutado y resuelto.
- Ningun archivo de test debe contener secrets, credenciales ni tokens (CA-1).
- Los resultados de tests son evidencia candidata (L3); no son autoritativos hasta que pasen el ciclo de vida de S11.

Trazabilidad: DEC-ACCEPTED-162; DEC-ACCEPTED-153; SCH-05; SCH-06; SCH-10; VAL-05; VAL-10; VAL-01; S14 CA-1; SPK-S14-02; S13 3.3; CRIT-07; AP-09.

###### 3.8 Restricciones de source policy aplicadas al modulo piloto

El modulo piloto opera dentro de la source policy minima definida por DEC-ACCEPTED-163 y operacionalizada en S12. Las restricciones son:

- **Fuentes pre-autorizadas unicamente:** toda referencia tecnica usada para diseñar, construir o validar el modulo (API de Odoo ORM, estructura de modulos Odoo, definicion de vistas XML, sistema de seguridad Odoo) debe provenir de docs.odoo.com o github.com/odoo/odoo. Ninguna otra fuente es elegible sin Curation Request aprobada por owner.
- **Version Odoo 18 obligatoria:** toda referencia tecnica debe corresponder a Odoo 18. Referencias a Odoo 16, 17 u otras versiones no son elegibles en V1.
- **Gaps de source policy en el modulo:** si durante la implementacion del modulo se detecta que se necesita una fuente no pre-autorizada, debe activarse el flujo de Knowledge Gap definido en S12 (VAL-09 trigger → Curation Request → aprobacion owner). S15 no puede ampliar source policy por iniciativa propia.
- **`framework/` excluido:** ningun artefacto ni referencia del directorio legado excluido puede usarse como input para el modulo piloto.

Trazabilidad: DEC-ACCEPTED-163; S12 source policy minima; S10 VAL-01; S10 VAL-09; AP-06; AP-12; RULE-10.

###### 3.9 Dependencias de spike tecnicas del modulo piloto

S15 identifica las dependencias de validacion tecnica que los spikes correspondientes (a ordenar en S16) deben resolver para que el modulo piloto pueda ser instalado y ejecutado. Estas son preguntas tecnicas abiertas; no pueden ser resueltas conceptualmente.

| Dependencia de spike | Descripcion | Spike relacionado de S14 | Riesgo relacionado | Requisito de evidencia |
| --- | --- | --- | --- | --- |
| Instalacion del modulo en el entorno decidido | Verificar que cafl_pilot (nombre logico) puede instalarse en la instancia Odoo 18 resultante del spike de entorno (S16) | SPK-S14-01 (environment setup without secrets embedding) | RISK-059 (critical); RISK-010 (high) | Spike debe producir evidencia L3 de instalacion exitosa sin secrets embebidos |
| Ejecucion de tests del modulo | Verificar que el test runner Odoo 18 ejecuta los tests del modulo y produce resultados capturables | SPK-S14-02 (pilot module installation test as spike) | RISK-010 (high) | Spike debe producir log de tests con al menos un test del flujo de estados ejecutado y resultado L3 bajo VAL-05 |
| Modelo de acceso ejecutable | Verificar que la ACL y record rules conceptuales de 3.5 pueden implementarse en Odoo 18 con los grupos de seguridad propios del modulo, sin conflictos con la instalacion base | SPK-S14-02 | RISK-010 | Spike debe confirmar que los grupos de seguridad del modulo funcionan conforme al modelo CA-2 sin exposicion de datos de otros modulos |
| Trazabilidad de codigo fuente del modulo | Verificar que los patrones de implementacion del modulo (herencia de modelos Odoo, estructura de vistas XML, definicion de ACL) tienen respaldo en github.com/odoo/odoo version 18 | Spike de entorno (S16) | DEC-ACCEPTED-163; RISK-010 | Spike debe confirmar referencias a github.com/odoo/odoo v18 para cada patron del modulo |

Ningun spike puede ser resuelto conceptualmente desde S15. S15 los declara para que S16 los incluya en el orden final de spikes con la prioridad correspondiente.

Trazabilidad: SPK-S14-01; SPK-S14-02; RISK-059; RISK-010; DEC-ACCEPTED-162; DEC-ACCEPTED-163; DEC-ACCEPTED-153; S14 CA-1; S14 CA-2; AP-09; S11 L3.

##### 4. Cross-Section Guidance / Handoff Rules

- **Para S16 Spikes and Technical Validations:** S15 entrega a S16 cuatro dependencias de spike tecnicas del modulo piloto (instalacion del modulo, ejecucion de tests, modelo de acceso ejecutable, trazabilidad de codigo fuente) mas las dos dependencias de spike heredadas de S14 (SPK-S14-01, SPK-S14-02) como insumos para el orden final de spikes. RISK-059 (critical) posiciona el spike de entorno como precondicion de todos los spikes del modulo. El modulo cafl_pilot (nombre logico) no puede ser instalado ni ejecutado hasta que el spike de entorno este resuelto.
- **Para S17 Bidirectional Traceability Matrix:** S15 entrega a S17 el mapa completo de componentes del modulo piloto (modelos, vistas, flujo de estados, seguridad, evidencia, tests) con su trazabilidad a DEC-ACCEPTED-162, DEC-ACCEPTED-163, DEC-ACCEPTED-135, BR-01, SCH-10, VAL-10, VAL-05, S14 CA-1..CA-4, S13 componentes logicos, S11 L1-L4. Este mapa es la base para la matriz bidireccional del modulo piloto.
- **Para S19 Acceptance Criteria:** S15 entrega a S19 las dependencias de spike del modulo y los tipos de evidencia candidata (L3) declarados en 3.6 como criterios de aceptacion candidatos para el componente de piloto en V1. S19 no puede cerrar acceptance criteria del modulo sin evidencia gobernada del spike correspondiente (L2).
- **Para S13 y S14 (no hay handoffs retroactivos):** S15 consume los handoffs de S13 y S14 como restricciones heredadas sin retroalimentacion ni modificacion de esas secciones.
- **Restriccion general:** ningun handoff de S15 crea el modulo ejecutable, instala Odoo, ejecuta tests ni crea scripts. Todo handoff es conceptual y su materializacion depende de los spikes correspondientes y de los ciclos de implementacion con autorizacion explicita del owner.

##### 5. Explicit Non-Decisions

- Esta seccion no crea el modulo Odoo 18 ejecutable ni ningun archivo de implementacion (Python, XML, CSV, JSON).
- Esta seccion no instala el modulo en ningun entorno ni ejecuta tests reales.
- Esta seccion no decide el nombre final del modulo Python (cafl_pilot es un nombre logico conceptual; el nombre exacto queda para spike e implementacion).
- Esta seccion no decide la estructura de archivos exacta del modulo (manifesto __manifest__.py, estructura de carpetas, herencia de clases Python especifica).
- Esta seccion no crea ir.model.access.csv ni record rules XML ejecutables; el modelo de acceso de 3.5 es conceptual unicamente.
- Esta seccion no crea PRD final, SDD final ni backlog funcional del piloto.
- Esta seccion no reabre la seleccion del piloto; DEC-ACCEPTED-162 (solicitudes internas / aprobaciones simples) esta cerrado y es restriccion no negociable.
- Esta seccion no amplia la source policy minima; docs.odoo.com + github.com/odoo/odoo son las unicas fuentes pre-autorizadas; cualquier ampliacion requiere Curation Request y aprobacion owner.
- Esta seccion no ejecuta los spikes SPK-S14-01 ni SPK-S14-02 ni resuelve sus dependencias; las declara para S16.
- Esta seccion no decide si el test runner de Odoo 18 usa odoo-bin test, unittest, pytest o cualquier otra forma; esa decision queda para spike y para la implementacion real.
- Esta seccion no modifica el entorno Odoo 18 definido en S13 ni los controles de seguridad definidos en S14.
- Esta seccion no crea RAG/base vectorial, SDK/server, dashboard/UI, CI/CD completo, base de datos avanzada, operacion multiusuario, plugins/MCP ni integraciones externas fuera de core V1.
- Esta seccion no convierte outputs runtime en evidencia formal; el registro gobernado (L3 → L2) requiere decision explicita y actor humano o proceso aprobado.
- Esta seccion no usa ni referencia `framework/` como input.
- Esta seccion no genera el orden final de spikes, la matriz de trazabilidad final, los outputs de backlog ni los acceptance criteria finales; esos pertenecen a S16-S19.
- Esta seccion no embebe secrets, tokens, credenciales ni claves en ningun componente conceptual descrito (restriccion absoluta de S14 CA-1).

##### 6. Open Questions / Owner Decisions

- none

##### 7. Acceptance Criteria

1. Framework support para el piloto explicado a nivel de componentes (modelos, vistas, flujo de estados, seguridad, evidencia, tests); no es PRD, SDD ni backlog.
2. Todos los componentes del modulo piloto trazan a S13/S14 handoffs, DEC-ACCEPTED-162, DEC-ACCEPTED-163, BR-01, SCH-10, VAL-05, VAL-10 como se declara en 3.1-3.9.
3. Source policy respetada; solo docs.odoo.com + github.com/odoo/odoo referenciadas como fuentes elegibles.
4. No hay secrets embebidos ni permission rules ejecutables en ningun componente conceptual descrito (S14 CA-1 y CA-2).
5. Instalacion y ejecucion de tests tratadas como spike-dependientes (SPK-S14-01 y SPK-S14-02 declarados en 3.9).
6. Modelo de evidencia S11 L1-L4 aplicado; evidencia del modulo como candidata L3 declarada en 3.6 con schemas y validators.
7. Boundaries V1 preservados: BR-01 (Odoo-only, Odoo 18, solicitudes internas / aprobaciones simples) y AP-08 (V1 minimo suficiente, anti-scope-creep).
8. Ningun artefacto prohibido presente: no PRD, SDD, backlog, modulo ejecutable, runtime, scripts ni implementacion.
9. `framework/` excluido como input en toda la seccion.
10. Todos los componentes son trazables; no hay componentes sin respaldo en TOM, CRIT aprobado o decision aceptada (RULE-04).

##### 8. Section Output / Handoff

- S15 entrega a S16 cuatro dependencias de spike tecnicas del modulo piloto (instalacion, ejecucion de tests, modelo de acceso ejecutable, trazabilidad de codigo fuente) mas las dependencias heredadas SPK-S14-01/02 como insumos para el orden final de spikes; RISK-059 es la precondicion critica.
- S15 entrega a S17 el mapa de componentes del modulo piloto (modelos, vistas, flujo de estados, seguridad conceptual, evidencia, tests) con trazabilidad completa a DEC-ACCEPTED-162, DEC-ACCEPTED-163, DEC-ACCEPTED-135, BR-01, SCH-10, VAL-10, VAL-05, S14 CA-1..CA-4, S13 componentes logicos, S11 L1-L4, como base para la matriz bidireccional.
- S15 entrega a S19 los tipos de evidencia candidata (L3) del modulo y las dependencias de spike como criterios de aceptacion candidatos para el componente de piloto; S19 no puede cerrar estos criterios sin evidencia gobernada (L2) del spike.
- S15 no cierra ninguna decision sobre implementacion del modulo, forma exacta de artefactos, test runner, ACL ejecutable, nombre final del modulo Python ni toolchain; esos pertenecen a los spikes y a fases de implementacion con autorizacion explicita del owner.

### Iteration 5 - Cierre del Blueprint

#### 16. Spikes and Technical Validations final order

Status: closed

Owner approval: approved explicitly by owner.

##### 16.1 Status and Inputs

**Status**: in-verification

**Inputs**:
- Iterations I1–I4 closed and owner-approved (I1: S01–S06, I2: S07–S08, I3: S09–S12, I4: S13–S15).
- S06 Initial Spike Map: SP-01..SP-13 in four bands A→B→C→D.
- S07 OpenCode Operating Design: SP-04/SP-05 preserved as open uncertainties.
- S08 Mechanism Split: SP-04/SP-05 confirmed as open spike uncertainties.
- S10 Validators: full VAL-01..VAL-10 set as spike ordering inputs.
- S11 Storage: validator results/alerts as spike inputs.
- S12 Source Policy: unresolved Knowledge Gaps and pending Curation Requests as spike inputs.
- S13 Odoo 18 Environment: 5 spike dependencies with RISK-059 (critical).
- S14 Security and Secrets: SPK-S14-01..SPK-S14-04 with ordering constraints.
- S15 Pilot Module Blueprint: 4 technical spike dependencies + 2 inherited from S14.
- Applicable risks: RISK-059, RISK-021, RISK-027, RISK-040, RISK-010, RISK-061, RISK-063.
- Accepted decisions: DEC-ACCEPTED-135, DEC-ACCEPTED-149, DEC-ACCEPTED-153, DEC-ACCEPTED-158, DEC-ACCEPTED-162, DEC-ACCEPTED-163, DEC-ACCEPTED-164.

##### 16.2 Purpose

This section consolidates all spikes and technical validations required for CAFL V1 into a single final ordered list with justified dependencies. The consolidation integrates:

1. SP-01..SP-13 from S06 (Initial Spike Map) with bands A→B→C preserved and band D (SP-11..SP-13) kept conditional/separated from core V1.
2. Five environment spike dependencies from S13 (exact environment form, DB compatibility, Odoo 18 test runner, evidence capture, code source traceability).
3. Four security spike dependencies from S14 (SPK-S14-01 secrets handling, SPK-S14-02 permissions model, SPK-S14-03 security validation, SPK-S14-04 compliance assessment) with their S14-defined ordering constraints.
4. Six pilot module spike dependencies from S15 (four technical + two inherited from S14).
5. Knowledge Gaps and Curation Requests from S12 as potential spike inputs, not as resolved items.

No spike is executed in this section. No validation result is closed. No flat list is produced; every spike entry carries explicit dependencies. This section is the authoritative S16 handoff to S17 (Bidirectional Traceability Matrix), S18 (Blueprint Outputs to Backlog), and S19 (Acceptance Criteria).

##### 16.3 Scope and Restrictions

**In scope**:
- Ordering and dependency justification for all V1 core spikes (bands A, B, C).
- Integration of S13, S14, and S15 spike dependencies into the consolidated list.
- Mapping of conditional/separated spikes (band D) with their conditional status preserved.
- Knowledge Gaps and Curation Requests as input context (not resolved or closed).
- SP-04/SP-05 as open uncertainties (not resolved).
- Traceability of each spike to TOM, CRIT, accepted decisions, and risks.

**Out of scope / restrictions**:
- Do not execute spikes or close validation results.
- Do not resolve SP-04 or SP-05 (remain open uncertainties per S07, S08).
- Do not close Knowledge Gaps or approve Curation Requests (owner-gated per S12).
- Do not create runtime, agents, commands, schemas, validators, scripts, RAG, backlog, PRD, SDD, or implementation artifacts.
- Do not reference or use `framework/` as input.
- Do not expand V1 scope, source policy, or pilot definition.
- Band D spikes (SP-11..SP-13) must remain conditional and separated from core V1.
- RULE-06: every spike must carry explicit justified dependencies; no flat list is permitted.

##### 16.4 Consolidated Spike Catalogue

The catalogue lists every spike with its unique identifier, origin section, description, dependencies, and traceability anchors. Identifiers from S06 (SP-nn) and from S13/S14/S15 (SPK-Snn-nn) are preserved to maintain traceability.

**Identifier reconciliation note**: Some spikes surfaced in S13, S14, and S15 refine or expand spikes already described in S06. Where the S06 spike and the downstream section spike cover the same validation concern, this is noted explicitly in the catalogue entry. The S06 band position of the underlying spike is preserved.

---

**BAND A — Scope / Source / Security Guardrails**
*(Precedence: must be initiated or unblocked before Band B proceeds)*

| ID | Title | Origin | Description | Depends On | Traceability |
|----|-------|--------|-------------|------------|-------------|
| SP-01 | Source Policy Enforcement | S06 Band A | Validate that the minimal source policy (docs.odoo.com + github.com/odoo/odoo) is operationally enforceable: detect unauthorized sources, trigger Knowledge Gap mechanism, block non-policy source use. Integrates S12 Knowledge Gap and VAL-01/VAL-09 control points. | None | DEC-ACCEPTED-163; AP-06; AP-12; CRIT-03; VAL-01; VAL-09; S12 |
| SP-02 | Secrets Posture | S06 Band A | Validate baseline secrets handling posture: no secrets embedded in source, OpenCode runtime, or evidence artifacts. Integrates S14 CA-1 conceptual constraints. Refined by SPK-S14-01 (see Band B). | None (SPK-S14-01 extends this) | AP-10; AP-11; CRIT-02; RISK-021; RISK-027; S14 CA-1; DEC-ACCEPTED-045 |
| SP-03 | V1 / Post-V1 Boundary Enforcement | S06 Band A | Validate that anti-scope-creep controls are enforceable: mechanisms correctly classify V1-in vs deferred, and boundary changes require owner decision. | SP-01 | BR-01; BR-02; S03; DEC-ACCEPTED-164; CRIT-01 |

---

**BAND B — OpenCode / Odoo 18 Base Capabilities**
*(Precedence: requires Band A unblocked; environment form spike must be initiated within this band)*

| ID | Title | Origin | Description | Depends On | Traceability |
|----|-------|--------|-------------|------------|-------------|
| SP-04 | OpenCode Permissions / Capabilities | S06 Band B | **[OPEN UNCERTAINTY — not resolved]** Validate actual OpenCode permission model and agent capability constraints relevant to CAFL V1 coordination patterns. Resolution requires live OpenCode environment access. Preserved as open uncertainty per S07 and S08. | SP-01, SP-02, SP-03 | AP-02; AP-04; S07; S08; DEC-ACCEPTED-136; DEC-ACCEPTED-137 |
| SP-05 | Commands / Skills Design | S06 Band B | **[OPEN UNCERTAINTY — not resolved]** Validate command candidate and skills/playbook design patterns that are feasible within OpenCode constraints discovered in SP-04. Preserved as open uncertainty per S07 and S08. Depends on SP-04 resolution. | SP-04 (open uncertainty) | AP-02; S07; S08; DEC-ACCEPTED-138; DEC-ACCEPTED-140 |
| SP-06 / SPK-S13-ENV | Odoo 18 Minimal Environment Form | S06 Band B + S13 | Validate exact form of the Odoo 18 execution environment: Docker, virtualenv, or local install. This is the S13 "exact environment form" spike dependency and expands SP-06 from S06. Result determines the concrete environment category used by all subsequent pilot module spikes. **RISK-059 (critical): environment spike is blocking precondition for all pilot module spikes.** | SP-01, SP-02, SP-03 | RISK-059; DEC-ACCEPTED-135; DEC-ACCEPTED-153; AP-08; S13 ENV-CAT-1/2/3; SCH-10; VAL-05; VAL-10; CRIT-06; CRIT-07 |
| SPK-S13-DB | DB Compatibility | S13 | Validate PostgreSQL version compatibility and connection patterns for the selected Odoo 18 environment form. Depends on SP-06/SPK-S13-ENV resolving the environment form. | SP-06/SPK-S13-ENV | RISK-059; DEC-ACCEPTED-135; S13 logical component: PostgreSQL; SCH-10; CRIT-06 |
| SPK-S14-01 | Secrets Handling in Environment | S14 CA-1 | Validate that no secrets are embedded in source, environment config files, or evidence artifacts within the selected Odoo 18 environment. Expands SP-02 for the confirmed environment form. **SPK-S14-01 blocks SPK-S14-02 and SPK-S14-03 (S14 ordering constraint).** Depends on environment form being established (SP-06/SPK-S13-ENV). | SP-06/SPK-S13-ENV, SP-02 | AP-10; AP-11; RISK-021; RISK-027; RISK-040; S14 CA-1; DEC-ACCEPTED-045; DEC-ACCEPTED-059 |

---

**BAND C — Control / Evidence Toolchain and Pilot Module Validations**
*(Precedence: requires Band A and core Band B unblocked; security ordering constraints apply within this band)*

| ID | Title | Origin | Description | Depends On | Traceability |
|----|-------|--------|-------------|------------|-------------|
| SP-07 | Language / Toolchain Scripts | S06 Band C | Validate that the deterministic control toolchain (language selection, script runner, CLI candidates) is compatible with the Odoo 18 environment. | SP-06/SPK-S13-ENV, SP-01 | AP-04; S08; SCH-06; VAL-06; DEC-ACCEPTED-140; CRIT-07 |
| SP-08 | Schemas / Validators Toolchain | S06 Band C | Validate that schema validation and validator execution are feasible within the confirmed environment and toolchain. SP-05 uncertainty noted: if SP-05 is unresolved, command-based validator invocation remains an open design point. | SP-07, SP-05 (open uncertainty noted) | SCH-01..SCH-10; VAL-01..VAL-10; AP-04; S09; S10; DEC-ACCEPTED-145 |
| SP-09 | Storage / Logs Convention | S06 Band C | Validate that the conceptual L1–L4 authority hierarchy and JSONL/YAML/Markdown storage conventions are operationally feasible in the confirmed environment and Git-compatible. | SP-06/SPK-S13-ENV, SP-07 | S11 L1-L4; AP-09; DEC-ACCEPTED-146; SCH-03; SCH-05; VAL-03; VAL-04 |
| SPK-S13-RUNNER | Odoo 18 Test Runner | S13 | Validate that the Odoo 18 test runner mechanism can be invoked within the confirmed environment form to produce evidence-eligible outputs. | SP-06/SPK-S13-ENV, SPK-S13-DB | RISK-059; S13 logical component: test execution mechanism; VAL-05; VAL-10; SCH-10; CRIT-06; DEC-ACCEPTED-135 |
| SP-10 / SPK-S13-EVIDENCE | Evidence Capture for Minimum Cycle | S06 Band C + S13 | Validate that the complete minimum evidence capture cycle is operational: environment event → capture → S11 lifecycle steps → L2 registration. Integrates S13 "evidence capture for minimum cycle" spike dependency. | SP-09, SPK-S13-RUNNER | S11 6-step lifecycle; SCH-05; SCH-10; VAL-05; VAL-06; VAL-10; AP-05; AP-09; RISK-059; CRIT-07 |
| SPK-S13-TRACE | Code Source Traceability | S13 + S15 | Validate that Odoo 18 pilot module source code is traceable to docs.odoo.com and github.com/odoo/odoo per S12 source policy. Applies to both the environment-level traceability (S13) and the pilot module code (S15). | SP-01, SP-06/SPK-S13-ENV, SPK-S14-01 | DEC-ACCEPTED-163; AP-06; AP-12; S12 source policy; S13; S15; VAL-01; VAL-09; SCH-09 |
| SPK-S14-02 | Permissions Model Validation | S14 CA-2 | Validate that the conceptual minimum-access permission model (CA-2) is enforceable within the Odoo 18 environment and the pilot module access model. **Blocked by SPK-S14-01.** Depends on environment form. | SPK-S14-01, SP-06/SPK-S13-ENV | RISK-040; RISK-061; S14 CA-2; AP-10; AP-11; DEC-ACCEPTED-064; DEC-ACCEPTED-076; CRIT-02; CRIT-04 |
| SPK-S14-03 | Security Validation Approach | S14 CA-3/CA-4 | Validate that security validation approach (evidence protection CA-3, security/risk triage CA-4) integrates with the S11 evidence lifecycle and S09/S10 schema-validator controls. **Blocked by SPK-S14-01.** | SPK-S14-01, SP-08, SP-10/SPK-S13-EVIDENCE | RISK-063; S14 CA-3; S14 CA-4; S11 L1-L4; SCH-05; VAL-04; AP-10; DEC-ACCEPTED-092; DEC-ACCEPTED-101 |
| SPK-S15-INSTALL | Pilot Module Installation | S15 | Validate that the conceptual pilot module (InternalRequest, ApprovalRecord, 4-state workflow) can be installed in the confirmed Odoo 18 environment. **Depends on environment form spike (RISK-059 critical precondition) and SPK-S14-01 (no embedded secrets).** | SP-06/SPK-S13-ENV, SPK-S14-01, SPK-S13-DB | RISK-059; S15; S13 logical component: installed pilot module; SCH-10; VAL-10; DEC-ACCEPTED-162; DEC-ACCEPTED-135 |
| SPK-S15-TEST | Test Execution | S15 | Validate that unit, workflow, scope, and source policy tests for the pilot module can be executed via the Odoo 18 test runner and produce evidence-eligible outputs. **Depends on SPK-S14-02 (minimum-access permission model enforced during test execution).** | SPK-S15-INSTALL, SPK-S13-RUNNER, SPK-S14-02 | RISK-059; S15 conceptual test approach; VAL-05; VAL-10; SCH-10; DEC-ACCEPTED-162; CRIT-06; CRIT-07 |
| SPK-S15-ACCESS | Access Model Executable | S15 | Validate that the CA-2 minimum-access permission model is enforceable for the pilot module (InternalRequest, ApprovalRecord) within the Odoo 18 access control mechanisms. **Depends on SPK-S14-02.** | SPK-S14-02, SPK-S15-INSTALL | S15 security model; S14 CA-2; RISK-040; RISK-061; DEC-ACCEPTED-064; SCH-10; VAL-10; CRIT-04 |
| SPK-S14-04 | Compliance Assessment | S14 CA-4 | Validate that the security/risk triage-in-gates posture (CA-4) is sufficient for the V1 pilot scope and that no deferred compliance risk blocks pilot operation. | SPK-S14-02, SPK-S14-03, SPK-S15-ACCESS | RISK-021; RISK-027; RISK-040; RISK-063; S14 CA-4; DEC-ACCEPTED-101; AP-11; CRIT-02; CRIT-03; CRIT-04 |

---

**BAND D — Conditional / Anti-Scope-Creep (Separated from Core V1)**
*(Band D spikes are explicitly separated from core V1 and only activated by an explicit owner decision expanding V1 scope. They must not be treated as V1 core work.)*

| ID | Title | Origin | Condition for Activation | Traceability |
|----|-------|--------|--------------------------|-------------|
| SP-11 | SDK / Server Core | S06 Band D | Activated only if owner decision re-includes SDK/server in V1 scope (currently excluded by DEC-ACCEPTED-164). | DEC-ACCEPTED-164; BR-02; S03; AP-08 |
| SP-12 | OpenAPI / PDF Integration | S06 Band D | Activated only if owner decision authorizes external integrations in V1 scope (currently deferred). | BR-02; S03; DEC-ACCEPTED-164 |
| SP-13 | Frontend / OWL / Playwright | S06 Band D | Activated only if pilot explicitly justifies UI/OWL/Playwright scope and owner grants approval. | BR-02; S03; S15 (UI deferred) |

---

##### 16.5 Execution Order with Justified Dependencies

The following is the authoritative final execution order for V1 core spikes (bands A, B, C). Band D remains conditional and is excluded from this sequencing. The order satisfies RULE-06 (no flat list) with explicit dependency justification.

**Tier 1a — No external dependencies (can be initiated concurrently)**

1. **SP-01** (Source Policy Enforcement) — No predecessor; foundational source policy constraint required by all downstream spikes that touch source artifacts.
2. **SP-02** (Secrets Posture) — No predecessor; foundational security constraint required before any environment or permission model work.

*Justification*: SP-01 and SP-02 have no structural predecessors and establish the source policy and secrets invariants (AP-06, AP-10, AP-11, CRIT-02, CRIT-03) required by all downstream bands. They can be initiated concurrently.

---

**Tier 1b — Depends on SP-01 result (Band A, sequential within Band A)**

3. **SP-03** (V1/Post-V1 Boundary Enforcement) — Depends on SP-01: source policy must be enforceable before boundary enforcement is tested, because SP-03 validates that anti-scope-creep controls correctly classify V1-in vs. deferred content using the same source policy invariants SP-01 establishes.

*Justification*: SP-03 is a Band A guardrail but cannot be initiated concurrently with SP-01 because its validation requires SP-01's result to be available. CRIT-01, AP-06 mandate boundary enforcement as dependent on source policy operationalization. SP-02 may proceed concurrently with or after SP-01 as it has no dependency on SP-01 result.

---

**Tier 2 — Environment form established (requires Tier 1a and Tier 1b complete)**

4. **SP-06 / SPK-S13-ENV** (Odoo 18 Minimal Environment Form) — Depends on SP-01, SP-02, SP-03. **RISK-059 critical**: this spike blocks all pilot module spikes. Environment form (Docker/venv/local) must be confirmed before DB compatibility, test runner, module installation, or evidence capture can be validated.
5. **SPK-S14-01** (Secrets Handling in Environment) — Depends on SP-06/SPK-S13-ENV (environment form known) and SP-02 (baseline posture established). **S14 ordering constraint**: SPK-S14-01 must complete before SPK-S14-02 and SPK-S14-03 are initiated.

*Justification*: SP-06/SPK-S13-ENV is the structural gate for the entire pilot track. SPK-S14-01 must immediately follow because all environment-level and module-level security work is blocked on secrets handling confirmation.

---

**Tier 3 — DB, runner, toolchain (requires SP-06/SPK-S13-ENV complete)**

6. **SPK-S13-DB** (DB Compatibility) — Depends on SP-06/SPK-S13-ENV. Can be concurrent with SP-07 and SPK-S14-01.
7. **SP-07** (Language / Toolchain Scripts) — Depends on SP-06/SPK-S13-ENV and SP-01.
8. **SPK-S13-TRACE** (Code Source Traceability) — Depends on SP-01, SP-06/SPK-S13-ENV, SPK-S14-01.

*Justification*: Once the environment form is confirmed, DB compatibility and toolchain language validation can proceed in parallel. Source traceability requires both the environment form and the secrets posture to be validated.

---

**Tier 4 — Test runner, schemas/validators, storage, permissions (requires Tier 3 complete)**

9. **SPK-S13-RUNNER** (Odoo 18 Test Runner) — Depends on SP-06/SPK-S13-ENV and SPK-S13-DB.
10. **SP-08** (Schemas / Validators Toolchain) — Depends on SP-07. SP-05 open uncertainty noted for command-based invocation.
11. **SP-09** (Storage / Logs Convention) — Depends on SP-06/SPK-S13-ENV and SP-07.
12. **SPK-S14-02** (Permissions Model Validation) — Depends on SPK-S14-01 and SP-06/SPK-S13-ENV. **SPK-S14-01 must be complete (S14 ordering constraint).**

*Justification*: Test runner validation requires DB compatibility confirmed. Schema/validator toolchain requires language choice. Storage convention requires environment and toolchain. SPK-S14-02 is unblocked only after SPK-S14-01 is complete per S14 ordering constraint.

---

**Tier 5 — Evidence capture, security validation, SP-04 (requires Tier 4 complete)**

13. **SP-10 / SPK-S13-EVIDENCE** (Evidence Capture for Minimum Cycle) — Depends on SP-09 and SPK-S13-RUNNER.
14. **SPK-S14-03** (Security Validation Approach) — Depends on SPK-S14-01, SP-08, SP-10/SPK-S13-EVIDENCE. **SPK-S14-01 must be complete (S14 ordering constraint).**
15. **SP-04** (OpenCode Permissions / Capabilities) — **[OPEN UNCERTAINTY]** Depends on SP-01, SP-02, SP-03 at minimum. Requires live OpenCode environment. Resolution unblocks SP-05 and any command-based invocation patterns in SP-08.

*Justification*: Evidence capture requires both storage convention and test runner to be operational. Security validation approach requires evidence capture to be testable. SP-04 is placed at this tier because it requires the Band A guardrails but its resolution path is external (OpenCode live environment); it does not block pilot module installation work on the Odoo track.

---

**Tier 6 — Pilot module installation and access model (requires Tier 5 complete on relevant paths)**

16. **SPK-S15-INSTALL** (Pilot Module Installation) — Depends on SP-06/SPK-S13-ENV, SPK-S14-01, SPK-S13-DB.
17. **SPK-S15-ACCESS** (Access Model Executable) — Depends on SPK-S14-02 and SPK-S15-INSTALL.

*Justification*: Module installation is unblocked once the environment is confirmed, DB is compatible, and the secrets posture is validated (no embedded secrets in module). Access model validation requires both the permissions model (SPK-S14-02) and the installed module.

---

**Tier 7 — Test execution and SP-05 (requires Tier 6 complete on relevant paths)**

18. **SPK-S15-TEST** (Test Execution) — Depends on SPK-S15-INSTALL, SPK-S13-RUNNER, SPK-S14-02.
19. **SP-05** (Commands / Skills Design) — **[OPEN UNCERTAINTY]** Depends on SP-04 resolution (open uncertainty). Cannot be scheduled until SP-04 produces a result.

*Justification*: Test execution requires module installed, runner validated, and permission model enforced. SP-05 is unschedulable until SP-04 resolves.

---

**Tier 8 — Compliance and full security gate (requires Tier 7 complete)**

20. **SPK-S14-04** (Compliance Assessment) — Depends on SPK-S14-02, SPK-S14-03, SPK-S15-ACCESS.

*Justification*: Compliance assessment is the final security gate; it can only be completed once permissions, security validation approach, and access model are all validated.

---

**Band D Conditional Spikes (not sequenced in V1 core)**

SP-11, SP-12, SP-13 remain conditional and separated. They are activated only by an explicit owner decision per S03 BR-02 and DEC-ACCEPTED-164.

---

##### 16.6 S12 Knowledge Gaps and Curation Requests as Spike Inputs

Per S12 handoff, unresolved Knowledge Gaps and pending Curation Requests are potential spike inputs to the S16 consolidated list. This section does not close Knowledge Gaps or approve Curation Requests (those are owner-gated per S12 governance). The following integration rules apply:

- **Knowledge Gap triggers (VAL-01, VAL-09)**: Any spike that touches source policy enforcement (SP-01, SPK-S13-TRACE) must respect the Knowledge Gap mechanism defined in S12. If a source reference needed during spike execution is not covered by the minimal source policy, a Knowledge Gap must be opened and registered before the spike can use that source.
- **Curation Request flow**: Any spike result that implies an expansion of the minimal source policy must produce a Curation Request for owner review; it cannot self-approve source expansion.
- **S11 evidence lifecycle applies**: Spike execution outputs that enter the evidence chain must follow the S11 6-step lifecycle (origin, capture, validation, eligibility evaluation, governed registration, authoritative reference).

##### 16.7 SP-04 and SP-05 Open Uncertainty Treatment

SP-04 and SP-05 are preserved as open uncertainties per S07 (OpenCode Operating Design) and S08 (Mechanism Split). They appear in this section's spike catalogue and execution order but carry the explicit **[OPEN UNCERTAINTY]** marker. The following constraints apply:

- SP-04 and SP-05 must not be resolved by this section or by any downstream Blueprint section without an explicit owner decision.
- Any design element in later Blueprint sections (S17, S18, S19) that depends on SP-04/SP-05 resolution must be marked as conditional on SP-04/SP-05 outcome.
- SP-05 is blocked by SP-04; both are placed in the execution order at their earliest feasible tier but their actual resolution remains external.

##### 16.8 Cross-Section Guidance and Handoff Rules

**Handoffs from S16 to downstream sections**:

| Receiving Section | Handoff Content |
|-------------------|-----------------|
| S17 — Bidirectional Traceability Matrix | Full consolidated spike catalogue (SP-01..SP-13 + SPK-Snn) with traceability anchors to TOM, CRIT-01..07, accepted decisions, and risks. Execution order provides the dependency chain for traceability links. |
| S18 — Blueprint Outputs to Backlog | Spike catalogue by band (A, B, C, D conditional) as candidate backlog categories. Each spike entry identifies the type of technical work and the blocked dependencies, informing backlog category structure. |
| S19 — Acceptance Criteria | Spike completion conditions are candidate acceptance criteria inputs. Band A/B/C spikes with RISK-059, RISK-021, RISK-027 must appear in acceptance criteria. Open uncertainties SP-04/SP-05 must be flagged as conditional acceptance criteria. |

**Coordination constraints**:
- S17 must use the S16 consolidated catalogue as the spike-side input to the traceability matrix; it must not reconstruct spike identifiers independently.
- S18 must not create a detailed implementation backlog; it uses spike bands as category inputs only.
- S19 must not close spike validation results; it references spike completion conditions as acceptance criteria.

##### 16.9 Explicit Non-Decisions

The following are explicitly not decided by this section:

- **Execution form of any spike**: how a spike will be run (toolchain, environment, agent, command, manual) is not decided here. Blueprint sections do not create runtime artifacts.
- **Resolution of SP-04 or SP-05**: open uncertainties per S07, S08; not resolved by S16.
- **Closure of Knowledge Gaps or approval of Curation Requests**: owner-gated per S12.
- **Physical environment**: whether Docker, venv, or local is selected (that is what SP-06/SPK-S13-ENV validates).
- **Physical schemas, validators, scripts, commands, agents, or toolchain implementations**: RULE-09 and S01 non-goals apply.
- **Band D activation**: SP-11, SP-12, SP-13 are not activated without explicit owner scope decision.
- **Pilot broadening or source policy expansion**: V1 pilot remains internal requests/simple approvals per DEC-ACCEPTED-162; source policy remains docs.odoo.com + github.com/odoo/odoo per DEC-ACCEPTED-163.
- **CRIT-01..07 re-opening or TOM revision**: fixed per S01 and DEC-ACCEPTED-161.

##### 16.10 Open Questions and Owner Decisions Required

| ID | Question | Status | Impact if Unresolved |
|----|----------|--------|----------------------|
| OQ-S16-01 | SP-04 (OpenCode permissions/capabilities): when will live OpenCode environment access be available for spike resolution? | Open uncertainty per S07, S08 | SP-05 and command-based invocation patterns in SP-08 remain unschedulable |
| OQ-S16-02 | SP-05 (Commands/skills design): blocked on SP-04 resolution. | Open uncertainty per S08 | Command-based mechanism candidates remain conceptual |
| OQ-S16-03 | Band D activation (SP-11..SP-13): owner must make an explicit scope decision to activate any Band D spike. | Owner decision required | Band D spikes remain inactive; SDK/server, external integrations, OWL/Playwright out of V1 core |
| OQ-S16-04 | Should any Knowledge Gap or Curation Request open at the time of spike execution be registered before the affected spike proceeds? | Owner decision required for policy | Spike execution touching non-policy sources would be non-compliant per DEC-ACCEPTED-163 |

##### 16.11 Acceptance Criteria

| Criterion | Verification Method |
|-----------|---------------------|
| AC-S16-01: Every V1 core spike (bands A, B, C) is present in the consolidated catalogue with a unique identifier, origin, description, dependencies, and traceability anchors. | Verifier reviews catalogue completeness against S06 SP-01..SP-13 and S13/S14/S15 spike inputs. |
| AC-S16-02: SP-01..SP-13 from S06 are incorporated with bands A→B→C structure preserved and band D kept conditional/separated. | Verifier confirms band labels match S06 band structure and D is not sequenced in core V1 order. |
| AC-S16-03: S13 five environment spike dependencies are integrated with RISK-059 priority noted. | Verifier confirms SPK-S13-ENV, SPK-S13-DB, SPK-S13-RUNNER, SPK-S13-EVIDENCE, SPK-S13-TRACE are present with RISK-059 traceability. |
| AC-S16-04: S14 four security spikes (SPK-S14-01..04) are integrated with S14 ordering constraint (SPK-S14-01 blocks SPK-S14-02 and SPK-S14-03). | Verifier confirms SPK-S14-01 appears before SPK-S14-02 and SPK-S14-03 in the execution order. |
| AC-S16-05: S15 4+2 technical spike dependencies (SPK-S15-INSTALL, SPK-S15-TEST, SPK-S15-ACCESS + SPK-S13-TRACE, SPK-S14-01, SPK-S14-02 inherited) are integrated. | Verifier confirms all six S15 spike dependencies are present with correct predecessors. |
| AC-S16-06: SP-04 and SP-05 are preserved as open uncertainties with **[OPEN UNCERTAINTY]** markers; they are not resolved. | Verifier confirms no resolution claim for SP-04 or SP-05. |
| AC-S16-07: No flat list; RULE-06 satisfied. Every spike in the execution order carries justified dependency justification. | Verifier confirms execution order section contains no entry without a "Depends On" or justification clause. |
| AC-S16-08: Knowledge Gaps and Curation Requests from S12 are referenced as spike inputs without closing gaps or approving requests. | Verifier confirms §16.6 references S12 mechanism without claiming gap closure or request approval. |
| AC-S16-09: No forbidden artifacts created (no runtime, agents, commands, schemas, validators, scripts, RAG, backlog, PRD, SDD, implementation). | Verifier confirms no forbidden content in section. |
| AC-S16-10: All spikes trace to at least one of: TOM, CRIT-01..07, accepted decision, or applicable risk. | Verifier spot-checks traceability column in spike catalogue. |
| AC-S16-11: V1 boundaries preserved: Odoo-only, Odoo 18, internal requests/simple approvals pilot, minimal source policy, framework/ excluded. | Verifier confirms no V1 scope expansion in section content. |

##### 16.12 Section Output and Handoff

**Primary output of S16**: The consolidated, ordered spike and technical validation catalogue for CAFL V1, with justified execution order, dependency chain, traceability anchors, and integration of all upstream spike inputs from S06, S13, S14, and S15.

**Handoff package to S17 (Bidirectional Traceability Matrix)**:
- Complete spike catalogue with identifiers SP-01..SP-13 and SPK-Snn entries.
- Dependency chain (Tiers 1–8) for traceability link generation.
- Traceability anchors per spike (TOM, CRIT, decisions, risks).
- Open uncertainties SP-04/SP-05 flagged for conditional traceability handling.

**Handoff package to S18 (Blueprint Outputs to Backlog)**:
- Spike bands A, B, C as candidate backlog category structure.
- Band D conditional spikes as a separate post-V1 or owner-decision-gated category.
- Open uncertainty spikes (SP-04/SP-05) as a conditional category.

**Handoff package to S19 (Acceptance Criteria)**:
- AC-S16-01..AC-S16-11 as candidate acceptance criteria for this section's verification.
- Spike completion conditions as candidate V1 milestone acceptance criteria.
- RISK-059 critical path (SP-06/SPK-S13-ENV → SPK-S13-DB → SPK-S15-INSTALL → SPK-S15-TEST) as critical acceptance criterion candidate.
- SP-04/SP-05 open uncertainties as conditional acceptance criteria candidates.

#### 17. Bidirectional Traceability Matrix

Status: closed

Owner approval: approved

##### 17.1 Status and Inputs

**Status**: in-verification.

**Inputs**:
- S01-S16 elaboradas; S16 aprobado como fuente autoritativa del catalogo consolidado de spikes.
- TOM aprobado por DEC-ACCEPTED-161.
- CRIT-01..CRIT-07 approved.
- Decisiones aceptadas aplicables, especialmente DEC-ACCEPTED-135, 136, 137, 138, 140, 144, 145, 146, 149, 153, 158, 161, 162, 163 y 164.
- Riesgos relevantes: RISK-006, 010, 021, 027, 040, 043, 044, 051, 052, 054, 055, 057, 059, 061, 063, 064, 065, 066 y 067.

##### 17.2 Purpose

Esta seccion define la matriz conceptual de trazabilidad bidireccional del Blueprint CAFL V1. La matriz responde a RULE-04 y RULE-05:

- **TOM -> Blueprint**: cada requerimiento operativo relevante del TOM queda enlazado a uno o mas componentes del Blueprint.
- **Blueprint -> TOM/CRIT/Decision**: cada componente del Blueprint queda enlazado a al menos un requerimiento TOM, CRIT aprobado o decision aceptada.

La matriz no aprueba el Blueprint, no cierra acceptance criteria finales, no ejecuta spikes y no sustituye la aprobacion owner. La aprobacion explicita del owner sigue siendo obligatoria.

##### 17.3 Specific Restrictions

- Usar el catalogo consolidado S16 como fuente autoritativa de spikes; no reconstruir identifiers fuera de SP-01..SP-13 y SPK-Snn ya consolidados.
- Preservar SP-04 y SP-05 como **conditional / open uncertainty**; no resolverlos.
- Preservar SP-11, SP-12 y SP-13 como **conditional / post-V1 / owner-decision-gated**; no activarlos como core V1.
- Seguir la estructura logica de SCH-02: identifier, origin, destination, relationship type, mandatory, state, evidence, gaps/conflicts, consuming section.
- No crear schemas fisicos, validators reales, scripts, commands, agents ejecutables, runtime, RAG/base vectorial, backlog, PRD, SDD ni implementacion.
- Preservar limites V1: Odoo-only, Odoo 18, piloto solicitudes internas / aprobaciones simples, source policy minima docs.odoo.com + github.com/odoo/odoo, SDK/server fuera de core V1 y `framework/` excluido como input.

##### 17.4 Traceability Anchor Index

Los siguientes aliases son identificadores internos de esta matriz para referenciar requerimientos ya aceptados; no crean requisitos nuevos.

| TOM anchor | Requerimiento operativo TOM | Authority anchors |
| --- | --- | --- |
| TOM-01 | `project-truth/` como fuente de verdad; narrativa LLM no es estado autoritativo. | DEC-ACCEPTED-001, 107; CRIT-06; AP-01 |
| TOM-02 | V1 Odoo-only sobre Odoo 18. | DEC-ACCEPTED-016, 135; CRIT-01, CRIT-07; BR-01 |
| TOM-03 | Flujo end-to-end verificable desde idea owner hasta modulo Odoo tecnicamente listo. | DEC-ACCEPTED-021, 153, 156; CRIT-01, CRIT-02 |
| TOM-04 | Modelo hibrido progresivo: OpenCode + agents/commands/control deterministico/rules/skills, no agents-only. | DEC-ACCEPTED-056, 136, 137, 138; CRIT-03, CRIT-07; AP-02..AP-05 |
| TOM-05 | PRD ligero, SDD ligero, task/context packet, DoR y contratos/gates obligatorios antes de ejecucion. | DEC-ACCEPTED-039, 041, 074, 077, 078, 079, 091; CRIT-02, CRIT-04, CRIT-05 |
| TOM-06 | Evidencia reproducible, logs, storage auditable y trazabilidad contract -> gate -> evidence. | DEC-ACCEPTED-100, 111, 114, 115, 146; CRIT-06, CRIT-07; AP-04, AP-05, AP-09 |
| TOM-07 | Separacion de recommendation, verification, decision; no autocierre ni self-approval. | DEC-ACCEPTED-063, 094; CRIT-05; AP-04, AP-05 |
| TOM-08 | Source policy minima, Knowledge Gap y Curation Request sin busqueda web libre. | DEC-ACCEPTED-126, 127, 128, 150, 163; CRIT-06, CRIT-07; AP-06, AP-12 |
| TOM-09 | Seguridad/riesgo/compliance transversal y secrets/access control. | DEC-ACCEPTED-045, 064, 076, 092, 101; CRIT-02..CRIT-05; AP-10, AP-11, AP-12 |
| TOM-10 | Rework acotado, blockers, owner escalation y approval log para decisiones criticas. | DEC-ACCEPTED-059, 067, 096, 104, 118; CRIT-03, CRIT-05, CRIT-06 |
| TOM-11 | Piloto V1 confirmado: solicitudes internas / aprobaciones simples, sin PRD/SDD/backlog final en Blueprint. | DEC-ACCEPTED-162; BR-01; S15 |
| TOM-12 | Automatizacion minima suficiente: validators, trazabilidad, evidencia, Odoo install/update/test y source policy basics. | DEC-ACCEPTED-139, 140, 145, 153; CRIT-07 |
| TOM-13 | V1 / post-V1 boundary: SDK/server, RAG/vector, dashboard/UI amplio, CI/CD completo, integraciones y capacidades amplias diferidas. | DEC-ACCEPTED-148, 149, 157, 164; BR-02 |
| TOM-14 | Technical validations/spikes formalmente planificados antes de materializar decisiones fisicas o incertidumbres. | DEC-ACCEPTED-142, 158; RISK-059, RISK-061, RISK-063; S16 |

##### 17.5 Link Type Legend (SCH-02 aligned)

| Field | Meaning in this matrix |
| --- | --- |
| Identifier | Stable link ID `TM-S17-nnn`. |
| Origin | TOM requirement, Blueprint component, CRIT, decision, risk, spike, schema, validator or section component. |
| Destination | The traced target component/anchor. |
| Relationship type | `satisfies`, `constrains`, `derives-from`, `validates`, `blocks-if-unresolved`, `conditional-post-v1`, `evidence-for` or `handoff-to`. |
| Mandatory | `yes`, `conditional`, or `post-V1-owner-gated`. |
| State | `active`, `conditional-open-uncertainty`, `conditional-post-V1`, or `owner-approval-pending`. |
| Evidence | Source section or authority anchor supporting the link. |
| Gaps/conflicts | `none` unless open uncertainty or owner gate is explicitly required. |
| Consuming section | Blueprint section(s) expected to consume the link. |

##### 17.6 TOM -> Blueprint Matrix

| Link ID | Origin | Destination Blueprint components | Relationship type | Mandatory | State | Evidence | Gaps/conflicts | Consuming section |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| TM-S17-001 | TOM-01 | S01, S02 AP-01, S05, S09 SCH-01/SCH-02, S10 VAL-01/VAL-02, S11 L1-L4, S17 | satisfies/constrains | yes | active | S01, S02, S05, S09-S11; CRIT-06 | none | S17-S19 |
| TM-S17-002 | TOM-02 | S01, S03 BR-01, S04, S13, S15, S16 SP-06/SPK-S13-ENV, SPK-S15-INSTALL/TEST | satisfies | yes | active | DEC-ACCEPTED-135; S13-S16 | none | S17-S19 |
| TM-S17-003 | TOM-03 | S03, S04, S06, S09-S11, S13-S16, SCH-03/04/05/10, VAL-03/04/05/10 | satisfies/evidence-for | yes | active | DEC-ACCEPTED-153, 156; S09-S16 | none | S18-S19 |
| TM-S17-004 | TOM-04 | S02 AP-02..AP-05, S04, S05, S07, S08, S10, S16 SP-04/SP-05/SP-07/SP-08 | satisfies/constrains | yes | active with open uncertainty for SP-04/SP-05 | DEC-ACCEPTED-136, 137, 138, 140; S07-S08/S16 | SP-04/SP-05 remain unresolved | S17-S19 |
| TM-S17-005 | TOM-05 | S08 mechanism split, S09 SCH-03/SCH-04/SCH-08, S10 VAL-03/VAL-04/VAL-08, S11, S12 | satisfies | yes | active | CRIT-04/05; DEC-ACCEPTED-074, 077, 078, 079 | none | S18-S19 |
| TM-S17-006 | TOM-06 | S09 SCH-02/SCH-05/SCH-06/SCH-07, S10 VAL-02/05/06/07, S11, S13 evidence events, S15 evidence, S16 SP-09/SP-10 | satisfies/evidence-for | yes | active | CRIT-06; DEC-ACCEPTED-100, 111, 114, 115, 146 | none | S17-S19 |
| TM-S17-007 | TOM-07 | S02 AP-04/AP-05, S07, S08, S10 validators as controls, S11 evidence lifecycle, S17 non-approval boundary | constrains | yes | active | DEC-ACCEPTED-063, 094; CRIT-05 | none | S17-S19 |
| TM-S17-008 | TOM-08 | S02 AP-06/AP-12, S05, S09 SCH-09, S10 VAL-01/VAL-09, S12, S16 SP-01/SPK-S13-TRACE | satisfies/constrains | yes | active | DEC-ACCEPTED-126, 127, 128, 150, 163 | none | S17-S19 |
| TM-S17-009 | TOM-09 | S02 AP-10/AP-11/AP-12, S09 SCH-04/SCH-05/SCH-10, S10 VAL-04/VAL-10, S14 CA-1..CA-4, S15 security, S16 SP-02/SPK-S14-01..04/SPK-S15-ACCESS | satisfies/constrains | yes | active | DEC-ACCEPTED-045, 064, 076, 092, 101; RISK-021/027/040/063 | none | S17-S19 |
| TM-S17-010 | TOM-10 | S02 AP-05/AP-12, S09 SCH-03/SCH-04, S10 VAL-03/VAL-04, S11 logs, S12 owner-gated curation, S16 open questions | satisfies/constrains | yes | active | DEC-ACCEPTED-059, 067, 096, 104, 118 | owner approval remains external | S18-S19 |
| TM-S17-011 | TOM-11 | S01, S03 BR-01, S13, S14, S15 all pilot module components, S16 SPK-S15-INSTALL/TEST/ACCESS | satisfies | yes | active | DEC-ACCEPTED-162; S15 | none | S18-S19 |
| TM-S17-012 | TOM-12 | S09 SCH-01..SCH-10, S10 VAL-01..VAL-10, S11, S13, S16 SP-07/SP-08/SP-09/SP-10/SPK-S15-TEST | satisfies/validates | yes | active | DEC-ACCEPTED-139, 140, 145, 153 | none | S18-S19 |
| TM-S17-013 | TOM-13 | S03 BR-02/BR-03/BR-04, S04/S05 non-goals, S12 no RAG, S15 no broad pilot, S16 SP-11/SP-12/SP-13 | constrains/conditional-post-v1 | conditional | conditional-post-V1 | DEC-ACCEPTED-148, 149, 157, 164 | owner decision required to activate | S18-S19 |
| TM-S17-014 | TOM-14 | S06 initial spikes, S13 env spikes, S14 security spikes, S15 pilot spikes, S16 consolidated order | validates/handoff-to | yes | active except conditional entries | DEC-ACCEPTED-142, 158; RISK-059/061/063 | SP-04/SP-05 open; Band D post-V1 | S17-S19 |

##### 17.7 Blueprint Sections -> Authority Matrix

| Link ID | Origin Blueprint component | Destination authority anchors | Relationship type | Mandatory | State | Evidence | Gaps/conflicts | Consuming section |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| TM-S17-015 | S01 Blueprint Scope and Non-Goals | TOM-01..TOM-14; CRIT-01..07; DEC-ACCEPTED-161..164 | derives-from/constrains | yes | active | S01 context summary | none | S17-S19 |
| TM-S17-016 | S02 Architecture Principles AP-01..AP-12 | TOM-01..TOM-14; CRIT-01..07; DEC-ACCEPTED-136/138/140/145/146/162/163/164 | derives-from/constrains | yes | active | S02 context summary | none | S17-S19 |
| TM-S17-017 | S03 V1/Post-V1 Boundary BR-01..BR-04 | TOM-02, TOM-11, TOM-13; DEC-ACCEPTED-148/149/157/162/164; CRIT-01/07 | constrains | yes | active | S03 context summary | none | S17-S19 |
| TM-S17-018 | S04 Runtime Layout Candidate | TOM-01, TOM-04, TOM-06, TOM-08, TOM-09, TOM-13; DEC-ACCEPTED-138/146/163/164 | derives-from | yes | active | S04 context summary | none | S17-S19 |
| TM-S17-019 | S05 Source-vs-Runtime Structure | TOM-01, TOM-04, TOM-06, TOM-08, TOM-13; DEC-ACCEPTED-107/138/146/163 | constrains | yes | active | S05 context summary | none | S17-S19 |
| TM-S17-020 | S06 Initial Spike Map SP-01..SP-13 | TOM-08, TOM-09, TOM-13, TOM-14; DEC-ACCEPTED-158/163/164; RISK-059/061/063 | validates/handoff-to | yes/conditional | active + conditional Band D | S06/S16 | SP-04/SP-05 open; SP-11..13 post-V1 | S16-S19 |
| TM-S17-021 | S07 OpenCode Operating Design | TOM-04, TOM-07; AP-02..AP-05; DEC-ACCEPTED-136/137/138; SP-04/SP-05 | derives-from/constrains | yes | active with open uncertainty | S07/S16 | SP-04/SP-05 unresolved | S17-S19 |
| TM-S17-022 | S08 Mechanism Split | TOM-04, TOM-05, TOM-06; AP-02..AP-05/AP-07/AP-10/AP-12; DEC-ACCEPTED-056/068/069/136/137/138/140 | derives-from | yes | active | S08 context summary | none | S17-S19 |
| TM-S17-023 | S09 Schemas SCH-01..SCH-10 | TOM-01, TOM-05, TOM-06, TOM-08, TOM-12; CRIT-06/07; DEC-ACCEPTED-144; AP-01/AP-04/AP-06/AP-09 | satisfies | yes | active | S09 context summary | none | S17-S19 |
| TM-S17-024 | S10 Validators VAL-01..VAL-10 | TOM-05, TOM-06, TOM-08, TOM-12; CRIT-06/07; DEC-ACCEPTED-145; AP-04/AP-05/AP-09 | satisfies/validates | yes | active | S10 context summary | none | S17-S19 |
| TM-S17-025 | S11 State/Logs/Evidence Storage | TOM-01, TOM-06, TOM-07, TOM-10; CRIT-06; DEC-ACCEPTED-107/111/114/115/146 | satisfies/evidence-for | yes | active | S11 context summary | none | S17-S19 |
| TM-S17-026 | S12 Knowledge Base and Source Policy | TOM-08, TOM-10, TOM-13; CRIT-06/07; DEC-ACCEPTED-126/127/128/150/163; RISK-043/044/051/052/054/062 | satisfies/constrains | yes | active | S12 context summary | Curation remains owner-gated | S17-S19 |
| TM-S17-027 | S13 Odoo 18 Execution Environment | TOM-02, TOM-03, TOM-06, TOM-11, TOM-12, TOM-14; DEC-ACCEPTED-135/153/162/163; RISK-059/010 | satisfies/validates | yes | active | S13 context summary | exact physical environment remains spike-dependent | S17-S19 |
| TM-S17-028 | S14 Security and Secrets CA-1..CA-4 | TOM-09, TOM-10, TOM-14; AP-10/AP-11/AP-12; DEC-ACCEPTED-045/059/064/076/092/101/162/163; RISK-021/027/040/059/061/063 | satisfies/constrains | yes | active | S14 context summary | none | S17-S19 |
| TM-S17-029 | S15 Pilot Module Blueprint | TOM-02, TOM-03, TOM-09, TOM-11, TOM-12; DEC-ACCEPTED-135/153/162/163; BR-01; SCH-10; VAL-05/VAL-10; RISK-059/010 | satisfies | yes | active | S15 context summary | implementation/test execution remain spike-dependent | S17-S19 |
| TM-S17-030 | S16 Spikes and Technical Validations final order | TOM-08, TOM-09, TOM-13, TOM-14; DEC-ACCEPTED-158/163/164; RISK-059/061/063; S06/S13/S14/S15 | validates/handoff-to | yes/conditional | active + conditional entries | S16 approved catalogue | SP-04/SP-05 open; Band D post-V1 | S17-S19 |

##### 17.8 Detailed Component Coverage Matrix

| Link ID | Origin | Destination | Relationship type | Mandatory | State | Evidence | Gaps/conflicts | Consuming section |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| TM-S17-031 | AP-01..AP-12 | S02, S04-S16 applicable constraints | constrains | yes | active | S02; TOM anchors | none | S17-S19 |
| TM-S17-032 | BR-01 | S03, S13, S15, S16 core V1 spikes | constrains | yes | active | S03; DEC-ACCEPTED-135/162 | none | S17-S19 |
| TM-S17-033 | BR-02 | S03, S16 SP-11/SP-12/SP-13 | conditional-post-v1 | conditional | conditional-post-V1 | S03; DEC-ACCEPTED-164 | owner decision required to activate | S18-S19 |
| TM-S17-034 | BR-03/BR-04 | S03, S14 CA-1..CA-4, S15 security/evidence | constrains | yes | active | S03/S14/S15 | none | S17-S19 |
| TM-S17-035 | SCH-01 Authority Source | TOM-01; S05; VAL-01; S12 source policy | satisfies | yes | active | S09/S10/S12 | none | S17-S19 |
| TM-S17-036 | SCH-02 Traceability Link | TOM-01/TOM-06; S17 matrix; VAL-02 | satisfies | yes | active | S09/S10/S17 | none | S17-S19 |
| TM-S17-037 | SCH-03 Work State | TOM-05/TOM-10; S11; VAL-03 | satisfies | yes | active | S09-S11 | none | S18-S19 |
| TM-S17-038 | SCH-04 Gate and Approval | TOM-05/TOM-07/TOM-10; S11; VAL-04 | satisfies | yes | active | S09-S11 | owner approval remains external | S18-S19 |
| TM-S17-039 | SCH-05 Evidence Record | TOM-06; S11/S13/S15; VAL-05 | satisfies/evidence-for | yes | active | S09-S11/S13/S15 | none | S17-S19 |
| TM-S17-040 | SCH-06 Deterministic Control | TOM-04/TOM-12; S08/S10; VAL-06 | satisfies | yes | active | S09/S10 | none | S17-S19 |
| TM-S17-041 | SCH-07 Runtime Output / Candidate Evidence | TOM-01/TOM-06/TOM-07; S11; VAL-07 | constrains | yes | active | S09-S11 | runtime output not authority by itself | S17-S19 |
| TM-S17-042 | SCH-08 Context Packet | TOM-05; S08/S12; VAL-08 | satisfies | yes | active | S09/S10/S12 | none | S18-S19 |
| TM-S17-043 | SCH-09 Source Policy / Knowledge Gap | TOM-08; S12; VAL-01/VAL-09; SP-01/SPK-S13-TRACE | satisfies/constrains | yes | active | S09/S10/S12/S16 | source expansion owner-gated | S17-S19 |
| TM-S17-044 | SCH-10 Odoo Pilot Artifact | TOM-02/TOM-11/TOM-12; S13/S15; VAL-10 | satisfies | yes | active | S09/S10/S13/S15 | physical Odoo artifacts not created | S17-S19 |
| TM-S17-045 | VAL-01..VAL-10 | SCH-01..SCH-10; TOM-06/TOM-08/TOM-12; S10 | validates | yes | active | S10 | conceptual validators only | S17-S19 |
| TM-S17-046 | CRIT-01..CRIT-07 | S01-S16 all components | derives-from | yes | active | critical-map.md; S01-S16 summaries | none | S17-S19 |
| TM-S17-047 | Accepted decisions referenced by S01-S16 | S01-S16, AP, BR, SCH, VAL, spikes and pilot components | constrains/derives-from | yes | active | accepted.md; section summaries | none | S17-S19 |
| TM-S17-048 | Relevant risks | S06/S13/S14/S15/S16 and controls in S09-S12 | constrains/validates | yes | active | risks.md; S16 catalogue | none | S17-S19 |
| TM-S17-049 | S13 logical components: Odoo 18 instance, PostgreSQL, installed pilot module, test execution mechanism, evidence capture mechanism, conceptual execution trigger, Odoo 18 source reference | TOM-02/TOM-03/TOM-06/TOM-08/TOM-11/TOM-12; SCH-05/SCH-06/SCH-10; VAL-05/VAL-10; SPK-S13-* | satisfies/validates | yes | active | S13/S16 | physical environment spike-dependent | S17-S19 |
| TM-S17-050 | S14 CA-1..CA-4 | TOM-09/TOM-10; AP-10/AP-11/AP-12; SPK-S14-01..04; S15 security | constrains/validates | yes | active | S14/S16 | none | S17-S19 |
| TM-S17-051 | S15 pilot components: InternalRequest, ApprovalRecord, form/list/search views, four-state workflow, conceptual security, candidate evidence events, test approach | TOM-02/TOM-03/TOM-09/TOM-11/TOM-12; DEC-ACCEPTED-162/163; SCH-10; VAL-05/VAL-10; SPK-S15-* | satisfies | yes | active | S15/S16 | executable module not created; tests spike-dependent | S17-S19 |

##### 17.9 Spike Traceability Matrix (S16 Authoritative Catalogue)

| Link ID | Origin spike | Destination authority anchors | Relationship type | Mandatory | State | Evidence | Gaps/conflicts | Consuming section |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| TM-S17-052 | SP-01 Source Policy Enforcement | TOM-08; DEC-ACCEPTED-163; AP-06/AP-12; CRIT-03; VAL-01/VAL-09; S12 | validates | yes | active | S16 | none | S18-S19 |
| TM-S17-053 | SP-02 Secrets Posture | TOM-09; AP-10/AP-11; CRIT-02; RISK-021/027; S14 CA-1; DEC-ACCEPTED-045 | validates | yes | active | S16 | none | S18-S19 |
| TM-S17-054 | SP-03 V1/Post-V1 Boundary Enforcement | TOM-13; BR-01/BR-02; S03; DEC-ACCEPTED-164; CRIT-01 | validates | yes | active | S16 | none | S18-S19 |
| TM-S17-055 | SP-04 OpenCode Permissions / Capabilities | TOM-04; AP-02/AP-04; S07/S08; DEC-ACCEPTED-136/137; RISK-061 | validates/blocks-if-unresolved | conditional | conditional-open-uncertainty | S16 | open uncertainty; not resolved | S18-S19 |
| TM-S17-056 | SP-05 Commands / Skills Design | TOM-04; AP-02; S07/S08; DEC-ACCEPTED-138/140 | validates/blocks-if-unresolved | conditional | conditional-open-uncertainty | S16 | blocked by SP-04; not resolved | S18-S19 |
| TM-S17-057 | SP-06 / SPK-S13-ENV Odoo 18 Minimal Environment Form | TOM-02/TOM-03/TOM-12/TOM-14; RISK-059; DEC-ACCEPTED-135/153; S13; SCH-10; VAL-05/VAL-10; CRIT-06/07 | validates | yes | active | S16 | environment physical form remains spike result | S18-S19 |
| TM-S17-058 | SPK-S13-DB | TOM-02/TOM-12; RISK-059; DEC-ACCEPTED-135; S13 PostgreSQL; SCH-10; CRIT-06 | validates | yes | active | S16 | none | S18-S19 |
| TM-S17-059 | SPK-S14-01 | TOM-09; AP-10/AP-11; RISK-021/027/040; S14 CA-1; DEC-ACCEPTED-045/059 | validates | yes | active | S16 | none | S18-S19 |
| TM-S17-060 | SP-07 | TOM-04/TOM-12; AP-04; S08; SCH-06; VAL-06; DEC-ACCEPTED-140; CRIT-07 | validates | yes | active | S16 | none | S18-S19 |
| TM-S17-061 | SP-08 | TOM-06/TOM-12; SCH-01..SCH-10; VAL-01..VAL-10; AP-04; S09/S10; DEC-ACCEPTED-145 | validates | yes | active with note | S16 | command invocation conditional on SP-05 | S18-S19 |
| TM-S17-062 | SP-09 | TOM-06; S11 L1-L4; AP-09; DEC-ACCEPTED-146; SCH-03/SCH-05; VAL-03/VAL-04 | validates | yes | active | S16 | none | S18-S19 |
| TM-S17-063 | SPK-S13-RUNNER | TOM-03/TOM-12; RISK-059; S13 test execution mechanism; VAL-05/VAL-10; SCH-10; CRIT-06; DEC-ACCEPTED-135 | validates | yes | active | S16 | none | S18-S19 |
| TM-S17-064 | SP-10 / SPK-S13-EVIDENCE | TOM-06/TOM-12; S11 lifecycle; SCH-05/SCH-10; VAL-05/VAL-06/VAL-10; AP-05/AP-09; RISK-059; CRIT-07 | validates/evidence-for | yes | active | S16 | none | S18-S19 |
| TM-S17-065 | SPK-S13-TRACE | TOM-08; DEC-ACCEPTED-163; AP-06/AP-12; S12/S13/S15; VAL-01/VAL-09; SCH-09 | validates | yes | active | S16 | none | S18-S19 |
| TM-S17-066 | SPK-S14-02 | TOM-09; RISK-040/061; S14 CA-2; AP-10/AP-11; DEC-ACCEPTED-064/076; CRIT-02/04 | validates | yes | active | S16 | blocked by SPK-S14-01 until validated | S18-S19 |
| TM-S17-067 | SPK-S14-03 | TOM-09; RISK-063; S14 CA-3/CA-4; S11 L1-L4; SCH-05; VAL-04; AP-10; DEC-ACCEPTED-092/101 | validates | yes | active | S16 | blocked by SPK-S14-01 until validated | S18-S19 |
| TM-S17-068 | SPK-S15-INSTALL | TOM-02/TOM-11/TOM-12; RISK-059; S15; S13 installed pilot module; SCH-10; VAL-10; DEC-ACCEPTED-162/135 | validates | yes | active | S16 | depends on environment form and secrets posture | S18-S19 |
| TM-S17-069 | SPK-S15-TEST | TOM-03/TOM-11/TOM-12; RISK-059; S15 test approach; VAL-05/VAL-10; SCH-10; DEC-ACCEPTED-162; CRIT-06/07 | validates/evidence-for | yes | active | S16 | depends on install, runner and permissions | S18-S19 |
| TM-S17-070 | SPK-S15-ACCESS | TOM-09/TOM-11; S15 security model; S14 CA-2; RISK-040/061; DEC-ACCEPTED-064; SCH-10; VAL-10; CRIT-04 | validates | yes | active | S16 | depends on permissions model and install | S18-S19 |
| TM-S17-071 | SPK-S14-04 | TOM-09/TOM-10; RISK-021/027/040/063; S14 CA-4; DEC-ACCEPTED-101; AP-11; CRIT-02/03/04 | validates | yes | active | S16 | final security gate after prerequisites | S18-S19 |
| TM-S17-072 | SP-11 SDK / Server Core | TOM-13; DEC-ACCEPTED-149/164; BR-02; AP-08 | conditional-post-v1 | post-V1-owner-gated | conditional-post-V1 | S16 | owner decision required; not core V1 | S18-S19 |
| TM-S17-073 | SP-12 OpenAPI / PDF Integration | TOM-13; BR-02; S03; DEC-ACCEPTED-164 | conditional-post-v1 | post-V1-owner-gated | conditional-post-V1 | S16 | owner decision required; not core V1 | S18-S19 |
| TM-S17-074 | SP-13 Frontend / OWL / Playwright | TOM-13; BR-02; S03; S15 UI deferred | conditional-post-v1 | post-V1-owner-gated | conditional-post-V1 | S16 | owner decision required or pilot justification; not core by default | S18-S19 |

##### 17.10 Gap-Free Coverage Statement

- **TOM coverage**: TOM-01..TOM-14 all map to Blueprint components in §17.6.
- **Section coverage**: S01..S16 all map back to TOM/CRIT/decision anchors in §17.7.
- **Principle/boundary coverage**: AP-01..AP-12 and BR-01..BR-04 are covered in §17.8.
- **Schema/validator coverage**: SCH-01..SCH-10 and VAL-01..VAL-10 are covered in §17.8.
- **Spike coverage**: SP-01..SP-13 and S16 SPK-Snn entries are covered in §17.9 using S16 identifiers only.
- **CRIT coverage**: CRIT-01..CRIT-07 are covered by TM-S17-046 and by section-specific links.
- **Decision coverage**: accepted decisions referenced by S01-S16 are covered by TM-S17-047 and explicit link evidence.
- **Risk coverage**: relevant RISK items are covered by TM-S17-048 and spike/security/environment rows.
- **S13/S14/S15 coverage**: S13 seven logical components, S14 CA-1..CA-4 and S15 pilot module components are covered by TM-S17-049..051 and spike rows.

No unbacked Blueprint component is intentionally retained. Conditional items are not gaps: SP-04/SP-05 are marked open uncertainty, and SP-11..SP-13 are marked post-V1 owner-gated.

##### 17.11 Explicit Non-Decisions

- Esta seccion no aprueba ni cierra el Blueprint completo.
- Esta seccion no concede owner approval ni cambia owner approval de ninguna seccion.
- Esta seccion no ejecuta, reordena ni resuelve spikes; usa S16 como fuente autoritativa.
- Esta seccion no resuelve SP-04/SP-05.
- Esta seccion no activa SP-11, SP-12 ni SP-13.
- Esta seccion no crea runtime, agents ejecutables, commands reales, schemas fisicos, validators reales, scripts, RAG/base vectorial, backlog, PRD, SDD ni implementacion.
- Esta seccion no expande source policy minima ni autoriza fuentes externas sin Curation Request y aprobacion owner.
- Esta seccion no reabre CRIT-01..CRIT-07, TOM aprobado ni decisiones aceptadas.

##### 17.12 Open Questions / Owner Decisions Required

| ID | Question | Status | Impact if unresolved |
| --- | --- | --- | --- |
| OQ-S17-01 | Owner approval of the full Blueprint traceability matrix. | owner-approval-pending | S17 can be verified but cannot approve or close the Blueprint. |
| OQ-S17-02 | SP-04/SP-05 resolution timing. | conditional-open-uncertainty | OpenCode permissions and commands/skills feasibility remain conditional. |
| OQ-S17-03 | Band D activation (SP-11..SP-13). | post-V1-owner-gated | SDK/server, external integrations and advanced frontend/test scope remain outside V1 core. |

##### 17.13 Acceptance Criteria

| Criterion | Verification Method |
| --- | --- |
| AC-S17-01: TOM -> Blueprint links cover all TOM anchors TOM-01..TOM-14. | Verifier reviews §17.6. |
| AC-S17-02: Blueprint -> TOM/CRIT/decision links cover S01..S16. | Verifier reviews §17.7. |
| AC-S17-03: AP-01..AP-12 and BR-01..BR-04 are represented. | Verifier reviews §17.8. |
| AC-S17-04: SCH-01..SCH-10 and VAL-01..VAL-10 are represented. | Verifier reviews §17.8. |
| AC-S17-05: SP-01..SP-13 and SPK-Snn entries are represented using S16 identifiers. | Verifier reviews §17.9 against S16. |
| AC-S17-06: SP-04/SP-05 are marked conditional/open uncertainty and not resolved. | Verifier checks TM-S17-055/056 and §17.11. |
| AC-S17-07: SP-11..SP-13 are marked conditional/post-V1/owner-gated and not activated. | Verifier checks TM-S17-072..074 and §17.11. |
| AC-S17-08: CRIT-01..CRIT-07, accepted decisions and relevant risks are covered. | Verifier checks §17.8 and link evidence. |
| AC-S17-09: S13 logical components, S14 CA-1..CA-4 and S15 pilot components are covered. | Verifier checks TM-S17-049..051. |
| AC-S17-10: Link rows follow SCH-02 fields. | Verifier checks table columns in §17.6..§17.9. |
| AC-S17-11: Matrix is gap-free or explicitly marks conditional/non-core items without resolving them. | Verifier checks §17.10 and open questions. |
| AC-S17-12: No forbidden artifacts or scope expansion are introduced. | Verifier checks §17.3, §17.11 and content. |

##### 17.14 Section Output and Handoff

**Primary output of S17**: bidirectional traceability matrix linking TOM requirements to Blueprint components and Blueprint components back to TOM/CRIT/accepted-decision anchors, with conditional items explicitly marked.

**Handoff to S18 (Blueprint Outputs to Backlog)**:
- Use §17.6..§17.9 to derive only backlog **categories**, not detailed tasks.
- Preserve open uncertainty category for SP-04/SP-05.
- Preserve post-V1 owner-gated category for SP-11..SP-13.
- Do not convert traceability links into implementation work without S18 boundaries and later owner authorization.

**Handoff to S19 (Acceptance Criteria)**:
- Use AC-S17-01..AC-S17-12 as candidate acceptance criteria for traceability closure.
- Include owner approval as a required closure condition; S17 itself does not grant approval.
- Ensure final acceptance criteria preserve RULE-04/RULE-05, V1 boundaries, source policy and forbidden-artifact restrictions.

#### 18. Blueprint Outputs to Backlog

##### 1. Status

Status: closed

Owner approval: approved

##### 2. Purpose

This section translates the approved Blueprint outputs from S01-S17 into conceptual categories of work that may feed a post-Blueprint backlog process. It does not create the backlog itself, does not prioritize or sequence work, and does not authorize implementation.

The purpose is limited to preserving a traceable bridge from the Blueprint to later planning so that future backlog elaboration can remain aligned with the CAFL V1 scope, TOM traceability, accepted decisions, spike dependencies, and global non-goals. The categories below are intentionally domain-level groupings only, in compliance with RULE-08 and RULE-09.

##### 3. Inputs / Scope

Inputs used for this section:

- S01-S17 Blueprint outputs as represented by their approved context summaries and upstream handoffs.
- S17 Bidirectional Traceability Matrix, including TOM-to-Blueprint and Blueprint-to-authority trace anchors.
- S16 consolidated spike catalogue and technical validation dependencies, including conditional and post-V1-gated spike groupings.
- Upstream handoffs from S07-S15 covering OpenCode operating design, mechanism split, schema and validator categories, evidence and storage posture, Knowledge Governance and source policy boundaries, Odoo 18 environment constraints, security and secrets posture, and pilot module component boundaries.
- Global Blueprint non-goals and acceptance criteria, especially the prohibitions on runtime creation, executable agents, real commands, physical schemas, real validators, scripts, RAG/vector base, detailed technical backlog, final PRD/SDD, and implementation.

Scope limits:

- This section lists only categories of work for a later backlog process.
- This section does not define tasks, work items, tickets, implementation steps, sequencing, estimates, owners, acceptance tests, or deliverable artifacts.
- This section does not reopen CRIT-01..CRIT-07, TOM, V1 pilot scope, source policy minima, SDK/server exclusion, or any approved V1/post-V1 boundary.
- Any category touching conditional or post-V1-gated capability remains conditional and requires explicit future owner decision before it can be moved into V1 execution planning.

##### 4. Backlog Categories

The following categories are conceptual planning domains only. They are not a technical backlog and must not be read as implementation order.

| Category | Conceptual scope | Traceability / upstream source | Boundary preserved |
| --- | --- | --- | --- |
| Runtime / OpenCode coordination setup | Work domain for representing the CAFL V1 operating arrangement around OpenCode coordination, contract-driven progression, gate discipline, and non-authoritative runtime support. | S01 scope guardrails; S02 architecture principles; S04 runtime layout candidate; S05 source-vs-runtime structure; S07 OpenCode operating design; S17 traceability matrix. | OpenCode remains coordination/runtime support, not authoritative state, gate owner, or sufficient evidence by itself. No runtime is created by this category. |
| Mechanism implementation boundaries | Work domain for later elaboration of the conceptual split between agents, commands, scripts/CLI, validators, deterministic controls, and LLM reasoning boundaries. | S07 operating design; S08 agents / commands / scripts / validators split; S10 validator categories; S16 spike catalogue; S17 trace anchors. | Category remains conceptual; it does not define executable agents, real commands, scripts, validators, or final permissions. |
| Control and evidence infrastructure | Work domain for later planning around state, logs, evidence capture, evidence lifecycle, storage posture, gate evidence, and auditability. | S02 evidence/control principles; S09 schema categories; S10 validator categories; S11 state/logs/evidence storage; S17 SCH/VAL traceability. | No physical schemas, storage implementation, real validators, or evidence tooling are created here. |
| Source policy and Knowledge Governance | Work domain for preserving source policy minima, Knowledge Gap handling, Curation Request handling, routing of source evidence, and governance of accepted knowledge boundaries. | S01 source-of-truth guardrails; S02 context/source principles; S03 V1/post-V1 boundary; S12 Knowledge Base and Source Policy Implementation; S16 spike inputs; S17 traceability matrix. | Source policy is not expanded; RAG/vector base, broad ingestion, and advanced curation remain deferred unless explicitly approved later. |
| Odoo 18 pilot environment and module | Work domain for later planning around the Odoo-only, Odoo 18 pilot environment and internal requests / simple approvals pilot module boundary. | S03 V1 boundary; S13 Odoo 18 execution environment; S15 pilot module blueprint; S16 environment and pilot-module spike dependencies; S17 trace anchors. | Does not create final PRD, final SDD, functional backlog, implementation plan, or broadened pilot scope. |
| Security and secrets | Work domain for later planning around security posture, secrets handling, permissions boundaries, credential exposure risks, and security-related validation needs. | S02 security principles; S08 mechanism split constraints; S11 evidence/storage posture; S14 Security and Secrets; S16 SPK-S14 spike dependencies; S17 trace anchors. | Does not define executable secrets policy, real credentials handling, permissions implementation, or security tooling. |
| Spike execution and technical validations | Work domain for later planning around the ordered spike catalogue, open technical uncertainties, and validation dependency families. | S06 initial spike map; S13 environment spike dependencies; S14 security spikes; S15 pilot module spikes; S16 final ordered spike catalogue; S17 spike traceability. | No spike is executed here; SP-04/SP-05 remain open uncertainties, and Band D / post-V1-gated spikes remain separated unless owner-approved later. |
| Traceability and quality gates | Work domain for preserving bidirectional traceability, acceptance-gate evidence, non-self-closure, validation coverage, and quality-control boundaries. | S01 scope; S02 AP-01 and control principles; S09 SCH-02 trace fields; S10 validator categories; S11 evidence posture; S17 bidirectional traceability matrix. | Does not approve sections, close gates, replace owner approval, or create final validators or gate automation. |
| Owner / governance workflows | Work domain for later planning around owner approvals, blocker registration, conflict handling, deferred/post-V1 owner decisions, and governance handoffs. | S01 conflict and non-goal guardrails; S02 governance principles; S03 V1/post-V1 boundary; S12 Knowledge Governance; S16 conditional spike handling; S17 owner-approval trace notes. | Does not grant approval, close the iteration, resolve owner-decision blockers, or move post-V1 capabilities into V1 core. |

##### 5. Handoff to S19

S18 hands these category-level outputs to S19 as input for final Blueprint acceptance criteria. S19 may use the categories to confirm that:

- every post-Blueprint planning domain remains traceable to S01-S17 and S17 trace anchors;
- backlog-facing outputs preserve RULE-08 by staying at category level only;
- RULE-09 and global non-goals remain intact;
- conditional, open-uncertainty, and post-V1-gated areas remain visibly separated from approved V1 core scope;
- owner approval remains required for any future scope movement, implementation authorization, or final Blueprint approval.

This handoff does not authorize backlog creation or implementation.

##### 6. Open Questions / Owner Decisions

No new blocking owner decision is introduced by this section.

The following items remain governed by upstream decisions and must not be resolved inside S18:

- Conditional-open uncertainties from S16, especially SP-04 and SP-05, remain open until handled by the appropriate future validation and owner governance process.
- Band D and other post-V1-gated spike categories remain outside V1 core unless a future explicit owner decision changes their status.
- Any future attempt to expand source policy, pilot scope, SDK/server role, RAG/vector base, broad ingestion, advanced curation, or other post-V1 capability requires explicit owner decision before backlog elaboration can treat it as V1 work.

##### 7. Acceptance Criteria

S18 is acceptable when all of the following hold:

- The section lists only conceptual backlog categories and does not list detailed tasks, work items, tickets, implementation steps, sequencing, estimates, owners, or execution plans.
- Each category is traceable to S01-S17 outputs through context summaries, S16 spike catalogue handoffs, or S17 traceability anchors.
- RULE-08 and RULE-09 are preserved.
- Global non-goals remain preserved: no runtime, executable agents, real commands, physical schemas, real validators, scripts, RAG/vector base, detailed technical backlog, final PRD/SDD, or implementation is created.
- V1 core boundaries remain intact, including Odoo-only / Odoo 18, internal requests / simple approvals pilot scope, minimal source policy, SDK/server outside core V1, and post-V1 capabilities deferred unless explicitly owner-approved later.
- The section hands category-level outputs to S19 without declaring final acceptance, closing the iteration, or requesting owner approval.

##### 8. Section Output

S18 delivers a traceable, non-executable set of post-Blueprint backlog categories derived from S01-S17. These categories provide a controlled bridge into later backlog planning while preserving the Blueprint's non-goals, V1/post-V1 boundary, spike uncertainty handling, traceability requirements, and owner-governance constraints.

#### 19. Acceptance Criteria

Status: closed

Owner approval: approved

##### 1. Purpose

S19 defines the final acceptance criteria for owner review of the complete CAFL V1 Implementation Blueprint. These criteria verify that S01-S18 satisfy the global acceptance criteria (AC-G01..AC-G09), preserve RULE-04..RULE-09, and keep the Blueprint non-executable until explicit owner approval and later authorized planning.

This section does not approve the Blueprint, close Iteration 5, authorize implementation, create backlog, or convert any conceptual design into runtime artifacts.

##### 2. Inputs And Preconditions

S19 relies on the following approved upstream inputs:

- S01-S15: approved Blueprint sections covering scope/non-goals, architecture principles, V1/post-V1 boundary, runtime/source structure, initial spike map, OpenCode operating design, artifact split, schemas, validators, state/evidence, source policy, Odoo 18 execution environment, security/secrets, and pilot module blueprint.
- S16: approved consolidated spike catalogue and execution order, with explicit dependencies, SP-04/SP-05 as conditional-open uncertainties, Band D spikes (SP-11..SP-13) separated and post-V1-gated, and no spike executed or result closed.
- S17: approved bidirectional traceability matrix covering TOM-01..TOM-14 to Blueprint and Blueprint to authority, including schema/validator/spike traceability, with no approval or closure implied.
- S18: approved conceptual post-Blueprint backlog categories only: Runtime/OpenCode coordination setup, Mechanism implementation boundaries, Control and evidence infrastructure, Source policy and Knowledge Governance, Odoo 18 pilot environment and module, Security and secrets, Spike execution and technical validations, Traceability and quality gates, and Owner/governance workflows.
- Global acceptance criteria AC-G01..AC-G09 and rules RULE-04..RULE-09.

##### 3. Final Acceptance Criteria

The complete CAFL V1 Implementation Blueprint is ready to be presented for owner approval only when all criteria below hold.

| ID | Final criterion | Verifies | Evidence source |
| --- | --- | --- | --- |
| FAC-01 | All 19 Blueprint sections are authored, verified, and eligible for owner review; no section is treated as approved or closed by S19 itself. | AC-G01, AC-G09 | Blueprint state, status summary, S01-S18 approved summaries, S19 verification handoff |
| FAC-02 | Every Blueprint component has traceable support in TOM anchors, CRIT-approved content, or accepted decisions; no component relies on hidden or undocumented technical decisions. | AC-G02, AC-G04, RULE-04 | S17 traceability matrix, S01-S18 context summaries |
| FAC-03 | Bidirectional traceability from TOM-01..TOM-14 to Blueprint outputs and from Blueprint outputs back to authority is complete without known gaps. | AC-G03, RULE-05 | S17 TOM-to-Blueprint and Blueprint-to-authority matrices |
| FAC-04 | The consolidated spike order is explicit, dependency-aware, and preserves unresolved uncertainty boundaries, including SP-04/SP-05 and post-V1-gated Band D spikes. | AC-G05, RULE-06 | S16 spike catalogue and S17 spike traceability |
| FAC-05 | The Pilot Module Blueprint remains at component and boundary level only; it does not contain PRD, SDD, functional backlog, implementation plan, estimates, or executable instructions. | AC-G06, RULE-07 | S15 approved output and S17 traceability anchors |
| FAC-06 | Blueprint Outputs to Backlog remains limited to conceptual categories and does not create tasks, tickets, sequencing, owners, estimates, detailed backlog, or implementation authorization. | AC-G07, RULE-08 | S18 approved backlog categories and handoff |
| FAC-07 | The Blueprint has not created runtime, executable agents, real commands, physical schemas, real validators, scripts, RAG/vector base, technical backlog, PRD/SDD, source code, or implementation artifacts. | AC-G08, RULE-09 | S01-S18 approved non-goals, S18 non-goals preservation, repository change scope |
| FAC-08 | Owner approval remains explicit and external to S19; until owner approval is recorded by the authorized governance process, the Blueprint remains pending owner approval and Iteration 5 remains not closed by this section. | AC-G01, AC-G09 | Blueprint state and owner approval fields |

##### 4. Rule Coverage

| Rule | Final acceptance requirement |
| --- | --- |
| RULE-04 | S17 must show that every Blueprint component is backed by TOM, approved CRIT content, or accepted decisions; S19 adds no new component. |
| RULE-05 | S17 must remain the controlling bidirectional traceability matrix with no known gaps for S01-S16 and their authority anchors. |
| RULE-06 | S16 must remain the controlling spike execution order; S19 accepts only an ordered, dependency-justified spike catalogue, not a flat list. |
| RULE-07 | S15 must remain a pilot module blueprint only, with no PRD/SDD/backlog functional expansion. |
| RULE-08 | S18 must remain category-level only, with no detailed backlog items or execution plan. |
| RULE-09 | No forbidden executable, physical, backlog, RAG/vector, script, schema, validator, runtime, or implementation artifact may be created by the Blueprint process. |

##### 5. Non-Goals And Forbidden Outcomes

Final acceptance fails if any of the following is introduced or implied:

- Approval of the complete Blueprint without explicit owner approval.
- Closure of Iteration 5 or transition of S19 to approved/closed by this section.
- Authorization to implement, create runtime, configure executable agents, write commands, create scripts, generate schemas or validators, build RAG/vector infrastructure, or create source code.
- Creation of PRD, SDD, functional backlog, detailed technical backlog, task list, estimates, owners, or execution schedule.
- Reopening of CRIT-01..CRIT-07, TOM, or approved S01-S18 content.
- Merging of SP-04/SP-05 open uncertainties or Band D post-V1-gated spikes into core V1 without later owner-governed decision.

##### 6. Acceptance Review Checklist

Before owner approval can be requested through the authorized governance process, the verifier/owner review should confirm:

- [ ] S01-S18 are approved and have context summaries sufficient to support final review.
- [ ] S19 has been verified without open blocking issues.
- [ ] FAC-01..FAC-08 each have supporting evidence in S01-S18 and operational state.
- [ ] AC-G01..AC-G09 are each covered by at least one final criterion.
- [ ] RULE-04..RULE-09 are each preserved.
- [ ] S16 spike uncertainty handling remains open where required and not falsely resolved.
- [ ] S17 traceability remains the authority for bidirectional coverage and has no known gaps.
- [ ] S18 backlog outputs remain categories only and do not authorize backlog creation.
- [ ] No forbidden artifact or implementation output has been created.
- [ ] Owner approval is recorded only by the authorized process, not by this section.

##### 7. Section Output

S19 delivers the final acceptance criteria for reviewing the complete CAFL V1 Implementation Blueprint against AC-G01..AC-G09 and RULE-04..RULE-09. It prepares the Blueprint for verifier and owner review while preserving pending owner approval, keeping Iteration 5 open until authorized governance closure, and avoiding any implementation or backlog authorization.

## Blueprint Status Summary

| Iteracion | Numero de seccion | Nombre de seccion | Status | Owner approval | Blocker retroactivo detectado |
| --- | --- | --- | --- | --- | --- |
| Iteration 1 | 1 | Blueprint Scope and Non-Goals | closed | approved | none |
| Iteration 1 | 2 | Architecture Principles | closed | approved | none |
| Iteration 1 | 3 | V1 / Post-V1 Boundary | closed | approved | none |
| Iteration 1 | 4 | Runtime Layout Candidate | closed | approved | none |
| Iteration 1 | 5 | Source-vs-Runtime Structure | closed | approved | none |
| Iteration 1 | 6 | Initial Spike Map | closed | approved | none |
| Iteration 2 | 7 | OpenCode Operating Design | closed | approved | none |
| Iteration 2 | 8 | Agents / Commands / Scripts / Validators Split | closed | approved | none |
| Iteration 3 | 9 | Schemas V1 Minimum Set | closed | approved | none |
| Iteration 3 | 10 | Validators V1 Minimum Set | closed | approved | none |
| Iteration 3 | 11 | State / Logs / Evidence Storage | closed | approved | none |
| Iteration 3 | 12 | Knowledge Base and Source Policy Implementation | closed | approved | none |
| Iteration 4 | 13 | Odoo 18 Execution Environment | closed | approved | none |
| Iteration 4 | 14 | Security and Secrets | closed | approved | none |
| Iteration 4 | 15 | Pilot Module Blueprint | closed | approved | none |
| Iteration 5 | 16 | Spikes and Technical Validations final order | closed | approved | none |
| Iteration 5 | 17 | Bidirectional Traceability Matrix | closed | approved | none |
| Iteration 5 | 18 | Blueprint Outputs to Backlog | closed | approved | none |
| Iteration 5 | 19 | Acceptance Criteria | closed | approved | none |
