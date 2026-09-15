---
name: presentation_structure
description: 14 meeting points (①-⑭) — the narrative flow and why order matters
metadata:
  type: reference
  critical: false
---

# 📋 PRESENTATION STRUCTURE — 14 Mötespunkter (①-⑭)

**This file defines the logical flow. For details, see [SLIDE_DETAIL_SPEC.md](../design/SLIDE_DETAIL_SPEC.md)**

---

## The 14 Meeting Points in Order

| # | Name | Purpose | Slide Count |
|---|------|---------|------|
| - | **Framsida** | Meeting header, this week's focus | 1 |
| ① | **Avklarat sedan förra mötet** | Merged PRs + closed issues + active issues + branches + commits (ALL verified activity per team) | 1+ (auto-split: ①A, ①B, ①C, ①D, ①E as needed) |
| ② | **Nuläge & Deadline** | Progress bars + deadline tracker with risk/actions | 1 |
| ③ | **Frontend** | Frontend-specific detailed status & impediments | 2-3 |
| ④ | **Backend** | Backend-specific detailed status & impediments | 2-3 |
| ⑤ | **Native** | Native-specific detailed status & impediments | 2-3 |
| ⑥ | **Blockers & Dependencies** | What's blocking progress? | 1-2 |
| ⑦ | **Risker** | What could fail? Risk matrix + mitigations | 1-2 |
| ⑧ | **Kapacitet & Estimering** | Do we fit? Capacity vs sprint plan | 1 |
| ⑨ | **Prioritering & Scope** | Phase-based prioritization (1→2→3) | 1-2 |
| ⑩ | **Tekniska Beslut** | Architecture decisions needed this week | 1 |
| ⑪ | **Sprintmål** | Sprint goal + success criteria | 1 |
| ⑫ | **Sprintplan** | Timeline, milestones, daily schedule | 1-2 |
| ⑬ | **Nästa Steg** | Post-meeting action items → GitHub | 1-2 |
| ⑭ | **Frågor till PL** | Open questions needing PL decision | 1 |

---

## Why This Order?

**The flow answers these questions in sequence:**

1. ① What happened? (Retrospect → shows delivery)
2. ② What's next? (Current state → shows progress)
3. ③-⑤ Who's working on what? (Team breakdown → shows ownership)
4. ⑥-⑦ What's stopping us? (Blockers + risks → shows constraints)
5. ⑧-⑨ Can we do this? (Capacity + prioritization → shows feasibility)
6. ⑩-⑫ How will we do this? (Technical + timeline → shows plan)
7. ⑬-⑭ What's next? (Actions + questions → shows execution)

---

## Key Rules

**One meeting point ≠ one slide**
- A point may be 1-3 slides, depending on data
- Presentation will have 15-30 slides per week
- All slides marked with ① ② ③ etc. to show which point they belong to

**For exact content of each slide → [SLIDE_DETAIL_SPEC.md](../design/SLIDE_DETAIL_SPEC.md)**  
**For design/layout rules → [VISUAL_DESIGN_MANDATORY.md](../../design/VISUAL_DESIGN_MANDATORY.md)**  
**For data sources → [DATA_SOURCES.md](../data/DATA_SOURCES.md)**

---

## Modular Composition Architecture

**Each meeting point (①-⑭) is a composable module that can be rendered independently, then assembled into final presentation.**

### Module Dependencies

```
Framsida (no dependencies)
  ↓
① Avklarat (depends on: GitHub data, team roster)
  ↓
② Nuläge (depends on: ①, deadline/sprint data)
  ↓
③④⑤ Teams (each depends on: ①, same deadline/sprint data)
  ↓
⑥⑦ Blockers+Risks (depend on: ③④⑤)
  ↓
⑧⑨ Capacity+Prioritization (depend on: ③④⑤, sprint data)
  ↓
⑩ Tech Decisions (independent of other modules)
  ↓
⑪ Sprint Goal (depends on: ①-⑨)
  ↓
⑫ Sprint Plan (depends on: ⑪)
  ↓
⑬ Next Steps (depends on: ⑫)
  ↓
⑭ Questions (independent of other modules)
```

### Required vs Optional Modules

