# CRIT-01: Intent And Scope

Status: approved

## Session Objective

- [accepted] Reconstruir la intencion real del owner y delimitar el alcance minimo antes de aceptar cualquier direccion del repo actual.
- [accepted] CRIT-01 define intencion y alcance; no define todavia flujo operativo, agentes, contratos, gates, trazabilidad tecnica ni plan de implementacion.

## Source And Authority

- [accepted] Fuente primaria: respuestas y aclaraciones del owner durante CRIT-01.
- [accepted] Si existe conflicto entre las respuestas del owner y documentos previos del repo, prevalece el owner.
- [accepted] `project-truth/` conserva autoridad bootstrap para registrar la verdad del proyecto.
- [accepted] El repo previo, `README.md`, `framework/` y documentos existentes son evidencia secundaria hasta validacion explicita.

## Intent Statement

- [accepted] CAFL Framework es un framework/plataforma operativo sobre OpenCode para desarrollar soluciones empresariales Odoo con asistencia de IA en todo el ciclo de vida.
- [accepted] CAFL debe permitir que un owner individual opere con capacidades equivalentes a un equipo de ingenieria especializado.
- [accepted] CAFL debe transformar ideas de negocio en modulos Odoo funcionales, testeados, documentados, auditables, seguros y tecnicamente listos para produccion.

## Problem To Solve

- [accepted] El problema principal es que el owner opera una empresa con una sola persona y no puede cubrir manualmente todas las fases del ciclo de vida de software requeridas para crear, mantener y mejorar soluciones empresariales Odoo.
- [accepted] CAFL debe reducir la dependencia de un equipo humano robusto, entregando capacidad operativa, tecnica y metodologica equivalente mediante asistencia de IA y flujo controlado.
- [accepted] CAFL debe cubrir el trabajo que normalmente requiere especialistas por fase: levantamiento, analisis, diseno, implementacion, testing, documentacion, seguridad, buenas practicas y validacion.

## Target User

- [accepted] El usuario inicial de CAFL es el owner.
- [accepted] CAFL no se define en CRIT-01 como producto para clientes, equipos externos o desarrolladores externos.

## Domain And Product Nature

- [accepted] CAFL nace especificamente para Odoo.
- [accepted] Odoo es el primer y unico dominio objetivo de este framework.
- [accepted] CAFL no es un framework generico multi-stack ni una plataforma general para desarrollar en cualquier tecnologia.
- [accepted] CAFL tiene enfasis en soluciones empresariales Odoo y en compliance legal/normativo cuando aplique.

## Expected Result

- [accepted] Cuando CAFL funcione correctamente debe producir soluciones empresariales basadas en el framework de Odoo.
- [accepted] Las soluciones producidas deben ser medibles, auditables, testeadas, documentadas, seguras y consistentes con buenas practicas Odoo.
- [accepted] CAFL debe producir los artefactos necesarios para controlar el ciclo de vida: definicion funcional, diseno tecnico, tareas, contratos internos, pruebas, validaciones, evidencia, documentacion y trazabilidad.
- [accepted] Estos artefactos no sustituyen el resultado final: el resultado final esperado es un modulo Odoo real listo para produccion tecnica.

## Autonomy And Human Control

- [accepted] CAFL debe aspirar a autonomia completa dentro del ciclo de desarrollo de soluciones Odoo.
- [accepted] Autonomia completa significa que CAFL puede tomar una idea del owner y avanzar por el flujo necesario hasta generar un modulo Odoo funcional, testeado, documentado y listo para produccion tecnica, sin intervencion operativa constante del owner.
- [accepted] Autonomia completa no significa ausencia total de control humano.
- [accepted] La aprobacion humana debe reservarse para decisiones criticas, no para microgestion operativa.
- [accepted] Decisiones criticas a nivel de intencion: falta de contexto suficiente, ambiguedad relevante sobre alcance funcional, impacto legal/normativo/compliance/seguridad, cambios importantes de arquitectura, ampliacion de alcance y aceptacion final de una solucion como lista para produccion tecnica.
- [accepted] El detalle operativo de deteccion, bloqueo, aprobacion y escalamiento corresponde a CRIT-02 y CRIT-05.

## Insufficient Context Rule

- [accepted] Si CAFL no tiene contexto suficiente, no debe inventar ni implementar por su cuenta.
- [accepted] Ante falta de contexto suficiente, CAFL debe detenerse, explicar que informacion falta, formular preguntas concretas y continuar solo despues de recibir informacion suficiente o una decision explicita del owner.
- [accepted] El diseno exacto de este flujo corresponde a CRIT-02.

## Initial Scope

- [accepted] La primera version util debe demostrar un flujo end-to-end desde idea del owner hasta modulo Odoo funcional.
- [accepted] La version util real debe incluir un modulo testeado en su totalidad segun el alcance definido y documentado.
- [accepted] El primer modulo debe ser un modulo Odoo completo pero acotado, elegido para validar el flujo end-to-end del framework.
- [accepted] El primer modulo no debe ser un modulo empresarial grande.
- [accepted] El primer modulo debe ser suficientemente pequeno para completarse dentro del marco de desarrollo inicial y suficientemente real para probar levantamiento de idea, definicion funcional, diseno tecnico, contratos/tareas, implementacion, testing, documentacion, validacion y evidencia.
- [open-question] El modulo exacto para validar el flujo end-to-end se definira despues.

## Out Of Scope Initial

- [accepted] El despliegue real en servidor productivo queda fuera del alcance inicial.
- [accepted] Generar un flujo de tareas tipo Scrum Master o PMBOK en una plataforma externa queda fuera del alcance inicial.
- [accepted] OpenSpec y OpenProject no son parte del producto CAFL Framework ni dependencias funcionales de su flujo de usuario final.
- [accepted] OpenSpec y OpenProject podrian considerarse herramientas auxiliares para desarrollar o coordinar el proyecto, pero esa evaluacion queda fuera del producto CAFL.

