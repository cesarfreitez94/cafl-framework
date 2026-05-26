# CRIT-07: Implementation Risks, Resources, Runtime And Feasibility

Status: approved

## Session Objective

- [accepted] CRIT-07 cierra la elicitacion critica CRIT-01..CRIT-07.
- [accepted] CRIT-07 define viabilidad, direccion candidata de runtime, recursos, riesgos, recortes V1 y criterios para implementacion posterior.
- [accepted] CRIT-07 no crea runtime, blueprint final, backlog tecnico, schemas fisicos finales, validators reales, commands, agents ejecutables, scripts, RAG, base vectorial ni configuracion OpenCode.
- [accepted] Despues de CRIT-07 no existe CRIT-08.
- [accepted] Los siguientes trabajos deben definirse formalmente por el proceso correspondiente: Consolidated Truth Review, Target Operating Model, Implementation Blueprint, technical validations/spikes, backlog tecnico e implementacion controlada.
- [accepted] CRIT-07 no impone una secuencia detallada post-CRIT-07 ni cierra esos trabajos posteriores.

## Context

- [accepted] CRIT-01 Intent and Scope esta approved.
- [accepted] CRIT-02 Operating Flow esta approved.
- [accepted] CRIT-03 Agent Responsibilities esta approved.
- [accepted] CRIT-04 Contracts esta approved como modelo contractual conceptual.
- [accepted] CRIT-05 Gates And Verification esta approved como modelo conceptual de gates y verificacion.
- [accepted] CRIT-06 State, Evidence, Traceability And Knowledge Governance esta approved como modelo logico/conceptual.
- [accepted] OpenCode sigue siendo runtime principal aprobado; CRIT-07 no reabre esa decision.
- [accepted] Odoo sigue siendo el unico dominio objetivo de CAFL.
- [accepted] CRIT-07 fue elicitado tecnicamente y aprobado por el owner con ajustes obligatorios.

## Owner Approval

- [accepted] El owner aprobo las recomendaciones de CRIT-07 Technical Elicitation con los ajustes obligatorios registrados en esta sesion.
- [accepted] CRIT-07 queda aprobado como cierre de la fase critica de elicitacion.
- [accepted] Las capacidades diferidas a V2/post-V1 no quedan rechazadas; quedan fuera de V1 por estrategia de alcance.

## Approved Decisions

### DEC-CRIT07-01: Cierre de elicitacion critica

- [accepted] CRIT-07 queda approved.
- [accepted] CRIT-01..CRIT-07 quedan completos como fase critica de elicitacion.
- [accepted] No existe CRIT-08.

### DEC-CRIT07-02: Estrategia sobre `framework/`

- [accepted] `framework/` queda eliminado como artefacto contaminado y descartado como input de diseno.
- [accepted] Nada de `framework/` debe usarse para layout, agents, commands, contracts, gates, schemas, validators, runtime ni knowledge base.
- [accepted] `framework/` no debe auditarse ni migrarse por defecto.
- [accepted] La eliminacion de `framework/` queda aprobada por el owner como accion separada de limpieza, no como fuente de diseno.

### DEC-CRIT07-03: Target Odoo V1

- [accepted] Odoo target V1 es Odoo 18.
- [accepted] V1 debe orientarse a Odoo 18.
- [accepted] La forma exacta de entorno Odoo 18, como Docker, venv/local u otra, no se decide en CRIT-07 y queda para spike/blueprint posterior.

### DEC-CRIT07-04: Operating model recomendado

- [accepted] CAFL V1 usara modelo hibrido progresivo sobre OpenCode.
- [accepted] El modelo combina agents para razonamiento, commands para entradas repetibles, scripts/CLI/validators para control deterministico, rules/config para invariantes minimos y skills/playbooks para conocimiento on-demand.
- [accepted] CAFL V1 no sera agents-only.

### DEC-CRIT07-05: V1 no es automatizacion debil

