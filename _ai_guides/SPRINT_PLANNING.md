# Sprint Planering - Team 1 Vägledning

**Denna guide hjälper dig planera sprintar som är fokuserade, realistiska och levererar värde.**

---

## 📋 Sprintplanering Checklist - KÖR DETTA VARJE VECKA

### 🟢 FÖRE PLANERING (Måndag morgon)

**Tid:** 60 minuter före sprintmöte  
**Ansvarig:** Team Lead / Scrum Master / AI

---

## 🔴 KRITISKT — AI MÅSTE LÄSA ALLT DETTA:

**Innan AI presenterar status, måste den läsa i denna ordning:**

```
1. 📋 MÖTESPROTOKOLLET (SENASTE)
   Länk: https://docs.google.com/document/d/1WD9XJBVrE49Csqz-XYiLgejlKlCA4t5sWiwoTkNiTD8/
   ├─ Vad diskuterades förra veckan?
   ├─ Vilka beslut togs? (B = beslut)
   ├─ Vilka action items? (I = information)
   ├─ Feedback från PL/CTO?
   ├─ Risker som identifierades?
   └─ Vad sa vi skulle fokuseras denna vecka?

2. 📊 GIT LOG (denna vecka)
   $ git log --oneline --since="1 week ago"
   ├─ Vilka commits kom in?
   ├─ Vilka PRs mergades?
   └─ Vad blev klart?

3. 📈 GITHUB PROJECT BOARD (denna vecka)
   ├─ Vilka issues är Done?
   ├─ Vilka är In Progress?
   ├─ Vilka blockers finns?
   └─ Status för denna veckas fokus?

4. ⏰ DEADLINES & FOKUS (från SPRINT_FOCUS_TIMELINE.md)
   ├─ Vilken vecka är det?
   ├─ Vad är fokus denna vecka?
   ├─ Vilka deadlines gäller?
   └─ Vad måste vi leverera?

5. 🚨 RISKER (från mötesprotokollet + Google Sheets)
   ├─ Vilka risker identifierades förra veckan?
   ├─ Är de lösta?
   ├─ Nya risker denna vecka?
   └─ Vilka är kritiska?
```

---

- [ ] **1. Läs Mötesprotokollet FÖRST (via RAW-LÄNK)**
  - **🔴 KRITISKT:** AI måste kunna läsa mötesprotokollet direkt
  - Google Docs länk: https://docs.google.com/document/d/1WD9XJBVrE49Csqz-XYiLgejlKlCA4t5sWiwoTkNiTD8/
  - **RAW-EXPORT LÄNK (för AI):** `https://docs.google.com/document/d/1WD9XJBVrE49Csqz-XYiLgejlKlCA4t5sWiwoTkNiTD8/export?format=txt`
  
  **🟢 DELA DIREKT MED AI — Google Docs ÄR redan öppen**
  ```
  Du: "Läs mötesprotokollet från denna raw-länk:
  https://docs.google.com/document/d/1WD9XJBVrE49Csqz-XYiLgejlKlCA4t5sWiwoTkNiTD8/export?format=txt
  
  Sedan: Förbered FÖR mandagsmötet"
  ```
  
  **✅ AI kan läsa det direkt — ingen autentisering behövs**
  (Dokumentet är inställt på "vem som helst med länken kan se")
  
  **FÖRDELAR:**
  ✅ AI läser mötesprotokollet direkt
  ✅ Ingen copy-pasta behövs
  ✅ Alltid aktuell (senaste versionen)
  ✅ Fungerar med vilken AI som helst (ChatGPT, Gemini, Claude, etc)
  
  **OM AI inte kan läsa den (för någon anledning):**
  ```
  Du: Copy-pasta innehållet från Google Docs här,
  så kan AI läsa det från texten istället
  ```

  ---

  **🔴 KRITISKT: AI MÅSTE SÄGA OM DEN INTE KAN LÄSA MÖTESPROTOKOLLET!**

  **Om AI inte kan läsa mötesprotokollet, måste den TYDLIGT säga:**
  
  ```
  ❌ "Jag kan inte läsa mötesprotokollet från länken (behöver autentisering).
  
  🔴 UTAN mötesprotokollet kan jag inte förbered mötet ordentligt!
  
  LÖSNING: Copy-pasta helt innehållet från Google Docs här, så kan jag:
  - Se vilka BESLUT som togs
  - Se vilka ACTION ITEMS som ska följas upp
  - Se feedback från PL/CTO
  - Förstå överenskomna prioriteringar
  
  Väntar på mötesprotokollet innan jag fortsätter."
  ```

  **AI SKA ALDRIG:**
  - ❌ Fortsätta utan mötesprotokollet
  - ❌ Låtsas att den läst det
  - ❌ Gissa vad som diskuterades
  - ❌ Skapa sprint-plan baserad på git log ensamt

  **AI SKA ALLTID:**
  - ✅ Säga tydligt "Jag behöver mötesprotokollet"
  - ✅ Förklara VARFÖR det är kritiskt
  - ✅ Vänta på mötesprotokollet
  - ✅ SEDAN förbered mötet med full kontext
  
  - Format: I = Information, B = Beslut
  - **DETTA är källan till vad som diskuterades förra veckan**
  - Vilka action items har vi?
  - Vilka beslut togs? (MÅSTE respekteras denna vecka!)
  
- [ ] **2. Se över vad som är gjort** (från mötesprotokollet + git)
  - Kör `git log --oneline --since="1 week ago"`
  - Vilka commits kom in förra sprinten?
  - Matcherar commits med mötesprotokollets action items?
  - Vad blev inte klart? (Lägg tillbaka i backlog)
  
- [ ] **3. Granska denna veckas fokus** (från mötesprotokollet + SPRINT_FOCUS_TIMELINE.md)
  - Vad sa vi skulle fokuseras denna vecka? (se mötesprotokollet)
  - Matchar mötesprotokollet med SPRINT_FOCUS_TIMELINE.md?
  - Vilka deadlines gäller denna vecka?
  
- [ ] **4. Uppdatera Project Board status**
  - Rapportera vad som är gjort (mark issues Done)
  - Notera blockers från förra sprinten (use labels)
  - Uppdatera fokus-område för denna vecka (add labels)
  - **Verifiera att status i Project Board matchar mötesprotokollet**

- [ ] **5. Kolla deadlines & risker**
  - Vilka deadlines nämnde mötesprotokollet?
  - Vilka risker identifierades förra veckan?
  - Är de lösta? Nya denna vecka?
  - Canvas-inlämningar denna vecka?

