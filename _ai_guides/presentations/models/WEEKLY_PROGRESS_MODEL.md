---
name: weekly_progress_model
description: Mandatory data model for "Sedan förra mötet" slide — how to reconstruct weekly progress from commits, PRs, and issues
metadata:
  type: process
  updated: 2026-09-13
---

# 📊 WEEKLY PROGRESS MODEL — Veckohistorik från GitHub

**"Sedan förra mötet"-sliden är en ERKÄNNANDE-RETROSPEKTIV, inte en statusrapport.**

Syftet är att ge teamet konkret feedback: "Det här gjorde ni faktiskt förra veckan. Bra jobbat."

**TWÅ SLIDES för denna punkt:**

**Slide ①A: "Levererat denna vecka"**
- Arbete som **mergades till develop** (verifierat i git)
- Visar **arbetsområden**, inte bara issues (#42, #43, etc)
- Format: Område → vad levererades → effekt för teamet

**Slide ①B: "Byggde vidare på denna vecka"**
- Arbete som **pågår med faktisk framdrift** (commits, PRs öppna)
- Visar **arbetsområden** som fortskrider
- Format: Område → vad jobbar vi på → nästa steg (inte blockers)

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

För perioden **förra mötet → nu** ska AI:n **ALLTID** samla in — **I denna ordning**:

### 1. COMMITS PÅ DEVELOP ← PRIMARY DATA SOURCE

```
Källa: GitHub API / commits?sha=develop&since=[MONDAY_DATE]
Datum-filter: från förra måndag 09:00 till idag
Extrahera:
  - Commit hash
  - Author (vem skrev koden)
  - Message (vad gjorde de)
  - Date

Exempel på RAW DATA:
  abc1234 — Marco — "Add FX calculation helper" — 2026-09-10 14:23
  def5678 — Lisa — "Auth refactor: separate concerns" — 2026-09-11 09:45
  ghi9012 — Lisa — "Add unit tests for refactor" — 2026-09-11 10:15
  jkl3456 — Marco — "Bugfix: edge case in FX calc" — 2026-09-12 08:30
  mno7890 — Marco — "Revert: FX edge case (wrong approach)" — 2026-09-12 09:45
  pqr2345 — Marco — "FX calc: correct edge case handling" — 2026-09-12 11:20
```

**REGEL: Commit count is evidence, not presentation content**
- ❌ INTE: Visa alla 6 commits som 6 rader
- ✅ ISTÄLLET: Klusta per arbetsområde/issue:
  ```
  Klustering av Marco's commits:
  "FX calculation improvements" (3 commits denna vecka, inklusive bugfix iteration)
  
  Klustering av Lisa's commits:
  "Auth refactor + test coverage" (2 commits denna vecka)
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

## 🎯 STRUKTURERA EFTER ARBETSOMRÅDEN (INTE ISSUES)

Med alla data samlad, organisera i **arbetsområden**, inte enskilda issues:

**ARBETSOMRÅDE = En sammanhängande del av MVP som teamet arbetat med**

Exempel på arbetsområden:
- Frontend & Auth — login, mock auth, protected routes, accessibility
- Backend & Session — centraliserad autentisering, controller-refaktorering  
- Native & Risk Motor — riskberäkning, rolling estimates, tester
- Infrastructure — deployment, CI/CD, database migrations

Varje arbetsområde visar vad som levererades + vad som pågår inom samma område.

**VIKTIGT:** Blockers, saker som behöver uppmärksamhet, och risker visas på ANDRA slides (Beroenden, Risker). Denna slide är ENBART erkännande och framsteg.

### 🟢 KLART FÖRRA VECKAN — Issue är STÄNGD eller PR är MERGAD

**Definition:** Arbete som påbörjades eller fortsatte denna vecka och blev verifierat färdigt enligt Definition of Done.

**Verifiera:**
- Issue är closed DENNA VECKA (eller PR är merged denna vecka)
- Arbetet ligger redan i develop
- Commits finns och är verifierade
- DoD är uppfylld (läs DEFINITION_OF_DONE.md för denna vecka)

**Format:**
```
🟢 #52 – Portfolio health summary (Rasha)
  Unblockade Frontend-Backend integration
  Merged PR #81 · 4 commits · klart 11 sep
```

**Data från:** Merged PRs + Closed Issues denna vecka (med DoD-verifiering)

---

### 🟠 PÅBÖRJAT FÖRRA VECKAN – FORTSÄTTER — Issue är ÖPPEN med denna veckas ARBETSAKTIVITET

**Definition:** Arbete som påbörjades eller fortsatte denna vecka med FAKTISK ARBETSAKTIVITET (kod/commits), men som inte är färdigt än.

**KRITISK: Vad räknas som "påbörjat denna vecka"?**

✅ **RÄKNAS SOM PÅBÖRJAT:**
- Commit på denna vecka (verifierad arbete i git)
- Push/branch med kodändringar
- PR skapad eller uppdaterad denna vecka (kod under granskning)
- Dokumentationscommit denna vecka

❌ **RÄKNAS INTE SOM PÅBÖRJAT:**
- Issue-kommentar ensam ("jag är på det" utan kod)
- Status-uppdatering på Project Board
- Diskussion i GitHub
- Issue öppnad men helt orörd denna vecka

**Verifiera:**
- Issue är open
- Minst ett av ovan ✅-punkter är uppfyllt denna vecka
- Senaste aktivitet denna vecka är ARBETSAKTIVITET (commit/PR), INTE bara diskussion
- Arbetet har faktisk framdrift (kod förflyttad framåt)

**Format:**
```
🟠 #63 – Drift calculation (Tomac)
  Kommer att unblockera Native-teamet när klart
  3 commits denna vecka · PR #82 öppen · ~60% progress
```

**Data från:** Open Issues + Open PRs med aktivitet denna vecka

---

## ⚠️ VISA INTE PÅ DENNA SLIDE

- ❌ Blockerat arbete (hör hemma på Beroenden-slide)
- ❌ Arbete som saknar ägare (hör hemma på Risker-slide)
- ❌ Arbete som står stilla utan aktivitet (är inte "påbörjat denna vecka")
- ❌ Backlog-items utan aktivitet denna vecka
- ❌ Framtida planerat arbete
- ❌ Rå commitlista (klustrat endast)

---

## 🎨 FORMAT FÖR NPF/DYSLEXIA-VÄNLIGHET

**VARJE rad i WEEKLY PROGRESS måste ha TRE lager:**

1. **SYMBOL** — Visuell status (läses före färg)
2. **FÄRG** — Semantisk status
3. **TEXT** — Konkret beskrivning

### FORMAT TEMPLATE

```
[SYMBOL] [FÄRG] #XX – Titel (Assignee)
  Vad det innebär för projektet · Konkret status · Antal commits · Klar-datum eller ETA
```

**VIKTIGT: "Vad det innebär" måste alltid visas**

Det är INTE tillräckligt att bara säga "4 commits" eller "klart".
Vi måste förstå: **Vilken effekt hade det här bidraget?**

Exempel på DÅLIGT (bara status):
```
✓ #52 – Portfolio summary (Rasha)
  Merged PR · 4 commits · klart 11 sep
```

Exempel på BRA (status + effekt):
```
✓ #52 – Portfolio summary (Rasha)
  🟢 Unblockade Frontend-integration · Merged PR #81 · 4 commits · klart 11 sep
```

Eller:
```
✓ #52 – Portfolio summary (Rasha)
  🟢 Portfolio kan nu visas på alla enheter · Merged PR #81 · klart 11 sep
```

Eller:
```
→ #63 – Drift calculation (Tomac)
  🔵 Gör att Native kan börja sitt arbete när klart · 3 commits denna vecka · PR öppen
```

### SYMBOL LEGEND

```
✓ = Klart (solid check)
→ = Pågår (framåtpil)
! = Behöver uppmärksamhet (varningstriangel)
× = Blockerad/Kritisk (stoppsymbol)
```

### FÄRG SEMANTIK — KONSEKVENT ÖVERALLT

**REGEL: Färger betyder alltid samma sak i HELA presentationen**

```
🟢 Grön = KLART denna vecka (verifierat färdigt enligt DoD)
🔵 Blå = PÅGÅR denna vecka (arbete med faktisk framdrift, fortsätter nästa vecka)
🟠 Orange = RISK/OSÄKERHET överallt (varning, ej på Slide ①)
🔴 Röd = BLOCKER/KRITISK överallt
```

**Varför detta är viktigt:**
- Orange betyder **enbart** risk/uppmärksamhet i presentationen
- "Pågår" används blått för att skilja från risk
- Slide ① visar bara två färger: grön (levererat) + blå (pågår)
- Risker och blockers visas på separata Beroenden/Risker-slides

**I presentationen förklaras detta:**
```
Förra veckan − status på teamets arbete:
🟢 KLART denna vecka (färdigt enligt DoD)
🔵 BYGGDE VIDARE denna vecka (faktisk framdrift, fortsätter)

[Risker, blockers och beroenden visas på senare slides]
```

Resultat: Färger är aldrig tvetydiga. Tittare förstår direkt vad som är levererat, pågår, eller behöver uppmärksamhet.

### KONKRET TEXT

Text ska visa:
- **Vad:** Issue title
- **Vem:** Assignee
- **Hur långt:** "X commits denna vecka" eller "PR öppen" eller "klart datum"
- **Nästa steg för 🟠 Påbörjat:** "PR öppen", "test återstår", "fortsätter med responsivitet"
  - ❌ ALDRIG: "blockerad på X" — blockers visas på separat Beroenden-slide
  - ❌ ALDRIG: "väntar på..." — bara framåtriktade nästa steg

### EXEMPEL — TVÅ SLIDES MED ARBETSOMRÅDEN

**SLIDE ①A: "LEVERERAT DENNA VECKA"**

```
Förra veckan levererade teamet arbete inom 4 fokusområden.

═══════════════════════════════════════════════════════════════

🟢 FRONTEND & AUTHENTISERING
Loginflödet är nu i develop och frontend kan arbeta mot riktig auth.
   ✓ Login page + mocked token handling
   ✓ Protected routes & session management
   ✓ Accessibility improvements på form
   Merged: PR #90 · 12 commits · klart 11 sep

🟢 BACKEND & SESSION SECURITY  
SessionSecurityFilter minskar duplicerad auth-logik och ger backend en tydligare arkitektur.
   ✓ Centraliserad authentication
   ✓ Controller-refaktorering (duplicerad session-check borttagen)
   ✓ API-kontakt dokumenterad
   Merged: PR #91 · 8 commits · klart 12 sep

🟢 NATIVE & INTEGRATION
Kan nu börja testa riskmotor-integrationen.
   ✓ Initial Risk Module setup
   ✓ Test-foundation för Native-layer
   Merged: PR #93 · 6 commits · klart 13 sep

═══════════════════════════════════════════════════════════════
Summa denna vecka: 3 arbetsområden mergade + extensive testing
```

---

**SLIDE ①B: "BYGGDE VIDARE DENNA VECKA"**

```
Parallellt pågick omfattande arbete inom riskberäkning och integration.

═══════════════════════════════════════════════════════════════

🔵 NATIVE & RISKMOTOR (pågår)
Omfattande utbyggnad av riskberäkning — rolling estimates och utökade tester.
   → Risk calculation logic utbyggd (rolling 3m, 12m, YTD)
   → Additional tests för edge cases
   → API-integration test-verktyg
   Pågår: PR #92 · 14 commits denna vecka · Fortsätter nästa vecka

🔵 FRONTEND & DASHBOARD
Layout, CSS-moduler och responsivitet påbörjades.
   → Dashboard-komponenter byggda
   → Responsive layout för desktop/tablet/mobile
   Pågår: 8 commits denna vecka · Design-review planerad

═══════════════════════════════════════════════════════════════
Summa denna vecka: Omfattande foundation för nästa iterations integration
```

**Vad som är rätt här:**
- ✅ Arbetsområden, inte issue-nummer (bredare och mer meningsfullt)
- ✅ Två separata slides (inte tvingat samma sida)
- ✅ Effekt för varje område (varför detta arbete spelar roll)
- ✅ "Levererat" = mergat till develop (verifierat i git)
- ✅ "Byggde vidare" = pågår med substantiell framdrift denna vecka
- ✅ Orange betyder "framskridande", inte risk eller blocker
- ✅ Känslan är: "Vi gjorde MYCKET arbete förra veckan" (inte "nästan ingenting")

---

## 📸 VISUELL VERIFIERING — Skärmdumpar från Dev

**Skärmdumparna är del av "Vad gjordes"-sliden, inte separat.**

### Format

För varje feature/arbete som är klart eller framskridande:

```
✓ #52 – Portfolio summary (Rasha)
  🟢 Gör Frontend-integration möjlig
  Merged PR #81 · 4 commits · klart 11 sep
  
  [SCREENSHOT: Inloggning fungerar]
  [SCREENSHOT: Portfolio-dashboard visas korrekt]
```

### Var Skärmdumparna Sparas

```
_memory/screenshots/
├── 01-login.png              ← Frontend denna vecka
├── 02-portfolio-dashboard.png ← Frontend denna vecka
├── 03-api-response.png        ← Backend denna vecka
└── 04-mobile-view.png         ← Native denna vecka
```

### Process Före Möte

1. Developer kör dev-miljön från developer-branchen
2. Loggar in, testar funktionen
3. Tar skärmdumpar (login, portfolio, API-svar, mobile)
4. Sparar i _memory/screenshots/
5. Commit & push
6. Säger till AI: "Ge mig en presentation"
7. Presentationen letar själv efter skärmdumparna
8. Inkluderar dem på rätt team-slide under "Vad gjordes"

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
