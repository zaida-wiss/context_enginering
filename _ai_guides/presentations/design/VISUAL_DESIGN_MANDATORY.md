---
name: visual_design_mandatory
description: MANDATORY — Canonical global slide layout and visual constants
metadata:
  type: process
  critical: true
  required_before: rendering
  version: 4.5
---

# 🎨 VISUAL DESIGN MANDATORY

This file is the **single authority for global presentation appearance**.

It owns:
- global palette
- slide background
- card surface family
- global slide-title and section-title roles
- maximum card density / grid behavior
- global visual consistency

It does **not** own card-internal spacing, card-internal type sizes, assignee emphasis, merge/review formatting or timestamp placement. Those belong exclusively to `CARD_COMPONENT_STANDARD.md`.

If a card-internal example in this file ever conflicts with `CARD_COMPONENT_STANDARD.md`, the card standard wins.

## Absolute rule: WCAG first

`ACCESSIBILITY_NEURODIVERSITY.md` and WCAG 2.2 AA are above all visual preferences.

At minimum:
- normal text contrast >= **4.5:1**
- WCAG large text contrast >= **3:1**
- information-bearing components >= **3:1**
- color is never the sole information carrier
- no clipping, overlap or hidden text

If a layout cannot satisfy these rules, change the layout or paginate.

---

## 1. GLOBAL VISUAL LANGUAGE

The deck uses:
- calm deep navy canvas
- soft dark glass-like cards
- rounded corners
- subtle depth/shadow
- low-glare surfaces
- clear hierarchy
- responsive cards
- cards as the primary information language, not tables/rows

One work/information item = one card unless a slide authority explicitly defines a diagram/group.

---

## 2. CANONICAL PALETTE

| Element | Hex | Role |
|---|---|---|
| Slide background | `#15182E` | calm deep navy canvas |
| Card surface | `#1E233B` | primary card surface |
| Alternate card surface | `#252A45` | optional subtle variation |
| Decorative card edge | `#33405D` | non-semantic separation |
| Meaningful neutral divider | `#7F8AA6` | structural meaning when needed |
| Main text | `#F7F8FC` | titles / primary content |
| Secondary text | `#D2D7E4` | supporting information |
| Metadata text | `#B0B8CC` | metadata |
| Quiet microcopy/timestamp | `#A2ABC0` | tertiary content, still WCAG-safe |

Palette rules:
- same background/card family across the entire deck
- no black/high-glare cards
- transparency must preserve contrast
- actual rendered colors must pass WCAG

---

## 3. CARD SURFACE — GLOBAL APPEARANCE ONLY

### Shape
- rounded corners, visually around **16–20 px**
- content-driven height
- subtle shadow/depth
- no fixed height that forces clipping

### Team accent and issue/PR identifiers
Team ownership is shown with a narrow left accent and, on issue/PR cards, the
same team color on the `#NUMBER`:
- Frontend `#2DD4BF`
- Backend `#FF4FA3`
- Native `#A855F7`
- Cross-team `#CBD5E1`
- Neutral `#94A3B8`

Do not use full team-colored outlines or team-colored card fills.
Color is supplementary: the visible team column/section or a text label must
also identify ownership. Every colored identifier must meet WCAG 2.2 AA.

All internal card rules are delegated to `CARD_COMPONENT_STANDARD.md`.

---

## 4. GLOBAL TYPOGRAPHY

This file owns only slide-level roles:
- slide title/header: **36 pt**, bold — this is both the preferred and minimum size
- section header: **22 pt minimum**, bold

### Slide-title hard rule

Slide titles are **never a responsive fit variable**.

Never shrink a slide title below 36 pt because content is crowded.
Never use automatic shrink-to-fit on slide titles.

If a title does not fit at 36 pt:
1. shorten the wording without losing meaning
2. widen or reposition the title zone
3. reduce slide content density
4. create a continuation slide

For every card-internal role, including title, pedagogical explanation, assignee/developer, operational metadata and timestamp, use **only** `CARD_COMPONENT_STANDARD.md` plus the hard readability minima in `READABILITY_HARD_RULES.md`.

Do not duplicate those numeric card-internal rules here.

---

## 5. CARD GRIDS — MAXIMUM DENSITY, NOT TARGET

### Meeting point 9: fixed four-team board

Every physical slide belonging to meeting point 9 uses exactly these four
vertical columns, in this order:

`Frontend | Backend | Native | Cross-team`

1. `Frontend`
2. `Backend`
3. `Native`
4. `Cross-team`

The columns classify ownership and impact. `Cross-team` is used only when work
genuinely spans or unlocks multiple teams; do not duplicate the same item in a
team column and the cross-team column.

