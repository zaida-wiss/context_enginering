---
name: mandatory_reading_order
description: THE ONLY instruction — read and follow SYSTEM_CONTRACT.yaml
metadata:
  type: process
  critical: true
---

# 🚨 MANDATORY READING ORDER

## 🚨 EXECUTION ENTRY POINT

**You are here because a user asked for a presentation.**

Follow this order exactly. Do not skip.

---

## ⚠️ COMMITMENT GATE — Answer before proceeding

**This applies to ALL AI models (Claude, GPT, Gemini, Llama, etc.)**

Before you read anything else, commit to ALL of these:

- [ ] **Never guess on data.** If data is unavailable, report it as INCOMPLETE.
- [ ] **Never hallucinate.** Do not invent assignees, PR numbers, branch names, or any GitHub data.
- [ ] **Never improvise.** Do not bypass these rules because "it's faster" or "the rules seem ceremonial".
- [ ] **Never skip steps.** Follow every rule, every gate, every verification step.
- [ ] **Stop when required.** If data is incomplete or unverifiable, STOP before rendering. No presentation is better than a false presentation.
- [ ] **Never auto-shrink or hide content to make cards fit.** Use deliberate component typography from `CARD_COMPONENT_STANDARD.md`; if the card still does not fit, create continuation slides.

If you cannot commit to all of these: STOP.

---

## 0️⃣ READ INTEGRITY_CONSTRAINT.md FIRST

**Location:** [`INTEGRITY_CONSTRAINT.md`](INTEGRITY_CONSTRAINT.md)

Non-negotiable data rule: if required data cannot be obtained from registered sources, STOP.

**CRITICAL:** Capacity is MEETING DATA, not estimated data.

### PRE-MEETING mode
- Capacity may be missing.
- Show: `○ Kapacitet fastställs under mötet`.
- Never estimate hours.

### POST-MEETING mode
- Capacity must be present.
- If missing: STOP and ask team to complete meeting data.

---

## 1️⃣ READ SYSTEM_CONTRACT.yaml

**Location:** [`SYSTEM_CONTRACT.yaml`](SYSTEM_CONTRACT.yaml)

This owns:
- Authority hierarchy
- Execution sequence
- Gates
- Data validation
- Delivery rules

Follow `execution_sequence` exactly.

---

## 2️⃣ READ PRESENTATION AUTHORITIES BEFORE COMPOSITION

Before composing or rendering any slide, read these files:

1. [`design/ACCESSIBILITY_NEURODIVERSITY.md`](design/ACCESSIBILITY_NEURODIVERSITY.md)
2. [`design/VISUAL_DESIGN_MANDATORY.md`](design/VISUAL_DESIGN_MANDATORY.md)
3. [`design/CARD_COMPONENT_STANDARD.md`](design/CARD_COMPONENT_STANDARD.md) — **authoritative for card internals, metadata sizes, spacing and timestamps**
4. [`monday_meeting/design/LAYOUT_OVERFLOW_GUARD.md`](monday_meeting/design/LAYOUT_OVERFLOW_GUARD.md)
5. [`monday_meeting/design/SLIDE_DETAIL_SPEC.md`](monday_meeting/design/SLIDE_DETAIL_SPEC.md)
6. [`monday_meeting/design/TEMPLATE_REFERENCE.html`](monday_meeting/design/TEMPLATE_REFERENCE.html) — **REFERENCE ONLY**

### Authority for layout conflicts

If content/layout instructions conflict, use this order:

1. Accessibility boundaries / WCAG contrast and legibility
2. Visual design theme and global slide geometry
3. Card component standard for card internals and compact typography
4. Overflow/pagination guard
5. Slide content specification
6. Template reference (never authoritative)

### Mechanical fit rule

For cards, fitting all required rows is mandatory.

Use the deliberate size ranges and spacing hierarchy in `CARD_COMPONENT_STANDARD.md` first:

- timestamp/evidence may be reduced first
- review/merged/branch metadata may be reduced next
- owner/team may use the compact owner size
- title remains visually dominant
- use even, natural vertical rhythm; do not distribute rows across the whole card height
- timestamp anchors at lower-left where applicable

If content still cannot fit within the permitted component sizes:

- Create continuation slide.
- Do NOT use PowerPoint shrink-to-fit / auto-reduce-font.
- Do NOT clip text.
- Do NOT overlap text.
- Do NOT omit required rows.
- Do NOT create large irregular whitespace merely to preserve oversized metadata.

Grid layouts are allowed only where explicitly approved by the overflow guard.

---

## 3️⃣ FOLLOW EXECUTION_SEQUENCE FROM SYSTEM_CONTRACT.yaml

Continue from `SYSTEM_CONTRACT.yaml` and execute each step in order.

---

## REGISTERED DATA SOURCES & ACCESS PATHS

### Required Dataset 1: team_roster
- Source: GITHUB_TEAM_ROSTER
- Access: local file `_memory/TEAM_ROSTER.md`
- Missing → STOP

### Required Dataset 2: merged_prs
- Source: GITHUB_MERGED_PRS
- Preferred access: GitHub REST API / GitHub Connector
- Use only registered fallback order from `EXTERNAL_SOURCES.yaml`
- All fallbacks fail → INCOMPLETE → build gate decides STOP

### Required Dataset 3: active_issues
- Source: GITHUB_OPEN_ISSUES
- Preferred access: GitHub REST API / GitHub Connector
- Use only registered fallback order from `EXTERNAL_SOURCES.yaml`
- All fallbacks fail → INCOMPLETE → build gate decides STOP

---

## FORBIDDEN IMPLEMENTATIONS

Do not use:
- Shell network commands (`git clone`, `git fetch`, `curl`, `wget`)
- Generic web search
- Unregistered URLs/sources
- Model knowledge as source

---

## CRITICAL: Data Completeness

Presentation rendering proceeds only if all required datasets pass the build gate.

- team_roster incomplete → STOP
- merged_prs incomplete → STOP
- active_issues incomplete → STOP

---

## CRITICAL: Render Completeness

A deck is NOT deliverable merely because the generator completed.
The rendered PPTX/PDF must pass artifact inspection.

Mandatory zero-count checks before delivery:

```text
text_overlap_count == 0
card_overlap_count == 0
text_outside_card_count == 0
text_clipping_count == 0
out_of_bounds_element_count == 0
unapproved_grid_slide_count == 0
font_below_component_minimum_count == 0
missing_required_card_row_count == 0
uneven_row_spacing_caused_by_vertical_justification == 0
```

If any check is non-zero:
1. STOP delivery.
2. Apply the compact component hierarchy / add continuation slides.
3. Rerender.
4. Reinspect the artifact.

---

## NEXT STEP

Go to [`SYSTEM_CONTRACT.yaml`](SYSTEM_CONTRACT.yaml), then follow the authority files above before rendering.
