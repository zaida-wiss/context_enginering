# 📊 Status Sync Meeting — Veckovisa Alignments

**Syfte:** Se aktuell status mot deadlines, vad behöver vara klart, och impact av kommande PRs.
**Publik:** HELA TEAMET (Backend, Frontend, Native/Systemutvecklare)

**Frekvens:** Varje vecka (tisdag eller onsdag)  
**Längd:** 45 min  
**Facilitator:** AI (läser git, GitHub, deadlines, och presenterar struktur)
**Beslut-fattar:** Produktledare + tech leads

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

## 🎨 SLIDE PRESENTATION FORMAT

**Vill du ha mötet som visuell presentation istället för text?**

**Kommando för AI:**
```
Du: "Gör en presentation av denna veckas status sync möte"
AI: [Skapar visuell slide-presentation, 1 slide per sektion]
```

**Presentation innehåller:**
- Slide 1: Cover slide (Status Sync - Vecka X)
- Slide 2: Deadlines & vad som måste vara klart
- Slide 3: Performance Metrics (Lighthouse, coverage %)
- Slide 4: Develop status (✅ klart, 🔄 pågår, ❌ inte startat)
- Slide 5: Active branches (prioriterad ordning + blockers)
- Slide 6: PRs under review (merge decisions)
- Slide 7: Nyligen startade (vad förbättrar de)
- Slide 8: BLOCKERS & lösningsförslag
- Slide 9: Gap analysis mot deadlines
- Slide 10: Action items & decisions
- Slide 11: Next steps

**Slide-design:**
- ✅ Luftig layout (mycket whitespace)
- ✅ Symboler/ikoner för varje punkt (✅ ❌ 🔴 🟡 🟢 ⏰)
- ✅ En huvud-punkt per slide (max 3-5 bullet points)
- ✅ Färger för prioriteter (röd=kritisk, gul=varning, grön=ok)
- ✅ Tydlig typografi (stor rubrik, läsbar text)
- ✅ Kontrastrik design (ljust/mörkt tema)

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

## 🎬 Mötesschema

| Veckodag | Tid | Mötestyp | Facilitator | Focus |
|----------|-----|----------|-------------|-------|
| Tisdag | 13:00 | Status Sync | AI | Denna veckas progress + deadlines |
| Torsdag | 15:00 | Sprint Review | AI | Vad blev klart? Vad learned vi? |
| Måndag | 09:00 | Sprint Planning | AI | Nästa veckas prioritering |

