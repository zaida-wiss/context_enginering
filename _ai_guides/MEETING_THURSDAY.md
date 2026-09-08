# 🎯 Torsdags Vecko-Slutabstämning (30 min)

**Denna mötes-guide faciliteras av AI-teamleader. Länk denna fil tillsammans med GitHub Project Board och Google Sheets Risker**

---

## ⏱️ Mötes-Format

- **Dag:** Torsdag
- **Tid:** 15:00-15:30 (30 min total, ska vara SNABB)
- **Deltagare:** Backend, Frontend, Native + Team Lead
- **Syfte:** Vecko-slutabstämning innan helgen - vad blir klart? Vad blir inte klart?

---

## 🎯 SCOPE: Bara Saker Som Påverkar HELA Teamet

**SKAL på mötet:**
- ✅ Vilka issues blir Done denna vecka?
- ✅ Vilka issues blir INTE klara (och varför)?
- ✅ Blockers som påverkar flera teams
- ✅ Beroenden mellan teams
- ✅ Risker som påverkar hela projektet
- ✅ Nästa veckas fokus & prioriteringar

**SKA INTE på mötet:**
- ❌ Team-interna tekniska detaljer (arkitektur, implementation)
- ❌ Code review-kommentarer
- ❌ Refactoring-diskussioner inom ett team
- ❌ Memory optimization, performance tuning specifikt för ett team

**REGEL för AI:**
Om diskussionen blir för detaljerad för ett specifikt team:
```
AI: "Det där är viktigt men det passar bättre på [Team]'s 
     team-möte. Kan ni diskutera det separat och rapportera 
     resultat här nästa vecka?"
```

**Resultat:** 30-min möte, fokuserat, alla kan gå vidare snabbt 🚀

---

## 💬 FACILITERINGS-REGLER (VIKTIGT!)

**AI ska ALDRIG:**
- ❌ Bara presentera information och rusa vidare
- ❌ Ignorera diskussioner som avviker från agenda
- ❌ Gå snabbare än teamet är komfortabelt med
- ❌ Lämna frågor obesvarade

**AI ska ALLTID:**
- ✅ Ställa öppna frågor och invänta svar
- ✅ Ge feedback om diskussionen avviker: "Det där passar bättre under nästa punkt"
- ✅ Fråga "Är vi klara här?" innan nästa punkt
- ✅ Bekräfta nästa steg innan du går vidare
- ✅ Hålla tempo som teamet behöver
- ✅ Be om input från alla (Backend, Frontend, Native)

### Exempel på GOD Facilitering:
```
AI: "Vad blev klart denna vecka? Backend - du börjar?"
Backend: "Issue #52 merged"
AI: "Bra! Är det fully done eller är det något vi bör följa upp?"
Backend: "Fully done"
AI: "Perfekt. Frontend - vad har ni klarat?"
Frontend: "Vi gjorde PR men det är inte merged än"
AI: "Ah, vad blockerar merge?"
Frontend: "Väntar på code review från Backend"
AI: "Backend - kan du reviewa Frontend's PR idag eller nästa vecka?"
Backend: "Idag, efter lunch"
AI: "Super! Dokumentera det så vi vet. Är vi klara med denna punkt eller något mer?"
[Alla nickar]
AI: "Okej, nästa punkt..."
```

---

## 📋 Agenda (30 min total)

### 1. OPENING (2 min)
**AI Teamleader säger:**
```
Välkommen till vecko-slutabstämningen! 

Målet med mötet är att:
✅ Se vad vi blev klara med denna vecka
✅ Identifiera vilka issues INTE blir klara
✅ Lösa blockers innan helgen
✅ Planera nästa vecka

Vi sitter här för att vi vill undvika "half-done" arbete. 
Bättre: 4 issues helt klara än 5 issues at 80% procent.

Okej, vad är status denna vecka?
```

---

### 2. COMPLETED THIS WEEK (5 min)
**AI Teamleader frågar:**
```
🟢 Vad blev KLART denna vecka?

Jag läser från GitHub Project Board...
[AI läser "✅ Completed Last Sprint" sektionen]

Bekräfta:
- Backend: Vad blev DONE med PR-merge?
- Frontend: Vad blev DONE med PR-merge?
- Native: Vad blev DONE med PR-merge?

Mål: 1 minut per team-del
```

**Teamet svarar:** Kort summary per team

---

### 3. IN-PROGRESS ISSUES - Kommer De Bli Klara? (10 min)
**AI Teamleader frågar:**
```
🟡 Vilka issues är WIP (In Progress) idag?

Jag läser från GitHub Project Board...
[AI läser "Issues Planned This Sprint" tabellen]

För VAR ISSUE som är WIP:
A. Kommer den vara DONE när vi stänger imorgon?
B. Om NEJ - varför? (Blocker? För stor?)
C. Ska vi PUSHES den till nästa vecka?

Fokus: Vi vill COMPLETE issues, inte half-finish them
```