- [ ] **6. ⚙️ ISSUE REVIEW & REFINEMENT — Granskar backlog för denna vecka (15 min)**

  **SYFTE:** Se till att issues är aktuella, realistiska och inte leder till blockers
  
  **AI/Team läser ALLA issues på backlog denna vecka och verifierar:**
  
  ```
  ✅ DEFINITION OF READY — Är varje issue startbar?
     ├─ Titel följer [Category] format? ([Frontend], [Backend], [Native])
     ├─ Problem är tydligt definierat?
     ├─ Acceptanskriterier är klara (AC)?
     ├─ Definition of Ready är uppfylld? (DoR checklist)
     ├─ Inga kritiska blockers?
     └─ Estimat är realistisk (story points eller timmar)?
  
  ✅ ÄR ISSUEN FORTFARANDE AKTUELL?
     ├─ Har något ändrat sedan den skapades?
     ├─ Är prioriteringen fortfarande rätt?
     ├─ Behöver vi ta bort eller uppdatera något?
     ├─ Matchar den denna veckas fokus?
     └─ Finns det en bättre ordning att göra dem?
  
  ✅ ARKITEKTUR & BLOCKERS — Kan vi göra den utan stopp?
     ├─ Hänger den på någon annan issues avslutande?
     ├─ Behöver vi något från annan team?
     ├─ Finns API/design/data redan, eller behöver vi vänta?
     ├─ Är det möjligt att parallellisera med andra issues?
     └─ Vad kan gå fel? (risk-analys)
  
  ✅ FÖRSLAG PÅ ÄNDRINGAR — AI föreslår förbättringar:
     ├─ "DoR är ofullständig — lägg till: @person ansvarig för API?"
     ├─ "Estimatet 8h verkar lågt — föreslår 12h baserat på komplexitet"
     ├─ "Denna issue hänger på PR #51 — vi kan inte starta än"
     ├─ "Denna issue kan göras parallellt med issue #52 — bra effektivitet"
     ├─ "AC är vag — föreslår: 'Risk metrics visar volatilitet + Sharpe ratio'"
     └─ "Issue #23 är redan delvis gjord i en annan branch — kan vi merge det först?"
  ```
  
  **OUTPUT — Före sprintmöte börjar:**
  
  ```
  ISSUE REVIEW RAPPORT:
  
  🟢 KLARA ATT STARTA (5 issues):
  ├─ #52: Risk Metrics (Backend) — DoR OK, estimat 16h ✅
  ├─ #53: FX Converter (Backend) — DoR OK, estimat 12h ✅
  ├─ #60: Target Allocation (Frontend) — DoR OK, estimat 8h ✅
  ├─ #61: Migrations (Backend) — DoR OK, estimat 16h ✅
  └─ #88: Test Improvements (QA) — DoR OK, estimat 12h ✅
  
  🟡 BEHÖVER UPPDATERING (3 issues):
  ├─ #54: Rebalance Suggestions
  │  └─ ⚠️ AC är vag — föreslår: "Beräkna optimal portfolio drift"
  │  └─ ⚠️ Estimat 20h är högt — Är detta för denna sprint?
  │  └─ ⚠️ Hänger på Risk Metrics — Kan vi starta nästa vecka?
  │
  ├─ #62: UI Refinement
  │  └─ ⚠️ Titel saknar [Category] — lägg till [Frontend]
  │  └─ ⚠️ DoR saknar: Vilka Figma-designs finns redan?
  │  └─ ⚠️ Kan vi göra lite av detta denna vecka, resten nästa?
  │
  └─ #89: Performance Testing
     └─ ⚠️ Prioritering låg — men nästan CTO deadline. Bör vi skjuta?
     └─ ⚠️ Behöver alla andra issues klara först (7 dagar fram)
  
  🔴 MÅSTE VÄNTA (2 issues):
  ├─ #70: Advanced Analytics — Hänger på Risk Metrics (inte klar än)
  └─ #71: Mobile Notifications — Scope unclear, behöver möte med PL först
  
  REKOMMENDATION:
  • Prioritera #52, #53, #60 denna vecka (kritiska för CTO)
  • Skjut #54 till nästa vecka (hänger på #52)
  • Uppdatera #62 DoR innan vi startar
  • Hoppa över #89 denna vecka (inte kritisk)
  ```

---

### 🟡 SPRINTPLANERING (Måndag 09:00-12:00) — VERKLIG MÖTESPRAXIS

**Deltagare:** Hela Team 1 (backend, frontend, native)  
**Resultat:** Sprint backlog i GitHub/Project board

---

## 📖 PEDAGOGISK INTRODUKTION — Vad Är Ett Sprintmöte?

**För de som aldrig varit på ett riktigt sprintmöte innan:**

### VAD? — Definition

```
📖 Ett sprintmöte är INTE:
❌ En rapport där alla säger vad de gjort (det är standup)
❌ En kodreview (det är ett separat möte)
❌ Ett möte där bara chefen pratar (det är en presentation)

✅ Ett sprintmöte ÄR:
✅ En planering tillsammans för nästa vecka
✅ Vi beslutar TILLSAMMANS vad vi ska göra
✅ Vi estimerar TILLSAMMANS hur långt det tar
✅ Vi löser blockers TILLSAMMANS
✅ Vi säkerställer att alla förstår sitt jobb
```

### VARFÖR? — Syftet

```
💡 VARFÖR gör vi det här?

Scenario 1 — UTAN sprintmöte:
├─ Backend tar ett estimat från GitHub: "8 timmar"
├─ Backend arbetar i 2 dagar, sedan: "Oops, det var 16 timmar"
├─ Frontend väntar på Backend-API (blockerad)
├─ Kund är besviken (vi inte klar på deadline)
└─ RESULTAT: Chaos och misslyckande

Scenario 2 — MED sprintmöte:
├─ Vi diskuterar tillsammans: "Risk Metrics tar 16 timmar"
├─ Vi säger: "Ok, det är hög prioritet denna vecka"
├─ Frontend VET att API kommer senare, kan jobba på annat
├─ Vi löser blockers INNAN veckan börjar
├─ Kund är nöjd (vi levererar på deadline)
└─ RESULTAT: Ordning och framgång

🎯 Sprintmötet = Vi jobbar smart tillsammans
```

### HUR? — Processen (Förenkl)

