---
name: troubleshooting
description: Reference index for diagnosing context and presentation failures
metadata:
  type: reference
  updated: 2026-09-19
---

# TROUBLESHOOTING

This file owns no presentation rules. Diagnose a problem through the active
authority that owns the affected behavior.

## Wrong or missing project data

Check:

1. the registered source in `../data/SOURCES.yaml`
2. `presentations/data/DATA_ACQUISITION_CONTRACT.yaml`
3. the acquisition receipt/data audit required by `presentations/SYSTEM_CONTRACT.yaml`

Do not repair missing data by guessing, by using an unregistered source or by
copying project examples into the context framework.

## Missing, duplicated or misclassified work

Check the active work-detection/data model reached through the presentation
authority registry, then run the data-integrity checks in
`presentations/verification/RENDER_GATE_CHECKLIST.md`.

A source mismatch remains a mismatch until verified. Do not silently choose the
more convenient source.

## Wrong meeting-point content or order

Check:

- `presentations/monday_meeting/structure/COMPOSITION_ARCHITECTURE.md`
- `presentations/monday_meeting/design/SLIDE_DETAIL_SPEC.md`

Do not recover structure from retired presentation guides.

## Wrong colors, symbols, typography or card layout

Check the active owners registered in
`presentations/AUTHORITY_REGISTRY.yaml`, especially:

- `presentations/design/VISUAL_DESIGN_MANDATORY.md`
- `presentations/design/READABILITY_HARD_RULES.md`
- `presentations/design/CARD_COMPONENT_STANDARD.md`
- `presentations/design/PROVENANCE_AND_AI_LABELING.md`
- `presentations/monday_meeting/design/LAYOUT_OVERFLOW_GUARD.md`

Then verify the rendered artifact with
`presentations/verification/RENDER_GATE_CHECKLIST.md`.

## Missing slide or overflow

A required content block must not disappear merely to make a slide fit.
Use the active composition, readability and overflow authorities and create
continuation slides when required.

## Conflicting instructions

If two active rules contradict one another:

1. stop the affected work
2. identify the exact rules/files
3. explain the available choices and consequences
4. ask the user for a decision
5. update the owning context and regression protection before continuing

Do not solve the conflict by choosing the newest, nearest or most convenient
rule.

## Recurring presentation defect

Fix the owning context rule or validator first. A one-off artifact patch is not
the final fix for a recurring framework defect.

## Validation after context changes

Use the repository's active mechanical audits and smoke tests after changes to
routing or presentation authorities. A historical report or retired guide is
not evidence that the current branch passes validation.