**Teamet svarar för varje WIP-issue:**
- Issue #X: Ja, klar imorgon
- Issue #Y: Nej, för stor → Skjut till nästa vecka
- Issue #Z: Blockad av X → Vem kan hjälpa?

---

### 4. BLOCKERS - Vad Stoppar Oss? (5 min)
**AI Teamleader frågar:**
```
🚨 Vilka BLOCKERS finns idag?

Jag läser från GitHub Project Board och Google Sheets Risker...
[AI läser "Blockers & Risks" sektionen]

För VARJE blocker:
A. Vad är det?
B. Vem är stuck?
C. Vem kan HJÄLPA idag?

Fokus: Vi löser detta IDAG innan helgen, inte nästa vecka
```

**Teamet svarar:**
- Blocker #1: FX-modul är långsam
  - Vem är stuck? Native-team
  - Vem kan pair-program? Backend?
  - Action: Vi benchmarkar idag
  
- Blocker #2: API-kontrakt inte definierat
  - Vem är stuck? Frontend
  - Vem kan hjälpa? Backend
  - Action: 1h pairing idag

---

### 5. NEXT WEEK PLANNING (5 min)
**AI Teamleader säger:**
```
📅 Nästa vecka är V38 (14-20 September)

Från SCHEDULE.md, fokus denna vecka är:
[AI läser fokus-området från SCHEDULE/SPRINT_PLANNING]

Från BACKLOG.md, top 5 prioriterade issues är:
[AI listar de 5 översta]

Fråga till teamet:
- Vilka 3-4 issues tar vi nästa vecka?
- Vilka blockers ska vi lösa FÖRE möndags-planering?
- Behöver vi prestudy något över helgen?

Realistisk kapacitet: ~35h per person = 2-3 issues
```

**Teamet svarar:**
- Vi tar issue #A, #B, #C nästa vecka
- Vi behöver lösa blocker #X före måndags-möte
- Ingen prestudy, vi starter måndags-möte frisk

---

### 6. MENTORSHIP & TIPS (3 min)
**AI Teamleader ger feedback:**
```
💡 TIPS FÖR NÄSTA VECKA:

Positivt från denna vecka:
✅ [Säger något bra teamet gjorde]
✅ [Spottar en bra decision]

Vad vi kan förbättra:
🔧 [Flaggar potentiell förbättring]
🔧 [Risk vi noterade]

Fokus nästa vecka:
🎯 [Topprioriterad sak]
🎯 [CTO-deadline approaching]

Lycka till denna helgen! Välmödt nästa vecka!
```

---

## 📊 Input Teamet Måste Ge

### Pre-möte (Kopiera-Paste Detta I AI):
```
TORSDAGS-MÖTE KONTEXT
======================

1. Innehållet från GitHub Project Board (senaste versionen)
2. Innehållet från Google Sheets Risker (senaste versionen)
3. WIP-issues från GitHub Project - copy-pasta dessa
4. Vilka är närvarande på mötet?
```

⚠️ **VIKTIG DISCLAIMER:**
AI kan INTE läsa GitHub Project direkt. Du MÅSTE copy-pasta issues från GitHub Project här.
Om backloggen har uppdaterats, kan AI:s svar vara förvirat.

---

## ✅ Output Efter Mötet

**AI Teamleader dokumenterar:**

```
📋 TORSDAGS MÖTES-SAMMANFATTNING
=================================

Datum: [Torsdag, vecka X]
Närvarande: [Backend], [Frontend], [Native], [Team Lead]

🟢 COMPLETED THIS WEEK:
- Issue #X: [Kort beskrivning]
- Issue #Y: [Kort beskrivning]
- Total: X issues slutförda denna vecka

🟡 WIP - READY FOR COMPLETION IMORGON:
- Issue #A: Backend working
- Issue #B: Frontend testing
Expected completion: Fredag kväll

🔴 WIP - PUSHING TO NEXT WEEK:
- Issue #C: Too large, needs scope reduction
- Reason: [Vad gjorde det för stort?]
- Next steps: Pre-planning Monday

🚨 BLOCKERS LÖSTA:
- Blocker #1: "FX-modul långsam"
  Status: PAIR-PROGRAMMING SCHEDULED Friday 10:00
  Owner: Native + Backend
  Mitigation: Benchmark test prepared

- Blocker #2: "API-kontrakt"
  Status: DEFINED in meeting
  Owner: BE + FE
  Next: Implement Friday

⚠️ NEW BLOCKERS IDENTIFIED:
- [Om nya risker identifierades]

📅 NÄSTA VECKA FOCUS:
- Priority 1: Issue #X
- Priority 2: Issue #Y
- Priority 3: Issue #Z
- Capacity: [X hours total]

💡 TEAM FEEDBACK:
Positive highlights:
✅ [Vad gick bra]

Areas for improvement:
🔧 [Vad kan bli bättre]

Next meeting: Monday 09:00 Sprint Planning
```

