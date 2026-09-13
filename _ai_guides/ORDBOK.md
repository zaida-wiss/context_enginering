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

**Exempel:** "Vi har en veckas sprint denna vecka — vi börjar måndag 09:00 och avslutar torsdag 15:00."

**Varför det spelar roll:** Sprinter skapar fokus och gör det möjligt att planera vad som ska göras.

---

### Sprintmål
**Vad:** Det konkreta måltagget för sprinten. Vad ska vi ha färdigställt denna sprint?

**Exempel:** "Denna veckas sprintmål är att få autentisering att fungera end-to-end och att riskmåtten visas."

**Varför det spelar roll:** Utan ett mål vet teamet inte när sprinten är lyckad.

---

### MVP (Minimum Viable Product)
**Vad:** Den enklaste versionen av produkten som löser kundens huvudproblem. Ingenting onödigt, bara det som behövs.

**Exempel:** "MVP v2 är portföljöversikt + riskmått + rebalanserings-förslag. Vi behöver inte en söklåda än, eller möjligheten att exportera PDF."

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

**Exempel:** "Native-teamet är blockerat — de väntar på API-schemat från Backend."

**Varför det spelar roll:** Blockers är högsta prioritet att lösa. Teamet kan inte jobba innan de är lösta.

---

## 💻 TEKNIK & KODARBETE

### API-kontrakt
**Vad:** En överenskommelse mellan två system om hur de pratar med varandra. Vilken information skickas? I vilket format?

**Exempel:** "Frontend och Backend måste enas om API-kontraktet: 'GET /portfolio' returnerar en lista med portföljer i JSON-format, med fält: id, name, value, risk-score."

**Varför det spelar roll:** Om Frontend och Backend har olika idéer om kontraktet, funkar inte systemet.

---

### Branch (Git-branch)
**Vad:** En egen arbets-kopia av koden där du gör ändringar utan att påverka huvudkoden.

**Exempel:** "Zaida jobbar på feature/portfolio-overview branchen. Erik jobbar på feature/risk-metrics branchen. De skriver inte över varandra."

**Varför det spelar roll:** Branches låter flera personer jobba på samma kodbase utan att krasha varandra.

---

### Merge / Mergad
**Vad:** Att kombinera ändringar från en branch tillbaka till huvudkoden (develop/main).

**Exempel:** "Zaidas portfolio-overview branch är mergad till develop. Den är nu en del av systemet."

**Varför det spelar roll:** Merge betyder att arbetet är framförhandlat och testat nog för att vara officiell.

---

### Pull Request (PR)
**Vad:** En förfrågan om att merga din kod. Andra tittar på den, reviewar den, och säger ja/nej.

**Exempel:** "Erik har skapat en PR för risk-metrics. Två reviewers har godkänt den. Den är klar att merga."

**Varför det spelar roll:** PRs säkerställer att koden är bra innan den blir officiell.

---

### Code Review
**Vad:** Att en annan utvecklare läser din kod och säger om det är bra, eller om det behövs ändringar.

**Exempel:** "Tomac reviewade Lisas auth-flow kod. Han sa: 'Bra säkerhet, men denna loop kan optimeras.'"

**Varför det spelar roll:** Code review fångar fel och delar kunskap mellan teamet.

---

### Commit
**Vad:** En "sparning" av ditt arbete. Du sparar en version av koden med ett meddelande om vad du gjorde.

**Exempel:** "Marco gjorde en commit: 'Add FX calculation helper function'"

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

**Exempel:** "Vi kan nu testa end-to-end: användare matar in portföljdata → systemet beräknar risk → visar resultatet på skärmen. Hela vägen funkar."

**Varför det spelar roll:** End-to-end test visar att systemet faktiskt löser användarens problem.

---

### Deploy / Deployment
**Vad:** Att flytta kod från utvecklingsmiljön till produktionen (där riktiga användare använder den).

**Exempel:** "Vi deployade version 2.1 till produktion på torsdag. Användare använder den nu."

**Varför det spelar roll:** Deployment är när arbetet faktiskt når användarna.

---

## 💰 DOMÄN: PORTFÖLJ & RISKMÅTT

### Portföljöversikt
**Vad:** En vy som visar allt pengar en person har investerat — vilka sparformer, hur mycket i varje, totala värdet.

