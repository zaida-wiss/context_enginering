---
name: ai_prompt_generate_presentation
description: COPY THIS PROMPT — Direct instructions for any AI to generate presentation from LIVE GitHub data
metadata:
  type: critical_instruction
  audience: ChatGPT, Claude, Gemini — any AI asked to generate presentation
---

# 🤖 AI PROMPT — Generate Avanza Team 1 Presentation

**Copy-paste denna prompt direkt till vilken AI som helst du ber om att skapa en presentation.**

---

## YOUR TASK

Generate a presentation for Avanza Team 1 Monday meeting following the deterministic pipeline in this context repo.

**CRITICAL: This is NOT a loose template. Follow the EXACT structure and LIVE GitHub data sources specified.**

---

## STEP 1 — READ MANDATORY FILES (15-20 min read)

Before doing ANYTHING, read these three files completely:

1. **MANDATORY_READING_ORDER.md**
   - https://github.com/zaida-wiss/context_enginering/blob/main/_ai_guides/presentations/MANDATORY_READING_ORDER.md
   - (Execution order, hierarchy, render-gate rules)

2. **SLIDE_DETAIL_SPEC.md**
   - https://github.com/zaida-wiss/context_enginering/blob/main/_ai_guides/presentations/monday_meeting/design/SLIDE_DETAIL_SPEC.md
   - (Exact slide ①-⑭ specifications, titles, content rules)

3. **TEMPLATE_REFERENCE.html**
   - https://github.com/zaida-wiss/context_enginering/blob/main/_ai_guides/presentations/monday_meeting/design/TEMPLATE_REFERENCE.html
   - (NPF-friendly design principles — NO TABLES, Symbol+Färg+Text only)

---

## STEP 2 — MANDATORY: DATA ACQUISITION (Follow DATA_ACQUISITION_CONTRACT.yaml)

**Read this FIRST:** `DATA_ACQUISITION_CONTRACT.yaml` — canonical acquisition method
**Then follow:** `DATA_COLLECTION_MANDATORY.md` — implementation guide with checklist

🚨 **If any PRIMARY source fails → STOP and report DATA_ACQUISITION_RECEIPT with status**
Never skip a source or substitute with fallback without trying primary first.

### Required Datasets (in order)

**DATASET 1: Team Roster (Local)**
- Read `TEAM_ROSTER.md` — 7 members with GitHub login + display name
- Verify all members appear in later work attribution

**DATASET 2: Merged PRs (GitHub API → develop branch)**
- URL: `https://api.github.com/repos/chas-challenge-2026/avanza-team1/pulls?state=closed&base=develop&merged:>=[REPORTING_PERIOD_START]`

**MANDATORY FIELDS (ALL MUST be extracted for each PR):**
- Extract: `pr.commits[].author.login` (actual code authors — PRIMARY for "Developed by")
- Extract: `pr.reviews[].user.login` + `reviews[].state` (APPROVED, CHANGES_REQUESTED, COMMENTED all count as "Reviewed by")
- Extract: `pr.merged_by.login` (MANDATORY — who actually merged the PR for "Merged by")
- Extract: `pr.linked_issues[]` (for deduplication via linked_issue_ids)

**CRITICAL RULE:**
- ❌ NEVER write "ej verifierat", "not verified", "GitHub-merge", or similar placeholder when GitHub data exists
- ✅ IF `pr.merged_by.login` exists → use it
- ✅ IF `pr.reviews[]` with APPROVED exists → use it
- ✅ IF neither exists → write "Ej verifierbart" ONLY
- ❌ Do NOT guess from PR author, assignee, or merge commit author

