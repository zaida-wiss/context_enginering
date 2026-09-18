---
name: project_context_router
description: Minimal router for Avanza project work
metadata:
  type: router
  status: active
  version: 2.1
---

# Avanza project context router

## Purpose

This file routes project work to the correct canonical owner. It does not repeat
presentation rules, data-source rules or team standards.

## Start from the repository map

Resolve canonical paths through [`../../CONTEXT_REGISTRY.yaml`](../../CONTEXT_REGISTRY.yaml).

For project work:

- team/code/Git workflow → `project.team_standards`
- testing and verification → `project.testing`
- Definition of Done → `project.definition_of_done`
- default communication/feedback tone → `project.team_tone_and_collaboration`
- conflict/needs/people-support → `project.hr_and_team_support`
- issue creation → `tasks.issue_creation`
- reusable issue checklist → `project.definition_of_done_template`
- risk-register template → `project.risk_register_template`
- long-lived team identity → `memory.team_roster`
- live/current project facts → registered live sources in `data/SOURCES.yaml`
- presentation requests → the `monday_meeting_presentation` task bundle in `CONTEXT_REGISTRY.yaml`

## Current-state principle

Current claims about issues, PRs, branches, commits, blockers, reviews, schedules
or other changing project state are resolved from the registered current source
for that fact.

Long-lived context explains the project; live data establishes current state.

## Model-neutral use

Give the model the goal, the canonical owner and the relevant verified data.
Load only the dependencies needed for the current task, then validate the
result with the task's registered acceptance checks.

---

**Status:** ACTIVE ROUTER
**Version:** 2.1
**Last updated:** 2026-09-18
