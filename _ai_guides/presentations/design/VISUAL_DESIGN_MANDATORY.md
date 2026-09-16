---
name: visual_design_mandatory
description: MANDATORY — Canonical slide layout and visual constants
metadata:
  type: process
  critical: true
  required_before: rendering
---

# 🎨 VISUAL DESIGN MANDATORY

**Every presentation slide uses EXACTLY this layout. Nothing else is allowed.**

---

## 🎯 CANONICAL SLIDE LAYOUT

Every slide contains:

```
┌─────────────────────────────────────┐
│  ① RUBRIK — Team/Mötespunkt        │  28pt BOLD (NPF: large hierarchy)
├─────────────────────────────────────┤
│                                     │
│  HUVUDBUDSKAP (one-liner)           │  13pt, clear statement
│                                     │
│  [CONTENT BLOCK 1]                  │  Fullwidth block
│  (work items or content)            │  Vertical stack only
│                                     │
│  [CONTENT BLOCK 2]                  │  Max 1–3 blocks per slide
│  (if needed)                        │
│                                     │
│  (If 4+ items: auto-split to ①A.1) │
└─────────────────────────────────────┘
```

### Content Block Structure

Each block displays ONE CATEGORY of work (merged PRs, open issues, etc):

```
✅ #107 BCrypt login fix
   Säkrar loginflödet. Rasha · väntar på review

◐ #104 Spring Security
   Fokus denna vecka. Erik · pågår

🔴 #108 Auth contract
   Blockerad på Backend. Tomac · waiting
```

**Each work item = ONE LINE (within a soft card):**
- Symbol (✅ ◐ 🔴 etc)
- Issue# and Title
- Owner/Status

**All text must be contained within soft, rounded cards with generous padding and responsive height.**

---

## ⚠️ EXCEPTION — SLIDE ①A MERGED OVERVIEW BOARD

Slide ①A ("Mergade PR:er") is the ONLY standard exception to the full-width single-card layout.

**For Slide ①A ONLY:**
- A 3 × 2 card grid IS REQUIRED
- Maximum 6 cards per slide
- Cards have identical dimensions
- Cards are read chronologically left-to-right, top-to-bottom
- Large whitespace must remain around the board
- Each card has team-colored border (teal/hot pink/purple/light slate)
- Cards are rendered as soft rounded cards with 12–18px corners
- This is a presentation summary, not a GitHub/Jira dashboard

**All other slides (①B-①E, ②, ③, etc.):**
- Continue to follow the canonical vertical full-width block layout
- Content rendered as stacked soft cards (not grid)
- Each card is a soft, rounded, responsive container
- Only exception to single-stacked layout is ①A

---

## 🎴 SOFT CARD SURFACES — Mandatory visual style

All content containers must be rendered as soft cards rather than hard rectangular boxes.

### Card shape
- Use clearly rounded corners on every content card (12–18px radius)
- Avoid sharp 90-degree corners
- Corners should be visually noticeable but not exaggerated
- Cards should feel soft and calm rather than technical or boxy

