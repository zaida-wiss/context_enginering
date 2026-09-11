# 📊 Status Sync Meeting — Veckovisa Alignments

**Syfte:** Se aktuell status mot deadlines, vad behöver vara klart, och impact av kommande PRs.
**Publik:** HELA TEAMET (Backend, Frontend, Native/Systemutvecklare)

**Frekvens:** Varje tisdag  
**Längd:** 45 min  
**Facilitator:** AI (läser git, GitHub, deadlines, och presenterar struktur)
**Beslut-fattar:** Produktledare + tech leads

---

## 🎯 COMMAND FOR AI

**Du kan säga:**
```
"Förbered FÖR tisdagsmötet"
```

**AI kommer då att:**
1. Läsa git log + GitHub Project Board
2. Läsa deadline-status från SPRINT_FOCUS_TIMELINE.md
3. Presentera struktur enligt denna guide
4. Stämma av med PL: "Vilka punkter vill du fokusera på?"
5. Förbereda mötet baserat på PL:s prioriteringar

---

---

## 📋 Agenda (I denna ordning)

### 1️⃣ **DEADLINES & VAD SOM MÅSTE VARA KLART** (10 min)

**Vad:** Vilka deadlines finns? Vad behöver vi leverera för att nå dessa?

```
DEADLINE 1: CTO-feedback deadline (24 sep, 16:00)
├── Vad försöker vi uppnå?
│   └── Visa CTO att MVP-flödet fungerar från start till slut
├── Vad MÅSTE vara klart?
│   ├── ✅/❌ Kärnflödet: Login → Portfolio → Allocate → Rebalance
│   ├── ✅/❌ Riskmått visas korrekt (volatilitet, Sharpe, max drawdown)
│   ├── ✅/❌ FX-konvertering fungerar (alla valutor → SEK)
│   ├── ✅/❌ Tests: 70%+ coverage, E2E test för kärnflödet
│   ├── ✅/❌ Dokumentation: README, arkitektur, beslut
│   └── ✅/❌ Git historia: tydlig, individuella bidrag synliga
├── Status denna vecka:
│   ├── Klart: Login, Portfolio overview
│   ├── Pågår: Risk calculations, FX converter
│   └── Inte startat: Rebalance suggestions
└── Gap: Behöver prioritera risk calculations denna vecka

---

DEADLINE 2: Kvaldemo (15 okt, för kund)
├── Vad försöker vi uppnå?
│   └── Imponera på kund, visa att vi förstår deras problem (Anna)
├── Vad MÅSTE vara klart?
│   ├── ✅/❌ Hela MVP-flödet fungerar live (ingen fallback)
│   ├── ✅/❌ UI matchar design mockups (clean, professional)
│   ├── ✅/❌ Data är realistisk (inte mock data)
│   ├── ✅/❌ Performance är snabb (< 2 sec för calculations)
│   ├── ✅/❌ Felhantering visar vad som gick fel (inte "error")
│   └── ✅/❌ Presentation material är klar (slides, talking points)
├── Status denna vecka:
│   ├── Klart: Kärnflöde funkar
│   ├── Pågår: UI polering, realistisk test-data
│   └── Inte startat: Presentation material
└── Gap: Behöver starta presentation prep nästa vecka

---

DEADLINE 3: Slutleverans (4 nov, 15:00)
├── Vad försöker vi uppnå?
│   └── Leverera ett komplett, dokumenterat, och testat system
├── Vad MÅSTE vara klart?
│   ├── ✅/❌ Allt från CTO deadline + all feedback implementerad
│   ├── ✅/❌ Alla AC för alla issues uppfyllda
│   ├── ✅/❌ 70%+ test coverage på alla lager
│   ├── ✅/❌ Ingen console.log, TODO, eller debug-kod
│   ├── ✅/❌ Database migrations är reproducible
│   ├── ✅/❌ README är komplett och testbar
│   ├── ✅/❌ Git history är clean (inga "fixed stuff")
│   └── ✅/❌ Fallback plan för live demo
├── Status denna vecka:
│   └── Långt bort - fokus på CTO deadline först
└── Gap: N/A, detta är prioritet EFTER kvaldemo
```

**AI Läser:** `SPRINT_FOCUS_TIMELINE.md` + `DEFINITION_OF_DONE.md` + GitHub Project Board

---

### 1.5️⃣ **PERFORMANCE & QUALITY METRICS** (5 min)

**Vad:** Lighthouse, Performance, Accessibility, Best Practices scores

```
FRONTEND METRICS (Lighthouse):
├── Performance: 78/100 (Target: 85+)
│   ├── Largest Contentful Paint: 2.8s (Target: <2.5s)
│   ├── Cumulative Layout Shift: 0.15 (Target: <0.1)
│   └── First Input Delay: 45ms (Target: <100ms) ✅
├── Accessibility: 92/100 ✅ (Target: 90+)
│   └── Missing ARIA labels? Check headings hierarchy
├── Best Practices: 88/100 ✅ (Target: 85+)
├── SEO: 95/100 ✅ (Target: 90+)

Trend denna vecka:
├── Performance: 75 → 78 ✅ (improving)
├── Accessibility: 90 → 92 ✅ (improving)
└── Overall: Trending positiv

GAP TO KVALDEMO (Target: 85+ all metrics):
❌ Performance: 7 points under target
✅ Accessibility: Above target
✅ Best Practices: Above target
✅ SEO: Above target

ACTION ITEMS:
□ Optimize LCP images (reduce size or use WebP)
□ Lazy-load non-critical components
□ Code-split frontend JS bundles
```

---

### 2️⃣ **NULÄGE PÅ DEVELOP** (5 min)

**Vad:** Vad fungerar/är klart på develop just nu?

```
Status på develop:
├── ✅ Klart & Working
│   ├── Login form component
│   ├── Mock auth module
│   └── Portfolio overview skeleton
├── ⚠️ Partial (funkar men begränsad)
│   ├── Backend API (20% endpoints)
│   └── FX converter (SEK only)
└── ❌ Not done
    ├── Risk calculations
    └── Back-test engine

Test Coverage: [X]%
Build Status: ✅ Passing
Linting: ✅ All green

GAP TO CTO DEADLINE:
❌ Risk metrics inte redo
❌ FX för alla valutor inte ready
⚠️ 70% test coverage - nu: 45%
```

**AI Läser:** `git log --oneline -20 develop` + test coverage reports

---

### 3️⃣ **PÅ GÅNG — ACTIVE BRANCHES** (10 min)

**Vad:** Vilka issues jobbar ni på? Blockeras de? Försenasde de?

