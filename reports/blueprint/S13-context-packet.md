# S13 Context Packet — Odoo 18 Execution Environment

## Packet Header
- `section_id`: S13
- `iteration`: I4 (Ejecucion Odoo y piloto)
- `iteration_position`: 13
- `mode`: normal
- `dependency_context_summaries_complete`: yes
- `generated`: 2026-05-28

## Section Objective
Definir conceptualmente el entorno Odoo 18 para alimentar security (S14), pilot module (S15), y spikes finales (S16). No instalar Odoo, crear entorno real, ejecutar tests ni crear scripts.

## Selected Section Excerpt
```
Inputs: Iteration 3 aprobada. S09..S12 aprobadas. DEC-ACCEPTED-135, DEC-ACCEPTED-153.
Outputs: Definicion conceptual del entorno Odoo 18 para alimentar security, pilot y spikes finales.
Restricciones: No instalar Odoo, crear entorno real, ejecutar tests ni crear scripts.
Acceptance: La seccion identifica dependencias de validacion sin ejecutar entorno.
```

## Dependency Context Summaries
- **S09 Schemas V1 Minimum Set**: SCH-01..SCH-10 definidos (logicos). S13 debe usar SCH-10 (Odoo Pilot Artifact) junto con SCH-01 (Authority), SCH-05 (Evidence Record), SCH-06 (Deterministic Control) para evidencia conceptual del entorno Odoo 18 sin crear entorno ni implementacion.
- **S10 Validators V1 Minimum Set**: VAL-01..VAL-10. S13 debe consumir VAL-10 (Odoo Pilot Artifact Scope) y VAL-05 (Evidence Record) para controles conceptuales del entorno. S13 debe verificar que artefactos conceptuales respetan BR-01 y DEC-ACCEPTED-162/163.
- **S11 State/Logs/Evidence Storage**: Jerarquia L1-L4 (L1 project-truth/ autoritativo, L2 evidencia registrada gobernada, L3 evidencia candidata, L4 efimeros). Ciclo de vida 6-pasos. Git-compatible. S13 debe registrar evidencia conceptual del entorno bajo niveles L2/L3.
- **S12 Knowledge Base & Source Policy**: Source policy minima operacionalizada: docs.odoo.com + github.com/odoo/odoo. Knowledge Gap + Curation Request flow owner-gated. S13 solo puede usar fuentes autorizadas; gaps activan el flujo de Knowledge Gap definido en S12. No ampliar source policy.

## Hard Inherited Constraints
- **BR-01 (S03)**: V1 core solo Odoo-only, Odoo 18, piloto internal requests / simple approvals.
- **AP-08**: V1 minimo suficiente y anti-scope-creep. RAG, SDK/server, dashboard/UI, CI/CD, DB avanzada, multiusuario, plugins/MCP, curacion avanzada, integraciones reales fuera de core V1.
- **AP-09**: Storage/logs/evidence simples, auditables, Git-compatibles.
- **RULE-04**: Todo componente Blueprint debe tener respaldo en TOM, CRIT aprobado o decision aceptada.
- **RULE-09**: No crear runtime, agents ejecutables, commands reales, schemas fisicos, validators reales, scripts, RAG, backlog ni implementacion.
- **RULE-10**: No usar `framework/` como input ni referencia.
- **TOM**: Entorno Odoo 18 exacto queda para spike/blueprint; en implementacion bloquea produccion tecnica real. Odoo 18 target confirmado (DEC-ACCEPTED-135). V1 debe ejecutar y evidenciar ciclo minimo real en Odoo 18 (DEC-ACCEPTED-153).

## Required Traceability Anchors
- **DEC-ACCEPTED-135**: Odoo target V1 es Odoo 18. Forma exacta queda para spike/blueprint.
- **DEC-ACCEPTED-153**: V1 debe ejecutar y evidenciar un ciclo minimo real en Odoo 18. Incluye install/update/test execution y captura de evidencia; entorno exacto para spike/blueprint.
- **DEC-ACCEPTED-162**: Piloto V1 = internal requests / simple approvals.
- **DEC-ACCEPTED-163**: Source policy minima: docs.odoo.com + github.com/odoo/odoo.
- **SCH-10**: Odoo Pilot Artifact Schema (S09). Traza a CRIT-06/07, TOM, BR-01, AP-08, DEC-ACCEPTED-162/163.
- **VAL-05**: Evidence Record Validator (S10). Evidencia con trazabilidad, tipo, resumen verificable, estado.
- **VAL-10**: Odoo Pilot Artifact Scope Validator (S10). Dentro de internal requests / simple approvals; fuentes Odoo autorizadas; evidencia/control asociados.
- **TOM-S06 (entorno Odoo)**: Entorno Odoo 18 exacto no definido; spike requirement. (TOM linea 184, 362, 371, 379, 388)
- **TOM Pilot**: Piloto real, acotado, Odoo 18, modelos/vistas/ACL/record rules/workflow/reglas/tests/docs/evidencia, sin integracion externa compleja por defecto. (TOM lineas 248-255)
- **RISK-059**: Falta de entorno Odoo 18 — critical. Entorno exacto (Docker/venv/local) debe decidirse en spike. Sin entorno no hay ejecucion ni evidencia real.
- **RISK-010**: Verificacion no reproducible — high. Comands/logs/entorno Odoo por materializar en Blueprint/spikes.

## Forbidden Moves / Non-Goals
- No instalar Odoo, crear entorno real, ejecutar tests, ni crear scripts.
- No crear PRD final, SDD final ni backlog funcional del piloto.
- No reabrir seleccion del piloto (DEC-ACCEPTED-162 cerrado).
- No ampliar source policy (docs.odoo.com + github.com/odoo/odoo solamente).
- No crear schemas fisicos, validators reales, runtime, implementacion.
- No usar `framework/`.
- No decidir entorno exacto (Docker vs venv vs local); eso es spike.
- No autorizar RAG/vector base, SDK/server, dashboard/UI, CI/CD, DB avanzada, multiusuario, plugins/MCP.

## Acceptance Checklist
- [ ] Define conceptualmente el entorno Odoo 18 (sin crearlo).
- [ ] Identifica dependencias de validacion (SCH-10, VAL-05, VAL-10, S11 storage, S12 source policy).
- [ ] Registra evidencia conceptual bajo niveles L2/L3 de S11.
- [ ] Usa solo fuentes autorizadas (docs.odoo.com + github.com/odoo/odoo).
- [ ] Respeta BR-01 (Odoo-only, Odoo 18, internal requests / simple approvals).
- [ ] Trazable a DEC-ACCEPTED-135, 153, 162, 163 y TOM.
- [ ] Prepara handoff a S14 (security) y S15 (pilot module).
- [ ] No crea runtime, entorno real, scripts, schemas fisicos, validators reales.
- [ ] No reabre piloto, no amplia source policy, no introduce scope creep.

## Fallback-to-Strict Triggers
- Packet no puede probar trazabilidad requerida por RULE-04.
- Conflicto entre S09/S10/S11/S12 handoffs y contenido de S13.
- Se introduce referencia a `framework/`.
- Se propone entorno exacto (Docker/venv/local) como decision cerrada.
- Se amplia source policy sin Curation Request.
- Se crean artefactos ejecutables o implementacion.
- Se reabre seleccion del piloto.
- Blocker retroactivo detectado.