### Card appearance
- Cards must visually feel like separate surfaces resting on top of the slide background
- Use subtle contrast between card surface (#18233D) and slide background (#0F1830)
- Borders should be thin and soft (1–2px)
- Team colour may be used as a subtle accent, but the whole card should still feel soft
- Never use a hard, bright rectangular outline

### Internal spacing (mandatory)
- Every card must have generous internal padding (16–20px on all sides)
- Text must never touch the card border
- Clear vertical spacing between: title → person/status → metadata

### Responsive card height
- Card height must be determined by content
- Never use fixed card heights when text length varies
- Cards must grow vertically when text wraps
- All text must stay fully inside the card
- Prefer taller, fewer cards over shallow, many boxes

### Slide density
- Prefer fewer, taller cards over many compressed boxes
- If cards cannot fit comfortably: create additional slide
- Never reduce padding or squeeze text simply to fit more

### Core visual principle
The presentation should resemble information cards placed on a dark tabletop:
soft rounded surfaces, generous whitespace, clear separation and calm visual hierarchy.

---

## 📐 FIXED DIMENSIONS & TYPOGRAPHY

These values NEVER change. Use them exactly.

### Layout

| Property | Value |
|----------|-------|
| Block width | 100% of slide |
| Block height | Auto (content-driven, never compressed) |
| Spacing between blocks | 20px |
| Padding inside block | 16–20px (all sides) |
| Line height | 1.8 (NPF standard) |
| Corner radius | 12–18px (all corners, mandatory softness) |

### Typography

| Element | Font Size | Weight | Color |
|---------|-----------|--------|-------|
| Slide header (meeting point ①②③) | 28pt | BOLD | #FFFFFF (white) |
| Section header (Frontend, Backend, etc) | 14pt | BOLD | #FFFFFF |
| Main message | 13pt | Regular | #CBD5E1 (light slate) |
| Work item title | 13pt | Regular | #FFFFFF |
| Owner/Status | 12pt | Regular | #94A3B8 (muted slate) |

---

## 🎨 PRESENTATION THEME — BACKGROUNDS (MANDATORY)

**ALL slides MUST use dark navy theme. NO EXCEPTIONS.**

| Element | Color | Hex | Usage |
|---------|-------|-----|-------|
| Slide background | Dark Navy | #0F1830 | Every slide |
| Content board/card | Secondary Navy | #18233D | Cards, blocks, containers |
| Alternate board (if needed) | Tertiary Navy | #202C47 | Variation for contrast |
| Dividers/borders (neutral) | Slate | #334155 | Separators (not team-related) |

**CRITICAL THEME RULE:**

All Monday Meeting presentation slides MUST use the dark navy theme (#0F1830).

DO NOT:
- Use white slide backgrounds
- Use light-gray slide backgrounds
- Alternate slide background colors
- Use team color as full-slide background

The dark navy background is constant throughout the deck.

---

## 🎨 STATUS COLORS (SEMANTIC)

Status is communicated via Symbol + Color + Text:

| Status | Symbol | Color | Hex | Usage |
|--------|--------|-------|-----|-------|
| Done/Merged | ✅ | Green | #4CAF50 | Completed work |
| In Progress | ◐ | Orange | #FF9800 | Active work |
| Waiting/Blocked | 🔴 | Red | #F44336 | Blocked or in review |
| Unknown/Closed | 🔵 | Gray | #94A3B8 | Closed or unknown |

**RULE:** Status color = symbol + border/accent color only. Never full-card background.

---

## 🏷️ TEAM COLORS (CATEGORY, NOT STATUS)

Team is communicated via border + badge. Team colors represent TEAM OWNERSHIP only.
They NEVER represent status or priority. **Team colors MUST NEVER overlap with status colors.**

| Team | Color | Hex | Usage | Contrast Check |
|------|-------|-----|-------|---|
| Frontend | Teal | #2DD4BF | Card border + badge | ✅ 4.5:1 on #18233D |
| Backend | Hot Pink | #FF4FA3 | Card border + badge | ✅ 4.5:1 on #18233D |
| Native | Purple | #A855F7 | Card border + badge | ✅ 3:1 on #18233D |
| Cross-team | Light Slate | #CBD5E1 | Card border + badge | ✅ 4.5:1 on #18233D |
| Other | Gray | #94A3B8 | Card border + badge | ✅ 4.5:1 on #18233D |

**RESERVED STATUS COLORS (MUST NOT be used as team colors):**
- Orange (#FF9800) — **ONLY** for status ◐ "In Progress"
- Green (#4CAF50) — **ONLY** for status ✅ "Merged/Complete"  
- Red (#F44336) — **ONLY** for status 🔴 "Blocked"

**CROSS-TEAM BORDER RULE:**
Light Slate border (#CBD5E1) means work affects multiple teams, not a single team.
It is neutral, showing coordination required across team boundaries.
Use on:
- Slide ①A: cross-team merged PRs (in chronological order)
- Slide ①C: cross-team pågår work

**EXAMPLE — Frontend card on slide ①A (Merged):**
- Slide background: #0F1830
- Card background: #18233D
- Card border: #2DD4BF (teal, team ownership)
- Status symbol: ✅ (text only, no colored border)
- Team badge: teal with #0F1830 text
- Text: #FFFFFF
- Metadata: #94A3B8

**EXAMPLE — Backend card on slide ①B (In Progress):**
- Slide background: #0F1830
- Card background: #18233D
- Card border: #FF4FA3 (hot pink, team ownership)
- Status symbol: ◐ (text only, no orange border)
- Team badge: hot pink with #0F1830 text
- Text: #FFFFFF
- Metadata: #94A3B8

**EXAMPLE — Cross-team card on slide ①A or ①C:**
- Slide background: #0F1830
- Card background: #18233D
- Card border: #CBD5E1 (light slate, neutral/multi-team)
- Status symbol: ✅ or ◐ (text only)
- Team badge: "Cross-team" or show affected teams
- Text: #FFFFFF
- Metadata: #94A3B8

**CRITICAL:**
Team colors and status colors are TWO DIFFERENT semantic systems.
On Slide ①A "Merged PRs": all cards already have status = MERGED.
On Slide ①B-①C "Pågår": all cards already have status = ◐ PÅGÅR.
Therefore border color represents TEAM. Do NOT add green/orange/red status borders.
Status is communicated by symbol + text ("Merged" / "◐ Pågår").

---

## 🎨 COLOR SEMANTICS — What Each Color Means

**STATUS COLORS (Indicate project status, not preferences):**

| Status | Symbol | Color | Hex | Meaning | Usage |
|--------|--------|-------|-----|---------|-------|
| **On Track** | ✅ | Green | #4CAF50 | Work completed, on schedule | Merged PRs, finished tasks |
| **In Progress** | ◐ | Orange | #FF9800 | Active work, slight delay acceptable | Ongoing features, open PRs in review |
| **Blocked/Critical** | 🔴 | Red | #F44336 | Critical blocker, needs immediate action | Blocked issues, failed deployments |
| **Unknown/Neutral** | ? | Gray | #94A3B8 | Status unverified or not applicable | Unassigned work, dependencies |

**STRUCTURE COLORS (Non-status information, for dark navy theme):**

| Element | Meaning | Hex | Usage |
|---------|---------|-----|-------|
| **Main Text** | Titles, primary content | #FFFFFF | All readable titles and headers |
| **Secondary Text** | Metadata, timestamps | #CBD5E1 | Assignee, dates, timestamps, secondary info |
| **Muted Text** | Tertiary information | #94A3B8 | Support text, less important details |
| **Neutral Dividers** | Visual separation | #334155 | Borders between sections (not team-related) |

**CRITICAL RULE:** Never use a status color (green/orange/red) unless you mean the status it represents.
If unsure, use neutral colors (#334155, #94A3B8, #CBD5E1) instead.

---

## 🖼️ BORDER & COLOR SEPARATION — Ownership vs Status

**TWO INDEPENDENT SEMANTIC SYSTEMS:**

### 1. OUTER TEAM BORDER (3-6px) — Ownership/Category ONLY

| Border Color | Meaning | Applies To |
|---|---|---|
| **Teal** #2DD4BF | Frontend team ownership | Frontend cards |
| **Hot Pink** #FF4FA3 | Backend team ownership | Backend cards |
| **Purple** #A855F7 | Native team ownership | Native cards |
| **Light Slate** #CBD5E1 | Cross-team / Multi-team | Cross-team cards |
| **Gray** #94A3B8 | Other (infra, chores, docs) | Other cards |

**These borders NEVER communicate status.**

### 2. STATUS SYMBOL + TEXT — Status ONLY

| Status | Symbol | Text Format | Usage |
|---|---|---|---|
| **Merged/Complete** | ✅ | "Merged 2026-09-16" | Completed work |
| **In Progress** | ◐ | "Pågår — [detail]" | Active work |
| **Blocked** | 🔴 | "Blockerad — [reason]" | Blocked work |
| **Unknown** | ? | "Status okänd" | Unverified work |

**Status is communicated by symbol + text, NEVER by border color.**

---

## 📦 TEXT BOX RULE — MANDATORY

**Ordinary text boxes, headers, titles, and captions:**
- fill: none / transparent
- outline: none / invisible
- border: none

A text box must NEVER receive a visible outline, border, or background merely because it contains text.

**Visible borders may ONLY be applied to:**
- Designated content cards (issue/PR cards with metadata)
- Team/category containers (Frontend, Backend, Native sections)
- Explicitly specified status components (severity indicators, risk badges)

**Headers, titles, dates, subtitles, captions, and metadata are plain text** — they must never have:
- Visible borders
- Colored fills
- Outlines or frames

Unless the slide specification in SLIDE_DETAIL_SPEC.md **explicitly** says "add border to [element]", the element MUST be plain text.

This rule prevents the exact problem seen on cover slides where text received unwanted borders.

---

## 📍 STATUS SYMBOLS — Consistent Meaning Everywhere

**ALWAYS use same symbol for same status, across all slides:**

| Symbol | Meaning | Usage | Example |
|--------|---------|-------|---------|
| ✅ | Done / Merged / Delivered | Completed work | Merged PR, finished task |
| ◐ | In Progress / Active / Doing now | Ongoing work | Open PR under review, active feature |
| 🔴 | Blocked / Critical / Stop | Urgent problem | Blocked by dependency, test failure |
| ? | Unknown / Unassigned / Unverified | Missing info | Unassigned PR, status unknown |
| → | Depends on / Waiting for / Next step | Relationship | "Waiting for #XX to merge" |

**CONSISTENCY RULE:** If you use ◐ to mean "in progress", ALWAYS use ◐ for that. Never switch symbols.

---

## ✅ MANDATORY BEFORE RENDERING

**Do not render unless:**

- [ ] Every slide has exactly: 1 header + 1 message + 1–3 blocks
- [ ] All blocks stack vertically (never horizontal/grid)
- [ ] All blocks are 100% width (never small cards)
- [ ] Spacing matches spec: 20px between, 16px inside
- [ ] Typography matches spec exactly (28/14/13/13/12pt per typography table)
- [ ] If 4+ work items exist on one topic → auto-split to continuation slide
- [ ] No nested structures, no tables, no cards
- [ ] Slide does NOT appear as dashboard, grid, or crowded

**If ANY check fails:**
- Do not render to PPTX
- Fix the content (split to continuation slide)
- Check again
- Only then render

---

## 🔗 DEPENDENCY DIAGRAMS — Mandatory visual rules

Dependency and blocker slides must use visual flow diagrams instead of paragraph-style text blocks.

### Node style
- Each issue must be shown as a separate rounded card/node
- Nodes must look like soft cards (see Soft Card Surfaces section above)
- Text must wrap inside the node
- Node size must adapt to content
- Use status markers on each node: ✅ ◐ ⏳ 🔴

### Arrows and flow
- Dependencies must be shown with arrows
- Arrow direction must clearly indicate what unlocks what
- Branching dependencies must be shown as branches, not inline prose
- Avoid crossing arrows when possible

### Layout
- Prefer left-to-right flow for short chains
- Prefer top-to-bottom flow when content becomes too wide
- Split into multiple chains if needed
- Do not compress diagram to fit too much on one slide

---

## 🚨 RENDER GATE (VISUAL CHECK)

After rendering to PPTX, page through every slide:

- [ ] Header is visible at top
- [ ] Main message is clearly readable
- [ ] Content blocks stack vertically
- [ ] No text clipping or overlap
- [ ] No blocks pushed off-slide
- [ ] Slide is NOT dense (60-70% whitespace visible)
- [ ] Work items display as clean lines (not in grid)
- [ ] Overall appearance is clean and readable

**If ANY visual check fails:**
- Do not deliver
- Fix the content
- Re-render to PPTX
- Re-check visually
- Repeat until all pass

---

**This is the only design specification. Everything else is deprecated.**

**Version:** 3.0 (Canonical layout only)  
**Status:** PRODUCTION
