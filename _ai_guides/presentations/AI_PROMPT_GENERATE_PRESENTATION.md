---
name: ai_prompt_generate_presentation
description: RETIRED — historical generation prompt; do not use in production
metadata:
  type: retired_reference
  status: retired
  audience: ChatGPT, Claude, Gemini — any AI asked to generate presentation
  version: 3.0
---

# 🤖 AI PROMPT — Generate Avanza Team 1 Presentation

> **RETIRED. DO NOT USE FOR PRODUCTION.** The active execution path is
> `MANDATORY_READING_ORDER.md` + `AUTHORITY_REGISTRY.yaml`. Content below may
> contain old numbering or layout examples and has no authority.

Generate a Monday Meeting presentation for Avanza Team 1 using the deterministic pipeline in this context repo.

This is not a loose template. Follow the authority hierarchy and live data requirements exactly.

---

## STEP 1 — READ THE AUTHORITIES

Read these files completely before building anything:

1. `MANDATORY_READING_ORDER.md`
2. `SYSTEM_CONTRACT.yaml`
3. `ACCESSIBILITY_NEURODIVERSITY.md`
4. `VISUAL_DESIGN_MANDATORY.md`
5. `SLIDE_DETAIL_SPEC.md`
6. `LAYOUT_OVERFLOW_GUARD.md`
7. `RENDER_GATE_CHECKLIST.md`
8. `DATA_ACQUISITION_CONTRACT.yaml`
9. `ACTIVE_WORK_DETECTION_MODEL.md`
10. `TEAM_ROSTER.md`

`TEMPLATE_REFERENCE.html` is reference only and never overrides an authority file.

---

## STEP 2 — VERIFY REPOSITORY STATE

Before data acquisition:

```text
REPOSITORY STATE VERIFICATION
Requested branch: [branch from user URL/request]
Remote HEAD: [latest SHA]
Instruction files loaded from SHA: [SHA]
MATCH: YES/NO
```

If MATCH is NO: STOP.

Do not use stale snapshots when live GitHub data is required.

---

## STEP 3 — DATA ACQUISITION

Follow `DATA_ACQUISITION_CONTRACT.yaml` and `EXTERNAL_SOURCES.yaml` exactly.

Required datasets include:

- Team roster
- PRs merged to `develop`
- Collection-branch merges
- Open PRs
- Open assigned issues
- Branches/recent commits needed for active-work evidence
- Actual reviews
- Actual merge identity

Never guess missing GitHub data.

### Attribution

**Developed by**:
1. actual commit authors
2. issue assignee as fallback
3. PR author only as weak fallback

**Reviewed by**:
- actual GitHub review activity
- distinguish review states when relevant

**Merged by**:
- actual `merged_by.login`

Do not write generic placeholders such as `GitHub-merge` when the identity exists in GitHub.

---

## STEP 4 — DATA AUDIT

Before slide generation, run the `DATA_AUDIT` required by `RENDER_GATE_CHECKLIST.md`.

Validate:

```text
COUNT
SET
UNIQUENESS
TEAM COVERAGE
ACTIVE ISSUE COMPLETENESS
```

All seven team members must be accounted for.

When a member has no verified active PR/issue/review, use:

`[Name] — Ny issue eller tillgänglig för hjälp i [teamet]`

Review work counts as work.

---

## STEP 5 — BUILD WITH THE MODERN CARD SYSTEM

`VISUAL_DESIGN_MANDATORY.md` is the visual authority.

### Core rule

> ONE ITEM = ONE CARD

Do not render work items as plain text rows, table rows, horizontal bands, or line-only lists.

### Canonical layouts

- `①A–①C`: 3 × 2 modern cards, max 6 per physical slide
- `①D`: 2 × 2 modern cards, max 4
- `①E`: 2 × 2 modern cards, max 4
- `①F`: 2 × 2 or 2 × 1 cards, max 4
- `②–⑤`: modern cards, normally 2 × 2, max 4
- `⑥`: modern cards; `⑥A` may use dependency diagram nodes
- `⑦–⑫`: modern cards, normally 2 × 2, max 4
- `⑬`: 4 × 1 or 2 × 2 cards, max 4
- `⑭`: grouped modern cards, continuation if needed

