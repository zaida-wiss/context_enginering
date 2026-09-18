# Memory — Project Context Index

`_memory` contains long-lived project knowledge and a small number of files
that are still awaiting migration to their canonical instruction/data domain.

Canonical repository paths and task bundles are resolved through
[`CONTEXT_REGISTRY.yaml`](../CONTEXT_REGISTRY.yaml).

## Long-lived project knowledge

| File | Purpose |
|---|---|
| [`TEAM_ROSTER.md`](TEAM_ROSTER.md) | Team membership and verified GitHub identities |
| [`GITHUB_MEMBER_MAPPING.md`](GITHUB_MEMBER_MAPPING.md) | GitHub username mapping; candidate for consolidation into TEAM_ROSTER |

## Pending instruction migration

These files currently remain in `_memory` only until their rules are migrated
to the appropriate `_ai_guides/project/` owner:

| File | Intended domain |
|---|---|
| `PROJEKTKONTEXT_AVANZA.md` | project instruction/router |
| `TEAMSTANDARDS.md` | project operating standards |
| `DEFINITION_OF_DONE.md` | project quality/workflow rules |
| `DEFINITION_OF_DONE_TEMPLATE.md` | project template |
| `RISK_REGISTER.md` | project template |
| `presentations/CURRENT_SPRINT.yaml` | presentation data schema |

## Living/manual data

Current course and assignment facts are stored under:

- [`data/manual/course/`](../data/manual/course/)
- [`data/manual/design/`](../data/manual/design/) when design-source migration is complete
- [`data/derived/`](../data/derived/) for reproducible derived state

The memory index does not duplicate live facts.

## Migration audit

Current classification and migration state is recorded in:

- [`_audit/MEMORY_DOMAIN_INVENTORY.yaml`](../_audit/MEMORY_DOMAIN_INVENTORY.yaml)

---

**Status:** transitional index
**Last updated:** 2026-09-18
