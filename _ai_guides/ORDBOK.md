---
name: ordbok
description: Branschterminologi och förklaringar för presentationen — växande ordbok
metadata:
  type: reference
  updated: 2026-09-13
---

# 📚 ORDBOK — Branschterm & Förklaringar

**Denna ordlista växer med presentationen. Varje term som används på en slide ska förklaras här.**

Presentationen markerar nya termer med 📚 första gången de dyker upp, länkad till denna ordbok.

---

## 🏃 AGILE & SPRINTPLANERING

### Sprint
**Vad:** En tidsperiod (ofta 1-2 veckor) då teamet fokuserar på att färdigställa specifika uppgifter.

**Exempel:** "Teamet arbetar i en tvåveckorssprint med ett tydligt start- och slutdatum."

**Varför det spelar roll:** Sprinter skapar fokus och gör det möjligt att planera vad som ska göras.

---

### Sprintmål
**Vad:** Det konkreta måltagget för sprinten. Vad ska vi ha färdigställt denna sprint?

**Exempel:** "Sprintmålet är att användaren ska kunna logga in och slutföra det viktigaste kärnflödet."

**Varför det spelar roll:** Utan ett mål vet teamet inte när sprinten är lyckad.

---

### MVP (Minimum Viable Product)
**Vad:** Den enklaste versionen av produkten som löser kundens huvudproblem. Ingenting onödigt, bara det som behövs.

**Exempel:** "MVP:n innehåller registrering, inloggning och den viktigaste användarresan. Avancerad export väntar."

**Varför det spelar roll:** Gränser arbetet och gör det genomförbart. Vi bygger det viktigaste först.

---

### Definition of Done (DoD)
**Vad:** En checklista över vad som behövs för att en uppgift är FAKTISKT färdig. Inte bara "kod skriven", utan också testerad, reviewad, dokumenterad.

**Exempel:** En DoD kan vara:
- ✅ Koden är skriven
- ✅ Minst 70% test-coverage
- ✅ Code review godkänd
- ✅ Dokumentation uppdaterad
- ✅ Deployad till test-miljön

**Varför det spelar roll:** Utan DoD vet vi aldrig om något är färdigt eller bara "nästan".

---

### Backlog
**Vad:** En lista över allt arbete som behöver göras, sorterad efter prioritet.

**Exempel:** "Backloggen innehåller 50 issues. De översta 7 är prioriterad för denna sprint."

**Varför det spelar roll:** Backloggen visar hela vägen framåt. Vi jobbar från toppen ned.

---

### Blocker / Blockerad
**Vad:** En uppgift som är STOPPAD för att den beror på något annat som inte är färdigt ännu.

**Exempel:** "Team B väntar på ett verifierat kontrakt från Team A innan integrationsarbetet kan fortsätta."

**Varför det spelar roll:** Blockers är högsta prioritet att lösa. Teamet kan inte jobba innan de är lösta.

---

## 💻 TEKNIK & KODARBETE

### API-kontrakt
**Vad:** En överenskommelse mellan två system om hur de pratar med varandra. Vilken information skickas? I vilket format?

**Exempel:** "En klient och en tjänst enas om att `GET /items` returnerar dokumenterade fält och typer i JSON."

**Varför det spelar roll:** Om Frontend och Backend har olika idéer om kontraktet, funkar inte systemet.

---

### Branch (Git-branch)
**Vad:** En egen arbets-kopia av koden där du gör ändringar utan att påverka huvudkoden.

**Exempel:** "Alex arbetar på `feature/profile` och Sam på `feature/search`. De kan utveckla parallellt utan att skriva över varandra."

**Varför det spelar roll:** Branches låter flera personer jobba på samma kodbase utan att krasha varandra.

---

### Merge / Mergad
**Vad:** Att kombinera ändringar från en branch tillbaka till huvudkoden (develop/main).

**Exempel:** "En färdig feature-branch är mergad till projektets integrationsbranch och ingår nu i den gemensamma koden."

**Varför det spelar roll:** Merge betyder att arbetet är framförhandlat och testat nog för att vara officiell.

---

### Pull Request (PR)
**Vad:** En förfrågan om att merga din kod. Andra tittar på den, reviewar den, och säger ja/nej.

**Exempel:** "Sam har öppnat en PR för en ny komponent. Review är godkänd och ändringen är redo att mergas."

**Varför det spelar roll:** PRs säkerställer att koden är bra innan den blir officiell.

---

