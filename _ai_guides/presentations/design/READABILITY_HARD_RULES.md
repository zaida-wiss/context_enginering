---
name: readability_hard_rules
description: MANDATORY — fixed slide-title size, larger text minima, spacing, pedagogical microcopy and dependency-aware ordering
metadata:
  type: design-specification
  critical: true
  required_before: composition
  version: 1.0
---

# READABILITY HARD RULES

This file is a hard authority for readability and meeting usability. It supplements the existing accessibility, visual, card and Monday-meeting specifications.

If a lower-level example conflicts with this file, this file wins for the rules below. WCAG 2.2 AA remains the absolute boundary.

## 1. SLIDE TITLES MUST NOT SHRINK

Slide titles / meeting-point headers use a normal fixed presentation size.

Hard rules:
- preferred and minimum slide-title size: **36 pt**, bold
- slide titles are **never** a fit variable
- do not shrink a slide title because the slide is crowded
- do not use automatic shrink-to-fit on slide titles

If a title does not fit at 36 pt:
1. shorten the wording without losing meaning
2. widen/reposition the title zone
3. reduce slide content density
4. create a continuation slide

Never reduce the title below 36 pt to preserve content density.

## 2. NORMAL TEXT STARTS LARGER

Normal presentation text should start larger than the minimum.

Use this fit principle:
1. start at the preferred size
2. reduce only if required to fit
3. reduce stepwise, never below the role minimum
4. if the minimum still does not fit, change geometry/density or paginate

Recommended normal body/supporting text start: **15 pt** when the role/layout permits.

For card-internal roles, these minima override older lower values:
- pedagogical/project-value explanation: **13 pt minimum**
- assignee/developer + team: **13 pt minimum**
- operational metadata: **11 pt minimum**
- timestamp/source microcopy: **11 pt minimum**
- card title remains **18 pt minimum**

A technically fitting smaller size is not a reason to use it. Use the largest comfortable size that fits the layout.

## 3. MINIMUM BLOCK SPACING IS LARGER

Semantic text blocks must remain visually separated.

Minimum rendered gaps:
- title → pedagogical explanation: **4 px minimum**, **6 px preferred**
- explanation → assignee/developer: **12 px minimum**
- assignee/developer → operational metadata: **8 px minimum**
- separate metadata row → next metadata row: **6 px minimum**
- operational metadata → timestamp/source area: **10 px minimum**

Wrapped lines inside one text block use natural line height. Never compress line height until the text looks crowded.

If these gaps do not fit:
- increase card height
- reduce cards per slide
- paginate

Do not solve fit by shrinking below these spacing minima.

## 4. PEDAGOGICAL MICROCOPY IS REQUIRED

Every action/work card that asks the team to do something must explain the project value, not only name the task.

Especially on `⑬ Nästa steg`, every card must answer directly under the title:
1. **Vad gäller detta?**
2. **Vad tillför det projektet / varför är det viktigt?**

This applies to:
- team-confirmed facts/actions
- `🔎 AI-analys`
- `⭐ AI-förslag`

Example:

```text
Fatta CI-beslut i #115
Avgör om lint, tester och build ska kontrolleras automatiskt i GitHub. Det minskar risken att fel kod mergas till develop.

⭐ AI-förslag
Ansvar: Hela teamet
```

If source evidence does not support the claimed project value, use neutral wording or mark the interpretation as AI-derived according to provenance rules. Never invent impact.

## 5. DEPENDENCIES MUST DRIVE ORDER

When verified dependencies exist, the presentation must make the suggested sequence visible.

The planning output should show, when evidence permits:
- **Först** — work that unlocks another item/team or removes a blocker
- **Parallellt** — independent work that can proceed safely
- **Därefter / vänta** — work dependent on unfinished prerequisites
- **Varför** — the blocker/dependency/deadline/core-flow reason

If the ordering is model-derived rather than already team-confirmed:
- reasoning uses `🔎 AI-analys`
- proposed sequence uses `⭐ AI-förslag — planeringsordning`

Example:

```text
⭐ AI-förslag — planeringsordning
1. Först: Lås API-kontraktet
   Varför: behövs för stabil Frontend/Backend-integration.
2. Parallellt: Verifiera JNA-minimiflödet
   Varför: låser Backend/Native-kopplingen.
3. Därefter: beroende integrationsarbete
   Varför: ska inte startas innan kontrakten/minimiflödet är verifierade.
```

The dependency graph and blocker slides must feed this ordering. Do not list a blocker without letting it influence the plan when it materially affects sequence.

## 6. RENDER / COMPOSITION FAILURE CONDITIONS

The deck fails when any of these are non-zero:

```text
slide_title_below_36pt_count > 0
slide_title_shrunk_for_fit_count > 0
body_text_below_role_minimum_count > 0
card_block_spacing_violation_count > 0
next_step_card_missing_project_value_microcopy_count > 0
verified_dependency_not_reflected_in_plan_count > 0
```

Fix by changing wording, geometry, density or pagination — not by shrinking titles or compressing text.

## CORE PRINCIPLE

**Readability and pedagogical clarity win over squeezing more information onto one slide.**

---

**Status:** PRODUCTION
**Version:** 1.0
**Last updated:** 2026-09-17