## Production Readiness

- [accepted] `Listo para produccion` en CRIT-01 significa listo desde el punto de vista tecnico y funcional, no desplegado en servidor productivo.
- [accepted] Un modulo listo para produccion tecnica debe ser funcional, instalable en Odoo, consistente con buenas practicas Odoo, testeado, documentado, seguro segun alcance, auditable, revisable y con evidencia suficiente para decidir si puede pasar a despliegue real.

## Definition Of Done Intent

- [accepted] CAFL no puede considerar una solucion terminada solo porque genero codigo.
- [accepted] Una solucion solo puede considerarse completa si cumple al menos: modulo funcional, instalacion o carga validada en Odoo, pruebas ejecutadas y aprobadas segun alcance, documentacion generada, evidencia de validacion, trazabilidad entre idea/alcance/tareas/implementacion/resultado, revision de seguridad y buenas practicas proporcional al alcance, y aceptacion final del owner o del gate definido.
- [accepted] El detalle verificable del DoD corresponde a CRIT-05 y CRIT-07.

## Testing And Documentation

- [accepted] Testing es obligatorio; CAFL no debe minimizar ni omitir pruebas.
- [accepted] Cada modulo generado debe tener pruebas suficientes para demostrar que funciona segun el alcance definido y no depende solo de revision manual superficial.
- [accepted] El nivel exacto de pruebas corresponde a CRIT-05 y CRIT-07.
- [accepted] Documentacion es obligatoria; CAFL no debe tratarla como accesorio opcional.
- [accepted] La documentacion debe permitir entender que se construyo, por que se construyo, como se usa, como se valida y que limites tiene.

## Internal Practices

- [accepted] PRD, SDD, CDD, TDD, tasks, contratos y gates se aceptan como capacidades internas deseadas del framework.
- [accepted] Estas practicas deben formar parte del flujo propio de CAFL y no depender de OpenSpec, OpenProject u otra plataforma externa como componente del producto.
- [accepted] El diseno exacto de estas practicas corresponde a CRIT-02, CRIT-04 y CRIT-05.

## Success And Failure Criteria

- [accepted] CAFL funciona si completa el ciclo completo desde la idea hasta generar un modulo Odoo listo para produccion tecnica.
- [accepted] CAFL falla si requiere intervencion humana operativa para completar tareas que deberian estar dentro de su flujo normal.
- [accepted] CAFL tambien falla si produce muchos documentos, agentes o artefactos pero no logra entregar un modulo Odoo funcional, testeado, documentado, auditable y validable.

## Scope Constraints And Risks

- [accepted] El plazo objetivo inicial es de 2 meses para construir una primera version util del framework con apoyo de IA.
- [accepted] El plazo de 2 meses debe actuar como restriccion de alcance: cualquier capacidad que no quepa razonablemente debe reducirse, diferirse o tratarse como futura.
- [accepted] Riesgos principales identificados por el owner: tiempo de implementacion, tareas interminables, DoD no claro, proceso manual para desarrollar el framework y tiempos iniciales no realistas.
- [accepted] CAFL debe evitar flujos infinitos o tareas interminables.
- [accepted] Cada tarea o fase debe tener objetivo claro, alcance limitado, salida esperada, criterio de aceptacion, condicion de bloqueo y condicion de cierre.
- [accepted] El diseno detallado para evitar tareas interminables corresponde a CRIT-02, CRIT-04, CRIT-05 y CRIT-07.

## Tooling Position

- [accepted] OpenCode es el runtime principal del framework.
- [accepted] OpenCode debe operar como entorno de ejecucion/interaccion para la asistencia de IA y coordinacion del desarrollo.
- [accepted] OpenSpec y OpenProject no son parte del producto CAFL Framework.
- [accepted] OpenSpec y OpenProject pueden considerarse ideas o herramientas auxiliares para organizar el desarrollo del framework, pero no dependencias funcionales de CAFL.

## Deferred Topics

- [open-question] CRIT-02 debe definir flujo operativo, fases, reglas de avance, bloqueo, retrabajo, cierre y escalamiento.
- [open-question] CRIT-03 debe definir responsabilidades, limites y autoridad de roles/agentes.
- [open-question] CRIT-04 debe definir contratos minimos, formato, campos y versionado.
- [open-question] CRIT-05 debe definir gates, severidades, evidencia, DoD verificable y criterios de testing.
- [open-question] CRIT-06 debe definir estado, evidencia, fuentes y trazabilidad.
- [open-question] CRIT-07 debe definir recursos, entorno Odoo, restricciones del runtime OpenCode, setup operativo, secuencia de implementacion y ajuste al plazo de 2 meses.

## Non-Goals For This Session

- [accepted] No definir arquitectura tecnica final.
- [accepted] No crear backlog de implementacion.
- [accepted] No aprobar agentes, contratos finales ni gates finales.
- [accepted] No configurar OpenSpec.
- [accepted] No modificar `framework/`.

## Acceptance Criteria Status

- [accepted] La intencion central, usuario inicial, dominio, resultado esperado, autonomia, no-alcance inicial, criterios de exito y riesgos principales quedaron respondidos por el owner.
- [accepted] Las decisiones operativas o tecnicas no resueltas quedaron derivadas a CRIT-02, CRIT-03, CRIT-04, CRIT-05, CRIT-06 o CRIT-07.
- [accepted] Ninguna hipotesis del repo actual queda elevada a verdad sin validacion del owner.
- [accepted] Verificacion independiente CRIT-01: APPROVED; CRIT-01 queda approved para intencion y alcance del producto.
