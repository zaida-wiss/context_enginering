# Decision — Point 1 order and Point 9 layout

**Date:** 2026-09-18  
**Status:** Confirmed by user

## Conflict 1 — Meeting point 1 order

### User decision: 1A

Keep the reusable completed-work routing order:

1. merged to the selected project's registered primary integration branch
2. registered collection branches in project-defined order
3. team summaries

Do **not** create a separate WIP/unfinished-work slide inside meeting point 1.

Unfinished work belongs to later planning points, especially 3–5 and 9.

## Conflict 2 — Meeting point 9 layout

### User decision: 2B

Meeting point 9 is an explicit exception to the general shared card/grid layout.

It MUST use vertically stacked execution groups in this order:

1. `Prioritering först`
2. `Parallellt`
3. `Backlog — lägre prioritet`
4. `Förslag framåt — finns ännu inte / behöver korrigeras`

The groups must read top-to-bottom as one execution sequence.

A 2×2/four-quadrant arrangement for the four execution groups is not allowed.

Cards remain the component language **inside** each group, but the slide-level
composition for point 9 is vertical.

## Accessibility boundary

The vertical layout must still satisfy WCAG/NPF rules. If it becomes too dense:
- reduce cards per physical slide;
- continue to additional point-9 slides;
- preserve group order;
- never shrink below readability minima.

## Regression expectation

Validators must reject:
- old point-1 WIP slide/order;
- point-9 2×2/four-quadrant group layout;
- point-9 layouts that lose top-to-bottom priority order.
