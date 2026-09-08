# 🤖 Vad Kan Jag (AI) Hjälpa Dig Med?

**Läs denna fil när du inte vet vad du ska be mig om.**

---

## 📝 MÖTESPROTOKOLLET - Primär Källa

**FÖRE ALLA MÖTES-FRÅGOR - LÄSA FÖRST:**

Mötesprotokollet är **PRIMÄR källa** för:
- Vad diskuterades på mötet?
- Vilka beslut togs?
- Vad är action items?
- Vad är nästa möte?

**Raw-länk för AI:**
- TXT: `https://docs.google.com/document/d/1WD9XJBVrE49Csqz-XYiLgejlKlCA4t5sWiwoTkNiTD8/export?format=txt`

**FORMAT I MÖTESPROTOKOLLET:**
```
I = Information (bara info, ingen åtgärd)
B = Beslutdiskussion (beslut togs här)
```

**Exempel ur protokoll:**
```
I: Backend-API är 80% klar
B: BESLUT - Vi pausar FX-optimering tills Oct 1
I: CTO feedback från Sep 3 är insamlad
B: BESLUT - Frontend prioriteras till Sep 20
```

**AI ska:**
1. Läsa mötesprotokollet
2. Identifiera B = Beslut (VIKTIGA!)
3. Identifiera I = Information (kontext)
4. Rapportera vilka beslut som togs

**Instruktion:** Läs protokollet INNAN du svarar på frågor om möten eller action items!

---

## 🎯 MÖTEN - Facilitering & Planering

### 1. Sprintmöten (Hela Teamet)

**Torsdags Vecko-Slutabstämning** (15:00-15:30, 30 min)
```
Du: "Förbered torsdags-möte"
AI: Läser git log → CURRENT_STATUS.md → RISKS.md
AI: Presenterar fresh status + agenda

Du: "Kör torsdags-möte"
AI: Faciliterar mötet enligt struktur
   - Vad blev klart denna vecka?
   - Vilka issues blir inte klara?
   - Vilka blockers?
   - Plan för nästa vecka

AI: Uppdaterar dokumenten direkt (VS Code) eller visar sammanfattning (Web)
```

**Måndags Sprintplanering** (09:00-12:00, 3 tim)
```
Du: "Förbered sprintplanering"
AI: Läser denna veckas fokus, risker, top issues
AI: Presenterar agenda

Du: "Kör sprintplanering"
AI: Faciliterar mötet enligt struktur
   - Denna veckas fokus
   - Diskutera & prioritera backlog
   - Estimera kapacitet per team
   - Tilldela issues åt personer

AI: Uppdaterar CURRENT_STATUS.md + RISKS.md
```

### 2. Team-Specifika Möten (Backend/Frontend/Native)

```
Du: "Förbered Backend-möte" (eller Frontend / Native)
AI: Läser denna teams commits + aktuella issues
AI: Föreslår diskussions-punkter

Du: "Kör Backend-möte"
AI: Faciliterar teknisk diskussion
   - Arkitektur-beslut
   - Code review & refactoring
   - Problem-lösning
   - Knowledge-sharing

AI: Dokumenterar beslut och action items
```

---

## 📊 PRE-MÖTE PREP

### "Förbered Nästa Möte"
```
Du: "Förbered nästa möte"
AI: Läser git log denna vecka
AI: Analyserar CURRENT_STATUS.md
AI: Granskar RISKS.md
AI: Visar:
   ✅ Vad blev klart denna vecka
   ✅ Vilka issues är WIP
   ✅ Vilka är blockers
   ✅ Vilka risker är nya
   ✅ Mötes-agenda

Du är ready att möte!
```

---

## 📝 DOKUMENTATION & STATUS

### "Vilka Issues Är I Progress?" (ELLER "Vad Jobbar Teamet På?")
```
Du: "Vilka issues är I Progress?"

AI: (MÅSTE följa denna prioritering)

PRIMÄR KÄLLA - GitHub Project Board:
   1. ✅ Läser: https://github.com/orgs/chas-challenge-2026/projects/31/views/1

PRIMÄR FALLBACK - Google Sheets:
   2. Om GitHub misslyckas → Läser: https://docs.google.com/spreadsheets/d/1TECz-PkbJhK6Jux6tpjcXDNvUNUZGI_nnIDE5rKr5UI/edit?gid=869242669#gid=869242669

PRESENTERA:
   3. Lista issues per status:
      - 🟢 To Do
      - 🟡 In Progress (PRIORITET)
      - ✅ Done

VIKTIGASTE:
   4. ⚠️ Berätta källa: "Läst från: GitHub" eller "Läst från: Google Sheets"
```

---

