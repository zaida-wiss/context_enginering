---
name: card_component_standard
description: MANDATORY — Canonical internal layout for all presentation cards
metadata:
  type: design-specification
  critical: true
  required_before: rendering
  version: 1.8
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

Team color normally appears as a narrow vertical accent on the left. For issue
and PR cards, the verified `#NUMBER` also uses the owning team's color. Team
color must not outline or fill the whole card.

Canonical team colors:
- Frontend: `#2DD4BF`
- Backend: `#FF4FA3`
- Native: `#A855F7`
- Cross-team: `#CBD5E1`
- Neutral: `#94A3B8`

Recommended left accent width: visually equivalent to **4–6 px**.

---

# 2. UNIVERSAL CARD VISUAL HIERARCHY — APPLIES TO ALL CARDS

This hierarchy applies to **every card in the entire presentation**, including Issue, PR, Merge, action, next-step, risk, decision, sprint-plan, capacity, dependency, question and informational cards.

Every text block has one of four visual-priority levels:

1. **Primary focus** — issue title and assignee/person identity
2. **Action focus** — `⭐ AI-förslag`, including proposed new issues
3. **Supporting meaning** — merge/review information, pedagogical explanation and `🔎 AI-analys`
4. **Quiet context** — sources/provenance, branch, timestamp and technical/operational metadata

Hard rules:
- issue title and assignee share the strongest level-1 treatment
- AI proposals are clearly visible at level 2 but never compete with the issue title/assignee
- merge/review and pedagogical explanation share the calmer level-3 treatment
- AI analysis uses level 3 unless another active content rule requires stronger warning semantics
- inline provenance symbols stay with their content blocks; full symbol + text provenance labels use level 4 in the bottom information zone
- branch, timestamps and technical metadata use level 4 and must not compete with levels 1–3
- do not use accent/team colors for ordinary metadata merely to attract attention
- level 4 blends most gently into the card surface while still meeting font-size and WCAG contrast requirements
- never reduce contrast below WCAG AA to make text look quieter
- avoid extra-bold/black weights; normal card titles should look clear, not heavy

Level is communicated by a combination of size, weight, spacing and WCAG-safe
color. Color alone never communicates priority. “Quiet” means low emphasis, not
low legibility.

The intended scan order is:

```text
Issue-titel → pedagogisk förklaring/AI → [luft] → assignee → källa/metadata/tid
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

**Name/identity and the full symbol + text verification/provenance row must always sit at the bottom of the card, not immediately after the body copy. Inline provenance symbols remain with their content blocks.**

This applies to all card types when those fields exist:
- status cards
- issue/PR cards
- merged PR cards
- decision cards
- action/next-step cards
- risk cards
- team-summary cards

Examples of bottom-zone verification/provenance:
- `👥 ✅ Mötesprotokoll 17 sep`
- `✅ GitHub + mötesprotokoll`
- `🔎 AI-analys`
- `⭐ AI-förslag`
- `📅 Schemafakta`
- branch / PR / merge-review metadata when relevant

If a card has no person identity, the verification/provenance row is still anchored to the bottom.

If a card has a timestamp, the timestamp is the lowest row and verification/metadata stays above it.

Do not vertically justify all rows across the card. The title/explanation stay grouped at the top; the identity/verification area is a deliberate bottom group.

Do not insert a separate full-text provenance row between title and pedagogical
explanation. An inline canonical symbol may prefix the semantic block it identifies.

For action and next-step cards, the pedagogical line must answer:
- what the action concerns
- what it contributes to the project / why it matters

---

# 4. PERSON IDENTITY ROW — FIRST NAME ONLY

Canonical visible format is the person's first name only. Team is shown by the
containing team section/column and may be reinforced by the card's left accent
and a team-colored issue/PR number.

**Name format: FIRST NAME ONLY** (no team label, no full name).

Team colors represent teams:
- Frontend: `#2DD4BF` (teal)
- Backend: `#FF4FA3` (pink)
- Native: `#A855F7` (purple)
- Cross-team: `#CBD5E1` (slate)
- Neutral: `#94A3B8` (gray)

Examples:
- `{FIRST_NAME}` on a dedicated team slide
- `{FIRST_NAME} · {TEAM}` only when an explicit non-color team cue is required
- `Hela teamet`

Hard rules:
- do **not** use full names — first name only
- team ownership must never rely on color alone across the complete slide context
- on a dedicated team slide whose primary header explicitly names the team, do not repeat the team name inside every card; the header supplies the non-color ownership cue and the left accent color is supplementary
- on mixed-team slides, include an explicit non-color team cue on each relevant card: `Frontend`, `Backend`, `Native/System` or `Cross-team`
- if a card is reused outside its original dedicated team slide, add the explicit team label again
- team accent color remains supplementary only
- do **not** prefix with `Utvecklat av`, `Developed by`, `Developer:`, `Assigned to:` or equivalent wording
- use the main/primary text color, not the team accent color, for ordinary identity text
- use semibold/bold weight, but not extra-bold/black

