# CRIT-07: Implementation Risks And Resources

Status: not-started

## Session Objective

- [draft] Definir setup operativo candidato, schemas finales, validators, commands, SDK/server/scripts, permissions, runtime, rutas, viabilidad, recursos, riesgos, secuencia y recortes para implementar el modelo mixto aprobado, sin reabrir OpenCode como runtime principal ni adelantar implementacion.

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

## Output Format

- [draft] Tabla de mecanismo/herramienta candidata, decision pendiente, razon, prerequisito, riesgo, costo, recurso requerido, evidencia esperada y estado.
- [draft] Mapa de recursos disponibles y brechas.
- [draft] Setup operativo candidato para OpenCode agents, schemas finales, validators, commands, SDK/server/scripts, permissions, config, skills, rules/AGENTS.md, rutas/ubicaciones runtime y operacion local/global.
- [draft] Materializacion tecnica candidata de CRIT-04 contracts, CRIT-05 gates y CRIT-06 state/evidence/traceability.
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
- [draft] No queda dependencia tecnica critica sin dueno ni mitigacion.
- [draft] La secuencia de implementacion no requiere asumir recursos no confirmados.
