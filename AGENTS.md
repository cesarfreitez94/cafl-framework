# AGENTS.md

## Scope
- This repo is the source/control repo for the CAFL Odoo AI Factory Framework, not an installed OpenCode runtime or an Odoo addon repo.
- Default project language is Spanish tecnico for artifacts, agents, reports, and control docs; preserve the existing ASCII style.

## Source Vs Runtime
- Do not create `.opencode/agents`, `.opencode/skills`, or `.opencode/opencode.json` under `framework/`; source lives outside runtime discovery on purpose.
- Future installer mapping is `framework/agents/*.agent.md -> .opencode/agents/*.md`, `framework/skills/*/SKILL.md.template -> .opencode/skills/*/SKILL.md`, and `framework/config/opencode.runtime.json.template -> .opencode/opencode.json`.
- `framework/config/opencode.runtime.json.template` is a runtime template, not active config for this source repo.

## Current State
- `framework/MANIFEST.md` marks the framework as `0.0.0-source` and non-installable; files marked `draft`, `candidato`, or `pendiente` are specifications to complete, not implemented behavior.
- Before detailed implementation planning, `ROADMAP.md` requires meta-elicitation/revalidation of agent responsibilities, contracts, gates, install model, permissions, and automatic approvals.
- `framework/examples/simple_odoo_module/` is a placeholder pilot for V1 validation, not a runnable Odoo module yet.

## Flow
- Conceptual module flow is elicitation -> PRD -> PRD gate -> SDD -> SDD gate -> contracts -> plan/backlog -> development -> testing -> final gates -> delivery.
- `framework/commands/*.command.md` files describe future OpenCode commands; they are not executable local commands.

## Verification
- There are currently no repo-level build, lint, format, typecheck, or test manifests (`package.json`, `pyproject.toml`, `Makefile`, or CI workflows).
- `framework/ci/local/COMMANDS.md` contains candidate future commands such as `cafl-odoo validate-structure` and `cafl-odoo test-backend`; they depend on an existing Odoo environment and are not implemented here.
- Module approval requires all applicable tests to pass: Python/Odoo, HttpCase/Tours, OWL/QUnit when applicable, Playwright E2E, migration/update, security, and basic performance.

## RAG And Sources
- V1 knowledge must prioritize official Odoo v18 sources; Chilean regulatory sources are only future/base structure in V1.
- Relevant technical decisions should cite official source, version/hash, confidence, and warnings per `framework/rag/queries/QUERY_CONTRACT.md`.
- Exact official URLs, embeddings, table schema, and ingestion commands are still pending; do not invent them.

## Gates And Risk
- Gate severities are `blocker`, `critical`, `major`, `minor`, and `info`; categories include legal, seguridad, datos, operacion, UX, performance, tecnica, comercial, and alcance.
- Legal critical risk, normative contradictions, or insufficient official sources should block/escalate; V1 excludes a full Chilean legal engine.