```
Pågående Branches (prioriterad ordning):

🔴 CRITICAL för CTO deadline:
├── feature/#52-risk-calculations (Backend)
│   ├── Status: 40% done, varning: BEHIND
│   ├── Estimat: 16h total, redan använt: 12h
│   ├── Finns tid denna vecka: JA (3 dagar kvar)
│   ├── Blockers: None
│   ├── Kommer in i dev: DENNA VECKA (måste!)
│   ├── Impact: Risk metrics accurate → KRITISKT för CTO
│   └── Bransch: feature/#52-risk-calculations
│
└── feature/#53-fx-converter (Backend)
    ├── Status: 30% done, on track
    ├── Estimat: 12h total, använt: 4h
    ├── Finns tid denna vecka: JA (2 dagar)
    ├── Blockers: None
    ├── Kommer in i dev: DENNA VECKA
    ├── Impact: FX till alla valutor → KRITISKT för CTO
    └── Branch: feature/#53-fx-converter

🟡 IMPORTANT (behövs för kvaldemo):
├── feature/#60-target-allocation (Frontend)
│   ├── Status: Not started yet
│   ├── Estimat: 8h
│   ├── Finns tid: JA, kan starta denna vecka
│   ├── Impact: Users can set targets → KVALdemo feature
│   └── Branch: feature/#60-target-allocation
│
└── feature/#61-rebalance-suggestions (Backend)
    ├── Status: Not started
    ├── Estimat: 12h
    ├── Finns tid: JA, nästa vecka
    ├── Impact: Rebalance recommendations → KVALdemo wow factor
    └── Branch: feature/#61-rebalance-suggestions

🟢 NICE TO HAVE (efter deadlines):
└── native/#88-volatility-rolling (Native)
    ├── Status: 50% done
    ├── Estimat: 16h, använt: 8h
    ├── Impact: More accurate calculations
    └── Deadline: Efter kvaldemo
```

**AI Läser:** `git branch -v` + GitHub Project Board "In Progress" + Issue estimates

---

### 4️⃣ **PULL REQUESTS AWAITING MERGE** (15 min)

**Vad:** Vilka PRs är under review? Vad blir resultatet när de mergas?

```
PRs to develop (prioriterad ordning):

🚀 MERGE DENNA VECKA (blockar ingenting):
├── PR #46 — feat(frontend): Add LoginForm
│   ├── Status: ✅ Approved, ready to merge
│   ├── Reviewers: 2/2 approvals
│   ├── Impact on develop:
│   │   ✅ Users can log in (removes blocker for #52)
│   │   ✅ Mock auth works
│   └── Bör mergas: OMEDELBAR
│
└── PR #49 — chore: Update README with setup instructions
    ├── Status: ✅ Approved
    ├── Impact: Developers can onboard faster
    └── Bör mergas: Denna vecka

🔄 UNDER REVIEW (VÄNTAR):
├── PR #51 — feat(backend): Add portfolio endpoint
│   ├── Status: 🔄 Waiting review from @backend-lead
│   ├── Changed: GET /api/portfolio endpoint
│   ├── Tests: ✅ 2 integration tests
│   ├── Impact on develop:
│   │   ✅ Frontend can fetch real data
│   │   ✅ Unblocks other backend features
│   ├── Bör mergas: DENNA VECKA (crítica för CTO)
│   ├── Förväntad review tid: 2 dagar
│   └── Varning: Om den ej godkänns denna vecka → CTO deadline missed!
│
└── PR #55 — perf(native): Optimize volatility calc
    ├── Status: ❌ Waiting for CI test results
    ├── Impact: Risk metrics 10x faster
    ├── CI status: 🏃 Running (ETA 3h)
    ├── Bör mergas: Nästa vecka (efter test results)
    └── Not critical för CTO deadline

⛔ BLOCKED / DO NOT MERGE:
└── (ingen för närvarande)
```

**AI Läser:** `gh pr list --state open` + PR descriptions + CI status + Comments

---

### 5️⃣ **NYA BRANCHES JUST STARTED** (5 min)

**Vad:** Vilka issues startade vi nyss på? Vad förbättrar de?

```
Nyligen Startade (senaste 3 dagar):

Denna vecka:
├── feature/#60-target-allocation (Frontend, startad idag)
│   ├── Estimat: 8h
│   ├── Förbättrar: Users can customize allocation (KVALDEMO feature)
│   ├── Blockers: None identified
│   └── Branch: feature/#60-target-allocation
│
└── feature/#61-flyway-migrations (Backend, startad förra dagen)
    ├── Estimat: 16h
    ├── Förbättrar: Database schema is versioned (slutleverans krav)
    ├── Blockers: None
    └── Branch: feature/#61-flyway-migrations

Förra veckan:
├── feature/#52-risk-calculations → PÅGÅR, not merged yet
├── feature/#53-fx-converter → PÅGÅR, not merged yet
└── feature/#54-test-improvements → MERGED denna vecka
```

**AI Läser:** `git log --oneline -10 --all --grep="Started\|feature/"` + recent branch creations

---

### 6️⃣ **BLOCKERS & RISKS** (5 min)

**Vad:** Vilka blockers finns? Vilka risker är misstänkta? Hur löser vi dem?

