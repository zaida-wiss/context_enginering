---
name: pl_questions_standard
description: RETIRED — slide 14 rules moved to SLIDE_DETAIL_SPEC and provenance authority
metadata:
  type: retired_reference
  status: retired
  version: 1.0
---

# ❓ PL QUESTIONS STANDARD — ⑭ FRÅGOR TILL PL

> **RETIRED. DO NOT USE FOR PRODUCTION.** This file contains old text-tag
> provenance labels. Slide 14 content is owned by `SLIDE_DETAIL_SPEC.md` and
> source symbols are owned by `PROVENANCE_AND_AI_LABELING.md`.

This file is authoritative for slide **⑭ Frågor till PL**.

It defines:
- where PL questions come from
- how team-authored questions are separated from AI suggestions
- mandatory source labels
- card layout
- adaptive typography so every question fits without clipping

Read together with:
- `ACCESSIBILITY_NEURODIVERSITY.md`
- `VISUAL_DESIGN_MANDATORY.md`
- `RESPONSIVE_LAYOUT_STANDARD.md`
- `CARD_COMPONENT_STANDARD.md`
- `SLIDE_DETAIL_SPEC.md`

---

## 1. EVERY QUESTION IS A CARD

Each PL question must be rendered as its own modern glass card.

Never render PL questions as:
- plain text rows
- a bullet list without cards
- large text blocks floating directly on the slide
- bordered legacy boxes that do not match the deck's card system

Use the same dark glass card surface as the rest of the presentation.

---

## 2. TWO QUESTION TYPES — NEVER MIX WITHOUT LABELS

Every PL question MUST be classified as exactly one of these:

### A. TEAM QUESTION — verified from meeting protocol

Use when the question was already written by the team in the meeting protocol / meeting notes before the presentation was generated.

Mandatory source label:

`TEAMFRÅGA · Mötesprotokoll`

These are not AI-generated questions.
The question may be lightly cleaned up for readability, but its meaning must remain unchanged.

### B. AI SUGGESTION — derived from verified project evidence

Use only when the question is not present in the meeting protocol but is a reasonable discussion question derived from verified project evidence such as:
- blocker
- dependency
- deadline risk
- scope ambiguity
- issue/PR state
- integration need
- actual capacity data when available

Mandatory source label:

`AI-FÖRSLAG · Härledd från underlag`

Also show a short evidence line, for example:

`Underlag: #6 JNA + CTO-deadline 24 sep`

AI suggestions may NEVER be presented as if the team asked them.

---

## 3. SOURCE PRIORITY

Build slide ⑭ in this order:

1. Read the latest relevant meeting protocol section for `Frågor till PL`, `Öppna frågor`, or equivalent.
2. Extract all actually filled-in questions.
3. Render all verified team questions first.
4. Mark them `TEAMFRÅGA · Mötesprotokoll`.
5. Only after that may optional AI suggestions be generated from verified evidence.
6. Mark every generated question `AI-FÖRSLAG · Härledd från underlag`.

If the meeting protocol contains no filled-in PL questions:
- do not imply that the team asked any
- either show only clearly labelled AI suggestions
- or show a compact note: `Inga teamfrågor ifyllda före mötet.`

---

## 4. CARD CONTENT

Each question card uses this hierarchy:

```text
TEAMFRÅGA · Mötesprotokoll
Q1 SCOPE — Vad ska vi lämna in till CTO den 24:e?
Påverkan: Avgör vad teamet behöver prioritera denna vecka.
```

or:

```text
AI-FÖRSLAG · Härledd från underlag
Q3 INTEGRATION — Behöver API-kontraktet låsas innan frontend går vidare?
Påverkan: Minskar risken för dubbelarbete mellan Frontend och Backend.
Underlag: öppen integration + CTO-deadline
```

Required fields:
- provenance/source label
- Q-number + category
- direct question
- short impact line
- evidence line for AI suggestions

---

## 5. ADAPTIVE TYPOGRAPHY

Question-card text must adapt to content length using `RESPONSIVE_LAYOUT_STANDARD.md`.

Recommended ranges:
- question title: 16–20 pt
- provenance label: 9–11 pt
- impact line: 11–14 pt
- AI evidence line: 9–11 pt

If a question is long:
- reduce question text deliberately toward 16 pt
- reduce impact/evidence text toward their minimums
- increase card height
- reduce cards per slide if necessary

Do not keep a 20 pt question if that makes the full card content clip.

No auto-shrink-to-fit.

---

## 6. RESPONSIVE QUESTION LAYOUT

Preferred:
- 2 × 2 cards when questions are short/medium

If one or more questions are long:
- 2 × 1
- 1 × 2
- single-column cards

If all cards still cannot fit cleanly at minimum sizes:
- create `⑭-2`, `⑭-3`, etc.

Do not force four long questions onto one slide.

---

## 7. PRIORITY GROUPING

Questions may still be grouped by urgency:

- `IDAG-SVAR BEHÖVS`
- `BRA ATT DISKUTERA`

But provenance is independent of urgency.

A card can therefore be:
- TEAMFRÅGA + IDAG-SVAR
- TEAMFRÅGA + BRA ATT DISKUTERA
- AI-FÖRSLAG + IDAG-SVAR
- AI-FÖRSLAG + BRA ATT DISKUTERA

Never use urgency styling to hide whether the question came from the team or AI.

---

## 8. FOOTER

The old footer `Källa: Team-feedback under mötet ✅` is insufficient when AI suggestions exist.

Use one of these:

Only team questions:
`Källa: Mötesprotokoll · verifierade teamfrågor ✅`

Only AI suggestions:
`Källa: AI-förslag härledda från verifierat projektunderlag ⚠️`

Mixed:
`Källa: Mötesprotokoll + tydligt märkta AI-förslag ✅`

---

## 9. RENDER GATE

Before delivery verify:

```text
pl_questions_as_cards == true
unlabelled_question_source_count == 0
team_question_falsely_labelled_ai_count == 0
ai_question_falsely_labelled_team_count == 0
ai_question_without_evidence_count == 0
question_text_clipping_count == 0
question_card_overflow_count == 0
```

Also verify visually:
- the full question is readable
- impact text is visible
- provenance can be scanned immediately
- card style matches the rest of the deck
- no card uses oversized text at the expense of missing content

---

**Status:** PRODUCTION
**Version:** 1.0
**Last updated:** 2026-09-17
