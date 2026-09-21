---
name: project_context_router
description: Generic router from a resolved project context to canonical task owners
metadata:
  type: router
  status: active
  version: 3.2
---

# Project context router

## Purpose

This file routes work after the active project has been resolved. It does not
choose a historical/default project and does not repeat project facts,
presentation rules, data-source rules or team standards.

## Resolve project first

Apply [`../AI_FRAMEWORK.yaml`](../AI_FRAMEWORK.yaml) and resolve project identity
through [`../../PROJECTS.yaml`](../../PROJECTS.yaml).

If neither the user nor a verifiable separate active project repository/workspace
identifies a project uniquely, ask the user which project applies. This applies
even when only one project is currently registered. Opening or linking only this
context repository never selects a project.

After resolution, load only:
1. the global framework,
2. the selected project's registered context,
3. task-specific authorities needed for the request.

Do not mix facts, course material, design references, sources, people or current
state between projects.

## Canonical task routing

Resolve canonical task paths through
[`../../CONTEXT_REGISTRY.yaml`](../../CONTEXT_REGISTRY.yaml).

The current registry still contains legacy project paths while project-specific
data is migrated preservation-first into registered project roots. A legacy path
may be used only after project resolution identifies the project that owns it.

## Project creation and information placement

For a new project, use `../../projects/_template/README.md` and
`../../projects/_template/PROJECT.yaml` as the global onboarding contract.

Before writing newly learned information, classify it as either global reusable
behavior or selected-project context. Exact placement follows
`../context/CONTEXT_PLACEMENT_CONTRACT.yaml`. Project context goes to the
narrowest registered project domain under the selected project's root.

Real project facts, examples, people, branches, repository/source IDs, course
material, screenshots/assets, project decisions and project-grounded audit
records remain under that project root. Global AI guides and validators use only
abstract routing language and synthetic project-neutral examples. Do not copy another project's folder contents as
defaults, invent a new project folder ad hoc, or use `context/` as a dumping
ground. If a genuinely new category recurs across projects, propose a generic
contract/category.

A project may omit conditional/optional capabilities. Task routing must require
only capabilities needed by the requested task and declared by the selected
project.

## Current-state principle

Current claims about issues, PRs, branches, commits, blockers, reviews,
schedules or other changing project state come from the selected project's
registered current source.

Long-lived context explains the selected project; live data establishes its
current state.

## Conflict behavior

A genuine active-rule conflict is handled by the global conflict-decision gate.
Router order must never silently resolve it.

---

**Status:** ACTIVE ROUTER
**Version:** 3.2
