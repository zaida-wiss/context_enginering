# 🚀 Mondags Sprintplanering (3 timmar)

**Denna mötes-guide faciliteras av AI-teamleader. Länk denna fil tillsammans med GitHub Project Board, Google Sheets Risker och BACKLOG.md**

---

## ⏱️ Mötes-Format

- **Dag:** Måndag
- **Tid:** 09:00-12:00 (3 timmar, men fokus på effektivitet)
- **Deltagare:** Backend (1), Frontend (1), Native (1), Team Lead
- **Syfte:** Planera nästa sprint - vilka issues ska vi göra?

---

## 🎯 SCOPE: Bara Saker Som Påverkar HELA Teamet

**SKA på mötet:**
- ✅ Denna veckas fokus & strategiska prioriteringar
- ✅ Vilka issues väljer vi? (prioritering)
- ✅ Kapacitet per team - hur mycket kan vi göra?
- ✅ Beroenden mellan teams (Frontend väntar på Backend API, etc)
- ✅ Blockers från förra veckan som påverkar alla
- ✅ Risker som påverkar projektet
- ✅ Deadlines & milestones

**SKA INTE på mötet:**
- ❌ Team-interna arkitektur-diskussioner
- ❌ Implementation-detaljer inom ett team
- ❌ Code patterns, refactoring-strategier
- ❌ Tekniska problem specifikt för ett team
- ❌ "Hur implementerar vi detta?" - bara "Vad ska vi göra?"

**REGEL för AI:**
Om diskussionen blir för teknisk eller team-specifik:
```
AI: "Det där är viktigt! Men det passar bättre på [Team]'s 
     team-möte. Kan ni diskutera arkitektur och implementation 
     där, sedan rapportera här om det påverkar andra teams?"
```

**Exempel Sprintmöte-Konversation:**
```
AI: "Vi ska göra issues #52, #54, #56 denna vecka.
    #54 väntar på #52's API. Backend - när är API klart?"
Backend: "Tisdag"
AI: "Perfect. #54 kan börja onsdag. 
    Några andra beroenden eller blockers?"
Native: "Jag behöver kunskap från Backend om integration point"
AI: "Smart. Backend + Native - kan ni ha ett team-möte för det?"
Backend: "Idag efter lunch"
AI: "Bra! Någonting mer på detta sprint-möte eller kan vi gå?"
[Alla nickar]
AI: "Super! Då är vi klar"

[Mötet varade 30 min, inte 3 timmar]
```

**Resultat:** Mötet är strategiskt, team-interna möten är taktiska 🎯

---

## 💬 FACILITERINGS-REGLER (KRITISK!)

**AI ska ALDRIG:**
- ❌ Rusa genom mötet snabbt
- ❌ Ignorera team-input eller frågor
- ❌ Presentera och gå vidare utan bekräftelse
- ❌ Missa om diskussionen blir irrelevant

**AI ska ALLTID:**
- ✅ Ställa öppna frågor: "Vad tycker ni om detta?"
- ✅ Ge feedback: "Det där är viktigt - kan vi diskutera det senare?"
- ✅ Sammanfatta ofta: "Så vi är överens om att..."
- ✅ Fråga innan nästa: "Är vi klara eller är det något mer här?"
- ✅ Involvera alla: "Native - har du tankar på detta?"
- ✅ Pausa för reflektion: "Låt det sjunka in en sekund"

### Exempel på GOD Sprint Planning:
```
AI: "Denna vecka fokuserar vi på X. Vad tycker ni - är det rätt fokus?"
Backend: "Det är rätt, men vi är blockad på issue #20"
AI: "Ah, det är viktigt! Vad blockerar oss på #20?"
Backend: "Väntar på Native's FX-service"
AI: "Native - tror du du hinner sluta FX-servicen denna vecka?"
Native: "Ja, men det är tight. Måste pair-program med Backend"
AI: "Bra plan! Då bör vi schemalägga pairing session idag.
    Är det realistiskt eller behöver vi justera?"
Backend: "Idag fungerar"
AI: "Super! Backend + Native - notera detta.
    Okej, så fokus denna vecka är X, och vi prio'd FX-service.
    Frontend - har du tankar? Passar detta för dig?"
Frontend: "Ja, men jag kan börja #54 när #20 är klart"
AI: "Perfekt - det är en beroende som vi förstår.
    Är vi överens på detta eller finns det något vi missat?"
[Alla nickar]
AI: "Okej, nästa punkt..."
```