**Exempel:** "Annas portföljöversikt visar: 100k i fonder, 50k i aktier, 30k i sparbokssparingen. Total: 180k."

**Varför det spelar roll:** Människor behöver förstå vart deras pengar är.

---

### Volatilitet
**Vad:** Prissvängningar. Hur mycket priserna går upp och ned.

**Exempel:** "Denna aktie har hög volatilitet — priset hoppar 5-10% upp eller ned varje dag."

**Varför det spelar roll:** Högre volatilitet = större risk att förlora pengar.

---

### Sharpe-ratio
**Vad:** Ett mått på hur bra avkastning du får per risk du tar.

**Exempel:** "En fond med Sharpe-ratio 1.5 ger bättre avkastning i förhållande till risk än en fond med Sharpe-ratio 0.8."

**Varför det spelar roll:** Hjälper investerare välja mellan olika investeringsalternativ.

---

### Allokering
**Vad:** Hur pengarna är fördelade mellan olika investeringstyper.

**Exempel:** "Annas allokering är: 40% aktier, 30% fonder, 20% obligationer, 10% kontanter. Det är hennes mix."

**Varför det spelar roll:** Bra allokering minskar risk och maximerar långsiktig avkastning.

---

### Rebalansering
**Vad:** Att justera portföljen när fördelningen har skiftat (t.ex. om aktier stiger mycket, blir de överrepresenterad).

**Exempel:** "Annas plan säger 40% aktier, men nu är det 50% för de har stigit. Vi bör sälja några aktier och köpa fonder för att komma tillbaka till 40%."

**Varför det spelar roll:** Rebalansering håller portföljen på målkursen.

---

### Back-testing
**Vad:** Att testa en strategi mot historiska data för att se hur den hade gått förut.

**Exempel:** "Vi back-testade Annas portföljstrategi mot data från 2008 (finanskrisen). Den klarade sig bra."

**Varför det spelar roll:** Visar om strategin är robust, eller bara lyckats under dessa år.

---

### Risk-mått / Risk-score
**Vad:** Ett tal som visar hur riskfylld en portfölj är.

**Exempel:** "Annas portföljrisk-score är 6 av 10. Det är medel-risk."

**Varför det spelar roll:** Investerare behöver veta vilken risk de tar.

---

### FX-justering / FX-integration
**Vad:** Att räkna in val utomlands. Om du har pengar i dollar och kronan faller, blir dina dollar värda mer i kronor.

**Exempel:** "Med FX-justering ser vi Annas investering i amerikanska aktier blir värda 5% mer denna vecka för att kronan föll."

**Varför det spelar roll:** Gör beräkningarna korrekta för internationell investerare.

---

### Kärnflödet
**Vad:** Den viktigaste vägen genom systemet. Det flöde som löser kundens huvudproblem.

**Exempel:** "Kärnflödet är: inmatning av portföljdata → riskanalys → visning av resultat. Allt annat är extra."

**Varför det spelar roll:** Kärnflödet måste fungera perfekt. Allt annat kan warten.

---

## 🎯 STATUS & TEMPO

### On Track
**Vad:** Vi ligger på schema. Vi kommer att nå våra mål inom tidsplanen.

**Exempel:** "Frontend är on track. De kommer ha auth klart torsdag enligt planen."

**Varför det spelar roll:** Visar att vi inte behöver oroa oss eller justera.

---

### Slight Delay
**Vad:** Vi är lite efter schema, men inget kritiskt. Vi kan förmodligen komma ikapp.

**Exempel:** "Backend är slight delay. De beräknar att API är klar fredag istället för torsdag."

**Varför det spelar roll:** Signalerar att vi behöver uppmärksamhet, men det är inte panik än.

---

### Critical
**Vad:** En allvarlig avvikelse från planen. Vi kommer INTE nå målet utan åtgärd.

**Exempel:** "Native är critical. De är blockerade av Backend och kan inte börja sitt arbete. Möte med Backend behövs omedelbar."

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
**Exempel:** [Ett konkret exempel från projektet]
**Varför det spelar roll:** [Varför användaren behöver förstå detta]
```

---

**Senast uppdaterad:** 2026-09-13
