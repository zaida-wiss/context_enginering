---
name: card_component_standard
description: MANDATORY — Canonical internal layout for all presentation cards
metadata:
  type: design-specification
  critical: true
  required_before: rendering
  version: 1.7
---

# 🎴 CARD COMPONENT STANDARD

This file is the **single authority for the internal layout of presentation cards**.

It owns:
- card-internal typography
- order of card content
- spacing between card text blocks
- person/team identity emphasis
- merge/review metadata presentation
- branch/status metadata presentation
- verification/provenance placement
- visible timestamps
- card-internal visual hierarchy
- card-internal responsive behavior

It does **not** own global slide colors, slide structure, data acquisition, evidence classification or slide selection.

If another document contains an example that conflicts with this file, **this file wins for card internals**, except that `READABILITY_HARD_RULES.md` may define stricter readability minima.

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

# 2. UNIVERSAL CARD VISUAL HIERARCHY — APPLIES TO ALL CARDS

This hierarchy applies to **every card in the entire presentation**, including Issue, PR, Merge, action, next-step, risk, decision, sprint-plan, capacity, dependency, question and informational cards.

Visual priority must be:

1. **Card title** — primary text color
2. **Pedagogical explanation/supporting text** — secondary, calmer color
3. **Person/team identity row when present** — primary text color, but physically anchored in the bottom zone
4. **Verification/provenance + operational metadata** — muted/quiet color in the bottom zone
5. **Relevant timestamp when present** — quiet microcopy/timestamp color, deliberately discreet

Hard rules:
- title is the strongest text layer
- supporting explanation must be visibly calmer than title
- identity remains easy to scan but must not interrupt the title/explanation reading flow
- metadata must be more discreet than the supporting explanation unless a blocker/critical semantic requires emphasis
- timestamps are contextual microcopy and must **not compete for attention** with title, identity, explanation or operational metadata
- do not use accent/team colors for ordinary metadata merely to attract attention
- secondary/quiet text must blend more gently into the card surface while still meeting WCAG contrast requirements
- never reduce contrast below WCAG AA to make text look quieter
- avoid extra-bold/black weights; normal card titles should look clear, not heavy

The intended scan order is:

```text
Rubrik → pedagogisk förklaring → [luft] → namn → verifiering/metadata → tid
```

---

# 3. REQUIRED CONTENT ORDER + BOTTOM ANCHOR

For Issue/PR/Merge/action cards, use this visual order:

1. **Title**
2. **Pedagogical contribution / project-value line** — directly under the title
3. flexible whitespace / remaining content area
4. **Person/team identity row** when relevant — anchored in the card's bottom information zone
5. **Verification/provenance + operational metadata** — directly below identity in the bottom information zone
6. **Timestamp** — bottom-most row when relevant according to the timestamp standard

### Bottom-anchor hard rule

**Name/identity and verification/provenance must always sit at the bottom of the card, not immediately after the body copy.**

This applies to all card types when those fields exist:
- status cards
- issue/PR cards
- merged PR cards
- decision cards
- action/next-step cards
- risk cards
- team-summary cards

Examples of bottom-zone verification/provenance:
- `✅ Mötesprotokoll 17 sep`
- `✅ GitHub + mötesprotokoll`
- `🔎 AI-analys`
- `⭐ AI-förslag`
- `📅 Schemafakta`
- branch / PR / merge-review metadata when relevant

If a card has no person identity, the verification/provenance row is still anchored to the bottom.

If a card has a timestamp, the timestamp is the lowest row and verification/metadata stays above it.

Do not vertically justify all rows across the card. The title/explanation stay grouped at the top; the identity/verification area is a deliberate bottom group.

Do not insert decorative or provenance rows between title and pedagogical explanation.

For action and next-step cards, the pedagogical line must answer:
- what the action concerns
- what it contributes to the project / why it matters

---

# 4. PERSON IDENTITY ROW — FIRST NAME ONLY

Canonical visible format is the person's first name only. **Team is shown by the card's left border color**, not by text.

**Name format: FIRST NAME ONLY** (no team label, no full name).

Card border colors represent teams:
- Frontend: `#2DD4BF` (teal)
- Backend: `#FF4FA3` (pink)
- Native: `#A855F7` (purple)
- Cross-team: `#CBD5E1` (slate)
- Neutral: `#94A3B8` (gray)

Examples:
- `Zaida` (not `Zaida Wiss`, not `Zaida · Frontend`)
- `Tomac`
- `Rasha`
- `Henrik`
- `Hela teamet`

Hard rules:
- do **not** use full names — first name only
- do **not** show team label in text — the card's left border color is the team indicator
- do **not** prefix with `Utvecklat av`, `Developed by`, `Developer:`, `Assigned to:` or equivalent wording
- use the main/primary text color, not the team accent color, for ordinary identity text
- use semibold/bold weight, but not extra-bold/black
- the row must be easier to scan than branch/status/provenance metadata
- the row belongs in the **bottom information zone** defined above
- do not infer a developer from commit authorship when project attribution evidence says otherwise

