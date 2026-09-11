# 🎯 SPRINTMÖTE — PRESENTATION GUIDE

**DETTA ÄR EN GUIDE FÖR MÖTESLEDAREN — INTE EN RAPPORT**

Denna guide visar **HUR man håller mötet snabbt och koncist**, inte vad man rapporterar från.

Mötet: **09:00-10:30 (90 minuter) — Fokuserad planering**

---

## 📊 ÖVERGRIPANDE TEAM STATUS (Innan Du Dyker in i detaljer)

**Visa detta FÖRST så alla förstår läget direkt:**

```
╔═══════════════════════════════════════════════════════════════╗
║                    🎯 SPRINT STATUS OVERVIEW                  ║
╠═══════════════════════════════════════════════════════════════╣
║                                                               ║
║  PROJEKTETS ÖVERGRIPANDE MÅL denna vecka:                    ║
║  ┌─────────────────────────────────────────────────────────┐ ║
║  │ ✅ Risk Metrics: 100% klar                              │ ║
║  │ ✅ FX Converter: 100% klar                              │ ║
║  │ ✅ Tests: 70%+ coverage                                 │ ║
║  │ ✅ Kärnflödet: Testbar end-to-end                       │ ║
║  └─────────────────────────────────────────────────────────┘ ║
║                                                               ║
║  DEADLINES:                                                  ║
║  ├─ 🔴 DENNA VECKA: Torsdag 15:00 (Sprint avslutas)          ║
║  ├─ 🟠 EXTERN: 24 september 16:00 (CTO-demo)                 ║
║  └─ 🟢 NÄSTA: 15 oktober (Kvaldemo för kund)                 ║
║                                                               ║
║  VÅR ÖVERGRIPANDE STATUS:                                    ║
║  ┌─────────────────────────────────────────────────────────┐ ║
║  │ 🟢 GRÖN — Vi ligger i fas                               │ ║
║  │    Tidsbudget OK, alla team på track                     │ ║
║  │                                                          │ ║
║  │ 🟠 ORANGE — Vi ligger lite efter                         │ ║
║  │    Risk Metrics är 40%, behöver acceleration             │ ║
║  │                                                          │ ║
║  │ 🔴 RÖD — KRITISK situation                              │ ║
║  │    Vi kommer missa deadline, omedelbar åtgärd behövs     │ ║
║  └─────────────────────────────────────────────────────────┘ ║
║                                                               ║
║  DETTA MÖTE:                                                 ║
║  → Vi planerar denna veckas arbete                           ║
║  → Vi säkerställer vi når målet torsdag 15:00                ║
║  → Vi identifierar risker & löser blockers                   ║
║  → Vi är klara på 90 minuter                                 ║
║                                                               ║
╚═══════════════════════════════════════════════════════════════╝
```

---

## 📊 PRESENTATIONEN: ÖVERGRIPANDE + TEAM-LEVEL (BÅDA TILLSAMMANS!)

**DENNA PRESENTATION visas I MÖTET och visar BÅDA nivåerna:**

### DEL 1: ÖVERGRIPANDE PROJECT STATUS

```
╔═══════════════════════════════════════════════════════════════╗
║                  🎯 PROJECT STATUS DENNA VECKA                ║
╠═══════════════════════════════════════════════════════════════╣
║                                                               ║
║  ÖVERGRIPANDEMÅLsättning:                                     ║
║  Risk Metrics ✅ | FX Converter ✅ | Tests (70%+) ✅          ║
║                                                               ║
║  ÖVERGRIPANDE STATUS:      🟢 GRÖN (i fas)                   ║
║  ├─ Tidsbudget: OK                                            ║
║  ├─ Risk: Låg                                                 ║
║  └─ Alla team på track                                        ║
║                                                               ║
║  DEADLINES:                                                  ║
║  ├─ Torsdag 15:00 (Sprint avslutas)                           ║
║  ├─ 24 sep 16:00 (CTO-demo)                                   ║
║  └─ 15 oktober (Kvaldemo)                                     ║
║                                                               ║
║  ÅTGÄRDSFÖRSLAG (om kritisk):                                 ║
║  ├─ Pair programming på blockers                              ║
║  ├─ Resource move mellan team                                 ║
║  ├─ Scope cut (prioritera MÅSTE-ha)                           ║
║  └─ Daily check-in (övervakning)                              ║
║                                                               ║
╚═══════════════════════════════════════════════════════════════╝
```

### DEL 2: TEAM-LEVEL STATUS (Färgkodade Borders - VISAR INTE BORT!)

