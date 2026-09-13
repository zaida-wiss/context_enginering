# 🎬 INSTRUKTIONER FÖR AI — Skapa Sprint Meeting Presentation

## 📍 DOKUMENTVÄGEN

**Du är här:** SPRINT_PRESENTATION_STRUCTURE.md (Presentationsguide)

```
START — README.md (denna repo)
        ↓
        VILL DU SKAPA EN PRESENTATION?
        ↓
🟢 DU ÄR HÄR: SPRINT_PRESENTATION_STRUCTURE.md (denna fil)
        ↓
LÄNG MOT: 
  • SPRINT_PROTOCOL_NUMBERED.md ← Vilka mötespunkter finns?
  • mötesprotokollet (Google Docs) ← Denna veckas status
  • DEFINITION_OF_DONE.md ← Vad är en KLAR issue?
        ↓
RESULTAT: Presentation med alla 13 mötespunkter (📝⓪-⑫)
```

**GÅ TILLBAKA TILL:** README.md om du är vilse

---

**DETTA ÄR EN REGEL FÖR AI** — Läs denna HELT innan du skapar presentationen.

**Vilken AI som helst (Claude, ChatGPT, Gemini) ska kunna följa denna guide och skapa SAMMA presentation varje gång.**

**Användaren kommer säga:** "Skapa en presentation till måndagsmötet" + länk till detta repo

**LÄSORDNING (MÅSTE följas):**
1. Du läser denna fil HELT (SPRINT_PRESENTATION_STRUCTURE.md)
2. Du läser PRESENTATION_DESIGN.md FÖR NPF-REGLER
3. Du läser PRESENTATION_FORMAT_GUIDE.md FÖR EXAKT LAYOUT
4. Du läser DATA_SOURCES.md FÖR FALLBACK-STRATEGI
5. Du samlar projektdata
6. **FÖRST DÅ** börjar du skapa presentationen enligt denna struktur

**Resultat:** Samma struktur, samma innehål, samma visuell känsla, NPF-vänlig & inspirerande, varje vecka

---

## 🎯 HUVUDMÅL — VARJE PERSON SKA KUNNA SVARA PÅ ÅTTA FRÅGOR

**Presentationens viktigaste uppgift är INTE bara att rapportera projektstatus.**

När måndagsmötet är slut ska VARJE teammedlem själv kunna svara på dessa frågor **UTAN ATT TOLKA ELLER GISSA**:

1. **Är mitt team på väg mot veckans mål?** (Grön/Orange/Röd och varför)
2. **Är min egen nuvarande uppgift fortfarande rätt prioriterad?** (Ja/Nej/Behöver ändras)
3. **Ligger mitt eget arbete enligt plan?** (Ja/Nej/Blockerad)
4. **Vad ska jag göra direkt efter mötet?** (Konkret issue-nummer + handling)
5. **Vilket issue äger jag denna vecka?** (Issue #XX, namn, deadline)
6. **När ska min uppgift vara klar?** (Konkret datum/tid)
7. **Är någon beroende av min leverans — och ska jag hjälpa någon annan?** (Ja/Nej + namn)
8. **Är jag blockerad — och vad gör jag i så fall istället?** (Blockad av vad / alternativ handling)

### ⚠️ KRITISKT KRAV:

**Det räcker INTE att presentationen SÄGER att mötets mål är att alla ska veta sitt jobb.**

Presentationens innehål måste innehålla tillräcklig information för att varje deltagare faktiskt kan besvara frågorna ovan.

Om en person efter mötet säger: "Jag förstår att statusen är orange, men vet inte om det påverkar mitt arbete eller vad jag ska göra nästa" — **då är presentationen INTE KLAR.**

**INFORMATIONSKEDJAN SOM MÅSTE FINNAS:**
```
Projektets status → Teamets läge → Min personliga situation → Min nästa handling
```

Om någon länk saknas är presentationen ofullständig.

### ✅ KONTROLL VID PRESENTATION-SLUT:

Mötet får INTE avslutas förrän för VARJE person kan presentation/protokollet visa:
- [ ] Vilken issue personen äger denna vecka
- [ ] Vad personen ska göra härnäst (konkret handling)
- [ ] Om arbetets ligger enligt plan eller är blockerat
- [ ] När uppgiften ska vara klar
- [ ] Vad personen är beroende av
- [ ] Om någon är beroende av denna persons leverans
- [ ] Om personen kan/bör avlasta någon annan

**Ingen person får lämnas med endast:** "Mitt team är grönt/orange/rött."

---

## 📋 KORT INSTRUKTION FÖR AI

1. ✅ Läs denna fil (SPRINT_PRESENTATION_STRUCTURE.md) från början
2. ✅ Läs mötesprotokollet (SPRINT_PROTOCOL_NUMBERED.md) för denna vecka
3. ✅ Läs mötesprotokollet från Google Docs (raw-export länk i README.md)
4. ✅ Läs KURSMAL_OCH_BETYG.md för kursdatum
5. ✅ Samla data denna vecka:
   - Git log (vad blev gjort)
   - GitHub Project Board (status)
   - Branches/PRs/blockers
   - Vem jobbar på vad
   - Frågor för PL (från team eller mötesprotokollet)
6. ✅ Skapa presentation **EXAKT enligt denna struktur** (normalt 16-22 slides)
   - Slide 0: Presentationsslide (enkel — bara typ, tid, syfte)
   - Slide 0.1: Agenda denna vecka
   - Slide 1-4: Övergripande (KURSEN + PROJEKTET + AVANZA + Progress Board)
   - Slides 5-7: Per-team status (Frontend/Backend/Native)
     - ⚠️ NYTT: Varje team-slide MÅSTE ha: STATUS → VARFÖR → VAD BETYDER DET FÖR ER → VEM GÖR VAD NU
   - Slide 8: Status sedan förra veckan
   - Slides 9-12: Prioritering, Estimering, Tekniska beslut, Blockers/Beroenden
   - 🆕 Slide N-2: 📝⑪ NÄR VI LÄMNAR MÖTET (TABELL: Person | Team | Issue | Gör nu | Klar när | Deadline | Beroende)
   - Slide N-1: 📝⑫ Sammanfattning (fokus, status, lycka till)
   - Slide N: Mötesprotokollet länk (för noteringar)
7. ✅ Symbol 📝 till VÄNSTER, copy-paste text till HÖGER
8. ✅ NPF-vänlig design:
   - Samma struktur VARJE vecka (förutsägbar)
   - 60-70% whitespace (WCAG AA contrast)
   - Visuell hierarki (stora rubriker, små detaljer)
   - Tydliga avsnittsskiljningar
9. ✅ Output: PowerPoint/Google Slides/Markdown (berätta vilket)

---

## ✅ FÖRE DU BÖRJAR — CHECKLIST

- [ ] Jag har läst SPRINT_PRESENTATION_STRUCTURE.md (denna fil)
- [ ] Jag vet vilken mötesprotokolls-data som gäller denna vecka
- [ ] Jag vet att samma STRUKTUR ska användas varje vecka
- [ ] Jag förstår att varje slide ska ha symbol 📝①②③ etc
- [ ] Jag vet vilka färger som är 🟢🟠🔴

---

**Sekreteraren ser symbolen 📝①②③ på varje slide och vet vilket protokoll-punkt att fylla in.**

---

## 🎬 SLIDE 0 — PRESENTATIONSSLIDE (ALLTID FÖRSTA)

**Slide 0.1 — PRESENTATIONSSLIDE**
```
📝⓪ MÅNDAGSMÖTE — SPRINT PLANNING

Tid: 09:00-10:30 (90 minuter)
Syfte: Planera denna vecka, säkerställa vi når målen

Vi täcker:
✅ Vad vi gjort
✅ Var vi står nu (3 målsystem)
✅ Vad som är kritiskt
✅ Prioritering & planering för denna vecka
```

**Slide 0.2 — AGENDA & PÅMINNELSE**
```
📝⓪ AGENDA — VI GÅR IGENOM DETTA SYSTEMATISKT

📝① Övergripande status (3 målsystem)
📝② Team-status: Frontend, Backend, Native
📝③ Vad gjordes förra veckan
📝④ Beroenden, Risker, Sårbarheter
📝⑤ Team-support förslag
📝⑥ Prioritering & Scope denna vecka
📝⑦ Estimering & Risk
📝⑧ Tekniska Beslut
📝⑨ Arbetsuppgifter denna vecka
📝⑩ Nästa Steg & Sammanfattning

💡 VI HÅLLER MÖTET KORT & KONCIST
- En punkt åt gången
- Fokuserat på beslut, inte pratet
- 90 minuter = vi är klara 10:30
```

---

## 🎬 SLIDE 1 — ÖVERGRIPANDE STATUS (TRE MÅLSYSTEM)

**Slide 1.1 — 📝① KURSEN (17 KURSMÅL + BETYG)**
```
📝① KURSEN — VAD BEHÖVER VI UPPNÅ?

Mål: Uppfylla alla 17 kursmål → G/VG betyg
Fokus: Individuell bedömning + slutleverans

Deadlines:
🔴 4 november 15:00 — SLUTLEVERANS
🟠 5 november 09:00 — FINALDAG (om vi är bland topp 4)

Vad behövs för godkänt:
✅ Kärnflödet fungerar
✅ Git-historia är tydlig (individuell bidrag)
✅ Dokumentation är komplett (README, beslut, tester)
✅ Alla 17 kursmål adresserade

Status denna vecka: 🟢 🟠 🔴 [välj EN]
- Fortskridande: [X av 17 kursmål adresserade]
- Risker: [Om någon kursmål hoppad?]
```

**Slide 1.2 — 📝① PROJEKTET (MVP V2 + LEVERABLES)**
```
📝① PROJEKTET — VAD SKA VI LEVERERA?

Mål: Funktionerande MVP v2 som löser Annas problem

MVP Scope:
✅ Portföljöversikt (alle sparformer)
✅ Riskmått (volatilitet, Sharpe, allokering)
✅ Back-testing motor
✅ FX-justering
✅ Rebalanserings-förslag

Deadlines:
🔴 24 september 16:00 — CTO-DEMO (kod + arkitektur)
🟠 15 oktober 17:00 — KVALDEMO (kund ser det)
🟢 4 november 15:00 — SLUTLEVERANS

Vad behövs för accept:
✅ Kärnflödet end-to-end testbar
✅ README, tester, beslutslogg
✅ Kan köras lokalt
✅ Inte perfekt, men säker & stabil

Status denna vecka: 🟢 🟠 🔴 [välj EN]
- Fortskridande: [X av MVP-features klara]
- Risker: [CTO-demo? Kundfeedback?]
```

**Slide 1.3 — 📝① AVANZA SOM KUND (BEHOV)**
```
📝① AVANZA SOM KUND — VAD BEHÖVER ANNA?

Problem Anna lösa:
"Förklara min portfölj utan att göra det för komplicerat"

Vad Anna behöver se:
✅ Portföljöversikt (total värde, alla sparformer)
✅ Risk-analys (vad är riskerna?)
✅ Allokering (hur är det fördelat?)
✅ Förslag (hur blir det bättre?)
✅ Back-testing (hur hade det gått förut?)

Feedback från Anna (om vi har den):
- [Vad tycker hon är bra?]
- [Vad behöver förbättras?]

Status denna vecka: 🟢 🟠 🔴 [välj EN]
- Löst: [Vilka av Annas behov lösta?]
- Återstår: [Vilka behov återstår?]
```

**Slide 1.4 — 📝① PROGRESS BOARD — BIG TEAM vs SMALL TEAMS**
```
📝① PROGRESS BOARD MED FÄRGKODNING

═══════════════════════════════════════════════════════════

🟢 BIG TEAM — VÄG TILL SLUTLEVERANS & KURSMÅL

Deadline: 4 november 15:00

Mål:
  Kursmål: ████████░░ 80% (14/17 adresserade)
  Projekt: ████████░░ 75% (MVP features)
  Kund:    ████████░░ 70% (Annas behov)
  
Status: 🟢 ON TRACK (eller 🟠 SLIGHT DELAY / 🔴 CRITICAL)

═══════════════════════════════════════════════════════════

SMALL TEAMS — VÄG TILL DENNA VECKAS DEADLINE

Deadline: Torsdag 15:00

🟢 FRONTEND TEAM — ON TRACK
   Progress: ████████░░ 80%
   Status: Grön ✅

🟠 BACKEND TEAM — SLIGHT DELAY
   Progress: ██████░░░░ 60%
   Status: Orange ⚠️
   Actions: [vad behövs]

🔴 NATIVE TEAM — CRITICAL
   Progress: ████░░░░░░ 40%
   Status: Röd 🚨
   Actions: [omedelbar åtgärd]

═══════════════════════════════════════════════════════════
```

**Design Notes (NPF-Vänlig):**
- Samma struktur varje vecka (förutsägbar)
- Tydliga färger (🟢🟠🔴) som visar status
- Visuella progressbars (████░░) för snabb scan
- Big team och small teams tydligt separerade
- Deadlines tydliga
- Whitespace mellan sektioner

---

## 📋 PRESENTATION FLOW (90 minuter — FLEXIBELT ANTAL SLIDES)

**ANTALET SLIDES ÄR INTE ETT MÅL I SIG SJÄLV.**

Normalt: 16-22 slides  
Färre/fler endast när informationen kräver det

**Prioritetsordning när du bygger:**
1. ✅ Alla förstår nuläget (projektstatus, teamstatus)
2. ✅ Alla förstår sin egen situation (är jag blockerad? vad gör jag nu?)
3. ✅ Alla vet nästa handling (konkret issue + deadline)
4. ✅ Ingen text överlappar eller blir för tät (WCAG AA)
5. ➜ Därefter minimeras antal slides

```
09:00-09:10 (10 min) — SLIDES 0-1
   📝⓪ Presentationsslide + Agenda
   📝① Övergripande (Kursen + Projektet + Avanza + Tidslinje)

09:10-09:25 (15 min) — SLIDES 2-7 (TEAM STATUS = 2 slides per team!)
   📝③ Frontend: Status & Varför
   📝③ Frontend: VAD BETYDER DET FÖR ER + VEM GÖR VAD NU
   📝④ Backend: Status & Varför
   📝④ Backend: VAD BETYDER DET FÖR ER + VEM GÖR VAD NU
   📝⑤ Native: Status & Varför
   📝⑤ Native: VAD BETYDER DET FÖR ER + VEM GÖR VAD NU

09:25-09:35 (10 min) — SLIDES 8-9
   📝⑥ Vad gjordes förra veckan
   📝⑦ Beroenden, Risker, Blocker-status

09:35-10:00 (25 min) — SLIDES 10-12
   📝⑧ Prioritering & Scope denna vecka
   📝⑨ Estimering & Kapacitet
   📝⑩ Tekniska Beslut (om några)

10:00-10:25 (25 min) — SLIDES 13-14
   🆕 📝⑪ NÄR VI LÄMNAR MÖTET (TABELL MED PERSON | TEAM | ISSUE | GÖR NU | KLAR NÄR)
   📝⑫ Sammanfattning (fokus, status, lycka till)

10:25-10:30 (5 min) — AVSLUT
   Bekräfta alla vet sitt jobb ✓
   Alla har tydlig nästa handling ✓
```

---

## 🎬 SLIDES MED NUMRERING

### SEKTION 📝⓪ — AGENDA & TEMA (5 min)

**Slide 0.1 — 📝⓪ PRESENTATIONSSLIDE**
- Titel: "MÅNDAGSMÖTE — SPRINT PLANNING"
- Innehål:
  - Tid: 09:00-10:30
  - Syfte: Planera denna vecka
  - Denna veckas tema: [Vad handlar mötet om? Ex: "Risk prioritization", "Customer feedback integration", "Performance optimization"]
  - Struktur: Systematisk genomgång, kort & koncist

**Slide 0.2 — 📝⓪ AGENDA & NÄSTA MÖTE PREVIEW**
- Titel: "AGENDA + PREVIEW"
- Innehål:
  - Lista alla 10 mötespunkter (📝①②③...)
  - Påminnelse: Vi håller mötet kort & koncist
  - 🔜 NÄSTA MÖTE (TIS 13:00): [Vad handlar det mötet om?]
    - Ex: "Halvtids-checkup och blockers"
    - Ex: "Feedback från CTO demo"
    - Ex: "Customer insights integration"

### SEKTION 📝① — FRÅGOR TILL PL (5 min)

**Slide 1.1 — 📝① FRÅGOR TILL PL**
- Titel: "Frågor Till Projektledaren"
- Innehål (om det finns):
  - Fråga 1: [Från team]
  - Fråga 2: [Från team]
  - Fråga 3: [Från PL:s updates]
- Om inga frågor: "Inga frågor denna vecka ✅"

### SEKTION 📝⑥ — VAD GJORDES FÖRRA VECKAN: RESULTAT, BIDRAG & TEMPO (5 min)

**Slide 6 — 📝⑥ VAD GJORDES FÖRRA VECKAN — RESULTAT & TEMPO**

**SYFTE:**
Denna mötespunkt ska spegla VERKLIGHETEN från föregående vecka.
AI:n ska inte automatiskt vara positiv, negativ eller neutral.
Tonen ska bestämmas av verifierad projektdata.

Målet är att teamet ska känna rätt sak utifrån vad som faktiskt hände:
- 🟢 Om mycket blev klart: "Bra jobbat — vi tog tydliga kliv framåt."
- 🟡 Om veckan var blandad: "Vi gjorde bra saker, men nådde inte den förflyttning vi planerade."
- 🔴 Om för lite blev klart: "Vi tappade fart förra veckan — nu behöver vi förstå varför och öka genomförandet."

**Presentationen ska ALDRIG försöka skapa artificiell pepp.**

---

**STEG 1: ANALYSERA FÖRST — FORMULERA TONEN SEDAN**

Innan sliden skrivs ska AI:n jämföra:

1. Vad planerade vi att få klart?
2. Vad blev faktiskt klart?
3. Vad flyttade produkten/projektet framåt?
4. Vad blev påbörjat men inte färdigt?
5. Vilka blockers påverkade resultatet?
6. Hur fördelades bidragen över teamet?
7. Är vi närmare sprintmålet än för en vecka sedan?
8. Är förflyttningen tillräcklig i förhållande till återstående tid?

**Först efter denna analys får presentationen välja ton och visuell känsla.**

---

**STEG 2: VISA VARJE PERSON — BIDRAG & EFFEKT**

För varje aktiv teammedlem:

**NAMN → Vad personen faktiskt bidrog med → Vad detta tillförde projektet**

```
📝⑥ VAD GJORDES FÖRRA VECKAN

🎯 FRONTEND TEAM:
  Lisa
  → Implementerade auth-flöde (80% klart)
  → Unblockade backend integration; CTO-demo nästa vecka blir möjlig

  Ali
  → Uppdaterade responsive layout + tester
  → Användare kan nu komma åt funktionen på alla enheter

  Jan
  → Codereview #50, #51 + dokumentation
  → Höll kodkvalitet; teamet behövde inte redigera efteråt

🎯 BACKEND TEAM:
  Marco
  → Löste FX-integrationsblocken (workaround implementerad)
  → Native kunde inte starta sitt arbete — nu kan de det

  Jana
  → 40+ nya unit-tests skrivna
  → Test-coverage från 62% → 68%; reduceradrisk vid deployment

  Anna
  → Core refactoring påbörjat
  → Arkitekturen blir hållbar för nästa fas

🎯 NATIVE TEAM:
  Kris
  → Error handling implementerat + merged
  → Användare får nu bättre feedback när något går fel

  Sam
  → Accessibility review + design-konsistens
  → Alla kan använda appen; ingen kvar utan möjligheter
```

**VIKTIGT — DETTA RÄKNAS SOM VERKLIGT BIDRAG:**
✅ Implementation ✅ Testning ✅ Code review ✅ Debugging ✅ Dokumentation
✅ Arkitektur-beslut ✅ UX-arbete ✅ Kravarbete ✅ Research ✅ Pairing/support
✅ Integration mellan team ✅ Blocker-lösning

**AI:n ska INTE dra slutsatsen: "ingen commit = inget bidrag"**

Om verifierad data inte visar något konkret bidrag: skriv inte påhittat beröm.
Visa istället neutralt: "Inget verifierat färdigställt bidrag hittades i tillgängliga källor."

---

**STEG 3: PROJEKTETS KLIV FRAMÅT**

Efter individuella bidrag, sammanfatta:

**DET HÄR KUNDE VI INTE FÖRRA MÅNDAGEN — MEN KAN NU**

```
✅ Auth-flödet kan testa end-to-end med backend
✅ Driftindikator baseras på live-data (inte mock)
✅ Test-coverage över 65% (högre än målsättning)
✅ FX-beräkningen blockar inte längre Native
✅ Användare på mobil får samma användarupplevelse
✅ Koden passar inte längre på ett napkin
```

---

**STEG 4: VECKANS HELHETSBILD & TEMPO**

Presentationen gör en gemensam bedömning av TEAMETS leveranstempo, baserat på:
- Planerat arbete ↔ faktiskt färdigställt arbete
- Merged PRs & issues i Done
- Integrationer som blivit möjliga
- Blockers som lösts
- Arbete som fortfarande står kvar

**Välj en av dessa baserat på DATA:**

```
🟢 TYDLIG FRAMÅTRÖRELSE
Majoriteten av det viktiga arbetet blev färdigt och projektet tog
konkreta kliv mot sprintmålet.

Visuell känsla: fyllda progressformer, gröna accenter, checkmarks, 
sammanhållna grupper, framåtriktade pilar, visuell tyngd på färdigställt.

🟡 BLANDAD VECKA
Viktigt arbete gjordes, men flera planerade resultat nådde inte hela
vägen till färdigt. Fokus behövs på att avsluta innan mer startas.

Visuell känsla: neutrala basfärger, gula/lila accenter för pågående,
delvis fyllda progressformer, färre checkmarks, övergångar mellan
klart och pågående.

🔴 FÖR LITEN FÖRFLYTTNING
För lite av det prioriterade arbetet blev klart i relation till planen
och återstående tid. Teamet behöver förstå orsakerna och justera tempo,
scope eller arbetssätt.

Visuell känsla: dämpad bas, sparsam orange accent, mindre fyllda
progressytor, fler öppna former, mindre visuell dominans av "done".
Undvik stora röda varningar om inget faktiskt är kritiskt.
```

**KRITISKT:** Detta är en TEAM-bedömning. Presentationen får aldrig peka ut en enskild person som "för långsam."

---

**OBLIGATORISK STRUKTUR:**

1. 🎉 VECKANS KLIV FRAMÅT (vad kunde vi inte göra förra veckan, men kan nu?)
2. 👥 VAD VAR OCH EN BIDROG MED (namn → bidrag → effekt)
3. 📈 VECKANS TEMPO (planerat vs faktiskt, teamets helhetsbild)
4. 🔎 Diskret verifiering: issue / PR / commit (visa inte som huvudbudskap)

**Git-data får aldrig vara huvudbudskapet.** Använd det för att VERIFIERA påståenden, inte för att fylla slides.

---

**KÄNSLA OCH TON:**

✅ VARJE person är synlig, även om job inte är "helt klart"
✅ Visa PÅVERKAN, inte bara "issues closed"
✅ Både merged och pågåande arbete är framsteg
✅ Lyfta fram svårt arbete (refactor, tester, reviews, blockers)
✅ Tonen bestäms av DATA: stark vecka → glad ton; svag vecka → fokus på förbättring

**ALDRIG:**
❌ Börja med "Bra jobbat!" innan veckan analyserats
❌ Göra låg aktivitet positiv bara för att vara uppmuntrande
❌ Bedöma tempo enbart från antal commits
❌ Bedöma individer utifrån commit count
❌ Bara antal öppna issues — visa rörelsen (vad var inte möjligt förra veckan)

**SAMMA FORMAT VARJE VECKA** → teamet ser tempo, förflyttning, och att alla bidrag räknas

---

### SEKTION 📝② — ÖVERGRIPANDE MÅL & STATUS (10 min)

**Slide 2.1 — 📝② (SYMBOL TILL VÄNSTER, TEXT TILL HÖGER)**
```
📝② DENNA VECKAS MÅL

Risk Metrics (#42 - Marco): [%]
FX Converter (#45 - Jana): [%]
Tests (#48 - Anna): [%]
Kärnflödet (#51 - Kiran): [status]
```
*Secretary copy-pastar allt till höger om 📝② direkt in i punkt ② i protokollet*

**Slide 2.2 — 📝② (FORTSÄTTNING — SAMMA PUNKT)**
```
📝② ÖVERGRIPANDE STATUS

Status: 🟢 GRÖN / 🟠 ORANGE / 🔴 RÖD

Deadlines:
- Torsdag 15:00 (Sprint end)
- 24 sep 16:00 (CTO-demo)
- 15 oktober (Kvaldemo)

Åtgärdsförslag (om orange/red):
[Åtgärder...]
```
*Secretary fortsätter copy-pasta till samma punkt ②*

---

### SEKTION 📝③ — FRONTEND TEAM STATUS (OBLIGATORISK STRUKTUR)

**Slide 3.1 — 📝③ FRONTEND: STATUS & VARFÖR**
```
📝③ Frontend — [🟢 GRÖN / 🟠 ORANGE / 🔴 RÖD]

STATUS:
Progress: [XX%] (████░░░░░░)
Denna vecka: [X av Y] issues done

VARFÖR denna status?
✅ Klart: #XX, #YY [namn]
🔄 Pågår: #ZZ [namn] — väntar på backend
🔴 Blockerad: [vad?] [namn]
```

**Slide 3.2 — 📝③ FRONTEND: VAD BETYDER DET FÖR ER + VEM GÖR VAD**
```
📝③ För varje person i Frontend:

VAD BETYDER DET FÖR ER?
Lisa (#40 Auth): Fortsätt med mockad integration → backend kommer torsdag
Ali (#52 Responsive): Kan jobba fullt ut → ingen blocker, prioritera tester
Kir (#XX): Ledig kapacitet → kan ta på sig extra test

FOKUS DENNA VECKA:
Lisa → #40 Auth (måste klart torsdag för integration)
Ali → #52 Responsive (kan avslutas, sen test #XX)
Kir → #XX Tester (kan ta extra om behövs)

Behöver vi hjälp? → Nej
Kan vi avlasta? → Ja, Ali kan ta backlog-test efter #52
```

---

### SEKTION 📝④ — BACKEND TEAM STATUS (OBLIGATORISK STRUKTUR)

**Slide 4.1 — 📝④ BACKEND: STATUS & VARFÖR**
```
📝④ Backend — [🟢 GRÖN / 🟠 ORANGE / 🔴 RÖD]

STATUS:
Progress: [XX%] (████░░░░░░)
Denna vecka: [X av Y] issues done

VARFÖR denna status?
✅ Klart: #XX [namn]
🔄 Pågår: #YY [namn]
🔴 Blockerad: FX-integrationstester väntar på möte med Avanza
```

**Slide 4.2 — 📝④ BACKEND: VAD BETYDER DET FÖR ER + VEM GÖR VAD**
```
📝④ För varje person i Backend:

VAD BETYDER DET FÖR ER?
Marco (#45 FX): Blockerad på Avanza-möte → kan jobba med fallback: risk-metriken istället
Jana (#48 Tests): Fokus på unit-tests (inte integration än) → kan jobba fullt ut
Anna (#51 Core): Väntar på Marco → kan börja refaktor medan du väntar

FOKUS DENNA VECKA:
Marco → #45 FX (blockerad) + #48 Risk parallellt
Jana → #48 Tests (ej blockerad, fortsätt)
Anna → Refaktor parallellt (#51) medan Marco löser FX

Behöver vi hjälp? → Ja, behöver 4h från Frontend för integration-review torsdag
Kan vi avlasta? → Nej, alla är blockerade/fokuserade
```

---

### SEKTION 📝⑤ — NATIVE TEAM STATUS (OBLIGATORISK STRUKTUR)

**Slide 5.1 — 📝⑤ NATIVE: STATUS & VARFÖR**
```
📝⑤ Native — [🟢 GRÖN / 🟠 ORANGE / 🔴 RÖD]

STATUS:
Progress: [XX%] (████░░░░░░)
Denna vecka: [X av Y] issues done

VARFÖR denna status?
✅ Klart: [—]
🔄 Pågår: #XX [namn]
🔴 KRITISK BLOCKER: Väntar på API-schema från Backend (blockerar allt)
```

**Slide 5.2 — 📝⑤ NATIVE: VAD BETYDER DET FÖ ER + VEM GÖR VAD + OMEDELBAR ÅTGÄRD**
```
📝⑤ För varje person i Native:

VAD BETYDER DET FÖR ER?
Kris: Du kan inte starta #XX tills Backend är klar → fallback-arbete: infrastruktur-setup
Sam: Samma blocker

FOKUS DENNA VECKA:
Kris → Vänta på #XX (blockerad av Backend) → jobba med infrastruktur-setup istället
Sam → Vänta på schema → review och design (kan göras offline)

⚠️ OMEDELBAR ÅTGÄRD:
Backend + Native pair-prog IDAG 14:00-17:00 → API-schema klart
= Då kan Native börja bygga i morgon 09:00

Blockers ownare: Marco (Backend) — status uppdateras dagligen
```

---

### BREAKOUT SEKTION 🎙️

**Slide 6.1 — 🎙️ BREAKOUTS**
- Titel: "Team Breakouts — 5 minuter"
- Innehål:
  - "Frontend rum: Vad behöver ni denna vecka?"
  - "Backend rum: Vad blockerar er?"
  - "Native rum: Vad behöver ni för att börja?"
  - "Vi ses om 5 minuter!"

**Slide 6.2 — 🎙️ PAUS**
- Titel: "Kaffepaus — 5 minuter"
- Innehål:
  - (Optional musik eller bara tom slide)
  - "Vi återsamlas om 5 minuter"

---

### SEKTION 📝⑥ — PRIORITERING & SCOPE (30 min)

**Slide 7.1 — 📝⑥**
- Titel: "Prioritering & Scope"
- Innehål:
  - MÅSTE-HA denna vecka: [Issues]
  - NICE-TO-HAVE: [Issues]
  - "Kan vi göra allt? Eller scope cut?"

**Slide 7.2 — 📝⑥** (om behövs)
- Titel: "Scope Cut Beslut"
- Innehål:
  - Skipped: [Issue - Why?]
  - Shifted: [Issue - To when?]

---

### SEKTION 📝⑦ — ESTIMERING & RISK (25 min)

**Slide 8.1 — 📝⑦**
- Titel: "Estimering & Kapacitet"
- Innehål:
  - Frontend: X hours available / Y hours needed
  - Backend: X hours available / Y hours needed
  - Native: X hours available / Y hours needed
  - "Passar det?"

**Slide 8.2 — 📝⑦**
- Titel: "Risker & Mitigation"
- Innehål:
  - Risk 1: [Beskrivning] → Mitigation: [Åtgärd]
  - Risk 2: [Beskrivning] → Mitigation: [Åtgärd]
  - Framgångskriterier: [Kriterium 1, 2, 3]

---

### SEKTION 📝⑧ — TEKNISKA BESLUT (Vid behov)

**Slide 9.1 — 📝⑧** (om det finns tekniska beslut denna vecka)
- Titel: "Tekniska Beslut"
- Innehål:
  - Beslut: [Vad?]
  - Varför: [Reasoning]
  - Impact: [Vad ändrar?]

---

### SEKTION 📝⑨ — BEROENDEN & BLOCKERS (Vid behov)

**Slide 10.1 — 📝⑨** (om det finns kritiska beroenden)
- Titel: "Beroenden Mellan Teams"
- Innehål:
  - Frontend väntar på: [Vad från vem] → Status
  - Backend väntar på: [Vad från vem] → Status
  - Native väntar på: [Vad från vem] → Status

---

### SEKTION 📝⑩ — DENNA VECKAS ARBETE — VAD BIDRAR DET TILL?

**Slide 10 — 📝⑩ DENNA VECKAS ARBETE OCH DESS SYFTE**

**SYFTE:** Visa VARJE issues bidrag till projektet — inte bara en lista

**OBLIGATORISK STRUKTUR — visa BÅDE issue OCH why it matters:**

```
📝⑩ DENNA VECKAS ARBETE

🎯 FRONTEND:
  #40 Auth flow (Lisa, 16h)
  → Enables users to log in securely
  → Unblocks Backend #45 (API integration)
  → Required for MVP demo to CTO

  #52 Responsive layout (Ali, 12h)
  → Users can access portfolio on all devices
  → Dependency for Native #60 (mobile UI)

🎯 BACKEND:
  #45 FX integration (Marco, 20h)
  → Calculates currency conversions correctly
  → Blocks Frontend #40 AND Native #60
  → Critical for customer demo (Avanza meeting)

  #48 Unit tests (Jana, 8h)
  → Increases code coverage to 70%+
  → Prevents regressions in #45 deployment

🎯 NATIVE:
  #60 Mobile auth screen (Kris, 16h)
  → Users can log in on phone
  → Blocked by Backend #45 (API ready)
  → After that: can parallelize with Frontend
```

**VID VARJE ISSUE, VISA:**
✅ Issue-nummer + titel
✅ Assignee
✅ Estimated hours
✅ **VAD det bidrar till** (customer value, enables other work, etc)
✅ **Blocking/blocked by** (dependencies)
✅ **Varför det spelar roll denna vecka**

**DATA MÅSTE KOMMA FRÅN:**
1. GitHub issues + descriptions (vad varje issue är)
2. Project Board dependencies (vem väntar på vem)
3. Meeting notes (varför var denna prioriterad)
4. Team's assessment (customer impact)

**KÄNSLA OCH TON:**
✅ Inte bara en lista — show the WHY
✅ Connect issues to project goals ("enables MVP demo")
✅ Show cross-team dependencies (Frontend waits on Backend → show both)
✅ Help teams understand what OTHER teams are doing and why it matters

**ALDRIG:**
❌ Bara issue-nummret utan kontext
❌ Tekniska detaljer utan customer/project value
❌ Silofält (Frontend lista skild från Backend lista)
❌ Glömma dependencies — visa alltid vem som blockerar vem

**RESULT:** Teams förstår inte bara VAD alla gör, utan VARFÖR och HUR det hänger ihop

---

### SEKTION 📝⑪ — NÄR VI LÄMNAR MÖTET (MÖTETS VIKTIGASTE SLIDE!)

**Slide 11 — 📝⑪ NÄR VI LÄMNAR MÖTET**

🆕 **DENNA SLIDE ÄR MÖTETS VIKTIGASTE — DEN ÄR EN FAKTISK INDIVIDUELL UTCHECKLING, INTE EN RAPPORT**

```
📝⑪ NÄR VI LÄMNAR MÖTET — VARJE PERSON KAN SVARA PÅ DENNA

Obligatorisk tabell (MÅSTE visas):

┌──────────┬────────┬────────┬──────────────────┬──────────┬──────────┬──────────────────┐
│ Person   │ Team   │ Issue  │ Gör nu            │ Klar när │ Deadline │ Beroende av      │
├──────────┼────────┼────────┼──────────────────┼──────────┼──────────┼──────────────────┤
│ Lisa     │Frontend│ #40    │ Frontend auth     │ Torsdag  │ 15:00    │ Backend #45      │
│ Ali      │Frontend│ #52    │ Responsive test   │ Torsdag  │ 15:00    │ —                │
│ Marco    │Backend │ #45    │ FX integration    │ Torsdag  │ 15:00    │ Avanza möte      │
│ Kris     │Native  │ #XX    │ Väntar på #45     │ Fredag   │ 17:00    │ Backend #45      │
└──────────┴────────┴────────┴──────────────────┴──────────┴──────────┴──────────────────┘

EXTRA SEKTIONER (om relevant denna vecka):

⚠️ SAKNAR TYDLIG UPPGIFT:
- [Namn] — ej assignad än, fördela under mötet
- [Namn] — blockerad, planera fallback-arbete

🤝 KAN AVLASTA:
- Ali (Frontend) — har 3h kapacitet efter #52 → kan ta backlog-test
- [Namn] — kan hjälpa [team] med [vad]

🔗 VÄNTAR PÅ:
- Kris (Native) blockerad av Backend #45 → arbetar med infrastruktur-setup istället
- Marco blockerad av Avanza-möte → arbetar med risk-metrics parallellt
```

**Mötet får INTE avslutas förrän:**
- [ ] Alla personer i tabellen är listade
- [ ] Alla aktiva issues har assignee
- [ ] Alla vet vad "klart" betyder för sin uppgift
- [ ] Alla blockers har owner + status
- [ ] Alla vet om de ska fortsätta, byta fokus eller hjälpa någon annan
- [ ] Saknade assignments är planerade eller delagda under mötet

---

### SEKTION 📝⑫ — SAMMANFATTNING & LYCKA TILL

**Slide 12 — 📝⑫ SAMMANFATTNING**
- Titel: "Sammanfattning & Lycka Till"
- Innehål:
  - Fokus denna vecka: [1-2 saker]
  - Kritiska actions: [Lista 2-3]
  - Status: 🟢 / 🟠 / 🔴 (kort förklaring)
  - "Lycka till denna vecka!" + emoji

---

## 🎨 DESIGN-REGLER FÖR ALLA SLIDES

- **Font:** Stor, läsbar (minst 24pt)
- **Kontrast:** WCAG AA (4.5:1 text/bakgrund)
- **Padding:** 12px horisontellt, 16px vertikalt (ingen text-overlap)
- **Färger:** 
  - 🟢 Grön = #2ecc71
  - 🟠 Orange = #e67e22
  - 🔴 Röd = #e74c3c
- **Varje slide:** Max 3-5 bullets, inte massa text
- **Symbol:** 📝① etc bör synas tydligt (övre högra hörnet?)

---

## ✅ CHECKLIST FÖR PRESENTATION

Innan mötet:
- [ ] Alla slides har rätt symbol (📝①②③ etc)
- [ ] Symbolerna matchar mötesprotokollet
- [ ] Slides är i rätt ordning
- [ ] Färger är WCAG AA contrast
- [ ] Padding är minst 12px/16px
- [ ] Breakout-slides är klara (🎙️)
- [ ] Paus-slide är klara (🎙️)

Under mötet:
- [ ] Secretary kan se både presentation + protokoll sida vid sida
- [ ] Secretary copy-pastar text från slides till rätt punkt
- [ ] Facilitator följer slide-order (springar inte omkring)

---

## 💡 TIPS FÖR CONSISTENCY

**Samma struktur varje vecka = Teamet känner igen den**
- Punkt ① är alltid Status
- Punkt ② är alltid Mål & Status
- Punkt ③④⑤ är alltid Teams
- Punkt ⑥⑦ är alltid Prioritering & Estimering
- Punkt ⑧⑨⑩⑪ är alltid Beslut/Nästa steg

Lag lär sig: "Jag vet att efter Breakout kommer Prioritering på slide 7"
Secretary vet: "Slide med 📝⑥ = Jag fyller in punkt 6 i protokollet"

**Resultat:** Mötet flyter snabbt, protokollet blir korrekt och komplett.

---

## 🤖 FÖR EXTERNA AIS — ANVÄNDA DENNA GUIDE

**Om någon säger:** "Skapa en presentation till måndagsmötet enligt context_enginering repo"

**Du gör:**
1. Läs denna fil (SPRINT_PRESENTATION_STRUCTURE.md) från början
2. Läs SPRINT_PROTOCOL_NUMBERED.md för att förstå strukturen
3. Fråga användaren: "Vilken vecka?" eller "Läs mötesprotokollet från Google Docs"
4. Samla data för denna vecka:
   - Git log denna vecka (vad blev done)
   - GitHub Project Board status
   - Mötesprotokollet från tidigare möten
   - Team-status från mötesprotokollet (🟢🟠🔴)
5. Skapa presentation **EXAKT enligt denna struktur**:
   - **SLIDE 0:** AGENDA med alla 11 punkter (📝①②③ etc) — ALLTID FÖRST
   - Slide 1.1 → 📝① med text till höger
   - Slide 2.1, 2.2 → 📝② med text till höger (båda samma punkt)
   - Slide 3.1 → 📝③ (Frontend)
   - Slide 4.1 → 📝④ (Backend)
   - Slide 5.1, 5.2 → 📝⑤ (Native)
   - osv enligt schema ovan

6. **KRITIGT:** VARJE SLIDE måste ha:
   - Symbol **📝① klistrad till VÄNSTER**
   - Text till HÖGER som kan copy-pastas direkt
   - Secretary kan se symbolen och veta exakt vilken punkt att fylla in

7. Output i format: **PowerPoint (.pptx), Google Slides, eller Markdown**
   - Berätta vilket format du använder
   - Sätt in all text direkt (inte "add text manually")

**KRITISKT — DESSA REGLER ÄR TVINGANDE:**

✅ MÅSTE GÖRA:
- [ ] Normalt 16-22 slides (fler/färre endast om information kräver det)
- [ ] Varje team-slide MÅSTE ha TVÅ sub-slides: STATUS & VARFÖR + VAD BETYDER DET FÖR OSS
- [ ] Slide 0: Presentationsslide + Agenda
- [ ] Slide 1: TRE MÅLSYSTEM (Kursen + Projektet + Avanza + Tidslinje)
- [ ] Slides med team-status (Frontend/Backend/Native) — minst 2 slides per team
- [ ] Slide: Vad gjordes förra veckan
- [ ] Slide: Beroenden, Risker, Blockers
- [ ] Slide: Prioritering & Scope
- [ ] Slide: Estimering & Kapacitet
- [ ] 🆕 Slide: NÄR VI LÄMNAR MÖTET (TABELL: Person | Team | Issue | Gör nu | Klar när | Deadline)
- [ ] Slide: Sammanfattning
- [ ] VARJE slide får symbol 📝⓪①②③ etc
- [ ] Symbol till VÄNSTER, text till HÖGER
- [ ] SAMMA struktur varje vecka (prediktibel)

❌ ALDRIG GÖRA:
- [ ] Aldrig hoppa över Slide 0 eller Slide 1 (tre målsystem är KRITISKT)
- [ ] Aldrig utelämna någon team eller göra bara EN slide per team
- [ ] Aldrig utelämna "NÄR VI LÄMNAR MÖTET" — den är mötets viktigaste slide
- [ ] Aldrig lägga till egna "kreativa" extra slides utan mål
- [ ] Aldrig ändra ordningen på slides
- [ ] Aldrig dölja deadlines eller kursmål
- [ ] Aldrig för mycket text (max 3-5 bullets per slide)
- [ ] Aldrig sälj en presentation utan tydlig tabell över vem som gör vad när

**Om du får denna instruktion och är en AI:**
- Du MÅSTE följa denna struktur
- Du MÅSTE ha minst två slides per team (Status & Varför + Betydelse & Handling)
- Du MÅSTE sätta symbol på varje slide
- Du MÅSTE inkludera alla tre målsystem (Kursen, Projektet, Avanza)
- Du MÅSTE inkludera "NÄR VI LÄMNAR MÖTET" tabell
- Avvikelse från denna struktur = MISSLYCKAD presentation

**EXEMPEL-OUTPUT (vad AI ska leverera):**
```
✅ Presentation klar! Format: PowerPoint

SLIDE-STRUKTUR (18-20 slides — FLEXIBELT antal):

Slide 0.1: 📝⓪ PRESENTATIONSSLIDE
Slide 0.2: 📝⓪ AGENDA & PÅMINNELSE

Slide 1.1: 📝① KURSEN (17 mål → G/VG)
Slide 1.2: 📝① PROJEKTET (MVP v2)
Slide 1.3: 📝① AVANZA SOM KUND
Slide 1.4: 📝① TIDSLINJE & CHECKLISTOR

Slide 3.1: 📝③ FRONTEND: Status & Varför
Slide 3.2: 📝③ FRONTEND: VAD BETYDER DET FÖR ER + VEM GÖR VAD NU

Slide 4.1: 📝④ BACKEND: Status & Varför
Slide 4.2: 📝④ BACKEND: VAD BETYDER DET FÖR ER + VEM GÖR VAD NU

Slide 5.1: 📝⑤ NATIVE: Status & Varför
Slide 5.2: 📝⑤ NATIVE: VAD BETYDER DET FÖR ER + VEM GÖR VAD NU

Slide 6: 📝⑥ Vad gjordes förra veckan
Slide 7: 📝⑦ Beroenden, Risker, Blockers

Slide 8: 📝⑧ Prioritering & Scope
Slide 9: 📝⑨ Estimering & Kapacitet
Slide 10: 📝⑩ Tekniska Beslut (om några)

🆕 Slide 11: 📝⑪ NÄR VI LÄMNAR MÖTET
   ┌──────────┬────────┬────────┬──────────┬──────────┬──────────┐
   │ Person   │ Team   │ Issue  │ Gör nu   │ Klar när │ Deadline │
   ├──────────┼────────┼────────┼──────────┼──────────┼──────────┤
   │ Lisa     │Frontend│ #40    │ Auth     │ Torsdag  │ 15:00    │
   │ Marco    │Backend │ #45    │ FX       │ Torsdag  │ 15:00    │
   │ Kris     │Native  │ #XX    │ Väntar   │ Fredag   │ 17:00    │
   └──────────┴────────┴────────┴──────────┴──────────┴──────────┘

Slide 12: 📝⑫ Sammanfattning & Lycka Till

TOTALT: 18-20 slides (normalt antal för denna struktur)

Du kan nu:
- Öppna denna presentation
- Visa den under mötet (09:00-10:30)
- Secretary använder symbolerna 📝 för att veta vad som ska fyllas in i protokollet
- ALLA DELTAGARE vet att:
  ✓ Deras team-status (grön/orange/röd och varför)
  ✓ Vad det betyder för dem personligen
  ✓ Vad de ska göra näst
  ✓ Deadline för deras arbete
```