## Issue and PR number team color

Every verified issue or PR identifier uses the owning team's canonical color:
- Frontend: `#2DD4BF`
- Backend: `#FF4FA3`
- Native: `#A855F7`
- Cross-team: `#CBD5E1`

The identifier is dynamic, for example `#ISSUE_ID` or `#PR_ID`; examples never
hard-code which PRs exist. For an open PR, the complete heading begins
`📌 #[PR_NUMBER]`. Apply team color to `#[PR_NUMBER]`, not to the pushpin.
The same card's bottom information zone must contain `📌 Väntar i PR`.
If the primary font lacks `📌`, draw the pushpin as a native/vector icon;
never replace it with `|`, another ASCII marker, a tag or text-only status.

The number color is supplementary. On mixed-team slides, team ownership must
also be explicitly available from a text label on the card. On dedicated team
slides, the primary slide header may provide that non-color team meaning. The
colored number must meet
WCAG 2.2 AA contrast. If the canonical color fails contrast on the selected
surface, use its approved accessible contrast variant without changing the team
meaning.
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
- multiline line spacing: **1.15 standard and minimum**; increase only when the rendered font requires it

## Operational metadata / verification
Examples:
- `Merged: {MERGER} | Review: {REVIEWER}`
- `Branch: {WORK_BRANCH}`
- `👥 ✅ Mötesprotokoll 17 sep`
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
- `Merged: {MERGER} | Review: {REVIEWER}`
- `Merged: {MERGER} | Review: {REVIEWER_A}, {REVIEWER_B}`
- `Merged: {MERGER} | Review:`
- `Merged: | Review: {REVIEWER}`

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
#ISSUE_ID · [verifierad titel]
Beräknar drift från aktuell målallokering i stället för mock-flagga.


{FIRST_NAME}
Merged: {MERGER} | Review: {REVIEWER}
                         14 sep · 10:16
```

Note: On a dedicated team slide, the slide header names the team and the card uses the supplementary left accent color without repeating the team text. On mixed-team slides, the card includes explicit team text plus the accent color.

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
#ISSUE_ID · [verifierad titel]
Testar login, målallokering och drift för kritiska MVP-flöden.


{FIRST_NAME}
PR #PR_ID · {WORK_BRANCH}
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
- multiline body/explanation: **1.15 standard and minimum**
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

## 10A. CONTENT-FLOW CONTAINERS — HARD RULE

Every card is a parent container with a vertical content-flow layout. Every
semantic text section is its own child container/flex row, for example:

1. title
2. pedagogical contribution
3. status or work detail
4. dependency/AI/fact blocks
5. flexible spacer when a bottom zone is required
6. identity
7. provenance/metadata
8. timestamp

Placement rules:
- measure each child after wrapping with the actual font, size, width and line spacing
- set the next child's top position from the previous child's measured bottom plus the required gap
- child containers use content-driven height; fixed text heights are forbidden
- a parent card height is calculated from padding + all measured children + all required gaps
- a bottom-anchored information zone reserves its full measured height before the upper content area is laid out
- upper content may never grow into the reserved bottom zone
- independent absolute-positioned textboxes may not be used for vertically stacked card content
- if the renderer lacks native flex layout, emulate vertical flex deterministically with measured bounding boxes and a single cursor advancing downward
- after rendering, compare all sibling bounding boxes; any intersection greater than zero fails the card

Fit order:
1. use 1.15 body line spacing and the role-specific font size
2. wrap and remeasure every child container
3. grow the card when space permits
4. reduce cards per slide toward the allowed minimum
5. continue the meeting point on the next lettered slide

Never reduce line spacing below its minimum to compensate for an incorrectly
measured container.

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
team_accent_uses_left_edge_not_full_outline == true
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
content_block_provenance_symbol_missing_count == 0
card_bottom_provenance_full_label_missing_count == 0
card_bottom_provenance_symbol_text_mismatch_count == 0
waiting_pr_pushpin_missing_before_identifier_count == 0
waiting_pr_bottom_pushpin_label_missing_count == 0
canonical_symbol_ascii_transliteration_count == 0
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
- every semantic content block begins with its canonical provenance symbol
- the bottom provenance row deduplicates every symbol used and shows symbol + full text label
- if a timestamp exists, the full bottom provenance row sits immediately above the timestamp
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
**Version:** 1.8
**Last updated:** 2026-09-17
