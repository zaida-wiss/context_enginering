# 👥 Team-Möte Template (Backend/Frontend/Native)

**Denna guide hjälper ett specifikt team att planera och facilitera sitt eget möte med AI-stöd.**

Använd denna för:
- Backend-möten (endast backend-utvecklare)
- Frontend-möten (endast frontend-utvecklare)
- Native-möten (endast native-utvecklare)

---

## 🎯 Syfte med Team-Möten

**Sprintmöten:** Strategiska (VHAT ska vi göra? Vilka är beroenden?)
**Team-möten:** Taktiska (HOW implementerar vi? Arkitektur? Tekniska detaljer?)

### Team-Möten Handlar Om:
- ✅ Tekniska arkitektur-beslut för detta team
- ✅ Code review & refactoring-strategi
- ✅ Implementerings-detaljer
- ✅ Problem-lösning för team-specifika blockers
- ✅ Lärande & knowledge-sharing

---

## 📋 Hur Du Använder Denna Guide

### Steg 1: Be AI om Hjälp

**Kopiera detta till AI tillsammans med denna fil:**

```
TEAM MÖTE PREP:
===============

Läs: _ai_guides/TEAM_MEETING_TEMPLATE.md

Team: [Backend / Frontend / Native]
Möte-typ: [Architecture / Code Review / Problem-solving / Knowledge-sharing]

Denna vecka gjorde vi:
[Copy-pasta från git log - bara detta teams commits]

Denna vecka jobbar vi på:
[Vilka issues jobbar vi på?]

Problem/Frågor vi ska diskutera:
1. [Fråga 1]
2. [Fråga 2]
3. [Fråga 3]

Nu: Förbered mötet för [Team]
```

### Steg 2: AI Förbereder

AI kommer då att:
- Läsa denna teams commits
- Förstå vad ni arbetar på
- Föreslå diskussions-punkter
- Presentera agenda för mötet

### Steg 3: Mötet Börjar

Du säger: "Kör team-möte" eller "Facilitera [Backend/Frontend/Native]-möte"

AI faciliterar enligt samma principer som sprintmöten:
- ✅ Ställer frågor
- ✅ Involverar alla
- ✅ Dokumenterar beslut
- ✅ Presenterar nästa steg

---

## 🏗️ Team-Möte Agenda (Flexibel - 30-60 min)

### 1. OPENING (2 min)
```
"Välkommen till [Backend/Frontend/Native]-mötet!

Vi ska diskutera:
1. [Punkt 1]
2. [Punkt 2]
3. [Punkt 3]

Denna vecka har vi gjort: [Summary]
Vi jobbar på: [Issues]

Okej, vad tycker ni om punkt 1?"
```

### 2. MAIN DISCUSSION (20-45 min)
**För varje punkt:**
- ✅ Presentera problem/fråga
- ✅ Diskutera möjliga lösningar
- ✅ Fatta beslut eller planera nästa steg
- ✅ Dokumentera beslut
- ✅ Fråga "Är vi klara här?"

### 3. DECISIONS & ACTION ITEMS (5 min)
```
AI summerar:
"Vi beslutade:
- [ ] Decision 1
- [ ] Decision 2

Action items:
- [ ] Person A gör X imorgon
- [ ] Person B gör Y innan nästa möte

Är vi klara eller något mer?"
```

---

## 📚 Möte-Typer: Vad Vi Kan Diskutera

### Type 1: Architecture & Design
```
Exempel-frågor:
- "Hur ska vi strukturera denna modul?"
- "Vilken design-pattern passar här?"
- "Hur integrerar vi detta med övriga systemet?"

Resultat: Arkitektur-beslut, nästa steg klar
```

### Type 2: Code Review & Refactoring
```
Exempel-frågor:
- "Hur ska vi refaktorera denna komponent?"
- "Vilka patterns bör vi följa?"
- "Vad tycker ni om denna kod-struktur?"

Resultat: Code review-feedback, refactoring-plan
```

### Type 3: Problem-Solving
```
Exempel-frågor:
- "Vi är stuck på detta problem - vad kan vi göra?"
- "Hur debuggar vi denna bug?"
- "Vilken är bästa lösningen här?"

Resultat: Lösning identifierad, nästa steg klar
```

### Type 4: Knowledge-Sharing
```
Exempel-frågor:
- "Låt mig förklara hur denna teknik fungerar"
- "Vilka best practices bör vi följa?"
- "Vad lärde ni er denna vecka?"

Resultat: Hela teamet förstår, shared knowledge
```