```
🟢 FRONTEND TEAM — ON TRACK
╔═══════════════════════════════════════════════════════════════╗
║  Frontend Team Status (Anna, Marco)                           ║
║                                                               ║
║  Progress denna vecka:  ████████░░  80%                       ║
║  Issues completed:      4 / 5                                 ║
║  Tests written:         ✅ All passing                        ║
║  Blockers:              ❌ None                               ║
║                                                               ║
║  🟢 Status: ON TRACK                                          ║
║  │  ✅ Target Allocation component working                    ║
║  │  ✅ API integration done                                   ║
║  │  ⏳ UI refinement (not blocking)                           ║
║  │                                                            ║
║  └─ Kan vi hjälpa Backend? Vill ni jobba på något annat?      ║
╚═══════════════════════════════════════════════════════════════╝

🟠 BACKEND TEAM — SLIGHT DELAY (RECOVERABLE)
╔═══════════════════════════════════════════════════════════════╗
║  Backend Team Status (Marco, Jana)                            ║
║                                                               ║
║  Progress denna vecka:  ██████░░░░  60%                       ║
║  Issues completed:      2 / 4                                 ║
║  Tests written:         ✅ 65% coverage                       ║
║  Blockers:              ⚠️  Swagger docs (1 dag)               ║
║                                                               ║
║  🟠 Status: SLIGHT DELAY (recoverable denna vecka)            ║
║  │  ✅ Risk Metrics API (80% done, klar torsdag)              ║
║  │  ⚠️  FX Converter (30%, väntar på swagger)                 ║
║  │  ❓ Tests (väntar på API klara)                            ║
║  │                                                            ║
║  └─ Åtgärdsförslag:                                           ║
║     • Pair programming Backend+Native idag 14:00              ║
║     • Swagger docs skrivs direkt (ej vänta)                   ║
║     • Resultat: Back on track torsdag                         ║
╚═══════════════════════════════════════════════════════════════╝

🔴 NATIVE TEAM — CRITICAL (OMEDELBAR ÅTGÄRD)
╔═══════════════════════════════════════════════════════════════╗
║  Native Team Status (Kiran)                                   ║
║                                                               ║
║  Progress denna vecka:  ████░░░░░░  40%                       ║
║  Issues completed:      1 / 3                                 ║
║  Tests written:         ⚠️  45% coverage (target 70%)          ║
║  Blockers:              🔴 CRITICAL — Calculation spec         ║
║                                                               ║
║  🔴 Status: CRITICAL — BLOCKER RISK                           ║
║  │  ✅ Volatility calculation (70% done)                      ║
║  │  ❌ Sharpe ratio calc (STARTED — waiting spec)             ║
║  │  ❌ Test coverage low (45% vs 70% target)                  ║
║  │                                                            ║
║  └─ 🚨 OMEDELBAR ÅTGÄRD (SAMMA DAG):                         ║
║     • Backend + Native = pair programming 14:00 idag           ║
║     • Skriva spec tillsammans (1 timme)                        ║
║     • Kiran implementerar därefter (3 timmar)                  ║
║     • Resultat: Sharpe ratio klar samma dag                   ║
║     • Frontend + Native: Test-writing session onsdag 10:00     ║
║                                                               ║
║     "Kiran behöver OMEDELBAR support idag, inte vänta"        ║
╚═══════════════════════════════════════════════════════════════╝

SAMMANFATTNING:
🟢 Frontend: Kan stödja andra
🟠 Backend: Recoverable denna vecka (actions taken idag)
🔴 Native: OMEDELBAR support behövs IDAG (14:00 pair prog)
```

---

## ⏱️ MÖTESTRUKTUREN (90 MINUTER)

**Följ denna struktur VARJE GÅNG — det är en återkommande mall.**

```
09:00-09:15 (15 min) — ALL-HANDS: KONTEXT
   Facilitator säger:
   ├─ "Här är vad som blev gjort förra veckan"
   ├─ "Här är denna veckas mål"
   ├─ "Här är vad vi behöver fokusera på"
   └─ "Frågor innan vi går till breakouts?"
   
   (INGET om källdokument, inget om "mötesprotokollet säger")
   (BARA kontext för denna veckan)

09:15-09:20 (5 min) — TEAM BREAKOUT INTRO
   Facilitator säger:
   ├─ "Vi tar 5 minuter eget team-samtal nu"
   ├─ "Gå till er rum med er lead"
   ├─ "Diskutera: Vad behöver vi? Vilka blockers?"
   └─ "Vi ses om 10 minuter"

09:20-09:25 (5 min) — TEAM BREAKOUTS (parallelt)
   🔴 Backend rum:        "Vad behöver vi denna vecka?"
   🔵 Frontend rum:       "Blockers? Support-behov?"
   🟢 Native rum:         "Spec klar? Vad behövs?"
   
   (Varje team löser sitt eget snabbt)

09:25-09:30 (5 min) — KAFFEPAUS
   ├─ Naturlig paus från mötet
   ├─ Peer-samtal möjlig: "Hur går det för dig?"
   └─ Energi för andra hälften

09:30-10:00 (30 min) — PRIORITERING & SCOPE
   Facilitator frågar:
   ├─ "Vilka är MÅSTE-ha denna vecka?"
   ├─ "Vilka är NICE-TO-HAVE?"
   ├─ "Kan vi göra allt? Eller behöver vi scope cut?"
   ├─ "Vem är huvudansvarig för vad?"
   └─ Uppdatera GitHub Project Board LIVE

10:00-10:25 (25 min) — ESTIMERING & RISK
   Facilitator frågor:
   ├─ "Hur många timmar per issue?"
   ├─ "Passar det inom vår kapacitet?"
   ├─ "Vilka blockers är kända? Hur löser vi dem?"
   ├─ "Vilka är framgångskriterier?"
   └─ "Vilka är riskerna och hur mitigerar vi?"

10:25-10:30 (5 min) — AVSLUT
   Facilitator bekräftar:
   ├─ "Alla vet sitt jobb?"
   ├─ "Deadlines klara? (Torsdag 15:00)"
   ├─ "Blockers identifierade?"
   └─ "Vi är redo. Lycka till denna vecka!"

NOTERA: Ingen rapport, ingen källcitat, bara mötesfasilitering!
```

