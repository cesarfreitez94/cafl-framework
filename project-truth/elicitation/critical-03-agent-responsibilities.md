# CRIT-03: Agent Responsibilities

Status: not-started

## Session Objective

- [draft] Definir roles, responsabilidades, limites y autoridad antes de crear o ajustar agentes.

## Context

- [accepted] `framework/agents/*.agent.md` existe como draft y evidencia secundaria.
- [draft] La lista actual de agentes puede ser util, incompleta, excesiva o incorrecta.

## Questions For The Owner

- [open-question] Que trabajos deben ser realizados por agentes y cuales por humanos?
- [open-question] Que rol debe coordinar alcance, estado y riesgos?
- [open-question] Que rol debe entender proceso de negocio?
- [open-question] Que rol debe decidir arquitectura Odoo?
- [open-question] El desarrollo Odoo debe dividirse por backend, frontend, QA, seguridad, migracion u otra granularidad?
- [open-question] Que autoridad tiene un agente para bloquear o replanificar?
- [open-question] Que debe hacer un agente cuando falta informacion?
- [open-question] Que agentes actuales parecen innecesarios o peligrosos?

## Decisions To Make

- [open-question] Lista minima de roles.
- [open-question] Responsabilidades y no-responsabilidades por rol.
- [open-question] Entradas y salidas por rol.
- [open-question] Handoffs principales.
- [open-question] Limites de autonomia y escalamiento.

## Non-Goals For This Session

- [accepted] No escribir prompts finales.
- [accepted] No crear agentes ejecutables.
- [accepted] No definir permisos tecnicos finales.
- [accepted] No elegir nombres definitivos de archivos runtime.

## Risks If Unresolved

- [draft] Solapamiento entre agentes.
- [draft] Trabajo duplicado o sin dueno.
- [draft] Handoffs debiles entre analisis, diseno, desarrollo y QA.
- [draft] Agentes con autoridad implicita no aceptada por el owner.

## Output Format

- [draft] Matriz de rol, proposito, responsabilidades, no-responsabilidades, entradas, salidas, autoridad y dudas.
- [draft] Lista de agentes candidatos a conservar, unir, dividir o descartar.

## Acceptance Criteria

- [draft] Cada rol candidato tiene proposito claro y limite explicito.
- [draft] No queda autoridad critica sin dueno o sin escalamiento.
- [draft] La granularidad de agentes queda aceptada o registrada como pendiente bloqueante.