```
ACTIVE BLOCKERS (blockerar just nu):

🔴 BLOCKER 1: PR #51 ej godkänd
├── Status: Waiting review från @backend-lead
├── Impact: Blocks issue #52 risk-calculations
├── Risk Level: KRITISK
├── Root Cause: @backend-lead är på sjukhuspermission
├── Lösningsförslag:
│   ├── Option 1: Hitta backup reviewer (@java-mentor kan review)
│   ├── Option 2: Pair programming session idag (1 tim)
│   ├── Option 3: Delay till imorgon, riskera CTO deadline
│   └── ✅ REKOMMENDERAD: Option 1 + Option 2 (reviewer + pair session)
├── Action: Kontakta @java-mentor nu, booka pair session 14:00
└── Timeline: MÅSTE lösa IDAG

🟡 BLOCKER 2: FX API integration väntar på swagger docs
├── Status: Backend-lead har ej levererat swagger docs ännu
├── Impact: Blocks PR #53 FX converter testing
├── Risk Level: MEDIUM (finns 2 dagar på buffert)
├── Root Cause: Dokumentation prioriterades under #51
├── Lösningsförslag:
│   ├── Option 1: Läs källkoden direkt, skriv swagger själv (2h)
│   ├── Option 2: Vänta på backend-lead (risk: försena deadline)
│   └── ✅ REKOMMENDERAD: Option 1 (be @api-dev skriva det idag)
├── Action: Tag @api-dev att prioritera swagger (1h arbete)
└── Timeline: Idag eller imorgon


MISSTÄNKTA BLOCKERS (kan bli problem):

🟡 RISK 1: Test coverage kräver extra arbete
├── Målat: 70%, faktiskt: 45%
├── Gap: 25% = ~20 timmar test-writing
├── Impact: Missas CTO deadline dead line on tests
├── Lösningsförslag:
│   ├── Option 1: Fokusera bara critical paths (70% -> 60%, 12h)
│   ├── Option 2: Öka test-kapacitet (anställ interim QA)
│   ├── Option 3: Parallellisera (risk-tests + fx-tests samtidigt)
│   └── ✅ REKOMMENDERAD: Option 1 + Option 3
├── Action: Identifiera critical test paths idag, distribuera denna vecka
└── Timeline: Planera denna vecka, starta nästa

🟡 RISK 2: Native module risk-calcs kräver mer tid än estimerat
├── Status: 50% done, estimat 16h
├── Risk: Backend kan behöva resultaten för CTO demo
├── Lösningsförslag:
│   ├── Option 1: Backend mockar native resultat tills native klar
│   ├── Option 2: Native går all-in denna vecka (16h sprint)
│   ├── Option 3: Prioritera: backend först, native senare
│   └── ✅ REKOMMENDERAD: Option 1 (backend mockar tills native ready)
├── Action: Backend-team startar mock-data generator idag
└── Timeline: Till CTO deadline är mock OK, native kan vara senare

🟢 RISK 3: Kvaldemo kräver realistisk data
├── Status: Vi har mock-data, behöver real Avanza data
├── Lösningsförslag:
│   ├── Option 1: Använd Avanza test-account (behöver permissions)
│   ├── Option 2: Synthetical data som ser realistiskt ut
│   └── ✅ REKOMMENDERAD: Option 1 (contact Anna för test-account)
├── Action: Kontakta Anna denna vecka för test-account
└── Timeline: Till kvaldemo (15 okt)
```

---

### 7️⃣ **GAP ANALYSIS: VÅ MISSAR VI?** (2 min)

**Vad:** Vad behövs för CTO deadline och vad är vi bakom på?

```
KRITISK GAP - CTO DEADLINE (24 sep):

Behövs:            │ Status        │ Tid kvar  │ Risk  │ Blocker?
──────────────────────────────────────────────────────────────
Risk metrics       │ 40% done      │ 3 dagar   │ 🔴 HIGH  │ ✅ PR #51
FX all currencies  │ 30% done      │ 2 dagar   │ 🔴 HIGH  │ ✅ Swagger
Test coverage 70%  │ Currently 45% │ 1 vecka   │ 🟡 MEDIUM │ ❌ None
Documentation      │ 80% done      │ OK        │ 🟢 LOW    │ ❌ None

MITIGATIONS:
□ Solve PR #51 blocker TODAY (call @java-mentor)
□ Get swagger docs IDAG (task @api-dev)
□ Focus critical test paths only (cut non-critical 25%)
□ Backend mockar native tills native är klar
```

---

## 🎯 Outputs från Mötet

**AI presenterar innan möte slutar:**

```
✅ MERGE DENNA VECKA:
   - PR #46 (LoginForm) → Ready now
   - PR #49 (README updates) → Ready now
   
🔴 CRITICAL WATCH:
   - PR #51 (Portfolio endpoint) → Måste godkännas IDAG för CTO deadline!
   - Branch #52 (Risk calc) → Must finish denna vecka!
   - Branch #53 (FX) → Must finish denna vecka!
   
🟡 HOLD DESSA:
   - PR #55 (Volatility opt) → Wait for CI (merge nästa vecka)
   
📅 NÄSTA VECKA:
   - Start feature/#62-performance-testing
   - Merge feature/#60 (target allocation)

⚠️ RISKS:
   - Risk metrics backend behöver 3 dagar mer arbete
   - Om PR #51 ej godkänns idag → CTO deadline i fara
   - Test coverage 25% under mål → behöver fokus nästa vecka
```

---

## 🔍 Hur AI Förbereder Denna Möte

**AI:s Pre-möte arbete (30 min innan möte):**

1. Läser `SPRINT_FOCUS_TIMELINE.md` (alla deadlines)
2. Läser `DEFINITION_OF_DONE.md` (vad betyder "klart")
3. Läser `git log develop` (vad är merged)
4. Läser `git branch -v` (vad är pågår)
5. Kör `gh pr list --state open` (alla PRs)
6. Läser GitHub Project Board (status)
7. Kompilerar gap mellan "måste klara" och "är klart"
8. Identifierar kritiska vägar och risker
9. Presenterar i möte

**Möteskommando för AI:**
```
Du: "Förbered status sync möte"
AI: [Läser allt ovan, presenterar struktur]

Du: "Kör status sync möte"
AI: [Faciliterar mötet enligt agenda ovan]
```

---

## 📝 Mötesprotokoll — Efter Möte

**AI dokumenterar:**
```markdown
# Status Sync — [Datum]

## Deadlines & Gap
- CTO deadline (24 sep): 🟡 ON TRACK (med varning)
  - Risk metrics: Bakom men recovery möjlig denna vecka
  - FX: On track
  - Tests: 25% under mål → start test sprint nästa vecka

## Merge Decisions
- ✅ PR #46, #49 → Merge now
- 🔴 PR #51 → CRITICAL: Must approve today
- 🔄 PR #55 → Hold pending CI results

## Branch Status
- #52 Risk calc: Finish by Friday (CRITICAL)
- #53 FX converter: Finish by Friday (CRITICAL)
- #60 Target allocation: On track
- #61 Migrations: On track

## Action Items & Owners
- @backend-lead: Review PR #51 by EOD today
- @risk-developer: Finish #52 by Friday (16h sprint)
- @fx-developer: Finish #53 by Friday (12h sprint)
- @qa-team: Add tests to hit 70% coverage

## Next Meeting
- Datum: [nästa vecka samma tid]
- Focus: Verify CTO deadline is met, start kvaldemo prep
```

---

## 🎨 SLIDE PRESENTATION FORMAT — NPF-Vänlig Pedagogisk Design

**Kommando för AI:**
```
Du: "Gör en PEDAGOGISK presentation av denna veckas status sync möte"
```

