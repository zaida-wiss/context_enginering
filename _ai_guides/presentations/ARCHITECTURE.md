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
- Grid dimensions (3 columns × 2 rows for ①A merged overview, full-width blocks for ①B-①D)
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
- Backend: #FF4FA3 (hot pink)
- Native: #A855F7 (purple)
- Cross-team: #CBD5E1 (light slate, WCAG compliant)

**Slide Layouts:**
- ①A: Merged PRs — 3×2 card grid (6 max) with team-colored borders
- ①B: Collection branch merges — full-width stacked cards (Java-Development-Environment, C/C++-Native, etc.)
- ①C: Pågår by team — full-width stacked cards (Frontend, Backend, Native, each team section)
- ①D: Pågår Cross-team — full-width stacked cards (work affecting multiple teams)

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

---

## 📍 FILE PLACEMENT GUIDE — Where Information Lives

**This section tells AI WHERE to put new information and WHEN to update existing files.**

### TIER 1 FILES — Never Create New, Always Update Existing

These files are **authoritative sources**. Do NOT create alternatives. When you need to add information, UPDATE these files.

| File | Owns | When to Update | How to Update |
|------|------|---|---|
| **VISUAL_DESIGN_MANDATORY.md** | ALL visual rules (colors, typography, spacing, borders, grids) | User wants to change colors, fonts, layout | Edit the relevant section; never create "VISUAL_DESIGN_V2.md" |
| **ACCESSIBILITY_NEURODIVERSITY.md** | WCAG/NPF boundaries (contrast, readability, symbol consistency) | Need to define new accessibility requirement | Add to the appropriate section; WCAG 2.2 AA is binding |
| **SLIDE_DETAIL_SPEC.md** | Content blueprint (what data goes where, card format) | Need to define new slide type or change card structure | Edit the slide section; do NOT add color/font rules (those go to VISUAL_DESIGN) |
| **DATA_ACQUISITION_CONTRACT.yaml** | Data collection method (canonical algorithm, no interpretation) | Need to add new data source or change collection | Add new `dataset` section; reference authority hierarchy |
| **ACTIVE_WORK_DETECTION_MODEL.md** | Evidence hierarchy for determining "what is someone working on?" | Need to add new detection signal or change priority | Edit the evidence levels; update algorithm section |
| **SYSTEM_CONTRACT.yaml** | Execution sequence, gates, authority conflicts, entity rules | Need to add new rule, gate, or policy | Add new top-level section; reference other files as needed |

---

### TIER 2 FILES — Reference Files (Supporting, Not Authoritative)

These files REFERENCE tier-1 files. They explain, visualize, or summarize tier-1 rules. Do NOT store original rules here.

| File | Purpose | When to Update | How to Update |
|------|---------|---|---|
| **TEMPLATE_REFERENCE.html** | Visual mockup showing VISUAL_DESIGN_MANDATORY rules in action | VISUAL_DESIGN_MANDATORY changes | Re-render mockup to show new colors/layout |
| **DATA_COLLECTION_MANDATORY.md** | Checklist/validation based on DATA_ACQUISITION_CONTRACT | DATA_ACQUISITION_CONTRACT changes | Update checklist items; add validation rules |
| **RENDER_GATE_CHECKLIST.md** | Pre-rendering verification based on all tier-1 files | New rules added to VISUAL_DESIGN, ACCESSIBILITY, or DATA | Add new checkboxes; reference tier-1 files |

---

### DIRECTORY STRUCTURE — Where Each Type Lives

```
_ai_guides/presentations/

├─ MANDATORY_READING_ORDER.md          (entry point — NEVER modified)
├─ SYSTEM_CONTRACT.yaml                (execution + authority — TIER 1)
├─ ARCHITECTURE.md                     (this file — how system is organized)
│
├─ data/
│  ├─ DATA_SOURCES.md                  (where sources are, not how to fetch)
│  ├─ DATA_ACQUISITION_CONTRACT.yaml   (HOW to fetch — TIER 1)
│  ├─ ACTIVE_WORK_DETECTION_MODEL.md   (evidence hierarchy — TIER 1)
│  └─ (no other data-collection files should exist)
│
├─ design/
│  ├─ VISUAL_DESIGN_MANDATORY.md       (all visual rules — TIER 1)
│  ├─ ACCESSIBILITY_NEURODIVERSITY.md  (WCAG/NPF — TIER 1)
│  ├─ TEMPLATE_REFERENCE.html          (mockup visualization — TIER 2)
│  └─ (no other design files; PRESENTATION_STYLE.md is deprecated)
│
├─ monday_meeting/
│  ├─ design/
│  │  ├─ SLIDE_DETAIL_SPEC.md          (content per slide — TIER 1)
│  │  └─ (no other slide-spec files)
│  │
│  ├─ data/
│  │  ├─ DATA_COLLECTION_MANDATORY.md  (validation checklist — TIER 2)
│  │  └─ (no other data-validation files)
│  │
│  └─ structure/
│     └─ PRESENTATION_STRUCTURE.md     (14 meeting points — reference only)
│
└─ verification/
   ├─ RENDER_GATE_CHECKLIST.md         (pre-render verification — TIER 2)
   └─ (no other verification files)
```

