# Architecture

## Separacion Fuente Y Runtime

El framework se desarrolla en `framework/`. OpenCode no debe descubrir estos archivos automaticamente como agentes o skills runtime.

Los instaladores futuros haran la transformacion:

```text
framework/agents/*.agent.md -> .opencode/agents/*.md
framework/skills/*/SKILL.md.template -> .opencode/skills/*/SKILL.md
framework/config/opencode.runtime.json.template -> .opencode/opencode.json
```

## Capas

- Fuente: definiciones editables del framework.
- Build: validacion y materializacion de runtime.
- Runtime local: instalacion en proyecto cliente.
- Runtime global: instalacion reutilizable por usuario.
- Overrides: configuracion especifica de cada proyecto Odoo.

## Flujo Conceptual

```text
idea/documento/proceso
  -> elicitacion
  -> PRD
  -> gate PRD
  -> SDD
  -> gate SDD
  -> contratos
  -> plan y backlog
  -> desarrollo
  -> testing
  -> gates finales
  -> entrega
```

## RAG

El RAG usara PostgreSQL con pgvector y snapshots auditables de fuentes oficiales.

Fuentes iniciales:

- Repo oficial Odoo 18.
- Documentacion oficial Odoo 18.
- Documentacion oficial de testing Odoo.
- Documentacion oficial de frontend/OWL Odoo.

Fuentes normativas chilenas quedaran como estructura inicial para fases posteriores.
