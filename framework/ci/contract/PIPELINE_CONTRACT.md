# CI/CD Pipeline Contract

## Proposito

Definir un contrato agnostico para ejecutar calidad de modulos Odoo.

## Etapas Minimas

- Validar estructura.
- Validar artefactos.
- Instalar modulo.
- Ejecutar tests backend.
- Ejecutar tests frontend cuando aplique.
- Ejecutar Playwright cuando aplique.
- Validar migracion/update.
- Generar evidencias.
- Publicar reporte.

## Artefactos Esperados

- Reporte Markdown.
- JUnit.
- Screenshots/videos cuando aplique.
- Matriz de trazabilidad actualizada.

## Criterio

Todos los tests aplicables deben pasar.
