# CAFL Blueprint Automation Loop

## 1. Current Source-Of-Truth Files

- `project-truth/implementation-blueprint.md` is the primary working contract and Blueprint artifact. If any automation rule conflicts with it, this file wins.
- `project-truth/blueprint-contract.yaml` governs the MVP author -> verify -> fix -> re-verify loop. It extracts rules for agent use and does not replace the working contract.
- `project-truth/blueprint-state.yaml` is the operational state for section selection, dependency checks, statuses, owner approvals, fix counters, reports, open issues, and context summaries.
- Authority order for Blueprint content remains: `project-truth/decisions/accepted.md`, `project-truth/TOM.md`, `project-truth/decisions/rejected.md`, `project-truth/decisions/superseded.md`, `project-truth/critical-map.md`, `project-truth/decisions/pending.md`, then `project-truth/risks.md` as support.
- Current state: Iteration 1 is `in-progress`; S01 is `approved`; S02-S19 are `not-started`; commits are `owner_only`.
- This document is operational coordination only. It is not a parallel source of truth.

## 2. MVP Workflow

- `cafl-blueprint-orchestrator` selects one eligible section per run from `project-truth/blueprint-state.yaml` and checks dependencies, current iteration, owner gates, and allowed status transitions.
- `cafl-blueprint-author` elaborates only the selected section in `project-truth/implementation-blueprint.md`, using the required inputs and prior approved context from `project-truth/blueprint-state.yaml`.
- In author mode, the author produces the compact section author report at `reports/blueprint/{section_id}-author-report.md`; `last_author_report` points to this author report.
- `cafl-blueprint-verifier` audits the selected section against the working contract, automation contract, section inputs, prior approved context, and traceability requirements.
- If verification fails, the section moves to `needs-fix`; `cafl-blueprint-author` runs in fixer mode and addresses only verifier-reported issues.
- In fixer mode, the author produces the compact fix report at `reports/blueprint/{section_id}-fix-report.md`; `last_fix_report` points to this fix report when fixer mode runs.
- Fix and re-verification can repeat up to `max_fix_iterations_per_section: 2`.
- If verification passes, the section waits for explicit owner approval; no agent can approve or close it.
- When all sections in an iteration are owner-approved, `cafl-blueprint-orchestrator` runs in gatekeeper mode, prepares the compact iteration gate report at `reports/blueprint/{iteration_id}-gate-report.md`, and asks the owner for the iteration gate decision.

## 3. Agent Responsibilities

- `cafl-blueprint-orchestrator`: coordinates the loop, selects eligible sections, enforces dependencies and status transitions, routes author/verifier work, detects owner gates, and acts as gatekeeper at iteration end.
- `cafl-blueprint-orchestrator` must not implement Blueprint section content directly.
- `cafl-blueprint-orchestrator` does not write section reports; section reports are owned by author mode, fixer mode, and verifier.
- `cafl-blueprint-author`: writes selected section content, keeps content within the selected section, updates required operational state/report fields, and in fixer mode changes only items reported by the verifier.
- `cafl-blueprint-author` must not verify its own work, self-approve, advance future sections, or change acceptance criteria to pass.
- `cafl-blueprint-verifier`: audits section output against contract, inputs, authority order, prior approved context, non-goals, and traceability.
- `cafl-blueprint-verifier` must not fix issues, implement content, change acceptance criteria, or approve the section.
- Fixer is author mode. Gatekeeper is orchestrator mode. No separate fixer or gatekeeper agent exists in MVP.

## 4. State Transitions

- Section flow: `not-started` -> `in-progress` -> `in-verification` -> `approved` only after explicit owner approval.
- Fix flow: `in-verification` -> `needs-fix` -> `in-progress` -> `in-verification`, with at most two fix iterations per section.
- If a retroactive blocker affects an earlier section or iteration, the loop stops and records the issue for owner decision; it does not silently fix prior approved content.
- If a component is not traceable to TOM, approved CRIT, or accepted decision, it must be eliminated, marked post-V1, or registered as `owner decision required`.
- Iteration flow: active iteration remains `in-progress` until all its sections are owner-approved, then reaches the `pending-owner-approval` gate.
- Iteration closure and next-iteration start require explicit owner gate approval.
- `closed` is owner-gated; agents do not close sections or iterations by themselves.

## 5. Context Continuity Rule

- Before authoring a section, the author must read the section inputs in `project-truth/implementation-blueprint.md` and the approved prior `context_summary` values in `project-truth/blueprint-state.yaml`.
- The verifier must check consistency with prior approved sections and the current operational state.
- After owner approval of a section, the section `context_summary` in `project-truth/blueprint-state.yaml` must be updated so the next section receives compact continuity context.
- Conflicts are registered, not resolved by agent judgment: blocking conflicts use `needs-owner-decision`; non-blocking conflicts use `open-question`.

## 6. Verification Rule

- Verification is mandatory before owner approval and must be performed by `cafl-blueprint-verifier`, not by the author.
- Verification checks scope, selected section boundaries, authority order, traceability, non-goals, prior context consistency, no use of `framework/`, no future-section advancement, and no forbidden artifacts.
- Verifier output is a compact verification report at `reports/blueprint/{section_id}-verification-report.md` with pass/fail status and concrete issues; `last_verification_report` points to this verification report.
- A passing verification does not approve the section; it only makes it ready for owner decision.

## 7. Owner Gates

- Owner explicitly approves sections; agents cannot self-approve or approve each other.
- Owner gate closes iterations after all sections in that iteration are approved.
- The next iteration starts only after explicit owner approval of the prior iteration gate.
- Commits remain owner-only. Agents do not run `git commit` or `git push`.
- Owner decisions are required for blocking conflicts, untraceable content that cannot be removed or marked post-V1, retroactive blockers, and any attempt to expand source policy or scope.

## 8. Non-Goals

- Do not create executable agents, separate fixer/gatekeeper agents, commands, scripts, schemas, validators, runtime, RAG/vector base, backlog, PRD, or SDD.
- Do not modify source code or use `framework/` as input or reference.
- Do not reopen CRIT-01..07, TOM, or accepted decisions.
- Do not advance future sections unless that section was explicitly selected and allowed by state/dependencies.
- Do not resolve source conflicts by agent criteria.
- Do not treat reports, this coordination document, or any file outside `project-truth/` as a parallel source of truth.
