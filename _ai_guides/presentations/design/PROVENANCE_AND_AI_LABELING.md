---
name: provenance_and_ai_labeling
description: MANDATORY — distinguish verified facts/team input from AI-derived proposals and analysis
metadata:
  type: design-and-content-integrity
  critical: true
  required_before: rendering
  version: 1.2
---

# 🏷️ PROVENANCE & AI LABELING STANDARD

Every presentation must make it immediately clear **where a statement comes from**.

AI analysis must never look like a confirmed team decision, a school-schedule fact, or a meeting-note fact.

## Absolute WCAG boundary

All provenance labels and symbols MUST comply with WCAG 2.2 AA.

- normal-text contrast >= 4.5:1
- color is never the sole information carrier
- source identity always uses icon + text
- provenance labels may never be hidden to save space
- minimum provenance/source text size in this deck: **10 pt**

If a provenance label cannot fit accessibly, change card geometry or paginate.

---

## 1. CANONICAL SOURCE CLASSES

### 📅 Schemafakta
Use only when the exact information is explicitly supported by the registered school schedule source, e.g. `SCHEDULE.yaml`.

May include:
- date
- time
- scheduled activity
- meeting name
- location/channel when explicitly stated

Example:

```text
📅 Schemafakta
PL-avstämning 12:30–14:00 i Slack Huddle.
```

Do not attach an inferred purpose to schedule text and still call the whole statement schemafakta.

---

### ✅ Mötes-/teamfakta
Use when an action, question, decision or plan is explicitly present in:
- meeting protocol / meeting notes
- prefilled meeting input
- approved team input
- another registered source that directly states the item

Labels:
- `✅ Mötesprotokoll`
- `✅ Förifyllt av teamet`
- `✅ Bekräftat i mötet`

---

### 🔎 AI-analys
Use when AI interprets, compares or draws a conclusion from verified source data, without claiming that the team already decided it.

Typical cases:
- dependency analysis
- risk interpretation
- prioritization analysis
- capacity interpretation
- identifying a likely blocker or consequence
- synthesizing patterns across GitHub/project data

Labels:
- `🔎 AI-analys`
- `🔎 AI-tolkning av underlaget`
- `🔎 AI-analys av beroenden`

Prefer analytical wording:
- `Analys: ...`
- `AI-bedömning: ...`
- `Underlaget tyder på ...`

---

### ⭐ AI-förslag
Use when AI recommends an action, question or next step that is not explicitly written/confirmed by the team.

Typical cases:
- suggested next step
- suggested sprint action
- suggested PL question
- suggested order of work
- suggested mitigation
- reasonable but undocumented action

Labels:
- `⭐ AI-förslag`
- `⭐ AI-förslag till PL`
- `⭐ Förslag baserat på underlaget`

Prefer proposal wording:
- `Förslag: ...`
- `Rimligt nästa steg: ...`
- `Förslag till fråga: ...`

---

### ⚠ Källa behöver verifieras
Use when provenance matters but cannot be safely verified.

Never silently convert unclear origin into fact.

---

## 2. ICON SEMANTICS — HARD RULE

Use the icons consistently across the whole deck:

- `📅` = verified schedule fact
- `✅` = verified meeting/team fact
- `🔎` = AI analysis / interpretation
- `⭐` = AI proposal / recommendation
- `⚠` = source/origin not safely verified

Do not use one AI icon for both analysis and proposal.

The audience should be able to distinguish immediately between:

> **Vad vet vi? Vad analyserar AI? Vad föreslår AI?**

---

## 3. COLOR MAY NOT REPLACE SOURCE LABELS

Do **not** use red text to mean fact.

Red means blocker/critical in the status system, and color alone may not carry meaning.

Source identity must always be represented by **icon + text**.

Color may support the source label, but never replace it.

---

## 4. MIXED CARDS MUST LABEL EACH BLOCK

A single card may contain fact, AI analysis and/or AI proposal.

Example:

