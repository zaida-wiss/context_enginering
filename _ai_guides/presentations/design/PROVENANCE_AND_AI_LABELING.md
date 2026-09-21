---
name: provenance_and_ai_labeling
description: MANDATORY — distinguish verified facts/team input from AI-derived proposals and analysis
metadata:
  type: design-and-content-integrity
  critical: true
  required_before: rendering
  version: 1.6
---

# 🏷️ PROVENANCE & AI LABELING STANDARD

Every presentation must make it immediately clear **where a statement comes from**.

AI analysis must never look like a confirmed team decision, a school-schedule fact, or a meeting-note fact.

## Absolute WCAG boundary

All provenance labels and symbols MUST comply with WCAG 2.2 AA.

- normal-text contrast >= 4.5:1
- color is never the sole information carrier
- each content block carries its canonical provenance symbol
- every symbol used in the card is repeated with its full text label in the card's bottom provenance row
- provenance symbols and bottom labels may never be hidden to save space
- minimum provenance/source text size in this deck: **11 pt**
- the bottom provenance row uses visual-priority level 4: lowest emphasis,
  but always with canonical symbol + text label and WCAG-compliant contrast
- inline block symbols inherit the block's readable treatment and must remain clearly visible

If a provenance label cannot fit accessibly, change card geometry or paginate.
Level 4 must never be implemented with opacity or color that makes the source
difficult to read against the card background.

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

### 👥 ✅ Mötesprotokoll
Use when an action, question, decision or plan is explicitly present in:
- meeting protocol / meeting notes

The meeting symbol `👥` is mandatory whenever the named source is a meeting
protocol. The verification symbol `✅` is also mandatory. Render `👥 ✅`
with the content block and the complete visible label
`👥 ✅ Mötesprotokoll` in the card's bottom provenance row.

### ✅ Teamfakta
Use when an action, question, decision or plan is explicitly present in:
- prefilled meeting input
- approved team input
- another registered source that directly states the item

Labels:
- `👥 ✅ Mötesprotokoll`
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
## 2A. CANONICAL PRESENTATION SYMBOL GRAMMAR

The presentation uses one semantic symbol grammar from data/composition through
rendered PPTX/PDF. Symbols are functional information architecture.

### Task / question meanings

Use these symbols whenever the corresponding meaning is rendered:

- `📅` = calendar / verified schedule source
- `🎯` = what / task / deliverable / focus
- `🕒` = when / time / deadline
- `📍` = where / channel / submission place
- `💡` = why / purpose / consequence
- `🛠` = how / method / execution/submission method
- `👤` = who / verified owner, assignee, contributor or responsible person

The symbol appears directly with the information it explains. A text heading
elsewhere on the slide does not replace the semantic symbol when the field is
shown.

### Provenance / reasoning

- `👥 ✅` = verified meeting-protocol fact
- `✅` = other verified team/source fact
- `🔎` = AI analysis / interpretation
- `⭐` = AI proposal / recommendation
- `⚠` = source/origin requires verification

`⚠` is reserved for source uncertainty. Risk content uses the separate risk
grammar below so the same symbol never carries two active meanings.

### GitHub verification

Verified GitHub-derived facts use a **GitHub icon + ✅** visual pair and the
visible text label `GitHub verifierat` where source identity is useful.

Renderer contract:
- use the registered/native GitHub/Lucide GitHub vector icon rather than an
  ASCII substitute;
- pair the icon with `✅` and readable source text in source/provenance rows;
- retain issue/PR/commit identifiers as text;
- source verification does not replace workflow state symbols such as `📌`.

### Workflow

- `📌` = verified open PR / waiting in PR
- `🔗` = dependency / cross-team relation
- `🔀` = verified integration/merge event when a merge/integration symbol is useful
- `✅` = completed/verified state only when its surrounding label makes that
  state unambiguous

### Risk analysis

Risk semantics use symbols that do not collide with source uncertainty:

- `⚡` = risk / uncertain threat to an objective
- `📈` = likelihood/probability assessment
- `💥` = consequence/impact
- `🛡` = mitigation/control
- `👤` = verified risk owner
- `↘` = residual risk after control
- `🔎` = AI interpretation of risk evidence
- `⭐` = AI-proposed mitigation, reprioritisation or candidate risk

Risk level/criticality additionally uses its registered **symbol + text + color**
semantics. Color remains supplementary.

### End-to-end persistence

For each semantic block:

```text
source/data field
  → composition meaning
  → canonical symbol token
  → renderer symbol/icon
  → exported PPTX/PDF
  → rendered visual inspection
```

A simplification may shorten wording or paginate content. It preserves the
symbol token attached to every surviving semantic field.


Canonical symbols are semantic content, not decoration. Layout simplification,
density reduction, refactoring and export may change placement but may not remove
the symbol layer. If a symbol-bearing block survives, its canonical symbol survives
with it.

Use the icons consistently across the whole deck:

