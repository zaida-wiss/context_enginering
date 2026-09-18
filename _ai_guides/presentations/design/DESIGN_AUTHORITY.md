---
name: design-authority
description: MANDATORY — Presentation design authority and conflict ownership
metadata:
  type: process
  critical: true
  version: 2.1
---

# 🎨 DESIGN AUTHORITY

This document explains **who owns what** in the presentation system. It does not redefine the detailed rules owned by those files.

The purpose is to prevent contradictory instructions.

---

## 1. AUTHORITY HIERARCHY

Use this order when rules conflict:

1. `SYSTEM_CONTRACT.yaml` — execution sequence, gates, STOP/CONTINUE, delivery
2. `ACCESSIBILITY_NEURODIVERSITY.md` — WCAG/readability; absolute boundary
3. `VISUAL_DESIGN_MANDATORY.md` — global appearance and slide-level visual rules
4. `READABILITY_HARD_RULES.md` — type minima, line spacing and meeting-point readability
5. `CARD_COMPONENT_STANDARD.md` — all card-internal layout and typography
6. `PROVENANCE_AND_AI_LABELING.md` — fact/team/AI source identity
7. `PR_MERGE_REVIEW_IDENTITY.md` — merger and actual review identity
8. `LAYOUT_OVERFLOW_GUARD.md` — responsive fit and pagination
9. `SLIDE_DETAIL_SPEC.md` — slide purpose, fields, ordering and content requirements
10. `TEMPLATE_REFERENCE.html` — example only; never authoritative

`AUTHORITY_REGISTRY.yaml` determines which files are active. This document
explains conflict handling but does not activate a retired file.

`RENDER_GATE_CHECKLIST.md` validates compliance with the authorities above. It does not invent new design rules.

---

## 2. SINGLE-OWNER RULE

A rule category must have **one owning document**.

Lower documents may reference the owner but must not repeat different values or redefine the rule.

Examples:
- contrast/accessibility → `ACCESSIBILITY_NEURODIVERSITY.md`
- global palette → `VISUAL_DESIGN_MANDATORY.md`
- slide-title minimum → `VISUAL_DESIGN_MANDATORY.md`
- card title/explanation/assignee sizes → `CARD_COMPONENT_STANDARD.md`
- card-internal spacing → `CARD_COMPONENT_STANDARD.md`
- merge/review formatting → `CARD_COMPONENT_STANDARD.md`
- timestamp placement/style → `CARD_COMPONENT_STANDARD.md`
- AI/fact labels → `PROVENANCE_AND_AI_LABELING.md`
- which fields belong on slide ①D → `SLIDE_DETAIL_SPEC.md`
- evidence classification Level 1–6 → `ACTIVE_WORK_DETECTION_MODEL.md` as internal data logic

---

## 3. NO DUPLICATE POLICY VALUES

Do not copy exact numeric component rules into multiple authority files.

Good:
> `VISUAL_DESIGN_MANDATORY.md`: Card internals follow `CARD_COMPONENT_STANDARD.md`.

Bad:
> both files separately define different contribution font sizes or timestamp placement.

If a rule needs to change, update the owning authority first. Then update examples/checklists only to reflect it.

---

## 4. REFERENCE FILES NEVER WIN

`TEMPLATE_REFERENCE.html`, screenshots, older decks and reference slides may demonstrate the desired result, but they never override an authority file.

If an example conflicts with an authority:
1. follow the authority
2. update the example

Never modify an authority merely to preserve a stale example.

---

## 5. PROJECT-REPO BOUNDARY

`context_enginering` owns presentation instructions.

`chas-challenge-2026/avanza-team1` is a **project-data source only** for presentations.

Allowed project data includes:
- issues
- PRs
- commits
- branches
- project-board state
- verified technical decisions
- team ownership

Do not copy presentation design rules from the application UI or its CSS/design system.

---

## 6. CHANGE PROCEDURE

When a new presentation requirement is added:

1. identify the rule category
2. update its single owning authority
3. update `RENDER_GATE_CHECKLIST.md` if the rule needs mechanical validation
4. update `TEMPLATE_REFERENCE.html` only as an example
5. update README/architecture only if authority ownership itself changed
6. search for stale duplicate wording and remove or delegate it

Do not create `_V2`, `_NEW`, `_UPDATED` competing policy files. Git history is the version history.

---

## 7. CURRENT CARD OWNERSHIP

`CARD_COMPONENT_STANDARD.md` exclusively controls:
- pedagogical explanation directly under title
- explanation text size
- visual emphasis of verified assignee/developer
- minimum vertical spacing between semantic blocks
- merge/review name display
- handling of unknown merger/reviewer identity
- timestamp format, alignment and visual weight
- whether internal evidence levels are visible in cards

Other files must reference this authority instead of redefining those details.

---

## 8. CONFLICT RESPONSE

If two authoritative files appear to own the same rule category and disagree:

**STOP rendering and fix the documentation hierarchy first.**

Do not choose whichever rule is more convenient for the current slide.

Create a visible instruction-conflict receipt before stopping. It must contain:

```text
RULE CONFLICT
- Category: [layout / provenance / typography / content / data]
- Higher authority: [file + exact rule]
- Conflicting authority: [file + exact rule]
- Why they cannot both be followed: [plain-language explanation]
- Applied action: STOP before composition/rendering
- Required documentation fix: [owning file that must be changed]
```

Do not silently overwrite, merge, weaken or ignore either rule. A warning such
as `used higher rule` is insufficient when both files claim ownership.

If a lower-level example conflicts with a clearly delegated owner, record it as
`STALE EXAMPLE`, follow the owner, and update the example in the same change.

---

**Status:** PRODUCTION
**Version:** 2.0
**Last updated:** 2026-09-17
