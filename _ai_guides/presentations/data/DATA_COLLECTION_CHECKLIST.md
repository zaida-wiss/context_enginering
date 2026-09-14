---
name: data_collection_checklist
description: Obligatorisk datainsamling FÖRE presentationen börjar byggas
metadata:
  type: process
  updated: 2026-09-13
---

# 📋 DATA COLLECTION CHECKLIST — GATE INNAN RENDERING

**PRESENTATIONEN FÅR INTE BÖRJA BYGGAS FÖRRÄN DETTA ÄR KLART.**

Live sources only. No snapshots — all data from direct links to GitHub, Project Board, Google Docs.

🔗 **Alla externa datakällor:** Se [`_memory/EXTERNAL_SOURCES.md`](../../../../_memory/EXTERNAL_SOURCES.md) för centraliserad register över Google Sheets, Google Docs, GitHub och alla fallback-URLs.

---

## ✅ PHASE 1: CONTEXT REPO SOURCES

**READ IN THIS ORDER — mandatory guides before data collection:**

```
[ ] README.md (root) — Läst via https://raw.githubusercontent.com/zaida-wiss/context_enginering/main/README.md
[ ] _ai_guides/presentations/README.md — Navigation guide
[ ] _ai_guides/presentations/design/DESIGN_AUTHORITY.md — Design source of truth
[ ] _ai_guides/presentations/data/DATA_COLLECTION_MANDATORY.md — Mandatory checklist
[ ] _ai_guides/presentations/content/PRESENTATION_SPEC.md — What to show
[ ] _ai_guides/presentations/structure/PRESENTATION_STRUCTURE.md — Slide structure
[ ] _ai_guides/presentations/design/PRESENTATION_STYLE.md — Visual design rules
[ ] _ai_guides/presentations/models/WEEKLY_PROGRESS_MODEL.md — Data model
[ ] _ai_guides/presentations/verification/VERIFICATION_THIS_WEEK.md — Verify sources
```

**Om någon misslyckas:** Använd github.com webbåtkomst istället för raw.githubusercontent.com

**STATUS:** Säg "CONTEXT REPO COMPLETE" när alla är lästa.

---

## ✅ PHASE 2: PROJECT GITHUB DATA — BRANCH & COMMITS

**SOURCE 1: GitHub Branches**

```
Källa 1: GitHub Connector/API
  [ ] Branches på develop listade
  [ ] Active branches denna vecka identifierade
  [ ] Stale branches (>3 dagar) identifierade
  Status: ✅ LÄST / ⚠️ FALLBACK / ❌ MISSLYCKAD

Källa 2: Fallback — GitHub web
  [ ] https://github.com/chas-challenge-2026/avanza-team1/branches
  Status: ✅ LÄST / ❌ MISSLYCKAD
```

**STATUS:** ✅ Vi har branch-data

---

**SOURCE 2: GitHub Commits (develop branch, denna vecka)**

```
Källa 1: GitHub Connector/API
  [ ] Commits sedan förra måndag (develop branch)
  [ ] Author för varje commit
  [ ] Commit message för varje
  Status: ✅ LÄST / ⚠️ FALLBACK / ❌ MISSLYCKAD

Källa 2: Fallback — GitHub web
  [ ] https://github.com/chas-challenge-2026/avanza-team1/commits/develop
  Status: ✅ LÄST / ❌ MISSLYCKAD

Källa 3: Fallback — Google Sheets historik
  [ ] https://docs.google.com/spreadsheets/d/1TECz-PkbJhK6Jux6tpjcXDNvUNUZGI_nnIDE5rKr5UI/edit?gid=77162861#gid=77162861
  Status: ✅ LÄST / ❌ MISSLYCKAD

Källa 4: Fallback — Merged PRs denna vecka (om commits-listan failar)
  [ ] Se issue 3 nedan för PR-data
  [ ] Använd merged PRs för att rekonstruera commits
  Status: ✅ REKONSTRUERAT / ❌ MISSLYCKAD
```

**STATUS:** ✅ Vi har commit-data eller ⚠️ rekonstruerat från PRs

---

## ✅ PHASE 3: PROJECT GITHUB DATA — ISSUES

**SOURCE 3: GitHub Issues**

```
Källa 1: GitHub Connector/API
  [ ] Open issues denna vecka
  [ ] Closed issues denna vecka
  [ ] Assignees för varje
  [ ] Labels för varje
  Status: ✅ LÄST / ⚠️ FALLBACK / ❌ MISSLYCKAD

Källa 2: Fallback — GitHub web
  [ ] https://github.com/chas-challenge-2026/avanza-team1/issues
  Status: ✅ LÄST / ❌ MISSLYCKAD
```

**STATUS:** ✅ Vi har issue-data

---

## ✅ PHASE 4: PROJECT GITHUB DATA — PULL REQUESTS

**SOURCE 4: GitHub Pull Requests**

```
Källa 1: GitHub Connector/API
  [ ] Open PRs denna vecka
  [ ] Merged PRs denna vecka
  [ ] Author för varje PR
  [ ] Linked issues
  Status: ✅ LÄST / ⚠️ FALLBACK / ❌ MISSLYCKAD

Källa 2: Fallback — GitHub web
  [ ] https://github.com/chas-challenge-2026/avanza-team1/pulls
  Status: ✅ LÄST / ❌ MISSLYCKAD
```

