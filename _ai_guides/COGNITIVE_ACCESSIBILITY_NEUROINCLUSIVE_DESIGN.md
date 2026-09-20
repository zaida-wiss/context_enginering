---
name: cognitive_accessibility_neuroinclusive_design
description: Global evidence-informed guidance for reducing cognitive load across web, systems, documents and presentations
version: 1.0
metadata:
  type: global_design_guidance
  scope: all_projects_and_artifacts
  status: active
  normative: false
  wcag_relationship: complementary
---

# Cognitive accessibility & neuroinclusive design

This authority provides reusable **advisory** design knowledge for web interfaces,
systems/apps, documents and presentations. It complements WCAG; it does not replace
or weaken WCAG requirements.

## Core principle

Design so users need to remember, decode, filter and mentally reorganize as little
as reasonably possible. Neurodivergent users are not one homogeneous group.
Recommendations are hypotheses to apply proportionally to the user, task and
context rather than claims that every person with ADHD, dyslexia, autism or another
cognitive difference needs the same design.

## Useful design strategies

When they improve comprehension or focus, consider:
- chunking information into meaningful groups;
- clear visual hierarchy and a visible reading/action order;
- stable placement, navigation and interaction patterns;
- concise text with meaningful headings and adequate whitespace;
- progressive disclosure or smaller steps instead of presenting everything at once;
- reducing competing highlights, decorative noise and unnecessary simultaneous choices;
- visible state, progress, next action and error recovery so users do not have to
  remember hidden system state;
- multiple complementary cues: **text + symbol/icon + shape/position + color**;
- diagrams, pictograms or other visual representations when they genuinely clarify
  relationships or sequence;
- user-controlled personalization where practical, rather than assuming one fixed
  neurodivergent-friendly presentation works for everyone.

### Color, form and symbols

Color may accelerate scanning and grouping, but must not be the only carrier of
meaning. Pair meaningful color with a non-color cue such as text, symbol, shape,
position or pattern.

Keep semantics stable. A symbol, shape, color role or location used for one meaning
should not silently acquire another meaning elsewhere in the same product/artifact.

More cues are not automatically better. Symbols and colors that add decoding work,
visual clutter or competing emphasis can increase cognitive load. Prefer the
smallest consistent cue system that materially improves recognition or navigation.

### Dyslexia-supportive tendencies

Consider clear hierarchy, readable typography, left-aligned body text where
appropriate, moderate line lengths, predictable spacing, concise paragraphs and
visual support for dense relationships. Do not claim a particular font, color or
layout is universally optimal for dyslexia without current evidence.

### ADHD / attention-supportive tendencies

Consider one clear primary purpose per view, visible grouping, stable hierarchy,
clear progress/next action, manageable information density and fewer competing
attention signals. Avoid turning "ADHD-friendly" into a decorative style.

### Predictability and sensory/cognitive load

Prefer consistent interaction and visual grammar. Avoid unnecessary motion,
surprise, hidden semantics and arbitrary layout changes. Allow users control over
non-essential motion or stimulation where applicable.

## Pedagogical contract

When AI recommends a material cognitive-accessibility technique, teach enough of
the mental model for the user/team to reuse the reasoning:

- explain **what cognitive work the design is intended to reduce**;
- explain why the proposed cue/grouping/sequence may help;
- connect the recommendation to the concrete interface, task or learning situation;
- distinguish a mandatory accessibility requirement from an evidence-informed tip;
- explain meaningful tradeoffs, including when a technique could instead create
  clutter, distraction or extra decoding work;
- prefer a small concrete example when it teaches the principle faster than an
  abstract explanation.

What/Where/Why/How/When are comprehension dimensions, not mandatory headings.
Use the adaptive system-first teaching model in `PROJECT_WORK_ANALYSIS.md`.

## Evidence and source contract

Claims must follow `_ai_guides/AI_BEST_PRACTICE_EVIDENCE_POLICY.yaml`.

Evidence preference for this domain:
1. current standards and authoritative accessibility guidance, especially W3C/WAI,
   WCAG and W3C COGA;
2. peer-reviewed systematic/scoping reviews and original HCI/accessibility research;
3. specialist guidance with transparent methodology and domain expertise;
4. practitioner/industry material as implementation signal, not proof by itself.

For material recommendations:
- cite or identify the source/evidence basis when it affects the decision;
- distinguish **WCAG/standard requirement**, **established guidance**,
  **research-supported tendency**, and **experimental/context-dependent suggestion**;
- include source date/version when freshness matters;
- do not convert association, preference studies or small samples into universal
  claims about a diagnosis;
- surface disagreement or weak evidence instead of presenting certainty;
- re-check current evidence when the user asks for latest/current best practice.

External sources inform recommendations; they do not become repository authority
and do not override project rules or user-decision/conflict gates.

## Relationship to presentation rules

Presentation-specific authorities may impose stricter rendering and consistency
rules. They should consume these general principles rather than redefine general
claims about neurodiversity. Existing presentation WCAG gates remain mandatory.

## AI recommendation language

Prefer:
> "This may reduce scanning or working-memory load because ..."

Avoid:
> "People with ADHD need this."

Prefer:
> "Evidence/guidance supports this as a useful design strategy; test it with the
> actual users and context."

## Review questions

When cognitive accessibility is material, ask:
- What must the user notice first?
- What must they remember between steps?
- Can important state or sequence be made visible?
- Are related items visually grouped?
- Are color meanings backed by non-color cues?
- Do symbols reduce decoding, or add another code to learn?
- Is the interface predictable across views?
- Is density forcing users to filter too much at once?
- Can personalization or progressive disclosure reduce unnecessary load?
- What evidence supports the recommendation, and how strong/current is it?

---
status: ACTIVE
