# Installation Model

## Proposito

Definir como el framework fuente sera instalado en OpenCode.

## Modos Candidatos

- Local por proyecto.
- Global por usuario.
- Mixto con core global y overrides por proyecto.

## Regla De Fuente

El directorio `framework/` es fuente y no runtime.

## Transformacion Esperada

```text
framework/agents/*.agent.md
  -> .opencode/agents/*.md

framework/skills/*/SKILL.md.template
  -> .opencode/skills/*/SKILL.md

framework/config/opencode.runtime.json.template
  -> .opencode/opencode.json
```

## Instalador Futuro

Debe soportar:

- Dry-run.
- Validacion previa.
- Instalacion local.
- Instalacion global.
- Manifest de archivos instalados.
- Backup de archivos reemplazados.
- Desinstalacion segura.