- Fallback: GitHub web UI (https://github.com/chas-challenge-2026/avanza-team1/pulls?q=is:pr+is:merged)

**DATASET 3: Collection Branch Merges (GitHub API)**
- Known branches: Java-Development-Environment (Backend), C/C++-Native (Native)
- Same attribution chain as Dataset 2
- CRITICAL: Apply DEDUPLICATION using `linked_issue_ids + commit_sha_ancestry`
  - If same work appears in both branches, show ONLY develop delivery
- Fallback: GitHub web UI per-branch

**DATASET 4: Open PRs + Active Issues (GitHub API)**
- Open PRs: `https://api.github.com/repos/chas-challenge-2026/avanza-team1/pulls?state=open`
- Active issues: `https://api.github.com/repos/chas-challenge-2026/avanza-team1/issues?state=open&updated:>=[REPORTING_PERIOD_START]`
- Extract: assignees, review requests, activity timestamps

**DATASET 5: Recent Commits (for pågår evidence)**
- Per-branch commits: `https://api.github.com/repos/chas-challenge-2026/avanza-team1/commits?sha=[branch]&since=[REPORTING_PERIOD_START]`
- Branches: develop, Java-Development-Environment, C/C++-Native, and any team branches
- Extract: author.login, commit.message, authored_at (proof of active work)

---

## STEP 3 — VERIFY ATTRIBUTION & DEDUPLICATION (Critical integrity check)

After collecting all datasets:

1. **Verify all 7 team members appear somewhere:**
   - Frontend: Tomac, Björn, Zaida
   - Backend: Erik, Rasha
   - Native: Pär, Henrik
   - If missing → show "○ [Name] — Ny issue eller tillgänglig för hjälp i [team]" (NOT "inaktiv")

2. **Apply DEDUPLICATION using linked_issue_ids + commit_sha_ancestry:**
   - Check if Collection branch PR #X and Develop PR #Y represent same work
   - Look for: same linked issue OR same commits in ancestry
   - Rule: Show ONLY the Develop delivery (final state)
   - Log deduplication decisions for verification

3. **Verify Reviewed-by includes ALL review states:**
   - NOT just "APPROVED" 
   - Include: APPROVED (✅), CHANGES_REQUESTED (⚠️), COMMENTED (💬)
   - All show as review work

4. **Verify Developed-by uses actual commit authors:**
   - NOT just PR author
   - Priority: commits[] > assignees[] > pr.user (fallback only)

---

## STEP 3.5 — VERIFY REPOSITORY STATE

**Before building presentation, verify you're reading current HEAD:**

**Output these verification lines before any other output:**

```
═══════════════════════════════════════════════════════════
REPOSITORY STATE VERIFICATION
═══════════════════════════════════════════════════════════

Requested branch: cleanup
Remote HEAD: [fetch latest SHA from origin/cleanup]
Instruction files loaded from SHA: [show actual loaded SHA]
MATCH: [YES or NO — must be YES to proceed]

Latest commit message: [show actual latest commit]
Timestamp: [show author date]

═══════════════════════════════════════════════════════════
```

**If MATCH is NO:**
- STOP immediately
- Do NOT proceed to data acquisition
- Report: "Branch mismatch — loaded from old SHA"

**If loaded SHA is stale (>30 min old):**
- Re-run acquisition step to get fresh data
- Update DATA_ACQUISITION_RECEIPT with new timestamp

---

## STEP 4 — BUILD PRESENTATION

**CRITICAL: Follow SLIDE_DETAIL_SPEC.md exactly for content + VISUAL_DESIGN_MANDATORY.md for rendering**

### ARTIFACT CREATION ORDER — MANDATORY

Before any Artifact/Open/Render operation:

1. **Determine output path** — where will presentation HTML live?
2. **Create the source artifact file** — write HTML to that path
3. **Verify file exists** — check that file was created successfully
4. **Verify file is non-empty** — file size > 0 bytes
5. **Only then open/render/convert** — start render-to-PPTX
6. **If creation fails → STOP** — report ARTIFACT_BUILD_ERROR

**Never attempt to open or render a source file that has not yet been created.**

### Slides ① — Avklarat sedan förra mötet (Global overview)

- **Slide ①A** "① Avklarat sedan förra mötet" — ALL merged PRs to develop (chronological, 3×2 card grid, max 6)
  - Cards show: PR#, title, Developed by (commit authors), Reviewed by (all states), Merged by
  - Team-colored borders (teal/pink/purple/slate)
  - Soft rounded cards (12–18px corners)

- **Slide ①B** (if relevant) "① Avklarat sedan förra mötet — Collection branches" — Merged to Java-Development-Environment, C/C++-Native
  - Same format as ①A
  - Apply deduplication: don't show if already in Develop
  - Different presentation-time label ("merged to collection")

### Slides ① continued — Pågår denna vecka (In progress work)

- **Slide ①C** "① Pågår denna vecka — Per team" — Open PRs + active work per team (Frontend, Backend, Native sections)
  - Full-width stacked cards
  - Show: PR#, issue#, assignee, review status, blockers

- **Slide ①D** "① Pågår denna vecka — Cross-team" — Work affecting multiple teams (if any)
  - Light slate border (#CBD5E1)
  - Full-width stacked cards

### Team Detail Slides (③④⑤) — COMPACT VERTICALLY STACKED RESPONSIVE CARDS

- **Slide ③** "③ Frontend — denna vecka" — Issue-status per card + operativ plan
- **Slide ④** "④ Backend — denna vecka" — Issue-status per card + operativ plan
- **Slide ⑤** "⑤ Native — denna vecka" — Issue-status per card + operativ plan

**MANDATORY LAYOUT (per TEAM_DETAIL_CARDS section in VISUAL_DESIGN_MANDATORY.md):**
- One issue/work item per card
- Vertically stacked (NOT horizontal bands, NOT tables)
- Text horizontally centered inside each card
- Card height is CONTENT-DRIVEN (grows to fit text)
- Cards may have different heights (acceptable and expected)
- Generous spacing between cards (20px minimum)
- NO TEXT CLIPPING — text must always fit inside card

**Card content per line:**
```
    ✓ #93 · PR #95
    SQL-injection fix
    
    Merged to develop
    
       Tomac
    Review: Erik
```

**Legend:** ✓ AVKLARAT, ◐ PÅGÅR, ✕ BLOCKERAD, ? OKÄND

**Design for all slides:**
- Dark navy background (#0F1830)
- Soft rounded cards/table cells (12–18px corners)
- Team-colored borders (borders only, NOT full background)
- Internal padding: 16–20px
- Typography: 28pt headers (bold), 13pt body (regular), 12pt metadata
- Responsive height: NO TEXT CLIPPING (split to new slide if needed)

---

## STEP 5 — BEFORE RENDERING: Run RENDER_GATE_CHECKLIST.md

Read: `verification/RENDER_GATE_CHECKLIST.md`

This checklist MUST pass before delivering presentation:
- Layout compliance (①A grid, ①B-①D full-width, ③④⑤ responsive cards)
- Visual design (soft cards, 12-18px corners, responsive height)
- Data integrity (no duplicates, dedup verified, checksums aligned)
- Attribution accuracy (commits > assignees > PR author priority)
- Review states (APPROVED + CHANGES_REQUESTED + COMMENTED all shown)
- WCAG compliance (contrast, color separation, no text clipping)

**Framsida footer MUST show:**
```
✅ [N] sources verified — Data från [DATE] [TIME] UTC
Sources: GitHub PRs, commits, issues, collection branches
```

If any source failed:
```
⚠️ GitHub [source name] fallback used (partially unavailable)
```

---

## STEP 6 — FINAL QUALITY CHECKS (Before delivery)

After rendering to PPTX:
- ☐ Open in PowerPoint and page through every slide
- ☐ Verify NO text clipping or overflow
- ☐ Verify responsive card heights working correctly
- ☐ Verify all 7 team members visible somewhere (work or "available")
- ☐ Verify ①A shows 3×2 grid (max 6 cards)
- ☐ Verify ①B-①D show full-width stacked cards
- ☐ Verify ③④⑤ show compact vertically stacked cards with centered text (NOT tables)
- ☐ Verify colors: team borders correct, status symbols clear
- ☐ Verify deduplication applied (no PR shown twice)

---

## MANDATORY FAILURE REPORTING

If you CANNOT complete ANY step:

1. **STOP rendering**
2. **Report exactly which step failed:**
   - "Step 2, Source 1: GitHub merged PRs not accessible"
   - "Step 3: Cannot verify all 7 team members"
   - "Step 4: Cannot read SLIDE_DETAIL_SPEC.md"

3. **Never skip a step. Never use cached data. Never hide failures.**

---

## DO NOT

- ❌ Use cached/snapshot data — fetch LIVE from GitHub
- ❌ Skip data acquisition steps — follow DATA_ACQUISITION_CONTRACT.yaml
- ❌ Forget deduplication — use linked_issue_ids + commit_sha_ancestry (not just PR IDs)
- ❌ Show only "APPROVED" reviews — include CHANGES_REQUESTED + COMMENTED as review work
- ❌ Use PR author as "Developed by" — use commit authors (primary) > assignees > PR author
- ❌ Show "inaktiv" or "ingen aktivitet" — use "Ny issue eller tillgänglig för hjälp i [team]" instead
- ❌ Write "ej verifierat", "not verified", "GitHub-merge", or similar placeholder when GitHub data exists
  - ✅ IF merged_by.login exists in GitHub → use it (never write "GitHub-merge")
  - ✅ IF reviews[] exists in GitHub → use reviewer name (never write "not verified")
  - ✅ ONLY write "Ej verifierbart" if GitHub truly lacks the data AND cannot be fetched
- ❌ Render ③④⑤ as tables or horizontal bands — MUST be compact vertically stacked cards with centered text
- ❌ Use corner radius < 12px or > 18px on soft cards
- ❌ Clip text to fit cards — split to new slide instead
- ❌ Hide data verification failures or source unavailability

---

## SUCCESS CRITERIA

✅ LIVE GitHub data fetched (today's date, all 5 datasets collected)  
✅ Data integrity checklist passed (dedup, attribution, reviews verified)
✅ All 7 team members appear (with work or "available" marker, never "inactive")
✅ Slide structure correct (①A grid, ①B-①D full-width, ③④⑤ responsive cards)
✅ Design compliant (dark navy, soft cards 12-18px, responsive height, no clipping)
✅ Team colors correct (borders only, not backgrounds; never overlap status colors)
✅ Framsida footer shows verified sources + timestamp
✅ Render-gate checklist PASSED (run before delivery)  
✅ Actually rendered to PPTX and visually verified (not just generated)

---

**This prompt is stored in the context repo so any AI can find and follow it automatically.**

**Last updated:** 2026-09-14
