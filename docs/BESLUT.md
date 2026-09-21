---
name: decisions_index
description: Index and storage guidance for global framework decisions
metadata:
  type: reference
  canonical_path: "docs/decisions/"
  updated: 2026-09-21
---

# Global framework decisions

This directory stores decisions about the reusable context-engineering framework.

Project-specific decisions belong under the selected project root, for example:

```text
projects/<project-id>/decisions/
```

Global decision files must remain project-neutral. They may use placeholders such
as `{TEAM_NAME}`, `{PRIMARY_BRANCH}` or synthetic `Team A`, but must not
contain real project names, people, repositories, branches, deadlines, course
facts or product-domain examples.

## Decision file shape

```markdown
---
id: <decision-id>
decision_date: YYYY-MM-DD
updated_date: YYYY-MM-DD
status: confirmed
---

# [Decision name]

## Decision
[Reusable framework decision]

## Impact
[How reusable behavior changes]
```

Project decision indexes and project presentation consumers resolve through the
selected project's manifest/context rather than this global index.

---
status: ACTIVE