- [accepted] V1 debe automatizar validaciones, trazabilidad, evidencia y ejecucion Odoo minima.
- [accepted] No se acepta una V1 donde los agents solo recomienden y el owner deba verificar manualmente todo el ciclo.
- [accepted] V1 debe tener suficiente automatizacion deterministica para demostrar un ciclo end-to-end real de modulo Odoo 18.
- [accepted] La automatizacion minima suficiente debe cubrir o semi-cubrir validacion estructural de packets/contratos/gates/evidencia, DoR, trazabilidad minima, logs/estado/evidencia, install/update/test execution de Odoo 18, captura de evidencia y source policy / knowledge gap basico.

### DEC-CRIT07-06: No double work

- [accepted] CAFL V1 debe evitar trabajo doble documental.
- [accepted] Los artefactos, schemas, logs y evidencia deben existir para controlar ejecucion, validacion, trazabilidad y cierre, no para duplicar manualmente informacion sin valor operativo.
- [accepted] Si un dato debe aparecer en narrativa y registro estructurado, debe definirse una sola fuente autoritativa y una representacion secundaria derivada o referenciada.

### DEC-CRIT07-07: Runtime architecture candidate

- [accepted] Runtime candidate V1: OpenCode + commands + scripts/CLI/validators locales + storage fisico simple y auditable.
- [accepted] SDK/server queda fuera de core V1 por defecto.
- [accepted] SDK/server solo puede reactivarse si un spike demuestra necesidad y beneficio claro para control de sesion, estado, automatizacion o evidencia que no pueda resolverse razonablemente con commands/scripts/validators.

### DEC-CRIT07-08: Scripts/CLI language

- [accepted] No se asume Python, Node u otro lenguaje como decision tomada para scripts/CLI.
- [accepted] El lenguaje debe definirse mediante spike o validacion tecnica.
- [accepted] Criterios de decision: facilidad local, validacion de JSON/YAML/JSONL, integracion con comandos Odoo, velocidad de implementacion, mantenibilidad y menor friccion con OpenCode.

### DEC-CRIT07-09: Schemas V1 minimos versionados

- [accepted] Se aprueban schemas minimos versionados para registros criticos de V1.
- [accepted] Los schemas V1 minimos no son schemas definitivos permanentes del framework.
- [accepted] Su proposito V1 es validar estructura, referencias, estados, IDs y campos obligatorios.

### DEC-CRIT07-10: Validators V1

- [accepted] V1 debe incluir validators deterministicos minimos para evitar que CRIT-04, CRIT-05 y CRIT-06 queden solo como texto no validable.
- [accepted] Los validators V1 deben enfocarse en estructura, referencias, estados, IDs, campos obligatorios, trazabilidad minima, evidencia, source policy, knowledge gap basico, rework/debt/approval cuando aplique y ejecucion Odoo minima.
- [accepted] Los validators no sustituyen juicio tecnico, decision de gate ni aceptacion del owner.

### DEC-CRIT07-11: State/evidence physical storage candidate

- [accepted] V1 usara una estrategia candidata de storage fisico simple, auditable y compatible con Git.
- [accepted] La direccion candidata es hibrida: Markdown para narrativa controlada, JSON/YAML para registros estructurados, JSONL para logs append-only y artifacts para evidencia.
- [accepted] La decision fisica exacta de rutas, schemas y formatos queda para Implementation Blueprint; CRIT-07 no crea storage final.

### DEC-CRIT07-12: Knowledge base V1

- [accepted] V1 usara curated files + lightweight source registry + knowledge artifacts + skills/playbooks como direccion candidata de knowledge base.
- [accepted] RAG/base vectorial no se aprueba para V1.
- [accepted] RAG/base vectorial queda diferido a V2/post-V1 si el volumen, busqueda o automatizacion futura lo justifica.
- [accepted] Source policy, Knowledge Gap y Curation Request basicos deben existir como parte de la automatizacion minima suficiente.