```
🛠️ ENKELT: Sprintmöte i tre faser

FASE 1: Vad blev gjort? (Förra veckan)
└─ "Vad blev klart? Vilka blockers?"
└─ Längd: 10 minuter
└─ Feeling: "Ok, vi vet var vi står"

FASE 2: Vad gör vi denna vecka? (Denna vecka)
└─ "Vilka är KRITISKA issues?"
└─ "Hur långt tar de?"
└─ "Vem gör vad?"
└─ Längd: 2 timmar
└─ Feeling: "Ok, jag vet mitt jobb"

FASE 3: Framgång & Risker (Denna vecka)
└─ "Hur vet vi att vi lyckas?"
└─ "Vad kan gå fel?"
└─ "Vem hjälper om vi fastnar?"
└─ Längd: 30 minuter
└─ Feeling: "Vi är redo att börja"
```

### NÄR? — Tidpunkt

```
⏰ TRADITIONELLT:
├─ MÅNDAG MORGON (inte fredag eftermiddag!)
├─ 09:00 - 12:00 (3 timmar för ett lag på ~6 personer)
├─ Första dagen av sprint (ny vecka = frisk energi)
└─ SAMMA TID varje vecka (förutsägbar)

💡 VARFÖR MÅNDAG?
└─ Veckans början = ny energi
└─ Du kan ge feedback redan tisdag
└─ Folk är friska (inte utmattade på fredag)
└─ Mötet sätter tonen för veckan
```

### VEM? — Roller & Ansvar

```
👥 ROLLERNA I MÖTET:

🎯 TEAM LEAD / SCRUM MASTER
├─ Facilitator (leder mötet)
├─ Timekeeper (håller tider)
├─ Konfliktlösare (Backend vs Frontend disagree)
├─ Motivator ("Vi kan göra detta!")
└─ Dokumenterare (skriver mötesprotokollet)

💼 PRODUCT LEAD / PRODUCT OWNER
├─ Säger prioriteringen ("Risk Metrics först")
├─ Svarar på scope-frågor ("Kan vi göra det utan detta?")
├─ Tie-breaker vid konflikter
└─ Representerar kunden/business

👨‍💻 BACKEND-UTVECKLARE
├─ Estimerar sitt arbete ("Risk Metrics = 16h")
├─ Säger blockers ("Vi behöver Swagger docs")
├─ Frågar om klarhet ("Vad betyder 'accurate'?")
└─ Lyssnar på Frontend-behov ("Vi behöver API på torsdag")

🎨 FRONTEND-UTVECKLARE
├─ Estimerar sitt arbete ("UI = 10h")
├─ Säger blockers ("Vi väntar på Backend API")
├─ Frågar om design ("Vilken Figma-design är det?")
└─ Lyssnar på Native-behov ("Behöver ni något från oss?")

📱 NATIVE/SYSTEM-UTVECKLARE
├─ Estimerar sitt arbete ("Calculations = 12h")
├─ Säger blockers ("Behöver vi data från Backend?")
├─ Verifierar arkitektur-antaganden
└─ Stödjer vid behov

🤝 ALLA TILLSAMMANS
├─ Lyssnar på varandra
├─ Ställer frågor om klarhet
├─ Löser blockers tillsammans
├─ Säger om något är orealistiskt
└─ Committar till veckan tillsammans
```

---

## 🎯 VERKLIGT SPRINTMÖTE — Hur Det Faktiskt Fungerar

### FÖRE MÖTET (AI + Team Lead gör detta)

**Ansvarig: Team Lead / Scrum Master**

```
30 min innan möte börjar:

✅ Läs mötesprotokollet (senaste beslut + action items)
✅ Gör Issue Review & Refinement (se SPRINT_PLANNING.md, punkt 6)
✅ Förbered 3-4 diskussionspunkter baserat på blockers från förra vecka
✅ Sätt upp fysisk/digital mötesutrymme
✅ Säkerställ att GitHub Project Board är uppdaterad
✅ Testa att presentation funkar (hvis den finns)
✅ Sätt timer på mobilen (3 timmar)
```

### PEDAGOGISKA EXEMPEL — Verkliga Mötes-Dialoger

**Här är exempel på vad mötet faktiskt låter som:**

**Exempel 1: Estimering (Vad det INTE ska låta som)**

```
❌ DÅLIGT:
Lead: "Risk Metrics, hur många timmar?"
Backend: "Eh... typ 8?"
Lead: "Ok, nästa issue..."

❌ PROBLEM:
└─ Backend är osäker ("typ 8")
└─ Vi vet inte varför
└─ Möjligt att det blir 16 timmar
└─ Hela planen brister
```

**Exempel 1b: Estimering (BRA)**

```
✅ BRA:
Lead: "Risk Metrics, hur många timmar?"
Backend: "Jag sa 16h förra veckan. Det är:
         ├─ API endpoint (4h)
         ├─ Beräkningar i Native (6h)
         ├─ Tester (4h)
         └─ Dokumentation (2h)
         Men jag är osäker på Native-delen..."

Native: "Jag kan hjälpa. Det är ungefär 6h om jag har spec."

Backend: "Vi har ingen Swagger spec än. Det kan ta 1-2h extra."

Lead: "Ok, så Risk Metrics = 16-18h denna vecka. Passar det?"

Backend: "Ja, om vi inte får andra blockers."

Lead: "Dokumenterar: Risk Metrics 16h, blocker = Swagger docs"

✅ BÄTTRE:
└─ Vi VET vad som ingår
└─ Vi VET vad som är osäkert
└─ Vi KAN adressera blockers
└─ Planen är realistisk
```

**Exempel 2: Lösa en konflikt**

```
Frontend: "Vi behöver UI-skisser från design innan vi kan börja Target Allocation"

Design: "Jag kan ha det på torsdag"

Lead: "Så Frontend kan inte starta Target Allocation förrän torsdag?"

Frontend: "Nej, och det tar 8 timmar. Så tidigast fredag."

Backend: "Men vi behöver Target Allocation för vår Rebalance-feature nästa vecka!"

Lead: "Ok, här är valet:
       A) Frontend väntar på design (torsdag start)
       B) Frontend börjar utan design (snabbare, men risk)
       C) Vi skjuter Target Allocation till nästa vecka"

PL: "Vi behöver det för kvaldemo. Design är viktig här. Option A — vi får acceptera att det blir sent denna vecka."

Lead: "Dokumenterar: Design prioriteras, Target Allocation startar torsdag, Backend jobbar på något annat denna vecka"

✅ RESULTAT: Beslut är fat, alla förstår, ingen är besviken
```

**Exempel 3: Att säga "Nej" realistiskt**

