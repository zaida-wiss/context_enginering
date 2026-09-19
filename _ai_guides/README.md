# AI Guides

This directory contains AI operating guidance. It is not itself the task entry
point.

## Start here

1. Start from the repository root `README.md`.
2. Load `AI_FRAMEWORK.yaml` for global behavior.
3. Resolve the task through `../CONTEXT_REGISTRY.yaml`.
4. Follow only the active authorities registered for that task.

If two active rules conflict, stop the affected work, identify the conflicting
rules and ask the user to decide. Never resolve an active-rule conflict
silently.

## Presentations

For a presentation task, use:

- `presentations/MANDATORY_READING_ORDER.md` — bootstrap/read order
- `presentations/AUTHORITY_REGISTRY.yaml` — active authority ownership
- `presentations/SYSTEM_CONTRACT.yaml` — execution contract

The Monday Meeting composition is owned by:

- `presentations/monday_meeting/structure/COMPOSITION_ARCHITECTURE.md`
- `presentations/monday_meeting/design/SLIDE_DETAIL_SPEC.md`

Presentation verification is owned by:

- `presentations/verification/RENDER_GATE_CHECKLIST.md`
- `presentations/design/DESIGN_AUTHORITY.md`
- `presentations/ARCHITECTURE.md`

Registered project data and source routing remain separate from framework
instructions. Follow the data/source authorities reached through the task
contract rather than copying project facts into this guide.

## Project guidance

Project-task routing starts in `project/PROJECT_CONTEXT_ROUTER.md` after the
root task route has been resolved.

## Reference-only helpers

- `NAVIGATION.md` — convenience index only
- `TROUBLESHOOTING.md` — troubleshooting index
- `ORDBOK.md` — terminology
- `SKILLS.md` — general task guidance

Reference files do not override active authorities.

## Retired material

Retired or historical guides are outside the production task bundle. They must
not be used to recover an old rule merely because an old file still exists.
Valuable generic behavior must first be represented by an active authority and
its regression protection.