### DEC-CRIT07-13: Ingesta, OpenAPI y PDF

- [accepted] V1 no automatizara de forma amplia la ingesta de documentacion, Swagger/OpenAPI o PDFs tecnicos.
- [accepted] OpenAPI/PDF processing queda como spike, validacion tecnica o capacidad post-V1, salvo que el piloto final lo requiera explicitamente.
- [accepted] La curacion manual controlada con source policy, snapshots y validators minimos es preferida para V1.

### DEC-CRIT07-14: Integration knowledge packs

- [accepted] Los integration knowledge packs se mantienen como mecanismo logico/estructural condicional.
- [accepted] V1 no incluye integraciones externas reales por defecto.
- [accepted] Una integracion externa real solo entra en V1 si el piloto final la requiere intencionalmente y el owner acepta el impacto de alcance.

### DEC-CRIT07-15: Odoo execution V1

- [accepted] V1 debe poder ejecutar y evidenciar un ciclo minimo real en Odoo 18.
- [accepted] La ejecucion minima debe cubrir install/update/test execution de modulo Odoo 18 y captura de evidencia.
- [accepted] El entorno exacto de ejecucion se decide por spike/blueprint posterior.

### DEC-CRIT07-16: Modulo piloto preferido

- [accepted] El candidato preferido de modulo piloto es solicitudes internas/aprobaciones simples.
- [accepted] La seleccion final del piloto queda para el blueprint posterior.
- [accepted] El piloto final debe ser real, acotado, Odoo 18, con modelos, vistas, ACL/record rules, workflow, reglas de negocio, datos minimos, tests backend, tests de acceso, documentacion, evidencia y sin integracion externa compleja por defecto.

### DEC-CRIT07-17: V1 scope direction

- [accepted] V1 debe demostrar un flujo end-to-end verificable de modulo Odoo 18.
- [accepted] V1 incluye direccion candidata para operating model, runtime candidate, automation minima, schemas minimos, validators minimos, state/evidence, knowledge governance basica, source policy/knowledge gap basico, Odoo 18 execution y piloto acotado.
- [accepted] V1 no debe ampliarse con capacidades diferidas si eso compromete el ciclo end-to-end verificable.

### DEC-CRIT07-18: Capacidades diferidas

- [accepted] Las capacidades no incluidas en V1 no quedan rechazadas.
- [accepted] Quedan diferidas a V2/post-V1 por estrategia de alcance: RAG/base vectorial, SDK/server runtime, dashboard/UI, CI/CD completo, integraciones externas reales, legal-compliance avanzado, knowledge base amplia, parsing automatico OpenAPI/PDF, PostgreSQL/pgvector/DB avanzada, multiusuario/equipo, plugins/MCP/custom tools, automatizacion avanzada de Curation Mode, frontend/OWL avanzado si no aplica al piloto y Playwright si no hay frontend custom en piloto.

## V1 Minimum Sufficient Automation

| Area | Approved V1 requirement | Boundary |
| --- | --- | --- |
| Packets/contracts/gates/evidence | Validacion estructural automatizada o semi-automatizada | No equivale a aprobacion semantica total |
| DoR | Check minimo de campos, fuentes, blockers/`none`, alcance, outputs y evidencia esperada | El receptor/validator conserva criterio de suficiencia |
| Trazabilidad | Links minimos entre modulo, capability/feature, tarea, contract, gate, evidence, decision y source cuando aplique | No crea dashboard ni DB avanzada |
| Logs/estado/evidencia | Registros persistentes y auditables | No cierra storage fisico final permanente |
| Odoo 18 execution | Install/update/test execution minimo con evidencia | Entorno exacto queda para spike/blueprint |
| Source policy / Knowledge Gap | Bloqueo basico por fuente insuficiente y Curation Request | No crea automatizacion avanzada de curacion |

## Deferred / Post-V1 Capabilities