### "Ge Mig En Status-Rapport" (ELLER "Vad är projektets status?")
```
Du: "Status-rapport denna vecka"

AI: (MÅSTE följa denna prioritering EXAKT)

PRIMÄR KÄLLA - GitHub Project Board:
   1. ✅ Läser GitHub Project Board: https://github.com/orgs/chas-challenge-2026/projects/31/views/1
   2. ✅ Läser Open PRs: https://github.com/chas-challenge-2026/avanza-team1/pulls?q=is%3Aopen+is%3Apr
   3. ✅ Läser Closed/Merged PRs: https://github.com/chas-challenge-2026/avanza-team1/pulls?q=is%3Apr+is%3Aclosed

PRIMÄR KÄLLA - Google Sheets (Risker & Assets):
   4. ✅ Läser Risker: `https://docs.google.com/spreadsheets/d/1A8XHxyAdbyrWlHSWTNgtwkKACdSiUr3F/export?format=csv&gid=1796827285`
   5. ✅ Läser Assets: `https://docs.google.com/spreadsheets/d/1A8XHxyAdbyrWlHSWTNgtwkKACdSiUr3F/export?format=csv&gid=684132349`

PRIMÄR FALLBACK - Google Sheets:
   5. Om GitHub misslyckas → Läser Google Sheets Project Board: https://docs.google.com/spreadsheets/d/1TECz-PkbJhK6Jux6tpjcXDNvUNUZGI_nnIDE5rKr5UI/edit?gid=869242669#gid=869242669
   6. Om GitHub PRs misslyckas → Läser Google Sheets PR Status: https://docs.google.com/spreadsheets/d/1TECz-PkbJhK6Jux6tpjcXDNvUNUZGI_nnIDE5rKr5UI/edit?gid=743460023#gid=743460023

SEKUNDÄR FALLBACK:
   7. Om allt misslyckas → Läser PR_UPDATES.md

PRESENTERA:
   8. Presenterar:
      - Issues I Progress (från Project Board)
      - 🟢 Open PRs + status
      - ✅ Recently merged PRs
      - Blockers & status
      - Risk-uppdateringar
      - Plan för nästa vecka

VIKTIGT - MÅSTE ALLTID GÖRA:
   9. ⚠️ BERÄTTA EXAKT vilken källa du använt för VARJE SEKTION:
      "Projekt Status: Läst från GitHub"
      "PRs: Läst från Google Sheets (GitHub var otillgänglig)"
      etc.
```

### "Uppdatera Dokumenten"
```
Du: "Uppdatera CURRENT_STATUS.md"
AI: Läser nuvarande fil
AI: Läser git log denna vecka
AI: Uppdaterar automatiskt (VS Code)
   - Completed This Week
   - Issues Planned
   - Team Capacity
   - Blockers & Risks

Du: "Uppdatera RISKS.md"
AI: Granskar alla risker
AI: Uppdaterar status på befintliga
AI: Identifierar nya risker från git log
AI: Uppdaterar automatiskt (VS Code)
```

---

## 🎯 PLANERING & PRIORITERING

### "Planera Denna Vecka"
```
Du: "Planera denna vecka"
AI: Läser SCHEDULE.md (denna veckas fokus)
AI: Läser BACKLOG.md (prioriterade issues)
AI: Läser RISKS.md (vad kan gå fel?)
AI: Presenterar:
   - Denna veckas fokus
   - Top 5 prioriterade issues
   - Vilka är blockers från senast
   - Vilka risker måste vi adressera
   - Rekommenderad plan
```

### "Vad Är Nästa Kritisk Sak?"
```
Du: "Vad är nästa kritisk sak?"
AI: Läser SCHEDULE.md (deadlines)
AI: Läser RISKS.md (HIGH/CRITICAL)
AI: Läser BACKLOG.md (prioritering)
AI: Säger:
   ✅ Nästa deadline
   ✅ Största risk
   ✅ Viktigaste issue
   ✅ Vad måste vi göra denna vecka
```

---

## 🚨 RISK-HANTERING

### "Vilka Är De Största Riskerna?"
```
Du: "Vilka är de största riskerna?"
AI: Läser RISKS.md
AI: Presenterar:
   - Top 3 CRITICAL/HIGH risker
   - Status på varje
   - Mitigations gjorda
   - Vad behöver vi göra
   - Deadline för varje risk
```

### "Ge Mig Risk Status Presentation" (Nuläge på Risker)
```
Du: "Ge mig risk status presentation" 
    ELLER "Risk-rapport denna vecka"
    ELLER "Hur ser det ut med risker?"

AI: (MÅSTE följa denna prioritering)

PRIMÄR KÄLLA - Google Sheets:
   1. ✅ Läser Risker: https://docs.google.com/spreadsheets/d/1A8XHxyAdbyrWlHSWTNgtwkKACdSiUr3F/export?format=csv&gid=1796827285
   2. ✅ Läser Assets: https://docs.google.com/spreadsheets/d/1A8XHxyAdbyrWlHSWTNgtwkKACdSiUr3F/export?format=csv&gid=684132349

