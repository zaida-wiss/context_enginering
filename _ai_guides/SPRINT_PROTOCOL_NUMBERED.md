# 🗂️ Mötesprotokoll — Sprint Planning (14 mötepunkter)

**Denna struktur är 1:1 med presentationen. En mötespunkt kan ha 1-3+ slides (märkta med samma symbol).**

---

## 🔍 FÖRE MÖTET: Obligatorisk Cross-Team Code & Contract Review

**AI:n måste granska actual code i alla aktiva branches/PRs innan presentation skapas.**

Kontrollera:
- ✅ API-kontrakt mellan Frontend och Backend (endpoints, request/response)
- ✅ JNA/Native-kontrakt mellan Backend och Native
- ✅ Auth/JWT-flöde — är implementationen samma överallt?
- ✅ Datamodeller och DTOer — matchar allt?
- ✅ Felhantering — olika strategier någonstans?
- ✅ Andra gemensamma antaganden (naming, versioning, etc)

**Resultat dokumenteras i relevanta mötespunkter:**
- Blockande avvikelser → ⑦ Beroenden & blockers
- Risk för dubbelarbete → ⑩ Risker
- Kontrakt som behöver fastslås → ⑪ Tekniska beslut
- Åtgärder efter möte → ⑬ Nästa steg
- Externa beslut → ⑭ Frågor till PL

---

## 📋 Framsida — Möte-info (ingen/📝⓪)

```
SPRINTPLANERING · TEAM 1
Måndag [datum] · 09:00–10:30

Fokus med PL denna vecka
[Fokustext — kort och tydlig]

Underlag kontrollerat inför mötet:
context_enginering · avanza-team1 · Git-status · Issues & PRs · Project Board
Code review: [status — kontrakt verifierade / avvikelser noterade]
Mötesprotokoll: [kontrolleras före möte]
```

---

## 📝① Sedan Förra Mötet
**Vad blev faktiskt klart? (Done/merged-vy)**

**VIKTIGT: Visar commits från ALLA teammedlemmar (7 dagar)**

Git-status denna vecka:
- Mergade commits: 
  - Zaida: #[XX] [beskrivning]
  - Tomac: #[XX] [beskrivning]
  - Björn: #[XX] [beskrivning]
  - Rasha: #[XX] [beskrivning]
  - Erik: #[XX] [beskrivning]
  - Pär: #[XX] [beskrivning]
  - Henrik: #[XX] [beskrivning]

- Active branches (pågår denna vecka):
  - feature/#42-[person]
  - feature/#51-[person]
  - feature/#60-[person]

- Stale branches (>3 dagar, ingen commit):
  - [branch] — senaste commit: [datum]

---

## 📝② Sprintmål
**Vad ska denna sprint åstadkomma?**

Överordnat tema:
[Kort beskrivning av sprintens huvudsakliga fokus]

Tre huvudmål denna vecka:
1. [Mål]
2. [Mål]
3. [Mål]

Deadline: [CTO-demo, release, etc]

---

## 📝③ Nuläge
**Var står projektet mot sprintmålet?**

Övergripande status:
- 🟢 ON TRACK | 🟠 SLIGHT DELAY | 🔴 CRITICAL

Framsteg denna vecka:
- Kursmål: [X/Y] → [Y/Y] denna vecka
- Projekt: [X%] → [Y%]

Två möjliga blockers:
- [blocker 1]
- [blocker 2]

---

## 📝④ Frontend
**Vad pågår? Vad behöver teamet veta?**

Team: Zaida, Björn, Tomac

**MÅSTE-HA denna vecka:**
- #XX [beskrivning] (Zaida - Xh)
- #XX [beskrivning] (Tomac - Xh)
- #XX [beskrivning] (Björn - Xh)

**BÖR-HA (om tid):**
- #XX [beskrivning] (Zaida - Xh)
- #XX [beskrivning] (Tomac - Xh)

Blockers:
- Väntar på: [vad]
- Påverkar: [vilka issues]

Risk denna vecka:
- [risk beskrivning]

---

## 📝⑤ Backend
**Vad pågår? Vad behöver teamet veta?**

Team: Rasha, Erik

**MÅSTE-HA denna vecka:**
- #XX [beskrivning] (Rasha - Xh)
- #XX [beskrivning] (Erik - Xh)