- `📅` = verified schedule fact
- `👥 ✅` = verified meeting-protocol fact
- `✅` = other verified team fact
- `🔎` = AI analysis / interpretation
- `⭐` = AI proposal / recommendation
- `⚠` = source/origin not safely verified

Do not use one AI icon for both analysis and proposal.

### Supplementary workflow symbols

- `📌 Väntar i PR` identifies work with a verified open pull request.
  The pushpin is rendered before the PR number/title inside the card, for example
  `📌 #114`, and repeated as `📌 Väntar i PR` in the card-bottom provenance row.
- `🔗 Beroende` identifies a dependency relation or dependency view.

Workflow symbols never replace source identity. In the content block, show the
workflow symbol together with the canonical provenance symbol:

`🔗 · 🔎 [analysis text]`

`🔗 · 👥 ✅ [verified dependency text]`

The bottom provenance row expands every symbol used in the card, for example:

`🔗 Beroende · 🔎 AI-analys`

`🔗 Beroende · 👥 ✅ Mötesprotokoll`

### Symbols may never be replaced by tags

The symbol is required inline at the start of its content block. The card's
bottom provenance row repeats that symbol immediately before its full text label.

Forbidden replacements include:
- a pill, tag, badge or chip that contains only `AI-förslag` or `AI-analys`
- a color-coded tag without the canonical symbol
- question-mark variants of the AI labels
- abbreviations such as `AI-F` / `AI-A`
- a slide-level legend as the only explanation of a card's symbols
- a card-bottom text label that is missing its matching canonical symbol

Correct:
- `🔎 AI-analys`
- `⭐ AI-förslag`

If the selected font cannot render a canonical symbol, use a symbol-capable
fallback font for that glyph. When no verified font can preserve the symbol,
render an embedded native/vector icon with the same canonical meaning. Do not
substitute a tag, question mark, ASCII character, letter, punctuation mark or
textual abbreviation.

ASCII transliteration is explicitly forbidden. Examples of forbidden output
include `📌 → |`, `✅ → +`, `🔎 → ~`, `⭐ → *`, `⚠ → !` and
`📅 → #`. The rendered audience-facing artifact must contain the intended
visual symbol, not merely equivalent source text.

### Rendered glyph integrity gate

The symbol requirement applies to the exported artifact, not only to the source
string.

Before delivery:
1. render every physical slide from the final exported artifact
2. inspect each canonical provenance and task symbol in the rendered output
3. fail when a symbol becomes an empty square, replacement character, missing
   glyph, unrelated fallback glyph or invisible character
4. select a verified symbol-capable fallback font for only the affected glyph/run
5. export and inspect again

A source-file search for the Unicode character is not sufficient proof that the
audience can see it. Both the inline block symbol and its matching symbol + text
label in the bottom provenance row must be legible.

Required result:

```text
rendered_missing_glyph_count == 0
rendered_replacement_glyph_count == 0
canonical_symbol_render_mismatch_count == 0
canonical_symbol_ascii_transliteration_count == 0
canonical_symbol_missing_after_simplification_count == 0
canonical_symbol_missing_in_export_count == 0
semantic_field_missing_required_symbol_count == 0
owner_field_missing_person_symbol_count == 0
github_verified_source_missing_github_icon_check_pair_count == 0
risk_field_missing_registered_risk_symbol_count == 0
rendered_symbol_inventory_mismatch_count == 0
waiting_pr_pushpin_missing_before_identifier_count == 0
waiting_pr_bottom_pushpin_label_missing_count == 0
```

The audience should be able to distinguish immediately between:

> **Vad vet vi? Vad analyserar AI? Vad föreslår AI?**

---

## 3. COLOR MAY NOT REPLACE SOURCE LABELS

Do **not** use red text to mean fact.

Red means blocker/critical in the status system, and color alone may not carry meaning.

Source identity must always be represented by both layers: **inline icon** and
the matching **icon + text** in the card's bottom provenance row.

Color may support either layer, but never replace them.

---

## 4. MIXED CARDS — SYMBOL IN BLOCK, FULL LABEL AT BOTTOM

A single card may contain fact, AI analysis and/or AI proposal. Prefix each
semantic content block with only its canonical symbol. At the bottom of the card,
show a deduplicated provenance row containing symbol + full text label for every
class used in the card.

Example:

```text
Tisdag 22 sep

📅 PL-avstämning 12:30–14:00 i Slack Huddle.

🔎 Integrationsstatus är den mest sannolika diskussionspunkten utifrån beroendena.

⭐ Ta med tydlig status på integration, test och README.

📅 Schemafakta · 🔎 AI-analys · ⭐ AI-förslag
```

Do not blend blocks without symbols. Do not repeat the full text label inside
each content block, and do not omit the consolidated bottom row.

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
📅 [schedule fact]
👥 ✅ [meeting fact]
🔎 [AI analysis]
⭐ [AI proposal]

