---
name: visual_design_mandatory
description: MANDATORY — Canonical slide layout and visual constants
metadata:
  type: process
  critical: true
  required_before: rendering
  version: 3.1
---

# 🎨 VISUAL DESIGN MANDATORY

This is the authoritative visual specification for Monday Meeting presentations.

**Core principle:** content is presented as modern cards, not as text rows or list-like bands.

If content does not fit, create a continuation slide. Never shrink, clip, overlap, or convert cards into plain rows.

---

## 🎯 CANONICAL SLIDE LAYOUT

Every meeting-point slide contains:

1. Slide title at top
2. Optional one-line main message
3. A card area
4. Optional compact footer/source line

**Work items and information items are rendered as individual cards.**

### Mandatory rule

> ONE WORK ITEM = ONE CARD

Never render issue/PR/work items as plain text rows, table rows, horizontal bands, or line-only lists.

---

## 🧩 CANONICAL CARD GRIDS

### ①A–①C — completed merge overview

Use a **3 × 2 card grid**.

- Maximum 6 cards per physical slide
- Read left-to-right, top-to-bottom
- If more than 6 items: create continuation slide
- Do not add a third row
- If one or more cards are too text-heavy for 3 columns at accessibility minimums, reduce that physical slide to 2 × 2 and continue on the next slide

### ①D — active team work

Use a **2 × 2 modern card grid**.

- Maximum 4 cards per physical slide
- One work item per card
- Team border color remains visible
- Branch/status/owner live inside the card
- If more than 4 items: create `①D-2`, `①D-3`, etc.

### ①E — cross-team + assigned/backlog

Use a **2 × 2 modern card grid**.

- Maximum 4 cards per physical slide
- One issue/work item per card
- Never render assigned/backlog items as rows
- If more than 4 items: create `①E-2`, `①E-3`, etc.

### ①F — decisions

Use cards.

- Prefer 2 × 2 when items are compact
- Prefer 2 × 1 or 1 × 2 when cards contain longer rationale
- Maximum 4 cards per physical slide

### ②, ③, ④, ⑤, ⑥, ⑦, ⑧, ⑨, ⑩, ⑪, ⑫, ⑭

Use **modern cards**.

- Default: 2 columns when cards are short/medium
- Fall back to 1 column when a card needs more text
- Never show plain rows or tables as the main information layout
- Maximum 4 cards per physical slide unless a slide-specific rule is stricter
- Create continuation slides instead of compressing cards

### ⑬ — next steps

Use a **4 × 1 card grid**.

- Maximum 4 prioritized cards
- If content is too long for four readable cards, use 2 × 2 and continue on a second slide

### ⑥A — dependency diagram

Exception: visual dependency graph is allowed.

- Every node is still a rounded card
- Maximum 3–4 chains per slide
- Split to continuation slide if needed

---

## 🎴 MODERN CARD SURFACES — MANDATORY

All content containers must look like modern card surfaces placed on a dark navy background.

### Card shape

- Corner radius: **16–20 px**
- No sharp 90° content boxes
- Card height is content-driven
- Equal heights are allowed only when all text fits naturally

### Card background

- Slide background: `#0F1830`
- Card background: `#18233D`
- Optional alternate card surface: `#202C47`

### Border

- Neutral border: `1px solid #334155`
- Team-owned cards may use a stronger team-color left border or outline accent
- Do not use bright hard rectangular frames

### Box shadow — modern depth

Cards MUST have a subtle shadow/depth effect when the renderer supports it.

Canonical CSS-equivalent shadow:

```css
box-shadow:
  0 10px 30px rgba(0, 0, 0, 0.22),
  0 2px 8px rgba(0, 0, 0, 0.16);
```

PowerPoint/PptxGenJS equivalent:

- opacity/transparency should remain subtle
- blur should be soft
- distance should be small
- shadow must not reduce text contrast
- shadow must not be used as a substitute for spacing

**Goal:** modern layered surface, not floating/glowing UI.

### Internal spacing

- Padding: **18–22 px** on all sides
- Title → contribution microcopy gap: **4–6 px**
- Contribution microcopy → primary detail gap: **10–12 px**
- Body → metadata gap: minimum **12 px**
- Gap between cards: minimum **20 px**

---

## ✨ CONTRIBUTION MICROCOPY — ISSUE, PR & MERGE CARDS

Every card whose primary object is an **Issue, Pull Request, or merged Pull Request** MUST contain one short pedagogical explanation immediately below the title.

### Purpose

The line answers, in plain Swedish:

> **Vad bidrar detta arbete med till koden eller produkten?**

It is supporting context, not status information. It should help a reader understand the technical value without opening GitHub.

### Placement

Always directly below the issue/PR/merge title and above owner/status/branch information.

```text
#85 · Responsive shared header
Gör navigationen användbar även på mindre skärmar.

Björn · Frontend
◐ Pågår
Branch: 85-frontend-responsive...
17 sep 08:42
```