```
Lead: "Vi har 5 issues här, totalt 48h, men vi har bara 35h denna vecka."

Backend: "Vi kan väl jobba snabbare?"

Lead: "Vi kan alltid försuöka, men estimat är baserat på erfarenhet. Vad gör vi?"

PL: "Risk Metrics är MÅSTE-ha. FX-converter är MÅSTE-ha. Rebalance kan skjutas."

Frontend: "Ok, då jobbar vi på Risk API-integration och Rebalance pushes till nästa vecka."

Lead: "Dokumenterar: Rebalance är BACKLOG nästa vecka, scope cut denna vecka"

✅ RESULTAT: Vi är realistiska, CTO-deadline är säker
```

---

### MÖTET — KONKRET AGENDA MED TIDER

```
TIMME 1 (09:00-10:00): STATUS & FOKUS

09:00-09:10 (10 min) — KOLLA IN & ENERGI-BOOST
├─ Kort rundning: "Hur mår ni?"
├─ Ingen deep-dive, bara check-in
└─ Skapa gott mötesutrymme

09:10-09:20 (10 min) — FÖRRA VECKAN (NULÄGE)
├─ Team Lead presenterar vad som blev gjort
├─ Vilka issues blev klara? (från GitHub)
├─ Vilka blockers identifierades?
└─ Feedback från PL/CTO? (från mötesprotokollet)

09:20-09:35 (15 min) — DENNA VECKAS FOKUS (MÅL)
├─ Team Lead läser från mötesprotokollet
├─ VAD ska vi försöka uppnå denna vecka?
├─ VARFÖR är detta prioriterat?
├─ Deadline och risker?
└─ Frågor från teamet?

09:35-10:00 (25 min) — ISSUE REVIEW & REFINEMENT (från förberedelsen)
├─ AI presenterar förslag på ändringar
├─ Diskutera: Är issues realistiska?
├─ Vilka kan vi starta? Vilka behöver vänta?
├─ Är DoR uppfylld för var issue?
└─ Uppdatera GitHub Project Board baserat på diskussion

TIMME 2 (10:00-11:00): PRIORITERING & ESTIMERING

10:00-10:15 (15 min) — PRIORITERING TILLSAMMANS
├─ "Vilka issues är KRITISKA för denna vecka?"
├─ Diskutera: Backend vs Frontend prioritet
├─ Lösa prioriteringskonflikter (PL är tie-breaker)
├─ Uppdatera prioritering i GitHub
└─ RESULTAT: Top issues för denna vecka klara

10:15-10:45 (30 min) — ESTIMERING (Agile Planning Poker eller diskussion)
├─ För varje kritisk issue:
│  ├─ "Hur många timmar? 5h? 10h? 16h?"
│  ├─ Backend sällan, vad är er bedömning?
│  ├─ Frontend, några höga-nivå estimat?
│  └─ Native, ser ni något som tar längre än estimat?
├─ Notera blockers under estimering
├─ Justera estimat baserat på team-feedback
└─ RESULTAT: Alla kritiska issues har estimat

10:45-11:00 (15 min) — KAPACITETSPLANERING
├─ "Vi har X timmar denna vecka (per person)"
├─ "Dessa issues tar Y timmar tillsammans"
├─ "Passar det? Eller behöver vi scope cut?"
├─ Beslut: Vilka issues är IN, vilka är BACKLOG?
└─ RESULTAT: Sprint backlog är finaliserad

TIMME 3 (11:00-12:00): TILLÄMPNING & LÄRDOM

11:00-11:30 (30 min) — TILLDELA ISSUES & KICKOFF
├─ "Vem gör vad denna vecka?"
├─ Tilldela issues till personer/pairs
├─ Notera blockers (vilka behöver support?)
├─ Notera dependencies (vilken ordning?)
├─ Uppdatera GitHub Project Board (assign issues)
└─ RESULTAT: Varje person vet sitt jobb

11:30-11:50 (20 min) — FRAMGÅNGSKRITERIER & RISKER
├─ "Hur vet vi att denna sprint är lyckad?"
├─ Diskutera varningscenarios:
│  ├─ "Om Risk Metrics tar längre tid?"
│  ├─ "Om vi får nya blockers?"
│  └─ "Om nära deadline dyker upp?"
├─ Mitigation för varje risk
├─ Vem är on-call för blockers?
└─ RESULTAT: Team vet vad som är framgång/misslyckande

11:50-12:00 (10 min) — AVSLUT & RETROSPEKTIV-PROMPT
├─ "Vad gick bra med detta möte?"
├─ "Vad kan vi göra annorlunda nästa vecka?"
├─ Kort feedback-runda
└─ "Håll humöret! Denna vecka fokuserar vi på..."

RESULTAT FRÅN MÖTET:
✅ Mötesprotokollet uppdaterat (vad var beslut?)
✅ GitHub Project Board uppdaterad (issues assigned)
✅ Estimat låst för denna sprint
✅ Risk Dashboard uppdaterad
✅ Varje person vet sitt jobb
✅ Deadlines klara
✅ Team är motiverat för denna vecka
```

### MÖTESFASILITERING — LEDARENS ROLL

**Vad gör Team Lead under mötet?**

```
✅ HÅLLA TIDER
├─ Timer på 15 min per sektion
├─ "Vi har 5 min kvar för denna punkt"
├─ Styr diskussion tillbaka om den går vilse
└─ Om vi behöver mer tid: "Parkeringslist" för senare

✅ SÄKERSTÄLLA DELTAGANDE
├─ Lyssna på alla röster (inte bara senior devs)
├─ "Anna, vad tycker du? Du känner frontend bäst"
├─ "Kiran, ser du någon risk här?"
├─ Om någon är tyst: "Marco, du jobbar på detta — vad behöver du?"

✅ LÖSA KONFLIKTER
├─ Backend vill göra X, Frontend vill göra Y
├─ "Jag förstår båda perspektiven. Låt oss rösta."
├─ Om inte enighet: "PL bestämmer prioritet"
├─ Dokumentera beslutet, gå vidare

✅ HÅLLA FOKUS
├─ "Det är en bra fråga, men den är för denna sprint review"
├─ "Låt oss adressera denna i nästa retrospektiv"
├─ Ej låta teknikdiskussioner ta över mötet
├─ "Tekniska detaljer kan ni lösa i pair programming"

✅ DOKUMENTERA VÄGEN
├─ "Noterar: Risk Metrics kan ta längre än estimat"
├─ "Noterar: Vi behöver Swagger docs från Backend"
├─ "Noterar: Frontend blockeras på API"
├─ Mötesprotokollet uppdateras under mötet
```

### VERKLIGA MÖTESBETEENDEN — VAD SOM KAN HÄNDA