**Resultatet blir:**
- ✅ Först: VAD-VARFÖR-HUR-NÄR-VEM som PROSA (kort, fokuserad)
- ✅ Sedan: Visuella slides med diagrams (inte bara text!)
- ✅ Pedagogisk struktur: Problem → Tänk → Lösning
- ✅ NPF-vänlig: Mycket whitespace, tydlig hierarki, symboler, färger
- ✅ Interaktiv: Paus för diskussion efter varje "problem"-slide

---

## 🎯 PRESENTATIONENS MASTER TEMPLATE — KONSISTENT STRUKTUR

**SAMMA STRUKTUR VARJE GÅNG — Du känner igen den direkt:**

```
┌─────────────────────────────────────────────┐
│ PRESENTATION MASTER TEMPLATE (Igenkännbar) │
├─────────────────────────────────────────────┤
│                                             │
│ STEG 1: KÄLLBEKRÄFTELSE (alltid först)     │
│ ├─ ✅ Vilka källor läste jag?              │
│ ├─ ✅ Mötesprotokollet OK?                 │
│ └─ ✅ Allt källkontrollerat                │
│                                             │
│ STEG 2: VAD-VARFÖR-HUR-NÄR-VEM (denna ordning)
│ ├─ 1️⃣ VAD? — Listan                       │
│ ├─ 2️⃣ VARFÖR? — Konsekvenser              │
│ ├─ 3️⃣ HUR? — Plan                         │
│ ├─ 4️⃣ NÄR? — Timeline                     │
│ └─ 5️⃣ VEM? — Roll-assignment              │
│                                             │
│ STEG 3: VISUELL DASHBOARD (samma layout)   │
│ ├─ Progress bars per team                  │
│ ├─ Status-ikoner (✅ 🟠 ❌)                │
│ ├─ Färgkodning (🔴 🟡 🟢)                 │
│ └─ Countdown timer                         │
│                                             │
│ STEG 4: SNYGGA TABELLER (samma design)     │
│ ├─ Färgad header (blå/lila)                │
│ ├─ Alternerad radförg (vit/grå)            │
│ ├─ Status-ikoner vänster                   │
│ ├─ Procent höger                           │
│ └─ Mjuka skuggor                           │
│                                             │
│ STEG 5: PEDAGOGISKA SLIDES (Problem-Lösning)
│ ├─ Slide 1: Cover (samma design)           │
│ ├─ Slide 2-10: Problem → TÄNK → Lösning    │
│ ├─ Varje: 📖 VAD? 🛠️ HUR? 💡 VARFÖR?      │
│ └─ Slide 11: Nästa steg (samma design)     │
│                                             │
│ STEG 6: AVSLUT (samma avslut varje gång)   │
│ ├─ Action items (vem gör vad, när)         │
│ ├─ Deadline (exakt tid)                    │
│ ├─ Nästa möte (tidpunkt)                   │
│ └─ Källa (citat från mötesprotokollet)     │
│                                             │
└─────────────────────────────────────────────┘

VISUELLA LANDMARKS (samma design varje gång):

📊 Cover Slide
   • Samma symbol (📊 eller 🎯 eller ⏰)
   • Samma färgschema
   • Samma typografi

📋 Section Headers
   • Blå/lila bakgrund (konsistent)
   • Vit text, bold
   • Samma padding & storlek
   • Samma ikonstorlek (80-100px)

📈 Tabeller
   • Header: Blå, vit text (ALLTID)
   • Rader: Vit/grå alternering (ALLTID)
   • Ikoner: Vänster, konsistent (ALLTID)
   • Siffror: Höger, högerjusterad (ALLTID)

📊 Diagrammen
   • Progress bars: Avrundade ändar (ALLTID)
   • Färger: Samma palett (ALLTID)
   • Skuggor: Mjuka (ALLTID)
   • Layout: Samma proporioner (ALLTID)

🎬 Avslut
   • Action items box (färgad)
   • Deadline box (röd/orange)
   • Nästa möte (blå box)
   • Källa (grå text, liten)
```

**RESULTAT:**
- ✅ Du känner igen strukturen efter första presentation
- ✅ Snabb scanning (du vet vart information ligger)
- ✅ Professionell känsla (konsistens = ordning)
- ✅ ADHD-vänligt (förutsägbar struktur)
- ✅ Brand-känsla (detta är VÅRT presentationsformat)

---

## 🔴 KRITISKT: AI PRESENTERAR VAD-VARFÖR-HUR-NÄR-VEM (NPF-vänlig)

**Innan slides visas, MÅSTE AI presentera i denna ordning (KORT, FOKUSERAD):**

### 1️⃣ VAD? — Vad ska vi göra denna vecka?

```
┌──────────────────────────────────────────────────────┐
│ DENNA VECKA (prioriteringsordning):                  │
├──────────────────────────────────────────────────────┤
│ 🔴 MÅSTE KLARA (för CTO deadline 24 sep):            │
│    • Risk Metrics: 100%                              │
│    • FX Converter: 100%                              │
│    • Tests: 70%+ coverage                            │
│                                                      │
│ 🟡 BORDE KLARA:                                      │
│    • Kärnflödet end-to-end                           │
│    • Dokumentation updated                           │
│                                                      │
│ 🟢 NICE TO HAVE:                                     │
│    • UI polering                                     │
│    • Performance optimization                        │
└──────────────────────────────────────────────────────┘
```

### 2️⃣ VARFÖR? — Varför är detta viktigt?

```
┌──────────────────────────────────────────────────────┐
│ KONSEKVENSER:                                        │
├──────────────────────────────────────────────────────┤
│ ❌ OM VI MISSAR:                                     │
│    • CTO deadline missas → sämre intryck             │
│    • Kvaldemo blir svagare → kunden blir nöjd       │
│    • Slutleverans försenades → risker ökar          │
│                                                      │
│ ✅ OM VI KLARAR:                                     │
│    • Visar leveransprecision (viktig i branchen)     │
│    • CTO ser att vi förstår krav                     │
│    • Team får confidence boost                       │
│    • Kvaldemo blir strong pitch                      │
└──────────────────────────────────────────────────────┘
```

### 3️⃣ HUR? — Hur ska vi jobba?

```
┌──────────────────────────────────────────────────────┐
│ PLAN DENNA VECKA:                                    │
├──────────────────────────────────────────────────────┤
│ 🚀 PRIORITERING:                                     │
│    1. Risk Metrics finish (pair programming idag)    │
│    2. FX Converter finish (om tid finns)             │
│    3. Tests add (parallellt med ovan)                │
│                                                      │
│ 👥 SAMARBETE:                                        │
│    • Backend & Native jobbar tillsammans             │
│    • Frontend testar API när den kommer              │
│    • Daily standup 09:00 (5 min sync)                │
│                                                      │
│ ⚙️ VERKTYG:                                          │
│    • GitHub Project Board (track status)             │
│    • Slack #dev-updates (blockers)                   │
│    • Pair programming (om stuck)                     │
└──────────────────────────────────────────────────────┘
```