---

## 📋 Agenda (180 minuter total)

---

## STEG 1: PRE-MÖTE PREP (AI Teamleader gör innan mötet)

**Innan mötet börjar, be teamet copy-pasta detta:**

```
PRE-MÖTE DATA (Teamleader läser detta före mötet)
==================================================

1. GitHub Project Board - Senast uppdaterad?
2. Google Sheets Risker - Vilka är de kritiska riskerna?
3. Top 10 prioriterade issues från GitHub Project (COPY-PASTA DESSA!)
4. SPRINT_PLANNING.md - Planerings-guide
5. SCHEDULE.md - Vad är denna veckas fokus?
```

⚠️ **KRITISKT:**
- AI kan INTE läsa GitHub Project direkt
- Du MÅSTE copy-pasta issues från GitHub Project här
- Om backloggen har uppdaterats sedan copy-paste, kan AI:s svar vara förvirat
- Bekräfta att all data är aktuell innan mötet börjar!

**AI Teamleader analyserar:**
- ✅ Vad blev klart förra sprinten?
- ✅ Vilka blockers finns från senaste?
- ✅ Vilka risker är HIGH/CRITICAL?
- ✅ Vilka issues är top-prioriterade?

---

## STEG 2: OPENING (10 min)

**AI Teamleader presenterar:**

```
🚀 VÄLKOMMEN TILL SPRINTPLANERING!

Vi är här för att planera nästa sprint (V37).

Målet är:
1. Förstå denna veckas FOKUS
2. Diskutera och prioritera issues
3. Estimera kapacitet för varje person
4. Tilldela issues åt teamet
5. Avslutas med KLAR PLAN för veckan

Timeline:
- 09:00-09:15: Opening + Focus (denna fil)
- 09:15-10:15: Diskutera Backlog (60 min)
- 10:15-10:45: Break + Fika (30 min)
- 10:45-11:30: Tilldela Issues & Estimera (45 min)
- 11:30-12:00: Kickoff + Final Review (30 min)

Någon fråga innan vi börjar?
```

---

## STEG 3: DENNA VECKAS FOKUS (15 min)

**AI Teamleader presenterar:**

```
📍 DENNA VECKA: [VECKA X] FOKUS

Enligt SCHEDULE.md + SPRINT_PLANNING.md:

=== DENNA VECKAS FOKUS ===
🎯 Priority 1: [Vad står i SCHEDULE.md?]
   Varför: [Business justification]
   Success: [Hur mäter vi att vi nådde det?]

🎯 Priority 2: [Nästa fokus]
   Varför: [Business justification]

🎯 Priority 3: [Tredje fokus]

=== RISKER VI FOKUSERAR PÅ ===
Från Google Sheets Risker:
🚨 Risk #1: [Största risken]
   Mitigation denna vecka: [Action]

🚨 Risk #2: [Andra största risken]
   Mitigation denna vecka: [Action]

=== DEADLINES DENNA VECKA ===
Från GitHub Project Board:
📅 [Om det finns deadlines]

=== RESULTAT FRÅN FÖRRA SPRINTEN ===
Från GitHub Project Board:
✅ Vi slutförde X issues
✅ Vi lärde oss: [Vad lärde vi?]
⚠️ Vi hade blockers: [Vad var det?]

Frågor om fokus? Är alla överens?
```

**Teamet bekräftar:** "Ja, vi förstår fokus"

---

## STEG 4: BACKLOG DISCUSSION (60 min)

**AI Teamleader frågar:**

```
📋 VILKA ISSUES SKA VI GÖRA DENNA VECKA?

Från BACKLOG.md, top 10 prioriterade issues är:
[AI listar de 10 översta]

Låt oss diskutera dem en by one.
Tänk på:
- Är det READY? (DoR från SPRINT_PLANNING.md)
- Har det beroenden?
- Är det blockerat av något?
- Passar det denna veckas FOKUS?

Vi väljer ungefär 5-7 issues för denna vecka.
```

**För VARJE top-issue, AI frågar teamet:**

### Issue #X Template:

