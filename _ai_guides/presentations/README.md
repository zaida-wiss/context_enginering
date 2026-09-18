---
name: presentations_navigation
description: Canonical navigation for the presentation system
metadata:
  type: navigation
  status: active
  updated: 2026-09-18
---

# Presentation system

## Production entry point

Start only with [`MANDATORY_READING_ORDER.md`](MANDATORY_READING_ORDER.md).
It loads [`AUTHORITY_REGISTRY.yaml`](AUTHORITY_REGISTRY.yaml), which determines
which files are active, validating, illustrative or retired.

Do not browse older guides to collect extra rules. If a required rule exists
only in a retired file, migrate it to the correct active authority before use.

## One owner per category

| Category | Owner |
|---|---|
| Execution, gates and delivery | `SYSTEM_CONTRACT.yaml` |
| Accessibility | `design/ACCESSIBILITY_NEURODIVERSITY.md` |
| Global layout and visual structure | `design/VISUAL_DESIGN_MANDATORY.md` |
| Readability minima | `design/READABILITY_HARD_RULES.md` |
| Card internals | `design/CARD_COMPONENT_STANDARD.md` |
| Source symbols and AI labeling | `design/PROVENANCE_AND_AI_LABELING.md` |
| Merger and submitted-review identity | `data/PR_MERGE_REVIEW_IDENTITY.md` |
| Responsive fit and pagination | `monday_meeting/design/LAYOUT_OVERFLOW_GUARD.md` |
| Meeting-point content | `monday_meeting/design/SLIDE_DETAIL_SPEC.md` |
| Data acquisition | `data/DATA_ACQUISITION_CONTRACT.yaml` |
| Allowed external sources | `_memory/EXTERNAL_SOURCES.yaml` |

## Current meeting-point 9 contract

Meeting points 3–5 remain Frontend, Backend and Native. Meeting point 9 uses
exactly four team columns:

`Frontend | Backend | Native | Cross-team`

Point 9 combines open PRs as `📌 #[PR-number]` with a grounded contribution
line, remaining assigned issues, delivery order, visible dependencies, justified
AI work allocation and suggested missing issues.
Source identity always retains its canonical symbol: `📅`, `✅`, `🔎`, `⭐` or
`⚠`. A tag, color or question mark never replaces these symbols.

## Conflict handling

Different categories must be applied together in registry order. If two active
files claim the same category and disagree, stop before composition and emit
the conflict receipt from `design/DESIGN_AUTHORITY.md`.

Retired files are listed in `AUTHORITY_REGISTRY.yaml` and have no production
authority even when their historical body uses words such as “mandatory”.

## Feedback after delivery

Discussion and feedback after a presentation target the context repository by
default. Improve the active instruction that owns the relevant rule so future
presentations reproduce the desired result.

Do not edit, regenerate or replace an already delivered presentation unless the
user explicitly asks for the presentation artifact itself to be updated.

If new feedback conflicts with an earlier active rule, report the old rule, the
new request and the consequence of each choice. Ask which is more important
before changing or retiring either rule. Recency alone does not resolve the
conflict, and rules must never be silently overwritten.

WCAG 2.2 AA is never part of that priority choice. If feedback conflicts with
accessibility or active readability minima, preserve WCAG, explain the conflict
and propose the closest accessible alternative.

## Collaborative contradiction audit

When asked to search for contradictions in the context repository, first perform
a read-only inventory. Present each conflict with its files, competing rules and
practical consequences in chat. Resolve unclear priorities together before
editing, deleting or retiring rules. After each decision, update the canonical
owner, clean up the duplicate and rerun the authority checks.

This audit never authorizes changes to an existing presentation artifact.
