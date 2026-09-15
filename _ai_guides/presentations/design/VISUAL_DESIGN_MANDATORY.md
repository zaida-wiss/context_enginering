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
| Slide header (meeting point ①②③) | 28pt | BOLD | #323232 (dark gray) |
| Section header (Frontend, Backend, etc) | 14pt | BOLD | #323232 |
| Main message | 13pt | Regular | #323232 |
| Work item title | 13pt | Regular | #323232 |
| Owner/Status | 12pt | Regular | #666666 (medium gray) |

---

## 🎨 COLOR PALETTE

Semantic colors for status indication (Symbol + Color + Text together):

| Status | Symbol | Color | RGB | Usage |
|--------|--------|-------|-----|-------|
| Done/Merged | ✅ | Green | 76, 175, 80 | Completed work |
| In Progress | ◐ | Orange | 255, 152, 0 | Active work |
| Waiting/Blocked | ⏳ 🔴 | Orange/Red | 255, 152, 0 / 244, 67, 54 | Blocked or review |
| Unknown/Closed | 🔵 | Gray | 200, 200, 200 | Closed or unknown |

**RULE:** Color carries semantic meaning. Always combine Symbol + Color + Text.

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
