# 📝 Sprint Meeting Protocol Template

**FÖR SEKRETERARE:** Använd denna mall under mötet. Facilitator presenterar → Du fyller i här.

**Datum:** [Veckodag, datum]  
**Tid:** 09:00-10:30  
**Närvaro:** [Lista namn]  
**Inställningar:** [Om någon var inställd]

---

## 🎯 SYFTE MED MÖTET (Facilitator säger)

Vad är huvudsyftet denna vecka?

```
Exempel: "Vi planerar denna veckas sprint. Vi måste fokusera på 
Risk Metrics (backend complete), FX Converter (frontend start), 
och få test-coverage till 70%."
```

**Skriv in:**
- [ ] Huvudfokus denna vecka
- [ ] Vilka stories/features vi prioriterar
- [ ] Kritiska deadlines (torsdag 15:00 sprint end)

---

## 📊 STATUS SEDAN FÖRRA MÖTE

**Facilitator läser från:** Git log förra veckan + GitHub Project Board

```
Exempel: "Förra veckan slutförde vi Portfolio Dashboard och 
Login-flödet. Risk Metrics är 60% klar (Marco arbetar vidare). 
Två issues blev blocked — vi löste dem under veckan."
```

**Skriv in:**
- [ ] Vilka issues blev DONE förra veckan
- [ ] Vilka issues är IN PROGRESS denna vecka
- [ ] Vilka issues är BLOCKED och varför

---

## 🟢🟠🔴 ÖVERGRIPANDE PROJECT STATUS (DEL 1 av presentation)

Facilitator visar slide med övergripande status. Du fyller in medan hen presenterar.

### ÖVERGRIPANDE MÅL denna vecka:
```
Skriv in varje goal med #issue-nummer och assignee:
- Risk Metrics (#42 - Marco): [% progress]
- FX Converter (#45 - Jana): [% progress]  
- Tests (#48 - Anna): [% progress / target]
- Kärnflödet (#51 - Kiran): [status]
```

### ÖVERGRIPANDE STATUS:

```
Välj EN:
🟢 GRÖN — Vi ligger i fas
   Tidsbudget OK, alla team på track
   
🟠 ORANGE — Vi ligger lite efter  
   [Vilka team ligger efter? Varför?]
   
🔴 RÖD — KRITISK situation
   [Vad kan gå fel? Vad behöver vi göra IDAG?]
```

### DEADLINES:
```
- Torsdag 15:00 (Sprint end)
- 24 sep 16:00 (CTO-demo)
- 15 oktober (Kvaldemo för kund)
```

---

## 👥 TEAM-LEVEL STATUS (DEL 2 av presentation)

Facilitator presenterar varje team. Du fyller in per team medan hen presenterar.

### 🟢 FRONTEND TEAM — ON TRACK / SLIGHT DELAY / CRITICAL

**Progress:**  
```
Exempel: 80% (████████░░)
- Issues completed: 4 / 5
- Tests passing: ✅ All passing / ⚠️ X failing
```

**Vad är klart denna vecka:**
```
- [Issue #39 - Anna] Target Allocation component ✅
- [Issue #43 - Marco] API integration done ✅
```

**Vad pågår:**
```
- [Issue #47 - Anna] UI refinement (not blocking) ⏳
```

**Blockers eller risker:**
```
❌ None
- eller -
⚠️ [Beskrivning av blocker]
```

**Åtgärdsförslag (om orange/red):**
```
- Pair programming med Backend idag 14:00
- [Annat stöd behövt?]
```

---

### 🟠 BACKEND TEAM — ON TRACK / SLIGHT DELAY / CRITICAL

**Progress:**  
```
Exempel: 60% (██████░░░░)
- Issues completed: 2 / 4
- Tests passing: ✅ 65% coverage
```

**Vad är klart denna vecka:**
```
- [Issue #42 - Marco] Risk Metrics API (80% done, klar torsdag) ✅
```