---

## 💬 Faciliterings-Principer (Samma Som Sprint-Möten)

**AI ska:**
- ✅ Ställa öppna frågor
- ✅ Involvera alla
- ✅ Dokumentera beslut
- ✅ Fråga innan nästa punkt
- ✅ Pausa för reflektion

**AI ska INTE:**
- ❌ Presentera utan input från teamet
- ❌ Rusa genom diskussionen
- ❌ Ignorera tekniska detaljer (det är POÄNGEN här)

---

## 🎯 Exempel: Backend-Möte

```
Team Lead (Backend): "Förbered backend-möte"

AI: "Backend-möte klar!
    Denna vecka gjorde ni: Issue #52 API, Issue #57 tests
    Ni jobbar på: #53 metrics
    
    Föreslagna diskussions-punkter:
    1. Arkitektur för metrics-service
    2. Database-optimization för portfolio-queries
    3. Error-handling strategi
    
    Okej, shall we start?"

Backend Team börjar mötet
Backend Dev 1: "Ja, vi måste diskutera metrics-service arkitektur"
Backend Dev 2: "Jag tänkte entity-mapping pattern"
AI: "Interessant! Vad tänker du på med entity-mapping här?"
Backend Dev 2: "Vi mappa direkt från DB till API DTO"
Backend Dev 1: "Men det är tight coupling med DB-schema"
AI: "Right - då måste vi ha en abstraction layer?
    Vad tycker ni är bästa approach här?"
[Discussion]
AI: "Så vi är överens om: Vi använder repository pattern
    med entity mapper i mellan. Backend Dev 2 - kan du skissa
    detta på whiteboard och push to branch?"
Backend Dev 2: "Klar"
AI: "Punkt 1 done. Nästa punkt: database optimization?"
```

---

## 📝 Dokumentation från Team-Möte

Efter mötet dokumentera:

```
TEAM MÖTE SAMMANFATTNING - [TEAM]
==================================

Datum: [Torsdag]
Deltagare: [Alla team-medlemmar]

🎯 DISKUTERAT:
1. Arkitektur för X
2. Refactoring av Y
3. Problem-lösning för Z

✅ BESLUT:
- Decision 1: Vi använder pattern X
- Decision 2: Vi refaktorerar modul Y såhär
- Decision 3: Vi löser problem Z genom

📝 ACTION ITEMS:
- [ ] Person A: Skissa arkitektur (idag)
- [ ] Person B: Refaktor modul Y (innan nästa möte)
- [ ] Person C: Implementera lösning Z (denna vecka)

💡 LÄRDOMAR:
- Vi lärde oss: X
- Vi bör följa: Y

📅 NÄSTA MÖTE:
- [Samma tid nästa vecka eller när nästa behov uppstår]
```

---

## ⏱️ Mötes-Längd (Flexibel)

- **30 min:** Ett två tekniska frågor, fokuserat
- **60 min:** Större arkitektur-diskussion, refactoring-planering
- **90 min:** Djupare problem-lösning, design-workshop

**Regel:** Håll mötet så kort som möjligt men så långt som behövs!

---

## 🚀 Snabbversion: Team-Möte på 3 Minuter

**Du säger till AI:**
```
Team: Frontend
Frågor:
1. Ska vi refaktorera komponenten så?
2. Vilken CSS-approach passar här?

Facilitera mötet
```

**AI faciliterar mötet** med samma struktur - bara snappare.

---

## 📚 Relaterade Filer

- **AI_TEAMLEADER.md** - Faciliterings-principer
- **MEETING_THURSDAY.md** - Sprint möte (för hela teamet)
- **MEETING_MONDAY.md** - Sprint planning (för hela teamet)

---

## ✅ Checklista: Innan Du Startar Team-Möte

- [ ] Är detta en teknisk diskussion? (Då passar det här)
- [ ] Har du några specifika frågor? (Lista dem)
- [ ] Är detta team-specifikt? (Inte sprintmöte-material?)
- [ ] Har du 30+ minuter? (Eller är det snabb fråga?)

**Då:** Ber du AI facilitera team-mötet.

---

*Last Updated: 2026-09-04*  
*Purpose: Team-specific technical meetings*  
*Facilitator: AI (Same principles as sprint meetings)*