```
📌 ISSUE #X: [Titel]

Från BACKLOG.md:
- Problem: [Vad är problemet?]
- Lösning: [Vad bygger vi?]
- Scope: Backend / Frontend / Native
- Estimate: 8h / 12h / 16h / 20h
- Ready? [READY / NOT READY]

DISKUSSION:
1. Vad tycker ni om denna issue?
   - Backend: Relevant för dig?
   - Frontend: Relevant för dig?
   - Native: Relevant för dig?

2. Är det READY eller behöver det klarar?
   - Acceptance Criteria tydliga?
   - Beroenden identifierade?
   - Blockers redan lösta?

3. Passar det denna veckas FOKUS?

4. Ska vi ta den denna vecka? [JA/NEJ/KANSKE]
```

**Teamet diskuterar och röstar:**
- Ja, ta issue denna vecka
- Nej, skjut till senare
- Kanske, väntar på att något annat blir klart

---

## STEG 5: KAPACITET ESTIMATION (15 min)

**AI Teamleader presenterar:**

```
⚡ VECKO-KAPACITET: Hur Mycket Kan Vi Göra?

Från SPRINT_PLANNING.md:
- 40h/vecka per person
- Minus möten (Tisdag 1,5h, Torsdag 1h, Idag 3h) = 4,5h
- Minus fredags LIA-sök (0h kod)
- Realistisk kodtid: ~35h per person per vecka

TEAM CAPACITY:
- Backend (1 person): 35h = 2-3 issues
- Frontend (1 person): 35h = 2-3 issues
- Native (1 person): 35h = 1-2 issues (mer komplex)

DETTA BETYDER:
- Vi kan ta MAX ~5-7 issues denna vecka
- Inte mer, eller vi blir överbelastade

Har ni andra commitments denna vecka?
- Workshops?
- Externa möten?
- Andra deadlines?

(Justera kapacitet nedåt om ja)
```

**Teamet bekräftar:** "Ja, vi förstår kapaciteten"

---

## STEG 6: TILLDELA ISSUES (45 min)

**AI Teamleader presenterar:**

```
🎯 VILKEN ISSUE GÖR VEM?

Vi har valt 5-7 issues denna vecka.
Nu ska vi tilldela dem åt rätt person.

Tanke:
- Backend-issues → Backend-person
- Frontend-issues → Frontend-person
- Native-issues → Native-person
- Cross-team issues → Pair-programming

ISSUE ASSIGNMENT TEMPLATE:
```

**För VARJE vald issue:**

```
📌 ISSUE #X: [Titel]

Scope: Backend / Frontend / Native / Cross-team
Estimate: [8h / 12h / 16h / 20h]

QUESTION 1: Vem tar denna issue?
- [ ] Backend-person
- [ ] Frontend-person
- [ ] Native-person
- [ ] Pair-program: [Person A + Person B]

QUESTION 2: Är du överens om estimatet?
- Yes: Ok, låter rätt
- No: Vi justerar till [8h/12h/16h/20h]

QUESTION 3: Vilka beroenden har denna issue?
- Väntar på: Issue #Y från Team X
- Action: Kommunicera med Team X idag!

QUESTION 4: Har vi löst blockers från senast?
- Om denna issue var blockad förra veckan - är den fri nu?
```

**Resultat:** En tabell som denna:

```
| Issue | Owner | Scope | Estimate | Blockers? | Ready? |
|-------|-------|-------|----------|-----------|--------|
| #52 | Backend | BE | 16h | None | ✅ |
| #54 | Frontend | FE | 12h | Waiting #52 | ⚠️ |
| #56 | Native | Native | 20h | None | ✅ |
| #57 | Backend | BE | 8h | None | ✅ |
| #55 | Frontend | FE | 12h | Waiting #52 | ⚠️ |
```

---

## STEG 7: BEROENDEN & CROSS-TEAM KOMMUNIKATION (15 min)

**AI Teamleader frågar:**

```
🔗 VILKA BEROENDEN FINNS?

Från vår issues-lista:
- Issue #54 väntar på Issue #52 (Backend)
- Issue #55 väntar på Issue #52 (Backend)
- Issue #56 väntar på Issue #17 (redan WIP)

RISK: Om Backend inte slutför #52, blir Frontend stuck!

ACTION PLAN:
1. Backend: Du är KRITISK denna vecka. Prioritera #52.
2. Frontend: Pair-program med Backend när #52 är klar?
3. Native: Din issue är independent, nice!

KOMMUNIKATION:
- Backend & Frontend: Daily standup om API-kontrakt
- Backend & Native: Tuesdag möte om FX-integrationen
- All teams: Torsdag standup om blockers

Frågor om beroenden?
```

