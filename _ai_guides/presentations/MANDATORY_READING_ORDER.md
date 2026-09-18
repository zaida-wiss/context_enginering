---
name: mandatory_reading_order
description: Minimal router for presentation tasks
metadata:
  type: router
  critical: true
  version: 2.0
---

# Presentation task router

This file is the short entry route for presentation work. It routes the AI to
the files that own the rules; it does not repeat those rules.

## Start sequence

Read these once, in this order, from the same repository ref as the entry README:

1. `AUTHORITY_REGISTRY.yaml`
   - establishes which files are active
   - identifies the owner for each rule category
   - remains the authority map throughout the task

2. `INTEGRITY_CONSTRAINT.md`
   - establishes what counts as verified project information
   - defines how incomplete or uncertain data is handled

3. `SYSTEM_CONTRACT.yaml`
   - establishes the execution flow, gates and delivery process
   - resolves which task-specific authorities and data dependencies are needed

## Task routing

After the start sequence:

- identify the requested presentation task
- load only the active authorities and supporting data required for that task
- resolve source locations through the registered context/data routing
- execute the task using the sequence in `SYSTEM_CONTRACT.yaml`
- validate the finished artifact with the registered validators before delivery

For Monday Meeting presentations, the active task-specific content and design
authorities are resolved through `AUTHORITY_REGISTRY.yaml`; this router does not
duplicate their rules or file lists.

## Repository ref

The branch, tag or commit used for the entry README is the execution ref.
Use that same ref for every internal context file during the run.

## Design principle

The routing path stays small and stable:

```text
README
  → MANDATORY_READING_ORDER
    → AUTHORITY_REGISTRY
      → INTEGRITY_CONSTRAINT
        → SYSTEM_CONTRACT
          → task-specific authorities + registered data
            → validation
              → delivery
```

A change to presentation behavior is made in the authority that owns that rule.
This router changes only when the routing structure itself changes.

---

**Status:** ACTIVE ROUTER
**Version:** 2.0
**Last updated:** 2026-09-18
