# ✅ Verification System - Source of Truth

**Denna guide visar hur vi verifierar att allt är konsistent mellan:**
- Git branches, commits, och PRs
- GitHub Project Board (issues & status)
- Google Sheets (Risker & Assets)
- Mötesprotokollet (decisions & action items)

---

## 🎯 Source of Truth (Primär -> Fallback)

| Vad | Primär Källa | Fallback | Uppdateras |
|-----|---|---|---|
| **Issue Status** | GitHub Project Board | Google Sheets Project | Real-time (vid merge/PR) |
| **Risker & Assets** | Google Sheets | Mötesprotokollet | Efter möten (1x/vecka) |
| **Sprint Fokus & Tidsplan** | SPRINT_FOCUS_TIMELINE.md (_memory/) | SCHEDULE.md (_memory/) | Årlig |
| **Commits & Branches** | git log & GitHub | Git history | Real-time (per commit) |
| **PR Status** | GitHub PRs | Git branches | Real-time (per PR event) |
| **Decisions & Action Items** | Mötesprotokollet | DECISIONS.md (_memory/) | Efter möten |

**REGEL: AI MÅSTE ALLTID berätta vilken källa den använt för varje sektion.**

---

## 🔍 Manuell Verifikations-Checklist

**Kör denna checklist veckovis (t.ex. tisdag morgon) för att stämma av allt:**

### ✅ STEG 1: Läs Git Log (Denna Vecka)

```bash
git log --oneline --since="1 week ago"
```

**Vad att kolla:**
- [ ] Vilka commits är mergade till `develop`?
- [ ] Format: `type(scope): message (#ISSUE)` ✅/❌
- [ ] Issue-nummer refereras i alla commits?
- [ ] Några branches som är >7 dagar utan commits (STALE)?

**Rapportera:**
- Antal commits denna vecka: _____
- Stale branches (>7d): _____
- Format-problem: _____

---

### ✅ STEG 2: Läs GitHub Project Board

**Gå till:** https://github.com/orgs/chas-challenge-2026/projects/31/views/1

**Vad att kolla:**
- [ ] Issues märkta "Done" — är de verkligen mergade? (Verifiera mot git)
- [ ] Issues märkta "In Progress" — finns commits denna vecka? (Verifiera mot git)
- [ ] Issues märkta "To Do" — finns redan en branch/PR? (Verifiera mot git)

**Stämma av mismatch:**
| Issue # | Title | Status på Board | Git Status | Mismatch? |
|---------|-------|---|---|---|
| #XX | Dashboard | Done | f/XX merged | ✅ OK |
| #YY | API | In Progress | f/YY has commits | ✅ OK |
| #ZZ | Back-test | To Do | f/ZZ exists | ⚠️ Uppdatera Board |

**Rapportera:**
- Antal issues korrekt stämda: _____
- Antal mismatches: _____
- Vilka issues behöver uppdateras på Board: _____

---

### ✅ STEG 3: Läs Open/Closed PRs

**Open PRs:** https://github.com/chas-challenge-2026/avanza-team1/pulls?q=is%3Aopen+is%3Apr

**Vad att kolla för VARJE open PR:**
- [ ] Vilken issue är denna för? (läs PR title/description)
- [ ] PR Status: 
  - ⏳ Needs Review (väntar på granskare)?
  - ✅ Approved (godkänd)?
  - ⚠️ Changes Requested (behöver fixes)?
- [ ] Hur länge har PR:n väntat på review?
  - < 1 dag: OK ✅
  - 1-2 dagar: Prioritera review 🟡
  - > 2 dagar: BLOCKERA! 🔴

**Rapportera:**
- Total open PRs: _____
- Needs Review: _____ (Tid väntad: ___)
- Approved ready-to-merge: _____
- Changes Requested: _____
- **🔴 Blockers (>2d väntat):** _____

---

### ✅ STEG 4: Läs Google Sheets Risker

**CSV-länk för AI:** https://docs.google.com/spreadsheets/d/1A8XHxyAdbyrWlHSWTNgtwkKACdSiUr3F/export?format=csv&gid=1796827285

**Vad att kolla:**
- [ ] CRITICAL risker — status? (Lösta? Pågår? Ej påbörjade?)
- [ ] HIGH risker — mitigation framsteg?
- [ ] Risk-prioritering — förändrad denna vecka?

**Verifiera mot git:**
- Risk säger "Mitigated" → Finns commits för denna mitigation? 
- Risk säger "In Progress" → Finns aktivt arbete (commits < 7d)?
- Risk säger "Open" → Är detta fortfarande en hot? Eller redan löst?

**Rapportera:**
- CRITICAL risker: _____ (Status: ___)
- HIGH risker: _____ (Status: ___)
- Mitigations pågår: _____
- ⚠️ Mismatches (status inte uppdaterad): _____

---

### ✅ STEG 5: Läs Mötesprotokollet

**TXT-länk för AI:** https://docs.google.com/document/d/1WD9XJBVrE49Csqz-XYiLgejlKlCA4t5sWiwoTkNiTD8/export?format=txt

**Vad att kolla:**
- [ ] Vilka beslut togs på senaste mötet? (markeras med "B:")
- [ ] Vilka action items gällde denna vecka?
- [ ] Är action items genomförda? (Verifiera mot git/Project Board)