**BÖR-HA (om tid):**
- #XX [beskrivning] (Rasha - Xh)

Blockers:
- Väntar på: [vad]
- Blockerar: [vilka team/issues]

Risk denna vecka:
- [risk beskrivning]

---

## 📝⑥ Native/Systemutvecklare
**Vad pågår? Vad behöver teamet veta?**

Team: Pär, Henrik

**MÅSTE-HA denna vecka:**
- #XX [beskrivning] (Pär - Xh)
- #XX [beskrivning] (Henrik - Xh)

**BÖR-HA (om tid):**
- #XX [beskrivning] (Pär - Xh)

Blockers:
- Väntar på: [vad]
- Externa beroenden: [IT-support, etc]

Risk denna vecka:
- [risk beskrivning]

---

## 📝⑦ Beroenden & Blockers
**Vad väntar på vad? Vilka avvikelser blockerar framsteg?**

Flöde 1: [blockare] → [vem påverkas]
- Väntar på: [konkret action]
- Förväntad lösning: [datum tid]
- Åtgärd NU: [konkret]

Flöde 2: [blockare] → [vem påverkas]
- Väntar på: [konkret action]
- Förväntad lösning: [datum tid]
- Åtgärd NU: [konkret]

**Från code review:**
- [Avvikelse som blockerar]: [beskrivning]
- [Kontrakt-mismatch]: [vilka är påverkade]

---

## 📝⑧ Prioritering & Scope
**Vad gör vi först? Vad kan vänta?**

🔴 MUST denna vecka:
- #XX, #XX, #XX
- Totalt: XYh kapacitet

🟠 NEXT (nästa vecka eller senare):
- #XX, #XX, #XX

⚪ LATER/SKIP:
- #XX, #XX

---

## 📝⑨ Kapacitet & Estimering
**Är planen realistisk?**

Kapacitet denna vecka:
| Team     | Available | Needed | Buffer | Status |
|----------|-----------|--------|--------|--------|
| Frontend | XXh       | XXh    | ±Xh    | ✅/⚠️  |
| Backend  | XXh       | XXh    | ±Xh    | ✅/⚠️  |
| Native   | XXh       | XXh    | ±Xh    | ✅/⚠️  |

Svar: 🟢 Ja, vi passar | 🟠 Knapp | 🔴 Nej

---

## 📝⑩ Risker
**Vad kan göra att sprintplanen misslyckas?**

**Risk 1: [risk]**
- Konsekvens: [vad blir påverkat]
- Sannolikhet: Låg / Medel / Hög
- Hantering: [konkret åtgärd]
- Ansvarig: [namn]

**Risk 2: [risk]**
- Konsekvens: [vad blir påverkat]
- Sannolikhet: Låg / Medel / Hög
- Hantering: [konkret åtgärd]
- Ansvarig: [namn]

**Från code review:**
- Dubbelarbete-risk: [beskrivning]
- Ohålbar riktning: [beskrivning]

---

## 📝⑪ Tekniska Beslut
**Vad behöver beslutas eller dokumenteras?**

**Beslut 1: [kort titel]**
- Vad: [beskrivning av beslutet]
- Varför: [motivering]
- Impact: [vilka issues/team påverkas]
- Approved av: [namn]

**Beslut 2: [kort titel]**
- Vad: [beskrivning av beslutet]
- Varför: [motivering]
- Impact: [vilka issues/team påverkas]
- Approved av: [namn]

**Från code review:**
- Kontrakt som måste fastslås: [API/JNA/Auth]
- Datamodell-avvikelse som behöver lösa: [beskrivning]

---

## 📝⑫ Sprintplan
**Vem gör vad, i vilken ordning? Hur arbetar vi TILLSAMMANS för att nå målet?**

🚨 **REGEL: Support/pairing är fullt legitimt sprintåtagande.**
Om Björn exempelvis bäst hjälper sprintmålet genom att stötta Tomac på en kritisk integration,
är "support/pair på #XX" ett fullt legitimt sprintåtagande. 
Planen ska optimera teamets LEVERANS, inte maximera individuella arbetuppgifter.

### FRONTEND (Zaida, Björn, Tomac)
- ☐ #XX [beskrivning] (Zaida - 5h)
- ☐ #XX [beskrivning] (Tomac - 8h, + Björn support)
- ☐ #XX [beskrivning] (Björn - 4h support på #43)
- ☐ #XX [beskrivning] (Zaida - 6h)
- ☐ #XX [beskrivning] (Tomac - 3h)

