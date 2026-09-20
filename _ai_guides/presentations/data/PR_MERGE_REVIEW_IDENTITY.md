---
name: pr_merge_review_identity
description: MANDATORY — canonical acquisition and rendering rules for merger and actual reviewer identity
metadata:
  type: data-contract
  critical: true
  required_before: composition
  version: 1.0
---

# PR MERGE + REVIEW IDENTITY — HARD DATA CONTRACT

This file exists to prevent merged-PR cards from showing empty `Merged:` / `Review:` fields when GitHub contains verifiable identity data.

## 1. MERGER IDENTITY

For every merged PR shown in the deck, attempt to resolve the person who actually merged it.

Canonical evidence order:
1. PR field `merged_by.login` when available.
2. Merge commit metadata when the PR endpoint omits `merged_by` but the merge commit clearly identifies the actor.
3. GitHub event/timeline evidence if available through the registered connector.

Do **not** use PR author, assignee or commit author as a substitute for merger identity.

If no registered source can verify the merger after the required lookup, leave the value blank internally and record the lookup failure in audit.

## 2. ACTUAL REVIEWER IDENTITY

For every merged PR shown in the deck, fetch submitted PR reviews.

The source must be the submitted review collection / review timeline, e.g. connector action equivalent to `list_pull_request_reviews` or a PR timeline that contains submitted reviews.

Use:
- `APPROVED` reviews as the canonical reviewer(s) for the visible `Review:` field.
- If multiple people approved, list all verified approving reviewers in a compact form.

`requested_reviewers` is **not** evidence that a review happened.
Never use `requested_reviewers` to populate the visible `Review:` field on merged PR cards.

Review comments or ordinary issue comments are not automatically approvals. They may count as review work elsewhere only when the presentation's activity model explicitly allows that.

## 3. REQUIRED LOOKUP SEQUENCE FOR EACH MERGED PR

Before rendering a merged-PR card:
1. Fetch PR metadata.
2. Resolve `merged_at` and base branch.
3. Resolve merger identity using section 1.
4. Fetch submitted reviews.
5. Collect all unique reviewers with `state == APPROVED`.
6. Map GitHub login to team display name when roster mapping exists.
7. Store source evidence in audit/data model.
8. Render `Merged:` and `Review:` from these verified values.

Do not skip steps 3–5 merely because basic PR metadata was already fetched.

## 4. VISIBLE CARD FORMAT

Canonical format:

```text
Merged: {MERGER_DISPLAY_NAME} | Review: {REVIEWER_DISPLAY_NAME}
```

Multiple approving reviewers:

```text
Merged: {MERGER_DISPLAY_NAME} | Review: {REVIEWER_A}, {REVIEWER_B}
```

If one identity remains genuinely unverifiable after the required lookup:

```text
Merged: {MERGER_DISPLAY_NAME} | Review:
```

or

```text
Merged: | Review: {REVIEWER_DISPLAY_NAME}
```

Do not print `ej verifierat`, `okänd`, technical API notes or retrieval diagnostics on the meeting card.

## 5. FAILURE CONDITIONS

The data/composition gate fails when:

```text
merged_pr_without_merger_lookup_count > 0
merged_pr_without_submitted_reviews_lookup_count > 0
review_field_populated_from_requested_reviewers_count > 0
verified_approving_reviewer_omitted_from_card_count > 0
verified_merger_omitted_from_card_count > 0
```

If a lookup endpoint is unavailable, record this explicitly in audit before continuing under the system contract. Do not silently treat missing lookup as "no reviewer".

## CORE PRINCIPLE

**Empty `Merged:` or `Review:` is allowed only after the dedicated identity lookup has actually been performed and produced no verifiable value.**

---

**Status:** PRODUCTION
**Version:** 1.0
**Last updated:** 2026-09-17