```
🟢 BRA MÖTESBETEENDEN:
✅ "Jag är osäker på detta estimat — kan vi parprogrammera på det?"
✅ "Jag ser ett blocker här — vi behöver API docs från Backend"
✅ "Det här tar längre än vi estimerade — bör vi reducera scope?"
✅ "Kan vi börja detta innan förutsättningen är klar?"
✅ "Vilken hjälp behöver ni från mig denna vecka?"

🟠 VARNINGS-BETEENDEN:
⚠️ "Jag estimerar 8h, men egentligen vet jag inte..."
   → Fråga: "Vad gör dig osäker? Kan vi dela upp det?"

⚠️ "Vi kan försöka göra allt detta"
   → Säg: "Vi har X timmar. Låt oss prioritera"

⚠️ "Vi behöver den här funktionen men det är ej klart..."
   → Fråga: "Kan vi göra det utan den? Eller behöver vi vänta?"

❌ RÖDA FLAGS:
❌ "Jag vet inte hur länge detta tar"
   → Måste estimera eller dela upp

❌ "Vi gör allt detta och mer"
   → Scope är för stor — behöver skära ner

❌ "Denna issue är helt oklar"
   → DoR är inte uppfylld — kan ej starta

❌ "Ingen vet vem som gör vad"
   → Tilldelning är ofullständig — måste lösa
```

### EFTER MÖTET (Samma dag)

```
✅ Team Lead uppdaterar GitHub Project Board
   └─ Alla issues assignade
   └─ Sprint label tillagd
   └─ Estimat synliga
   └─ Priority-ordning klar

✅ Skicka mötesprotokollet till teamet
   └─ "Här är vad vi beslutade"
   └─ "Action items denna vecka"
   └─ "Deadline: 24 sep 16:00"

✅ Kickoff-möte (kort) för varje team
   └─ Backend: "Här är era issues denna vecka"
   └─ Frontend: "Här är era issues denna vecka"
   └─ Parprogrammering setup om behövs
```

---

## 🎯 STRUKTUR: NULÄGE → MÅL → FRAMGÅNGSKRITERIER

**Varje sprintmöte MÅSTE innehålla dessa tre delar (i denna ordning):**

### 📊 DEL 1: NULÄGE (Status från förra sprint) — 10 min

Team Lead presenterar:
```
NULÄGE:
├─ Vad blev klart förra veckan? (commits från git log)
├─ Vad blev INTE klart? (varför? vilka blockers?)
├─ Vilka risker identifierades förra veckan?
├─ Vilken feedback fick vi från PL/CTO?
└─ Hur är vi ställda mot deadlines?

EXEMPEL:
✅ Login form fungerar (från PR #46)
❌ Risk metrics inte klara (blocked by API)
⚠️ Performance metrics försämrades (Lighthouse 75→70)
📝 Feedback: "Vi behöver mer tests"
📅 CTO-deadline: 24 sep (11 dagar kvar, på rätt väg)
```

### 🎯 DEL 2: MÅL FÖR DENNA SPRINT (Vad ska vi försöka uppnå?) — 15 min

Team Lead presenterar:
```
MÅL DENNA SPRINT (Vecka X):

Från SPRINT_FOCUS_TIMELINE.md:
"V6: Kunna visa CTO att kärnflödet fungerar"

För att nå det måste vi denna vecka:
1. ✅ Risk metrics (backend) - MÅSTE vara klart
2. ✅ FX converter (backend) - MÅSTE vara klart
3. ✅ Test coverage 70% - MÅSTE vara klart
4. 🟡 Portfolio optimization (frontend) - om tid

Resultat om vi lyckas:
- Vi kan demot kärnflödet för CTO
- Vi har 70%+ test coverage
- Vi är redo för CTO-feedback session

Resultat om vi INTE lyckas:
- Vi missar CTO deadline → Sämre intryck
- Vi är i backlog och måste in nästa vecka igen
- Vi kan inte gå vidare till kvaldemo-prep
```

### ✅ DEL 3: FRAMGÅNGSKRITERIER (Hur vet vi att vi lyckades?) — 5 min

```
FRAMGÅNGSKRITERIER - Sprint är LYCKAT om:

✅ Risk metrics är 100% klara (PR merged, tests pass)
✅ FX converter är 100% klara (PR merged, tests pass)
✅ Test coverage är 70%+ (CI rapporterar det)
✅ Kärnflödet kan demos (login → portfolio → allocate)
✅ All dokumentation uppdaterad (README, decisions)
✅ Git history är tydlig (commits i rätt format)

VARNING-TECKEN (Sprint är i risk om):
⚠️ Risk metrics eller FX-converter är < 80% klara
⚠️ Test coverage sjunker (< 60%)
⚠️ Blockers identifieras utan mitigation
⚠️ Pull requests inte reviewade i tid

MISSLYCKANDE (Sprint är FAILED om):
❌ Risk metrics eller FX-converter inte klara
❌ Test coverage < 60%
❌ Kärnflödet kan INTE demoas
❌ Git history är rörig/omorganiserad
```

---

#### Steg 1: Presentera Fokus (15 min)
Team Lead presenterar:
- **NULÄGE:** Vad blev klart/ej klart förra veckan?
- **MÅL:** Vad ska vi försöka uppnå denna vecka?
- **FRAMGÅNGSKRITERIER:** Hur vet vi att vi lyckades?
- **RISK DASHBOARD:** Status per team (färgkodad)
- Vilka deadlines gäller?

---

### 🚨 RISK DASHBOARD (Per Team + Färgkodning)

**Presenteras på mötet som ett tydligt dashboard:**

```
┌─────────────────────────────────────────────────────────┐
│           🚨 RISK DASHBOARD — Vecka 6                   │
├─────────────────────────────────────────────────────────┤
│                                                         │
│  FRONTEND TEAM                    Status               │
│  ├─ LoginForm: ✅ 100% DONE        🟢 ON TRACK        │
│  ├─ Portfolio Overview: 80% done   🟠 SLIGHT DELAY    │
│  ├─ Test Coverage: 45% (need 70%)  🔴 CRITICAL        │
│  ├─ Performance (Lighthouse): 75   🟠 NEEDS WORK      │
│  └─ Blockers: Waiting on CSS vars  🟠 MINOR BLOCKER   │
│                                                         │
│  BACKEND TEAM                     Status               │
│  ├─ Risk Metrics: 40% done         🔴 CRITICAL        │
│  ├─ FX Converter: 30% done         🔴 CRITICAL        │
│  ├─ API Endpoints: 60% done        🟠 ON TRACK        │
│  ├─ Blockers: Swagger docs missing 🔴 BLOCKER         │
│  └─ DB Migrations: Not started     🟠 RISK            │
│                                                         │
│  NATIVE TEAM                      Status               │
│  ├─ Volatility Calc: 50% done      🟢 ON TRACK        │
│  ├─ Max Drawdown: 30% done         🟠 SLIGHT DELAY    │
│  ├─ Performance: Good              🟢 ON TRACK        │
│  ├─ Blockers: None                 🟢 CLEAR           │
│  └─ Tests: 80% coverage            🟢 GOOD            │
│                                                         │
│  OVERALL SPRINT STATUS:            🟠 AT RISK         │
│  (Backend kritisk, andra ok)                           │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

---

#### Förklaring av Färgkoder:

| Färg | Betydelse | Vad Det Betyder | Åtgärd |
|------|-----------|-----------------|--------|
| 🟢 GRÖN | ON TRACK | Ligger i fas, ingen risk | Fortsätt så! |
| 🟠 ORANGE | SLIGHT DELAY | Börjar bli lite bråttom | Fokusera denna vecka |
| 🔴 RÖD | CRITICAL | Kritisk, riskerar blocker | MÅSTE prioritera NU |

**Exempel på varje nivå:**

```
🟢 GRÖN — LoginForm 100% done
   Status: Klart, testat, merged, inga blockers
   Risk: 0%
   Åtgärd: Ingen, gå vidare

