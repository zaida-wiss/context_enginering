---
name: presentation_data
description: Single source of truth for weekly presentation — snapshot updated from GitHub, never read live by presentation tool
metadata:
  type: data
  snapshot_date: 2026-09-13
  snapshot_time: "08:42"
  snapshot_tz: "CEST"
---

# 📊 PRESENTATION_DATA.md — Snapshot för presentationen

**DETTA ÄR DEN ENDA FIL SOM PRESENTATIONEN FÅR LÄSA FÖR PROJEKTDATA**

Presentationen klonar ALDRIG något. Den läser bara denna fil.

---

## 📋 METADATA

**Snapshot Date:** 2026-09-13  
**Snapshot Time:** 08:42 CEST  
**Data Freshness:** ~ 1 hour old  
**Updated By:** [Who/Process — manual or automated]  

**Sources Verified:**
- ✅ GitHub branches (develop)
- ✅ Commits this week
- ✅ Open issues
- ✅ Open PRs
- ✅ Project Board
- ✅ Meeting protocol

---

## 🎯 VECKANS MÅL (Status sedan förra mötet)

**Frontend:**
- Progress: 80%
- Lead: Lisa
- Status: 🟢 ON TRACK
- Key issue: #40 Auth flow

**Backend:**
- Progress: 60%
- Lead: Marco
- Status: 🟠 SLIGHT DELAY
- Key blocker: FX integration waiting for Avanza meeting

**Native:**
- Progress: 40%
- Lead: Kris
- Status: 🔴 CRITICAL
- Key blocker: Waiting on Backend #45 API schema

---

## ✅ DENNA VECKA GJORDES

### Merged This Week
- ✅ #90 Frontend auth integration (Lisa) — enables secure login
- ✅ #92 Native error handling (Kris) — better error messages
- ✅ #87 Responsive layout (Ali) — users on all devices

### In Progress (Near Done)
- → #40 Auth flow (Lisa, 80%) — unblocks Backend #45
- → #52 Responsive tests (Ali, 60%) — quality assurance
- → #45 FX integration (Marco, blocked by external API)

### Blockers Solved
- 🔓 #78 (was blocked by external API) — solved by workaround
- 🔓 Native waiting on auth API — Frontend #40 near complete

**People Involved This Week:**
- Lisa (Frontend) — Auth flow, code reviews
- Ali (Frontend) — Responsive design, testing
- Marco (Backend) — FX calculation, documentation
- Jana (Backend) — Unit tests (40+ new cases)
- Kris (Native) — Error handling, accessibility
- Sam (Native) — Design review

**Leadership Comment:**
"Great progress this week. You broke a critical blocker and got closer to MVP. Kris and Marco together solved something that blocked Native for two weeks. Well done, team!"

---

## 🔄 DENNA VECKAS ARBETE OCH BIDRAG

### Frontend Team
- **Lisa — #40 Auth flow (16h)**
  - Enables users to log in securely
  - Unblocks Backend #45 (API integration)
  - Required for MVP demo to CTO
  - Status: 80% done, deploy Thursday

- **Ali — #52 Responsive layout (12h)**
  - Users can access portfolio on all devices
  - Dependency for Native #60 (mobile UI)
  - Status: testing phase, finish Thursday

- **Jan — Code review + documentation**
  - Reviewed #50, #51
  - Updated API docs for consistency

### Backend Team
- **Marco — #45 FX integration (20h)**
  - Calculates currency conversions correctly
  - Blocks Frontend #40 AND Native #60
  - Critical for customer demo (Avanza meeting)
  - Status: blocked by external API (workaround found)

- **Jana — #48 Unit tests (8h)**
  - 40+ new test cases
  - Increases code coverage to 70%+
  - Prevents regressions in #45 deployment

- **Anna — #51 Core refactoring**
  - Architecture improvements
  - Tech debt reduction
  - Status: ongoing

### Native Team
- **Kris — #60 Mobile auth screen (16h)**
  - Users can log in on phone
  - Blocked by Backend #45 (API ready)
  - After that: can parallelize with Frontend
  - Status: design complete, waiting for API

- **Sam — Design review + accessibility**
  - Ensured all screens meet accessibility standards
  - Design consistency review

---

## 📊 DENNA VECKA — SAMMANFATTNING

- 3 features merged (or near)
- 4 blockers solved
- 6 people contributed actively
- 40+ new test cases
- 0 bugs produced
- Team velocity: STRONG

---

## 📌 NÄSTA VECKA FOKUS

**Must-Have:**
- #40 Frontend auth (finish)
- #45 Backend FX (deploy)
- #52 Frontend responsive (complete)

**Nice-to-Have:**
- #60 Native auth screen (start if APIs ready)
- #51 Refactoring (continue)

**Blockers to watch:**
- FX integration waiting on external API (tracked daily)
- Native waiting on Backend #45 API schema (ETA: end of week)

---

## 🔗 BEROENDEN

**Frontend blocks:**
- #40 blocks Backend #45 → Ready by Thursday

**Backend blocks:**
- #45 blocks Frontend integration → ETA Friday
- #45 blocks Native #60 → ETA Friday

**Native blocks:**
- None currently (waiting on Backend, not blocking others)

---

## ⚠️ RISKER & ÅTGÄRDER

| Risk | Impact | Mitigation |
|------|--------|-----------|
| FX API external delay | 🔴 Critical | Daily status check, pair-prog ready |
| Native blocked too long | 🟠 Medium | Marco prioritizing #45 |
| Test coverage gaps | 🟠 Medium | Jana's test cases in progress |

---

## 📝 MÖTESBESLUT (från förra veckan)

- ✅ Frontend prioriterar auth flow
- ✅ Backend focuses on FX integration
- ✅ Native does design while blocked
- ✅ Pair programming if blockers emerge
- ✅ Daily standup if FX integration stalls

---

## 🎯 FRAMGÅNGSKRITERIER DENNA VECKA

By end of week:
- [ ] Frontend #40 merged (enables API integration)
- [ ] Backend #45 deployed (unblocks Native)
- [ ] Native design approved (ready to build)
- [ ] All tests passing
- [ ] No production incidents

---

## 📊 METRIKER

| Metric | Target | Current | Status |
|--------|--------|---------|--------|
| Test coverage | 70%+ | 68% | ⚠️ Close |
| Code review turnaround | <24h | ~12h | ✅ Good |
| Blockers resolved | 100% | 4/4 | ✅ On track |
| Velocity vs plan | ±10% | +5% | ✅ Ahead |

---

## 💬 SÄKERHET & TILLFÖRLITLIGHET

**Denna fil uppdateras genom:**
- Manual github-data-collection (vecklig)
- Automated snapshot (om tillgängligt)
- AI presentation läser INTE live GitHub

**Denna fil representerar status klockan 08:42 på dagen för mötet.**

**Presentation får ALDRIG:**
- Klona repositories
- Göra git-kommandon
- Läsa GitHub live
- Stressa om fallback

**Presentation får ALLTID:**
- Läsa denna fil
- Visa denna filen's tidsstämpel
- Rapportera denna filen's datum/tid i chatten

