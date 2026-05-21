# Framework Source

Directorio fuente del framework CAFL Odoo AI Factory.

Nada dentro de este directorio debe ser asumido como runtime directo de OpenCode. Los archivos aqui son fuentes, templates o especificaciones. Instaladores futuros generaran la estructura OpenCode real en ubicaciones locales o globales.

## Regla Principal

No crear aqui `.opencode/agents`, `.opencode/skills` ni `.opencode/opencode.json` runtime.

## Directorios

- `agents`: fuentes de agentes y contratos de responsabilidad.
- `skills`: templates de skills.
- `commands`: fuentes de comandos.
- `config`: templates de configuracion y permisos.
- `templates`: plantillas de artefactos.
- `rag`: definiciones de ingesta, fuentes, queries y schemas.
- `ci`: contrato y plantillas CI/CD.
- `examples`: pilotos y modulos de ejemplo.