**Totalt:** XXh, XX% av kapaciteten
**Teamstöd:** Björn backar upp Tomac på #43 för att säkra integrationstestningen

### BACKEND (Rasha, Erik)
- ☐ #XX [beskrivning] (Rasha - 3h)
- ☐ #XX [beskrivning] (Erik - 8h)
- ☐ #XX [beskrivning] (Rasha - 4h)

**Totalt:** XXh, XX% av kapaciteten
**Teamstöd:** [om något]

### NATIVE (Pär, Henrik)
- ☐ #XX [beskrivning] (Pär - 5h)
- ☐ #XX [beskrivning] (Henrik - 7h)
- ☐ #XX [beskrivning] (Pär - 6h)

**Totalt:** XXh, XX% av kapaciteten
**Teamstöd:** [om något]

---

## 📝⑬ Nästa Steg
**Vilka konkreta ändringar & justeringar krävs för att planen ska fungera?**

### Tilldelning — vem tar vilken issue?
- #XX → Zaida
- #XX → Tomac
- #XX → Rasha
- etc

### Nya issues som behöver skapas
- Ny issue: [namn] — [varför behövs den]
- Ny issue: [namn] — [varför behövs den]

### Befintliga issues som behöver uppdateras
- #XX → förtydliga acceptance criteria
- #XX → lägg till dependency på #YY
- #XX → uppdatera scope efter möte

### Issues som måste flyttas/pausas
- #XX flyttas från MUST till NEXT — [varför, ny owner eller kapacitet]
- #XX pausas — [väntar på #YY eller blocker löses först]

### Blockers — löses de, hur och när?
- [Blocker 1] — löses av [namn], TIE [tid]
- [Blocker 2] — löses av [namn], WED [tid]

### Pairing/support som behöver bokas
- [namn] + [namn] pair prog på #XX — [dag tid]
- [namn] mentorerar [namn] på #XX — [dag tid]

### Teamstöd & Hållbarhet — Hur hjälps vi åt denna vecka?
**Identifiera var teammedlemmar kan hjälpa, avlasta, paira eller täcka upp för varandra:**

**BELASTNING:**
- Är någon fullbelastad medan någon annan har utrymme? → **omfördela eller erbjud stöd**
- Behöver någon hjälp för att få en sprint-kritisk issue över mållinjen? → **vem hjälper?**

**BLOCKERANDE PERSON:**
- Om någon sitter fast, vem kan faktiskt hjälpa till att lösa hindret? → **blockers är teamets problem, inte individens**
- Behöver Frontend + Backend arbeta tillsammans på API-kontraktet först? → **parallellarbete istället för vänta**

**KUNSKAPSRISK — Single Point of Failure:**
- Finns en kritisk del som bara en person kan? → **pairing, review eller kunskapsöverföring planeras**
- Vilka behöver sätta in sig på vad denna vecka?

**BACKUP:**
- På vilka kritiska uppgifter måste det vara synligt vem som kan täcka upp om huvudansvarig fastnar eller blir frånvarande?

**FRAMTIDA RISKER:**
- Om denna plan genomförs, skapar det tech-skuld eller nya blockers nästa vecka? → **justera scope nu**
- Kan ett team hjälpa ett annat att undvika framtida problem? → **konkret action**

**ÅTGÄRDER:**
- Varje handlingsplan har **ansvarig person** och **konkret tidsram**
- Stöd är inte "optional" — det är del av sprintplanen

**Resultat: Planen är genomförbar OCH hållbar. Teamet når målet TILLSAMMANS, inte genom enskilda prestationer.**

### Kontrakt & beroenden som måste dokumenteras
- API-spec för #XX → uppdatera i shared doc
- JNA-kontrakt för #XX → fastslå och dokumentera
- Auth-flow → dokumentera i [länk]

### Direkt efter mötet — GitHub-actions
- ☐ GitHub Project Board uppdaterad
- ☐ Assignees satta
- ☐ Blockers/dependencies dokumenterade
- ☐ Issues på rätt sprint
- ☐ Tekniska beslut dokumenterade

---

