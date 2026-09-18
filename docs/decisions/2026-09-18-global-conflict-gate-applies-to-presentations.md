# Decision — Global conflict gate applies to presentations

**Date:** 2026-09-18  
**Status:** Confirmed by user

## Conflict

The global normative contract in `_ai_guides/AI_FRAMEWORK.yaml` states that a
genuine conflict between active rules must STOP and require a user decision.

`_ai_guides/presentations/design/DESIGN_AUTHORITY.md` still used wording that
could be interpreted as letting authority order resolve conflicts automatically.

## User decision

Choose **A**.

The global AI conflict-decision gate applies to presentation work without
exception.

Authority order is used only to:
- identify rule ownership;
- identify delegation;
- identify absolute/non-negotiable boundaries.

Authority rank must never silently choose between two incompatible active
presentation intentions.

## Required behavior

When two active presentation rules genuinely conflict:
1. STOP the affected path.
2. Name both conflicting rules and files.
3. Explain the consequences of the available choices.
4. Ask the user to decide.
5. Wait.
6. Update the owning rules and regression protection.
7. Continue only after the conflict has been removed.

Normal specialization/delegation is not a conflict.
