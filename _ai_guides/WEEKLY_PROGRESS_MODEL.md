---
name: weekly_progress_model
description: Mandatory data model for "Sedan förra mötet" slide — how to reconstruct weekly progress from commits, PRs, and issues
metadata:
  type: process
  updated: 2026-09-13
---

# 📊 WEEKLY PROGRESS MODEL — Veckohistorik från GitHub

**"Sedan förra mötet"-sliden visar vad teamet FAKTISKT GJORDE förra veckan, inte vad som är öppet just nu.**

Denna modell är **obligatorisk före presentation kan byggas**.

---

## 🎯 DEFINITION: FÖRRA VECKAN

```
Från: Förra måndagsmötet (09:00 CET förra vecka)
Till: Nu (idag, aktuell tid)

Exempel:
- Förra veckan: Måndag 2026-09-08 09:00
- Denna vecka: Idag 2026-09-13 11:30
```

---

## 📋 WEEKLY PROGRESS DATASET — Vad Att Samla In

För perioden **förra mötet → nu** ska AI:n **ALLTID** samla in:

### 1. COMMITS PÅ DEVELOP

```
Källa: GitHub API / git log
Datum-filter: från förra måndag 09:00 till idag
Extrahera:
  - Commit hash
  - Author (vem skrev koden)
  - Message (vad gjorde de)
  - Date

Exempel:
  abc1234 — Marco — "Add FX calculation helper" — 2026-09-10 14:23
  def5678 — Lisa — "Auth refactor: separate concerns" — 2026-09-11 09:45
```

### 2. MERGED PULL REQUESTS

```
Källa: GitHub PRs filter: merged denna vecka
Datum-filter: från förra måndag till idag
Extrahera:
  - PR number + title
  - Author (vem skrev PR:en)
  - Merge date
  - Linked issue (vilken issue löste den?)
  - Commits in PR

Exempel:
  #81 — Portfolio health summary (Rasha) — Merged 2026-09-11
    Linked to: #52
    Commits: 4
```

### 3. CLOSED ISSUES

```
Källa: GitHub Issues filter: closed denna vecka
Datum-filter: från förra måndag till idag
Extrahera:
  - Issue number + title
  - Assignee (vem ägde den)
  - Closed date
  - Closed PR (vilken PR stängde den)
  - Labels (vad var typen: feature/bug/test/docs)

Exempel:
  #52 — Portfolio health summary (Rasha) — Closed 2026-09-11
    Closed by: PR #81
    Labels: feature
```

### 4. OPEN ISSUES WITH ACTIVITY THIS WEEK

```
Källa: GitHub Issues filter: open + activity denna vecka
Extrahera:
  - Issue number + title
  - Assignee (vem arbetar på det)
  - Latest activity date (senaste uppdateringen denna vecka)
  - Status (% done om tillgängligt)
  - Linked PR (om en PR är öppen för den)

Exempel:
  #63 — Drift calculation (Tomac) — Updated 2026-09-12
    Linked to: PR #82 (open, 60% done)
    Progress: 3 commits denna vecka
```

### 5. OPEN PRS WITH ACTIVITY THIS WEEK

```
Källa: GitHub PRs filter: open + activity denna vecka
Extrahera:
  - PR number + title
  - Author (vem skrev den)
  - Latest activity date
  - Linked issue (vilken issue löser den)
  - Reviews pending (vem behöver godkänna)

Exempel:
  #82 — Drift calculation (Tomac) — Updated 2026-09-12
    Linked to: #63
    Reviews pending: Marco, Lisa
    Commits: 3
```

---

## 🎯 STRUKTURERA I TRE GRUPPER

Med alla data samlad, organisera i **exakt tre grupper**:

### ✓ KLART — Issue är STÄNGD eller PR är MERGAD

**Definition:** Arbete som är färdigt enligt projektets Definition of Done.

**Verifiera:**
- Issue är closed (eller PR är merged)
- Arbetet ligger redan i develop
- Commits finns och är verifierade

**Format:**
```
✓ #52 – Portfolio health summary (Rasha)
  Merged PR #81 · 4 commits · klart 11 sep
```

**Data från:** Merged PRs + Closed Issues denna vecka

---

### → PÅGÅR — Issue är ÖPPEN med denna veckas aktivitet

**Definition:** Arbete som har commits eller PR-aktivitet denna vecka, men är inte slutfört.

**Verifiera:**
- Issue är open
- Det finns en PR som är öppen (eller en branch med commits)
- Senaste aktivitet denna vecka (commit, comment, push)

**Format:**
```
→ #63 – Drift calculation (Tomac)
  3 commits denna vecka · PR #82 öppen · 60% progress
```

**Data från:** Open Issues + Open PRs med aktivitet denna vecka

---

### ! BEHÖVER UPPMÄRKSAMHET — Issue är BLOCKERAD, saknar ÄGARE, eller STÅR STILL

**Definition:** Arbete som behöver åtgärd nu — blockerat, utan assignee, eller långsamt.

**Typer:**

**a) BLOCKERAD**
```
! #45 – Auth schema (Lisa)
  Blockerad på Backend #48 (ETA torsdag)
```