**Vad är bakom plan:**
```
- [Issue #45 - Jana] FX Converter (30%, väntar på swagger)
```

**Blockers:**
```
⚠️ Swagger spec unclear (needs clarification)
```

**Åtgärdsförslag (om orange/red):**
```
- Pair programming Backend+Frontend idag 14:00
- Swagger docs skrivs direkt (not wait)
- Expected: Back on track torsdag
```

---

### 🔴 NATIVE TEAM — ON TRACK / SLIGHT DELAY / CRITICAL

**Progress:**  
```
Exempel: 40% (████░░░░░░)
- Issues completed: 1 / 3
- Tests passing: ⚠️ 45% coverage (target 70%)
```

**Vad är klart denna vecka:**
```
- [Issue #50 - Kiran] Volatility calculation (70% done) ✅
```

**Vad är blockat:**
```
- [Issue #51 - Kiran] Sharpe ratio calc (WAITING — spec missing) ❌
- [Issue #52 - Kiran] Test coverage (45% vs 70% target) ❌
```

**Kritiska blockers:**
```
🔴 CALCULATION SPEC IS MISSING
   → Cannot start Sharpe ratio implementation
   → Decision needed: Use placeholder or wait for spec?
```

**OMEDELBAR ÅTGÄRD BEHÖVS:**
```
- Backend + Native pair programming IDAG 14:00
- Spec written together (1 hour)
- Kiran implements after (3 hours)
- Target: Sharpe ratio complete SAME DAY

- Frontend + Native: Test writing session wed 10:00
```

---

## 🏗️ TEKNISKA BESLUT DENNA VECKA

**Skriv in varje beslut medan det diskuteras:**

```
Exempel:

BESLUT 1: FX Converter API Design
- Vi returnerar aggregated rates från /api/portfolio/metrics
- Inte separate endpoint per rate (decision: slower, many calls)
- Vem beslutade: Marco + Anna
- Varför: Enkel för frontend, backend kan casha aggregation

BESLUT 2: Error Handling Pattern
- Vi använder custom error types istället för try-catch
- Vem beslutade: Kiran + Marco
- Varför: Bättre type safety, easier testing
```

---

## 🔗 BEROENDEN MELLAN TEAMS

**Vilka teams väntar på varandra?**

```
Exempel:
- Frontend väntar på: Backend API contract för /api/portfolio/metrics
  → Status: Contract documented, ready for frontend to use
  → Risk: Backend might change response shape (low risk)
  
- Native väntar på: Calculation spec from Backend
  → Status: NOT READY YET (this is the blocker!)
  → Action: Backend decides on spec approach
  → Timeline: Must be done today (14:00 pair session)
  
- All väntar på: CTO feedback (24 sep, 16:00)
  → Status: Not yet, but planning starts this week
```

---

## ⚠️ PROBLEM / BLOCKERS (Sammanfattning)

**Vilka är de KRITISKA blockers denna vecka?**

```
🔴 KRITISK:
- Native blocked on Sharpe ratio spec (löses idag 14:00)
- Action: Backend + Native pair programming IDAG

🟠 MEDIUM:
- Backend Swagger spec unclear (impacts FX Converter testing)
- Action: Clarify during Backend+Frontend pair prog
- Timeline: Resolved today

🟢 LOW:
- Frontend needs UI polish (not blocking)
```

---

## 📋 ARBETSUPPGIFTER (Issues som startas denna vecka)

**Vilka issues startar vi DENNA VECKA?**

