# Glossary

Status: CRIT-01 answered / pending verification

| Term | Definition | Status | Notes |
| --- | --- | --- | --- |
| CAFL | Framework/plataforma operativo sobre OpenCode para desarrollar soluciones empresariales Odoo con asistencia de IA en todo el ciclo de vida. | accepted | Especializado en Odoo; no es framework generico multi-stack. |
| project-truth | Directorio autoritativo inicial para decisiones, riesgos, preguntas y sesiones criticas del proyecto. | accepted | Autoridad inicial por instruccion explicita del owner. |
| source of truth | Fuente documental que tiene prioridad para decidir que esta aceptado, pendiente, rechazado o superado. | accepted | En este bootstrap corresponde a `project-truth/`. |
| owner | Persona con autoridad para aceptar, rechazar o cambiar la intencion y decisiones del proyecto; usuario inicial de CAFL. | accepted | CAFL debe permitir que el owner opere con capacidades equivalentes a un equipo de ingenieria especializado. |
| Odoo | Dominio unico objetivo de CAFL. | accepted | CAFL nace especificamente para soluciones empresariales Odoo. |
| modulo Odoo | Entregable tecnico funcional construido sobre el framework de Odoo. | accepted | V1 debe validar un modulo real, completo pero acotado. |
| OpenCode | Runtime principal de CAFL. | accepted | CRIT-07 definira restricciones de entorno y setup operativo, no si OpenCode es runtime. |
| OpenSpec | Herramienta externa que no forma parte del producto CAFL ni es dependencia funcional de su flujo. | accepted | Puede evaluarse como herramienta auxiliar para desarrollar o coordinar el proyecto fuera del producto. |
| OpenProject | Herramienta externa que no forma parte del producto CAFL ni es dependencia funcional de su flujo. | accepted | Puede evaluarse como herramienta auxiliar para desarrollar o coordinar el proyecto fuera del producto. |
| framework | Conjunto operativo de capacidades, artefactos, reglas y automatizacion para ejecutar el ciclo de desarrollo Odoo con IA. | accepted | `framework/` actual sigue siendo evidencia secundaria hasta validacion especifica. |
| autonomia completa | Capacidad esperada de CAFL para avanzar desde una idea hasta un modulo Odoo listo para produccion tecnica sin intervencion operativa constante del owner. | accepted | No elimina control humano en decisiones criticas. |
| decision critica | Decision que requiere aprobacion humana por falta de contexto, ambiguedad relevante, impacto legal/normativo/compliance/seguridad, cambio arquitectonico importante, ampliacion de alcance o aceptacion final. | accepted | El mecanismo operativo se define en CRIT-02 y CRIT-05. |
| falta de contexto suficiente | Situacion en que CAFL no tiene informacion suficiente para convertir una idea en solucion sin inventar. | accepted | Debe bloquear, explicar lo faltante, preguntar y continuar solo con informacion suficiente o decision explicita. |
| listo para produccion tecnica | Estado en que un modulo esta funcional, instalable en Odoo, testeado, documentado, seguro segun alcance, auditable, revisable y con evidencia suficiente para decidir despliegue real. | accepted | No significa desplegado en servidor productivo. |
| despliegue productivo | Instalacion o puesta en marcha real en un servidor productivo. | accepted | Fuera del alcance inicial de CAFL. |
| Definition of Done | Criterio minimo para considerar completa una solucion, incluyendo funcionalidad, validacion Odoo, pruebas, documentacion, evidencia, trazabilidad, revision proporcional y aceptacion. | accepted | DoD verificable se define en CRIT-05 y CRIT-07. |
| testing obligatorio | Principio de que CAFL no debe omitir ni minimizar pruebas para un modulo generado. | accepted | Nivel exacto de pruebas se define en CRIT-05 y CRIT-07. |
| documentacion obligatoria | Principio de que CAFL debe documentar que se construyo, por que, como se usa, como se valida y que limites tiene. | accepted | No es accesorio opcional. |
| agent | Rol automatizado o semi-automatizado con responsabilidades, entradas, salidas, limites y autoridad definidos. | draft | No implica agente ejecutable final; se define en CRIT-03. |
| contract | Acuerdo formal interno entre fases, roles o artefactos que define entradas, salidas y criterios de suficiencia. | draft | Los contratos finales no existen en este bootstrap; se definen en CRIT-04. |
| gate | Punto de decision interno que verifica criterios y evidencia para avanzar, bloquear, replanificar o escalar. | draft | Los gates finales no existen en este bootstrap; se definen en CRIT-05. |
| evidence | Prueba documental o tecnica que respalda una decision, resultado, verificacion o entrega. | draft | Su formato minimo se decide en CRIT-06 y CRIT-05. |
| traceability | Capacidad de rastrear relacion entre idea, alcance, decision, fuente, requisito, tarea, implementacion, prueba, evidencia y entrega. | draft | Su alcance final depende de CRIT-06. |
| implementation task | Trabajo concreto de construccion o configuracion posterior a decisiones criticas aceptadas. | draft | Debe tener objetivo, alcance, salida, aceptacion, bloqueo y cierre. |
| verification | Actividad que comprueba si un artefacto, decision o entrega cumple criterios definidos. | draft | Puede ser manual, automatizada o mixta segun decisiones futuras. |
| critical point | Area de decision que puede bloquear implementacion si queda sin resolver. | accepted | IDs iniciales: CRIT-01 a CRIT-07. |
| elicitation session | Sesion estructurada para obtener decisiones del owner sin asumir respuestas desde el repo actual. | accepted | Las plantillas iniciales estan en `project-truth/elicitation/`. |
