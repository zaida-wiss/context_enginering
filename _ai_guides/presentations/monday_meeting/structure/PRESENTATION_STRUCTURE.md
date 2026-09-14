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

| # | Name | Purpose |
|---|------|---------|
| - | **Framsida** | Meeting header, this week's focus | See SLIDE_DETAIL_SPEC |
| ① | **Avklarat sedan förra mötet** (1-3 slides) | What shipped this week | Merged PRs per team |
| ② | **Aktuell status** (1-3 slides) | What's in progress | Open PRs + active issues |
| ③ | **Frontend** (1-3 slides) | Frontend-specific status | Team breakdown |
| ④ | **Backend** (1-3 slides) | Backend-specific status | Team breakdown |
| ⑤ | **Native** (1-3 slides) | Native-specific status | Team breakdown |
| ⑥ | **Blockers & Dependencies** (1-2 slides) | What's blocking? | Includes code-review findings |
| ⑦ | **Risker** (1-2 slides) | What could fail? | Risk + mitigation |
| ⑧ | **Kapacitet & Estimering** (1 slide) | Do we fit in the week? | Capacity vs plan |
| ⑨ | **Prioritering & Scope** (1-2 slides) | Phase-based order (what first?) | Fas 1 → 2 → 3 |
| ⑩ | **Tekniska Beslut** (1 slide) | Architecture decisions needed | Owners for each |
| ⑪ | **Sprintmål** (1 slide) | What's the goal? | Based on capacity + priorities |
| ⑫ | **Sprintplan** (1-2 slides) | Timeline + milestones | Daily schedule + deadlines |
| ⑬ | **Nästa Steg** (1-2 slides) | Action items post-meeting | GitHub actions + owners + deadline |
| ⑭ | **Frågor till PL** (1 slide) | Open questions for PL | Scope + decisions needed |

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
**For design/layout rules → [VISUAL_DESIGN_MANDATORY.md](../design/VISUAL_DESIGN_MANDATORY.md)**  
**For data sources → [DATA_SOURCES.md](../data/DATA_SOURCES.md)**

---

**Status:** Simplified (detail moved to SLIDE_DETAIL_SPEC)  
**Last updated:** 2026-09-15
