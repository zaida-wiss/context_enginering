---
name: layout_overflow_guard
description: Hard render rules that prevent overlap, clipping, inaccessible compression and stale fixed layouts
metadata:
  type: process
  critical: true
  required_before: rendering
  version: 3.6
---

# 🚨 LAYOUT OVERFLOW GUARD — Responsive Cards, WCAG First

This is a HARD RENDER GATE.

Global visual authority: `VISUAL_DESIGN_MANDATORY.md`  
Readability hard rules: `READABILITY_HARD_RULES.md`  
Card internals: `CARD_COMPONENT_STANDARD.md`  
Accessibility boundary: `ACCESSIBILITY_NEURODIVERSITY.md`

---

## 1. ABSOLUTE RULE

Content must fit **without violating WCAG 2.2 AA or the readability hard rules**.

A slide is invalid if it solves space pressure by:
- shrinking a slide title below 36 pt
- clipping text
- overlapping text/cards
- hiding required content
- removing pedagogical/project-value microcopy
- using color alone for meaning
- lowering contrast below WCAG AA
- reducing text below its component/readability minimum
- compressing semantic spacing below the hard minimum
- automatic PowerPoint shrink-to-fit

When content is dense, responsive adaptation is required before pagination.

---

## 2. RESPONSIVE FIT SEQUENCE

For every card/slide, use this order:

1. Keep slide titles fixed at **36 pt or larger**; slide titles are never a fit variable.
2. Start normal/card text at preferred typography sizes.
3. Wrap text naturally.
4. Step down normal/card text deliberately only when required and only within the role-specific ranges in `CARD_COMPONENT_STANDARD.md` / `READABILITY_HARD_RULES.md`.
5. Use the 1.15 standard/minimum body line spacing and keep hard block gaps.
6. Recalculate every flex-row/container height from wrapped rendered text.
7. Measure and reserve the per-slide source footer before calculating available card height.
8. Let card height grow when space permits.
9. Reduce grid density so cards become wider/taller.
10. Move remaining cards to continuation slide(s).

A continuation slide is mandatory when content still does not fit at the defined accessible/readability minimums.

---

## 3. SHARED CARD/GRID RULE

The responsive card/grid system is the default composition language across the deck.

For ordinary work/information items:

> ONE ITEM = ONE CARD

Chronology, dependencies, risk and priority are expressed inside the shared
card/grid system through card order, group headings, symbols, short connectors
and provenance.

Allowed:
- 3×2, 2×2, 2×1 or 1×1 responsive grids;
- grouped cards under a shared heading;
- arrows/connectors between cards when they clarify dependencies;
- continuation slides when the common grid cannot remain readable.

Forbidden:
- replacing the shared grid with a mandatory full-slide timeline;
- replacing the shared grid with a mandatory full-slide dependency graph;
- multiple unrelated work items inside one ordinary card merely to save space.

Registered exception:
- meeting point 9 uses a mandatory vertical execution-group layout at slide level;
  cards remain the internal components.

The grid must adapt to content. Consistency never justifies smaller-than-allowed
text, clipping, weak contrast or excessive density.

---

## 4. GRID LIMITS — MAXIMUMS, NOT TARGETS

| Slide type | Default | Maximum |
|---|---|---:|
| meeting point 1 + any continuation pages | responsive, 3 × 2 when readable | 6 per physical slide |
| `②`–`⑤` | 2 × 2 | 4 |
| `⑥`–`⑧`, `⑩`–`⑫`, `⑭` | 2 × 2 | 4 |
| `⑨` | vertical execution groups; cards inside groups | responsive / paginate |
| `⑬` | 4 × 1 only when readable with required microcopy; otherwise 2 × 2 | 4 |
| `⑥` | responsive cards with optional connectors | 4 |

If cards are text-heavy, use fewer cards than the maximum.

Examples:
- 4 long cards may become 2 cards + 2 cards on continuation
- 6 merge cards may become 4 + 2 if the 3-column cards cannot remain readable
- next-step cards with pedagogical explanations must paginate rather than drop the explanations

---

## 5. CONTENT-DRIVEN CARD HEIGHT

Calculate required height from actual wrapped content.

Conceptually:

```text
required_card_height =
  top_padding
  + title_block_height
  + pedagogical_project_value_height
  + primary_detail_height
  + metadata/provenance_height
  + internal_gaps
  + bottom_padding
```

Do not assume equal text height merely because cards share a grid.

