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

**Each work item = ONE LINE:**
- Symbol (✅ ◐ 🔴 etc)
- Issue# and Title
- Owner/Status

**NO nested tables, NO grid, NO cards. Just clean lines.**

---

## ⚠️ EXCEPTION — SLIDE ①A MERGED OVERVIEW BOARD

Slide ①A ("Mergade PR:er") is the ONLY standard exception to the full-width block rule.

**For Slide ①A ONLY:**
- A 3 × 2 card grid IS REQUIRED
- Maximum 6 cards per slide
- Cards have identical dimensions
- Cards are read chronologically left-to-right, top-to-bottom
- Large whitespace must remain around the board
- Each card has team-colored border (teal/orange/purple/yellow/gray)
- This is a presentation summary, not a GitHub/Jira dashboard

**All other slides (①B-①E, ②, ③, etc.):**
- Continue to follow the canonical vertical full-width block layout
- NO card grids
- NO nested tables
- Only exception is ①A

---

## 📐 FIXED DIMENSIONS & TYPOGRAPHY

These values NEVER change. Use them exactly.

### Layout

| Property | Value |
|----------|-------|
| Block width | 100% of slide |
| Block height | Auto (content-driven, never compressed) |
| Spacing between blocks | 20px |
| Padding inside block | 16px |
| Line height | 1.8 (NPF standard) |
| Corner radius | None (blocks are rectangular) |

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
They NEVER represent status or priority.

| Team | Color | Hex | Usage |
|------|-------|-----|-------|
| Frontend | Teal | #2DD4BF | Card border + badge |
| Backend | Orange | #FB923C | Card border + badge |
| Native | Purple | #A855F7 | Card border + badge |
| Cross-team | Yellow | #FACC15 | Card border + badge |
| Other | Gray | #94A3B8 | Card border + badge (docs, infra, chores) |

**EXAMPLE — Frontend card on slide ①A:**
- Slide background: #0F1830
- Card background: #18233D
- Card border: #2DD4BF (teal)
- Team badge: teal
- Text: #FFFFFF
- Metadata: #94A3B8

**CRITICAL:**
Team colors and status colors are TWO DIFFERENT semantic systems.
On Slide ①A "Merged PRs": all cards already have status = MERGED.
Therefore border color represents TEAM. Do NOT add green status borders.
"Mergad" text communicates completion.

---

## 🎨 COLOR SEMANTICS — What Each Color Means

**STATUS COLORS (Indicate project status, not preferences):**

| Status | Symbol | Color | Hex | Meaning | Usage |
|--------|--------|-------|-----|---------|-------|
| **On Track** | ✅ | Green | #2ecc71 | Work completed, on schedule | Merged PRs, finished tasks |
| **In Progress** | ◐ | Orange | #ff9800 | Active work, slight delay acceptable | Ongoing features, open PRs in review |
| **Blocked/Critical** | 🔴 | Red | #e74c3c | Critical blocker, needs immediate action | Blocked issues, failed deployments |
| **Unknown/Neutral** | ? | Gray | #9e9e9e | Status unverified or not applicable | Unassigned work, dependencies |

**STRUCTURE COLORS (Non-status information):**

| Element | Meaning | Hex | Usage |
|---------|---------|-----|-------|
| **Dark Gray** | Main text, titles | #323232 | All readable content |
| **Medium Gray** | Metadata, secondary | #666666 | Assignee, timestamps, notes |
| **Light Gray** | Backgrounds, dividers | #f5f5f5 | Block backgrounds, separators |

**CRITICAL RULE:** Never use a status color (green/orange/red) unless you mean the status it represents.
If unsure, use gray or dark gray instead.

---

## 🖼️ BORDER RULES — Status Visualization

**COLORED BORDERS = STATUS ONLY**

```
🟢 GREEN BORDER (3px solid #2ecc71):
   Meaning: ON TRACK / Klart / Vi når målet
   Apply to: Completed work blocks, finished tasks
   Padding: 16px inside
   Background: Light green (5% opacity)

🟠 ORANGE BORDER (3px solid #ff9800):
   Meaning: IN PROGRESS / Slightly delayed / Not yet on track
   Apply to: Active work blocks, items needing attention
   Padding: 16px inside
   Background: Light orange (5% opacity)

🔴 RED BORDER (3px solid #e74c3c):
   Meaning: CRITICAL / Blocked / Immediate action needed
   Apply to: Blockers, failed items, urgent issues
   Padding: 16px inside
   Background: Light red (5% opacity)
```

**NEUTRAL BORDERS = INFORMATION ONLY (No status meaning)**

```
⬛ DARK BORDER (2px solid #323232):
   Meaning: Information ONLY, no status judgment
   Apply to: Headers, lists, deadlines, action items
   Padding: 16px inside
   Background: Neutral (white or light gray)

RULE: Never mix status colors with neutral information.
      One block = one message (either status OR information, not both).
```

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
