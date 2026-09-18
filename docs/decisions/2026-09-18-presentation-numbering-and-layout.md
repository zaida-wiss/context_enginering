# Decision — Monday presentation numbering and layout

**Date:** 2026-09-18  
**Status:** Confirmed by user

## Conflict

Two active presentation directions conflicted:

1. meeting-point identity used either circled symbols (`①–⑭`) or ordinary Arabic numbers;
2. slide composition used either slide-type-specific structures (timeline/graph/vertical sequence) or a mostly uniform card/grid system.

Per `_ai_guides/AI_FRAMEWORK.md`, the conflict was surfaced to the user and no further autonomous choice is permitted.

## User decision

### D1 — Meeting-point numbering

Use **ordinary Arabic numbers** in rendered meeting-point headers:

```text
✏️ 1. Avklarat sedan förra mötet
✏️ 2. Nuläge och deadlines
...
✏️ 14. Frågor till PL
```

Circled number glyphs such as `①`, `②`, `⑨` may be used internally in documentation as identifiers, but must not be used as the rendered meeting-point identity.

### D2 — Layout system

Use a **consistent card/grid system as the primary visual structure across the deck**.

Implications:
- ordinary information is rendered as cards;
- timelines, dependency graphs and special vertical-priority layouts are not mandatory;
- chronology, dependencies, risk impact and priority are communicated inside the shared card/grid language through ordering, headings, symbols, connectors or grouped cards;
- use continuation slides rather than replacing the common visual grammar with a different full-slide layout.

## Accessibility / NPF boundary

This decision does not weaken WCAG 2.2 AA or NPF requirements.

The grid must adapt through:
- fewer cards per slide;
- wider/taller cards;
- continuation slides;
- stable reading order;
- predictable hierarchy;
- sufficient whitespace and contrast.

Uniformity must not be achieved by shrinking text, clipping content or increasing cognitive load.

## Regression expectation

Active authorities and render validators must reject:
- circled symbols as the rendered meeting-point header identity;
- mandatory special-layout requirements that contradict the shared card/grid standard;
- card grids that violate WCAG/NPF/readability rules.