If equal outer card heights are used:
- align primary content from the top
- anchor timestamp/source metadata consistently near bottom when relevant
- let middle whitespace vary naturally
- do not distribute each row evenly from top to bottom

---

## 6. RESPONSIVE TYPOGRAPHY BOUNDARIES

Use `READABILITY_HARD_RULES.md` and `CARD_COMPONENT_STANDARD.md` exactly.

Current hard minima:
- slide title: **36 pt fixed minimum; never shrink for fit**
- section header: **22 pt**
- card title: **18 pt**
- owner/team: **13 pt**
- pedagogical/project-value explanation: **13 pt**
- operational metadata: **11 pt**
- timestamp/source/provenance: **11 pt**

Normal/supporting text should start around **15 pt** where the role/layout permits and reduce only if required.

These are minima, not targets.

**Never go below them.**

All text must also satisfy WCAG AA contrast and remain visually readable in the actual rendered artifact.

If a technically compliant minimum still looks too small/unreadable in the actual presentation context, increase the size and reduce density/paginate.

---

## 7. PADDING / SPACING BOUNDARIES

Use canonical values from `READABILITY_HARD_RULES.md` and the card standard.

Hard minimum rendered gaps:
- title → pedagogical explanation: **6 px minimum, 8 px preferred**
- explanation → assignee/developer: **14 px minimum**
- assignee/developer → operational metadata: **8 px**
- metadata row → separate metadata row: **6 px**
- operational metadata → timestamp/source area: **10 px**

Do not solve overflow by removing the visual separation required to distinguish lines/cards.

Hard rules:
- no text collision
- no overlapping text zones
- no negative spacing
- no line-height compression that causes crowded or colliding text
- every stacked text block is a measured child container in vertical flow
- each child's top edge is derived from the previous child's measured bottom edge plus the required gap
- bottom information zones reserve space before upper content is placed
- the physical slide's source footer reserves its full wrapped height before any card is placed
- no card, diagram or decoration may enter the source-footer bounding box
- card gap remains visually clear

---

## 8. SOURCE / PROVENANCE AND MICROCOPY MUST FIT

Provenance labels from `PROVENANCE_AND_AI_LABELING.md` and required pedagogical/project-value explanations are required content.

Do not remove:
- `📅 Schemafakta`
- `👥 ✅ Mötesprotokoll` / meeting source
- `🔎 AI-analys`
- `⭐ AI-förslag`
- `⚠ Källa behöver verifieras`
- project-value explanation on work/action cards

to save space.

If a card contains both facts and AI interpretation, each block remains separately labeled.

---

## 9. FORBIDDEN FIXES

Never:
- shrink slide titles below 36 pt
- automatic shrink-to-fit
- fonts below component/readability minimums
- text clipping
- text/card overlap
- required content outside its card
- contrast below WCAG AA
- color-only meaning
- hidden provenance
- omitted pedagogical/project-value explanation
- block spacing below the hard readability minimum
- full team-colored card outline instead of the canonical left accent
- fixed-height card that cuts wrapped text

---

## 10. ARTIFACT INSPECTION GATE

Inspect the actual rendered PPTX/PDF.

The deck FAILS if:

```text
wcag_aa_violation_count > 0
color_only_information_count > 0
text_overlap_count > 0
card_overlap_count > 0
text_outside_card_count > 0
text_clipping_count > 0
out_of_bounds_element_count > 0
font_below_component_minimum_count > 0
slide_title_below_36pt_count > 0
slide_title_shrunk_for_fit_count > 0
body_text_below_role_minimum_count > 0
card_block_spacing_violation_count > 0
next_step_card_missing_project_value_microcopy_count > 0
verified_dependency_not_reflected_in_plan_count > 0
missing_required_card_row_count > 0
uneven_row_spacing_caused_by_vertical_justification > 0
plain_row_work_item_count > 0
shared_card_grid_not_used_without_registered_exception_count > 0
```

---

## 11. REQUIRED FAILURE RESPONSE

When a slide fails:

1. identify the exact overflowing/colliding block
2. keep the slide title fixed at 36 pt+
3. verify the correct role-specific typography range
4. adapt normal/card text deliberately within that range only if required
5. adapt card geometry/grid density
6. paginate if still required
7. rerender
8. reinspect

Do not deliver until all hard-failure counts are zero.

---

**Status:** REQUIRED
**Version:** 3.6
**Last updated:** 2026-09-17