---

## 📝 STEG EFTER MÖTE: UPPDATERA DOKUMENTEN

**AI säger vid slutet av mötet:**

```
🎉 Mötet är klart! Nu uppdaterar du dokumenten:

1. ÖPPNA: _sprint/GitHub Project Board

2. HIT ÄR DENNA VECKA:
   "## 🟢 Completed Last Sprint (V37: 7-13 Sep)"
   → COPY-PASTA denna vecka's completions här
   → Märk "V37" istället för gamla veckan

3. HIT ÄR WIP-STATUS:
   "### ✅ Issues Planned This Sprint"
   → Uppdatera % Done för varje issue
   → Märk färdiga issues som ✅ DONE
   → Uppdatera Status kolumn

4. HIT ÄR BLOCKERS:
   "## 🔴 Blockers & Risks This Sprint"
   → COPY-PASTA nya/lösta blockers från mötet
   → Uppdatera status på risk-register

5. HIT ÄR NÄSTA VECKA:
   "## 🎯 What's Next This Week"
   → Vilka issues prioriterades för nästa vecka?
   → Ny fokus-område?

SEDAN: Öppna _sprint/Google Sheets Risker
6. HIT ÄR RISKER:
   "## 🎯 Risk Response Matrix"
   → Uppdatera status på varje risk
   → Nya risker identifierade? Lägg till

SPARAD! Du är klar 🎉
```

---

## 🎯 Success Criteria

Mötet är lyckat om vi:
- ✅ Vet exakt vilka issues blir DONE denna vecka
- ✅ Vet vilka bliver skjutna till nästa vecka (och varför)
- ✅ Har löst minst 1 blocker
- ✅ Har plan för nästa vecka
- ✅ Mötet varade < 45 minuter
- ✅ Alla förstår nästa steg

Mötet är INTE lyckat om:
- ❌ Vi inte vet status på WIP-issues
- ❌ Vi lämnar blockers osölda
- ❌ Vi skjuter issues utan att säga varför
- ❌ Mötet blir längre än 60 minuter
- ❌ Ingen har plan för nästa vecka

---

## 🚨 Red Flags - Vad Ska AI Fråga Vidare Om?

### Om AI Hör Detta:
- **"Vi hinner inte denna vecka"** 
  → Fråga: "Vilka 2 issues ska vi prioritera? Vilket skjuter vi?"
  
- **"Issue X är stuck"**
  → Fråga: "Varför? Vem kan hjälpa? Gör vi det IDAG?"
  
- **"Vi är trötta"**
  → Säg: "Då fokuserar vi på 2 issues nästa vecka. Vilka två?"
  
- **"Test-coverage är låg"**
  → Säg: "CTO deadline 24 sep - prioritera tests framåt. Allocera 8h nästa vecka"
  
- **"Backend och Frontend har inte talat"**
  → Säg: "Define API-kontrakt IDAG eller Monday morgon. This blocks progress"

---

## 📚 Länkade Dokument

Läs dessa före mötet:
- **GitHub Project Board** - Actual sprint status
- **Google Sheets Risker** - Risk matrix
- **BACKLOG.md** - Vilka issues finns?
- **SPRINT_PLANNING.md** - Planning guide

---

## 🎓 Viktiga Poänger För AI Teamleader

1. **Fokusera på OUTCOMES, inte processen**
   - Inte: "Vad har du gjort?"
   - Utan: "Är det klart? Varför inte?"

2. **Lösa Blockers OMEDELBAR**
   - Inte: "Vi löser det nästa vecka"
   - Utan: "Vem kan hjälpa idag? Gör vi det nu?"

3. **Dokumentera ALLT**
   - Varje decision → skriva i mötes-summary
   - Varje blocker → uppdatera GitHub Project Board
   - Varje risk → uppdatera Google Sheets Risker

4. **Ge Credit & Learning**
   - Positivt feedback → moral upp
   - Konstruktiv kritik → lär teamet
   - Tips → mentorhip

5. **Kolla Mot Deadlines**
   - CTO deadline 24 sep - 20 dagar kvar
   - Fokus på kärnflödet, inte nice-to-have

---

## 🚀 Quick Start

1. Kopiera länken till denna fil
2. Kopiera länken till GitHub Project Board
3. Kopiera länken till Google Sheets Risker
4. Klistra in dessa i AI-modellen tillsammans med AI_TEAMLEADER.md
5. Säg: "Kör torsdags-möte"
6. Ge teamets svar när AI frågar

**Resultat:** Effektivt möte på 30 minuter, allt dokumenterat! ✅

---

*Last Updated: 2026-09-04*  
*Purpose: Structured Thursday end-of-week check-in*  
*Duration: 30-45 minutes*  
*Facilitator: AI (Any Model)*