### 4️⃣ NÄR? — Når är deadline?

```
┌──────────────────────────────────────────────────────┐
│ TIMELINE:                                            │
├──────────────────────────────────────────────────────┤
│ 📅 IDAG (Tisdag):    Swagger docs + start Risk       │
│ 📅 IMORGON (Ons):    Pair programming + API test     │
│ 📅 TORSDAG:          Finish Risk Metrics + test      │
│ 📅 FREDAG:           Final touches + deployment prep │
│                                                      │
│ 🚨 HARD DEADLINE:    24 sep kl 16:00 (CTO session)   │
│                                                      │
│ ⏱️ BUFFER:           48 timmar för fixes              │
└──────────────────────────────────────────────────────┘
```

### 5️⃣ VEM? — Vem gör vad?

```
┌──────────────────────────────────────────────────────┐
│ TEAM-ANSVARSFÖRDELNING:                              │
├──────────────────────────────────────────────────────┤
│ 🔴 BACKEND TEAM:                                     │
│    • Risk Metrics API (Marco) — PRIORITY             │
│    • FX Converter (Jana) — if time                    │
│    • Test setup (both) — parallel                    │
│                                                      │
│ 🔵 FRONTEND TEAM:                                    │
│    • Wait for Risk API, then integrate               │
│    • Write integration tests                         │
│    • UI refinement (low priority)                     │
│                                                      │
│ 🟢 NATIVE/SYSTEMUTVECKLARE:                          │
│    • Support Backend with calcs verification         │
│    • QA testing                                      │
│    • Performance checks                              │
│                                                      │
│ ⚠️ BLOCKER OWNER:                                    │
│    • If PR #51 not approved → call backup reviewer   │
│    • If Swagger missing → write it directly          │
└──────────────────────────────────────────────────────┘
```

---

## 📊 NPF-VÄNLIG VISUELL LAYOUT

**Presentationen följer denna layout för ADHD/neurodiverse users:**

```
VARJE PRESENTATION:

[SYMBOL] BIG EMOJI (80-100px)
[RUBRIK] Kort titel (max 5 ord)
[VISUAL] Diagram/bild (inte bara text!)
[POINTS] Max 4 bullet points
[BRÖDTEXT] Kort förklaring (2-3 meningar)
[HANDLINGAR] Vem gör vad (explicit!)
[TIMELINE] Exakt tidslinje (inte "denna vecka")
```

### Exempel: Visuell Status-dashboard (Snygg Design)

```
╔═══════════════════════════════════════════════════════════╗
║               📊 STATUS DENNA VECKA                       ║
╠═══════════════════════════════════════════════════════════╣
║                                                           ║
║  Risk Metrics       ████████░░  80%  🔴 (CRITICAL: 1d)   ║
║  FX Converter       ██░░░░░░░░  20%  🟠 (BEHIND: 2d)     ║
║  Tests             ████░░░░░░  40%  🟠 (BEHIND: 3d)      ║
║  Documentation     ████████░░  80%  🟢 (OK)               ║
║                                                           ║
║ ─────────────────────────────────────────────────────── ║
║                                                           ║
║  🚨 BLOCKERS:       0  (All PRs green!)                   ║
║  ⏰ TIME UNTIL CTO:  5 dagar                              ║
║  📌 PRIORITIES:     Risk → FX → Tests                     ║
║                                                           ║
╚═══════════════════════════════════════════════════════════╝

(Design: Mjuka skuggor, färgade progress bars, ikoner,
avrundade hörn, lekfull känsla)
```

### Exempel: Snygg Tabell (Active Issues)

```
╔═══════════════════════════════════════════════════════════╗
║             ✅ ACTIVE ISSUES - DENNA VECKA                ║
╠══════╦═══════════════════════╦═════════╦════════╦═══════╣
║ ID   ║ ISSUE               ║ OWNER   ║ STATUS ║ %     ║
╠══════╬═══════════════════════╬═════════╬════════╬═══════╣
║ ✅   ║ #52 Risk Metrics    ║ Marco   ║ Done   ║ 100%  ║
║ 🟠   ║ #53 FX Converter    ║ Jana    ║ In Prog║ 60%   ║
║ 🟡   ║ #60 Target Alloc.   ║ Anna    ║ Ready  ║ 0%    ║
║ ❌   ║ #61 Rebalance       ║ Marco   ║ Blocked║ 20%   ║
║ 🔵   ║ #88 Tests           ║ QA Team ║ Ready  ║ 0%    ║
╚══════╩═══════════════════════╩═════════╩════════╩═══════╝

(Design: Färgad blå header, alternerade radfarger,
status-ikoner, avrundade hörn, mjuka skuggor)
```

### Exempel: Team-ansvars diagram

```
                    ┌──────────────────┐
                    │   CTO DEADLINE    │
                    │   24 sep 16:00    │
                    └────────┬──────────┘
                             │
                ┌────────────┼────────────┐
                │            │            │
           ┌────▼────┐  ┌───▼────┐  ┌───▼────┐
           │ BACKEND │  │FRONTEND │  │ NATIVE │
           │ (Marco) │  │ (Anna)  │  │(Kiran) │
           └────┬────┘  └───┬────┘  └───┬────┘
                │            │           │
        ┌──────▼─┐    ┌─────▼──┐   ┌───▼────┐
        │ Risk   │    │ Test   │   │ Verify │
        │Metrics │    │ API    │   │ Calcs  │
        └────────┘    └────────┘   └────────┘
```

### Exempel: Timeline visualisering

```
TIS  │  ONS  │  TOR  │  FRE  │  [BUFFER]  │ CTO
─────┼───────┼───────┼───────┼────────────┼────
✅✅ │ ✅    │ ✅    │ ✅✅   │    ✅✅     │ 📊
     │       │       │       │            │
Risk │ Risk  │ Risk  │ Tests │ Final fix  │ Demo
Start│ +API  │ +Test │ +Docs │ + deploy   │ time!
     │       │       │       │            │
```

---

## 🔴 KRITISKT — INNAN PRESENTATION: MÖTESPROTOKOLLET FÖRST!

**Om du säger:** `"Ge mig en presentation till mötet"`