```text
Tisdag 22 sep

📅 Schemafakta
PL-avstämning 12:30–14:00 i Slack Huddle.

🔎 AI-analys
Integrationsstatus är den mest sannolika diskussionspunkten utifrån beroendena.

⭐ AI-förslag
Ta med tydlig status på integration, test och README.
```

Do not blend these into one unlabelled paragraph.

---

## 5. SLIDE ⑫ — SPRINTPLAN

Every day card must distinguish:

1. verified schedule facts
2. verified meeting/team actions
3. AI-derived analysis
4. AI-derived planning suggestions

Order inside the card when present:

```text
Dag + datum
📅 Schemafakta
✅ Mötes-/teamfakta
🔎 AI-analys
⭐ AI-förslag
```

Only text explicitly present in the schedule is `📅 Schemafakta`.

Items such as these are normally AI-derived unless separately verified:
- `Lås scope, kapacitet och ägare`
- `Prioritet: API-kontrakt + JNA + öppna PR-reviewer`
- `Få svar om CTO-underlaget`
- `Stäng öppna frågetecken`
- `Verifiera att CTO-materialet har ägare och checkbar status`

Classify each as either analysis (`🔎`) or proposal (`⭐`) based on what the sentence actually does.

---

## 6. SLIDE ⑬ — NÄSTA STEG

Build next steps in this evidence order:

1. explicit actions from meeting protocol
2. explicit actions from approved/prefilled team input
3. AI-derived proposals based on verified project data

Every card must contain its own provenance label.

Verified:
```text
✅ Mötesprotokoll
```

AI-derived recommended action:
```text
⭐ AI-förslag
```

If a card explains **why** a step is sensible, that explanatory block may additionally be marked:

```text
🔎 AI-analys
```

If both verified and AI-derived items occur on one slide, verified actions appear first unless the meeting itself sets another priority.

Do not present `⭐ AI-förslag` as a confirmed action.

---

## 7. SLIDE ⑭ — FRÅGOR TILL PL

Every question card must identify whether it is a real team question or an AI suggestion.

Verified:
- `✅ Från mötesprotokoll`
- `✅ Teamfråga`

AI-proposed question:
- `⭐ AI-förslag till PL`

AI explanation/interpretation supporting the question:
- `🔎 AI-analys`
- `🔎 AI-analys av beroenden`

Urgency groups such as `IDAG-SVAR BEHÖVS` and `NICE-TO-HAVE` do not replace provenance.

---

## 8. GLOBAL APPLICATION

This rule applies to **all slides**, not only ⑫–⑭.

Whenever content is inferred rather than copied/faithfully summarized from a registered source, mark it correctly as either:

- `🔎 AI-analys` when AI is interpreting evidence
- `⭐ AI-förslag` when AI is recommending an action/question

Common examples:
- sprint goals
- prioritization
- risk interpretation
- dependency recommendation
- capacity recommendation
- decision candidates
- next steps
- PL questions

---

## 9. VISUAL TREATMENT

Provenance is compact metadata:

- preferred: 10–11 pt
- minimum: 10 pt
- contrast must remain WCAG AA
- icon + short text
- left aligned
- inside the relevant card/block

Do not rely only on a slide footer when different cards have different origins.

Icons must remain legible and must not be the only carrier of meaning; always pair with text.

---

## 10. RENDER GATE

Required zero-count checks:

```text
wcag_aa_violation_count == 0
color_only_information_count == 0
sprint_plan_fact_without_source_label_count == 0
sprint_plan_ai_content_without_source_icon_count == 0
next_step_card_without_provenance_count == 0
pl_question_card_without_provenance_count == 0
ai_analysis_without_magnifying_glass_count == 0
ai_proposal_without_star_count == 0
unverified_item_presented_as_confirmed_count == 0
mixed_provenance_card_without_block_labels_count == 0
```

The audience must always be able to answer:

> Är detta fakta från en källa, något teamet faktiskt har sagt, en AI-analys eller ett AI-förslag?

---

**Status:** PRODUCTION
**Version:** 1.2
**Last updated:** 2026-09-17
