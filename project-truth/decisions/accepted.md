# Accepted Decisions

Status: bootstrap + CRIT-01 approved

| ID | Decision | Source | Truth status | Notes |
| --- | --- | --- | --- | --- |
| DEC-ACCEPTED-001 | `project-truth/` sera la fuente de verdad inicial del proyecto. | Prompt del owner | accepted | Autoridad inicial para reconstruir intencion. |
| DEC-ACCEPTED-002 | El repo actual no debe tratarse como verdad oficial. | Prompt del owner | accepted | Incluye README, docs, agentes, contratos e ideas preliminares. |
| DEC-ACCEPTED-003 | `framework/` no es autoridad en esta etapa. | Prompt del owner | accepted | Solo puede usarse como evidencia secundaria. |
| DEC-ACCEPTED-004 | El contenido actual del repo es evidencia secundaria. | Prompt del owner | accepted | Puede informar preguntas, riesgos y alternativas. |
| DEC-ACCEPTED-005 | No se implementa en `framework/` hasta resolver puntos criticos minimos. | Prompt del owner | accepted | Bloquea desarrollo prematuro. |
| DEC-ACCEPTED-006 | Este bootstrap trabaja solo creando archivos bajo `project-truth/`. | Prompt del owner | accepted | No modifica codigo ni `framework/`. |
| DEC-ACCEPTED-007 | No se crean agentes ejecutables, comandos, contratos finales ni gates finales en este bootstrap. | Prompt del owner | accepted | La salida son plantillas y control de verdad. |
| DEC-ACCEPTED-008 | No se instala ni configura OpenSpec durante este bootstrap. | Prompt del owner | accepted | OpenSpec queda fuera del producto CAFL salvo posible uso auxiliar para desarrollar el framework. |
| DEC-ACCEPTED-009 | No se usara informacion de conversaciones externas. | Prompt del owner | accepted | Solo documentos disponibles y prompt actual. |
| DEC-ACCEPTED-010 | No se inventaran decisiones del owner ni se convertiran hipotesis en decisiones. | Prompt del owner | accepted | Las hipotesis quedan como `assumption` u `open-question`. |
| DEC-ACCEPTED-011 | Toda afirmacion relevante debe marcarse por estado. | Prompt del owner | accepted | Estados permitidos: `accepted`, `draft`, `assumption`, `open-question`, `rejected`, `superseded`. |
| DEC-ACCEPTED-012 | Estado inicial de `project-truth/`: bootstrap, no aprobado todavia. | Prompt del owner | accepted | CRIT-01 queda answered / pending verification, no approved. |
| DEC-ACCEPTED-013 | CAFL es un framework/plataforma operativo sobre OpenCode para desarrollar soluciones empresariales Odoo con asistencia de IA en todo el ciclo de vida. | CRIT-01 owner | accepted | Define naturaleza del producto a nivel de intencion. |
| DEC-ACCEPTED-014 | El problema principal es permitir que un owner individual opere con capacidades equivalentes a un equipo de ingenieria especializado. | CRIT-01 owner | accepted | Responde el dolor central de una empresa con un solo trabajador. |
| DEC-ACCEPTED-015 | El usuario inicial de CAFL es el owner. | CRIT-01 owner | accepted | No se define V1 para clientes, equipos externos o desarrolladores externos. |
| DEC-ACCEPTED-016 | Odoo es el primer y unico dominio objetivo de CAFL. | CRIT-01 owner | accepted | CAFL no nace como framework generico. |
| DEC-ACCEPTED-017 | CAFL debe producir soluciones empresariales Odoo medibles, auditables, testeadas, documentadas, seguras y consistentes con buenas practicas. | CRIT-01 owner | accepted | Los artefactos intermedios existen para soportar ese resultado. |
| DEC-ACCEPTED-018 | CAFL debe aspirar a autonomia completa dentro del ciclo de desarrollo de soluciones Odoo. | CRIT-01 owner | accepted | La autonomia no elimina control humano. |
| DEC-ACCEPTED-019 | La aprobacion humana debe reservarse para decisiones criticas, no para microgestion operativa. | CRIT-01 owner | accepted | El mecanismo detallado se define en CRIT-02 y CRIT-05. |
| DEC-ACCEPTED-020 | Ante falta de contexto suficiente, CAFL no debe inventar ni implementar; debe detenerse, explicar lo faltante, preguntar y continuar solo con informacion suficiente o decision explicita. | CRIT-01 owner | accepted | Condicion de bloqueo a nivel de intencion. |
| DEC-ACCEPTED-021 | La primera version util debe demostrar un flujo end-to-end desde idea del owner hasta modulo Odoo funcional. | CRIT-01 owner | accepted | El flujo detallado se define en CRIT-02. |
| DEC-ACCEPTED-022 | `Listo para produccion` significa listo tecnica y funcionalmente, no desplegado en servidor productivo. | CRIT-01 owner | accepted | Evita confundir readiness tecnica con deployment real. |
| DEC-ACCEPTED-023 | El despliegue real en servidor productivo queda fuera del alcance inicial. | CRIT-01 owner | accepted | El producto debe generar evidencia para decidir despliegue posterior. |
| DEC-ACCEPTED-024 | El primer modulo debe ser Odoo real, completo pero acotado, y orientado a validar el flujo end-to-end. | CRIT-01 owner | accepted | El modulo exacto se define despues. |
| DEC-ACCEPTED-025 | Una solucion no esta completa solo por generar codigo; requiere funcionalidad, validacion Odoo, pruebas, documentacion, evidencia, trazabilidad, revision proporcional y aceptacion final. | CRIT-01 owner | accepted | DoD verificable se define en CRIT-05 y CRIT-07. |
| DEC-ACCEPTED-026 | Testing es obligatorio y no debe omitirse ni minimizarse. | CRIT-01 owner | accepted | Alcance exacto de pruebas se define en CRIT-05 y CRIT-07. |
| DEC-ACCEPTED-027 | Documentacion es obligatoria y debe explicar que se construyo, por que, como se usa, como se valida y que limites tiene. | CRIT-01 owner | accepted | No es accesorio opcional. |
| DEC-ACCEPTED-028 | OpenCode es el runtime principal de CAFL. | CRIT-01 owner | accepted | CRIT-07 solo definira restricciones de entorno y setup operativo del runtime. |
| DEC-ACCEPTED-029 | OpenSpec y OpenProject no son parte del producto CAFL ni dependencias funcionales de su flujo de usuario final. | CRIT-01 owner | accepted | Pueden evaluarse como herramientas auxiliares fuera del producto. |
| DEC-ACCEPTED-030 | PRD, SDD, CDD, TDD, tasks, contratos y gates son capacidades internas deseadas del framework, no integraciones obligatorias con metodologias o plataformas externas. | CRIT-01 owner | accepted | El diseno exacto corresponde a CRIT-02, CRIT-04 y CRIT-05. |
| DEC-ACCEPTED-031 | CAFL no es un framework generico multi-stack ni una plataforma general de desarrollo para cualquier tecnologia. | CRIT-01 owner | accepted | Define limite de producto. |
| DEC-ACCEPTED-032 | El plazo objetivo inicial es de 2 meses para una primera version util del framework con apoyo de IA. | CRIT-01 owner | accepted | Debe actuar como restriccion de alcance. |
| DEC-ACCEPTED-033 | CAFL debe evitar flujos infinitos o tareas interminables; cada tarea o fase debe tener objetivo, alcance, salida, aceptacion, bloqueo y cierre. | CRIT-01 owner | accepted | El diseno detallado se resuelve en CRIT-02, CRIT-04, CRIT-05 y CRIT-07. |
| DEC-ACCEPTED-034 | CRIT-01 Intent and Scope approved. | independent CRIT-01 verification | accepted | Resultado: APPROVED. Alcance: intencion y alcance del producto. Limite: no aprueba todavia flujo operativo, agentes, contratos, gates, trazabilidad ni planificacion detallada. |
