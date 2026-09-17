---
name: card_component_standard
description: MANDATORY — Canonical internal layout for all presentation cards
metadata:
  type: design-specification
  critical: true
  required_before: rendering
  version: 1.4
---

# 🎴 CARD COMPONENT STANDARD

This file is the **single authority for the internal layout of presentation cards**.

It owns:
- card-internal typography
- order of card content
- spacing between card text blocks
- assignee/developer emphasis
- merge/review metadata presentation
- branch/status metadata presentation
- visible timestamps
- card-internal responsive behavior

It does **not** own global slide colors, slide structure, data acquisition, evidence classification or slide selection.

If another document contains an example that conflicts with this file, **this file wins for card internals**, except that `READABILITY_HARD_RULES.md` may define stricter minima.

## Absolute accessibility boundary

`ACCESSIBILITY_NEURODIVERSITY.md` and WCAG 2.2 AA remain an absolute hard boundary.

Every card must satisfy at minimum:
- normal text contrast: **4.5:1**
- large text contrast: **3:1** where WCAG large-text definition applies
- information-bearing component/accent contrast: **3:1**
- color is never the sole information carrier
- no clipping, overlap, hidden text or illegible compression

If content cannot fit while remaining readable, reduce card density or paginate.

---

# 1. CARD SURFACE

Card surfaces follow the global palette in `VISUAL_DESIGN_MANDATORY.md`.

Team color appears only as a narrow vertical accent on the left. Team color must not outline or fill the whole card.

Canonical team accents:
- Frontend: `#2DD4BF`
- Backend: `#FF4FA3`
- Native: `#A855F7`
- Cross-team: `#CBD5E1`
- Neutral: `#94A3B8`

Recommended left accent width: visually equivalent to **4–6 px**.

---

# 2. REQUIRED CONTENT ORDER

For Issue/PR/Merge/action cards, use this visual order:

1. **Title**
2. **Pedagogical contribution / project-value line** — directly under the title
3. **Assignee/developer + team** when relevant
4. **Operational metadata** — PR/branch/status or merge/review
5. **Timestamp** — when relevant

Do not insert decorative or provenance rows between title and pedagogical explanation.

The explanation and title form one semantic group. Other rows are separate blocks and must have visible spacing between them.

For action and next-step cards, the pedagogical line must answer:
- what the action concerns
- what it contributes to the project / why it matters

---

# 3. RESPONSIVE TYPOGRAPHY — START LARGE, NEVER AUTO-SHRINK

General principle:
1. start at the preferred size
2. reduce only when required to fit
3. reduce stepwise, never below the role minimum
4. if minimum still does not fit, change geometry/density or paginate

Do not choose a smaller size merely because it technically fits.

## Card title
- preferred: **19–20 pt**
- minimum: **18 pt**
- bold
- main text color from global palette

## Pedagogical contribution / project-value line
This answers: **Vad gäller detta och vad löser/tillför detta i projektet?**

- preferred: **14–15 pt**
- minimum: **13 pt**
- regular
- readable secondary text color
- normally 1–3 visual lines when needed for pedagogical clarity
- placed immediately under the title
- no extra paragraph gap between title and explanation

## Assignee/developer + team
Examples:
- `Tomac · Frontend`
- `Rasha · Backend`
- `Henrik · Native`

Rules:
- preferred: **14–15 pt**
- minimum: **13 pt**
- semibold/bold
- **the verified assignee/developer name uses the same primary text color as the card title**
- the team name may use secondary text color
- this row must be visually easier to find than branch/status metadata
- do not infer a developer from commit authorship when issue-assignee evidence says otherwise; use the project attribution rules

## Operational metadata
Examples:
- `Merged: Zaida | Review: Björn`
- `Merged: Zaida | Review:`
- `Branch: frontend/#83-save-allocation`
- `Öppen PR · väntar på review`

Style:
- preferred: **12–13 pt**
- minimum: **11 pt**
- regular
- muted but WCAG-AA-safe color

### Merge/review identity rule
Only show a person's name when the identity is verified by source evidence.

Before rendering a merged PR card, the generator MUST perform the dedicated merger + submitted-review lookup in `data/PR_MERGE_REVIEW_IDENTITY.md`.

Canonical format:

`Merged: [verified name or blank] | Review: [verified approving reviewer(s) or blank]`

Examples:
- `Merged: Björn | Review: Zaida`
- `Merged: Björn | Review: Zaida, Rasha`
- `Merged: Björn | Review:`
- `Merged: | Review: Zaida`

`requested_reviewers` must never populate the visible `Review:` field for a merged PR. Only actual submitted `APPROVED` reviews count for that field.

Never render uncertainty commentary in this row.

Forbidden visible wording includes:
- `ej verifierat`
- `verifierad`
- `verifierat via merge-commit`
- `faktisk review behöver verifieras`
- `Merged by:`
- `Reviewed by:`

Verification state belongs in the internal data/audit layer, not in the meeting card.

## Timestamp / source microcopy
- preferred: **11–12 pt**
- minimum: **11 pt**
- quiet WCAG-AA-safe text color
- timestamp should be visually subordinate to all work content

Never go below 11 pt.

