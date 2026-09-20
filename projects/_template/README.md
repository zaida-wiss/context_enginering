# Project template

This directory is the canonical blueprint for adding a new project to the context-engineering framework.

## Goal

A project must be removable without breaking the global framework. Project facts belong under `projects/<project_id>/`; reusable behavior belongs outside `projects/`.

## Create a project

1. Copy this template to `projects/<project_id>/`.
2. Fill `PROJECT.yaml` and replace all placeholders.
3. Create only conditional/optional files that the project actually needs.
4. Register the project in root `PROJECTS.yaml`.
5. Verify every path declared by `PROJECT.yaml` exists.
6. Run the repository integrity audit.
7. Never copy another project's facts as defaults.

## Information placement

| Information | Canonical destination | Level |
|---|---|---|
| Project identity/repository | `PROJECT.yaml` | REQUIRED |
| External/live sources and fallbacks | `sources/SOURCES.yaml` | REQUIRED |
| People, roles, teams | `team/TEAM_ROSTER.md` | CONDITIONAL |
| Sprint/cadence/timezone | `project/cadence/CADENCE.yaml` | CONDITIONAL |
| Working-time constraints | `project/constraints/WORKING_TIME.yaml` | CONDITIONAL |
| Branch/integration flow | `project/repository/REPOSITORY_FLOW.yaml` | CONDITIONAL |
| Requirements | `requirements/REQUIREMENTS.md` | CONDITIONAL |
| Milestones | `requirements/MILESTONES.yaml` | CONDITIONAL |
| Deadlines | `requirements/DEADLINES.md` | CONDITIONAL |
| Visual identity/design facts | `design/VISUAL_IDENTITY.yaml` | OPTIONAL |
| Confirmed project decisions | `decisions/` | CONDITIONAL |
| Other long-lived project facts | `context/` | OPTIONAL |

## Placement rules for AI

1. Classify new information as **global reusable behavior** or **project-owned fact/context** before writing.
2. Global reusable AI behavior belongs in the owning global authority, normally under `_ai_guides/`; never place it in a project merely because it was discovered while working on that project.
3. Project-owned information goes to the narrowest matching project domain in the table above.
4. Do not invent a project directory because information does not fit. Use `context/` only for genuine long-lived project context that has no narrower owner.
5. If the same new category recurs across projects, propose a generic category/contract rather than silently creating inconsistent folders.
6. Do not duplicate the same fact into several canonical files. Reference its owner.
7. Dynamic state (PRs, issues, current blockers, current branches) should normally be read from registered sources, not stored as long-lived facts.
8. When moving information, use preservation-first migration: compare, preserve unique value, repoint consumers, verify, then retire the old copy.
9. If active rules conflict, stop and ask for a decision; folder precedence does not resolve semantic conflicts.

## Deletion invariant

Deleting one project directory and removing its entry from `PROJECTS.yaml` must not break global framework files. Global files may resolve selected-project capabilities abstractly, but must not require one named project to exist.
