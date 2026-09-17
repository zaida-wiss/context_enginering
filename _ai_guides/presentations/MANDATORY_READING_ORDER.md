---
name: mandatory_reading_order
description: THE ONLY instruction — read and follow SYSTEM_CONTRACT.yaml
metadata:
  type: process
  critical: true
---

# 🚨 MANDATORY READING ORDER

## EXECUTION ENTRY POINT

Before creating any presentation, follow this order exactly.

### Commitment gate

You must commit to all of these:

- Never guess on data.
- Never hallucinate assignees, PRs, branches, statuses, reviewers, times or source facts.
- Never skip required authority files or validation gates.
- Never present AI inference as verified fact or team decision.
- Never violate WCAG 2.2 AA for any reason, including layout pressure.
- Never clip, overlap or hide required content.
- Never use automatic shrink-to-fit.
- Use responsive, deliberate typography only within the ranges permitted by `CARD_COMPONENT_STANDARD.md`.
- If content still does not fit at the accessible minimum, change card geometry, reduce card density or paginate.

If these conditions cannot be met: STOP.

---

## 0️⃣ READ `INTEGRITY_CONSTRAINT.md`

Data integrity rules are non-negotiable.

Capacity is meeting data, not invented data.

PRE-MEETING:
- capacity may be missing
- show `○ Kapacitet fastställs under mötet`
- never estimate hours

POST-MEETING:
- capacity must be present
- otherwise STOP

---

## 1️⃣ READ `SYSTEM_CONTRACT.yaml`

This owns orchestration:
- execution sequence
- gates
- STOP/CONTINUE decisions
- data validation
- delivery rules

Follow `execution_sequence` exactly.

---

## 2️⃣ READ PRESENTATION AUTHORITIES BEFORE COMPOSITION

Read in this order:

1. [`design/ACCESSIBILITY_NEURODIVERSITY.md`](design/ACCESSIBILITY_NEURODIVERSITY.md)
2. [`design/VISUAL_DESIGN_MANDATORY.md`](design/VISUAL_DESIGN_MANDATORY.md)
3. [`design/CARD_COMPONENT_STANDARD.md`](design/CARD_COMPONENT_STANDARD.md)
4. [`design/PROVENANCE_AND_AI_LABELING.md`](design/PROVENANCE_AND_AI_LABELING.md)
5. [`monday_meeting/design/LAYOUT_OVERFLOW_GUARD.md`](monday_meeting/design/LAYOUT_OVERFLOW_GUARD.md)
6. [`monday_meeting/design/SLIDE_DETAIL_SPEC.md`](monday_meeting/design/SLIDE_DETAIL_SPEC.md)
7. [`monday_meeting/design/TEMPLATE_REFERENCE.html`](monday_meeting/design/TEMPLATE_REFERENCE.html) — reference only

### Authority order for conflicts

1. **Accessibility / WCAG 2.2 AA** — absolute boundary
2. **Global visual design** — theme, hierarchy and responsive typography roles
3. **Card component standard** — card internals, compact metadata, timestamps, spacing
4. **Provenance standard** — fact/team/AI source identity
5. **Overflow guard** — responsive fit, grid density, pagination
6. **Slide detail spec** — content fields and slide purpose
7. **Template reference** — example only

No lower authority may weaken WCAG or hide required provenance.

---

## 3️⃣ RESPONSIVE FIT RULE

For every slide/card:

1. Start at preferred typography sizes.
2. Wrap text naturally.
3. Reduce deliberately only inside the role-specific ranges in `CARD_COMPONENT_STANDARD.md`.
4. Maintain WCAG AA contrast and symbol+text redundancy.
5. Keep even natural spacing; never vertically justify rows across the whole card.
6. Let cards grow or reduce grid density when required.
7. If content still does not fit at the permitted accessible minimum, create a continuation slide.

Forbidden:
- clipping
- overlaps
- missing rows
- automatic shrink-to-fit
- fonts below component minimum
- contrast below WCAG AA
- color-only meaning
- provenance removed to save space

---

## 4️⃣ PROVENANCE RULE

Whenever content is not explicitly present in a registered source, label it.

Use:
- `📅 Schemafakta` — explicitly in registered school schedule
- `✅ Mötesprotokoll` / equivalent — explicitly supplied or confirmed by team
- `🔎 AI-analys` — AI interpretation, synthesis or assessment of verified evidence
- `⭐ AI-förslag` — AI recommendation, suggested action or suggested question
- `⚠ Källa behöver verifieras` — origin cannot be verified

Do not use the same icon for analysis and proposals.

This applies globally, especially to sprintplan, sprintmål, prioritering, nästa steg and frågor till PL.

---

## 5️⃣ FOLLOW `execution_sequence`

Continue from `SYSTEM_CONTRACT.yaml` and execute every step in order.

---

## REQUIRED DATASETS

### team_roster
- Source: `GITHUB_TEAM_ROSTER`
- Access: `_memory/TEAM_ROSTER.md`
- Missing → STOP

### merged_prs
- Source: `GITHUB_MERGED_PRS`
- Preferred access: GitHub Connector/API
- Follow registered fallback order only
- All fallbacks fail → INCOMPLETE → gate decides STOP

### active_issues
- Source: `GITHUB_OPEN_ISSUES`
- Preferred access: GitHub Connector/API
- Follow registered fallback order only
- All fallbacks fail → INCOMPLETE → gate decides STOP

---

## FORBIDDEN IMPLEMENTATIONS

Do not use:
- shell network commands (`git clone`, `git fetch`, `curl`, `wget`)
- generic web search for registered project data
- unregistered URLs/sources
- model knowledge as source

---

## RENDER COMPLETENESS

Before delivery, the rendered artifact must satisfy:

```text
wcag_aa_violation_count == 0
color_only_information_count == 0
text_overlap_count == 0
card_overlap_count == 0
text_outside_card_count == 0
text_clipping_count == 0
out_of_bounds_element_count == 0
font_below_component_minimum_count == 0
missing_required_card_row_count == 0
uneven_row_spacing_caused_by_vertical_justification == 0
ai_analysis_without_magnifying_glass_count == 0
ai_proposal_without_star_count == 0
unverified_item_presented_as_confirmed_count == 0
```

If any check is non-zero:
1. STOP delivery.
2. Fix typography/layout/provenance.
3. Add continuation slide(s) where required.
4. Rerender.
5. Reinspect the actual artifact.

---

## NEXT STEP

Go to `SYSTEM_CONTRACT.yaml`, then follow the authorities above before rendering.
