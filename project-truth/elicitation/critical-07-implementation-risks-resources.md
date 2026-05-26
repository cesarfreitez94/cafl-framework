# CRIT-07: Implementation Risks And Resources

Status: not-started

## Session Objective

- [draft] Definir setup operativo candidato, schemas finales, validators, commands, SDK/server/scripts, permissions, runtime, rutas, viabilidad, recursos, riesgos, secuencia y recortes para implementar el modelo mixto aprobado, sin reabrir OpenCode como runtime principal ni adelantar implementacion.
- [draft] Definir tambien la implementacion fisica/runtime candidata de la base de conocimiento curada derivada de CRIT-06: RAG o no RAG, base vectorial o no, archivos curados, schemas finales, validators, commands, scripts de ingesta/actualizacion, source-vs-runtime layout y consulta desde agents/commands/skills/scripts.

## Context

- [accepted] Este bootstrap no instala ni configura herramientas.
- [accepted] OpenCode ya es runtime principal aprobado; CRIT-07 no reabre esa decision.
- [accepted] OpenSpec y OpenProject no son producto CAFL ni dependencias funcionales obligatorias.
- [accepted] CAFL es Odoo-only y requiere validacion contra un entorno Odoo real.
- [draft] La separacion source-vs-runtime debe respetar que `framework/` es fuente y no runtime activo.
- [draft] El setup operativo debe cubrir OpenCode agents, commands, SDK/server/scripts, permissions, config, skills, rules/AGENTS.md, operacion local/global y evidencia ejecutable.
- [draft] CRIT-07 no adelanta implementacion antes de que CRIT-04, CRIT-05 y CRIT-06 definan contratos, gates y estado/evidencia/trazabilidad.
- [draft] CRIT-07 debe definir la materializacion tecnica de CRIT-04 contracts, CRIT-05 gates y CRIT-06 state/evidence/traceability en schemas finales, validators, commands, SDK/server/scripts, permissions, rutas/ubicaciones runtime y ejecucion reproducible.
- [draft] CRIT-07 define el cierre de elicitacion critica antes del Consolidated Truth Review y no propone CRIT-08.
- [draft] RAG, pgvector, CI/CD, Playwright y herramientas auxiliares deben validarse contra valor, recursos, secuencia y plazo de 2 meses.
- [draft] El plazo de 2 meses es restriccion de alcance para recursos, tooling operativo, recortes y secuencia.
- [draft] OpenCode ya es runtime principal aprobado; CRIT-07 decide como operar fisicamente el modelo, no si OpenCode sera reemplazado.
- [draft] CRIT-07 debe decidir si la knowledge base se materializa con RAG, base vectorial, archivos curados, JSON/YAML/JSONL/Markdown, SQLite, PostgreSQL, pgvector u otro mecanismo.
- [draft] CRIT-07 debe definir como implementar knowledge domains extensibles para Odoo, OWL, Playwright/testing, Python aplicado a Odoo, integraciones externas, APIs oficiales/de terceros, Swagger/OpenAPI, PDFs tecnicos y dominios futuros como legal-compliance.
- [draft] CRIT-07 debe definir como bloquear ejecucion si falta conocimiento autorizado suficiente, sin implementar todavia ese bloqueo en esta sesion.
- [draft] Despues de CRIT-07 corresponde Consolidated Truth Review y diseno implementable; no corresponde crear CRIT-08.

## Questions For The Owner