🟠 ORANGE — Portfolio Overview 80% done
   Status: Nästan klart men slow progress
   Risk: Kan bli blocker om inte fokuseras
   Åtgärd: Allokera extra timmar denna vecka

🔴 RÖD — Risk Metrics 40% done (MÅSTE klart denna vecka!)
   Status: Långt bakom, blockar andra
   Risk: Kommer ALDRIG klart om ingenting ändras
   Åtgärd: ALLT team fokuserar på detta IDAG
          Pausera allt annat
          Pair programming if needed
          Escalera till PL om ej löst
```

---

#### Vilka Risker Ska Visas?

**Per team, visa:**
- 📊 Varje issue + progress (% done)
- 🎯 Beräknad färg (🟢/🟠/🔴)
- 🚫 Blockers (explicit)
- ⏱️ Estimat vs faktisk tid använd
- 📅 Tid kvar till deadline

**Exempel Risk-Analys:**

```
BACKEND: Risk Metrics

📊 Status: 40% done (12h använt av 16h estimat)
⏱️ Tid kvar: 3 dagar
✅ Estimat vs faktisk: OK så långt (12h vs 12h)
🚫 Blocker: Swagger docs från API team (ORANGE)
🎯 Färg: 🔴 RÖD (kommer inte klart om ingenting ändras)

VARFÖR RÖD?
- 40% done × 3 dagar = max 50-60% done
- Vi behöver 100% klart för CTO deadline
- Blockern (Swagger) förhindrar full progress

ÅTGÄRD:
1. API team: PRIORITY! Swagger docs idag
2. Backend team: Pair programming imorgon
3. Cut scope om needed: Enbart kritiska metrics
4. Update PL if still at risk på tisdag
```

---

### 👥 VAD FÅR VARJE LITET TEAM VID MÖTET?

**De tre små teamen (Frontend, Backend, Native) får TEAM-STATUS för sitt område:**

---

## FRONTEND TEAM — DIN TEAM STATUS:

**ISSUES & STATUS:**
```
Issue #24 - LoginForm
  └─ Status: ✅ 100% DONE
     ├─ Tests: Pass
     ├─ Code review: Approved
     └─ Merged: Yes

Issue #42 - Portfolio Overview
  └─ Status: 75% done (ON TRACK)
     ├─ Estimat: 16h
     ├─ Använt: 12h
     ├─ Blockers: Väntar CSS vars från design
     └─ Next: Tests this week

Issue #50 - Test Coverage
  └─ Status: 45% done (RISK)
     ├─ Estimat: 20h (totalt)
     ├─ Använt: 10h
     ├─ Problem: Tests tar längre än estimerat
     └─ Impact: May not hit 70% target
```

**HUR VI KAN HJÄLPA:**
```
Blockrar:
├─ Design CSS vars - Vem kan prioritera från design IDAG?
├─ Tests komplexare - Vem kan pair programming imorgon?
└─ Performance work - Native team kan support (de är klara)

Lösningar:
├─ Pair programming på tests (intern eller external help?)
├─ Omfördela: Vem tar vad denna vecka?
├─ Cut scope: Skip nice-to-have polish denna vecka?
└─ Support: Backend team kan review CSS när den kommer

Fokus denna vecka: Tests är viktiga för DoD
```

---

## BACKEND TEAM — DIN TEAM STATUS:

**ISSUES & STATUS:**
```
Issue #52 - Risk Metrics
  └─ Status: 40% done (🔴 KRITISK!)
     ├─ Estimat: 16h
     ├─ Använt: 12h
     ├─ BLOCKER: Swagger docs saknas från API team
     └─ Impact: MÅSTE klart för CTO deadline
     
Issue #53 - FX Converter
  └─ Status: 30% done (🟠 AT RISK)
     ├─ Estimat: 12h
     ├─ Använt: 4h
     ├─ Blockers: Risk Metrics får prioritet
     └─ Impact: May slip to next week

Issue #47 - API Endpoints
  └─ Status: 60% done (ON TRACK)
```

**HÖG PRIORITET DENNA VECKA:**
```
🔴 Risk Metrics MÅSTE klart för CTO deadline
   - API team: Swagger docs ASAP?
   - Backend: Pair programming om Swagger kommer?
   - Native: Kan ni verify calculations?
   - Frontend: Kan ni test Risk Metrics API?
```

**HUR VI KAN HJÄLPA:**
```
Blockers:
├─ Swagger docs saknas - Vem fixar? Idag?
└─ Risk Metrics komplexare - Behöver support?

Lösningar:
├─ Pair programming med Native om Swagger klara?
├─ Frontend kan help test API endpoints
├─ Native kan verify calculations
├─ Omfördela: Cut FX scope denna vecka?
└─ Fokus: Risk Metrics är #1 prioritet

Observation: Risk Metrics är CRITICAL för deadline
```

---

## NATIVE TEAM — DIN TEAM STATUS:

**ISSUES & STATUS:**
```
Issue #88 - Volatility Calculations
  └─ Status: 50% done (ON TRACK 🟢)
     ├─ Estimat: 16h
     ├─ Använt: 8h
     ├─ Blockers: None
     └─ Tests: 80% coverage (good!)

Issue #89 - Max Drawdown
  └─ Status: 30% done (SLIGHT DELAY 🟠)
     ├─ Estimat: 12h
     ├─ Använt: 4h
     └─ Blockers: None (just slower progress)
