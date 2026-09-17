---
name: provenance_and_ai_labeling
description: MANDATORY — distinguish verified facts/team input from AI-derived proposals and analysis
metadata:
  type: design-and-content-integrity
  critical: true
  required_before: rendering
  version: 1.0
---

# 🏷️ PROVENANCE & AI LABELING STANDARD

Every presentation must make it immediately clear **where a statement comes from**.

AI analysis must never look like a confirmed team decision, a school-schedule fact, or a meeting-note fact.

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

Do not attach an inferred purpose to schema text and still call the whole statement schemafakta.

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

### ? AI-förslag / AI-analys
Use when the item is inferred or proposed by AI, including:
- recommendation
- suggested next step
- suggested sprint action
- suggested PL question
- interpretation/prioritization based on source data
- reasonable but not explicitly documented action

The question mark is mandatory.

Labels:
- `? AI-förslag`
- `? AI-analys`
- `? AI-tolkning av underlaget`

Prefer proposal language:
- `Förslag: ...`
- `Rimligt nästa steg: ...`
- `AI-bedömning: ...`

---

### ⚠ Källa behöver verifieras
Use when provenance matters but cannot be safely verified.

Never silently convert unclear origin into fact.

---

## 2. COLOR MAY NOT REPLACE SOURCE LABELS

Do **not** use red text to mean fact.

Red already means blocker/critical in the status system, and color alone may not carry meaning.

Source identity must always be represented by **icon + text**.

Color may support the source label, but never replace it.

---

## 3. MIXED CARDS MUST LABEL EACH BLOCK

A single card may contain both fact and AI reasoning.

Example:

```text
Tisdag 22 sep

📅 Schemafakta
PL-avstämning 12:30–14:00 i Slack Huddle.

? AI-förslag
Ta med tydlig status på integration, test och README.
```

Do not blend these into one unlabelled paragraph.

---

## 4. SLIDE ⑫ — SPRINTPLAN

Every day card must distinguish:

1. verified schedule facts
2. verified meeting/team actions
3. AI-derived planning suggestions

Order inside the card:

```text
Dag + datum
📅 Schemafakta
✅ Mötes-/teamfakta (if any)
? AI-förslag (if any)
```

Only text explicitly present in the schedule is `📅 Schemafakta`.

Items such as these are normally AI-derived unless separately verified:
- `Lås scope, kapacitet och ägare`
- `Prioritet: API-kontrakt + JNA + öppna PR-reviewer`
- `Få svar om CTO-underlaget`
- `Stäng öppna frågetecken`
- `Verifiera att CTO-materialet har ägare och checkbar status`

---

## 5. SLIDE ⑬ — NÄSTA STEG

Build next steps in this evidence order:

1. explicit actions from meeting protocol
2. explicit actions from approved/prefilled team input
3. AI-derived suggestions based on verified project data

Every card must contain its own provenance label.

Verified:
```text
✅ Mötesprotokoll
```

AI-derived:
```text
? AI-förslag
```

If both types occur on one slide, verified actions appear first unless the meeting itself sets another priority.

---

## 6. SLIDE ⑭ — FRÅGOR TILL PL

Every question card must identify whether it is a real team question or an AI suggestion.

Verified:
- `✅ Från mötesprotokoll`
- `✅ Teamfråga`

AI-derived:
- `? AI-förslag till PL`
- `? AI-analys av beroenden`

Urgency groups such as `IDAG-SVAR BEHÖVS` and `NICE-TO-HAVE` do not replace provenance.

---

## 7. GLOBAL APPLICATION

This rule applies to **all slides**, not only ⑫–⑭.

Whenever content is inferred rather than copied/faithfully summarized from a registered source, mark it as AI-derived.

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

## 8. VISUAL TREATMENT

Provenance is compact metadata:

- preferred: 10–11 pt
- dense slide minimum: 9 pt when still WCAG-readable in the rendered artifact
- high enough contrast for WCAG AA
- icon + short text
- left aligned
- inside the relevant card/block

Do not rely on a slide footer when different cards have different origins.

---

## 9. RENDER GATE

Required zero-count checks:

```text
sprint_plan_fact_without_source_label_count == 0
sprint_plan_ai_suggestion_without_question_icon_count == 0
next_step_card_without_provenance_count == 0
pl_question_card_without_provenance_count == 0
ai_generated_item_without_question_icon_count == 0
unverified_item_presented_as_confirmed_count == 0
mixed_provenance_card_without_block_labels_count == 0
```

The audience must always be able to answer:

> Är detta fakta från en källa, något teamet faktiskt har sagt, eller ett förslag från AI?

---

**Status:** PRODUCTION
**Version:** 1.0
**Last updated:** 2026-09-17