### Code Review
**Vad:** Att en annan utvecklare läser din kod och säger om det är bra, eller om det behövs ändringar.

**Exempel:** "Alex reviewade Sams valideringskod och föreslog en enklare lösning innan merge."

**Varför det spelar roll:** Code review fångar fel och delar kunskap mellan teamet.

---

### Commit
**Vad:** En "sparning" av ditt arbete. Du sparar en version av koden med ett meddelande om vad du gjorde.

**Exempel:** "Alex gjorde en commit: `Add validation helper`."

**Varför det spelar roll:** Commits visar vad som gjordes och möjliggör att gå tillbaka om något går fel.

---

### Test-coverage
**Vad:** Hur stor del av koden är testad med automatiska tester.

**Exempel:** "Vi har 68% test-coverage. Det betyder 68% av koden har tester som verifierar att det fungerar."

**Varför det spelar roll:** Högre coverage = mindre risk för buggar när vi gör ändringar.

---

### Accessibility (A11y)
**Vad:** Att alla kan använda systemet, även människor med funktionshinder. Till exempel: ska gå att använda med tangentbord, ska funka för dövblinda, etc.

**Exempel:** "Denna button är inte accessible — texten är för liten för personer med nedsatt syn."

**Varför det spelar roll:** Rättvisa. Alla ska kunna använda systemet.

---

### Refactoring
**Vad:** Att skriva om kod för att göra den bättre, utan att ändra vad den gör. Rent arbete, ingen ny funktion.

**Exempel:** "Anna refaktorerar core-modulen. Koden gör samma sak, men är nu lättare att förstå och underhålla."

**Varför det spelar roll:** Refactoring minskar "tech debt" — gamla lösningar som blir dyra att underhålla.

---

### End-to-end (E2E)
**Vad:** Ett flöde som går från början till slut av systemet — från användarens input till det resultat användaren ser.

**Exempel:** "Vi testar end-to-end: användaren skickar ett formulär → servern behandlar datan → en bekräftelse visas."

**Varför det spelar roll:** End-to-end test visar att systemet faktiskt löser användarens problem.

---

### Deploy / Deployment
**Vad:** Att flytta kod från utvecklingsmiljön till produktionen (där riktiga användare använder den).

**Exempel:** "Vi deployade version 2.1 till produktion på torsdag. Användare använder den nu."

**Varför det spelar roll:** Deployment är när arbetet faktiskt når användarna.

---

## 🎯 STATUS & TEMPO

### On Track
**Vad:** Vi ligger på schema. Vi kommer att nå våra mål inom tidsplanen.

**Exempel:** "Team A är on track och väntas nå sprintmålet enligt den verifierade planen."

**Varför det spelar roll:** Visar att vi inte behöver oroa oss eller justera.

---

### Slight Delay
**Vad:** Vi är lite efter schema, men inget kritiskt. Vi kan förmodligen komma ikapp.

**Exempel:** "Team B har en mindre försening och behöver uppdatera sin verifierade leveransplan."

**Varför det spelar roll:** Signalerar att vi behöver uppmärksamhet, men det är inte panik än.

---

### Critical
**Vad:** En allvarlig avvikelse från planen. Vi kommer INTE nå målet utan åtgärd.

**Exempel:** "Team C har en kritisk blockerare som stoppar ett nödvändigt integrationssteg."

**Varför det spelar roll:** Kritisk status betyder att vi behöver agera NU, eller projektet misslyckas.

---

## 📖 HUR MAN ANVÄNDER DENNA ORDBOK

**PRESENTATIONEN:**
Varje nytt branschterm markeras 📚 på sliden.

**LÄSAREN:**
1. Du ser ordet markerat 📚
2. Du slår upp det här i ORDBOK.md
3. Du förstår vad ordet betyder och varför det spelar roll
4. Du kan fortsätta följa presentationen

**RESULTATET:**
Du bygger ordförråd organiskt genom möten. Efter några möten använder du dessa ord naturligt.

---

## 📝 TILLÄGG AV NYA TERMER

**När en ny term läggs till presentationen, läggs den också här.**

Ordbok uppdateras före mötet så att läsarna kan förstå ordet.

Format för ny term:
```
### Termens namn
**Vad:** [En mening som förklarar vad ordet betyder]
**Exempel:** [Ett syntetiskt, projektneutralt exempel]
**Varför det spelar roll:** [Varför användaren behöver förstå detta]
```

---

**Senast uppdaterad:** 2026-09-21