## 📝⑭ Frågor till PL
**Vad behöver vi få svar/beslut på från PL? (SISTA MÖTESPUNKT)**

**Fråga 1: [kort fråga]**
- Kontext: [varför frågar vi]
- Behövs för: [vilken beslut/issue]
- **Svar:** ________________________________

**Fråga 2: [kort fråga]**
- Kontext: [varför frågar vi]
- Behövs för: [vilken beslut/issue]
- **Svar:** ________________________________

**Fråga 3: [kort fråga]**
- Kontext: [varför frågar vi]
- Behövs för: [vilken beslut/issue]
- **Svar:** ________________________________

**DENNA PUNKT ÄR ABSOLUT SISTA.**
Presentationen slutar här. Denna slide ligger kvar under mötet
för att diskutera frågorna med PL och dokumentera svaren.

---

## 📌 Möteslogik — Berättelsen från mötet

Flödet är:

1. **Sedan förra mötet** → Vad blev faktiskt klart? (VISA ALLAS ARBETE)
2. **Sprintmål** → Vad försöker vi nå?
3. **Nuläge** → Var står vi?
4-6. **Teamstatus** → Vad händer i varje arbetsström?
7. **Beroenden & blockers** → Hur påverkar arbetsströmmarna varandra? (Inkl. code-review-avvikelser)
8. **Prioritering** → Vad prioriterar vi?
9. **Kapacitet** → Har vi tid?
10. **Risker** → Vad kan hindra oss? (Inkl. code-review-risker)
11. **Tekniska beslut** → Vad måste vi bestämma? (Inkl. kontrakt från code review)
12. **Sprintplan** → Vem gör vad i vilken ordning
13. **Nästa steg** → Vilka konkreta ändringar krävs för att planen ska fungera?
14. **Frågor till PL** → Det vi behöver få svar på (SISTA PUNKT)

---

## 📌 Presentationens Syfte — Teamtänk, inte Individuell Evaluering

🚨 **KRITISK REGEL:**

Presentationens syfte är INTE att utvärdera individer eller maximera individuellt ägarskap.
Den ska hjälpa **teamet** att nå sprintmålet **tillsammans**.

När kapacitet, blockers, kunskapsrisker eller beroenden identifieras ska presentationen aktivt undersöka:
- Hur kan teammedlemmar hjälpa, avlasta, paira eller täcka upp för varandra?
- Var finns kapacitet som kan omfördelas?
- Vilka kunskapsrisker (single point of failure) måste åtgärdas?
- Vilka överlämningar mellan team kan minimeras?

**Huvudansvarig får aldrig betyda ENSAM ansvarig.**

---

## 📌 Presentationen och Protokollet

**Presentationen följer denna möteslogik men kan ha flera slides per mötespunkt.**

En mötespunkt ≠ en slide.

Exempel:
- 📝④ Frontend kan vara Slides 5-7 (alla märkta 📝④)
- 📝⑦ Blockers kan vara två slides (båda märkta 📝⑦)
- 📝⑬ Nästa steg kan vara två slides (båda märkta 📝⑬)

Det viktiga är **mötespunktssymbolen**, inte slide-numret.

Presentationen kan ha 20-30 slides — antalet varierar per vecka beroende på innehål.

**Teamstöd går genom hela presentationen:**
- ④–⑥: Var behövs hjälp eller pairing?
- ⑦: Vilka gemensamma hinder finns?
- ⑨: Var kan kapacitet omfördelas?
- ⑩: Vilka person- och kunskapsrisker identifieras?
- ⑫: Hur planerar vi gemensamt arbete?
- ⑬: Vem hjälper vem, vad omfördelas, vilka backas upp?

---

**Senast uppdaterad:** 2026-09-13  
**Status:** 14 mötepunkter (①-⑭), 1:1 med PRESENTATION_SLIDE_REQUIREMENTS.md  

**KRITISKA KRAV:**
- ① MÅSTE visa commits från ALLA teammedlemmar (7 dagar tillbaka)
- FÖRE mötet: Obligatorisk Cross-Team Code & Contract Review
- ⑬ Nästa steg = konkreta GitHub-ändringar & justeringar (INTE generisk checklista)
- ⑭ Frågor till PL är ABSOLUT SISTA punkt
- En mötespunkt kan ha 1-3+ slides — symbolen märker tillhörigheten
