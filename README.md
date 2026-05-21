# CAFL Odoo AI Factory Framework

Framework fuente para construir una fabrica interna de desarrollo Odoo v18 Community operada con agentes de IA en OpenCode.

Este repositorio no contiene la instalacion runtime de OpenCode. El codigo fuente del framework vive en `framework/` y futuros instaladores materializaran agentes, skills, comandos y configuraciones hacia una instalacion local o global de OpenCode.

## Objetivo

Crear una solucion/framework capaz de elicitar, explorar, disenar, desarrollar, testear y entregar modulos Odoo v18 bajo un proceso controlado, trazable y verificable.

## Principios

- Separar desarrollo del framework de su runtime OpenCode.
- Evitar que agentes en construccion sean descubiertos automaticamente por OpenCode.
- Trabajar con artefactos, contratos, gates, trazabilidad y evidencia.
- Usar fuentes oficiales Odoo y fuentes oficiales normativas cuando aplique.
- Mantener control de alcance para evitar un proyecto interminable.
- Priorizar Odoo v18 Community.
- Operar en espanol tecnico.

## Estructura Principal

```text
framework/
  agents/       # Fuentes de agentes, no runtime OpenCode
  skills/       # Fuentes/templates de skills, no runtime OpenCode
  commands/     # Fuentes de comandos, no runtime OpenCode
  config/       # Templates de configuracion e instalacion
  templates/    # Plantillas de artefactos
  rag/          # Fuentes, schemas y procesos RAG
  ci/           # Contrato y plantillas CI/CD
  examples/     # Pilotos y ejemplos
```

## Estado Actual

Se creo la estructura fuente y se respaldaron las decisiones iniciales de elicitacion. La siguiente etapa es ejecutar nuevas sesiones de elicitacion para cerrar roles, contratos, gates, granularidad de agentes y modelo de aprobacion antes de planificar la implementacion detallada.