**AI MÅSTE först:**
1. Läsa mötesprotokollet (raw-länk)
2. Läsa Git log, GitHub Project Board, Google Sheets, etc
3. Bekräfta alla lästa källor
4. **RENSA BORT tidigare samtalhistorik från svaret** ← VIKTIGT!
5. SEDAN presentera baserat ENDAST på källorna

**AI SKA SÄGA:**
```
"Jag läser källorna för denna presentation...

✅ LÄSTA KÄLLOR:
   • Mötesprotokollet (från raw-länk)
   • GitHub Project Board (denna vecka)
   • Git log (commits denna vecka)
   • SPRINT_FOCUS_TIMELINE.md
   • Google Sheets Risker

FRÅN DESSA SER JAG:
- Senaste beslut (B = Beslut): [lista]
- Action items från förra veckan: [lista]
- Feedback från PL/CTO: [lista]
- Denna veckas fokus: [lista]

PRESENTATIONEN (baserad endast på ovan):"
```

**🔴 VIKTIGT — RENSA SAMTALHISTORIK:**

AI SKA **INTE** säga:
- ❌ "Som vi diskuterade tidigare..."
- ❌ "Du nämnde att..."
- ❌ "Vi pratade om..."
- ❌ "Från vår tidigare konversation..."

AI SKA säga:
- ✅ "Enligt mötesprotokollet..."
- ✅ "Från GitHub Project Board..."
- ✅ "Git log visar..."
- ✅ "Från SPRINT_TIMELINE.md..."

**VARFÖR?**
- Presentationen ska vara fristående (kan delas utan konversationshistorik)
- Baseras på dokumentation, inte samtal
- Är reproducerbar för andra AI:er
- Är neutral och källkontrollerad

**OM AI INTE KAN LÄSA mötesprotokollet:**
```
"❌ Jag kan inte läsa mötesprotokollet från länken.

🔴 UTAN det kan jag inte presentera ordentligt!

Lösning: Copy-pasta innehållet här, så kan jag:
- Se vilka BESLUT som togs
- Se vilka ACTION ITEMS som gäller
- Förstå feedback från ledning
- Presentera baserat på överenskomst, inte bara git log

Väntar på mötesprotokollet..."
```

---

**SEDAN (efter VAD-VARFÖR-HUR-NÄR), visa AI visuella slides:**

```
AI: [Skapar visuell interaktiv slide-presentation]
   [Problem-slide → TÄNK SJÄLV paus → Lösning-slide]
   [Varje Problem-slide har pedagogisk brödtext]
   [Varje Lösning-slide visar konkreta exempel & resonemang]
   [Förklarar bransch-principer & varför vi gör det så]

Resultat: En presentation som TVINGAR studenterna att tänka
```

---

## 🎨 MED ARKITEKTUR-DIAGRAM (för visuella tänkare)

**Om du vill ha diagram tillsammans med slides, säg:**
```
Du: "Gör en PEDAGOGISK presentation med DIAGRAM över arkitektur"
```

**AI skapar då:**

1. **System-arkitektur diagram**
   ```
   Frontend (React)  ←→  Backend (Java)  ←→  Native (C++)
   ├─ LoginForm      ├─ API             ├─ Risk Calc
   ├─ Portfolio      ├─ Auth            ├─ FX Conv
   └─ Dashboard      └─ DB              └─ Backtest
   ```

2. **Sprint-flöde visuellt**
   ```
   VAD: Risk Metrics ──→ VARFÖR: CTO Deadline ──→ HUR: Pair Prog ──→ NÄR: Torsdag
   ```

3. **Risk-dashboard som bild**
   ```
   🟢 Frontend: On Track
   🔴 Backend: Critical  ← Risk Metrics
   🟠 Native: Slight Delay
   ```

4. **Team-ansvar diagram**
   ```
   Backend: Risk Metrics (PRIORITY)
   Frontend: Tests + API integration
   Native: Verify calculations + support Backend
   ```

**Varför diagram hjälper:**
✅ Visuell tänkare förstår arkitektur direkt
✅ Flöden blir tydliga (VAD → VARFÖR → HUR → NÄR)
✅ Risk-status läses på en gång (färger)
✅ Team-ansvar blir explicit
✅ Mer än bara text = djupare förståelse

**Hur presentationen fungerar:**

```
SLIDE 2: ⏰ PROBLEM - Deadlines
├─ Visar: CTO deadline 24 sep, risk-metrics bara 40% klara
├─ Brödtext: VAD är deadline? HUR jobbar vi? VARFÖR är det kritiskt?
└─ Fråga: "Vad skulle DU prioritera denna vecka?"

🧠 PAUS — Studenterna diskuterar/tänker själva (5 min)

SLIDE 2c: ✅ LÖSNING - Deadlines
├─ Visar: Förslag på prioritering
├─ Exempel: "Risk-metrics är KRITISK → allokooa 16h denna vecka"
├─ Resonemang: "Varför? Utan det missar vi CTO deadline"
└─ Bransch-princip: "Deadlines är om leveransprecision, inte perfekt kod"

---

SLIDE 3: 📈 PROBLEM - Metrics
├─ Visar: Lighthouse 78/100 (behövs 85+), test coverage 45% (behövs 70%)
└─ Fråga: "Vilka problem ser DU här? Hur skulle du lösa dem?"

🧠 PAUS — Studenterna tänker

SLIDE 3c: ✅ LÖSNING - Metrics
├─ Exempel: "Performance gap = 7 poäng. Lösning: Optimize LCP images"
├─ Kod-exempel: "Använd WebP format istället för PNG"
└─ Resultat: "Då når vi 85+ och är ready för kvaldemo"
```

**Presentation innehåller (INTERAKTIV LÄRSTIL):**