---

# 4. TIMESTAMP STANDARD

When a timestamp is useful, show it as **one compact line aligned to the lower-right of the card**.

Canonical example:

```text
14 sep · 10:16
```

Rules:
- one line only
- bottom/right aligned where card geometry permits
- use the quietest WCAG-AA-safe text color in the global palette
- no prefix such as `Merged`, `Mergad`, `Senaste commit` or evidence label
- do not place timestamp so close to other metadata that the rows visually merge

For active work, use the relevant verified activity timestamp only when it helps the meeting.

---

# 5. CANONICAL MERGED-PR CARD

```text
#80 · Drift från live target
Beräknar drift från aktuell målallokering i stället för mock-flagga.

Tomac · Frontend
Merged: Zaida | Review: Björn

                         14 sep · 10:16
```

Rendering rules:
- pedagogical explanation sits directly under the title
- assignee/developer is clearly emphasized
- only verified merger and actual approving reviewer names appear
- dedicated merger/review lookup is mandatory before an empty field is accepted
- timestamp is a discreet one-line element at lower right

---

# 6. CANONICAL ACTIVE ISSUE / PR CARD

```text
#88 · Kritiska MVP-tester
Testar login, målallokering och drift för kritiska MVP-flöden.

Zaida · Frontend
PR #114 · Build/frontend/#88-critical-interactions

                         17 sep · 09:19
```

Evidence level is **not rendered as text on the card**. Do not show `GitHub · nivå 1`, `nivå 2`, etc.

The evidence hierarchy remains an internal classification used to decide whether/how an item is shown.

If a status symbol is already useful for the meeting (for example waiting/blocked), it may be used together with text. Do not add a separate evidence-level symbol merely to expose the internal classification.

---

# 7. CANONICAL DEPENDENCY / NEXT-STEP NODE

Dependency and next-step nodes use the same internal hierarchy:

```text
API-kontrakt
Definierar endpoints + payload så Frontend och Backend kan integrera stabilt.

🔴 Behöver låsas
```

Hard rules:
- title first
- pedagogical/project-value line immediately below title
- status/dependency is a separate block with minimum spacing
- arrows/connectors stay outside cards
- if evidence is insufficient, use the approved uncertainty wording from the content/data authority
- on `⑬ Nästa steg`, every card must explain both what the action concerns and why it matters to the project

---

# 8. MINIMUM VERTICAL SPACING — HARD RULE

Separate semantic blocks must never visually touch.

Use these **minimum rendered gaps**:
- title → pedagogical explanation: **4 px minimum, 6 px preferred**
- explanation → assignee/developer: **12 px minimum**
- assignee/developer → operational metadata: **8 px minimum**
- one operational metadata row → next separate metadata row: **6 px minimum**
- operational metadata → bottom timestamp/source area: **10 px minimum** unless flexible whitespace is larger

Wrapped lines inside the same text block use natural line-height and no artificial paragraph gap.

These values are minimums, not targets for compression.

If a card cannot fit while respecting them:
1. let the card grow
2. reduce grid density
3. paginate

Never solve fit by collapsing these gaps below minimum, overlapping rows, shrinking text below role minimums, or removing the pedagogical explanation.

Do not vertically justify all rows across the card height.

---

# 9. RESPONSIVE CARD GEOMETRY

Allowed adaptations:
- natural text wrapping
- card grows in height
- wider cards through a lower-density grid
- 2×2 → 2×1 → 1×1 when needed
- continuation slide

Fit order:
1. preferred typography
2. typography reduction only when required and only within explicit role ranges
3. canonical spacing, never below hard minimums
4. adapt card/grid dimensions
5. paginate

Never:
- clip or overlap text
- omit required rows
- omit pedagogical/project-value explanation
- expose internal evidence-level labels to save explanation space
- reduce below component minimums
- reduce contrast below WCAG AA
- use automatic shrink-to-fit

---

# 10. RENDER CHECKS

Before delivery verify:

```text
wcag_aa_violation_count == 0
color_only_information_count == 0
team_color_left_accent_only == true
full_team_outline_count == 0
required_card_rows_missing == 0
font_below_component_minimum_count == 0
text_clipping_count == 0
text_overlap_count == 0
card_block_spacing_violation_count == 0
pedagogical_line_not_directly_under_title_count == 0
next_step_card_missing_project_value_microcopy_count == 0
assignee_not_visually_emphasized_count == 0
visible_evidence_level_label_count == 0
unverified_identity_commentary_count == 0
timestamp_not_single_line_count == 0
timestamp_not_right_aligned_count == 0
verified_approving_reviewer_omitted_from_card_count == 0
verified_merger_omitted_from_card_count == 0
```

Also verify:
- dedicated merger + submitted-review lookup was performed for every merged PR
- only verified merger/reviewer names are printed
- `Review:` is based on submitted approvals, never requested reviewers
- unknown merger/reviewer values are blank only after lookup
- assignee/developer name is visually prominent
- explanation is larger than operational metadata
- timestamp is discreet and subordinate
- cards form one coherent component system across all slides

---

**Status:** PRODUCTION
**Version:** 1.4
**Last updated:** 2026-09-17