Hard rules:
- exactly four team columns on every slide for point 9
- column headers remain visible and use at least the section-header minimum
- empty team columns remain visible and show a verified empty state
- support up to six cards per physical slide within meeting point 9
- card geometry may adapt to text length using 3×2, 2×3 or a balanced mixed arrangement within the team structure
- narrow columns must not force text below component minima
- if content is too tall, paginate to `9-2`, `9-3` and so on; do not add a fifth column
- status color may support meaning but never replaces status/source symbols
- point 9 renders each PR heading as `📌 #[PR_NUMBER]` with a grounded contribution line directly below
- point 9 visualizes issue order and dependency direction rather than describing them only in prose
- point 9 keeps `🔎 AI-analys` and `⭐ AI-förslag` visible at item level
- provenance remains visible inside every relevant item

### ①A–①C merge overview
- maximum 6 cards
- default may be 3×2 only when readable
- otherwise reduce density and continue on another slide

### ①D / ①E active/backlog
- maximum 4 cards per physical slide
- default 2×2 when content permits

### ①F decisions
- maximum 4 cards
- 2×2, 2×1 or 1×1 based on content

### ②–⑧, ⑩–⑫ and ⑭
- maximum 4 cards unless slide authority is stricter
- lower density when text length requires it

The four-team-board and six-card exception above governs meeting point 9, not
the ninth physical slide in the deck.

### ⑬ next steps
- 4×1 only when each card remains readable
- otherwise 2×2 or continuation

### ⑥A dependency diagram
- graph allowed
- maximum 3–4 chains per slide
- nodes remain card components

---

## 6. PROJECT-VALUE EXPLANATION

Issue/PR/Merge cards, dependency nodes and action/next-step cards must explain what the work contributes when source evidence supports it.

Content rule:
- short, grounded, plain Swedish
- directly connected to the title
- answer what it concerns and why it matters to the project
- no invented impact

**Placement, font size and spacing are owned by `CARD_COMPONENT_STANDARD.md` and `READABILITY_HARD_RULES.md`.**

Evidence grounding order:

Issue:
1. issue title/body/acceptance criteria
2. linked PR
3. verified branch/commits

PR:
1. PR title/body
2. changed files/diff
3. linked issue
4. commits

Merged PR:
1. merged PR title/body + changed files
2. linked issue
3. commits

---

## 7. PROVENANCE

Source identity is owned by `PROVENANCE_AND_AI_LABELING.md`.

Color may support source/status meaning but never replace icon + text where provenance must be visible.

---

## 8. STATUS VISUALS

Status must use symbol + text when status is shown.

Examples:
- ✅ klart/merged
- ◐ pågår
- ⏳ väntar/beroende
- 🔴 blockerad/kritisk
- ? oklar

Do not use color alone.

Evidence strength levels from `ACTIVE_WORK_DETECTION_MODEL.md` are **internal data classification**, not visible status labels.

---

## 9. RESPONSIVE FIT ORDER

When content is dense:
1. keep slide title fixed at 36 pt
2. keep required content
3. wrap naturally
4. start normal/card text at preferred sizes and reduce only when required
5. follow card-specific typography/spacing rules in `CARD_COMPONENT_STANDARD.md` and `READABILITY_HARD_RULES.md`
6. let cards grow
7. reduce grid density
8. paginate

Forbidden:
- shrinking slide titles
- clipping
- overlap
- missing content
- automatic shrink-to-fit
- typography below the owning component minimum
- contrast below WCAG AA
- removing required provenance
- removing pedagogical explanation to save space

---

## 10. TEXT BOX RULE

Ordinary slide titles, captions and footers:
- transparent fill
- no decorative border
- no unnecessary panel behind text

Visible card surfaces are reserved for actual information components.

---

## 11. RENDER GATE HANDOFF

Detailed mechanical checks live only in `verification/RENDER_GATE_CHECKLIST.md`.

This file requires globally:
- canonical palette consistent
- card system consistent
- WCAG AA pass
- no high-glare surfaces
- no full team outlines
- slide titles remain at 36 pt or larger
- slide titles are never shrunk for fit
- slide-level typography minimums respected

Do not duplicate the full render-gate checklist here.

---

## CORE PRINCIPLE

**Calm navy canvas + soft cards + clear hierarchy + responsive geometry + accessible rendering.**

Card internals are governed by `CARD_COMPONENT_STANDARD.md`; global design must not redefine them.

---

**Status:** PRODUCTION
**Version:** 4.4
**Last updated:** 2026-09-17
