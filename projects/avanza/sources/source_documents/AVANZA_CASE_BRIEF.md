**{ case_avanza } Kundcase · Chas Extended Challenge 2026**

# Avanza: Portföljhälsa med back-testing

Hjälp sparare med växande, komplexa portföljer att förstå sitt sparande – se risk, allokering och målavvikelse, och back-testa strategier mot historik.

**Kund**

### Avanza

**Segment**

Privatsparande och investeringar

**Backend**

Java

**Vad handlar det om**

## Kundens problem

**Kundens röst · ur casefilmen**

”Anna har pengar. Hon har investeringar. Men hon saknar överblick. Och Anna är faktiskt inte ensam.”

Avanzas fiktiva kund Anna, 38, har sparat i tio år: ISK, kapitalförsäkring, tjänstepension, svenska och amerikanska aktier och flera fonder – runt 700 000 kr. Hon vet hur mycket hon har, men inte hur stor risk hon tar, hur pengarna är fördelade eller hur dollarkursen påverkar henne. Hennes plan var 60 % aktier / 40 % stabilt, men marknaden har tyst dragit henne mot 75/25 – utan att hon märkt det. Det centrala begreppet är rebalansering: att återställa portföljen till den strategi man en gång valde.

**Edda Hallin · systemutvecklare, Avanza**

### Painen

När portföljen växer tappar kunden överblicken. ISK, KF, depå och pension hamnar i silos. Kunden ser inte sin risk, sin allokering eller när strategin har driftat från målet. Allt fler har dessutom utländsk valutaexponering och behöver portföljen översatt till hemvaluta med korrekt FX-justering (FX = valutakurs). Idag lämnar kunder Avanza för externa verktyg för att förstå sitt eget sparande.

### Vad kunden vill uppnå

Kunden ska känna **kontroll** utan att vara finansexpert: en tydlig helhetsbild över alla sparformer, förståelse för sin risk och allokering, och en signal när något förändrats så mycket att det är värt att se över. Inte personlig rådgivning – utan begriplig information och möjligheten att utforska konsekvenser.

**Ert uppdrag**

## Från v1 till v2

Ni tar över en trög v1 där portföljanalysen och back-testingen är svårbegriplig och långsam. Uppdraget är att göra den begriplig, snabbare och mer användbar: en samlad portföljvy, korrekt FX, tydliga riskmått och en indikator när portföljen driftar från målallokeringen.

**MVP-flödet er v2 ska klara**Användaren loggar in, ser portföljen översatt till SEK med korrekt FX-justering, sätter en målallokering och får en indikator när driften överskrider tröskeln.

**Vad lösningen ska kunna**

## Features att arbeta med

- Samlad portföljvy över alla sparformer, värden uppdateras via polling.
- Multivaluta-stöd med FX-konvertering – användaren kan växla basvaluta.
- Allokering och riskmått: fördelning, volatilitet (hur mycket värdet svänger), max drawdown (största fall från topp till botten) och Sharpe (avkastning i förhållande till risk).
- Målallokering med avvikelse-indikator när driften överskrider tröskel.
- Back-testing-motor mot 5 års historik för upp till 500 instrument.
- Rebalanseringsförslag och en alerts-lista med historik.

**C/C++-öppningen i det här caset**

Back-testing-motorn och de rullande riskmåtten är prestandakritiska och lämpar sig för en native-modul: back-testing över 5 års historik för upp till 500 instrument, samt rullande riskmått och FX-justering över stora tidsserier.

Ni ska inte bygga *allt*. En junior konsult förstår problemet, prioriterar det som skapar störst kundvärde och avgränsar resten – och kan motivera varför.

**Teknisk fördjupning · för den som vill djupare**

## Kravställningen bakom caset

Det här är hela den tekniska bilden: v1-stacken ni tar över, målen för v2 och datamodellen. Den är tätare än pitchen ovan med flit – använd den som referens under projektet, inte som läsning dag 1.

### v1-stacken ni tar över (brownfield)

| **LagerSå ser v1 ut** |                                                                                               |
| --------------------- | --------------------------------------------------------------------------------------------- |
| **Backend**           | Spring Boot 2.7, Java 11, raw JDBC, monolit-controllers som blandar HTTP, affärslogik och SQL |
| **Frontend**          | jQuery och Bootstrap 3 eller server-renderade JSP-vyer                                        |
| **Databas**           | Postgres 12, delvis denormaliserat schema, handgjorda SQL-skript (inget migrationsverktyg)    |
| **Native**            | Saknas – back-testing och riskmått körs ineffektivt i Java                                    |
| **Tester**            | Enstaka JUnit-tester utan täckning på det viktiga                                             |
| **Build**             | Maven, beroenden ej låsta i pom.xml                                                           |

### v2-målen ni bygger mot

- Spring Boot 3.x, Java 21, JPA/Hibernate, Flyway-migrationer.
- React 18 med TypeScript, TanStack Query och modernt chart-bibliotek.
- C/C++-modul för back-testing-motor och rullande riskmått.
- Konsekvent FX-pipeline med historisk lookup.
- Testtäckning på alla tre lager och grön CI-pipeline.

### C/C++-modulens innehåll i v2

- Back-testing-motor över 5 års historik för upp till 500 instrument.
- Rullande riskmått och FX-justering över stora tidsserier.

### Datamodell

User · Account (ISK/KF/Depå/Pension) · Holding (med currency) · Transaction · Instrument (med currency) · PriceHistory · FxRate (date, from, to, rate) · TargetAllocation · Alert · BacktestRun

**Gemensam Definition of Done för v2**Kärnflödet fungerar och kan visas · README beskriver installation, körning, testning, kända brister och avgränsningar · teststatus är dokumenterad och rimlig · beslutslogg visar viktiga vägval · individuella bidrag går att härleda · specialistfeedforward är bearbetad · det finns en fallback om livedemon inte fungerar.
