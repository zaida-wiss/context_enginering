# End-to-end run — Monday Meeting Presentation

**Date:** 2026-09-18  
**Context ref:** `dev`  
**Test case:** `_audit/END_TO_END_TEST_CASES.md` → Test 4

## Test prompt

> Skapa presentationen till måndagsmötet utifrån dev.

## Routing verified

Presentation routing resolves:

```text
README.md
  → MANDATORY_READING_ORDER.md
  → AUTHORITY_REGISTRY.yaml
  → INTEGRITY_CONSTRAINT.md
  → SYSTEM_CONTRACT.yaml
  → monday_meeting_presentation task bundle
```

The task bundle includes the shared project authorities for:

- goals/sprint planning
- risk management
- dependencies/capacity
- cross-layer awareness
- technical debt

and the presentation-specific content/design/verification authorities.

## Verified behavior

### Data integrity

- current facts require registered, verified sources
- unavailable values remain unknown/incomplete
- analysis and proposals remain separate from verified facts

### Sprint planning

- `GOOGLE_SPRINT_PLANNING` is a conditional source
- current Team Avanza 1 spreadsheet metadata does not yet contain
  `Sprintplanering`
- the current meeting protocol's Sprintmål/Sprintplan cells are empty
- presentation must therefore not invent a decided sprint goal
- future planning can still appear as `⭐ AI-förslag`

### Capacity

- no verified numeric capacity is currently present in the inspected meeting
  planning section
- a qualitative availability constraint exists
- numeric hours/percentages must not be inferred

### Meeting point 1

The slide authority still owns completed-work-only semantics plus the permitted
short "Påbörjat men inte avklarat" ending in team summaries when verified partial
value exists.

### Meeting point 9

Canonical model:

```text
Prioritering först
↓
Parallellt
↓
Backlog — lägre prioritet
↓
Förslag framåt — finns ännu inte / behöver korrigeras
```

Frontend, Backend, Native/System and Cross-team remain analysis perspectives,
not four fixed columns.

### AI provenance

- `🔎 AI-analys` = interpretation
- `⭐ AI-förslag` = recommendation
- verified facts keep source identity
- AI health-checks that conclude "nothing new" can show an exact source trace
  listing the actual sources/locations inspected

### Delivery

Default finished presentation delivery remains PDF unless another format is
explicitly requested.

## Conflict discovered during test

Before this run, `SLIDE_DETAIL_SPEC.md` used the new vertical point-9 model,
but `RENDER_GATE_CHECKLIST.md` still required a fixed four-column `1×4`
board.

That meant a correct presentation could fail the validator, or a model could
reintroduce the obsolete layout to satisfy the validator.

## Fix implemented

`RENDER_GATE_CHECKLIST.md` now validates the vertical priority view and checks
four-team/layer **coverage** rather than column layout.

The gate also validates the new exact-source AI check trace.

## Regression protection

`_audit/context_smoke_test.py` now checks that:

- `GOOGLE_SPRINT_PLANNING` is registered with dynamic tab discovery
- point 9 remains vertical
- the old four-column slide rule is absent
- the render gate uses the vertical point-9 validation
- the old fixed `1×4` validator wording is absent

A direct post-fix regression run against push `dev` passed all tested
conditions.

Direct fetch of active files confirmed no remaining four-column/1×4 point-9
rules in:

- `verification/RENDER_GATE_CHECKLIST.md`
- `design/DESIGN_AUTHORITY.md`
- `design/CARD_COMPONENT_STANDARD.md`

GitHub code-search results that still showed an older phrase were treated as
stale index results and were not used as authoritative evidence.

## Test verdict

**PASS**

The presentation flow now has a consistent rule chain for:

- verified current state
- source-backed/unknown sprint goals
- capacity handling
- shared risk/dependency/cross-layer/technical-debt reasoning
- vertical point-9 prioritization
- AI provenance
- exact-source AI check trace
- PDF default delivery

## Scope note

This run verifies routing, source behavior and content/validator consistency.

It does not render a PowerPoint/PDF artifact. Visual artifact rendering remains
a separate render-gate test.

---

**Status:** PASS