📅 Schemafakta · 👥 ✅ Mötesprotokoll · 🔎 AI-analys · ⭐ AI-förslag
```

Only text explicitly present in the schedule is `📅 Schemafakta`.

Items such as these are normally AI-derived unless separately verified:
- `Lås scope, kapacitet och ägare`
- `Prioritet: API-kontrakt + JNA + öppna PR-reviewer`
- `Få svar om det verifierade kursunderlaget`
- `Stäng öppna frågetecken`
- `Verifiera att det verifierade kursmaterialet har ägare och checkbar status`

Classify each as either analysis (`🔎`) or proposal (`⭐`) based on what the sentence actually does.

---

## 6. SLIDE ⑬ — NÄSTA STEG

Build next steps in this evidence order:

1. explicit actions from meeting protocol
2. explicit actions from approved/prefilled team input
3. AI-derived proposals based on verified project data

Every card must contain inline provenance symbol(s) and a matching consolidated
symbol + text provenance row at the bottom.

Verified:
```text
👥 ✅ Mötesprotokoll
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

## 9. AI CHECK TRACE — EXACT SOURCES CHECKED

When AI performs a project-health check and reports an analytical result such as:

- no new candidate risk identified
- no new dependency/blocker identified
- no additional capacity concern found
- no new cross-layer mismatch found
- no new technical-debt signal found

the result must remain auditable.

Use a compact block:

```text
🔎 AI-kontroll
Kontrollerat:
- [exact registered source / file / GitHub area / branch set]
- [exact registered source / file / GitHub area / branch set]

Resultat:
[short conclusion]
```

The `Kontrollerat` list names the **actual places inspected**, not generic
categories. Good examples include:

- `GOOGLE_RISK_REGISTER · RISK REGISTER`
- `GitHub · open issues linked to current sprint`
- `GitHub · active branches touching [verified integration boundary]`
- `GOOGLE_MEETING_PROTOCOL · sprint planning / blockers`
- selected project's registered decision-record path
- a named API-contract file or registered source

Only list sources that were actually inspected in that analysis run.

If a relevant expected source could not be checked, say so with `⚠` rather
than implying it was analysed.

This trace teaches the team which recurring project sources are useful to
inspect and lets the audience understand how the AI reached a "nothing new"
conclusion.

The trace is **evidence metadata**, not an invitation to invent a proposal.
When the analysis genuinely finds nothing actionable, the result may simply say
that no new signal was identified in the inspected sources.

---

## 10. VISUAL TREATMENT

Provenance uses two coordinated visual layers:

- inline content layer: canonical symbol only at the start of each semantic block
- card-bottom layer: deduplicated canonical symbol + short full text label for every class used
- both layers remain left aligned and inside the relevant card
- contrast must remain WCAG AA

Do not rely only on a slide footer when different cards have different origins.
The bottom card row supplies the text meaning for inline symbols; a slide-level
footer remains an additional source summary.

## Mandatory per-slide source footer

Every physical slide, including continuation slides, has a reserved source
footer at the bottom. It lists the sources actually used for content on that
physical slide, not every source consulted for the whole deck.

Verified source format:

`✅ GitHub Projects · ✅ PR-data · 📅 Schema`

Use the canonical source symbol that matches the source class and include a
short human-readable source name. Deduplicate repeated use of the same source
within the slide. Card/block-level provenance remains mandatory; the footer is
an additional slide-level summary and never replaces it.

### Expected but unverifiable source

If a source was required or reasonably expected for that slide but could not be
verified, include it in the footer with all three cues:

1. `⚠` symbol
2. text such as `kunde inte verifieras`
3. strikethrough on the source name

Rendered example: `⚠ ~~GitHub Projects~~ — kunde inte verifieras`

Strikethrough alone is forbidden because it is not a sufficient accessible
status cue. Never list an unverifiable source as used or verified. If a required
source failure triggers a STOP rule, retain the failure in the audit/report;
the footer does not make delivery permissible.

The footer uses priority level 4 but must remain at least 11 pt and pass WCAG
2.2 AA contrast. If the source list does not fit, wrap it within the reserved
footer or continue content on another slide; never overlap the footer.

---

## 11. RENDER GATE

Required zero-count checks:

```text
wcag_aa_violation_count == 0
provenance_symbol_replaced_by_tag_count == 0
provenance_text_without_canonical_symbol_count == 0
ai_suggestion_without_star_count == 0
ai_analysis_without_magnifying_glass_count == 0
color_only_information_count == 0
sprint_plan_fact_without_source_label_count == 0
sprint_plan_ai_content_without_source_icon_count == 0
next_step_card_without_provenance_count == 0
pl_question_card_without_provenance_count == 0
ai_analysis_without_magnifying_glass_count == 0
ai_proposal_without_star_count == 0
unverified_item_presented_as_confirmed_count == 0
content_block_provenance_symbol_missing_count == 0
card_bottom_provenance_full_label_missing_count == 0
card_bottom_provenance_symbol_text_mismatch_count == 0
```

The audience must always be able to answer:

> Är detta fakta från en källa, något teamet faktiskt har sagt, en AI-analys eller ett AI-förslag?

---

**Status:** PRODUCTION
**Version:** 1.6
**Last updated:** 2026-09-21
