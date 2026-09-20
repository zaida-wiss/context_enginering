---
name: data_collection_mandatory
description: How to collect attribution and team branch data for presentation rendering
metadata:
  type: process
  critical: true
  synced_with: DATA_ACQUISITION_CONTRACT.yaml v1.0
---

# DATA COLLECTION MANDATORY

**This file describes HOW to collect the actual data for presentations.**
**It is the implementation guide for DATA_ACQUISITION_CONTRACT.yaml**

---

## Core Collection Strategy

**Primary Data Source:** GitHub API (live)
**Secondary Sources:** GitHub web UI, Google Sheets (if API fails)
**Authority:** Data must be current as of REPORTING_PERIOD_END

---

## Attribution Fields (Required for Every PR)

### Merged PR Attribution Chain

For each **merged PR to the selected project's registered primary integration branch** or **registered collection branch**:

1. **Developed by** (WHO WROTE THE CODE)
   - Query: `pr.commits[].author.login` — actual commit authors (PRIMARY)
   - Fallback: `pr.assignees[].login` — assigned team members
   - Fallback: `pr.user.login` — PR opener
   - Output: List all commit authors if multiple, ordered by commit count

2. **Reviewed by** (WHO DID REVIEW WORK)
   - Query: `pr.reviews[].user.login` with `reviews[].state`
   - Include: APPROVED, CHANGES_REQUESTED, COMMENTED
   - Meaning: All three states represent actual review labor
   - Output: List reviewer + state indicator (✅ APPROVED, ⚠️ CHANGES_REQUESTED, 💬 COMMENTED)

3. **Merged by** (WHO COMPLETED THE ACTION)
   - Query: `pr.merged_by.login` — person who clicked merge
   - Output: One person only (the merger)

### Collection Branch Treatment

Registered collection branches track work before delivery to the selected project's primary integration branch.

**Same attribution chain** applies to collection PRs:
- Commits → authors
- Reviews → all submitted review states
- Merged by → collection merger

---

## Deduplication Rule (CRITICAL)

When same work appears in BOTH collection branch AND develop branch:

**Deduplicate by WORK IDENTITY, not PR number:**

1. Check **linked_issue_ids** — if both PRs link same issue, they are same work
2. Check **commit SHA ancestry** — if commits appear in both PRs, same work
3. Check **source branch + commit set** — if same changes, same work

**Result:** Prefer the final primary-integration delivery when the selected project's repository-flow presentation rule requires a single representation. Hide the intermediate collection PR in that case.

---

## Data Collection Checklist

### Before Rendering

- [ ] Merged PRs fetched from API or GitHub web
- [ ] For EACH merged PR:
  - [ ] commits[] populated with author.login
  - [ ] reviews[] populated with user.login + state
  - [ ] merged_by.login recorded
  - [ ] linked_issues[] recorded
- [ ] Every collection branch registered by the selected project's repository-flow config scanned
- [ ] Collection branch PRs use SAME attribution chain
- [ ] Deduplication applied: linked issues + commit ancestry checked
- [ ] Every member in the selected project's canonical roster is accounted for (or explicitly shown as having no verified work)

### Verification Before Presentation

- [ ] No PR shown twice (dedup verified)
- [ ] All reviewers shown with review state (not just APPROVED)
- [ ] Developed by uses actual commit authors when available
- [ ] Merged by shows who pressed the button
- [ ] Collection branch work clearly labeled (diff color/marker)
- [ ] Cross-check: GitHub web UI shows same PR count for time period

---

## Integration Points

**Uses from:** DATA_ACQUISITION_CONTRACT.yaml
**Feeds to:** `monday_meeting/design/SLIDE_DETAIL_SPEC.md`. The retired
`AI_PROMPT_GENERATE_PRESENTATION.md` must not be used.
**Validated by:** RENDER_GATE_CHECKLIST.md (DELIVERY SEPARATION & REVIEW STATES section)

---

## Status

**Version:** 1.0  
**Status:** PRODUCTION — synced with DATA_ACQUISITION_CONTRACT.yaml v1.0