### Wording

- One short sentence only
- Prefer **8–14 words**
- Maximum roughly **90 characters** when practical
- Plain language before implementation jargon
- Explain code/product contribution, not project administration
- Do not repeat the title with different words
- No hype, sales language or vague phrases such as “förbättrar systemet” without saying how

Good:
- `Lägger till JWT-autentisering så API-anrop kan verifiera användaren.`
- `Gör portföljdata tillgänglig via en återanvändbar React-hook.`
- `Skyddar loginflödet mot SQL-injektion.`
- `Gör toppnavigationen responsiv på mindre skärmar.`

Bad:
- `Arbete med autentisering.`
- `Förbättrar koden.`
- `Viktig feature.`
- `Denna PR är nu mergad.`

### Evidence / no guessing

The contribution line MUST be grounded in verified repository evidence.

Use this order:

**For Issue cards:**
1. Issue title + issue body / acceptance criteria
2. Linked PR when one exists
3. Verified matching branch/commit messages

**For PR cards:**
1. PR title + PR body
2. Changed files / diff summary when available
3. Linked issue / acceptance criteria
4. Commit messages

**For merged PR cards:**
1. Actual merged PR title/body + changed files
2. Linked issue
3. Commit messages

If there is not enough verified information to explain the contribution safely, show:

`Bidrag till koden behöver verifieras.`

Do not invent implementation effects.

### Tense

- Open Issue: describe the intended contribution, e.g. `Gör ...`, `Lägger till ...`
- Open PR: describe what the PR changes, e.g. `Kopplar ...`, `Inför ...`
- Merged PR: describe the delivered contribution, e.g. `Skyddar ...`, `Lägger till ...`

Avoid process phrasing such as `ska jobba med`, `är mergad`, `PR för` when the actual code contribution can be stated instead.

---

## 🌫️ DISCREET MICROCOPY & TIMESTAMP STYLE

Contribution microcopy and card timestamps share one deliberately low-emphasis visual style.

### Canonical style

- Font size: **12–13 pt**
- Weight: regular
- Text color: **`#8290A7`**
- Line height: approximately **1.3–1.4**
- No badge, pill, border or background behind the line
- Left aligned
- Maximum 1–2 visual lines

This color should feel close to the card surface without disappearing. It is intentionally quieter than normal metadata (`#94A3B8`) and much quieter than primary text.

### Timestamp

Dates/timestamps inside cards use the same style and color:

```text
17 sep · 08:42
```

or, when the semantic label matters:

```text
Merged 16 sep · 18:40
Senaste commit 17 sep · 08:42
```

### Important accessibility boundary

This low-emphasis style may ONLY be used for:

- contribution microcopy
- timestamps/dates
- optional evidence/source micro-labels

Never use it for:

- issue/PR title
- assignee/owner
- status
- blocker
- branch when branch is operationally important
- deadline/action that must be discussed

Those remain at their normal readable hierarchy.

If the rendered projector/view makes `#8290A7` unreadable, increase contrast while keeping the same muted visual role. Never lower contrast further merely for aesthetics.

---

## 📋 CARD CONTENT STACK

Every Issue/PR/Merge card uses this internal hierarchy:

1. **Title**
   - Issue/PR number + short title
   - 20 pt minimum

2. **Contribution microcopy**
   - One pedagogical sentence explaining the contribution to code/product
   - 12–13 pt, `#8290A7`
   - Same visual family as timestamps

3. **Primary detail**
   - Owner, status, team, or short summary
   - 18 pt minimum

4. **Secondary detail**
   - Branch, blocker, review state
   - 18 pt minimum when it must be read during the meeting

5. **Timestamp / metadata**
   - Date/time in contribution-microcopy color
   - 12–13 pt
   - Other small source/evidence labels: 12–14 pt

Example:

```text
┌────────────────────────────────┐
│ ◐ #85 · Responsive header      │
│ Gör navigationen användbar     │
│ även på mindre skärmar.        │
│                                │
│ Björn · Frontend               │
│ Pågår                          │
│ Branch: 85-frontend-responsive │
│ 17 sep · 08:42                 │
└────────────────────────────────┘
```

**Never collapse these fields into a single text row merely to save vertical space.**

---

## 📐 RESPONSIVE CARD BEHAVIOR

Cards must behave like responsive UI surfaces.

- Height: auto/content-driven
- Text wraps inside card
- No text clipping
- No shrink-to-fit
- No fixed text-box heights that can cause overlap
- Geometry adapts to content

### Fit priority

When content is too large:

1. Let the card grow
2. Use fewer cards on that physical slide
3. Move remaining cards to a continuation slide

Never:

- reduce body text below minimum
- reduce card padding below minimum
- overlap text zones
- convert cards to rows
- hide contribution microcopy, branch/status/owner merely to force fit

---

## 📐 TYPOGRAPHY — BINDING MINIMUMS