| Capability | V1 status | Notes |
| --- | --- | --- |
| RAG/base vectorial | deferred | No rechazado; no aprobado para V1 |
| SDK/server runtime | deferred/conditional | Solo vuelve con spike favorable |
| dashboard/UI | deferred | No necesario para validar V1 |
| CI/CD completo | deferred | V1 prioriza ejecucion local reproducible |
| integraciones externas reales | deferred/conditional | Solo si piloto final lo exige |
| legal-compliance avanzado | deferred | V1 no es motor legal |
| knowledge base amplia | deferred | V1 usa bootstrap incremental |
| parsing automatico OpenAPI/PDF | deferred/conditional | Requiere spike y revision |
| PostgreSQL/pgvector/DB avanzada | deferred | No necesario para V1 |
| multiusuario/equipo | deferred | Usuario inicial es owner |
| plugins/MCP/custom tools | deferred | Evita superficie temprana |
| automatizacion avanzada de Curation Mode | deferred | V1 requiere basico enforceable |
| frontend/OWL avanzado | conditional/deferred | Solo si aplica al piloto |
| Playwright | conditional/deferred | Solo si hay frontend custom en piloto |

## Technical Validations / Spikes To Define Later

- [accepted] Technical validations/spikes son trabajo posterior a CRIT-07 y deben definirse formalmente en el proceso correspondiente.
- [accepted] Spikes necesarios incluyen al menos OpenCode permissions, OpenCode commands/skills, SDK/server go/no-go, lenguaje scripts/CLI, schema/validator toolchain, storage/log convention, source policy enforcement, knowledge without RAG, Odoo 18 local environment, Odoo 18 install/update/test execution, evidence capture y secrets handling.
- [accepted] CRIT-07 registra la necesidad de estos spikes; no los ejecuta ni cierra sus resultados.

## Non-Goals Confirmed

- [accepted] No se implementa runtime.
- [accepted] No se crean agents ejecutables.
- [accepted] No se crean commands reales.
- [accepted] No se crean schemas fisicos finales.
- [accepted] No se crean validators reales.
- [accepted] No se crean scripts.
- [accepted] No se crea RAG.
- [accepted] No se crea base vectorial.
- [accepted] No se configura OpenCode.
- [accepted] No se configura OpenSpec.
- [accepted] No se crea CRIT-08.
- [accepted] No se cierra Implementation Blueprint.
- [accepted] No se cierra backlog tecnico.
- [accepted] No se impone planificacion detallada post-CRIT-07.
- [accepted] No se usa `framework/` como fuente de diseno.

## Handoff

- [accepted] CRIT-07 entrega decisiones aprobadas, direccion candidata de runtime, restricciones V1, riesgos y criterios para trabajo posterior.
- [accepted] Los trabajos posteriores deben partir desde las decisiones CRIT-01..CRIT-07 aprobadas.
- [accepted] Los trabajos posteriores no deben reabrir `framework/` como fuente de diseno ni convertir capacidades diferidas en requisitos V1 sin decision explicita del owner.
- [accepted] No existe CRIT-08.

## Acceptance Criteria Result

- [accepted] CRIT-07 queda aprobado documentalmente.
- [accepted] CRIT-01..CRIT-07 quedan completos.
- [accepted] `framework/` queda descartado como input y aprobado para eliminacion.
- [accepted] Odoo 18 queda como target V1.
- [accepted] Automatizacion minima suficiente queda definida como automatizacion real de validacion, trazabilidad, evidencia y ejecucion Odoo 18 minima.
- [accepted] No double work queda registrado.
- [accepted] Lo diferido a V2/post-V1 queda como diferido, no rechazado.
- [accepted] RAG/base vectorial no queda aprobado para V1.
- [accepted] SDK/server no queda aprobado como core V1.
- [accepted] V1 queda como flujo end-to-end verificable y no puramente narrativo.
- [accepted] No se impone planificacion detallada posterior.
- [accepted] No se implementa runtime ni se crean artefactos ejecutables.
- [accepted] CRIT-08 no existe.
