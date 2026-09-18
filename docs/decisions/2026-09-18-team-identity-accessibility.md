# Decision — Team identity must not rely on color alone

**Date:** 2026-09-18  
**Status:** Confirmed by user

## Conflict

Active presentation authorities conflicted:

- WCAG/NPF authorities required that color never be the sole carrier of team meaning.
- `CARD_COMPONENT_STANDARD.md` contained an example stating that team was shown by left-border color and not by text.

## User decision

Choose **A — WCAG/NPF-strong team identity**.

### Binding rule

Team ownership must never be communicated by color alone.

Every card must include a non-color team cue when team ownership is relevant:
- visible team text, e.g. `Frontend`, `Backend`, `Native/System`, `Cross-team`; or
- an equivalent explicit non-color label defined by the active design authorities.

Team accent color remains supplementary.

If the slide heading already identifies the team, the card may still use a compact
team label when needed for accessibility and mixed-content clarity. Do not rely
on the heading + color alone when the card could be copied, moved, exported or
read out of context.

## Accessibility rationale

This follows the active WCAG/NPF rule that meaningful color must be paired with
text/symbol/shape and must not be the sole information carrier.

## Regression expectation

Validators must reject any card where team ownership is relevant but available
only through color.