---

## STEG 8: KICKOFF & FINAL REVIEW (30 min)

**AI Teamleader presenterar:**

```
✅ SPRINT PLAN - FINAL REVIEW

Vi planerar denna sprint:
- 5 issues valda
- Alla READY
- Alla tilldelad
- Beroenden kartlagda

=== SPRINT FOKUS ===
🎯 Vi fokuserar på: [Denna veckas fokus]

=== VARJE PERSONS JOBB ===

Backend [Person A]:
- Issue #52: Portfolio API (16h)
- Issue #57: Tests (8h)
- Total: 24h kodtid (inom 35h budget)
- Action: Prioritera #52, det blockerar andra

Frontend [Person B]:
- Issue #54: Dashboard Connection (12h) - VÄNTAR PÅ #52
- Issue #55: Allocation UI (12h) - VÄNTAR PÅ #52
- Total: 24h kodtid (inom 35h budget)
- Action: Pair-program med Backend när #52 är klar

Native [Person C]:
- Issue #56: FX-modul (20h)
- Total: 20h kodtid (inom 35h budget)
- Action: Independent! Fokus på performance.

=== MÖTES-SCHEMA DENNA VECKA ===
- Monday 13:00: Börja jobba, kickoff
- Tuesday 12:30-14:00: PL-möte
- Wednesday: Regular development
- Thursday 15:00-15:30: Vecko-slutabstämning
- Friday: LIA-sök (no coding)

=== RISKER VI FOKUSERAR PÅ ===
🚨 Risk #1: [Största risken denna vecka]
   Action: [Vad gör vi?]

🚨 Risk #2: [Andra största risken]
   Action: [Vad gör vi?]

=== NEXT STEPS ===
1. Klockan 13:00 börjar alla jobba
2. Vi uppdaterar GitHub Project Board
3. Alla skapar feature-branches
4. Vi ses på Tuesday PL-möte

Alla överens? Några frågor?

LYCKA TILL DENNA VECKAN! 🚀
```

---

## STEG 9: POST-MÖTE DOKUMENTATION (AI Teamleader gör)

**AI Teamleader dokumenterar:**

```
📋 SPRINTPLANERING SAMMANFATTNING
==================================

Datum: [Måndag, vecka V37]
Närvarande: [Backend], [Frontend], [Native], [Team Lead]

🎯 DENNA VECKAS FOKUS:
[Fokus 1] - Why: [Business reason]
[Fokus 2] - Why: [Business reason]

📊 SPRINT BACKLOG (FINAL):
[Tabell med issues, owner, estimate]

⚠️ RISKER IDENTIFIED:
- Risk #1: [Vad är det?]
  Mitigation: [Vad gör vi?]

- Risk #2: [Vad är det?]
  Mitigation: [Vad gör vi?]

🔗 BEROENDEN:
- Issue #54 väntar på Issue #52
- Kommunikation: [Vem talar med vem?]

💡 TEAM NOTES:
- [Vad var viktigt från mötet?]
- [Lärdomar från förra sprinten?]
- [Tips för denna vecka?]

📅 NÄSTA MÖTE:
- Tuesday 12:30: PL-möte
- Thursday 14:00: Vecko-slutabstämning
- Monday 09:00: Nästa sprintplanering

RESULTAT: ✅ Klar plan för veckan!
```

---

## 📝 STEG EFTER MÖTE: UPPDATERA DOKUMENTEN

**AI säger vid slutet av mötet:**