```
Från Sprint Planning, listan på issues:

FRONTEND:
- [ ] #47: UI Refinement - Target Allocation (Anna, 1 day) — START TUE
- [ ] #53: Error handling for FX conversions (Marco, 1 day) — START WED

BACKEND:
- [ ] #42: Risk Metrics API (Marco, 2 days) — CONTINUE, finish THU
- [ ] #45: FX Converter (Jana, 2 days) — START TUE (after Swagger)
- [ ] #54: Optimize database query (Jan, 1 day) — START WED

NATIVE:
- [ ] #51: Sharpe ratio implementation (Kiran, 2 days) — START MON 14:00 (after spec)
- [ ] #52: Test coverage (Kiran, 1 day) — START WED

Kapacitet denna vecka: [Total hours vs available]
Risk: ⚠️ Capacity tight if spec delayed beyond 14:00
```

---

## 🔓 ÖPPNA FRÅGOR

**Vilka frågor fanns eller uppstod under mötet?**

```
Exempel:
- Q: Vad gör vi om Sharpe spec inte är klar 14:00?
  A: Scope cut FX Converter, fokusera på core Risk Metrics

- Q: Behöver vi polera UI innan CTO-demo?
  A: Nej, functional är viktigare än pretty

- Q: Vilka tests är kritiska att ha för CTO-demo?
  A: E2E för kärnflödet (portfolio view → back-test)
```

---

## 🚀 NÄSTA STEG (Innan mötet slutar)

**Vad händer DIREKT efter mötet?**

```
- [ ] Alla går hem med sitt jobb tydligt definierat
- [ ] GitHub Project Board är uppdaterat med veckovisa issues
- [ ] Pair programming sessions är bokat:
  - Backend + Frontend: TIS 14:00 (for Swagger clarity)
  - Backend + Native: MON 14:00 (for Sharpe spec)
  - Frontend + Native: WED 10:00 (test writing)

- [ ] Blocker owners know next actions:
  - Backend: Finalize Sharpe spec by 14:00 today
  - Native: Ready to dev after 14:00 today

- [ ] Risk Dashboard uppdaterad
- [ ] Mötes-protokollet är i Google Docs (sparad)
```

---

## 📋 INFÖR NÄSTA MÖTE SKA FÖLJANDE VARA GJORT

**Vad måste vara klart innan TIS 13:00 status-möte?**

```
Deadlines för denna vecka:

MON 14:00:
- [ ] Sharpe ratio spec documented
- [ ] Backend + Native pair prog done

TIS 09:00:
- [ ] All issues started on GitHub Project
- [ ] Swagger docs drafted (Backend)

TUE 14:00:
- [ ] Backend + Frontend pair prog (Swagger clarity)
- [ ] Risk Metrics API 80% done

WED 09:00:
- [ ] FX Converter logic complete (Backend)
- [ ] Risk Metrics 100% tested

THU 15:00:
- [ ] ALL SPRINT GOALS DONE
- [ ] No Friday coding (Friday = review + rest)
```

---

## ✅ SAMMANFATTNING (Facilitator läser upp)

**Kort överblick av vad vi bestämde:**

```
Denna vecka fokus:
✅ Risk Metrics → DONE by Thursday
✅ FX Converter → Started, target DONE by Friday
✅ Tests → 70% coverage target
✅ Kärnflödet → End-to-end testbar

Kritiska actions denna vecka:
🔴 IDAG 14:00: Sharpe spec session (Backend + Native)
🔴 IDAG 14:00: Swagger clarity session (Backend + Frontend)

Status gå in:
🟢 Overall: ON TRACK (if spec done today)
🟠 Backend: SLIGHT DELAY (recoverable)
🔴 Native: BLOCKED (unblocks at 14:00)

Nästa möte: TIS 13:00 (Status sync)
Deadline: THU 15:00 (Sprint end)
No Friday coding!
```

---

## 📅 NÄSTA MÖTE

**Dag:** Tisdag  
**Tid:** 13:00-13:45  
**Syfte:** Mid-week status sync + blockers check  
**Förberedelse:** Git log denna vecka + GitHub Project updates

---

**Mötes-protokoll slutfört av:** [Namn på sekreterare]  
**Datum:** [Datum]  
**Länk till Google Docs:** [Länk här]
