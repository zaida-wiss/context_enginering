---
name: visual_design_mandatory
description: MANDATORY — Canonical global slide layout and visual constants
metadata:
  type: process
  critical: true
  required_before: rendering
  version: 4.0
---

# 🎨 VISUAL DESIGN MANDATORY

This is the authoritative global visual specification for Monday Meeting presentations.

## Absolute rule: WCAG first

All design decisions MUST comply with `ACCESSIBILITY_NEURODIVERSITY.md` and WCAG 2.2 AA.

No visual preference, card density, slide count, or desire to preserve a grid may weaken accessibility.

At minimum:
- normal text contrast: **4.5:1**
- WCAG large text: **3:1**
- information-bearing borders/components: **3:1**
- color is never the sole information carrier
- text must not clip, overlap or disappear

If a layout cannot satisfy these rules, change the layout or paginate.

---

## 1. GLOBAL VISUAL LANGUAGE

The deck uses:

- dark navy canvas
- modern glass-like dark cards
- rounded corners
- subtle depth/shadow
- clear hierarchy
- compact but readable metadata
- generous enough whitespace to separate information
- responsive cards that adapt to content

**Cards are the primary visual language. Rows/tables are not.**

One work/information item = one card unless the slide-specific specification explicitly defines a diagram/group.

---

## 2. THEME

| Element | Hex |
|---|---|
| Slide background | `#0F1830` |
| Card surface | `#18233D` |
| Alternate card surface | `#202C47` |
| Neutral divider/edge | `#334155` |
| Main text | `#FFFFFF` |
| Secondary text | `#CBD5E1` |
| Metadata text | `#94A3B8` |
| Quiet microcopy/timestamp | `#8290A7` |

All text colors must be checked against their actual rendered background.

`#8290A7` is allowed only where it still meets WCAG AA against the actual dark surface. If renderer/transparency changes the effective contrast, increase contrast rather than preserving the exact hex value.

Do not use white/light slide backgrounds in this deck.

---

## 3. CARD SURFACE

### Shape
- corner radius: **16–20 px**
- content-driven height
- no fixed text-box height that causes clipping
- subtle shadow/depth

### Glass effect
The renderer may use translucency/soft depth, but never at the expense of text contrast.

Suggested visual equivalent:

```css
box-shadow:
  0 10px 30px rgba(0,0,0,.22),
  0 2px 8px rgba(0,0,0,.16);
```

### Team accent
Team ownership is shown ONLY with a narrow left accent line.

- Frontend: `#2DD4BF`
- Backend: `#FF4FA3`
- Native: `#A855F7`
- Cross-team: `#CBD5E1`
- Neutral/other: `#94A3B8`

Rules:
- team color must NOT outline the entire card
- team color must NOT fill the card
- accent should be approximately **4–6 px** visually
- team color never replaces status/source symbols and text

---

## 4. INTERNAL SPACING

Canonical card rhythm:

- outer card padding: **18–22 px** preferred
- title → supporting text: **4–6 px**
- supporting text → primary detail: **8–10 px**
- primary detail → metadata: **5–7 px**
- gap between separate cards: **20 px minimum**

Do not vertically justify all text rows across the full card height.

When cards have equal outer height:
- top-align main content
- bottom-anchor timestamp/source metadata when appropriate
- allow middle whitespace to absorb small differences

---

## 5. RESPONSIVE TYPOGRAPHY

This file defines global roles; `CARD_COMPONENT_STANDARD.md` defines exact card-internal ranges.

### Global fixed roles
- slide title/header: **32 pt minimum**, bold
- section header: **22 pt minimum**, bold

### Card roles
Use `CARD_COMPONENT_STANDARD.md`:
- card title: preferred 18–20 pt, minimum 18 pt
- owner/team: preferred 13–14 pt, minimum 12 pt
- contribution/supporting text: preferred 11–12 pt, minimum 11 pt
- operational metadata: preferred 11–12 pt, minimum 10 pt
- timestamp/source/provenance: preferred 10–11 pt, minimum 10 pt

The renderer may deliberately step down within these ranges on dense slides.

This is **not** shrink-to-fit. Sizes are selected intentionally based on content density.

If content does not fit at the permitted minimum size:
- change card geometry
- reduce cards per slide
- create continuation slide

Never reduce below the component minimum merely to preserve a grid.

---

## 6. LINE HEIGHT AND WRAPPING

