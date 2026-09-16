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

## STEP 2 — MANDATORY: FETCH LIVE GITHUB DATA

**You MUST visit and read data from these 5 GitHub URLs. Do NOT skip any.**

🚨 **If you cannot reach ANY source → STOP and report: "⚠️ GitHub [source] not accessible"**  
Never skip a source because you couldn't reach it.

### Source 1: Merged PRs (PRIMARY for Slide ①)
```
https://github.com/chas-challenge-2026/avanza-team1/pulls?q=is:pr+is:merged+merged:>=[TODAY-7d]
```
**What to extract:**
- PR number, title, assignee (owner of work), merge date
- Count total merged PRs this week
- Group by team (Frontend/Backend/Native)

### Source 2: Commits (Proof of work)
```
https://github.com/chas-challenge-2026/avanza-team1/commits/develop?since=[TODAY-7d]&until=[TODAY]
```
**What to extract:**
- Author, commit message, date
- Group by person and work area
- Count commits per team member

### Source 3: Open PRs (In progress, awaiting review)
```
https://github.com/chas-challenge-2026/avanza-team1/pulls?q=is:pr+is:open+updated:>=[TODAY-7d]
```
**What to extract:**
- PR number, title, assignee, review status
- How many commits since creation?
- Who is waiting for review?

### Source 4: Project Board Status
```
https://github.com/orgs/chas-challenge-2026/projects/31
```
**What to extract:**
- Which issues moved to "Done" this week?
- Which are "In Progress"?
- Which are "In Review"?

### Source 5: Open Issues with activity
```
https://github.com/chas-challenge-2026/avanza-team1/issues?q=is:issue+is:open+updated:>=[TODAY-7d]
```
**What to extract:**
- Issue number, title, assignee
- Any recently updated/commented on?

---

## STEP 3 — VERIFY ALL 7 TEAM MEMBERS

From TEAM_ROSTER.md, verify you found work for:

**Frontend:**
- Tomac Barin Jansson
- Björn Boman
- Zaida Wiss

**Backend:**
- Erik Berglund
- Rasha Knifdi

**Native/System:**
- Pär Lundh
- Henrik Westerlund

If anyone is missing → Slide must show "❌ Ingen aktivitet denna vecka" (No activity this week)

---

## STEP 4 — BUILD PRESENTATION

### Slide ① — Avklarat sedan förra mötet

**Title format (MUST match meeting protocol):**
- Slide ①A: "① Avklarat sedan förra mötet — Develop"
- Slide ①B: "① Avklarat sedan förra mötet — Collection branches"
- Slide ③: "③ Frontend — denna vecka"
- Slide ④: "④ Backend — denna vecka"
- Slide ⑤: "⑤ Native — denna vecka"

**NOT:** "Frontend — avklarat + pågår + review" ❌

**Design: NPF-friendly (NO TABLES)**
- Symbol + Färg + Text trio (not separate)
- 24px+ row height
- 14pt bold headers, 13pt body text
- Rounded corners (6-8px)
- Colored sections: 🟢 Grön (RGB 76,175,80) for Merged, 🟡 Orange (RGB 255,152,0) for In Progress

**Structure (3 sections per slide):**
1. ✅ MERGED DENNA VECKA — Merged PRs
2. ◐ PÅGÅR DENNA VECKA — Open branches with commits
3. ⏳ VÄNTAR PÅ REVIEW — Open PRs awaiting approval

---

## STEP 5 — DATA VERIFICATION & TIMESTAMPING

Every slide footer MUST show:
```
Data från [DATE] [TIME] UTC | Källor: GitHub PRs + Commits + Project Board ✅
```

If any GitHub source failed:
```
⚠️ GitHub [source name] kunde inte verifieras. Manuell verifiering krävs.
```

---

## STEP 6 — RENDER-GATE CHECKLIST

Before generating final presentation, verify:

- ☐ All 7 team members have work listed OR marked "Ingen aktivitet"
- ☐ Slide titles match "Avklarat sedan förra mötet — [Team]"
- ☐ No tables (NPF-friendly design only)
- ☐ All data is from LIVE GitHub (not cached/snapshot)
- ☐ Timestamp on every slide showing when data was fetched
- ☐ If any GitHub source failed → Clearly marked with ⚠️

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

- ❌ Use cached/snapshot data
- ❌ Skip GitHub sources because they're slow
- ❌ Use tables (NPF violation)
- ❌ Show individual team members without their team color badge
- ❌ Hide data verification failures
- ❌ Forget to timestamp all slides

---

## SUCCESS CRITERIA

✅ Presentation rendered from LIVE GitHub data (fetched today)  
✅ All 7 team members verified or marked "no activity"  
✅ Slide ① titles follow "Avklarat sedan förra mötet — [Team]"  
✅ NPF-friendly design (no tables, Symbol+Färg+Text)  
✅ Every slide timestamped with data fetch time  
✅ All GitHub sources either verified or marked ⚠️  

---

**This prompt is stored in the context repo so any AI can find and follow it automatically.**

**Last updated:** 2026-09-14
