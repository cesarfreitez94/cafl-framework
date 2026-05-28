# CAFL V1 Implementation Blueprint Working Contract

Status: iteration-02-closed__iteration-03-ready

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
| Iteration 1 | 1 | Blueprint Scope and Non-Goals | closed | approved | none |
| Iteration 1 | 2 | Architecture Principles | closed | approved | none |
| Iteration 1 | 3 | V1 / Post-V1 Boundary | closed | approved | none |
| Iteration 1 | 4 | Runtime Layout Candidate | closed | approved | none |
| Iteration 1 | 5 | Source-vs-Runtime Structure | closed | approved | none |
| Iteration 1 | 6 | Initial Spike Map | closed | approved | none |
| Iteration 2 | 7 | OpenCode Operating Design | closed | approved | none |
| Iteration 2 | 8 | Agents / Commands / Scripts / Validators Split | closed | approved | none |
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