| # | Slide Type | Symbol | Content |
|---|-----------|--------|---------|
| 1 | Cover | 📊 | Status Sync - Vecka X |
| 2 | Problem | ⏰ | Deadlines: vad måste vara klart? |
| 2b | **TÄNK SJÄLV** 🧠 | — | *Pausera här — vad skulle DU prioritera?* |
| 2c | Solution | ✅ | Lösning: Prioritering + exempel |
| 3 | Problem | 📈 | Metrics: Vad säger siffrorna? |
| 3b | **TÄNK SJÄLV** 🧠 | — | *Pausera — vad är problemet här?* |
| 3c | Solution | ✅ | Lösning: Vad vi bör göra |
| 4 | Info | ✅ | Develop status (klart/pågår/ej startat) |
| 5 | Problem | 🔄 | Active branches: vilka är blocked? |
| 5b | **TÄNK SJÄLV** 🧠 | — | *Pausera — vilka är kritiska?* |
| 5c | Solution | ✅ | Lösning: Prioritering + nästa steg |
| 6 | Problem | 🚀 | PRs: vilka kan mergas? |
| 6b | **TÄNK SJÄLV** 🧠 | — | *Pausera — skulle DU merga denna?* |
| 6c | Solution | ✅ | Lösning: Merge decisions + varför |
| 7 | Info | ✨ | Nyligen startade branches |
| 8 | Problem | 🚫 | Blockers: vad hindrar oss? |
| 8b | **TÄNK SJÄLV** 🧠 | — | *Pausera — hur skulle DU lösa det?* |
| 8c | Solution | ✅ | Lösning: Förslag + implementation |
| 9 | Problem | ⚠️ | Gap: vad saknas? |
| 9b | **TÄNK SJÄLV** 🧠 | — | *Pausera — vilka är de kritiska gapen?* |
| 9c | Solution | ✅ | Lösning: Plan för att fylla gap |
| 10 | Info | ☑️ | Action items & decisions |
| 11 | Next | 📅 | Next steps & focus |

**Slide-design (SAMMA FÖR ALLA SLIDES) — NPF-OPTIMERAD + SNYGG & LEKFULL:**

```
LAYOUT-PRINCIPER (ADHD/Neurodiverse friendly):
├─ Luftig layout: 60-70% whitespace, max 30% text
├─ En STOR symbol/ikon i toppen (80-100px)
├─ Max 3-4 bullet points per slide
├─ Tydliga visuella separatörer (boxes, lines, borders)
├─ Färgkodning för prioritet (🔴🟡🟢)
├─ Typography med tydlig hierarki
└─ ALLTID ett DIAGRAM, BILD, eller VISUELL (inte bara text!)

TYPOGRAFI:
├─ Symbol/Ikon: 80-100px (första intryck)
├─ Rubrik: 36-48pt, bold, tydlig
├─ Bullets: 20-24pt, regular
├─ Pedagogisk brödtext: 14-16pt, muted
├─ Status/källa: 10-12pt, very muted
└─ Radavstånd: 1.6-1.8 (läsbar, inte tätt)

FÄRGKODNING:
├─ 🔴 Kritisk/Blocker/Danger — Röd (#E53E3E)
├─ 🟠 Varning/Behind schedule — Orange (#ED8936)
├─ 🟢 OK/On track — Grön (#48BB78)
├─ 🔵 Info/Neutral — Blå (#4299E1)
└─ 🟣 Lekfull accent — Lila (#9F7AEA) för highlights

VISUELLA ELEMENT (MÅSTE ingå):
├─ Progress bars (████░░░░ 60%) med avrundade hörn
├─ Diagram (boxes, arrows, timelines) med mjuka former
├─ Ikoner för varje punkt (🎯 ⚠️ ✅)
├─ Färgade boxes för varje sektion (avrundade)
├─ Tydliga separatörer mellan sektioner (───────)
└─ Snygga tabeller med färgade headers

🎨 SNYGGA TABELLER:
├─ Header: Färgad bakgrund (blå/lila) + vit text, bold
├─ Varje rad: Alterneras mellan vit + ljusgrå bakgrund
├─ Ikonkolumn: Centered icons (✅ 🟠 ❌)
├─ Siffror: Högerjusterade (alignment)
├─ Ramar: Mjuka skuggor istället för harda linjer
├─ Padding: Generöst utrymme mellan celler
└─ Typografi: Konsistent, läsbar font (sans-serif)

EXEMPEL TABELL (Snygg design):
┌─────────────────────────────────────────┐
│ 📊 ISSUE STATUS (Blå header, vit text) │
├─────────────────────────────────────────┤
│ # │ Issue             │ Status    │ %   │
├─────────────────────────────────────────┤
│ ✅│ Risk Metrics      │ Ready     │ 100%│
│ 🟠│ FX Converter      │ In prog   │ 60% │
│ ❌│ Rebalance Suggest │ Blocked   │ 20% │
└─────────────────────────────────────────┘
(Notera: varje rad har ljusgrå bakgrund, mjuk skugga)
```

**Kontrastrik & Tillgänglig:**
- ✅ Minst WCAG AA kontrast (4.5:1)
- ✅ Stöd för ljust & mörkt tema
- ✅ Inga uttryck som endast förlitar sig på färg
- ✅ Tydlig fokus-ordning

**KÄNSLA & TON:**
- ✅ Lekfull (ikoner, färger, mjuka former)
- ✅ Behaglig (mycket whitespace, mjuka övergångar)
- ✅ Lätt (inte tung eller formell)
- ✅ Professionell (men varm och tillgänglig)
- ✅ Inspirerande (färger uppmuntrar, inte skräcker)

---

## 📚 PEDAGOGISK BRÖDTEXT — VAD/HUR/VARFÖR

**Varje slide inkluderar en kort förklarande text:**

```
VAD?   — Vad är detta? (kort definition)
HUR?   — Hur jobbar vi med detta i branchen?
VARFÖR? — Varför är detta viktigt för projektet?
```

**Exempel: Slide 2 (Deadlines)**
```
┌─────────────────────────────────────────────────────┐
│                    ⏰ DEADLINES                      │
├─────────────────────────────────────────────────────┤
│                                                     │
│ 🔴 CTO Deadline (24 sep)                            │
│    Risk metrics: 40% done ❌                         │
│    FX converter: 30% done ❌                         │
│    Tests: 45% coverage (need 70%) ❌                │
│                                                     │
│ ───────────────────────────────────────────────     │
│                                                     │
│ 📖 VAD?                                             │
│ En deadline är en tidsgräns då ett arbete måste     │
│ levereras. Det är inte bara ett datum — det är ett  │
│ mål som hela teamet jobbar mot.                     │
│                                                     │
│ 🛠️  HUR?                                             │
│ Vi använder GitHub Project Board + SPRINT_TIMELINE  │
│ för att spåra deadlines. Vi läser denna vecka vad   │
│ som är klart vs vad som MÅSTE vara klart.           │
│                                                     │
│ 💡 VARFÖR?                                          │
│ CTO behöver se att vi förstår kundens behov. Om vi  │
│ missar denna deadline, visar vi att vi inte kan     │
│ leverera på tid — något viktigt i branchen.         │
│                                                     │
│ Denna vecka: Risk metrics är bakom (40% vs 100%).   │
│ Nästa vecka måste vi prioritera det här för att     │
│ klara CTO-deadline.                                 │
│                                                     │
└─────────────────────────────────────────────────────┘
```