```

**HUR VI KAN HJÄLPA ANDRA TEAM:**

```
Status: Du är klar med Volatility snart!
        Kan du hjälpa Backend?

Möjligheter:
├─ Backend: Verify Risk Metrics calculations?
├─ Backend: Pair program på Risk Metrics?
├─ Frontend: Performance optimization support?
└─ Support: Du kan vara "force multiplier" för andra

Fokus denna vecka: 
├─ Finish Volatility (du ligger bra till)
└─ Support Backend Risk Metrics (kritisk för deadline)
```
```

---

### 🤝 TEAM-FOKUSERAD ÅTGÄRD (Inte personlig)

**Istället för personlig feedback, fokusera på HUR VI HJÄLPER VARANDRA:**

```
PROBLEM: Risk Metrics kommer inte klart

PERSONLIG FEEDBACK (❌ UNDVIK):
"Marcus, du är bakom. Du måste fokusera bättre."
→ Defensivt, demotiverande, löser inget

TEAM-FOKUSERAD ÅTGÄRD (✅ GÖR DET HÄR):
"Risk Metrics är KRITISK. Hur kan vi hjälpa?
 ├─ API team: Priority Swagger docs IDAG?
 ├─ Backend team: Pair programming imorgon?
 ├─ Native: Kan ni hjälpa verify calculations?
 ├─ Frontend: Kan ni test Risk Metrics API?
 └─ Alla: Risk Metrics är högsta prioritet denna vecka"

→ Samarbete, lösnings-fokus, gemensamt ansvar

---

PROBLEM: Frontend tests tar längre tid

PERSONLIG FEEDBACK (❌ UNDVIK):
"Alex, du är ineffektiv. Tests borde vara snabbare."
→ Kritiserande, löser inget

TEAM-FOKUSERAD ÅTGÄRD (✅ GÖR DET HÄR):
"Tests tar längre än estimerat. Hur kan vi lösa?
 ├─ Pair programming: Vem kan paja tests imorgon?
 ├─ Omfördela: Kan Native/Backend hjälpa test-arbete?
 ├─ Cut scope: Kan vi skip niceto-have tests denna vecka?
 └─ Support: Vad behövs för att gå snabbare?"

→ Samarbete, lösnings-fokus, "vi löser detta tillsammans"
```

---

#### Steg 1b: Risk Dashboard Presentation (5 min extra)

#### Steg 2: Diskutera Backlog (20 min)
- Vilka 5-7 topprioritet-issues ska vi göra denna vecka?
- Finns det beroenden mellan frontend/backend/native?
- Vilka blockers finns redan? (Se GitHub Project Board eller mötesprotokollet)
- Vilka väntar på feedback från förra vecka?

**Använd denna prioriteringsmall:**
```
🔴 KRITISK - Måste vara klart denna vecka (deadline, blocker)
🟡 HÖG - Bör vara klart denna vecka (MVP, risk)
🟢 MEDIUM - Gör om tid (dokumentation, polish)
🔵 LÅG - Nästa sprint (nice-to-have, future)
```

#### Steg 3: Estimera Kapacitet (15 min)
- Hur många timmar jobbar var och en denna vecka? (40h totalt, minus möten)
- Fredagar = 0h kod (LIA-sök + dialoger)
- Tisdagar = 1,5h möte (12:30-14:00)
- Måndagar = 3h sprintplanering + kickoff
- **Realistisk kodtid = ~35h per vecka per person**

**Exempel för 3-personersteam:**
- Backend (1 person): 35h = 2-3 issues à 10-15h
- Frontend (1 person): 35h = 2-3 issues à 10-15h
- Native (1 person): 35h = 1-2 issues à 15-20h (komplexare)

#### Steg 4: Tilldela Issues (10 min)
- Vilken issue jobbar vem på?
- Är det klar-definierad? (Acceptance criteria, beroenden)
- Vem granskar PRn när det är klart?

**Använd denna template för varje issue:**
```
## [Issue Title]
- **Owner:** @person
- **Scope:** Frontend / Backend / Native
- **Acceptance Criteria:** (3-5 checkboxes)
- **Blockers:** (Väntar på X från Y)
- **Estimate:** 8h / 12h / 16h / 20h
- **Definition of Ready:** Klart-definierad? ✅/❌
```

#### Steg 5: Kickoff (5 min)
- Sammanfattning: Vi gör DETTA denna vecka för att nå DETTA
- Vem kontaktar vem om frågor?
- Nästa möte: Torsdag 14:00 (standup/blockers)
- Push alla issues till Project board

---

## 🎯 Definition of Ready (DoR) - Innan Vi Börjar

En issue är **ready** när den har:

- [ ] **Tydlig titel** - "Add portfolio overview dashboard" (inte "dashboard")
- [ ] **Beskrivning** - Vad är problemet? Vad bygger vi?
  ```
  ## Problem
  Vi saknar en portföljöversikt som visar alla sparformer

  ## Lösning
  Build en dashboard med följande paneler: Total value, allocation chart, risk metrics

  ## Acceptance Criteria
  - [ ] Dashboard visar ISK, KF, depå tillsammans
  - [ ] Värden är konverterade till SEK
  - [ ] Komponenten är TypeScript-typed
  ```

- [ ] **Acceptance Criteria** - 3-5 mätbara checkboxes (inte "make it work")
- [ ] **Scope** - Frontend, Backend, Native, eller combo?
- [ ] **Blockers** - Väntar denna issue på något annat?
  - "Väntar på: Backend API för portfolio-data"
  - "Väntar på: FX-konvertering från Native"
  
- [ ] **Estimat** - Hur många timmar? (8/12/16/20h)
- [ ] **Länk till design** - Om UI: länk till mockup/Figma
- [ ] **Länk till arkitektur-beslut** - Om teknisk: länk till DECISIONS.md

**Exempel på READY issue:**
```
## feat(frontend): Add portfolio overview dashboard (#26)

### Problem
User cannot see total portfolio value across all savings forms

### Solution
Build a dashboard that shows:
- Total value (ISK + KF + depå + pension)
- Allocation chart (aktier % vs stabilt %)
- Risk metrics (volatilitet, Sharpe-ratio)
- Values converted to SEK

### Acceptance Criteria
- [ ] Dashboard displays all portfolio data
- [ ] Values are correctly converted to SEK
- [ ] Chart shows allocation breakdown
- [ ] Components are TypeScript-typed
- [ ] CSS modules used (no inline styles)
- [ ] E2E test covers happy path

### Blocks
- Waiting for: Backend portfolio API (#20)
- Waiting for: FX-conversion in native (#17)

### Estimate
16 hours
```

---

## ✅ Definition of Done (DoD) - För PR/Merge

