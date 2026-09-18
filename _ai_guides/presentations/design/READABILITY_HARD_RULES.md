---
name: readability_hard_rules
description: MANDATORY — fixed slide-title size, dyslexia-friendly typography, larger text minima, spacing, pedagogical microcopy and dependency-aware ordering
metadata:
  type: design-specification
  critical: true
  required_before: composition
  version: 1.1
---

# READABILITY HARD RULES

This file is a hard authority for readability and meeting usability. It supplements the existing accessibility, visual, card and Monday-meeting specifications.

If a lower-level example conflicts with this file, this file wins for the rules below. WCAG 2.2 AA remains the absolute boundary.

## 1. SLIDE TITLES MUST NOT SHRINK

Slide titles / meeting-point headers use a normal fixed presentation size.

Hard rules:
- preferred and minimum slide-title size: **36 pt**
- slide titles are **never** a fit variable
- do not shrink a slide title because the slide is crowded
- do not use automatic shrink-to-fit on slide titles
- use a clear sans-serif typeface with open letterforms
- use **semibold/bold only as much as needed for hierarchy**; avoid extra-bold, black or visually heavy title weights
- the title must feel easy to scan rather than dense or block-like

If a title does not fit at 36 pt:
1. shorten the wording without losing meaning
2. widen/reposition the title zone
3. reduce slide content density
4. create a continuation slide

Never reduce the title below 36 pt to preserve content density.

## 2. DYSLEXIA-FRIENDLY TYPE & GLYPHS — HARD RULE

Typography must support fast scanning, letter recognition and stable line tracking.

Hard rules:
- use a familiar sans-serif family with clearly differentiated letterforms; prefer **Arial, Aptos, Atkinson Hyperlegible, Verdana or equivalent** when available
- body/supporting copy uses regular weight by default
- card titles and slide titles may use semibold/bold, but **must not look excessively heavy**
- avoid condensed fonts, decorative display fonts, all-caps paragraphs and long stretches of italic text
- avoid tightly packed uppercase labels when normal sentence case is clearer
- keep left alignment for normal text
- never reduce letter spacing to make text fit
- do not use stylized circled-number glyphs for meeting-point identity

### Meeting-point numbering and continuation hierarchy

Use **ordinary Arabic digits** so the meeting-point number is immediately recognizable.

The primary header contains only:
`✏️ [meeting-point number]. [meeting-point title]`

Canonical pattern:

```text
✏️ 1. Sprint in progress
c. Påbörjat, inte klart

✏️ 2. Nuläge och närmaste deadline
Kronologisk tidslinje över hela kursperioden
```

Continuation letters belong to the **smaller subtitle**, not to the main
meeting-point number/title.

A per-meeting-point page counter `(x/y)` sits at the far right of the primary
header row and uses visual-priority level 4.

Example:

```text
✏️ 1. Sprint in progress                                      (4/6)
c. Påbörjat, inte klart
```

Forbidden in rendered meeting headers:
- `①`, `②`, `⑨`, `⑬`, `⑭` and equivalent circled-number symbols
- a pen icon without the visible ordinary number
- attaching continuation letters to the meeting-point number, e.g. `1c.`
- replacing the meeting-point title with the physical-page topic

A lower-level slide/content specification may define semantic subsection IDs,
but rendered hierarchy follows the pattern above.

## 3. NORMAL TEXT STARTS LARGER

Normal presentation text should start larger than the minimum.

Use this fit principle:
1. start at the preferred size
2. reduce only if required to fit
3. reduce stepwise, never below the role minimum
4. if the minimum still does not fit, change geometry/density or paginate

Recommended normal body/supporting text start: **15 pt** when the role/layout permits.

For card-internal roles, these minima override older lower values:
- pedagogical/project-value explanation: **13 pt minimum**
- assignee/developer + team: **13 pt minimum**
- operational metadata: **11 pt minimum**
- timestamp/source microcopy: **11 pt minimum**
- card title remains **18 pt minimum**

A technically fitting smaller size is not a reason to use it. Use the largest comfortable size that fits the layout.

### Collision prevention takes priority over body-size preference

For body/supporting/card text, **overlap is never acceptable**.

When a text block is too large:
1. reduce that block stepwise from its preferred size
2. stop at the owning role minimum
3. recalculate block height and spacing after every reduction
4. if it still does not fit, shorten wording or paginate

