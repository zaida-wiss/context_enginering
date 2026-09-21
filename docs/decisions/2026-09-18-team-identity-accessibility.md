# Decision — Team identity must not rely on color alone

**Date:** 2026-09-18  
**Status:** Confirmed by user

## Conflict

Active presentation authorities conflicted:

- WCAG/NPF authorities required that color never be the sole carrier of team meaning.
- `CARD_COMPONENT_STANDARD.md` contained an example stating that team was shown by left-border color and not by text.

## User decision

Choose **C — context-aware non-color team identity**.

### Binding rule

Team ownership must never be communicated by color alone.

Team ownership must never rely on color alone **across the complete slide context**.

Rules:
- On a dedicated team slide whose header explicitly names the team, e.g.
  `{MEETING_POINT}. {TEAM_NAME}`, the header provides the non-color team meaning. Individual cards
  do not repeat the team name; the left team accent color is sufficient as the
  supplementary card-level cue.
- On mixed-team slides, each card must include an explicit non-color team cue,
  e.g. `{TEAM_NAME}` or a registered project-owned team symbol, in addition
  to the team accent color.
- If a card is exported or reused outside its original team slide, it must regain
  an explicit team label because the surrounding header context is no longer present.

Team accent color remains supplementary and never carries ownership alone when
the slide itself does not already name the team.

## Accessibility rationale

This follows the active WCAG/NPF rule that meaningful color must be paired with
text/symbol/shape and must not be the sole information carrier.

## Regression expectation

Validators must reject:
- mixed-team cards where ownership is available only through color;
- dedicated team slides whose header does not explicitly name the team while card
  ownership is shown only through color.
