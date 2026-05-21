# Elicitation Record

## Sesion Inicial

Objetivo: definir direccion general del framework.

## Respuestas Capturadas

- Tipo de solucion: Framework OpenCode.
- Objetivo V1: crear fabrica Odoo.
- Modulos objetivo: simples, procesos de negocio, integraciones, frontend OWL y cumplimiento normativo chileno futuro.
- Control humano: bajo.
- Entorno Odoo: instancia existente.
- Conocimiento: base curada de repo oficial y pagina oficial indexadas.
- Testing: cobertura completa.
- Control de alcance: roadmap, backlog y documento maestro.
- Roles V1: PM, analista funcional, arquitecto Odoo, dev backend, dev frontend OWL, QA/testing, legal/normativo Chile y curador de conocimiento.
- Flujo: modo mixto.
- Entradas: entrevista, documentos, normativa, proceso actual e idea breve.
- Artefactos antes de codigo: PRD, SDD, contratos, matriz de trazabilidad, plan de testing, estimacion y fases.
- Falla de gate: segun severidad.
- Unidad de control: por modulo.
- Arquitectura OpenCode: agentes, skills, comandos, permisos, MCP y plantillas versionadas.
- Base de conocimiento: mixta con snapshots e indice/RAG.
- Odoo: Community.
- Addons: framework separado.
- Estandares: ORM, seguridad, vistas, UX, datos, fixtures, i18n, performance y mantenibilidad.
- Fuentes extra: solo oficiales.
- Normativa chilena: BCN/Ley Chile, Direccion del Trabajo, SUSESO, ministerios y documentos cliente/legal externo.
- Responsabilidad legal: motor normativo como objetivo, pero V1 sin motor avanzado.
- Migraciones: formal.
- Despliegue: CI/CD.
- Pruebas obligatorias: Python/Odoo, HttpCase/Tours, OWL/QUnit, Playwright E2E, migracion/update, seguridad y performance basica.
- Criterio QA: todos pasan.
- Evidencias: Markdown, JUnit/CI, screenshots/videos, matriz de trazabilidad y bitacora de decisiones.
- Severidades: combinada con categoria de riesgo.
- CI/CD: agnostico.
- Conexion Odoo: configurable.
- Datos de prueba: normativos, escenarios de negocio y fixtures minimos.
- Deuda tecnica: segun severidad.
- Entregables comerciales: propuesta, SOW, estimacion, plan de implementacion y acta de aceptacion.
- Idioma: espanol tecnico.
- Actores humanos: aprobador interno, sponsor cliente, usuario experto, experto legal y TI cliente.
- Funcionalidades legales futuras: obligaciones, evidencias, matrices de riesgo, workflows, reportes e integraciones.
- Confidencialidad: no datos reales, anonimizacion, perfiles de seguridad y auditoria.
- Elicitacion: adaptativa.
- Scope creep: exclusiones, control de cambios, backlog futuro y presupuesto por fase.
- Definition of Done: funcional probado, trazable, desplegable, documentado y aceptable comercialmente.
- Instalacion: mixta.
- MVP V1: fabrica completa, luego acotada a framework completo sin legal avanzado.
- Piloto: modulo simple.
- RAG tecnico: pgvector.
- Actualizacion KB: mixta auditada.
- Modelos IA: agnostico.
- Aprobaciones humanas obligatorias: ninguna.
- Comercial/IP: uso interno.
- Corte V1 final: framework completo sin legal avanzado.
- Riesgo legal: bloqueo solo critico.
- Ingesta RAG: mixta controlada.
- Generacion de codigo: configurable.
- Permisos: por perfil.
- Runtime esperado: Python/Odoo CLI, PostgreSQL/pgvector, Node/Playwright, Docker y Git.
- CI/CD V1: comandos estandar, plantillas y contrato pipeline.
- Estado: Markdown versionado.
- Correccion estructural: fuente del framework en `framework/`, no en `.opencode`.
- Nueva necesidad: fase previa de meta-elicitacion y revalidacion antes de planificar.

## Decisiones Pendientes Para Proximas Sesiones

- Si habra una, dos o tres fases previas de meta-elicitacion.
- Granularidad de agentes de desarrollo Odoo.
- Contrato formal de cada agente.
- Tipos y formatos de contratos.
- Gates exactos por fase.
- Extension de contratos.
- Aprobacion automatica entre fases.
- Instaladores local/global.
- Perfil de permisos por etapa.
