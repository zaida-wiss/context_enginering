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

## 🎯 VAD PRESENTATIONEN VISAR (INGET ANNAT!)

**Visa BARA dessa två saker:**

### 1. ÖVERGRIPANDE STATUS (början av möte)
```
Grön/Orange/Röd status för HELA projektet
├─ Vad är målet denna vecka?
├─ När ska det vara klart? (Torsdag 15:00)
├─ Vilka andra deadlines närmar sig?
└─ Pedagogisk förklaring: Varför är detta viktigt?
```

### 2. TEAM-LEVEL STATUS (under mötet)
```
🟢 Frontend Team: 80% progress — On track
   ├─ Vad är klart?
   ├─ Vad pågår?
   └─ Behövs hjälp?

🟠 Backend Team: 60% progress — Slight delay
   ├─ Vad är klart?
   ├─ Vad är bakom?
   └─ Konkreta stödinsatser? (Pair prog? Resource move?)

🔴 Native Team: 40% progress — CRITICAL
   ├─ Vad är klart?
   ├─ Blockers?
   └─ OMEDELBAR ÅTGÄRD BEHÖVS (vem hjälper?)
```

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
