# Roadmap

## Fase -1: Meta-Elicitacion Y Revalidacion

Objetivo: cerrar el modelo operativo antes de planificar la implementacion.

Entregables:

- Blueprint operativo.
- Especificacion de agentes.
- Catalogo de contratos.
- Catalogo de gates.
- Modelo de instalacion local/global OpenCode.
- Politica de aprobacion automatica por severidad.

Criterio de cierre:

- No quedan decisiones criticas sin resolver.
- Cada agente tiene responsabilidades, entradas, salidas y limites claros.
- Cada fase tiene contrato de entrada, contrato de salida y gates.
- La estructura fuente `framework/` queda validada.

## Fase 0: Control Del Proyecto

Objetivo: establecer control versionado del proyecto.

Entregables:

- `PROJECT_CONTROL.md`.
- `BACKLOG.md`.
- `DECISIONS.md`.
- `RISKS.md`.
- Plantillas de control.

## Fase 1: Arquitectura Fuente Del Framework

Objetivo: construir el framework fuente sin activarlo como runtime OpenCode.

Entregables:

- `framework/agents`.
- `framework/skills`.
- `framework/commands`.
- `framework/config`.
- `framework/templates`.
- `framework/rag`.
- `framework/ci`.
- `framework/examples`.

## Fase 2: Instaladores OpenCode

Objetivo: convertir fuente del framework en runtime OpenCode local o global.

Entregables:

- Instalador local por proyecto.
- Instalador global de usuario.
- Validadores de estructura.
- Manifiesto de archivos instalados.
- Modo dry-run.

## Fase 3: Metodologia Y Plantillas

Objetivo: definir artefactos obligatorios, contratos y gates documentales.

Entregables:

- Plantillas PRD.
- Plantillas SDD.
- Plantillas de contratos.
- Matriz de trazabilidad.
- Plan de testing.
- Reporte de entrega.
- Artefactos comerciales.

## Fase 4: Pipeline De Fabrica

Objetivo: operar de idea a entrega con comandos y agentes.

Entregables:

- Comandos por etapa.
- Orquestacion de handoffs.
- Validacion de gates.
- Reportes de estado.

## Fase 5: RAG Oficial Odoo

Objetivo: recuperar conocimiento oficial Odoo v18 con citas auditables.

Entregables:

- Ingesta repo oficial Odoo 18.
- Ingesta documentacion oficial Odoo 18.
- PostgreSQL con pgvector.
- Snapshots auditables.
- Politica de actualizacion.

## Fase 6: Testing Y CI/CD

Objetivo: asegurar calidad reproducible.

Entregables:

- Contrato CI/CD agnostico.
- Comandos estandar locales.
- Plantillas GitHub Actions.
- Plantillas GitLab CI.
- Evidencias JUnit, Markdown, screenshots y videos.

## Fase 7: Piloto Modulo Simple

Objetivo: validar V1 end-to-end.

Entregables:

- PRD del modulo piloto.
- SDD del modulo piloto.
- Contratos del modulo piloto.
- Addon Odoo simple.
- Tests backend/frontend aplicables.
- Reporte de entrega.

## V1.1: Motor Normativo Chileno

Objetivo: extender el framework hacia cumplimiento legal chileno.

Alcance preliminar:

- Obligaciones.
- Evidencias.
- Matrices de riesgo.
- Workflows.
- Reportes legales.
- Integraciones futuras.