**Exempel: Slide 5 (Active Branches)**
```
┌─────────────────────────────────────────────────────┐
│                  🔄 ACTIVE BRANCHES                 │
├─────────────────────────────────────────────────────┤
│                                                     │
│ feature/#52-risk-calculations (Backend)             │
│   Status: 40% done, BEHIND schedule                 │
│   Estimat: 16h total, redan använt: 12h             │
│   Kommer in i dev: DENNA VECKA (crítica!)           │
│                                                     │
│ ───────────────────────────────────────────────     │
│                                                     │
│ 📖 VAD?                                             │
│ En branch är en separat arbetslinje i Git där vi    │
│ utvecklar en feature utan att påverka main-koden.   │
│ Varje issue får sin egen branch.                    │
│                                                     │
│ 🛠️  HUR?                                             │
│ Vi skapar en branch: git checkout -b feature/#52    │
│ Vi jobbar där tills det är klart, sedan gör vi en   │
│ Pull Request för att merge tillbaka till develop.   │
│ Branch-status visas i GitHub Project Board.         │
│                                                     │
│ 💡 VARFÖR?                                          │
│ Branches skyddar main-koden. Om något går fel på    │
│ vår branch påverkas inte team-koden. Vi kan jobba   │
│ parallellt utan att trampa på varandra.             │
│                                                     │
│ ⚠️  BRANSCH-PRINCIP:                                │
│ Om en branch är BEHIND schedule (40% av 16h redan   │
│ använt) måste vi prioritera. Vi kan inte lägga mer  │
│ arbete på nya branches tills denna är klar.         │
│                                                     │
└─────────────────────────────────────────────────────┘
```

**Exempel på en slide (Deadlines):**
```
┌─────────────────────────────────────────────────┐
│         ⏰ DEADLINES & VÅ MÅSTE VARA KLART      │
├─────────────────────────────────────────────────┤
│                                                 │
│   🔴 CTO Deadline — 24 sep                      │
│      ├─ Risk metrics: 40% ✅ (MUST finish)     │
│      ├─ FX converter: 30% ✅ (MUST finish)     │
│      └─ Tests: 45% ❌ (target 70%)             │
│                                                 │
│   🟡 Kvaldemo — 15 okt                         │
│      ├─ UI polishing: On track ✅              │
│      └─ Real Avanza data: Pending ⏳           │
│                                                 │
│   🟢 Slutleverans — 4 nov                      │
│      └─ All customer feedback implemented ✅   │
│                                                 │
└─────────────────────────────────────────────────┘
```

---

## 🎓 LEARNING OUTCOMES — VAD SKA NI LÄRA ER?

**Denna presentation använder PROBLEM-TÄNK-LÖSNING modellen:**

1. **PROBLEM-slide** — Vi presenterar situationen
2. **TÄNK SJÄLV 🧠** — 5-10 min paus, ni diskuterar
3. **LÖSNING-slide** — Vi visar hur professionella gör det

**Varför denna modell?**
- ✅ Ni engageras aktivt (inte bara passiv lyssnare)
- ✅ Ni tränar på problem-solving (en bransch-skicklighet)
- ✅ Ni förstår VARFÖR vi gör det så (inte bara VAD)
- ✅ Ni jämför er egen tanke med professionell lösning (lärdom!)
- ✅ Presentationen blir mer engagerande

**Efter denna presentation ska ni kunna:**

### Deadlines (Slide 2)
- 📖 Förstå vad en deadline är (INTE bara ett datum)
- 🛠️ Veta hur vi spårar deadlines (GitHub + SPRINT_TIMELINE)
- 💡 Förstå varför deadlines är kritiska i branchen (leveransprecision)

### Active Branches (Slide 5)
- 📖 Förstå vad en Git branch är och varför de existerar
- 🛠️ Veta hur man läser branch-status från Project Board
- 💡 Förstå konsekvensen av "behind schedule" (andra kan inte börja sitt arbete)

### PRs Under Review (Slide 6)
- 📖 Förstå att en PR är en "förfrågan att merge" — inte bara kod
- 🛠️ Veta att PRs behöver reviews innan de mergas (kvalitetskontroll)
- 💡 Förstå att "merge decisions" är en TEAM-aktivitet, inte en individ-aktivitet

### Blockers & Solutions (Slide 8)
- 📖 Förstå vad en blocker är (något som hindrar arbete)
- 🛠️ Veta att VARJE blocker behöver en mitigation (lösningsplan)
- 💡 Förstå att "problem-solving" är en central bransch-skicklighet

### Gap Analysis (Slide 9)
- 📖 Förstå vad "gap" betyder (skillnad mellan målat och faktiskt)
- 🛠️ Veta hur man beräknar gap (målat - faktiskt)
- 💡 Förstå att gap-analys hjälper oss prioritera arbete rätt

---

## 🎬 Mötesschema & Kommandon

| Veckodag | Tid | Mötestyp | Kommando | Focus |
|----------|-----|----------|----------|-------|
| **Måndag** | 09:00 | Sprint Planning | "Förbered mandagsmötet" eller "Kör sprintplanering" | Nästa veckas prioritering |
| **Tisdag** | 13:00 | Status Sync | "Förbered tisdagsmötet" eller "Kör status sync" | Denna veckas progress + deadlines |
| **Torsdag** | 15:00 | Sprint Review | "Förbered torsdagsmötet" eller "Kör sprint review" | Vad blev klart? Feedback? |

**Möteskommandon för AI:**

```
TISDAG (Status Sync) ← Du är här:
Du: "Förbered FÖR tisdagsmötet" 
    (AI läser git log, GitHub, deadlines — presenterar struktur)

Du: "Kör status sync möte"
    (AI faciliterar mötet enligt agenda)

Du: "Presentation av status sync möte"
    (AI skapar visuell slide-presentation)
```

⚠️ **VIKTIGT:** AI avstämmer med PL innan möte:
```
AI: "Vilka punkter vill du fokusera på denna tisdag?"
PL: "Blockers på risk-calculations och FX-converter"
AI: [Fokuserar på dessa i mötet, läser relevant kod/branches]
```

**Vilken guide vill du läsa?**
- 👈 **Du är här:** MEETING_STATUS_SYNC.md (Tisdagsmötet)
- 📋 **Se även:** SPRINT_PLANNING.md (Mandagsmötet)
- 📊 **Se även:** SPRINT_REVIEW.md (Torsdagsmötet) - *kommer senare*

