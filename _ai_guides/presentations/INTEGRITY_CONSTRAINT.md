---
name: integrity_constraint
description: Positive data-integrity contract for verified presentation content
metadata:
  type: rule
  critical: true
  enforced: always
  version: 2.0
---

# Data integrity contract

## Purpose

This file defines what counts as trustworthy project information in presentation work.

The goal is to produce a presentation that the team can safely use for planning
and decisions. Every factual statement therefore has a traceable source and a
clear verification state.

## Verified data standard

A factual data point is ready for use when all applicable conditions are met:

- **Source:** the source is registered in `data/SOURCES.yaml`
- **Access method:** the access method is registered for that source
- **Verification:** the acquisition result is recorded in the current data-acquisition receipt
- **Fallback order:** registered fallbacks are followed in their defined order when needed
- **Status:** the data point is verified as available, or clearly represented as incomplete/unknown according to the owning content rule

Examples of factual fields covered by this standard include:

- issue and PR numbers
- assignees and owners
- reviewers and merger identity
- branch names
- timestamps and deadlines
- meeting facts
- project status and source-derived technical facts

## Working with incomplete information

When a required dataset cannot be verified:

1. record which dataset is incomplete
2. record the reason the source could not be verified
3. apply the gate defined in `SYSTEM_CONTRACT.yaml`
4. continue only when that gate allows incomplete data to be represented explicitly
5. keep unknown information visibly unknown rather than converting it into a factual value

This preserves useful verified material while keeping the boundary between
known and unknown information clear.

## Data acquisition flow

```text
registered source
    ↓
registered access method
    ↓
successful acquisition
    ↓
verification receipt
    ↓
verified factual content
```

When the primary source is unavailable:

```text
primary source unavailable
    ↓
registered fallback order
    ↓
verified fallback succeeds → use verified result
    ↓
all applicable fallbacks unavailable → mark dataset incomplete
    ↓
SYSTEM_CONTRACT gate decides the next action
```

## AI interpretation

Verified source data and AI interpretation are separate layers.

- verified source information is presented with its source provenance
- model-derived interpretation is labeled `🔎 AI-analys`
- model-derived recommendations are labeled `⭐ AI-förslag`
- uncertain source origin is represented with `⚠ Källa behöver verifieras`

The canonical symbol and text are defined by
`design/PROVENANCE_AND_AI_LABELING.md`.

## Relationship to the presentation pipeline

This file owns **data integrity semantics**.

The surrounding files have separate roles:

- `AUTHORITY_REGISTRY.yaml` identifies which files own each rule category
- `SYSTEM_CONTRACT.yaml` decides execution flow and STOP/CONTINUE gates
- `data/SOURCES.yaml` owns source definitions, access methods and fallback order
- `data/DATA_ACQUISITION_CONTRACT.yaml` owns the acquisition procedure
- `design/PROVENANCE_AND_AI_LABELING.md` owns visual/source labeling

The presentation router determines when this file is read. This file does not
define its own position in the reading order.

## Success condition

Presentation facts are considered integrity-safe when:

```text
registered_source == true
source_access_is_registered == true
verification_state_is_known == true
unknown_values_remain_explicit == true
ai_interpretation_is_labeled == true
```

---

**Status:** ACTIVE
**Version:** 2.0
**Last updated:** 2026-09-18
