---
name: dependency_chain_planning
description: Presentation adapter for global dependency and sequencing analysis
metadata:
  type: presentation_adapter
  for_presentations: true
  applies_to: "Blockers/dependencies and prioritization views"
  global_analysis_authority: "_ai_guides/PROJECT_WORK_ANALYSIS.md"
---

# Dependency and sequencing — presentation adapter

General dependency, collision, ownership-aware sequencing and pre-implementation
reasoning is owned by `_ai_guides/PROJECT_WORK_ANALYSIS.md`.

This file owns only how relevant findings are selected for a presentation.

## Presentation use

When verified project analysis contains material dependencies or sequencing
findings, the deck may show:
- verified dependency chains that matter to the meeting;
- blockers and the work they prevent or unlock;
- safe parallel work;
- work that should wait because of a verified dependency or material rework risk;
- mitigations or coordination actions;
- ownership boundaries and integration contracts when they materially explain
  the dependency.

Do not invent a dependency merely because two issues touch the same area.
Do not turn historical specialization into permanent personal ownership.
Do not recommend moving implementation across registered team ownership
boundaries.

## Provenance

Keep source facts, AI analysis and AI recommendations distinct according to the
presentation provenance authority.

A derived sequence is an AI recommendation unless the team has explicitly
decided that sequence in a registered source.

## Presentation structure

The presentation may use a dependency graph, ordered cards or another accessible
layout appropriate to the meeting. Visual layout, density, colors and typography
are owned by the presentation design authorities.

Do not force:
- a fixed number of phases;
- a fixed issue count per person;
- a universal one-active-issue rule;
- a universal requirement that every dependency must be merged before any
  dependent work begins.

Those are project/team constraints only when explicitly registered.

## Project isolation

Examples in this global presentation adapter must be synthetic. Real project
people, issue numbers, branch names, repository names and project-specific
workflow rules belong under the selected project's context.

---
status: ACTIVE