Typography:
- preferred: **14–15 pt**
- minimum: **13 pt**

---

# 5. RESPONSIVE TYPOGRAPHY — START LARGE, NEVER AUTO-SHRINK

General principle:
1. start at the preferred size
2. reduce only when required to fit
3. reduce stepwise, never below the role minimum
4. if minimum still does not fit, change geometry/density or paginate

Do not choose a smaller size merely because it technically fits.

All card text follows the dyslexia-friendly typography rules in `READABILITY_HARD_RULES.md`.

## Card title
- preferred: **19–20 pt**
- minimum: **18 pt**
- semibold/bold
- **avoid extra-bold/black/heavy display weights**
- main/primary text color from global palette
- multiline title line spacing: **1.05 minimum**

## Pedagogical contribution / project-value line
This answers: **Vad gäller detta och vad löser/tillför detta i projektet?**

- preferred: **14–15 pt**
- minimum: **13 pt**
- regular
- secondary text color; deliberately calmer than title/identity
- normally 1–3 visual lines when needed for pedagogical clarity
- placed immediately under the title
- multiline line spacing: **1.15 minimum, 1.2 preferred**

## Operational metadata / verification
Examples:
- `Merged: Zaida | Review: Björn`
- `Branch: frontend/#83-save-allocation`
- `✅ Mötesprotokoll 17 sep`
- `⭐ AI-förslag`

Style:
- preferred: **12–13 pt**
- minimum: **11 pt**
- regular
- metadata/quiet text color from the global palette
- visually subordinate to title, identity and pedagogical explanation
- placed in the bottom information zone
- multiline metadata line spacing: **1.1 minimum**

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

## Timestamp typography
- preferred: **11–12 pt**
- minimum: **11 pt**
- uses the global **Quiet microcopy/timestamp** color from `VISUAL_DESIGN_MANDATORY.md` (`#A2ABC0` unless the palette authority changes it)
- regular weight
- deliberately low-emphasis while remaining WCAG-AA compliant
- visually compact and never styled like title/identity text

Never go below 11 pt.

---

# 6. TIMESTAMP STANDARD — RELEVANT TIME ONLY

A timestamp is not generic activity decoration. It is shown only when the time itself helps the meeting understand delivery or current status.

## Merged PR cards
Show the **merge timestamp**.

Do not substitute:
- PR creation time
- latest commit time
- issue creation time

when the card represents a completed merge.

## Active/open work cards
Show the latest commit/push timestamp only when it materially helps the meeting understand recency of work.

Do **not** use:
- PR opened/created timestamp
- issue created timestamp
- issue updated timestamp

If shown:
- exactly **one compact line** — date and clock time must never wrap to separate lines
- canonical format: `14 sep · 10:16`
- use a middle dot separator (`·`), not a line break
- lower-right aligned where card geometry permits
- use the global **Quiet microcopy/timestamp** color (`#A2ABC0` in the current palette)
- keep it visually more discreet than the operational metadata
- no prefix such as `Merged`, `Mergad`, `Senaste commit`, `PR skapad` or evidence label
- do not place timestamp so close to metadata that rows visually merge
- if the card is too narrow for one-line timestamp at the minimum font size, change geometry or paginate; **never wrap the timestamp**

Canonical example:

```text
14 sep · 10:16
```

If the timestamp is not useful to the meeting, omit it rather than filling space because the source exposes a date.

---

# 7. CANONICAL MERGED-PR CARD

```text
#80 · Drift från live target
Beräknar drift från aktuell målallokering i stället för mock-flagga.


Tomac
Merged: Zaida | Review: Björn
                         14 sep · 10:16
```

Note: Team is shown by the card's left border color (teal=Frontend), not by text.

Rendering rules:
- pedagogical explanation sits directly under the title
- flexible whitespace separates the explanation from the bottom information zone
- `Tomac` sits near the bottom of the card
- merge/review verification sits directly below the name
- timestamp sits at the bottom and stays one line
- identity uses the primary text color, not team accent color
- timestamp uses the quiet microcopy/timestamp color and stays visually unobtrusive
- only verified merger and actual approving reviewer names appear
- dedicated merger/review lookup is mandatory before an empty field is accepted
- timestamp is the merge timestamp

---

# 8. CANONICAL ACTIVE ISSUE / PR CARD

```text
#88 · Kritiska MVP-tester
Testar login, målallokering och drift för kritiska MVP-flöden.


Zaida
PR #114 · Build/frontend/#88-critical-interactions
```

Name and operational verification/metadata are anchored at the bottom.

Do not append PR creation/latest-commit time by default.

Evidence level is **not rendered as text on the card**. Do not show `GitHub · nivå 1`, `nivå 2`, etc.

The evidence hierarchy remains an internal classification used to decide whether/how an item is shown.

If a status symbol is useful for the meeting (for example waiting/blocked), it may be used together with text. Do not add a separate evidence-level symbol merely to expose the internal classification.

