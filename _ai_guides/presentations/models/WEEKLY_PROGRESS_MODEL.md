---
name: weekly_progress_model
description: Generic supporting model for reconstructing verified progress between meeting boundaries
metadata:
  type: process
---

# Weekly progress model

Progress reporting is reconstructed from verified repository activity for the exact registered reporting period. It is a retrospective of what was actually delivered or materially advanced, not a backlog or future-planning view.

Read `REPO_FIRST_RECONSTRUCTION.md` first.

## Evidence to collect

Collect and cross-reference:
1. commits on registered relevant branches;
2. PRs merged during the reporting period;
3. open PRs with verified work activity during the period;
4. issues closed during the period;
5. open issues with verified code/documentation/PR activity during the period.

Commit counts are evidence, not presentation structure. Cluster related evidence into meaningful work areas instead of rendering raw activity lists.

## Classification

### Delivered
Work may be classified as delivered only when the active integrity/Definition-of-Done rules support that conclusion.

### Materially advanced
Open work counts as materially advanced only when there is verified work activity such as commits, code changes, PR creation/update or documentation changes. A comment, board-status change or untouched newly opened issue is not sufficient by itself.

## Presentation semantics

Organize progress by registered work areas/teams derived from project data. Do not hard-code team names, people, issue numbers, repository paths, branch names or dates in this framework.

Each rendered progress item should communicate:
- what changed;
- who contributed, when verified;
- its grounded status;
- why the change matters;
- concise evidence/provenance.

Risks, blockers, dependencies, backlog and future plans belong to their owning meeting points rather than being mixed into completed-work reporting.

## Accessibility

Status must not rely on color alone. Use the canonical symbol/text semantics from the active design and provenance authorities. The active authorities own colors, typography, card structure and final slide composition.

## Completeness gate

Before composition:
- the exact reporting period is known;
- commits, PRs and issues have been cross-referenced;
- activity without a linked issue has still been considered;
- all canonical roster members have been checked;
- unknown or incomplete evidence remains explicitly unknown/incomplete rather than guessed.

This supporting model does not override active authorities.