It is better to use a slightly smaller **allowed** body size than to let two
text blocks overlap. This exception does not apply to the fixed 36 pt
meeting-point header, which must instead trigger reflow/pagination.

No renderer may preserve a preferred body size when that causes collision.

## 4. LINE HEIGHT & BLOCK SPACING MUST STAY OPEN

Text must never feel vertically compressed.

Hard rules:
- multiline body/supporting text uses **1.15 line spacing as the standard and minimum**; increase it only when the rendered font needs more clearance
- multiline card titles use at least **1.05 line spacing**
- wrapped lines within one semantic text block must not touch or visually collide
- separate semantic blocks must have an explicit gap; do not rely on accidental textbox placement
- do not place two independent textboxes on top of the same vertical band unless they are intentionally side-by-side and non-overlapping
- reducing line spacing never counts as collision prevention; block geometry must be recalculated from rendered text height

Minimum rendered gaps:
- title → pedagogical explanation: **6 px minimum**, **8 px preferred**
- explanation → assignee/developer: **14 px minimum**
- assignee/developer → operational metadata: **8 px minimum**
- separate metadata row → next metadata row: **6 px minimum**
- operational metadata → timestamp/source area: **10 px minimum**

If these gaps do not fit:
- increase card height
- reduce cards per slide
- shorten copy without removing meaning
- paginate

Do not solve fit by shrinking below these spacing minima.

## 5. PEDAGOGICAL MICROCOPY IS REQUIRED

Every action/work card that asks the team to do something must explain the project value, not only name the task.

Especially on `13. Nästa steg`, every card must answer directly under the title:
1. **Vad gäller detta?**
2. **Vad tillför det projektet / varför är det viktigt?**

This applies to:
- team-confirmed facts/actions
- `🔎 AI-analys`
- `⭐ AI-förslag`

Example:

```text
Fatta CI-beslut i #115
Avgör om lint, tester och build ska kontrolleras automatiskt i GitHub. Det minskar risken att fel kod mergas till develop.

⭐ AI-förslag
Ansvar: Hela teamet
```

If source evidence does not support the claimed project value, use neutral wording or mark the interpretation as AI-derived according to provenance rules. Never invent impact.

## 6. DEPENDENCIES MUST DRIVE ORDER

When verified dependencies exist, the presentation must make the suggested sequence visible.

The planning output should show, when evidence permits:
- **Först** — work that unlocks another item/team or removes a blocker
- **Parallellt** — independent work that can proceed safely
- **Därefter / vänta** — work dependent on unfinished prerequisites
- **Varför** — the blocker/dependency/deadline/core-flow reason

If the ordering is model-derived rather than already team-confirmed:
- reasoning uses `🔎 AI-analys`
- proposed sequence uses `⭐ AI-förslag — planeringsordning`

Example:

```text
⭐ AI-förslag — planeringsordning
1. Först: Lås API-kontraktet
   Varför: behövs för stabil Frontend/Backend-integration.
2. Parallellt: Verifiera JNA-minimiflödet
   Varför: låser Backend/Native-kopplingen.
3. Därefter: beroende integrationsarbete
   Varför: ska inte startas innan kontrakten/minimiflödet är verifierade.
```

The dependency graph and blocker slides must feed this ordering. Do not list a blocker without letting it influence the plan when it materially affects sequence.

## 7. RENDER / COMPOSITION FAILURE CONDITIONS

The deck fails when any of these are non-zero:

```text
slide_title_below_36pt_count > 0
slide_title_shrunk_for_fit_count > 0
body_text_below_role_minimum_count > 0
card_block_spacing_violation_count > 0
text_line_spacing_below_minimum_count > 0
meeting_point_uses_circled_number_count > 0
meeting_point_number_missing_count > 0
excessively_heavy_heading_weight_count > 0
next_step_card_missing_project_value_microcopy_count > 0
verified_dependency_not_reflected_in_plan_count > 0
```

Fix by changing wording, geometry, density or pagination — not by shrinking titles, using heavier type, or compressing text.

## CORE PRINCIPLE

**Readability and pedagogical clarity win over squeezing more information onto one slide.**

---

**Status:** PRODUCTION
**Version:** 1.1
**Last updated:** 2026-09-17