- [open-question] Que entorno Odoo existe hoy y que permisos hay sobre el?
- [open-question] Que version, datos, permisos y restricciones tiene el entorno Odoo real para instalar, cargar, actualizar y probar un modulo piloto?
- [open-question] Que setup operativo de OpenCode se requiere para agents, commands, SDK/server/scripts, permissions, config, skills y rules/AGENTS.md?
- [open-question] Que debe operar local, global o por repo, y como se mantiene la separacion source-vs-runtime?
- [open-question] Que rutas/ubicaciones runtime deben existir para agents, skills, commands, SDK/server/scripts, config, rules y artefactos de evidencia?
- [open-question] Que permissions y restricciones de seguridad son necesarias para evitar ejecucion no autorizada o lectura de contexto prohibido?
- [open-question] Que schemas finales, validators y commands deben materializar CRIT-04, CRIT-05 y CRIT-06?
- [open-question] Que SDK/server/scripts y tooling operativo se necesitan para ejecucion reproducible sin implementarlos en esta sesion?
- [open-question] Que evidencia ejecutable debe poder producirse mediante comandos, scripts, tests, capturas o reportes, sin crearla en esta sesion?
- [open-question] RAG es esencial para V1, debe limitarse a alcance minimo o puede diferirse?
- [open-question] La base de conocimiento curada se implementara con RAG o sin RAG?
- [open-question] Se usara base vectorial, pgvector, PostgreSQL, SQLite, archivos curados, JSON, YAML, JSONL, Markdown u otro mecanismo?
- [open-question] Que schemas finales de knowledge artifacts, source registry, source snapshots, source usage y knowledge domains se necesitan?
- [open-question] Que validators finales deben validar fuentes, snapshots, freshness/vigencia, applicability, knowledge artifacts y knowledge packs?
- [open-question] Que commands de ingesta, actualizacion, validacion, consulta y reporte de knowledge base se requieren?
- [open-question] Que scripts o tooling se requieren para procesar Swagger/OpenAPI, PDFs tecnicos, documentacion de autenticacion, endpoints, payloads, errores, seguridad, datos sensibles, compliance, ejemplos oficiales y pruebas recomendadas?
- [open-question] Que scripts o tooling se requieren para snapshots/versiones, hashes, vigencia y deprecacion de fuentes?
- [open-question] Como se integra la knowledge base con OpenCode agents, commands, skills/playbooks, SDK/server/scripts, permissions y context routing?
- [open-question] Que source-vs-runtime layout y rutas/ubicaciones runtime deben existir para knowledge packs, indices, caches, snapshots, artifacts, logs y evidencia?
- [open-question] Como consultaran agents/commands/scripts la base de conocimiento y como se registrara source usage?
- [open-question] Como se bloqueara ejecucion o decision cuando falte conocimiento autorizado suficiente?
- [open-question] Como se materializan dominios extensibles y como se agregan dominios futuros como legal-compliance, tax-regulation, public-sector-processes, accounting, industry-specific-rules y regulatory-reporting sin redisenar el framework?
- [open-question] Que OpenSpec/OpenProject u otras herramientas auxiliares aportan valor sin convertirse en producto CAFL ni dependencia funcional?
- [open-question] Que recursos existen para CI/CD y pruebas end-to-end?
- [open-question] Que nivel de esfuerzo cabe en el plazo de 2 meses y que recortes son aceptables?
- [open-question] Cual es el modulo piloto exacto para validar el flujo end-to-end?
- [open-question] Cual es la secuencia de implementacion despues de CRIT-04, CRIT-05 y CRIT-06?
- [open-question] Que riesgos tecnicos bloquearian implementacion?

## Decisions To Make

