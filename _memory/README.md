# Memory — Legacy Domain Index

`_memory` is no longer the canonical home for project-specific memory.

Project-specific long-lived context is resolved through:
`PROJECTS.yaml → selected project → PROJECT.yaml → context.*`.

For example, team identity/membership belongs to the selected project's
registered `context.team_roster.path`, not to a global roster in this folder.

Global reusable behavior belongs under `_ai_guides/`. Project facts belong
under the corresponding `projects/<project>/` root.

Do not add new project-specific facts to `_memory`.

---

**Status:** legacy domain index
**Last updated:** 2026-09-20