### Modern card style

- Slide background: `#0F1830`
- Card surface: `#18233D`
- Rounded corners: 16–20 px
- Padding: 18–22 px
- Gap between cards: 20 px minimum
- Subtle border/accent
- Subtle box shadow/depth
- Team color only as accent/border, not full-card fill

Canonical shadow feeling:

```css
box-shadow:
  0 10px 30px rgba(0,0,0,.22),
  0 2px 8px rgba(0,0,0,.16);
```

### Typography minimums

- Slide title: 32 pt
- Section header: 22 pt
- Card title/main content: 20 pt
- Secondary meeting information: 18 pt
- Metadata/footer: 12–14 pt only

Never shrink text below minimums.

---

## STEP 6 — PAGINATION / OVERFLOW

When content does not fit:

1. Let the card grow
2. Use fewer cards on that physical slide
3. Create continuation slide(s)

Examples:

```text
①D-2
①E-2
③-2
⑭-2
```

Never solve overflow by:

- shrinking font
- reducing padding
- overlapping text
- clipping text
- replacing cards with rows
- hiding required branch/status/owner metadata

More slides are preferred over compressed slides.

---

## STEP 7 — CONTENT RULES

Follow `SLIDE_DETAIL_SPEC.md` for WHAT each slide contains.

If `SLIDE_DETAIL_SPEC.md` contains legacy visual wording such as `rows`, `stacked`, `columns`, `table`, or old font sizes, that wording does NOT control rendering.

For visual choices always follow:

1. `ACCESSIBILITY_NEURODIVERSITY.md`
2. `VISUAL_DESIGN_MANDATORY.md`
3. `LAYOUT_OVERFLOW_GUARD.md`

`SLIDE_DETAIL_SPEC.md` remains the content authority only.

---

## STEP 8 — RENDER GATE

Before delivery, run `RENDER_GATE_CHECKLIST.md` against the actual rendered PPTX/PDF.

The artifact must satisfy:

```text
text_overlap_count == 0
card_overlap_count == 0
text_outside_card_count == 0
text_clipping_count == 0
out_of_bounds_element_count == 0
font_below_minimum_count == 0
plain_row_work_item_count == 0
```

Also verify:

- ①D and ①E are card grids, not row lists
- card shadow/depth is subtle and consistent
- every card has enough padding
- team accents are correct
- no data item disappeared because of layout pressure
- continuation slides exist whenever necessary

---

## STEP 9 — FINAL QUALITY CHECK

Page through every rendered slide.

Check:

- no overlap
- no clipping
- no text below minimum size
- no row/list work-item layouts
- modern soft-card feel throughout
- all required data accounted for
- actual developers/reviewers/mergers shown where required
- all seven team members represented
- no duplicated PR/work item

If anything fails: fix → rerender → reinspect.

---

## DO NOT

- Do not use cached or guessed GitHub data
- Do not use PR author as automatic `Developed by`
- Do not use requested reviewer as proof of actual review
- Do not write `inaktiv` / `ingen aktivitet`
- Do not use plain text rows for issue/PR items
- Do not use table rows as the main layout
- Do not shrink text to keep a slide count low
- Do not force more than 4 cards onto ①D/①E
- Do not clip text
- Do not reduce card padding below the minimum
- Do not ignore render-gate failures

---

## SUCCESS CRITERIA

```text
LIVE_DATA == PASS
DATA_AUDIT == PASS
CONTENT_COMPLETENESS == PASS
MODERN_CARD_SYSTEM == PASS
TYPOGRAPHY == PASS
OVERFLOW == PASS
ARTIFACT_COLLISION_CHECK == PASS
```

The desired result is:

**dark navy canvas + modern rounded cards + subtle shadow + large readable text + generous whitespace + continuation slides instead of compression.**

---

**Last updated:** 2026-09-17
**Version:** 3.0
