# Project Control

## Proposito

Documento maestro para controlar alcance, decisiones, fases, riesgos, gates y estado del proyecto CAFL Odoo AI Factory Framework.

## Estado

- Estado actual: fase previa de definicion y resguardo de contexto.
- Implementacion runtime: no iniciada.
- Framework fuente: estructura inicial creada en `framework/`.
- Instaladores OpenCode: pendientes.
- RAG: pendiente.
- Piloto: pendiente.

## Objetivo De La Solucion

Crear un framework OpenCode para operar una fabrica interna de desarrollo Odoo v18 Community con agentes de IA capaces de:

- Elicitar requerimientos.
- Explorar procesos y documentos.
- Disenar PRD, SDD y contratos.
- Desarrollar modulos Odoo.
- Testear backend, frontend, OWL, tours y Playwright.
- Generar evidencias y reportes.
- Controlar alcance, riesgos, decisiones y deuda.

## Corte V1 Acordado

La V1 sera un framework completo sin motor legal avanzado.

Debe incluir:

- Agentes, skills, comandos, permisos, plantillas y modelo instalable para OpenCode.
- Flujo completo de idea a entrega.
- RAG inicial con fuentes oficiales Odoo v18 usando PostgreSQL y pgvector.
- CI/CD agnostico con contrato, comandos y plantillas.
- Testing completo definido y ejecutable.
- Piloto de modulo Odoo simple end-to-end.
- Estructura base para riesgo legal critico, sin automatizar el motor normativo completo.

## Fuera De Alcance V1

- Motor normativo chileno completo.
- Automatizacion legal sin control de riesgo critico.
- Soporte Odoo Enterprise como objetivo principal.
- Despliegue productivo totalmente autonomo.
- Marketplace o producto comercial vendible.
- Multi-cliente avanzado.
- Integraciones legales externas complejas.

## Decisiones Clave

- Tipo de solucion: framework OpenCode.
- Uso comercial: interno para el emprendimiento.
- Instalacion: modelo mixto con core reutilizable y overrides por proyecto.
- Desarrollo del framework: fuente en `framework/`, no en `.opencode`.
- Runtime: instaladores copiaran/generaran archivos hacia OpenCode local o global.
- Odoo objetivo: Community v18.
- Addons custom: framework separado de repositorios de addons.
- Flujo: modo mixto, pipeline completo y comandos por etapa.
- Gates: automaticos por severidad.
- Aprobaciones humanas obligatorias: ninguna por defecto.
- Riesgo legal: bloqueo solo critico.
- Estado de control: Markdown versionado.
- Idioma: espanol tecnico.
- Modelos IA: agnostico por proveedor.

## Criterio De Cierre V1

La V1 se considera cerrada cuando:

- La estructura fuente del framework esta completa.
- Existen instaladores local/global para OpenCode.
- Existen agentes fuente y contratos de agente.
- Existen skills y comandos fuente.
- Existe modelo de permisos por perfil.
- Existe set de plantillas obligatorias.
- Existe contrato CI/CD agnostico.
- Existe RAG Odoo oficial inicial.
- Existe piloto de modulo simple generado por el flujo.
- Todos los gates aplicables del piloto pasan.
- Todos los tests aplicables del piloto pasan.
- Existe reporte final con evidencias.
- Queda documentado lo que pasa a V1.1.

## Proxima Fase

Antes de planificar la implementacion detallada se ejecutaran sesiones adicionales de elicitacion y revalidacion para cerrar:

- Responsabilidades de cada agente.
- Granularidad de agentes de desarrollo.
- Contratos entre fases y agentes.
- Gates por fase.
- Formato y extension de contratos.
- Aprobacion automatica de fases.
- Estructura de instaladores OpenCode.
- Limites de autonomia.