**IF YOU FIND OTHER FILES IN THESE DIRECTORIES:**
- PRESENTATION_STYLE.md → deprecated, info is in VISUAL_DESIGN_MANDATORY.md
- DESIGN_AUTHORITY.md → deprecated, info is in SYSTEM_CONTRACT.yaml
- *_v2.md, *_UPDATED.md, etc. → delete and consolidate into tier-1 file

**MAINTENANCE REMINDER:**
Every 4 weeks, run FILE_CONSISTENCY_AUDIT (defined in SYSTEM_CONTRACT.yaml).
This prevents context-bloat and conflicting files.

**DEPRECATION PROCESS:**
If a file is no longer used:
1. Add deprecation header at top (see template below)
2. Copy unique content to tier-1 replacement
3. Keep for 2 weeks (grace period)
4. Delete permanently after 2 weeks
5. Never keep alternative versions

---

### HOW TO ADD NEW INFORMATION

**Scenario 1: New slide type (e.g., "①⑬ Risk Assessment")**

1. WHERE: SLIDE_DETAIL_SPEC.md — add new section `## 📊 ①⑬ RISK ASSESSMENT`
2. WHAT: Define content format, required fields, data source
3. DO NOT: Add visual rules here
4. THEN: If new visuals needed, update VISUAL_DESIGN_MANDATORY.md
5. THEN: If new data needed, update DATA_ACQUISITION_CONTRACT.yaml

**Scenario 2: New color or typography rule**

1. WHERE: VISUAL_DESIGN_MANDATORY.md — add to relevant section
2. WHAT: Define exact hex value, usage, contrast ratio
3. WHY: Add context (e.g., "for new risk-severity indicator")
4. DO NOT: Mention this color in SLIDE_DETAIL_SPEC.md
5. THEN: Update TEMPLATE_REFERENCE.html to show the new color

**Scenario 3: New data source needed**

1. WHERE: DATA_ACQUISITION_CONTRACT.yaml — add new `dataset:` section
2. WHAT: Define canonical method, fallback order, required fields, correlation logic
3. WHO: Is this data tied to a specific slide? Reference SLIDE_DETAIL_SPEC.md
4. WHY: Is this data needed for active work detection? Add to ACTIVE_WORK_DETECTION_MODEL.md
5. DO NOT: Create a separate "DATA_SOURCES_NEW.md"

**Scenario 4: New accessibility boundary (e.g., "all borders must be 3:1 contrast")**

1. WHERE: ACCESSIBILITY_NEURODIVERSITY.md — add to "MANDATORY — WCAG 2.2 AA" section
2. WHAT: Define the rule + contrast ratio + why
3. THEN: Update VISUAL_DESIGN_MANDATORY.md to implement this boundary
4. THEN: Update RENDER_GATE_CHECKLIST.md with a checkbox

**Scenario 5: Need to change existing rule**

1. FIND: Which tier-1 file owns this rule?
2. VERIFY: Check SYSTEM_CONTRACT.yaml authority hierarchy — does this file own it?
3. UPDATE: Edit the tier-1 file directly
4. PROPAGATE: Update all tier-2 files that reference it
5. DO NOT: Create alternative versions or work-arounds

---

### CONSISTENCY CHECKS FOR AI

**Before writing or editing any file, ask yourself:**