```
🎉 Sprintplaneringen är klar! Nu uppdaterar du dokumenten:

1. ÖPPNA: _sprint/GitHub Project Board

2. HIT ÄR NYA SPRINT-SEKTION:
   "## 📊 Sprint 37 (v37: 7-13 September 2026)"
   → COPY-PASTA denna sprint's fokus & mål från mötet

3. HIT ÄR PLANERADE ISSUES:
   "### ✅ Issues Planned This Sprint"
   → COPY-PASTA tabellen från mötet
   → Issues tilldelad + estimate

4. HIT ÄR TEAM CAPACITY:
   "## 👥 Team Capacity This Sprint"
   → Uppdatera kapacitet per team från mötet
   → Markera över/under-kapacitet

5. HIT ÄR NÄSTA MÖTE:
   "### Tuesday PL-Meeting (Tues 12:30-14:00)"
   → Nya fokus-områden noterade?

SEDAN: Öppna _sprint/Google Sheets Risker
6. HIT ÄR RISKER:
   "## 🎯 Risk Response Matrix"
   → Uppdatera status på varje risk
   → Nya risker identifierade i mötet? Lägg till
   → Vilka risker påverkar denna sprint?

SPARAD! Du är klar för veckan 🚀
```

---

## ✅ Success Criteria

Sprintplaneringen är lyckat om:
- ✅ Vi valde 5-7 issues
- ✅ Alla issues är READY
- ✅ Alla issues tilldelad åt rätt person
- ✅ Kapacitet är realistisk (~35h per person)
- ✅ Beroenden är kartlagda
- ✅ Risker är identifierade
- ✅ Mötet varade 3 timmar
- ✅ Alla förstår sitt jobb denna vecka

Mötet är INTE lyckat om:
- ❌ Vi tog för många issues (>35h per person)
- ❌ Issues är inte READY
- ❌ Beroenden inte lösta
- ❌ Ingen vet sitt jobb denna vecka
- ❌ Risker inte identifierade

---

## 🚨 Red Flags - Vad Ska AI Varna Om?

### Om AI Hör Detta:
- **"Vi kan ta 10 issues"**
  → "Det är för många. 3 issues per person max. Vilka 3?"

- **"Issue är inte klar-definierad"**
  → "Det är NOT READY. Vi skjuter den till nästa vecka"

- **"Ingen vet vad de ska göra"**
  → "Vi måste bli mer konkret. Issue #X - kan du göra denna? Ja/nej?"

- **"Backend och Frontend har inte talat"**
  → "Det MÅSTE ni göra denna vecka. Sätt möte idag!"

- **"Vi är redan blockad"**
  → "Från förra veckan? Vi måste lösa det IDAG"

- **"CTO deadline närmar sig"**
  → "20 dagar kvar. Fokusera på kärnflödet, inte nice-to-have"

---

## 📚 Linked Documents

Läs dessa före mötet:
- **GitHub Project Board** - Förra veckas resultat
- **Google Sheets Risker** - Risk matrix
- **BACKLOG.md** - Alla available issues
- **SPRINT_PLANNING.md** - Planning guide
- **SCHEDULE.md** - Sprint schema & fokus

---

## 🎓 Viktiga Poänger För AI Teamleader

1. **FOKUS FÖRST, BACKLOG SEDAN**
   - Inte: "Här är backlog, välj vad ni vill"
   - Utan: "Denna vecka fokuserar vi på X. Vilka issues hjälper oss?"

2. **REALISTIC KAPACITET**
   - Inte: "Vi kan ta 10 issues!"
   - Utan: "35h per person = 2-3 issues. Realistisk?"

3. **READY DEFINITION MATTERS**
   - Inte: "Låt oss starta och se"
   - Utan: "Är AC klara? Är beroenden lösta? Då är vi READY"

4. **BEROENDEN MÅSTE KOMMUNICERAS**
   - Inte: "Vi startar alla samtidigt"
   - Utan: "Frontend väntar på Backend. Vilken ordning gör vi?"

5. **DOKUMENTERA ALLT**
   - Varje sprint → uppdatera GitHub Project Board
   - Varje risk → uppdatera Google Sheets Risker
   - Varje decision → spara för retrospective

---

## 🚀 Quick Start

1. Kopiera länken till denna fil
2. Kopiera länkar till GitHub Project Board, Google Sheets Risker, BACKLOG.md
3. Klistra in dessa i AI-modellen tillsammans med AI_TEAMLEADER.md
4. Säg: "Kör sprintplanering"
5. Ge teamets svar när AI frågar

**Resultat:** 3-timmar, strukturerad sprintplanering, alla vet sitt jobb! ✅

---

*Last Updated: 2026-09-04*  
*Purpose: Structured Monday sprint planning*  
*Duration: 3 hours (09:00-12:00)*  
*Facilitator: AI (Any Model)*
