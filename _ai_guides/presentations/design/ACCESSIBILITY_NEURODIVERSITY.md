---
name: accessibility_neurodiversity
description: MANDATORY — WCAG 2.2 AA and neurodiverse-friendly presentation boundaries
metadata:
  type: process
  critical: true
  for_ai: true
  version: 2.5
---

# 🧠 ACCESSIBILITY & NEURODIVERSITY — ABSOLUTE BOUNDARY

This file is the highest visual/accessibility authority for presentation rendering.

## 🚨 WCAG 2.2 AA IS NON-NEGOTIABLE

The presentation must **never** violate WCAG 2.2 AA to preserve a layout, card count, visual effect, brand choice or preferred font size.

If a design cannot remain compliant:

> Change the design. Never weaken accessibility.

### Binding contrast requirements

| Element | Minimum contrast |
|---|---:|
| Normal text | **4.5:1** |
| WCAG large text | **3:1** |
| Meaningful UI/card boundaries/components | **3:1** |
| Metadata / secondary normal text | **4.5:1** |

These ratios apply to the **actual rendered foreground/background combination**, including transparency/glass effects.

### Color as information

Color MUST NOT be the only way information is communicated.

Every meaningful color must be paired with a symbol, text label, shape or other non-color cue.

Examples:
- ✅ + text = done
- ◐ + text = in progress
- 🔴/✕ + text = blocked/critical
- ? + text = unknown / AI-derived where defined by provenance rules
- team color + team name/accent placement = team ownership

### Red

Red is reserved for blocker/critical/risk semantics.

Do NOT use red merely to indicate:
- fact
- source
- school schedule content
- decoration

---

## Shared-screen readability

WCAG contrast compliance alone is not enough for a meeting deck. Content must
also remain comfortably readable when screen-shared or projected.

Mandatory:
- prefer fewer items per slide over visually small text;
- ordinary explanatory/body text should target at least **20 pt**;
- metadata/supporting text should target at least **18 pt**;
- if those targets cannot be maintained, paginate before compressing;
- a dense infographic/dashboard that requires close inspection is not an
  acceptable substitute for readable meeting slides.

These are readability targets in addition to the component hard minima. Where
another authority requires a larger size, the larger requirement wins.

---

## 1. ACCESSIBILITY OVERRIDES LAYOUT DENSITY

If content cannot fit while staying accessible:

1. use the allowed responsive typography range
2. adapt card geometry
3. reduce number of cards on the slide
4. create continuation slide(s)

Never:
- clip text
- overlap text
- hide required content
- reduce contrast
- reduce below component minimums
- use automatic shrink-to-fit
- rely on color alone

---

## 2. TYPOGRAPHY OWNERSHIP

This file defines accessibility/readability boundaries, **not the exact size for every card role**.

Exact typography ranges are owned by:
- `VISUAL_DESIGN_MANDATORY.md` — global roles
- `CARD_COMPONENT_STANDARD.md` — card-internal roles

Therefore, stale fixed examples such as “all secondary text must be 18 pt” must not override the current component ranges.

### Accessibility rule for size

A font size is acceptable only when:
- it is at or above the relevant component minimum
- it remains clearly readable in the actual rendered/projected artifact
- it meets WCAG contrast requirements
- it does not require excessive crowding or line collision

If the minimum technically fits but is not comfortably readable in context, increase it and reduce density/paginate.

---

## 3. LINE SPACING & TEXT FLOW

Text must be easy to track visually.

Rules:
- use natural line spacing appropriate to the text role
- never compress line height until lines/glyphs visually collide
- wrapped lines stay together as one text block
- do not create irregular large gaps between related rows
- do not vertically justify card rows across the whole card height
- keep line lengths reasonably short where practical

Exact compact spacing values are owned by `CARD_COMPONENT_STANDARD.md`.

---

## 4. WHITESPACE & SEPARATION

Whitespace is functional, not decorative.

It should help users distinguish:
- one card from another
- title from supporting text
- facts from AI suggestions
- one team/category from another

Rules:
- cards must have visible separation
- related lines remain grouped
- unrelated items are not visually merged
- whitespace must not become so large that cards look broken or rows become hard to associate
- density is solved responsively, not by random spacing

---