PRESENTERA (i denna ordning):
   3. Executive Summary (1-2 mening):
      - Antal CRITICAL/HIGH risker
      - Antal mitigations pågår
      - Största hot denna vecka

   4. Risk Status Tabell (Google Sheets format):
      Asset / system | Category | Risk | Status | Risk level | Mitigation | Owner | Deadline
      
   5. Risker Efter Status:
      - 🔴 CRITICAL risker (lista alla)
      - 🟠 HIGH risker (lista alla)
      - 🟡 MEDIUM risker (lista alla)
      
   6. Mitigations i Progress:
      - Vad jobbar vi på?
      - Framsteg denna vecka?
      - Blockers?
      
   7. Nästa Steg:
      - Vad måste vi adressera denna vecka?
      - Vilka risker närmar sig deadline?
      - Nya risker som behöver dokumenteras?

VIKTIGT:
   ⚠️ BERÄTTA vilken källa: "Läst från: Google Sheets Risker"
   ✅ Presentera i tabellformat (klar för copy-pasta)
   ✅ Fokusera på CRITICAL/HIGH (ignorera LOW)
   
VERIFIKATION MOT NULÄGET:
   🔍 För varje risk - stämma av:
   - Risk säger "Mitigated" → Verifiera: Finns commits för denna mitigation? (kolla git)
   - Risk säger "In Progress" → Verifiera: Pågår arbetet? Är det mergat?
   - Risk säger "Open" → Verifiera: Är detta fortfarande en hot? Eller redan löst?
   - 🚨 Mismatch → FLAGGA: "⚠️ Risk #XX verkar löst men status uppdaterad i Google Sheets?"
   
   För varje asset:
   - Asset säger "Active" → Verifiera: Finns den fortfarande i koden?
   - Asset säger "Deprecated" → Verifiera: Är den verkligen borttagen?
   - 🚨 Mismatch → FLAGGA: "⚠️ Asset #XX status stämmer inte med nuläget"
```

### "Uppdatera Risk Register"
```
Du: "Ny risk: Back-testing är långsam"
AI: Läser RISKS.md
AI: Lägger till ny risk enligt template
AI: Skapar mitigation-plan
AI: Uppdaterar automatiskt (VS Code)
```

---

## 💬 MÖTES-SUPPORT

### "Ge Mig Issues Nuläge Presentation" (Mötes-Format)
```
Du: "Ge mig issues nuläge för mötet"
    ELLER "Issues presentation denna vecka"
    ELLER "Hur ser det ut med issues?"

AI: (MÅSTE följa denna prioritering)

PRIMÄR KÄLLA - GitHub Project Board:
   1. ✅ Läser: https://github.com/orgs/chas-challenge-2026/projects/31/views/1
   2. ✅ Läser git log denna vecka (commits på develop)

PRIMÄR FALLBACK - Google Sheets:
   3. Om GitHub misslyckas → Läser: https://docs.google.com/spreadsheets/d/1TECz-PkbJhK6Jux6tpjcXDNvUNUZGI_nnIDE5rKr5UI/edit?gid=869242669#gid=869242669

PRESENTERA (MÖTES-FORMAT):

   📊 EXECUTIVE SUMMARY (överst):
   ┌─────────────────────────────────────┐
   │ Issues Status Denna Vecka           │
   │ Done denna vecka:      X issues     │
   │ In Progress:           X issues     │
   │ To Do / Backlog:       X issues     │
   │ Blockers:              X issues     │
   │ Kritiska:              X issues     │
   │ Dagar till deadline:   X dagar      │
   └─────────────────────────────────────┘

   ✅ COMPLETED (Denna vecka):
   Tabell: #XX | Title | Owner | Branch | Merged
   - Visa alla issues som är Done denna vecka
   - Visa om de är mergade till develop
   
   🟡 IN PROGRESS (Pågår nu):
   Tabell: #XX | Title | Owner | Status | Progress % | Blocker?
   - Visa alla issues i In Progress
   - Flagga blockers (🔴)
   - Flagga kritiska (⚠️)
   - Visa progress/commits denna vecka
   
   🟢 TO DO / BACKLOG (Nästa på tur):
   Tabell: #XX | Title | Priority | Estimate | Owner | Ready?
   - Top 5 prioriterade
   - Vilka kan starta nästa?
   - Vilka är kritiska för deadline?
   
   🚨 BLOCKERS & KRITISKA:
   - Lista alla blockers (red flags)
   - Lista alla CRITICAL priority issues
   - Vad behöver vi göra?
   - Vilka är beroenden?
   
   ⏰ DEADLINE RISK:
   - Dagar kvar till Sep 24 (CTO deadline)
   - Issues som måste vara Done innan SWE23
   - Risk för att inte hinna?