**REQUIRED (presentation cannot render without these):**
- ① Avklarat (must show verified activity)
- ③④⑤ Teams (must show all 3 team breakdowns)
- ⑪ Sprint Goal (must have documented goal)

**OPTIONAL (may be empty or skipped if data unavailable):**
- ⑥ Blockers (empty state: "Inga identifierade blockers denna vecka")
- ⑦ Risks (empty state: "Inga kända risker denna vecka")
- ⑩ Tech Decisions (empty state: "Inga beslut krävda denna vecka")
- ⑭ Questions (empty state: "Ingen input från team")

**PRESENTATION RULES:**
- If ANY required module fails → presentation STOPS (do not render)
- If optional module fails → render as empty state with ⚠️ marker
- Framsida always renders (header slide)

### Shared Data Inputs

**These data sources are fetched ONCE and shared by multiple modules:**

| Data | Modules Using | Cached By |
|------|---------------|-----------|
| GitHub PRs/issues/commits | ①②③④⑤⑥⑦⑧⑨⑪⑫ | DATA_AUDIT (shared across all) |
| Team roster + GitHub handles | ①③④⑤⑧⑨⑪ | TEAM_ROSTER.md (local) |
| Sprint dates + deadlines | ②⑧⑨⑪⑫ | External source (Sheets/Board/Issues) |
| Project board status | ②⑥⑦⑧⑨ | External source (GitHub Projects/Board) |

**Key rule:** Data is acquired ONCE per execution (step_2 of SYSTEM_CONTRACT), not re-fetched per module.

### Module-Level Render Gates

**Before rendering each module, verify:**

| Module | Must Verify | Failure Behavior |
|--------|------------|-----------------|
| ① | GitHub data complete + all team members checked | STOP (required) |
| ② | Sprint dates exist + deadline tracker data present | STOP (required) |
| ③④⑤ | Team has activity OR explicitly zero data | STOP if no team roster (required) |
| ⑥ | Blocker identification method functional | Render empty state if none found (optional) |
| ⑦ | Risk assessment data available | Render empty state if none found (optional) |
| ⑧ | Capacity/velocity data present | STOP (required for sprint planning) |
| ⑨ | Prioritization schema defined | STOP (required) |
| ⑩ | Tech decision list exists | Render empty state if none (optional) |
| ⑪ | Sprint goal documented | STOP (required) |
| ⑫ | Timeline + milestones defined | STOP (required) |
| ⑬ | Action items from ⑫ exist | Render with standard template if none (optional) |
| ⑭ | Open questions submitted | Render empty state if none (optional) |

### Skip Semantics & Empty States

**When module data is missing or incomplete:**

```
REQUIRED module with missing data:
  → STOP rendering entire presentation
  → Report: "Module ① failed: GitHub data incomplete"

OPTIONAL module with missing data:
  → Render as empty state slide
  → Format: "⑦ Risker\n\n⚠️ Inga identifierade risker denna vecka"
  → Still counts as rendered slide (maintains slide numbering)
```

### Composition Order (Rendering)

1. Fetch + audit ALL shared data (DATA_AUDIT gate)
2. Render Framsida (no dependencies)
3. Render ① (required, gates ②)
4. Render ②-⑤ in parallel (all depend on ①)
5. Render ⑥-⑨ in parallel (depend on ③④⑤)
6. Render ⑩ (independent)
7. Render ⑪-⑫ in sequence (⑪ → ⑫)
8. Render ⑬ (depends on ⑫)
9. Render ⑭ (independent)
10. RENDER_GATE verifies all modules + assembly
11. Assemble all modules into final PDF

### Verification Checklist (before delivery)

**Before assembling final presentation, verify:**

- [ ] All required modules (①②③④⑤⑧⑨⑪⑫) rendered successfully
- [ ] All optional modules either rendered or marked with ⚠️
- [ ] No module data leaked between teams/contexts
- [ ] Slide numbering continuous (①①A①B②③... etc)
- [ ] All slides have correct meeting-point symbol at start
- [ ] DATA_AUDIT checksums match slides (no data lost/added)
- [ ] Visual render gate passed (VISUAL_DESIGN_MANDATORY checked)
- [ ] Total slide count 15-30 (reasonable for 90-min meeting)

---

**Status:** Simplified (detail moved to SLIDE_DETAIL_SPEC)  
**Last updated:** 2026-09-15