## 5. PREDICTABILITY FOR NPF

The deck should remain visually predictable across slides.

Predictability includes reusing the same card component grammar across meeting
points. The default slide-level composition is responsive card/grid. Chronology,
dependencies and risk should normally be expressed through card order, grouping,
headings, symbols and connectors. A registered slide-level exception may use a
different composition when its owning authority requires it; meeting point 9's
vertical execution sequence is such an exception. The exception must preserve
the same NPF predictability, reading-order and WCAG boundaries.

Use consistently:
- same background system
- same card surface system
- same team-accent placement
- same status symbols
- same source/provenance symbols
- same hierarchy for title → body → metadata
- same timestamp treatment where relevant

Do not change visual grammar arbitrarily from slide to slide.

---

## 6. DYSLEXIA-FRIENDLY PRINCIPLES

Support scanning and line tracking through:
- clear hierarchy
- moderate line lengths
- consistent left alignment
- adequate contrast
- predictable spacing
- concise wording
- avoiding dense paragraphs
- using symbols together with text

Do not solve accessibility by simply making everything huge; use responsive hierarchy and card structure.

---

## 7. ADHD-FRIENDLY PRINCIPLES

Support focus through:
- one clear purpose per slide
- visible grouping
- limited number of cards per slide
- concise card text
- consistent visual hierarchy
- clear status/source cues
- continuation slides instead of overloaded slides
- a stable header/content/footer zone pattern
- a five-second scan in which meeting point, primary purpose and reading order are immediately apparent

Avoid visual clutter, excessive decoration or competing highlights.

---

## 8. AUTISM / SENSORY-PREDICTABILITY PRINCIPLES

Support predictability through:
- consistent layout patterns
- stable meanings for symbols/colors
- no unnecessary animation
- explicit source/status labels
- clear card boundaries
- no hidden or ambiguous semantics

A source/status should never require guessing from context alone.

---

## 9. STATUS SYMBOL SYSTEM

Canonical meanings:

```text
✅ = klart / verifierat where explicitly defined
◐  = pågår
✕ / 🔴 = blockerad / kritisk
?  = okänd / AI-derived only where provenance standard defines it
→  = beroende / riktning
```

The same symbol must keep the same meaning within its context throughout the deck.

For source provenance, follow `PROVENANCE_AND_AI_LABELING.md` exactly.

---

## 10. SOURCE / PROVENANCE ACCESSIBILITY

Facts and AI-derived suggestions must be distinguishable without color.

Use icon + text:
- `📅 Schemafakta`
- `👥 ✅ Mötesprotokoll`
- `⭐ AI-förslag`
- `🔎 AI-analys`
- `⚠ Källa behöver verifieras`

Mixed source blocks inside one card must each be labeled.

---

## 11. GLASS / TRANSPARENCY RULE

Glass-like surfaces are permitted only when accessibility is preserved.

The actual rendered background behind text must maintain required contrast.

If transparency reduces contrast:
- increase card opacity
- increase text contrast
- simplify the glass effect

Never preserve the effect at the expense of WCAG.

---

## 12. PRE-DELIVERY ACCESSIBILITY GATE

The rendered artifact must satisfy:

```text
wcag_aa_violation_count == 0
normal_text_contrast_failure_count == 0
large_text_contrast_failure_count == 0
meaningful_component_contrast_failure_count == 0
color_only_information_count == 0
text_clipping_count == 0
text_overlap_count == 0
font_below_component_minimum_count == 0
unreadable_projected_text_count == 0
competing_primary_focus_count == 0
unclear_reading_direction_count == 0
npf_visual_grammar_inconsistency_count == 0
card_grid_information_hierarchy_failure_count == 0
five_second_scan_failure_count == 0
slide_zone_predictability_failure_count == 0
```

Any non-zero count = FAIL.

Required response:
1. fix the accessibility problem
2. adapt typography/layout
3. paginate if needed
4. rerender
5. reinspect

No exception is allowed because “it looks better” or “otherwise there are too many slides”.

---

## CORE PRINCIPLE

**Accessibility is not one design preference among others. It is the boundary within which every other presentation rule operates.**

---

**Status:** PRODUCTION
**Version:** 2.4
**Last updated:** 2026-09-17
