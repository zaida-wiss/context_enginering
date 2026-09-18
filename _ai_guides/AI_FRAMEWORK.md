---
name: ai_framework
description: GLOBAL MANDATORY — behavior contract for every AI task in this context repository
metadata:
  type: global_authority
  critical: true
  status: active
  version: 1.0
---

# GLOBAL AI FRAMEWORK

This file defines behavior that applies to **every AI task** using this repository:
coding, issue creation, planning, risk work, documentation, presentations,
reviews, audits and future task types.

Domain-specific authorities may add rules, but they may not bypass this framework.

## 1. CONTEXT-FIRST CORRECTION

When the user identifies a recurring behavior/design/process defect caused by
repository instructions:

1. locate the owning context rule;
2. update the context repository first;
3. add/update regression validation when practical;
4. only then regenerate or patch the affected artifact/output.

A one-off artifact patch is not the final fix for a context-driven defect.

## 2. CONFLICT DECISION GATE — USER DECIDES

A **genuine conflict** exists when two active instructions/authorities require
incompatible outcomes and both cannot be followed at the same time.

When a genuine conflict is detected, the AI MUST:

1. **STOP before resolving or editing the conflicting rules.**
2. Tell the user that a conflict was found.
3. Name the exact owning files/rules involved.
4. Explain the concrete consequence of each available interpretation/option.
5. Identify any non-negotiable external boundary (for example WCAG 2.2 AA,
   security, law, tool limitation) without pretending the conflicting internal
   rule has already been resolved.
6. Ask the user for the intended decision.
7. Wait for that decision.
8. Record the user's decision in the correct owning authority/decision record.
9. Add or update a regression test/check so the conflict does not silently return.
10. Continue the original task only after the context has been made internally consistent.

### Forbidden conflict behavior

The AI MUST NOT:
- silently choose the newest rule;
- silently choose the highest-ranked file;
- infer "what the user probably meant" and edit accordingly;
- weaken one rule until the conflict disappears;
- resolve the conflict only in the generated artifact;
- continue rendering/building as though no contradiction exists;
- call an ambiguity a confirmed decision.

Authority order may determine **where** a rule belongs and which external
boundary is absolute. It does not grant permission to silently decide between
two genuinely contradictory active project intentions.

## 3. DISTINGUISH CONFLICT FROM NORMAL SPECIALIZATION

Do not stop for normal rule layering.

Not a conflict:
- one rule owns global palette and another owns card spacing;
- a general rule says "cards" and a slide-specific rule explicitly defines an
  allowed timeline exception;
- a task-specific rule adds detail without contradicting the general rule.

A conflict:
- one active rule requires circled meeting symbols while another forbids them;
- one active rule requires a dedicated slide while another forbids that slide;
- two active rules assign different semantic meanings to the same color/symbol;
- one rule requires an item and another requires it to be omitted.

If uncertain whether two rules are incompatible, surface the possible conflict
to the user rather than silently choosing.

## 4. DECISION TRACE

After the user resolves a conflict, preserve a compact trace:
- conflict identified;
- options presented;
- user decision;
- owning authority updated;
- affected duplicate/contradictory rule corrected or retired;
- regression check added/updated.

Do not leave both contradictory active rules in place after a decision.

## 5. ABSOLUTE BOUNDARIES

External/non-negotiable boundaries remain binding, including applicable safety,
security, accessibility and platform/tool constraints.

If a user preference conflicts with such a boundary:
- inform the user of the conflict;
- explain which outcome is unavailable and why;
- ask for a decision among compliant alternatives when multiple alternatives exist;
- never silently reinterpret the preference.

## 6. MODEL-INDEPENDENT BEHAVIOR

This framework is written as an observable contract, not model-specific advice.

A compliant AI should be testable by asking:
- Did it detect the contradiction before editing?
- Did it identify both owning rules?
- Did it ask the user to decide?
- Did it wait?
- Did it update context before regenerating?
- Did it remove/prevent the contradiction afterward?

Any "no" is a framework failure.
