# Context Engineering — AI Context & Process Framework

This repository is a **multi-project context-engineering framework** for:
- global AI behavior and conflict handling
- project-context routing
- reusable task workflows
- presentation generation and validation
- registered project data sources and project-specific context

Project-specific facts do not belong in the global framework. Resolve the
requested project through `PROJECTS.yaml`, then load that project's manifest
and only the project context required for the task.

---

## Global AI framework

Before any task-specific routing, apply
[`_ai_guides/AI_FRAMEWORK.yaml`](_ai_guides/AI_FRAMEWORK.yaml).

Its conflict-decision gate applies to every AI task in this repository. When
active rules genuinely contradict each other, the AI must stop, show the
conflicting rules and consequences, and ask the user to decide **before** it
changes the rules or continues the affected task.

## Project resolution

Registered projects and their context roots are resolved through
[`PROJECTS.yaml`](PROJECTS.yaml).

The context repository itself never selects a project. A project must be
identified from the user's request or another verified project-selection signal
defined by the global framework. If no project can be resolved, ask which
project applies.

Each project owns its project-specific facts, source definitions, schedules,
people, design references and other project context under its registered project
root.

## Context registry

Machine-readable global paths and task bundles are registered in
[`CONTEXT_REGISTRY.yaml`](CONTEXT_REGISTRY.yaml). Use it as the global path
atlas for reusable authorities and task dependencies. Project-specific paths are
resolved through the selected project's manifest.

New information is placed through
[`_ai_guides/context/CONTEXT_ROUTING.yaml`](_ai_guides/context/CONTEXT_ROUTING.yaml)
and the exact-placement contract
[`_ai_guides/context/CONTEXT_PLACEMENT_CONTRACT.yaml`](_ai_guides/context/CONTEXT_PLACEMENT_CONTRACT.yaml).

Before canonical repository mutation, the AI resolves and normally tells the user:
- global/project/task-only scope,
- information class,
- owning authority/capability,
- exact target file,
- required propagation.

Mixed user text is split into separate information units before routing. A focused
control question is required when project/destination/authority is genuinely
ambiguous or a new canonical capability is needed; otherwise the AI may proceed
after stating the destination.

## What do you want to do?

### Regular project work
→ [`_ai_guides/project/PROJECT_CONTEXT_ROUTER.md`](_ai_guides/project/PROJECT_CONTEXT_ROUTER.md)

### Create a presentation
→ [`_ai_guides/presentations/MANDATORY_READING_ORDER.md`](_ai_guides/presentations/MANDATORY_READING_ORDER.md)

### Improve presentation behavior
Update the owning instruction in the context repository. Do not alter an
existing presentation unless the user explicitly asks for that artifact to be
updated or regenerated.

If new feedback contradicts an active rule, show both rules and ask which one
has priority before changing the context. The latest wording never silently wins
by default.

WCAG 2.2 AA cannot be deprioritized. A conflicting request must be explained
and converted into the closest accessible alternative instead.

### AI guidelines
→ [`_ai_guides/README.md`](_ai_guides/README.md)

---

## Authority map — one owner per rule category

| Question | Authority |
|---|---|
| Which presentation files are active authorities? | [`AUTHORITY_REGISTRY.yaml`](_ai_guides/presentations/AUTHORITY_REGISTRY.yaml) |
| How does the presentation pipeline work? | [`SYSTEM_CONTRACT.yaml`](_ai_guides/presentations/SYSTEM_CONTRACT.yaml) |
| What data sources are allowed? | Selected project's manifest → source registry |
| What are the absolute WCAG/NPF boundaries? | [`ACCESSIBILITY_NEURODIVERSITY.md`](_ai_guides/presentations/design/ACCESSIBILITY_NEURODIVERSITY.md) |
| How does the deck look globally? | [`VISUAL_DESIGN_MANDATORY.md`](_ai_guides/presentations/design/VISUAL_DESIGN_MANDATORY.md) |
| What are the hard readability/typography rules? | [`READABILITY_HARD_RULES.md`](_ai_guides/presentations/design/READABILITY_HARD_RULES.md) |
| How must cards behave internally? | [`CARD_COMPONENT_STANDARD.md`](_ai_guides/presentations/design/CARD_COMPONENT_STANDARD.md) |
| How do facts/team input differ from AI suggestions? | [`PROVENANCE_AND_AI_LABELING.md`](_ai_guides/presentations/design/PROVENANCE_AND_AI_LABELING.md) |
| How is responsive fit/pagination handled? | [`LAYOUT_OVERFLOW_GUARD.md`](_ai_guides/presentations/monday_meeting/design/LAYOUT_OVERFLOW_GUARD.md) |
| What slides exist and what data belongs on them? | [`SLIDE_DETAIL_SPEC.md`](_ai_guides/presentations/monday_meeting/design/SLIDE_DETAIL_SPEC.md) |
| How is active work detected? | [`ACTIVE_WORK_DETECTION_MODEL.md`](_ai_guides/presentations/data/ACTIVE_WORK_DETECTION_MODEL.md) |
| How is the final artifact validated? | [`RENDER_GATE_CHECKLIST.md`](_ai_guides/presentations/verification/RENDER_GATE_CHECKLIST.md) |
| Where should new rules be placed? | [`DESIGN_AUTHORITY.md`](_ai_guides/presentations/design/DESIGN_AUTHORITY.md) + [`ARCHITECTURE.md`](_ai_guides/presentations/ARCHITECTURE.md) |
| Where should newly supplied context/facts/rules be stored? | [`CONTEXT_PLACEMENT_CONTRACT.yaml`](_ai_guides/context/CONTEXT_PLACEMENT_CONTRACT.yaml) + [`CONTEXT_ROUTING.yaml`](_ai_guides/context/CONTEXT_ROUTING.yaml) |
| How are files/folders moved safely without breaking routing? | [`PATH_MIGRATION_PLAN.yaml`](_ai_guides/context/PATH_MIGRATION_PLAN.yaml) |

Do not add competing rules outside the owning authority. Project facts are
resolved through the selected project's manifest rather than embedded in these
global authorities.

After changing presentation instructions, run:

```bash
python3 _audit/validate_presentation_authorities.py
```

## Conflict rule

Global conflict behavior is normatively owned by
[`_ai_guides/AI_FRAMEWORK.yaml`](_ai_guides/AI_FRAMEWORK.yaml).

For a genuine conflict:
1. STOP the affected work.
2. Show the conflicting rules and owning files.
3. Explain the consequence of each option.
4. Ask the user to decide.
5. Update the owning context rule(s) and regression test after the decision.
6. Continue only when the context is consistent.

Authority maps identify ownership; they must not be used to silently choose
between genuinely incompatible active requirements.