---

## 🎯 VAD PRESENTATIONEN VISAR (BÅDA NIVÅERNA — INGENTING FÖRSVINNER!)

**Presentationen visar ALLTID två nivåer tillsammans:**

### NIVÅ 1: ÖVERGRIPANDE PROJECT STATUS (Början av möte)
```
🟢🟠🔴 Grön/Orange/Röd status för HELA projektet
├─ Vad är målet denna vecka? (Risk Metrics, FX, Tests)
├─ När ska det vara klart? (Torsdag 15:00 + 24 sep)
├─ Vilka deadlines närmar sig? (Kvaldemo 15 okt)
└─ Åtgärdsförslag om kritisk: Pair prog? Resource move? Scope cut?
```

### NIVÅ 2: TEAM-LEVEL STATUS MED FÄRGKODADE BORDERS (Samma möte)

**INGENTING försvinner! Varje team visas med sin färgkodade border:**

```
🟢 FRONTEND TEAM — ON TRACK (grön border)
   ├─ Progress: 80%
   ├─ Vad är klart? (API integration done)
   ├─ Vad pågår? (UI refinement)
   └─ Kan vi hjälpa andra team?

🟠 BACKEND TEAM — SLIGHT DELAY (orange border)
   ├─ Progress: 60%
   ├─ Vad är klart? (Risk Metrics 80%)
   ├─ Vad är bakom? (FX Converter, waiting for spec)
   └─ Konkreta stödinsatser: Pair prog idag 14:00!

🔴 NATIVE TEAM — CRITICAL (röd border)
   ├─ Progress: 40%
   ├─ Blockers: Calculation spec missing
   └─ OMEDELBAR ÅTGÄRD: Backend+Native pair 14:00 IDAG!
```

**BÅDA nivåerna visas tillsammans — INGENTING försvinner!**

---

## ✅ MÖTESFACILITÖRENS CHECKLISTA

**Innan möte börjar (10 min före):**
- [ ] Vet jag denna veckas mål?
- [ ] Vet jag deadlines denna vecka + kommande?
- [ ] Vet jag vilka team som ligger bakom?
- [ ] Är GitHub Project Board uppdaterad med förra veckan?
- [ ] Är breakout-rum bokat (eller online-breakout-länk klar)?

**Under möte:**
- [ ] Starta 09:00 SHARP (inte 09:05)
- [ ] Håll all-hands fokuserad (ingen detaljdiskussion)
- [ ] Ge team-breakouts exakt 5 minuter
- [ ] Notera vad teamen sa från breakouts
- [ ] Uppdatera GitHub Project Board LIVE
- [ ] Sluta 10:30 (inte 10:40)

**Efter möte:**
- [ ] Är GitHub Project Board uppdaterad?
- [ ] Vet varje person sitt jobb denna vecka?
- [ ] Är blockers dokumenterade?
- [ ] Är nästa möte bokad (nästa måndag 09:00)?

---

## 🎨 PRESENTATION = STRUKTUR, INTE INNEHÅL

**DENNA GUIDE visas INTE till teamet.**

**Denna guide hjälper FACILITATÖREN att hålla mötet:**
- ✅ Snabbt (90 minuter, punkt)
- ✅ Fokuserat (en struktur varje gång)
- ✅ Effektivt (inget gödslay, bara beslut)
- ✅ Igenkännligt (samma flöde varje vecka)

**Presentationen visar:**
- ✅ Övergripande team-status (färger)
- ✅ Mål denna vecka (tydligt)
- ✅ Deadlines denna vecka + senare (tydligt)
- ✅ Pedagogisk förklaring (varför det spelar roll)
- ✅ Team-level bedömning (grön/orange/röd)

**Presentationen visar INTE:**
- ❌ Källdokument-referenser
- ❌ Mötesprotokolls-citat
- ❌ GitHub-link-hemsidor
- ❌ Lång prosa
- ❌ Mycket text

**Det är en GUIDE för snabbt möte, inte en RAPPORT med källor.**
