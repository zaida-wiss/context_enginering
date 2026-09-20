---
name: presentations_navigation
description: Navigation for the presentation system
metadata:
  type: navigation
  status: active
---

# Presentation system

Start with [`MANDATORY_READING_ORDER.md`](MANDATORY_READING_ORDER.md).

That route loads the global framework, the presentation authority registry and the active owners required for the task. Do not recover production rules from retired or historical guides.

## Authority map

Use [`AUTHORITY_REGISTRY.yaml`](AUTHORITY_REGISTRY.yaml) to determine:
- active rule owners;
- validators;
- supporting data models;
- references;
- retired material.

Navigation files do not own presentation behavior. Meeting-point structure, content, design, acquisition, accessibility, provenance, conflict handling and delivery are owned by the files registered in the authority registry.

## Maintenance

When feedback reveals a recurring framework defect, update the active authority that owns that category, then run the registered validation/smoke checks.

If two active authorities genuinely conflict, follow the global conflict-decision gate: stop the affected work, identify the competing rules and consequences, and ask the user to decide before resolving the conflict.

Project-specific facts belong in registered project data/memory/source configuration, not in this navigation file.
