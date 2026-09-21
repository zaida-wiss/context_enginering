---
project: avanza
type: visible_content_boundary
version: 1.0
status: active
scope: projects/avanza/presentation
---

# Avanza Visible Content Boundary

This file defines what may become visible text in the user-facing Avanza Monday presentation.

## 1. Visible text sources

Visible meeting text may come only from:

1. verified Avanza repository events, PRs, commits, branches, issues and project-board data;
2. registered Avanza course/schedule/deadline sources;
3. registered Avanza team roster and project context;
4. explicit team-confirmed decisions or meeting data;
5. clearly labelled AI analysis/proposals that answer the meeting point.

Framework rules, hierarchy rules, render-control notes, validator messages, QA checks, debug receipts and generator explanations are **control input only**. They may shape selection, layout and validation, but they are not presentation content.

## 2. Forbidden visible control-language leakage

The delivered deck must not contain visible phrases whose source is the AI framework or generator process rather than Avanza/project evidence, for example:

- "hierarki" as an explanation of the generation method;
- "dev after hierarchy fix" or commit/version receipts;
- "whitespace is better than fake data";
- "renderkontroll", "leveranskontroll", "QA", "debug", "validator";
- explanations of how the AI should behave.

If such information is useful, it belongs in an internal audit log, not on a meeting slide.

## 3. Meeting-point 1 branch semantics

Meeting point 1 must distinguish delivery targets:

- `develop` shows work completed into the primary integration branch.
- `Java-Development-Environment` shows work completed into the Backend/Java collection branch.
- `C/C++-Native` shows work completed into the Native/System collection branch.

For collection branches, completed means verified branch activity during the active sprint window that changed the collection branch. Evidence may be:

- merged PR to that branch;
- merge commit on that branch;
- rebase/squash/fast-forward update on that branch;
- direct commit on that branch when it is the registered collection branch.

Collection-branch completion does **not** require the work to have reached `develop` yet. If it is on the registered collection branch, it is avklarat for that branch page and should be shown there with its own evidence state.

## 4. Required card bottom facts for completed work

When evidence exists, completed-work cards in meeting point 1 must render these facts as distinct concepts:

- developed by / assigned to / contributor;
- merged by or branch-updater when the event is a direct collection-branch update;
- approved by / reviewer when the source is a PR with submitted approval;
- branch and event type: PR merge, merge commit, rebase/fast-forward, or direct collection-branch commit;
- relevant event time.

If a fact is unavailable, show an explicit quiet unknown only when it affects trust; do not replace it with an AI instruction or omit the whole branch page.

## 5. Visual semantics that must survive rendering

- Team ownership uses Avanza team identity from `TEAM_VISUAL_IDENTITY.yaml`.
- Criticality uses red/orange/green symbol + text + color.
- Cross-team uses its own Cross-team identity and is not rendered as neutral metadata.
- Provenance symbols from the active provenance authority remain attached to the content they qualify.

## 6. Special layouts override ordinary card grid

When a meeting point has a registered special layout, that layout wins over the ordinary six-slot card grid:

- ② timeline;
- ⑥ dependency/blocker map;
- ⑨ vertical execution order;
- ⑫ chronological sprint/day plan.

The ordinary card grid is fallback for ordinary card pages only.
