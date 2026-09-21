---
name: sources_guide
description: Generic guide to project-resolved external source registries
metadata:
  type: reference
  critical: false
---

# External sources — generic routing guide

Global framework files do not own project source IDs, URLs, document IDs,
repository names or fallback endpoints.

For project work:

1. resolve the selected project through `PROJECTS.yaml`;
2. load its manifest;
3. resolve `context.sources.path`;
4. use only the source definitions and access methods declared there.

Project-specific source examples belong inside the owning project root.
Global documentation may use only synthetic placeholders such as:

```yaml
source_id: "EXAMPLE_CURRENT_WORK"
reference: "selected project source registry"
```

Do not place real project URLs, sheet/document IDs, branch names or source IDs
in this global guide.

---
status: ACTIVE_GENERIC_REFERENCE