- [open-question] Recursos disponibles.
- [open-question] Setup operativo OpenCode sin reabrir OpenCode como runtime principal.
- [open-question] Schemas finales, validators, commands y materializacion tecnica de CRIT-04 contracts, CRIT-05 gates y CRIT-06 state/evidence/traceability.
- [open-question] Uso candidato de agents, commands, SDK/server/scripts, permissions, config, skills y rules/AGENTS.md.
- [open-question] Operacion local/global, rutas/ubicaciones runtime y separacion source-vs-runtime.
- [open-question] Entorno Odoo real, instalacion/carga/actualizacion de modulo y ejecucion de tests aplicables.
- [open-question] Evidencia ejecutable minima esperada.
- [open-question] Herramientas auxiliares incluidas, excluidas o postergadas.
- [open-question] Alcance RAG V1 o diferimiento.
- [open-question] Implementacion fisica/runtime de la curated knowledge base derivada de CRIT-06.
- [open-question] Mecanismo de almacenamiento/contenido para knowledge artifacts: archivos curados, JSON/YAML/JSONL/Markdown, SQLite, PostgreSQL, pgvector, base vectorial u otro.
- [open-question] Schemas finales de knowledge artifacts, source registry, snapshots/versiones, source usage, prohibited sources y knowledge domains.
- [open-question] Validators de fuentes, knowledge packs, freshness/vigencia, trust level, applicability y consistencia de artifacts.
- [open-question] Commands y scripts de ingesta, actualizacion, validacion, consulta, snapshots/versiones, Swagger/OpenAPI, PDFs tecnicos y reportes.
- [open-question] Integracion con OpenCode agents, commands, skills/playbooks, SDK/server/scripts, permissions, context routing y bloqueo por falta de conocimiento autorizado.
- [open-question] Politica fisica de actualizacion, vigencia, deprecacion, rutas runtime y source-vs-runtime layout.
- [open-question] Materializacion de knowledge domains extensibles para integraciones externas y dominios futuros legales/regulatorios.
- [open-question] Secuencia de implementacion candidata.
- [open-question] Modulo piloto exacto y recortes compatibles con 2 meses.
- [open-question] Recursos, riesgos, recortes y plan de implementacion compatibles con el plazo de 2 meses.
- [open-question] Restricciones de permisos y seguridad.
- [open-question] Riesgos bloqueantes antes de desarrollo.

## Non-Goals For This Session

- [accepted] No instalar OpenSpec.
- [accepted] No configurar OpenCode runtime.
- [accepted] No reabrir la decision de OpenCode como runtime principal.
- [accepted] No crear archivos ni implementacion de schemas finales, validators finales, agentes ejecutables, commands, scripts, permisos ni config runtime.
- [accepted] No adelantar implementacion antes de CRIT-04, CRIT-05 y CRIT-06.
- [accepted] No proponer CRIT-08.
- [accepted] No crear CI/CD real.
- [accepted] No implementar RAG.
- [accepted] No modificar `framework/`.
- [accepted] No crear base vectorial real ni base de datos real de conocimiento.
- [accepted] No crear knowledge packs, ingesta, snapshots fisicos ni indices reales en esta sesion.
- [accepted] No implementar schemas, validators, commands o scripts de knowledge base en esta sesion; solo definir decisiones pendientes de implementacion.
- [accepted] No crear CRIT-08 ni nuevas sesiones criticas para knowledge governance.

## Risks If Unresolved

- [draft] Reabrir decisiones aprobadas sobre runtime o producto en vez de decidir setup operativo.
- [draft] Integracion prematura con herramientas sin contratos, gates y estado definidos.
- [draft] Planificacion basada en recursos inexistentes.
- [draft] Falta de entorno Odoo real para instalar, actualizar o testear modulo.
- [draft] Confusion source-vs-runtime que lleve a crear archivos ejecutables en ubicaciones incorrectas.
- [draft] Permissions demasiado amplios, contexto prohibido no protegido o ejecucion no reproducible.
- [draft] V1 bloqueada por dependencias tecnicas no priorizadas.
- [draft] RAG completo, CI/CD o E2E exceden el plazo de 2 meses sin recortes.
- [draft] Sobrecosto por automatizacion antes de validar valor.
- [draft] RAG/base de conocimiento se convierte en scope creep y consume V1 antes de validar flujo Odoo end-to-end.
- [draft] Implementacion fisica demasiado rigida impide agregar dominios futuros como legal-compliance sin redisenar el framework.
- [draft] Knowledge base fisica sin validators permite usar fuentes desactualizadas, no oficiales o no aplicables.
- [draft] Scripts para Swagger/OpenAPI, PDFs o API docs mal definidos producen conocimiento incorrecto pero aparentemente autorizado.
- [draft] Bloqueo por falta de conocimiento autorizado no se implementa o queda solo en prompts.