| Element | Minimum |
|---|---:|
| Slide title/header | **32 pt** |
| Section header | **22 pt** |
| Card title / main content | **20 pt** |
| Secondary readable information | **18 pt** |
| Contribution microcopy | **12–13 pt** |
| Card timestamp | **12–13 pt** |
| Other small labels/footer | **12–14 pt** |

### Line height

- Main/secondary text: approximately **1.4–1.6**
- Microcopy/timestamps: approximately **1.3–1.4**
- Never compress line height until lines visually collide

### Forbidden

- Shrink-to-fit
- Auto-reduce-font
- Main content below 20 pt
- Secondary meeting content below 18 pt
- Contribution microcopy below 12 pt
- Tiny text used to preserve a grid

---

## 🖊️ MEETING-POINT HEADERS

All meeting point slides ①–⑭:

- Format: `✏️① Slide Title`
- Pen first
- No space between pen and meeting-point symbol
- One space after meeting-point symbol
- 32 pt bold minimum

Cover slide ⓪ has no pen and no meeting-point header.

---

## 🎨 PRESENTATION THEME

All slides use dark navy background.

| Element | Hex |
|---|---|
| Slide background | `#0F1830` |
| Card surface | `#18233D` |
| Alternate surface | `#202C47` |
| Neutral border/divider | `#334155` |
| Main text | `#FFFFFF` |
| Secondary text | `#CBD5E1` |
| Muted text | `#94A3B8` |
| Contribution/timestamp microcopy | `#8290A7` |

Do not use white/light slide backgrounds.

---

## 🏷️ TEAM COLORS

Team color communicates ownership/category only.

| Team | Color |
|---|---|
| Frontend | `#2DD4BF` |
| Backend | `#FF4FA3` |
| Native | `#A855F7` |
| Cross-team | `#CBD5E1` |
| Other | `#94A3B8` |

Use team color as:

- left accent border
- subtle outline
- small badge/accent

Do not use team color as full-card background.

---

## 🎨 STATUS COLORS

Status uses symbol + text.

| Status | Symbol | Color |
|---|---|---|
| Done/Merged | ✅ | `#4CAF50` |
| In progress | ◐ | `#FF9800` |
| Blocked/Critical | 🔴 | `#F44336` |
| Unknown/Neutral | ? | `#94A3B8` |

Status color must not replace team ownership color.

---

## 📦 TEXT BOX RULE

Ordinary text boxes such as titles, captions, dates and footers:

- fill: none/transparent
- border: none
- outline: none

Visible card surfaces are reserved for actual information cards/components.

---

## 🎯 TEAM DETAIL CARDS — ③④⑤

Frontend, Backend and Native detail slides use identical modern card geometry.

- Cards only
- No tables
- No row bands
- Default 2 × 2 layout, max 4 work cards per slide
- If a card needs more room: use 2 × 1 or single-column cards
- Continuation slides when needed
- Only team accent color differs
- Issue/PR cards include contribution microcopy directly below the title

---

## 🎴 COMPACT CARD STANDARD — ②, ⑥–⑫, ⑭

Use modern cards, not rows.

Default behavior:

- 2 × 2 for compact/medium information
- 2 × 1 for longer cards
- 1 × 1 when a single item needs significant space
- Maximum 4 cards per physical slide
- Continue on next slide instead of reducing readability

No full-width text banners unless a slide specification explicitly calls for a single hero/message card.

---

## 🔗 DEPENDENCY DIAGRAMS — ⑥A

- Each issue = rounded shadowed card/node
- Use arrows for relationships
- Prefer left-to-right for short chains
- Prefer top-to-bottom when wide
- Avoid crossing arrows
- Never compress diagram until card text becomes unreadable

---

## 🚨 OVERFLOW & COLLISION GATE

Before delivery, the rendered artifact must satisfy:

```text
text_overlap_count == 0
card_overlap_count == 0
text_outside_card_count == 0
text_clipping_count == 0
out_of_bounds_element_count == 0
font_below_minimum_count == 0
plain_row_work_item_count == 0
missing_contribution_microcopy_count == 0
```

Also verify:

- Cards have visible separation from background
- Cards have modern rounded geometry
- Shadow/depth is subtle and consistent
- ①D and ①E are card grids, not row lists
- Every Issue/PR/Merge card has contribution microcopy directly under its title
- Contribution microcopy and timestamps use the same muted visual family
- No page becomes dense merely to avoid adding another slide

If any condition fails:

1. Do not deliver
2. Create continuation slide(s)
3. Rerender
4. Inspect again

---

## ✅ CORE PRINCIPLE

The presentation should feel like a modern dashboard translated into a calm meeting deck:

**dark navy canvas + modern soft cards + subtle shadow + clear primary type + discreet explanatory microcopy + generous whitespace.**

Cards are the visual language. Rows are not.

---

**Status:** PRODUCTION
**Version:** 3.1
**Last updated:** 2026-09-17