- slide/section headings: natural readable spacing
- card title/body: approximately **1.25–1.45** depending on font/rendering
- compact metadata: approximately **1.2–1.35**
- never reduce line height until glyphs/lines visually collide
- text wraps naturally inside card boundaries
- prefer shorter source-grounded wording over cramped lines

---

## 7. CANONICAL CARD GRIDS

These are maximum densities, not targets.

### ①A–①C merge overview
- default: **3 × 2**
- max 6 cards
- if content is dense: use 2 × 2 or fewer and continue

### ①D / ①E active/backlog
- default: **2 × 2**
- max 4 cards

### ①F decisions
- 2 × 2, 2 × 1, or 1 × 1 depending on content
- max 4

### ②–⑫ and ⑭
- default: 2 × 2 for compact content
- switch to 2 × 1 or 1 × 1 for longer content
- max 4 cards unless slide-specific rules are stricter

### ⑬ next steps
- 4 × 1 only when each card remains readable
- otherwise 2 × 2 / fewer cards + continuation

### ⑥A dependency diagram
- graph allowed
- each node still uses card styling
- max 3–4 chains per slide

---

## 8. CONTRIBUTION MICROCOPY

Issue/PR/Merge cards must explain the code/product contribution directly below the title.

Rules:
- one short grounded sentence
- plain Swedish
- normally 8–14 words
- do not invent impact
- if insufficient evidence: `Bidrag till koden behöver verifieras.`
- use card-standard supporting-text size and WCAG-compliant contrast

Evidence order:

Issue:
1. title/body/acceptance criteria
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

## 9. TIMESTAMPS AND MERGE METADATA

Follow `CARD_COMPONENT_STANDARD.md`.

Merge metadata labels:

```text
Merged: [name] | Review: [name/status]
```

Do not use:
- `Merged by:`
- `Reviewed by:`

Timestamp is normally bottom-left and may use two lines:

```text
14 sep
10:16
```

Do not prefix the date with `Merged`, `Mergad`, or `Senaste commit` when the semantic meaning is already established by the card.

---

## 10. PROVENANCE / FACT VS AI

Source identity follows `PROVENANCE_AND_AI_LABELING.md`.

Canonical labels include:
- `📅 Schemafakta`
- `✅ Mötesprotokoll`
- `? AI-förslag`
- `? AI-analys`
- `⚠ Källa behöver verifieras`

Never use color alone to distinguish fact from AI.
Never use red to mean `fact`; red remains blocker/critical status.

Mixed cards must label each fact/AI block separately.

---

## 11. STATUS COLORS

Status always uses symbol + text.

| Status | Symbol | Meaning |
|---|---|---|
| Done/Merged | ✅ | klart |
| In progress | ◐ | pågår |
| Blocked/Critical | 🔴 / ✕ | blockerad/kritisk |
| Unknown | ? | oklar/ej verifierad |

Color supports the symbol/text but never replaces them.

---

## 12. TEXT BOX RULE

Ordinary text boxes such as titles, captions and footers:
- transparent fill
- no decorative border
- no unnecessary panel behind text

Visible card surfaces are reserved for actual information components.

---

## 13. RESPONSIVE FIT ORDER

When content is dense:

1. keep all required content
2. wrap naturally
3. move within the permitted typography range toward the minimum
4. use canonical compact spacing
5. let cards grow
6. reduce grid density / increase card width
7. paginate

Forbidden:
- clipping
- overlap
- missing content
- automatic shrink-to-fit
- fonts below allowed minima
- contrast below WCAG AA
- color-only meaning
- removing provenance labels

---

## 14. RENDER GATE

Before delivery, the rendered artifact must satisfy:

```text
wcag_aa_violation_count == 0
color_only_information_count == 0
text_overlap_count == 0
card_overlap_count == 0
text_outside_card_count == 0
text_clipping_count == 0
out_of_bounds_element_count == 0
font_below_component_minimum_count == 0
plain_row_work_item_count == 0
missing_contribution_microcopy_count == 0
uneven_row_spacing_caused_by_vertical_justification == 0
full_team_outline_count == 0
```

If any count is non-zero:
1. do not deliver
2. fix the slide
3. adapt typography/layout within accessible limits
4. add continuation slide(s) if needed
5. rerender
6. inspect again

---

## CORE PRINCIPLE

**WCAG-first dark dashboard + coherent glass cards + responsive deliberate typography + clear provenance + no clipping.**

Cards adapt to content; accessibility never adapts downward to the layout.

---

**Status:** PRODUCTION
**Version:** 4.0
**Last updated:** 2026-09-17
