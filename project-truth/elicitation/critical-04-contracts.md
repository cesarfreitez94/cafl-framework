# CRIT-04: Contracts

Status: not-started

## Session Objective

- [draft] Definir que contratos son necesarios para coordinar fases, agentes y entregables, sin crear contratos finales.

## Context

- [accepted] `framework/CONTRACT_CATALOG.md` existe como catalogo preliminar y evidencia secundaria.
- [draft] Los contratos deben reducir ambiguedad, no crear documentacion innecesaria.

## Questions For The Owner

- [open-question] Que tipo de informacion debe estar obligatoriamente acordada antes de avanzar de fase?
- [open-question] Que contratos son indispensables para evitar trabajo ambiguo?
- [open-question] Que contratos serian exceso documental para V1?
- [open-question] Los contratos deben ser legibles por humanos, validables por maquina o ambos?
- [open-question] Que nivel de formalidad necesita cada contrato?
- [open-question] Como se versionan cambios de contrato?
- [open-question] Que contrato conecta requerimientos con pruebas?
- [open-question] Que contrato conecta diseno con implementacion?

## Decisions To Make

- [open-question] Inventario minimo de contratos.
- [open-question] Formato preferido: Markdown, YAML, JSON, frontmatter, schema u otro.
- [open-question] Campos minimos.
- [open-question] Reglas de versionado y cambios.
- [open-question] Relacion con gates, evidencias y trazabilidad.

## Non-Goals For This Session

- [accepted] No redactar contratos finales.
- [accepted] No crear JSON Schema final.
- [accepted] No implementar validadores.
- [accepted] No modificar templates existentes.

## Risks If Unresolved

- [draft] Avance con entradas incompletas.
- [draft] Contratos extensos sin uso operativo.
- [draft] Diferencias no detectadas entre requerimiento, diseno, codigo y prueba.

## Output Format

- [draft] Tabla de contrato candidato, proposito, productor, consumidor, campos minimos, evidencia relacionada y estado.
- [draft] Lista de contratos rechazados o postergados.

## Acceptance Criteria

- [draft] Cada contrato candidato tiene consumidor claro.
- [draft] Cada contrato candidato justifica su costo documental.
- [draft] Los formatos quedan aceptados o registrados como decision pendiente.