**Rapportera:**
- Nya beslut från senaste möte: _____
- Action items denna vecka: _____
- ✅ Genomförda: _____
- ⚠️ Ej genomförda: _____
- ⏳ Pågår: _____

---

## 🤖 Automated Verification (För AI)

**Använd denna prompt för att be AI verifiera consistency:**

```
Verifiera consistency denna vecka:

1. Git log denna vecka (copy-pasta från `git log --oneline --since="1 week ago"`):
[PASTE GIT LOG]

2. GitHub Project Board status (copy-pasta eller beskriv):
[PASTE ELLER BESKRIV STATUS]

3. Open PRs (copy-pasta PR-listan):
[PASTE PR LIST]

4. Google Sheets Risker (copy-pasta CSV):
[PASTE RISKS CSV]

5. Mötesprotokollet (copy-pasta relevanta sections):
[PASTE MEETING NOTES]

Nu: Verifiera consistency och rapportera:
- Vilka issues har status-mismatch?
- Vilka PRs blockerar?
- Vilka risker är ej uppdaterade?
- Vilka action items är ej genomförda?
- Vilka commits stämmer inte med issue-status?
```

**AI rapporterar då:**
- ✅ Vad som är korrekt
- ⚠️ Vad som behöver fixas
- 🔴 Blockers
- 📋 Action items för nästa möte

---

## 📊 Veckovis Verifikations-Cadence

| Dag | Tid | Vad | Vem | Källa |
|-----|-----|-----|-----|-------|
| **Tisdag** | 09:00 | Läs git log | Team Lead | `git log --oneline` |
| | | Verifiera Project Board vs git | Team | GitHub Project Board |
| | | Granska öppna PRs | Team | GitHub PRs |
| **Torsdag** | Efter möte | Uppdatera risker i Google Sheets | Team Lead | Möte-resultat |
| | | Verifiera action items från möte | Team Lead | Mötesprotokollet |
| **Varje dag** | Vid commit | Format checka: `type(scope): message (#ISSUE)` | Alla | git log |
| | Vid PR | Verifiera: PR title, issue ref, test coverage | Reviewer | GitHub PR |

---

## 🚨 Red Flags (Vad Är Fel?)

| Tecken | Problem | Åtgärd |
|--------|---------|--------|
| Issue säger "Done" men ingen commit på develop | Issue markerad färdig utan merge | ❌ Uppdatera Project Board eller merge PR |
| PR väntar på review > 2 dagar | Blockerar andra issues | 🚨 Prioritera review NU |
| Commit-format inte följd (`type(scope): #ISSUE`) | Dålig traceability | ❌ Ångra + re-commit med rätt format |
| Risk säger "Mitigated" men ingen commit för mitigation | Status ej uppdaterad | ⚠️ Verifiera i git + uppdatera risk-status |
| Branch > 7 dagar utan commits | Stale/abandoned arbete | 📋 Diskutera på möte — fortsätt eller arkivera? |
| Too many WIP PRs | Parallelt arbete blir svårt | 🔴 Fokusera — stäng 1-2 PRs innan nya börjas |

---

## ✅ Definition of "Stämmer"

Systemet är **konsistent** när:

1. ✅ **Git = Project Board:** Alla commits på `develop` motsvarar issues märkta "Done"
2. ✅ **Issues = Branches:** Alla open issues har motsvarande feature-branch
3. ✅ **PRs = Reviews:** Alla open PRs är reviewade (eller tildelade reviewer)
4. ✅ **Risks = Mitigations:** Alla risker har uppdaterad status baserad på arbete denna vecka
5. ✅ **Möte = Action Items:** Alla action items från möte är påbörjade eller markerade Done
6. ✅ **Commits = Format:** Alla commits följer `type(scope): message (#ISSUE)`

---

## 📝 Veckovis Verifikations-Rapport Template

**Tisdagar 09:30 — Använd denna template:**

```
# Veckovis Verification Report - V[X] (2026-09-0X)

## ✅ GIT LOG
- Commits denna vecka: X
- Format OK: X/X ✅
- Stale branches (>7d): [lista]

## ✅ PROJECT BOARD VS GIT
- Issues Done & merged: X ✅
- Issues In Progress & commits denna vecka: X ✅
- Issues To Do & no branch: X ✅
- Mismatches: [lista eller "0"]

## 🟡 OPEN PRS
- Total: X
- Needs Review: X (⏳ longest waiting: Y dagar)
- Approved: X
- Changes Requested: X
- 🔴 Blockers (>2d): [lista eller "0"]

## 🚨 RISKER
- CRITICAL: X (Status: ___)
- HIGH: X (Status: ___)
- Mitigations pågår: X
- ⚠️ Status-mismatch: [lista eller "0"]

## 📋 ACTION ITEMS
- Från förra möte: X
- Genomförda: X ✅
- Pågår: X
- Ej påbörjade: [lista]

## 🎯 NÄSTA STEG
- Prioritera: [PR #X - Y dagar väntad]
- Fixera: [Issue #Y - status-mismatch]
- Diskutera: [Stale branch, risk-status, etc]

**Källa:** Git + GitHub Project Board + Google Sheets Risker + Mötesprotokollet
**Verifiera av:** [Namn]
**Datum:** 2026-09-0X
```

---

**Senast uppdaterad:** 2026-09-08  
**Ändring:** Ny källa för konsistensverifiering (GitHub Project Board + Google Sheets i stället för lokala filer)
