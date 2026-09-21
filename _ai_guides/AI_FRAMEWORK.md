---
name: ai_framework_guide
description: Human-readable guide to the normative global AI framework
metadata:
  type: explanatory_guide
  critical: false
  status: active
  normative: false
  version: 1.2
---

# GLOBAL AI FRAMEWORK — HUMAN GUIDE

> **Normative source:** [`AI_FRAMEWORK.yaml`](AI_FRAMEWORK.yaml)

This Markdown file is explanatory only. It must not define competing behavior.
If this guide and the YAML contract differ, the YAML file is the source of truth.

The framework applies to every AI task in this repository: coding, issues,
planning, risk work, documentation, presentations, reviews and audits.

## Writing AI instructions: positive, hierarchical and executable

When AI-facing rules are updated, describe the **desired behavior first**.

A strong instruction tells the model:
- what action to take;
- which authority owns the behavior;
- which hierarchy or router resolves the next step;
- in which order execution happens;
- what a correct result looks like;
- how completion is validated.

Use hard prohibitions for material boundaries such as project isolation,
destructive actions, genuine authority conflicts and data-integrity protection.
For ordinary behavior, prefer a complete positive execution path over a growing
list of negations.

Preferred pattern:

```text
Resolve scope → resolve owner → resolve target → execute → propagate → validate.
```

Instead of accumulating:

```text
Do not put it here.
Do not use that file.
Do not forget this other case.
```

When a material AI instruction changes, improve the hierarchy, desired state and
completion contract at the same time. Examples should demonstrate the correct
pattern first and remain synthetic/project-neutral at global scope.

The normative contract is
`AI_FRAMEWORK.yaml -> instruction_authoring_standard`.

## Context-first correction

When a recurring defect is caused by repository instructions, the context rule
is corrected first, regression protection is added when practical, and only then
is the affected artifact/output regenerated.

## Conflict decision gate

A genuine conflict means two active rules require incompatible outcomes.

The normative YAML contract requires the AI to:
- stop before choosing or modifying either conflicting rule;
- identify both rules and their owning files;
- explain the practical consequence of the available options;
- ask the user to decide;
- wait for the decision;
- record the decision and correct the context;
- add/update regression protection before continuing.

Authority rank is used to locate ownership and delegation. It does **not**
silently decide a genuine internal contradiction.

## Normal specialization is not a conflict

Different authorities may own different layers, for example global palette and
card spacing. A specific rule may also add detail to a general rule when the two
remain compatible.

## Decision trace

After a user resolves a conflict, the repository should retain a compact trace:
conflict, options, decision, authority update and regression protection.

## Absolute boundaries

Safety, security, accessibility, law and platform/tool constraints remain
binding. When a preference conflicts with such a boundary, explain the boundary
and ask the user to choose among compliant alternatives when there is more than
one.

For machine-readable behavior, validators and task routing, always use
`AI_FRAMEWORK.yaml`.