```
[ ] Is this information already defined elsewhere?
    If yes → edit that file, don't create a new one
    
[ ] Does this file own this type of information?
    Check SYSTEM_CONTRACT.yaml authority hierarchy
    If no → add it to the file that owns it
    
[ ] Am I creating a *_v2 or alternative file?
    If yes → STOP. Consolidate into existing tier-1 file instead
    
[ ] Does this change affect other files?
    - Visual rule change → check TEMPLATE_REFERENCE.html
    - Data rule change → check RENDER_GATE_CHECKLIST.md
    - Accessibility rule change → check VISUAL_DESIGN_MANDATORY.md
    
[ ] Am I adding rules to SLIDE_DETAIL_SPEC.md?
    If they're visual (color, font, spacing) → move to VISUAL_DESIGN_MANDATORY.md
    If they're accessibility → move to ACCESSIBILITY_NEURODIVERSITY.md
    If they're data-related → reference DATA_ACQUISITION_CONTRACT.yaml
```

---

### WHAT TO DO WITH DEPRECATED FILES

When you find old/redundant files:

1. **IDENTIFY:** Which tier-1 file now owns this information?
2. **MIGRATE:** Copy any unique content to the tier-1 file
3. **CONSOLIDATE:** If information is duplicated, keep only tier-1 version
4. **DELETE:** Remove the deprecated file
5. **COMMIT:** "chore: consolidate [OLD_FILE] into [TIER_1_FILE]"

**Example:**
- Found: `PRESENTATION_STYLE.md` (deprecated)
- Owner: `VISUAL_DESIGN_MANDATORY.md`
- Action: Delete `PRESENTATION_STYLE.md`, reference is now in VISUAL_DESIGN_MANDATORY.md

---

### AUTHORITY HIERARCHY APPLIED TO FILE PLACEMENT

If TWO files claim the same responsibility:

1. Check SYSTEM_CONTRACT.yaml `authority` section
2. Higher-level file wins
3. Lower-level file becomes reference/validation only
4. DO NOT maintain both as alternatives

**Example:** If both SLIDE_DETAIL_SPEC.md and VISUAL_DESIGN_MANDATORY.md say "Backend is orange":
- VISUAL_DESIGN_MANDATORY.md wins (TIER 1, owns HOW)
- SLIDE_DETAIL_SPEC.md updates to reference it (TIER 2)
- Result: One source of truth

---

## 🗑️ DEPRECATION HEADER TEMPLATE

When a file is superseded, add this header immediately after the frontmatter:

```markdown
---
name: old_filename
description: [old description]
metadata:
  type: [type]
  status: DEPRECATED
---

🚨 **DEPRECATED** — This file is no longer maintained.

**Reason:** [Brief reason why this file is no longer used]

**See instead:** 
- [`NEW_FILE.md`](path/to/NEW_FILE.md) — [why this file is authoritative now]
- [`ANOTHER_FILE.md`](path/to/ANOTHER_FILE.md) — [other relevant files]

**Grace period:** This file will be deleted [DATE]. Copy any unique content to 
[NEW_FILE.md] before then.

**Git history:** If you need old content, check `git log -- old_filename.md`

---

[Rest of old file content below — DO NOT EDIT]
```

**Example (real deprecation):**
```markdown
🚨 **DEPRECATED** — This file is no longer maintained.

**Reason:** Visual design rules moved to single authoritative source.

**See instead:**
- [`VISUAL_DESIGN_MANDATORY.md`](../design/VISUAL_DESIGN_MANDATORY.md) — all visual rules
- [`TEMPLATE_REFERENCE.html`](../design/TEMPLATE_REFERENCE.html) — visual mockups

**Grace period:** This file will be deleted 2026-10-01. All unique content 
has been consolidated into VISUAL_DESIGN_MANDATORY.md.

---
```

---

## 🔍 CONFLICT DETECTION QUICK REFERENCE

**Before any edit, grep for these patterns:**

```bash
# Find duplicate color definitions
grep -r "#[0-9A-Fa-f]{6}" _ai_guides/presentations/ | sort | uniq -d

# Find duplicate font sizes
grep -r "[0-9]\+pt" _ai_guides/presentations/ | sort | uniq -d

# Find multiple files claiming same responsibility
grep -r "TEAM COLORS" _ai_guides/presentations/
grep -r "Backend.*orange\|orange.*Backend" _ai_guides/presentations/

# Find all *_v2, *_OLD, *_DEPRECATED files
find _ai_guides/presentations/ -name "*_v[0-9]*" -o -name "*_OLD*" -o -name "*_BACKUP*"
```

If grep finds duplicates → run FILE_CONSISTENCY_AUDIT immediately.