**b) SAKNAR ÄGARE**
```
! #67 – Documentation update
  Assignee saknas — behöver åtgärd nu
```

**c) STÅR STILL (>3 dagar utan aktivitet)**
```
! #71 – Legacy refactor (Marco)
  Senaste aktivitet: 5 dagar sedan · behöver push
```

**Data från:** Open Issues utan nylig aktivitet + Open PRs väntande på review

---

## 🎨 FORMAT FÖR NPF/DYSLEXIA-VÄNLIGHET

**VARJE rad i WEEKLY PROGRESS måste ha TRE lager:**

1. **SYMBOL** — Visuell status (läses före färg)
2. **FÄRG** — Semantisk status
3. **TEXT** — Konkret beskrivning

### FORMAT TEMPLATE

```
[SYMBOL] [FÄRG] #XX – Titel (Assignee)
  Konkret status · Antal commits · Klar-datum eller ETA
```

### SYMBOL LEGEND

```
✓ = Klart (solid check)
→ = Pågår (framåtpil)
! = Behöver uppmärksamhet (varningstriangel)
× = Blockerad/Kritisk (stoppsymbol)
```

### FÄRG LEGEND

```
🟢 Grön = ✓ KLART (verifierat färdigt)
🔵 Blå = → PÅGÅR (neutral status)
🟡 Gul = ! BEHÖVER UPPMÄRKSAMHET (varning)
🔴 Röd = × BLOCKERAD (kritisk stopp)
```

### KONKRET TEXT

Text ska visa:
- **Vad:** Issue title
- **Vem:** Assignee
- **Hur långt:** "X commits denna vecka" eller "PR öppen" eller "klart datum"
- **Nästa steg:** "ETA torsdag" eller "väntar på review" eller "blockerad på X"

### EXEMPEL — ALLTING TILLSAMMANS

```
KLART:
✓ #52 – Portfolio health summary · Rasha
  🟢 Merged PR #81 · 4 commits · klart 11 sep

PÅGÅR:
→ #63 – Drift calculation · Tomac
  🔵 3 commits denna vecka · PR #82 öppen · 60% progress

BEHÖVER UPPMÄRKSAMHET:
! #45 – Auth schema · Lisa
  🟡 Blockerad på Backend #48 · ETA torsdag

! #67 – Documentation
  🟡 Assignee saknas · behöver åtgärd nu

× #71 – Legacy refactor · Marco
  🔴 Står still 5 dagar · ingen nylig aktivitet · påminnelse behövs
```

---

## 🔄 KORSREFERENS-EXEMPEL: Hur All Data Hänger Ihop

**Scenario:** #52 (Portfolio health summary) var klart denna vecka.

```
GitHub Issues:
  #52 – Portfolio health summary (Rasha)
  Status: CLOSED (11 sep)
  
GitHub PRs:
  #81 – Merge PR (Rasha)
  Linked issue: #52
  Status: MERGED (11 sep)
  
Git Commits:
  abc123 — Rasha — "Initial portfolio calc" — 2026-09-09
  def456 — Rasha — "Add styling" — 2026-09-10
  ghi789 — Rasha — "Fix edge case" — 2026-09-11
  jkl012 — Rasha — "Final polish" — 2026-09-11
  
RESULTAT I PRESENTATION:
✓ #52 – Portfolio health summary (Rasha)
  Merged PR #81 · 4 commits · klart 11 sep
```

---

## 🔒 MANDATORY RULES FÖR WEEKLY PROGRESS

1. **PERIOD MÅSTE VARA EXPLICIT**
   - Från: [Förra mötet datum/tid]
   - Till: [Idag datum/tid]
   - Presentationen måste visa denna period

2. **COMMITS + PRS + ISSUES MÅSTE KORSREFERERAS**
   - En closed issue utan merged PR = verifiera varför
   - En merged PR utan linked issue = dokumentera vad den gör
   - En öppen PR utan commits denna vecka = inte PÅGÅR, flytta till backlog

3. **VERIFIERA AGAINST DoD (Definition of Done)**
   - En issue får bara vara ✓ KLART om den möter DoD
   - Exempel: Merged ≠ Klart om tester saknas eller docs inte uppdaterad
   - Se DEFINITION_OF_DONE.md före klassificering

4. **ASSIGNEE MÅSTE VISAS**
   - Varje rad måste ha assignee namn (eller "Behöver ägare" om saknas)
   - Format: `(Vem)`

5. **KONKRET METRIK, ALDRIG GISSNING**
   - "4 commits" inte "mycket arbete"
   - "Blockerad på #48" inte "har ett problem"
   - "3 dagar utan aktivitet" inte "långsamt"

---

## 🎯 RESULTAT

Med denna modell blir Slide ① ("Sedan förra mötet"):

✅ **TYDLIG** — Varje rad är en konkret historik
✅ **KOMPLETT** — Inget arbete missas (commits + PRs + issues alla lästa)
✅ **ÅTKOMLIG** — Symbol + färg + text (NPF/dyslexia-vänlig)
✅ **VERIFIERAD** — Baserad på faktisk GitHub-data, inte gissningar
✅ **KONSEKVENT** — Samma format varje vecka

---

**Senast uppdaterad:** 2026-09-13