VIKTIGASTE:
   ⚠️ BERÄTTA källa: "Läst från: GitHub Project Board"
   ✅ Presentera i tabellformat (mötes-klar)
   ✅ Fokusera på KRITISKA och BLOCKERS
   ✅ Visa nästa backlog-items
   ✅ Ge konkreta rekommendationer
   
VERIFIKATION (KRITISK):
   🔍 STÄMMA AV MOT NULÄGET - för VARJE issue:
   - Issue säger "Done" → Verifiera: Är den mergad till develop? (kolla git log)
   - Issue säger "In Progress" → Verifiera: Finns commits denna vecka? (kolla git)
   - Issue säger "To Do" → Verifiera: Är den verkligen inte påbörjad?
   - 🚨 Om något stämmer inte → FLAGGA DETTA: "⚠️ Issue #XX säger Done men ingen merge på develop"
   
   Samma verifikation för RISKER & ASSETS:
   - Risk säger "Mitigated" → Verifiera: Finns commits för mitigation?
   - Asset säger "Active" → Verifiera: Är den faktiskt i användning?
   - Mismatch → FLAGGA: "⚠️ Risk #XX status uppdaterad i Google Sheets?"
```

### "Förbered Sprintmöte Presentation" (Nuläge + Förslag Framåt)
```
Du: "Förbered sprintmöte presentation"
    ELLER "Sprint prep - vad ska vi diskutera?"
    ELLER "Ge mig sprint meeting prep"

AI: (MÅSTE följa denna prioritering)

PRIMÄR KÄLLOR:
   1. ✅ Läser git log (commits denna vecka + senaste)
   2. ✅ Läser GitHub Project Board: https://github.com/orgs/chas-challenge-2026/projects/31/views/1
   3. ✅ Läser RISKS.md (vilka risker att diskutera)
   4. ✅ Läser SCHEDULE.md (denna veckas fokus)
   5. ✅ Läser mötesprotokollet (förra mötes action items)

PRIMÄR FALLBACK - Google Sheets:
   6. Om GitHub misslyckas → Google Sheets Project Board

PRESENTERA (MÖTES-PREP FORMAT):

   📊 SPRINT SUMMARY (överst):
   ┌─────────────────────────────────────┐
   │ Sprint Vecka XX Nuläge              │
   │ Fokus denna vecka: [från SCHEDULE]  │
   │ Förra veckan:                       │
   │  - X issues genomförda ✅           │
   │  - Y issues blockers/WIP 🟡         │
   │  - Z dagar till nästa deadline ⏰   │
   └─────────────────────────────────────┘

   ✅ VIKEN GJORT FÖRRA VECKAN:
   - Tabell: Issue # | Title | Owner | Status | Merged to develop?
   - Lista alla issues Done på GitHub Project Board
   - Vilka PRs är mergade denna vecka?
   - Vilka commits på develop?
   - Vad levererar det för värde?

   🟡 PÅGÅR - BLOCKERS & WIP:
   - Tabell: Issue # | Title | Owner | Status | Blocker? | Progress
   - Vilka är stuck?
   - Vad behöver göras för att lösa?
   - Vilka kan pushes denna veckan?
   - Vilka är nära att bli klara?

   🎯 DENNA VECKA - FOKUS & FÖRSLAG:
   - Denna veckas fokus (från SCHEDULE.md): [läs]
   - 🔴 KRITISKA issues som MÅSTE klara denna vecka
   - 🟡 HÖG prioritet issues
   - 🟢 MEDIUM prioritet om det finns tid
   - Kapacitet: ~35h per person denna vecka

   🚨 RISKER & DEADLINES ATT DISKUTERA:
   - Vilka risker från RISKS.md påverkar denna vecka?
   - Vilka är nära sitt mitigation-datum?
   - Vilka deadlines närmar sig? (Sep 24 CTO-underlag!)
   - Vilka arkitektur-beslut behövs?
   - Vilka dependency-issues mellan teams?

   🛣️ VÄGAR FRAMÅT - REKOMMENDATIONER:
   - "Vi bör prioritera [X] för att [Y]"
   - "Risk att vi inte hinner med [Z] - förslag: fokusera på MVP"
   - "Deadline för [W] är nästa vecka - rekommendation: starta nu"
   - "[Team A] behöver hjälp från [Team B] - kan vi lösa det?"
   - "Action items från förra möte - status:" [verifiera]

   📋 MÖTES-AGENDA FÖRSLAG:
   1. (5 min) Summera vad som blev gjort ✅
   2. (10 min) Diskutera blockers från förra veckan
   3. (15 min) Gå igenom denna veckas fokus & risker
   4. (20 min) Prioritera och estimera issues
   5. (10 min) Tilldela issues + kickoff

