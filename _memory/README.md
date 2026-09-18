# Memory — Project Context Index

`_memory` contains long-lived project knowledge.

Canonical repository paths and task bundles are resolved through
[`CONTEXT_REGISTRY.yaml`](../CONTEXT_REGISTRY.yaml).

## Canonical memory

| File | Purpose |
|---|---|
| [`TEAM_ROSTER.md`](TEAM_ROSTER.md) | Team membership and verified GitHub identities |
| [`GITHUB_MEMBER_MAPPING.md`](GITHUB_MEMBER_MAPPING.md) | GitHub username mapping; candidate for consolidation into TEAM_ROSTER |

## Other domains

- project instructions → [`_ai_guides/project/`](../_ai_guides/project/)
- living/manual course data → [`data/manual/course/`](../data/manual/course/)
- manual design sources → [`data/manual/design/`](../data/manual/design/)
- derived data → [`data/derived/`](../data/derived/)
- presentation schemas/instructions → [`_ai_guides/presentations/`](../_ai_guides/presentations/)

The memory index does not duplicate rules or live facts.

## Migration audit

Current classification and migration state is recorded in:

- [`_audit/MEMORY_DOMAIN_INVENTORY.yaml`](../_audit/MEMORY_DOMAIN_INVENTORY.yaml)

---

**Status:** canonical memory index
**Last updated:** 2026-09-18
