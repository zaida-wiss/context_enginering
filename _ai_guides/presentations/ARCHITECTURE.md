---
name: presentation_architecture
description: Design architecture — Single Source of Truth for presentation system
metadata:
  type: critical_specification
  version: 1.0
---

# 📐 PRESENTATION ARCHITECTURE — Design Authority Hierarchy

**This document establishes where each design decision lives and how information flows.**

---

## 🎯 Single Source of Truth (SSOT)

### TIER 1: VISUAL_DESIGN_MANDATORY.md (Master Authority)
**Owns:** All visual design rules that apply to every slide
- Colors (theme + team + status)
- Typography (font sizes, weights, colors)
- Layout (full-width blocks, card grids, spacing, margins, padding)
- Component structure (cards, borders, badges)
- Dark navy theme (#0F1830) — MANDATORY on all slides
- Grid dimensions (3 columns × 4 rows for ①A-①C)
- Exceptions (①A is the ONLY card-grid exception to full-width blocks)

**When to update:** Whenever a design rule changes (colors, layout, typography)
**Impact:** Changes here ripple to TEMPLATE_REFERENCE.html and SLIDE_DETAIL_SPEC.md

**AI Guidance:** If you need to know how something should LOOK or be POSITIONED, read VISUAL_DESIGN_MANDATORY.md first.

---

### TIER 2: SLIDE_DETAIL_SPEC.md (Content Authority)
**Owns:** What content goes on each slide and in what order
- Slide purpose
- Card format and data fields
- Sort order (chronological vs. team-based)
- Mandatory content per card (#, title, branch, assignee, etc.)
- Exclusions (what NOT to show)

**References:** VISUAL_DESIGN_MANDATORY.md for "how to display"

**When to update:** When content requirements change (e.g., "add branch info to cards")
**Impact:** Changes here affect DATA_ACQUISITION_CONTRACT.yaml (what data to fetch)

**AI Guidance:** If you need to know WHAT goes on a slide, read SLIDE_DETAIL_SPEC.md. If you need to know HOW to display it, see VISUAL_DESIGN_MANDATORY.md.

---

### TIER 3: TEMPLATE_REFERENCE.html (Visual Implementation)
**Owns:** Visual mockups showing how VISUAL_DESIGN_MANDATORY.md rules look in practice
- Working HTML/CSS examples of ①A, ①B, ①C
- Shows dark navy theme in action
- Shows card grids with team colors
- Shows team columns with team borders
- Is a REFERENCE, not a live template

**Updates when:** VISUAL_DESIGN_MANDATORY.md changes
**DOES NOT override:** Rules in VISUAL_DESIGN_MANDATORY.md (reference only)

**AI Guidance:** If you need to SEE how cards should look, open TEMPLATE_REFERENCE.html. But if there's a conflict between the HTML and VISUAL_DESIGN_MANDATORY.md, VISUAL_DESIGN_MANDATORY.md wins.

---

### TIER 4: DATA_ACQUISITION_CONTRACT.yaml (Data Authority)
**Owns:** How to fetch and structure data for slides
- Which GitHub API endpoints to call
- What fields to include
- How to filter (chronological, team-based, cross-team)
- Fallback sources

**References:** SLIDE_DETAIL_SPEC.md for "what fields are needed"

**AI Guidance:** If you need to know what DATA to fetch, read DATA_ACQUISITION_CONTRACT.yaml. It tells you the HOW; SLIDE_DETAIL_SPEC.md tells you the WHAT.

---

## 🔄 Information Flow

```
VISUAL_DESIGN_MANDATORY.md (colors, layout, grid, typography)
    ↓
TEMPLATE_REFERENCE.html (visualizes the rules)
    ↓
SLIDE_DETAIL_SPEC.md (references both for display rules + content)
    ↓
DATA_ACQUISITION_CONTRACT.yaml (fetches the data)
```

---

## ✅ Consistency Rules for AI

1. **If adding a new color:** Define it in VISUAL_DESIGN_MANDATORY.md, show it in TEMPLATE_REFERENCE.html
2. **If adding a new field to a card:** Update SLIDE_DETAIL_SPEC.md and DATA_ACQUISITION_CONTRACT.yaml
3. **If changing a card layout:** Update VISUAL_DESIGN_MANDATORY.md first, then TEMPLATE_REFERENCE.html
4. **If conflicted:** VISUAL_DESIGN_MANDATORY.md always wins (it's the master)

---

## 📋 Current Design State (as of 2026-09-16)

**Dark Navy Theme (MANDATORY):**
- Slide background: #0F1830
- Card background: #18233D
- Dividers: #334155
- Text: #FFFFFF, #CBD5E1, #94A3B8

**Team Colors (Borders only):**
- Frontend: #2DD4BF (teal)
- Backend: #FB923C (orange)
- Native: #A855F7 (purple)
- Cross-team: #000000 (svart/neutral)

**Grid Layout (①A-①C):**
- 3 columns × 4 rows = max 12 cards per slide
- Card border shows team ownership
- Status shown via symbol + text (✅ Merged, ◐ Pågår, etc.)

**Slides:**
- ①A: Merged PRs (chronological, all teams mixed)
- ①B: Pågår by team (Frontend | Backend | Native columns)
- ①C: Pågår Cross-team (separate slide, svart borders)

---

## 🚀 How to Update the System

**Scenario 1: Change a color**
1. Edit VISUAL_DESIGN_MANDATORY.md
2. Update TEMPLATE_REFERENCE.html to show the new color
3. Commit both together

**Scenario 2: Add a new field to cards**
1. Update SLIDE_DETAIL_SPEC.md (add field to card format)
2. Update DATA_ACQUISITION_CONTRACT.yaml (add to data fetch)
3. Update TEMPLATE_REFERENCE.html to show the new field
4. Commit all three together

**Scenario 3: Change grid layout**
1. Update VISUAL_DESIGN_MANDATORY.md (new grid dimensions)
2. Update SLIDE_DETAIL_SPEC.md (max cards per slide changes)
3. Update TEMPLATE_REFERENCE.html (show new layout)
4. Commit all together

**Golden Rule:** Changes never travel one way. If you update one tier, check the others.