**STATUS:** ✅ Vi har PR-data

---

## ✅ PHASE 5: PROJECT BOARD

**SOURCE 5: GitHub Project Board**

```
Källa 1: GitHub Connector/API (Project Board)
  [ ] URL/Project ID från DATA_SOURCES.md finns
  [ ] Columns listade (Backlog, Ready, In Progress, Review, Done)
  [ ] Issues i varje kolumn
  Status: ✅ LÄST / ⚠️ FALLBACK / ❌ MISSLYCKAD

Källa 2: Fallback — GitHub web (direkt URL från DATA_SOURCES.md)
  [ ] Project Board URL existing och åtkomlig
  Status: ✅ LÄST / ❌ MISSLYCKAD

Källa 3: Fallback — Rekonstruera från Issues + PRs
  [ ] Använd issue-status för att säga vilket kolumn
  [ ] Använd PR-status för att säga in-review
  Status: ✅ REKONSTRUERAT / ❌ MISSLYCKAD
```

**STATUS:** ✅ Vi har Board-data eller ⚠️ rekonstruerat

---

## ✅ PHASE 6: MEETING PROTOCOL

**SOURCE 6: Mötesprotokollet denna vecka**

```
Källa 1: Google Docs eller TXT-export (URL från DATA_SOURCES.md)
  [ ] URL existing
  [ ] Dokumentet åtkomligt
  [ ] Denna veckas möte identifierat
  Status: ✅ LÄST / ⚠️ FALLBACK / ❌ MISSLYCKAD

Källa 2: Fallback — TXT-export från Google Docs
  [ ] Försök export?export=txt från Google Docs URL
  Status: ✅ LÄST / ❌ MISSLYCKAD
```

**STATUS:** ✅ Vi har protocol

---

## ✅ OPTIONAL: PROJECT CODE REVIEW

**SOURCE 7: Kod-review av aktiva branches (ENDAST om blockers/beroenden behöver verifieras)**

```
[ ] API-kontrakt mellan Frontend-Backend verifierat (om relevant)
[ ] JNA-kontrakt mellan Backend-Native verifierat (om relevant)
[ ] Auth-flow konsekvent över team (om relevant)
[ ] Kärnflöde end-to-end reviewat (om relevant)
Status: ✅ REVIEWAT / ⏭️ SKIPPAT (ej relevant denna vecka) / ❌ MISSLYCKAD
```

**STATUS:** ✅ Done eller ⏭️ Skipped (inte alltid nödvändigt)

---

## 📋 SAMMANFATTNING FÖRE RENDERING

**Innan presentationen BÖRJAR byggas, kontrollera detta:**

```
✅ CONTEXT REPO — Alla presentationsguider lästa
✅ BRANCHES — Från GitHub Connector eller fallback
✅ COMMITS — Från GitHub Connector eller rekonstruerat
✅ ISSUES — Från GitHub Connector eller fallback
✅ PULL REQUESTS — Från GitHub Connector eller fallback
✅ PROJECT BOARD — Från Board-API eller rekonstruerat
✅ PROTOCOL — Från Google Docs eller fallback
✅ CODE REVIEW — (om relevant denna vecka)
```

**RESULTAT:**

```
Datainsamlingen är KOMPLETT.
Presentationen har all information den behöver.
Slide-rendering kan börja.

Säg: "DATA COLLECTION GATE ✅ PASSED"
```

---

## ❌ OM NÅGOT FAILAR

**Presentationen får ALDRIG säga att något är "ej verifierat" efter bara ETT försök.**

Fallback-ordningen MÅSTE följas:

```
1. Primär källa failar? → Prova källa 2
2. Källa 2 failar? → Prova källa 3 (rekonstruktion)
3. Ingenting fungerar? → Markera som "ej verifierat denna vecka" + rapportera vilken källa
```

**EXEMPEL:**

```
❌ MISSLYCKAD FALLBACK:
GitHub Connector failar → Presentationen säger "commits ej verifierade"

✅ KORREKT FALLBACK:
GitHub Connector failar → Försök GitHub web → 
Rekonstruera från merged PRs eller annan källa → Använd en av dessa
```

---

## 📝 DATASAMLINGS-LOGG

Fyll i denna innan presentation börjar:

```
CHECKLIST DATUM: [YYYY-MM-DD]
CHECKLIST TIDSPUNKT: [HH:MM TIMEZONE]

✅ Context repo: COMPLETE
✅ Branches: SOURCE [Connector/Web]
✅ Commits: SOURCE [Connector/Web/Reconstructed]
✅ Issues: SOURCE [Connector/Web]
✅ PRs: SOURCE [Connector/Web]
✅ Board: SOURCE [Connector/Web/Reconstructed]
✅ Protocol: SOURCE [Google Docs]
✅ Code Review: [DONE/SKIPPED]

GATE STATUS: ✅ PASSED eller ⚠️ PARTIAL (om något är rekonstruerat)

Presentation kan börja byggas.
```

---

## 🎯 KRITISK REGEL

**Om denna checklist INTE är komplett innan rendering börjar:**

→ STANNA RENDERINGEN  
→ Fyll i saknade sources  
→ Prova fallbacks  
→ Bygg först när checklist är ✅  

Presentationen ska ALDRIG byggas med ofullständig data.

---

**Senast uppdaterad:** 2026-09-13
