---
name: project_context_router
description: Generic router from a resolved project context to canonical task owners
metadata:
  type: router
  status: active
  version: 3.0
---

# Project context router

## Purpose

This file routes work after the active project has been resolved. It does not
choose a historical/default project and does not repeat project facts,
presentation rules, data-source rules or team standards.

## Resolve project first

Apply [`../AI_FRAMEWORK.yaml`](../AI_FRAMEWORK.yaml) and resolve project identity
through [`../../PROJECTS.yaml`](../../PROJECTS.yaml).

If multiple projects are registered and neither the user nor a verifiable active
repository/workspace identifies one uniquely, ask the user which project applies.
Never assume the historically most common project.

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
**Version:** 3.0