## Output Format

- [draft] Tabla de mecanismo/herramienta candidata, decision pendiente, razon, prerequisito, riesgo, costo, recurso requerido, evidencia esperada y estado.
- [draft] Mapa de recursos disponibles y brechas.
- [draft] Setup operativo candidato para OpenCode agents, schemas finales, validators, commands, SDK/server/scripts, permissions, config, skills, rules/AGENTS.md, rutas/ubicaciones runtime y operacion local/global.
- [draft] Materializacion tecnica candidata de CRIT-04 contracts, CRIT-05 gates y CRIT-06 state/evidence/traceability.
- [draft] Implementacion fisica/runtime candidata de curated knowledge base: RAG o no RAG, base vectorial o no, archivos curados, JSON/YAML/JSONL/Markdown, SQLite, PostgreSQL, pgvector u otro mecanismo.
- [draft] Schemas finales candidatos, validators, commands y scripts para knowledge artifacts, source registry, source snapshots, knowledge packs, ingesta, actualizacion, validacion, consulta, Swagger/OpenAPI, PDFs tecnicos y source usage.
- [draft] Layout source-vs-runtime y rutas/ubicaciones runtime candidatas para knowledge domains, snapshots, artifacts, indices/caches, logs, permissions y evidencia.
- [draft] Politica candidata de actualizacion, vigencia, deprecacion, consulta desde agents/commands/scripts y bloqueo por falta de conocimiento autorizado.
- [draft] Plan candidato de entorno Odoo real, instalacion/carga/actualizacion, tests aplicables y evidencia ejecutable.
- [draft] Lista de recursos, riesgos, recortes, alcance RAG V1 o diferimiento, modulo piloto exacto, plan de implementacion y secuencia candidata compatible con 2 meses.
- [draft] Lista de bloqueadores tecnicos antes de implementar.

## Acceptance Criteria

- [draft] Ninguna pregunta reabre OpenCode como runtime principal aprobado.
- [draft] CRIT-07 cierra la elicitacion critica antes del Consolidated Truth Review y no propone CRIT-08.
- [draft] Cada mecanismo/herramienta candidata queda aceptada, rechazada, postergada o pendiente para la futura implementacion.
- [draft] Setup operativo cubre agents, schemas finales, validators, commands, SDK/server/scripts, permissions, config, skills, rules/AGENTS.md, rutas/ubicaciones runtime, operacion local/global y source-vs-runtime.
- [draft] La materializacion tecnica de CRIT-04, CRIT-05 y CRIT-06 queda definida sin crear implementacion.
- [draft] Viabilidad Odoo cubre instalacion/carga/actualizacion de modulo, tests aplicables y evidencia ejecutable.
- [draft] RAG, CI/CD, Playwright y automatizacion quedan dimensionados o diferidos segun plazo de 2 meses.
- [draft] La implementacion fisica de knowledge base queda decidida como mecanismo candidato sin crear runtime en esta sesion.
- [draft] RAG/base vectorial/archivos curados quedan incluidos, excluidos, postergados o pendientes con razon, costo, riesgo y dependencia.
- [draft] Schemas, validators, commands y scripts de ingesta/actualizacion/validacion de knowledge base quedan definidos como decisiones de implementacion futura, sin crearlos todavia.
- [draft] La integracion con OpenCode agents/commands/skills/scripts y el bloqueo por falta de conocimiento autorizado quedan definidos operacionalmente, sin reabrir OpenCode como runtime principal.
- [draft] La extensibilidad de knowledge domains futuros queda resuelta a nivel de plan implementable sin proponer CRIT-08.
- [draft] No queda dependencia tecnica critica sin dueno ni mitigacion.
- [draft] La secuencia de implementacion no requiere asumir recursos no confirmados.