En feature är **klar** när:

### Code
- [ ] Acceptanskriterier är uppfyllda
- [ ] Commits följer format: `type(scope): message (#issue)`
- [ ] Ingen `console.log()`, `TODO`, `FIXME` i kod
- [ ] Linting passerar (`npm run lint`, `mvn clean verify`)

### Testing
- [ ] Unit tests skrivna (min 70% backend, 60% frontend)
- [ ] Integration tests för backend-changes
- [ ] E2E test för user-facing features
- [ ] Alla tests passerar lokalt

### Documentation
- [ ] README uppdaterad (om arkitektur ändrades)
- [ ] Arkitektur-beslut loggat i DECISIONS.md
- [ ] API dokumenterat (Swagger/OpenAPI om ny endpoint)
- [ ] Eventuella gotchas documenterade

### Review
- [ ] PR är granskat av annan teammedlem
- [ ] Granskare är **INTE** samma som skribent
- [ ] Feedback är adresserad
- [ ] PR är uppdaterad med feedback

### Performance
- [ ] Database-queries är optimerade (ingen N+1)
- [ ] Back-testing < 2 sekunder för 500 instrument
- [ ] UI rendererar snabbt (< 1s initial load)

---

## 🔄 Vecko-Rytm för Sprint Execution

### Måndag
- **09:00-12:00:** Sprintplanering (se ovan)
- **13:00-17:00:** Kickoff + börja jobba på första issue

### Tisdag
- **09:00-12:30:** Utveckling
- **12:30-14:00:** PL-möte (ca 1,5h)
- **14:00-17:00:** Utveckling

### Onsdag
- **09:00-12:00:** Utveckling
- **13:00-17:00:** Utveckling eller individuella möten

### Torsdag
- **09:00-14:00:** Utveckling
- **14:00-15:00:** Standup/blocker-löpning
  - Vem är stuck? Vem kan hjälpa?
  - Kommer något block att påverka slutklocket?
  - Behöver vi skriva saker på detta klart före vecka-slutet?

### Fredag
- **08:00-17:00:** LIA-sök + dialoger (KOD FÖRBJUDET!)
- Dock kan du dokumentera feedback från veckan

---

## 📊 Sprint Metrics - Mät Framsteg

### Burndown Chart
Spåra detta under veckan:
- **Måndag 09:00:** Antal öppna issues
- **Mittväg (onsdag):** Hur många är stängda?
- **Fredag 16:00:** Burndown klart? Hur många issues stängda?

**Mål:** Ingen issues ska ta mer än 16h, så om du planerar 5 issues à 12h bör 2-3 vara stängda vid mittväg

### Velocity (Om Du Vill)
```
Sprint 2: 40 story points gjorda
Sprint 3: 45 story points gjorda
Sprint 4: 50 story points gjorda
→ Team blir snabbare när de får ritm
```

### Blockers & Risks
- **Tracking:** Spåra alla blockers i GitHub Project Board (labels: blockers, risk)
- **Lösa:** Dedikera tid att lösa blockers samma dag (inte nästa vecka!)
- **Preventera:** Om samma blocker uppstår två gånger, åtgärda root cause

---

## 🚨 Vad Gör Vi Om Vi Inte Hinner?

### Mitten av Veckan (Onsdag)
Om vi märker att vi inte hinner:

1. **Identifiera:** Vilka issues kommer inte bli klara?
2. **Prioritera:** Vilka är KRITISKA för denna veckas fokus?
3. **Minska:** Vad kan vi skjuta till nästa vecka?
4. **Ajustera:** Lägg om prioriteringar torsdag morgon

### Torsdag Kvall
- Några issue ska **INTE PUSHES** som half-done
- Bättre: Stäng 4 issues helt än 5 issues at 80%
- Flytta incomplete issues EXPLICIT tillbaka till backlog

### Rapporterad till PL
Tisdags-mötet ska vi kunna säga:
- "Vi gjorde THIS denna vecka ✅"
- "Vi skipade THAT för att fokusera på THIS ✅"
- "Nästa vecka gör vi THAT istället ✅"

**Inte:** "Vi jobbar på X men den är inte klar än" → detta är halvklar arbete

---

## 🏆 Sprint Retro - Efter Sprinten (Frivilligt)

**Tid:** 15 minuter, Fredag 16:30 (efter LIA-sök) eller Måndag 08:00

Frågor:

1. **Vad gick bra denna vecka?**
   - "Vi löste dependencyn snabbt"
   - "Bra kommunikation mellan frontend och backend"

2. **Vad gick dåligt?**
   - "Issue var inte ready-definierad, tog 2 timmar att förstå"
   - "Native-modulen var langsam, vi ska benchmarka tidigare"

3. **Vad bör vi prova nästa vecka?**
   - "Mer detaljerade acceptance criteria"
   - "Pair-programming för komplicerade features"
   - "Daglig 10-min standup för att fånga blockers tidigt"

**Notera:** Inte alla sprintar behöver retro. Bara när något kändes väldigt off.

---

## 📚 Mall: Sprint Backlog för Git Project Board

**Använd denna struktur när du skapar issues i GitHub:**

```markdown
## [TYPE] [Scope]: [Issue Title]

### Description
[Vad bygger vi? Varför?]

### Acceptance Criteria
- [ ] Criterion 1
- [ ] Criterion 2
- [ ] Criterion 3

### Blockers
- Waiting for: #20 (Backend API)
- Waiting for: #17 (Native FX module)

### Scope
- Frontend: [x] / [ ]
- Backend: [ ] / [x]
- Native: [ ] / [ ]

### Estimate
8h / 12h / 16h / 20h

### Ready Checklist
- [x] Issue is clearly defined
- [x] AC are measurable
- [x] No hidden dependencies
- [x] Team member assigned

### Branch
feature/#ISSUE-description

### Related
- Design: [Figma link]
- Architecture: DECISIONS.md [ref]
- Similar issue: #XX
```

---

## 🎓 Viktigt: Tävlingen ≠ Betyget

Din betyg BYGGER PÅ:
- Slutleverans (vad du gjort)
- 17 Kursmål (hur bra du gjort det)
- Din Git-historia (vem gjorde vad)

Tävlingsresultatet påverkar **INTE** betyget.

**Fokusera på att:**
1. ✅ Uppfylla alla kursmål
2. ✅ Leverera fungerande system
3. ✅ Dokumentera ordentligt
4. ✅ Spåra individuella bidrag i Git

Vinna tävlingen är bonus, inte målet.

---

**Senast uppdaterad:** 2026-09-04  
**Ansvarig:** Team 1
