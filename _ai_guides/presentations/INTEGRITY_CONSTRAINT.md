---
name: integrity_constraint
description: Non-negotiable data integrity rule — no hallucinations, no guesses
metadata:
  type: rule
  critical: true
  enforced: always
---

# 🛑 INTEGRITY CONSTRAINT — NON-NEGOTIABLE

## The Rule

**If you cannot obtain ALL required data from registered sources ONLY:**

You MUST STOP immediately.

You are FORBIDDEN to:
- ❌ Guess on assignees, reviewers, or owners
- ❌ Hallucinate issue numbers or PR data
- ❌ Improvise GitHub metadata
- ❌ Use unregistered sources as fallback
- ❌ "Fill in the blanks" with invented data
- ❌ Deliver a presentation with incomplete or unverified data

## Why This Matters

If you deliver a presentation with fabricated data:

1. **The team makes decisions based on FALSE information**
2. **Decisions based on false data cause real harm**
3. **You have not helped — you have DAMAGED the process**

It does not matter if you "delivered something". 

A false deliverable is worse than no deliverable.

## What "Verified Data" Means

For EACH data point in the presentation:

- **Source:** Must be registered in EXTERNAL_SOURCES.yaml
- **Access method:** Must be in allowed_implementations
- **Verification:** Must be confirmed in DATA_ACQUISITION_RECEIPT
- **Fallback chain:** Must follow EXTERNAL_SOURCES.yaml order
- **Status:** Must be SUCCESS (not INCOMPLETE, not GUESSED)

If ANY data point cannot be verified:
- Report which dataset failed
- Report why it failed
- STOP before rendering

## Decision Tree

```
Can you get ALL required data from registered sources?
├─ YES → Continue to build_gate ✓
└─ NO → 
    ├─ Try registered fallbacks?
    │  ├─ YES, fallback works → Continue ✓
    │  └─ NO, fallback fails → STOP (go to "Failure" below)
    └─ STOP (see "Failure" below)

Failure: Cannot complete data collection
├─ Report which datasets are INCOMPLETE
├─ Report why each failed (blocked, unavailable, etc.)
├─ Do NOT guess or fabricate
└─ STOP before rendering
```

## This Is Not Negotiable

This rule exists to protect the team from hallucinated data.

If you choose to ignore this rule because:
- "It's faster to guess"
- "The rules seem ceremonial"
- "Incomplete data is better than no data"
- "I'll just fill in the obvious parts"

Then you have chosen to harm the team's decision-making.

You have failed.

---

**Read this FIRST, before reading anything else in the presentation system.**

If you commit to following this rule exactly — even if it means STOP with incomplete data — you are ready to continue.

If you plan to rationalize your way around this rule: STOP now.
