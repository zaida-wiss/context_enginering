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

**Status:** Simplified (detail moved to SLIDE_DETAIL_SPEC)  
**Last updated:** 2026-09-15