KRITISKT:
   ⚠️ BERÄTTA källa: "Läst från: GitHub Project Board + git log"
   ✅ Presentera i mötes-format (klar att presentera direkt)
   ✅ Fokusera på DECISIONER som behöver tas
   ✅ Ge KONKRETA rekommendationer
   ✅ Inkludera RISKER + DEADLINES
   ✅ Verifiera action items från förra möte
   
VERIFIKATION MOT NULÄGET:
   🔍 Stämma av mellan sources:
   - Project Board säger "Done" → Verifiera: Mergad till develop? (kolla git)
   - Issue säger "In Progress" → Verifiera: Commits denna vecka?
   - Förra mötes action items → Verifiera: Är de genomförda?
   - 🚨 Mismatch → FLAGGA: "⚠️ Issue #XX säger klar men inte mergad"
```

### "Vad Ska Vi Diskutera I Mötet?"
```
Du: "Vad ska vi diskutera i mötet?"
AI: Läser CURRENT_STATUS.md
AI: Läser RISKS.md
AI: Läser git log
AI: Föreslår diskussions-punkter:
   - Issues som är stuck
   - Beroenden mellan teams
   - Risker som påverkar alla
   - Deadlines närmar sig
   - Vad gick bra/dåligt senast
```

### "Ge Mig Mötes-Agenda"
```
Du: "Ge mötes-agenda för idag"
AI: Presenterar struktur för mötet
AI: Listar diskussions-punkter
AI: Visar tid per punkt
AI: Förbered dig för möte!
```

---

## 🚨 RISKER OCH ASSETS - Hantering

**Google Sheets är ENDA källan för dokumenterade risker och assets**

### Scenario 1: Användaren Frågar "Vilka Risker För Denna Issue?"
1. Läs Google Sheets (Risker CSV)
2. Identifiera relevanta risker från sheet
3. Presentera i tabellformat (klar för copy-pasta):
   ```
   Asset / system | Category | Risk | Cause | Consequence | Likelihood | Impact | Risk score | Risk level | Response | Mitigation | Owner | Status
   ```

### Scenario 2: Användaren Frågar "Vilka Risker BORDE Finnas Men Står Inte I Google Sheets?"
1. Analysera issuen
2. Identifiera potentiella risker
3. Identifiera saknade assets
4. Presentera BÅDE i tabellformat (klar för copy-pasta till Google Sheets):

**Nya Risker Som BORDE Dokumenteras:**
```
Asset / system | Category | Risk | Cause | Consequence | Likelihood | Impact | Risk score | Risk level | Response | Mitigation | Owner | Status
```

**Saknade Assets Som BORDE Dokumenteras:**
```
System / application | Owner | Lifecycle status | Description / purpose | Type of information | Personal data | Criticality
```

**Instruktion:** "Dessa risker/assets finns inte i Google Sheets än. Kopiera och lägg till dem om du håller med."

---

## 🎫 ISSUES - Format & Presentation

**VIKTIGT:** När du frågar om nya issues eller uppdateringar - presentera i denna tabellformat:

```
Title | Body | Assignees | Status | Priority | Labels | Estimate
------|------|-----------|--------|----------|--------|----------
feat(frontend): Add LoginForm | Implementera inloggnings-form med TypeScript. Se UI_DESIGN_REFERENCE.md mockup 01_login.webp | @developer-name | To Do | High | frontend, feature, #26 | 8h
```

**Kolumner (i denna ordning):**
1. **Title** - Issue-titel (format: `type(scope): message`)
2. **Body** - Beskrivning av vad som ska göras
3. **Assignees** - Vem jobbar på det (@username)
4. **Status** - To Do / In Progress / In Review / Done
5. **Priority** - Critical / High / Medium / Low
6. **Labels** - Tags (comma-separated, inkludera GitHub-issue #nummer)
7. **Estimate** - Tidsuppskattning (4h, 8h, 16h, 1d, etc.)

**INNAN VI BÖRJAR - RISK ASSESSMENT:**

1. ⚠️ AI MÅSTE fråga: "Är du medveten om några risker för denna issue?"
2. Om JA - Presentera riskerna i Google Sheets-format (Asset / system | Category | Risk | osv.)
3. Om NEJ - Presentera eventuella risker från Google Sheets som är relevanta

### Assets & Risker Presentation (Efter issuen)

**Assets för denna issue (Google Sheets format):**
```
System / application | Owner | Lifecycle status | Description / purpose | Type of information | Personal data | Criticality
```

**Risker för denna issue (Google Sheets format):**
```
Asset / system | Category | Risk | Cause | Consequence | Likelihood | Impact | Risk score | Risk level | Response | Mitigation | Owner | Likelihood after fix | Impact after fix | Residual score | Residual level | Status
```

**Workflow:**
1. AI presenterar issuen (tabellformat)
2. AI frågar: "Är det någon risk du tänker på för denna issue?"
3. AI presenterar assets (Google Sheets format)
4. AI presenterar relevanta risker (Google Sheets format)

---

## 📝 COMMITS - Efter Varje Commit

**EFTER ATT ISSUEN ÄR KLAR - när du frågar om commit-meddelande:**

1. ✅ AI presenterar kort, informativt commit-meddelande (rätt format enligt TEAMSTANDARDS)
   ```
   type(scope): message (#ISSUE)
   ```

2. ⚠️ AI FRÅGAR: "Vill du se relevanta assets och risker för denna commit?"

3. 📊 **Om JA - Presentera Assets** (Google Sheets format):
   ```
   System / application | Owner | Lifecycle status | Description / purpose | Type of information | Personal data | Criticality
   ```

4. 🚨 **Om JA - Presentera Risker** (Google Sheets format):
   ```
   Asset / system | Category | Risk | Cause | Consequence | Likelihood | Impact | Risk score | Risk level | Response | Mitigation | Owner | Likelihood after fix | Impact after fix | Residual score | Residual level | Status
   ```

**Workflow:**
1. Issuen är klar
2. Du frågar AI om commit-meddelande
3. AI ger commit-text
4. AI frågar om du vill se assets/risker
5. Du svarar JA/NEJ
6. AI presenterar (om JA) i Google Sheets-format

---

## 🎨 FRONTEND-KOD HJÄLP

### "Hjälp Mig Bygga [LoginForm/PortfolioOverview/etc]"
```
Du: "Hjälp mig bygga LoginForm"

AI: (MÅSTE göra detta)
   1. Läser FRONTEND_AI_INSTRUCTIONS.md
   2. Läser UI_DESIGN_REFERENCE.md
   3. Kollar mockup 01_login.webp
   4. Baserar svaret på mockup-specen
   5. Säger: "Enligt mockup 01_login.webp behöver komponenten..."
   6. Ger TypeScript + React kod
   7. Länkar till full spec

AI: Svar innehåler:
   ✅ "Enligt mockup XX.webp..."
   ✅ Design-requirements från mockup
   ✅ React + TypeScript kod
   ✅ CSS modules (en per komponent)
   ✅ Länk till UI_DESIGN_REFERENCE.md
```

**Viktigt:** AI ska ALLTID läsa `FRONTEND_AI_INSTRUCTIONS.md` och mockups för frontend-frågor!

---

## 📚 GUIDER & INSTRUKTIONER

### "Hur Kör Jag Ett Möte?"
```
Du: "Hur kör jag ett möte?"
AI: Visar två metoder:
   1. Web-based AI (ChatGPT, claude.ai)
   2. VS Code + Claude Code (SNABBARE!)

AI: Länka till HOW_TO_RUN_MEETINGS.md
```

### "Vilka Är Kodstandarder?"
```
Du: "Vilka är kodstandarder?"
AI: Läser TEAMSTANDARDS.md
AI: Presenterar:
   - Commit-format
   - Branch-naming
   - Kod-regler per språk (BE/FE/Native)
   - PR-process
   - Vad är NOT allowed
```

### "Vad Är Kunskapen Om Projektet?"
```
Du: "Vad handlar detta projekt om?"
AI: Läser PROJEKTKONTEXT.md
AI: Presenterar:
   - Kundens problem (Anna)
   - MVP-features
   - Teknisk stack
   - Tidsplan
   - Vad bygger vi och varför
```

---

## 🔍 UTREDNING & ANALYS

### "Vad Är Status På Issue #X?"
```
Du: "Vad är status på issue #52?"
AI: Läser git log för #52
AI: Läser CURRENT_STATUS.md
AI: Presenterar:
   - Är den DONE / WIP / Blocked?
   - Senaste commits
   - Vem jobbar på den?
   - Är den på rätt väg?
   - Något som blockerar?
```

### "Vilka Issues Är Blocked?"
```
Du: "Vilka issues är blockade?"
AI: Läser CURRENT_STATUS.md
AI: Läser RISKS.md
AI: Läser git log för inaktiva branches
AI: Listar:
   - Vilka är stuck
   - Varför
   - Vem kan hjälpa
   - Vad behöver göras
```

---

## 🎯 ISSUE-HJÄLP - Pedagogisk Vägledning (VAD, HUR, VARFÖR)

### "Hjälp Mig Med Denna Issue #X"

**Hur du copy-pastas issue-data som AI kan läsa:**

```
1. Öppna issue på GitHub: 
   https://github.com/chas-challenge-2026/avanza-team1/issues/52

2. Copy-pasta issue-innehållet i detta format:

---
ISSUE CONTEXT:
Title: [Issue title från GitHub]

Description: 
[Hela issue-beskrivningen]

Acceptance Criteria:
- [ ] Criterion 1
- [ ] Criterion 2
- [ ] Criterion 3

Assignee: [Du]
Labels: [Any labels]
---

Du: "Vad bör jag fokusera på här? Förklara VAD, HUR och VARFÖR för varje steg."
```

**AI kommer då att (PEDAGOGISKT):**

För **VARJE STEG** presentera:
- 🎯 **VAD** - Vad behöver jag göra? (konkret uppgift)
- 🔧 **HUR** - Hur gör jag det? (steg-för-steg instruktion)
- 💡 **VARFÖR** - Varför gör jag det så? (resonemang & lärdom)

**EXEMPEL på pedagogisk respons:**

```
STEG 1: Skapa API-endpoint

🎯 VAD:
Du behöver skapa en REST-endpoint GET /api/portfolio 
som returnerar användarens portföljdata

🔧 HUR:
1. Öppna backend/src/controllers/PortfolioController.java
2. Lägg till denna metod:
   @GetMapping("/api/portfolio")
   public ResponseEntity<PortfolioDTO> getPortfolio() { ... }
3. Implementera logik för att hämta data från database

💡 VARFÖR:
- Endpoint måste vara REST-kompatibel (GET för att läsa data)
- /api/portfolio är RESTful naming convention
- ResponseEntity<PortfolioDTO> ger TypeScript-compatible format
- Denna struktur följer TEAMSTANDARDS.md

---

STEG 2: Skapa Integration Test

🎯 VAD:
Du behöver skriva ett test som verifierar att 
endpoint returnerar rätt data

🔧 HUR:
1. Skapa fil: backend/src/test/PortfolioControllerTest.java
2. Skriv test med @SpringBootTest annotation
3. Mock database-data
4. Verifiera att endpoint returnerar korrekt DTO

💡 VARFÖR:
- Integration tests kollar att alla lager fungerar tillsammans
- @SpringBootTest startar whole spring context
- Mocking gör test snabb och reproducible
- Denna approach är DEFINITION_OF_DONE requirement
```

**PLUS: Uppmuntran & Kontrollfrågor**

Under gången får du också:
- 🎉 **Uppmuntran** - "Du är på rätt väg!", "Bra tänk!"
- 🧠 **Kontrollfrågor** - "Kan du förklara varför...?" (för att befästa kunskap)
- 🔗 **Kopplingar** - "Du gjorde något liknande här...", "Märkte du mönstret?"
- 🌍 **Bred förståelse** - Hur detta kopplar till andra delar av projektet
- ⚖️ **Balanserad ton** - "Det här är komplext FAST du klarar det"
- 😊 **Roligt att lära** - Du blir expert genom att förstå VARFÖR

**Resultat:** Du förstår inte bara VAD du gör, utan VARFÖR det är viktigt - och du blir EXPERT!

### "Är Min Implementering Klar?"

```
Du: [Paste samma issue-innehål som ovan]
    
    Jag har gjort detta:
    - Feature implementerad
    - Tests skrivna
    - PR: https://github.com/.../pull/123
    
    Du: "Uppfyller jag acceptance criteria?"

AI: Validerar mot:
   ✅ Definition of Done
   ✅ Acceptance Criteria
   ✅ Kodstandarder (TEAMSTANDARDS.md)
   
AI: Presenterar:
   ✅ Vad som är bra
   ⚠️ Vad som saknas
   ❌ Vad som inte uppfyller krav
```

### "Vilken Issue Ska Jag Göra Nästa?"

```
Du: "Vilken issue ska jag prioritera nästa?"

AI: Läser:
   - BACKLOG (prioritering från backlog_template)
   - RISKS.md (vilka risker påverkas)
   - CURRENT_STATUS.md (beroenden)
   
AI: Rekommenderar:
   - Top 3 candidates
   - Varför dessa är viktiga
   - Beroenden att vara medveten om
   - Vilka är BLOCKED vs READY
```

---

## 💼 VANLIGA UPPGIFTER (FRÅN SKILLS)

### "Ge Mig En Commit-Besked"
```
Du: "Jag skapade en ny React-komponent för dashboard"
AI: Läser TEAMSTANDARDS.md (commit-format)
AI: Presenterar:
   "build(frontend): Create dashboard panel components with CSS modules (#26)"

Format: type(scope): message (#issue)
```

### "Förklara Arkitektur-Valet"
```
Du: "Varför använder vi C++ för back-testing?"
AI: Läser DECISIONS.md
AI: Presenterar:
   - Valet
   - Varför
   - Påverkan
   - Alternativ som övervägdes
```

### "Är Detta Godkänt?"
```
Du: "Jag skrev en ny feature - är den godkänd?"
AI: Läser DEFINITION_OF_DONE.md
AI: Validerar arbetet mot checkboxar
AI: Presenterar:
   ✅ Vad som är bra
   ⚠️ Vad som saknas
   ❌ Vad som inte uppfyller krav
```

### "Vad Fokuserar Vi På Denna Vecka?"
```
Du: "Vad fokuserar vi på V37?"
AI: Läser SCHEDULE.md
AI: Läser DEFINITION_OF_DONE.md
AI: Presenterar:
   - Vecka fokus
   - PL-prioriteringar
   - Deadlines
   - Vad ska prioriteras
```

---

## 🎓 LÄRANDE & MENTORSKAP

### "Ge Mig Tips För Denna Vecka"
```
Du: "Tips för denna vecka?"
AI: Läser denna vecka's arbete
AI: Läser RISKS.md
AI: Läser SPRINT_PLANNING.md
AI: Ger:
   - Vad gick bra senast
   - Vad kan vi förbättra
   - Tips för framsteg
   - Vad ska vi fokusera på
   - Vad ska vi vara försiktiga med
```

### "Förklara Arkitektur-Beslutet"
```
Du: "Varför använder vi C++ för back-testing?"
AI: Läser DECISIONS.md
AI: Söker efter beslutet
AI: Förklarar:
   - Varför beslutet gjordes
   - Vilka alternativ fanns
   - Vilka trade-offs
   - Vad lärde vi oss
```

---

## 🚀 QUICK COMMANDS

Korta kommandon du kan använda:

```
"Status" eller "Rapport"           → Ge status-rapport
"Issues nuläge" eller "Issues"     → Issues status presentation
"Sprint prep" eller "Sprint meeting" → Sprint möte prep-presentation
"Plan" eller "Vad nästa?"          → Vad ska vi göra nästa
"Risks" eller "Vad är riskerna?"   → Visa risker
"Risk presentation"                → Nuläge på risker (detaljerat)
"Mötes-prep"                       → Förbered mötet
"Blocker?" eller "Vad stoppar oss" → Visa blockers
"Help" eller "Vad kan du göra?"    → Denna guide
"Prepare"                           → Förbered mötet
"Run meeting"                       → Kör mötet
"Update docs"                       → Uppdatera dokument
"Agenda"                            → Mötes-agenda
"Team meeting"                      → Team-specifikt möte
"What went well?"                   → Feedback från veckan
```

---

## 📋 FULL LISTA: Vad Jag KAN Göra

✅ **Mötes-Facilitering**
- Sprint meeting prep (nuläge + förslag framåt)
- Sprintmöten (Torsdag/Måndag)
- Team-möten (Backend/Frontend/Native)
- Pre-möte prep & agenda
- Issues status presentation (mötes-format)
- Risk status presentation (mötes-format)

✅ **Dokumentation**
- Läsa status-dokument
- Uppdatera automatiskt (VS Code)
- Presentera sammanfattningar

✅ **Analys**
- Git log → insighter
- Risk-identifiering
- Risk status presentation (nuläge)
- Issue-status tracking
- Blocker-detection

✅ **Planering**
- Denna vecka fokus
- Prioritering
- Kapacitet-planning
- Nästa steg

✅ **Mentorskap**
- Tips & lärdom
- Feedback
- Förbättrings-förslag
- Best practices

✅ **Utredning**
- Vad gick bra?
- Vad gick dåligt?
- Varför gjorde vi detta?
- Vad lärde vi oss?

---

## ❌ Vad Jag INTE KAN Göra

❌ Läsa GitHub Project direkt (du måste copy-pasta)
❌ Skapa issues i GitHub automatiskt
❌ Kolla CI/CD pipelines
❌ Debugga kod (kan ge suggestions, inte testa)
❌ Göra design-beslut åt dig (kan föreslå)
❌ Ta ansvar för resultat (du är ansvarig)

---

## 🎯 MIN ROLL: Facilitator, Inte Leader

**Jag är:**
✅ Co-worker & facilitator
✅ Dokumentations-helper
✅ Mötes-guide
✅ Status-tracker
✅ Mentorsk rådgivare

**Jag är INTE:**
❌ Team Lead (du är det)
❌ Project Manager (din roll)
❌ Decision-maker (du och teamet gör beslut)
❌ Ansvarig för resultat (du är det)

---

## 🚀 Nästa Steg

**Vet du vad du vill göra?**
- "Kör torsdags-möte" → Sprint möte
- "Förbered nästa möte" → Pre-möte prep
- "Status-rapport" → Se vad vi gjort
- "Vilka risker?" → Risk-granskning
- Något helt tredje? → Berätta, jag hjälper till!

**Vet du inte vad du vill?**
- Läs denna fil igen
- Eller fråga: "Vad bör jag göra nu?"
- Jag ger dig ett förslag baserat på git log + status

---

*Last Updated: 2026-09-04*  
*Purpose: Quick guide to AI capabilities in this project*  
*Note: This file is AI-generated help text — use it as a menu*