---

# 9. CANONICAL DEPENDENCY / NEXT-STEP NODE

Dependency and next-step nodes use the same universal hierarchy:

```text
API-kontrakt
Definierar endpoints + payload så Frontend och Backend kan integrera stabilt.


🔴 Behöver låsas
```

Hard rules:
- title first
- pedagogical/project-value line immediately below title
- verification/status/dependency belongs in the bottom information zone
- arrows/connectors stay outside cards
- if evidence is insufficient, use the approved uncertainty wording from the content/data authority
- on `13. Nästa steg`, every card must explain both what the action concerns and why it matters to the project
- if person/team appears, it follows the identity rule and is bottom-anchored
- if a relevant timestamp appears, it follows the quiet timestamp rule and remains a single line

---

# 10. MINIMUM VERTICAL SPACING & LINE HEIGHT — HARD RULE

Separate semantic blocks must never visually touch.

Use these **minimum rendered gaps**:
- title → pedagogical explanation: **6 px minimum, 8 px preferred**
- explanation → bottom identity zone: **14 px minimum**; normally much larger because identity is bottom-anchored
- identity → operational metadata/verification: **8 px minimum**
- one operational metadata row → next separate metadata row: **6 px minimum**
- operational metadata → bottom timestamp/source area: **10 px minimum** unless flexible whitespace is larger

Line spacing:
- multiline body/explanation: **1.15 minimum, 1.2 preferred**
- multiline card title: **1.05 minimum**
- metadata: natural line height, never compressed until glyphs visually collide

Wrapped lines inside the same text block use natural line-height and no artificial paragraph gap.

These values are minimums, not targets for compression.

If a card cannot fit while respecting them:
1. shorten wording without losing meaning
2. let the card grow
3. reduce grid density
4. paginate

Never solve fit by collapsing these gaps below minimum, overlapping rows, shrinking text below role minimums, or removing the pedagogical explanation.

---

# 11. RESPONSIVE CARD GEOMETRY

Allowed adaptations:
- natural text wrapping
- card grows in height
- wider cards through a lower-density grid
- 2×2 → 2×1 → 1×1 when needed
- continuation slide

Fit order:
1. preferred typography
2. typography reduction only when required and only within explicit role ranges
3. canonical spacing and line-height, never below hard minimums
4. preserve top content group + bottom information zone
5. adapt card/grid dimensions
6. paginate

Never:
- clip or overlap text
- allow independent textboxes to occupy the same vertical space
- omit required rows
- omit pedagogical/project-value explanation
- move name/verification up into the body area merely to make a card fit
- expose internal evidence-level labels to save explanation space
- reduce below component minimums
- reduce contrast below WCAG AA
- use automatic shrink-to-fit
- wrap date and time onto separate lines

---

# 12. RENDER CHECKS

Before delivery verify across **all cards**:

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
text_line_spacing_below_minimum_count == 0
pedagogical_line_not_directly_under_title_count == 0
identity_not_bottom_anchored_count == 0
verification_not_bottom_anchored_count == 0
bottom_information_zone_overlap_count == 0
next_step_card_missing_project_value_microcopy_count == 0
legacy_developed_by_label_count == 0
legacy_identity_prefix_count == 0
unnecessary_activity_timestamp_count == 0
identity_row_not_primary_color_count == 0
timestamp_not_quiet_microcopy_color_count == 0
timestamp_too_prominent_count == 0
secondary_text_too_prominent_count == 0
assignee_not_visually_emphasized_count == 0
visible_evidence_level_label_count == 0
unverified_identity_commentary_count == 0
timestamp_not_single_line_count == 0
timestamp_wrapped_line_count == 0
timestamp_not_right_aligned_count == 0
verified_approving_reviewer_omitted_from_card_count == 0
verified_merger_omitted_from_card_count == 0
```

Also verify:
- these hierarchy checks apply to **every card type**, not only PR/issue cards
- no card displays `Utvecklat av`, `Developed by`, `Developer:` or `Assigned to:` before the person/team identity row
- person identity is first-name-only and sits in the bottom information zone
- verification/provenance is at the bottom of the card; if a timestamp exists, it sits immediately above the timestamp
- merged PR timestamp is the merge timestamp
- open/active cards do not display PR-created/latest-commit timestamps merely because that data exists
- timestamps use the quiet microcopy/timestamp color and do not compete for focus
- every displayed timestamp is a single line in `D MMM · HH:MM` style, localized like `14 sep · 10:16`
- pedagogical explanation is calmer than the primary layer
- metadata/provenance is visually quiet while still WCAG-AA compliant
- dedicated merger + submitted-review lookup was performed for every merged PR
- only verified merger/reviewer names are printed
- `Review:` is based on submitted approvals, never requested reviewers
- unknown merger/reviewer values are blank only after lookup
- cards form one coherent component system across all slides

---

**Status:** PRODUCTION
**Version:** 1.7
**Last updated:** 2026-09-17
