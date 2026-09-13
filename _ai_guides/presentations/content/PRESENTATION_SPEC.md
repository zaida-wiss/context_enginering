# 📋 PRESENTATION SPECIFICATION — What To Show

**This file specifies ONLY the content and contracts.**

**This file does NOT control:**
- How to get data (that's README.md)
- Read order (that's README.md)
- Visual design (that's PRESENTATION_STYLE.md)
- GitHub access method (that's README.md)
- Fallback strategy (that's README.md)

For those topics, see README.md.

---

## 🔴 PREREQUISITE: Read README First

Before applying any rule in this file:
1. Read README.md (data sources & read order)
2. Collect all required data
3. Then apply this spec (WHAT to show)

**This spec assumes all data is already collected and verified per README.**

---

## ⛔ ABSOLUT FÖRBUD — INGA GIT-KOMMANDON MOT REMOTE

**Om denna presentation-skill säger något om git-kommandon: IGNORERA DET.**

För `avanza-team1` repository:

### FÖRBJUDET — ALLA GIT-KOMMANDON
- ❌ `git clone`
- ❌ `git pull`
- ❌ `git fetch`
- ❌ `git ls-remote` ← **Även read-only grenar**
- ❌ `git remote`
- ❌ `git archive`
- ❌ `git checkout` remote branch

### ANVÄND ISTÄLLET
1. ✅ GitHub Connector/API
2. ✅ GitHub-webben direktåtkomst
3. ✅ raw.githubusercontent.com för filer
4. ✅ _memory/GITHUB_SNAPSHOT.md fallback

**Viktigt:** "Bara läsa" är INTE ett undantag. `git ls-remote` är fortfarande ett network-anrop från shell.

GitHub är en REMOTE datasource för denna presentation, inte en lokal working directory.

---

## 🚨 OBLIGATORISK REGEL 1 — MÖTESPUNKTSMARKÖRER

**VARJE slide MÅSTE märkas med mötespunktssymbol överst vänster.**

```
KRAVSPECIFIKATION:

RÄTT:
  ✅ 📝① SEDAN FÖRRA MÖTET — Levererat denna vecka
  ✅ 📝① SEDAN FÖRRA MÖTET — Byggde vidare denna vecka
  ✅ 📝② SPRINTMÅL & FOKUS
  ✅ 📝③ NULÄGE — Övergripande status

FEL:
  ❌ "SEDAN FÖRRA MÖTET — Levererat denna vecka" (ingen symbol)
  ❌ "Nuläge" (saknas symbol, rubrik tydlig men inte märkad)
  ❌ 📝⑤ "Något helt annat" (helt vit symbol)

RULE: Om presentationen har slide utan symbol = presentationen är FELBYGGD
      även om innehållet råkar matcha rätt mötespunkt

VARFÖR: Symbolerna navigerar mötet. Utan dem kan inte mötesledaren
        snabbt hitta rätt del av presentationen.
```

**Source:** PRESENTATION_STRUCTURE.md definierar alla 14 mötespunkter (📝①-⑭)

---

## 🚨 OBLIGATORISK REGEL 2 — DATA SOURCES ENDAST FRÅN REPO & GITHUB

**Presentationen MÅSTE rekonstrueras ENDAST från:**
- ✅ context_enginering repo (PRESENTATION_SPEC.md, STYLE.md, etc)
- ✅ GitHub Project data denna vecka (issues, PRs, commits)
- ✅ Meeting protocol denna vecka (Google Docs från README)
- ✅ Google Sheets fallback (från DATA_SOURCES.md)

**Presentationen MÅSTE ALDRIG använd:**

```
❌ FÖRBJUDET: Tidigare konversationer eller chathistorik
   Exempel: "Vi diskuterade att containers borde..."
   
❌ FÖRBJUDET: Design-intuition från andra presentationer
   Exempel: "Det här såg bra ut på föregående möte..."
   
❌ FÖRBJUDET: Personliga minnesanteckningar
   Exempel: "Jag tror Jan arbetade på..."
   
❌ FÖRBJUDET: Antaganden utan GitHub-verifiering
   Exempel: "Frontend-teamet verkar vara på rätt väg"
   
✅ TILLÅTET: GitHub commits, PRs, issues (verifierad data från denna vecka)
✅ TILLÅTET: Meeting protocol från denna vecka
✅ TILLÅTET: Context-repo regler och templates
✅ TILLÅTET: Project Board status (med filter för Board vs Issues divergens)

❌ FÖRBJUDET: Presentationen uppfinner eller skapar nya issues
   Exempel: "Vi borde ha en issue för..." → INTE på presentation-slides
   
✅ TILLÅTET: Förslag på nya issues → ENDAST på en separat sida märkt TYDLIGT "Förslag"
   Regel: Issue-förslag får ALDRIG blandas med verifierad GitHub-data
   Regel: Varje förslag-issue MÅSTE ha "FÖRSLAG:" prefix
   Regel: Förslag-sidan är OPTIONAL och kommer EFTER all GitHub-data
```

**VARFÖR DENNA REGEL FINNS:**

ChatGPT-presentationen från förra veckan:
- Saknade Björn's design system arbete (#79)
- Saknade Native risk motor arbete (#92)
- Saknade andra commits/PRs som inte var explicita issues

Root cause: Modellen läste "intuitiv kontext" från konversation
           istället för att metodiskt gå genom alla GitHub-data

**MEKANISK KONTROLL:**

Presentationen kan verifiera sig själv:
```
För varje issue/PR/commit som visas:
  ☐ Kan jag citera GitHub-länken?
  ☐ Kan jag se issue/PR/commit-hash på GitHub?
  ☐ Kan jag visa merge-datum från GitHub?
  
Om något svar är NEJ → datan kom från konversation, inte repo
  → Presentationen är INVALID och måste byggas om från GitHub
```

---

## 📋 READING CHECKLIST — Innan Du Börjar Presentationen

**Du behöver läsa DESSA filer för att skapa presentation:**

```
☐ DENNA FIL (PRESENTATION_SPEC.md) — du läser den nu
☐ _ai_guides/presentations/models/WEEKLY_PROGRESS_MODEL.md — för "Sedan förra mötet"-sliden
☐ _memory/DEFINITION_OF_DONE.md — FÖR DENNA VECKA (krävs för att verifiera "klart")
☐ _ai_guides/presentations/structure/PRESENTATION_STRUCTURE.md — för slide-ordning & mötespunkter
☐ GitHub-data denna vecka (via GitHub Connector/API per README.md)
  - Commits sedan förra möte
  - Merged PRs
  - Closed Issues
  - Open Issues/PRs med aktivitet
☐ Mötesprotokollet från denna vecka (Google Docs-länk från README.md)
☐ GitHub Project Board status denna vecka
  - https://github.com/orgs/chas-challenge-2026/projects/31/views/1

DU BEHÖVER INTE LÄSA (dessa är referens endast):
  ✗ avanza-team1 README (bara läs vid behov för specifik kod)
  ✗ KURSMAL_OCH_BETYG.md (inte relevant för presentation)
  ✗ Gamla möten/protokoll (bara DENNA vecka räknas)

MINNESRENSNING (obligatorisk före läsning):
  1. Glöm allt minne från denna vecka
  2. Glöm möten, diskussioner, tidigare presentationer
  3. Läs ENDAST filerna ovan, ingenting annat
  4. Börja helt clean
```

**KRITISKT: Definition of Done (DoD) är obligatorisk läsning.**
- Varje issue klassificerad som 🟢 KLART DENNA VECKA måste verifiera mot denna veckas DoD
- DoD avgör om något är faktiskt färdigt eller bara "moved to Done on board"

---

## ❌ EXEMPEL I INSTRUKTIONER ≠ EXEMPEL I PRESENTATION

**Kritisk regel:** Exemplen i denna fil är BARA för att förklara reglerna. De är ALDRIG mall för presentationen.

```
🔴 FEL — Kopierade namn från instruktioner:
"Instruktionerna säger 'Zaida fortsätter #42'"
→ Presentationen visar "Zaida fortsätter #43" (kopierad struktur, byta nummer)
→ PROBLEM: Zaida kanske inte ens hade aktivitet denna vecka!

🔴 FEL — Kopierade team-ordning:
"Instruktionerna visar 'Frontend, Backend, Native'"
→ Presentationen visar samma team i samma ordning
→ PROBLEM: Det är instruktions-ordning, inte faktisk prioritering denna vecka

✅ RÄTT:
"Instruktionerna visar HUR man skriver"
→ Presentationen visar BARA namn från verifierad GitHub-aktivitet denna vecka
→ Ordning och fokus baserad på faktisk data, inte exempel-ordning
→ Exempel-namn slötas helt efter verifiering-sliden
```

**MANDATORY RULE:**

Efter att "Alla i teamet" verifiering-sliden körs:

1. ✅ Slut på exempel-namn — använd BARA verifierade namn från denna slide
2. ✅ Om Zaida finns på verifiering-sliden → kan nämnas senare
3. ❌ Om Jan INTE finns på verifiering-sliden → får INTE nämnas senare (om inte ny GitHub-data dök upp)
4. ❌ Presentationen får ALDRIG växla mellan "verifierad" och "exempel"

Presentationen ska ha:
- **Faktiska namn från GitHub denna vecka** (inte exempel-namn från instruktioner)
- **Faktiska team-ordning denna vecka** (inte instruktions-ordning)
- **Balanserad täckning** (alla medlemmar som HAD aktivitet)

---

## 🚨 NO META-INSTRUCTIONS ON SLIDES

**AI-regler, presentationsspecifikationer, formatteringsregler, validators och instruktioner om hur presentationen skapas får ALDRIG visas för mötesdeltagarna.**

ENDAST resultatet av reglerna får synas.

**Exempel på vad som är INSTRUKTION (får inte på slide):**
- "Assignee på varje aktiv issue och särskilt (#XX - Namn)"
- "5-sekunders-testet för visual-first"
- "Render QA checklist"
- "Verifiera brancher mot develop"
- "Denna regel är tvingande"
- "AI ska analysera integrations-kedjor"

**Exempel på vad som är MÖTESINNEHÅL (får vara på slide):**
- "#43 – API client · ?? (Beslut idag: vem tar detta?)"
- Integration-diagram med Zaida, Rasha, Pär + branches
- "🟠 Behöver synkas: login request/response"
- "Backend-branch ligger 75 commits efter develop"
- "Fallback-arbete: Frontend testning (oberoende)"

**Publiktest för varje textrad:**
```
"Skulle en projektledare säga detta till teamet på mötet,
utan att förklara att en AI skapade presentationen?"

Om nej → Ta bort texten från sliden.
```

---

---

## 🚨 PROJECT LEAD REVIEW — MANDATORY BEFORE POINT ⑫ RENDERS

**DENNA CHECKLISTA VISAS ALDRIG PÅ SLIDE — den är bara internt för AI.**

Innan point ⑫ (Sprintplan) byggs ska AI:n genomföra följande kontrollfrågor på verifierad projektdata.

Visa endast relevanta fynd på sliden, aldrig checklistan själv.

### SCOPE REVIEW
- ✅ Vad måste bli klart för sprintmålet?
- ✅ Vad är nice-to-have (kan skjutas upp)?
- ✅ Finns arbete utan tydlig koppling till målet?
  → Om ja: föreslå att prioritera ned detta

### DELIVERY REVIEW
- ✅ Vad är kritisk väg? (vem → vem → vem)
- ✅ Vad måste göras först för att andra ska kunna arbeta?
- ✅ Finns en demonstrerbar vertikal slice denna vecka?
  → Om nej: föreslå en eller justera prioritering

### OWNERSHIP REVIEW
- ✅ Har varje planerad issue en faktisk ägare?
  → Om nej: markera som "Behöver ägare" eller föreslå assignee
- ✅ Har någon för mycket kritiskt arbete?
  → Om ja: föreslå omfördelning
- ✅ Finns arbete utan ägare?
  → Om ja: lägg till i "Beslut idag"

### DEPENDENCIES REVIEW
- ✅ Vem väntar på oss?
- ✅ Vem väntar vi på?
- ✅ Vad händer om beroendet blir en dag sent?
  → Visar sig i fallback-arbete?
- ✅ Vilket fallback-arbete finns?
  → Om inget: markera som risk

### QUALITY REVIEW
- ✅ Är tester/review/docs planerade som ARBETE?
  → Eller förväntas de bara "hända på slutet"?
- ✅ Finns issues marked Board:Done / Issue:Open?
  → Dessa måste stängas mot DoD denna vecka
- ✅ Finns issues utan AC?
  → Markera som "Behöver AC-klarificering"
- ✅ Finns issues utan DoD?
  → Markera som "DoD saknas"

### BACKLOG HEALTH REVIEW
- ✅ Saknas issue för verifierat arbete?
  → Föreslå nya issues per kategori
- ✅ Finns dubletter?
  → Föreslå att slå ihop
- ✅ Är någon issue för stor för att följa upp?
  → Föreslå att dela upp (med konkreta deluppgifter)
- ✅ Finns issue utan estimat?
  → Markera "Ej estimerad"
- ✅ Finns gamla backlog-items (>2 veckor utan aktivitet)?
  → Föreslå omprioritering eller arkivering

### RISK REVIEW
- ✅ Vilken del av planen är mest sannolik att spricka?
- ✅ Vad blir konsekvensen?
- ✅ Kan ordningen ändras för att reducera risken?
  → Om ja: föreslå ny ordning med orsak

### OUTPUT

Visa endast:
- Relevanta fynd från review
- Konkreta förslag för Board/Backlog-ändringar
- Punkter som teamet måste bestämma på mötet

VISA ALDRIG:
- Checklistan själv
- AI-instruktionerna
- Generiska råd utan verifierad grund

---

## 🎯 Presentationens Tre Syften

1. **TEAMTÄNK** — Hjälpa teamet att nå sprintmålet tillsammans, inte rapportera individuella insatser
2. **BRANSCHPEDAGOGIK** — Lära teamet domänvokabulär medan vi arbetar
3. **TEAMSTÖD** — Identifiera var hjälp behövs och omfördela kapacitet

---

## 🚨 KRITISK DISTINKTION: Project Board Status ≠ GitHub Issue State

**VIKTIGT:** Dessa är två OLIKA saker:

```
Project Board Status (Done/In Progress/Backlog)
    ≠
GitHub Issue State (Open/Closed)
```

**Exempel på möjliga kombinationer:**

| Board | Issue | Betyder |
|-------|-------|---------|
| Done | Open | Arbetet är på boarden färdigt, men issuen är fortfarande öppen (kvar till DoD) |
| Done | Closed | Arbetet är helt slutfört enligt DoD |
| In Progress | Open | Normalt tillstånd — arbetet pågår |
| In Progress | Closed | Onormalt — closed issues bör inte aktiveras igen |
| Backlog | Open | Inte påbörjat ännu |
| Backlog | Closed | Beslutad att inte göra denna sprint |

**För presentation — visar ALLTID båda:**

```
❌ DÅLIGT: "#42 – Login page är klart"
✅ RÄTT: "#42 – Login page (Zaida) · Board:Done · Issue:Open · DoD: Review✓ Tests✓ Docs⏳"
```

**DoD är vad som gör issuen faktiskt "färdig"** — inte bara Board:Done och inte bara Issue:Open.
Se DEFINITION_OF_DONE.md för vad som krävs.

---

## 📌 Issue Format — Enda Giltiga Format

**VARJE issue-referens MÅSTE följa detta format, överallt:**

```
#40 – Login page · Zaida
#43 – API client · Erik (förslag)
#48 – Risk dashboard · ??
```

**Tolkning:**
- `#40 –` = issue-nummer med bindestreck
- `Login page` = kortfattad titel
- `·` = mitternpunkt som separator
- `Zaida` = faktisk assignee
- `Erik (förslag)` = föreslaget namn (ännu ej bekräftat)
- `??` = okänd assignee (behöver beslut på mötet)

**Detta gäller överallt:**
- Issue-tabeller
- Risk-kort
- Dependency-diagram
- Footnotes
- Sprint goals
- Löptext

Ingen issue-referens får sakna assignee-information.

---

## 🎨 Färgsemantik — Förbjudna & Obligatoriska Regler

**PRINCIP: Färg är semantik, aldrig dekoration. Varje färg måste betyda något.**

### Status-Färger (Endast För Faktisk Status)

```
🟢 GRÖN = Verifierat bra / Klart / On track / Låg risk
🟡 GUL = Behöver uppmärksamhet / Beslut ausstående
🟠 ORANGE = Risk / Osäkerhet / Kapacitets-/beroenderisk
🔴 RÖD = Blockerad / Kritisk risk / Måste agera omedelbar
```

**STRIKT REGEL:**
Dessa färger får ENDAST användas när elementet faktiskt kommunicerar denna status.
Om du måste förklara "det betyder inte verkligen rött" → använd neutral färg istället.

### Neutral Färger (För All Övrig Information)

```
🔵 Marinblå = Huvudrubriker, viktig struktur
🔵 Ljusblå = Neutral information, processer, tekniska samband
⚫ Blågrå / Ljusgrå = Vanliga informationskort, team-kort
⚪ Vit = Luft, huvudytor, negativt utrymme
```

### Accent-Färger (Icke-Status Syften)

```
💜 Lila = Sprintplanering, beslut, prioriteringar, förslag, "nästa steg"
🌸 Dämpad rosa = Människor, ägarskap, assignees, samarbete
```

### BORDER-FÖRBUDSREGEL

```
🚨 STRIKT: Röda, orange, gröna eller gula borders är FÖRBJUDNA på neutral mark.

❌ FELAKTIGT:
  [Neutral teamkort med grön border]  ← ser ut som "bra status" men är bara struktur
  [Neutral risklista med orange border] ← förbisningen risker
  [Neutral issue-container med röd border] ← får oläslig prioritet

✅ KORREKT:
  [Neutral grå teamkort → liten 🟠 markering bredvid "API dependency"]
  [Neutral grå riskkort → 🔴 indikator på kritisk item, inte hela kortet]
```

**Om ett neutralt element innehåller status:** Visa status med liten lokaliserad indikator INNANFÖR kortet, aldrig genom att färga hela kortet eller ramen.

### Preflight-Kontroll

Presentationen **misslyckades** om:
- [ ] En neutral ruta har grön border
- [ ] En neutral ruta har orange border
- [ ] En neutral ruta har röd border
- [ ] En hel teamruta färgas efter en enskild risk
- [ ] En färg används utan att kunna förklara dess status-betydelse

---

## ⚡ Risk / Dependency / Blocker — Definitioner & Format

### Risk
```
Potentiell framtida problem som kan påverka sprint-leverans.

OBLIGATORISK STRUKTUR:
  Risk: [namn]
  Nuläge: [faktisk situation nu]
  Konsekvens: [vad händer om det inträffar]
  Sannolikhet: 🟢 / 🟡 / 🟠 / 🔴
  Åtgärd: [vad gör vi]
  Ägare: [vem ansvarar]
```

### Dependency
```
Arbetet är beroende av något annat, men produktivt arbete KAN fortsätta.

OBLIGATORISK STRUKTUR:
  Dependency: [namn]
  Väntar på: [vad/vem]
  Blockerar: [vilka uppgifter]
  Fallback-arbete: [vad kan vi göra istället denna vecka]
  Förväntat löst: [datum]
```

### Blocker
```
Aktuellt arbete KAN INTE fortsätta utan detta löst.

OBLIGATORISK STRUKTUR:
  Blocker: [namn]
  Blockerar: [vilka uppgifter / vilket team]
  Root cause: [varför kan arbetet inte fortsätta]
  Åtgärd: [vad gör vi NU]
  Ägare: [vem ansvarar]
  Förväntat löst: [tid/datum]
```

### Team Blockerad (Inte Bara Ett Beroende)
```
Teamet saknar produktivt oberoende arbete att göra.

KAN BARA HÄNDA OM:
- Alla kritiska beroenden är obeslutade/okända
- Fallback-arbete saknas eller är också blockerat
- Team-medlemmar kan inte rediriera till annan MVP-feature

ÅTGÄRD: Omfördela från annat team eller prioritera annan feature.
```

---

## 📊 Sprint-Planering: Kapacitet & Avlastning

### Obligatorisk Struktur

```
KAPACITET → KRITISK VÄG → KAN AVLASTA → HUR

Exempel:

FRONTEND
  Tillgänglig: 60 timmar denna vecka
  Kritisk väg: #40 Portfolio (20h) + #43 Risk calc (25h) = 45h
  Margin: 15h
  
  Kan avlasta: Ja
    · API-kontrakt & mock-data prep (5h)
    · Integrations-tests setup (5h)
    · Target-allocation responsivitet (5h)

RESULTAT: Frontend kan ta #52 Target allocation denna vecka
```

### Fallback-Arbete (Obligatoriskt För Varje Beroende)

**För varje kritiskt beroende: identifiera nästa högst prioriterade OBEROENDE arbete.**

```
FRONTEND PRIMÄRT: #40 Integration med Backend
  ↓ Backend API ej redo → DEPENDENCY

FALLBACK A: #52 Frontend-testgrund (oberoende)
  ↓ (om färdigt snabbare)

FALLBACK B: #55 Target-allocation (oberoende)
  ↓ (om ännu tidigare färdigt)

FALLBACK C: #58 Responsivitet-UX polish (oberoende)
```

Fallback-arbete **måste** hämtas från GitHub Project Board denna vecka — aldrig uppfunna.

---

## ✅ Preflight-Validator (Obligatorisk Innan Leverans)

Presentationen accepteras **INTE** förrän alla dessa kontroller passerar:

```
ISSUE-FORMAT:
  ☐ Varje #XX har assignee eller ?? (ingen exception)
  ☐ Format konsekvent (#XX – Title · Name) överallt
  ☐ Förslag märkta (förslag), inte osäkra

FÄRGKODNING:
  ☐ Grön används ENDAST för faktisk god status
  ☐ Orange används ENDAST för faktisk risk/osäkerhet
  ☐ Röd används ENDAST för faktisk blockering/kritisk
  ☐ Gul används ENDAST för "behöver beslut"
  ☐ Inga statusfärger på neutral mark
  ☐ Inga statusfärgade borders på neutral info
  ☐ Neutral information använder marinblå/grå/vit

INTEGRATION-ANALYS (inbyggd i punkt ⑥ och ⑩):
  ☐ Läst PRESENTATION_STRUCTURE.md punkt ⑥ (Beroenden & blockers)
  ☐ Läst PRESENTATION_STRUCTURE.md punkt ⑩ (Tekniska beslut)
  ☐ Identifierat integrations-kedjor (Frontend API → Backend → Native)
  ☐ API-kontrakt mellan team har avskrivits (punkt ⑩)
  ☐ Beroenden mellan team är märkta (punkt ⑥)
  ☐ Branches som påverkar integration är namngivna
  ☐ Kritiska synk-punkter identifierade och åtgärdade

RISK/BLOCKER/DEPENDENCY:
  ☐ Varje risk har: Nuläge + Konsekvens + Nivå + Åtgärd + Ägare
  ☐ Varje dependency har: Fallback-arbete identifierat
  ☐ Varje blocker har: Root cause + Åtgärd + Förväntat löst
  ☐ Om team är blockerat: Omfördelning eller ny feature föreslagen

KAPACITET & AVLASTNING:
  ☐ Kapacitet visar: Tillgängligt + Kritisk väg + Margin
  ☐ Avlastning analyserad: Kan andra team ta arbete?
  ☐ Fallback-arbete listades för alla dependencies

VISUAL-FIRST & LAYOUT SAFETY:
  ☐ 5-Sekunders-test: Förstår du budskapet utan att läsa brödtext?
  ☐ Finger-test: Kan presentatören peka vägen visuellt?
  ☐ Skumläsnings-test: Förstår du med bara rubriker + symboler?
  ☐ Padding synlig överallt (min 12px inuti boxar)
  ☐ Fontstorlek min 16pt (huvudtext), 14pt (metadata)
  ☐ Ingen text clipped eller överlappar
  ☐ Textblock max 4 rader utan avsnittuppdelning
  ☐ Kort innehåller ≤60% text (≥40% whitespace)

TEAM-SLIDES ACTIONABILITY (FÖR JUNIOR-UTVECKLARE):
  ☐ Varje team har TWÅ slides: "Var är vi?" + "Vad gör vi?"
  ☐ "Vad gör vi?"-slide svarar på FYRA frågor:
    • FORTSÄTT: nästa steg?
    • BEHÖVER STÄNGAS: saknad DoD-krav?
    • KAN TAS NU: oberoende arbete?
    • AGERA PÅ: möte/decision?
  ☐ 5-10 sekundersregel: Junior förstår vad de ska göra utan att läsa allt
  ☐ DoD-status synlig per issue (AC, Tests, Review, Docs checkboxes)

CONTENT SEPARATION (NO META-INSTRUCTIONS):
  ☐ Publiktest: Skulle en PL säga denna textrad på mötet?
  ☐ Ingen AI-instruktioner exponerad (5-sekunders-test, render QA, etc)
  ☐ Inga presentationsregler synliga för teamet
  ☐ Endast resultat av reglerna syns, inte reglerna själva

LESBARHET:
  ☐ Ingen text går utanför sin box
  ☐ Min. 4.5:1 kontrast (WCAG AA)
  ☐ 60-70% whitespace (NPF-vänligt)
  ☐ Varje branschterm på sliden förklaras (inte nya termer i förklaring)

OM NÅGON KONTROLL MISSLYCKAS:
  Presentationen är INTE färdig.
  Åtgärda problemen och genomför validator igen.
```

---

## 📌 Team-Slides: Två-Slide Struktur (Nyckelbeskrivning)

**För Frontend, Backend och Native: Två slides per team.**

### Slide A: "Var är vi?" — ISSUE STATUS TABLE (OBLIGATORISKT FORMAT)

**MÅSTE VISAS SOM EN TABELL — ALDRIG som lista eller generell text.**

Varje aktiv eller relevant issue måste ha en egen rad.

#### OBLIGATORISKA KOLUMNER (i denna ordning):

| Issue | Vad handlar den om? | Ansvarig | Status | AC | Tests | Review | Docs | Git/PR |
|-------|----------------------|----------|--------|----|----|--------|------|--------|

**1. Issue**
- Formatet: `#XX – Faktisk titel från GitHub`
- Titeln hämtas från GitHub Issue, ALDRIG gissad
- Exempel: `#89 – Login page`

**2. Vad handlar den om?**
- En kort mening på vanlig svenska
- VAD som byggs/fixas och gärna VARFÖR det behövs
- Max 1-2 korta rader
- Härledas från issue title + description + acceptance criteria
- Exempel: "Bygger användarens inloggningsflöde och felhantering"

**3. Ansvarig**
- Faktisk GitHub assignee/assignees
- Om flera: visa alla namn
- Om ingen assignee: `⚪ Ej tilldelad`
- Commit author får ALDRIG användas som ersättning för assignee

**4. Status**
- Visa BÅDE Project Board status OCH GitHub Issue state
- Exempel:
  - `Pågår · Open`
  - `Board: Done · Issue: Open`
  - `Klart · Closed`
- Använd 🟢/🟡/🔴 för tydlighet om relevant

**5-8. DoD-Checkpoints (separata kolumner)**

**KÄLLA: Läs DoD från issue-meddelandet på GitHub**

För varje issue:
1. Öppna GitHub issue
2. Läs issue-description/body
3. Hitta "Definition of Done" eller "DoD" sektion
4. Extrahera status för: AC, Tests, Review, Docs
5. Använd för att fylla kolumnerna

Använd:
- `✓` = verifierat uppfyllt (från issue-DoD)
- `◐` = delvis / pågår (från issue-DoD)
- `✕` = verifierat saknas (från issue-DoD)
- `?` = kunde inte verifieras eller DoD saknas i issue-meddelandet

**REGEL:** En check får ALDRIG sättas utifrån antagande. Om DoD-status inte finns i issue-meddelandet: `?`

**VIKTIGT:** AC (Acceptance Criteria) och DoD är OLIKA:
- AC = vad kunden/PO förväntar sig
- DoD = vad utvecklare kräver innan "klart"

Båda kan finnas i samma issue-meddelande, men i separata sektion

**9. Git/PR**
- Relevant PR-status och/eller verifierad aktivitet denna vecka
- Exempel: `PR #104 open`, `PR #98 merged`, `3 commits denna vecka`

#### EXEMPEL PÅ RÄTT FORMAT:

| Issue | Vad handlar den om? | Ansvarig | Status | AC | Tests | Review | Docs | Git/PR |
|-------|----------------------|----------|--------|----|----|--------|------|--------|
| #89 – Login page | Bygger användarens inloggningsflöde och felhantering | Zaida | Pågår · Open | ✓ | ◐ | ? | ✕ | PR #104 open |
| #88 – Risk dashboard | Visar riskindikatorer per projekt | Tomac, Marco | Board: Done · Open | ✓ | ✓ | ◐ | ✕ | PR #101 merged |

#### FÖRBJUDET FORMAT:

❌ `Aktiva issues: #89, #88, #87, #86` (bara lista)
❌ `"Alla issues kräver tester, review och dokumentation"` (generell text)
❌ En gemensam DoD-status för hela teamet (per-issue-basis krävs)

#### VIKTIGT:

- DoD är PER ISSUE, aldrig en generell text för hela teamet
- AC och DoD får inte blandas ihop
- "Board: Done" ger INTE automatiskt ✓ på DoD
- Issue: Closed ger INTE bevis för enskilda DoD-steg
- Om tabellen inte ryms läsbart → dela på flera slides (③A.1, ③A.2, etc)
- Ta ALDRIG bort kolumner eller assignees för att få plats

#### 5-10 SEKUNDERS REGEL:

En person som inte känner till issuen ska på 5-10 sekunder kunna förstå:
- Vad gör vi?
- Vem äger arbetet?
- Hur långt har det kommit?
- Vad återstår innan det faktiskt uppfyller DoD?

### Slide B: "Vad behöver vi göra?" — OPERATIV HANDLINGSPLAN (OBLIGATORISKT)

**SYFTE:**
Efter denna slide ska teammedlemmen direkt förstå:
1. Vad gör vi först?
2. Vem gör det?
3. Vad måste bli klart innan nästa steg?
4. Vem väntar vi på?
5. Vem väntar på oss?
6. Vad kan vi göra om beroendet inte blir klart?
7. Vilka risker behöver diskuteras eller bevakas?

#### OBLIGATORISK STRUKTUR — FYRA SEKTIONER

**A. NÄSTA ARBETE (prioriterad ordning)**

| Prio | Issue | Ansvarig | Nästa konkreta steg | Klart när |
|------|-------|----------|---------------------|-----------|
| 1 | #92 – Riskmotor | Anna | Integrera med Backend API | Tests ✓ + integration verifierad |
| 2 | #93 – … | … | … | … |

- Issue måste följa formatet: `#XX – Titel · Assignee`
- "Nästa konkreta steg" ska vara en faktisk aktivitet (inte "fortsätt arbeta")
- "Klart när" ska kopplas till AC/DoD eller verifierbart resultat

**B. VI VÄNTAR PÅ (inkommande beroenden)**

| Vi behöver | Från team/person | Blockerar | Läge | Förväntat klart | Fallback |
|------------|------------------|-----------|------|-----------------|----------|
| API-kontrakt | Backend (Kiran) | Integration | 🟡 | Fredag 13:00 | Vi börjar med mock-data |
| … | … | … | … | … | … |

VIKTIGT:
- **Dependency** = vi kan fortfarande göra annat produktivt arbete
- **Blocker** = arbetet kan faktiskt inte fortsätta
- Skillnaden är KRITISK för handlingsplanen

**C. ANDRA VÄNTAR PÅ OSS (utgående beroenden)**

| Vi måste leverera | Väntande team | Vad de inte kan göra ännu | Ägare | Deadline |
|-------------------|--------------|----------------------------|-------|----------|
| Riskdata-format | Frontend | Riskvy-gränssnittet | Anna | Torsdag EOD |
| … | … | … | … | … |

Denna sektion är OBLIGATORISK även om teamet självt inte är blockerat.

Om inget verifierat utgående beroende finns:
```
Saknar verifierade team som väntar på oss
```
(INTE en tom ruta)

**D. RISKER ATT DISKUTERA (teamspecifika)**

| Risk | Påverkan | Sannolikhet | Åtgärd | Ägare | Diskutera idag? |
|------|----------|-------------|--------|-------|-----------------|
| Kontrakt ändras sent | Integrationsarbete måste göras om | 🟡 Medel | Lås kontrakt i punkt ⑩ | Anna | 🟢 Ja |
| Backendet blir inte klart i tid | Frontend väntar | 🟠 Hög | Börja med mock-data | Tomac | 🟢 Ja |

VIKTIGT:
- **Risk** ≠ **Blocker**
- Risk: något som KAN inträffa
- Blocker: något som redan hindrar arbete
- "Diskutera idag?" = JA endast om mötet behöver fatta beslut, fördela ansvar eller ändra plan

#### FÖRBJUDET FORMAT:

❌ Generella råd ("Fortsätt med tester", "Stäng DoD", "Ta oberoende arbete")
❌ Lista utan verifierbar koppling till issues eller personer
❌ Samma innehål för två olika team
❌ Tömda beroendsektion ("Inget verifierat beroende") utan att det är faktiskt verifierat

#### EMPTY-STATE RULE:

En kategori får ALDRIG fyllas med generell text bara för att skapa innehåll.

Om verifierad data saknas:
```
Ingen verifierad blocker denna vecka
Inget verifierat utgående beroende
Ingen ny risk identifierad i underlaget
```

Hellre detta än ett generellt råd som ser projektspecifikt ut men är generellt.

**5-10 sekunders regel:** Någon som precis började i teamet ska på 5-10 sekunder kunna svara:
- "Vad ska jag göra nästa?"
- "Vad kan jag ta på mig?"
- "Vem blockar oss?"
- "Vem väntar på oss?"
- "Vad måste vi diskutera på mötet?"

---

## 🔴 ISSUE DATA CONTRACT — Obligatorisk

**Varje gång en issue visas i presentationen MÅSTE detta visas tillsammans:**

```
#42 — Implementera driftanalys
Ansvarig: Lisa
Status: 🟡 Pågår · 3 commits denna vecka
```

### Obligatoriska Fält

- ✅ **Issue-nummer** (#XX)
- ✅ **Titel** (Vad är uppgiften?)
- ✅ **Assignee/Assignees** (Vem är ansvarig?)
- ✅ **Status** (🟢/🟡/🔴 + ord)
- ✅ **Framsteg** (Commits, PR-status, etc)

### ALDRIG

❌ Utelämna assignee för att spara plats  
❌ Ersätt assignee med commit author (de är olika)  
❌ Gissa ansvarig utifrån branch-namn  
❌ Gruppera issues utan att visa vem som äger vilken  

### Om Issue Saknar Assignee i GitHub

Visa:
```
#42 — Implementera driftanalys
Ansvarig: ⚪ Ej tilldelad
Status: 🔴 Behöver ägare
```

### Innan Presentationen Renderas

AI ska skapa ett internt dataset för VARJE issue:

```
- issue_number
- issue_title
- assignees
- github_state (open/closed)
- project_status (Backlog/Ready/In Progress/Review/Done)
- labels
- milestone
- linked_pr
- dod_status
```

**Om `assignees` inte har hämtats:**
→ STOPPA presentationens issue-slides  
→ Försök hämta GitHub-data igen  
→ Presentationen får INTE byggas med ofullständig data

---

## 📝 Mötespunkter (Struktur)

**En mötespunkt ≠ en slide. Presentationen blir 20–30 slides.**

**14 OFFICIELLA MÖTESPUNKTER** (från SPRINT_PROTOCOL_NUMBERED.md):

1. **📝① Sedan förra mötet** — Retrospektiv arbetsöversikt & teamerkännande (2 slides)
   
   **SYFTE:** Ge teamet konkret erkännande för vad de faktiskt arbetade med förra veckan. Sliden ska kännas positiv och visa att arbetet rört sig framåt. INTE en statusrapport — en arbetsverk-överblick.
   
   **PRIMÄR DATAKÄLLA:** Commits sedan förra mötet (från SOURCES.md: GitHub API / commits?sha=develop&since=[MONDAY])
   
   **DATAINSAMLING:**
   1. Läs ALLA commits sedan förra mötet (denna vecka)
   2. Gruppera commits efter issue/branch/arbetsområde (kluster, inte enskilda commits)
   3. Koppla varje cluster mot PRs, issues, Project Board för kontext
   4. Visa ALLT substantiellt arbete som påbörjades eller genomfördes denna vecka
   5. Visa INTE backlog-items utan aktivitet denna vecka
   
   **REGEL: Commit count is evidence, not presentation content**
   - Läs hela commit-historiken för perioden
   - Visa INTE varje commit som egen punkt
   - Sammanfatta arbete per område: "Dashboard — komponenter, styling och responsivitet arbetades vidare med"
   - Format: statusikon + issue/område + beskrivning + person/personer
   
   **Måste inkludera:**
   - 🟢 KLART denna vecka: Merged PRs + Closed Issues med verifiering att arbete faktiskt avslutades
   - 🟠 PÅBÖRJAT denna vecka – FORTSÄTTER: Open Issues/PRs med konkret aktivitet (commits/comments)
   - ! BEHÖVER UPPMÄRKSAMHET: Blockerat/Saknar ägare/Står still
   
   **FÄRGKOD FÖR DENNA SLIDE (VIKTIGT UNDANTAG):**
   - 🟢 = KLART förra veckan (arbete verifierat avslutad: merged, closed eller DoD-markerad)
   - 🟠 = PÅBÖRJAT förra veckan – FORTSÄTTER (pågående arbete med konkret framdrift denna vecka)
   - Orange betyder INTE varning här — det är pågående arbete, inte risk
   
   **Öppning:** En kort positiv sammanfattning överst, tex:
   ```
   Förra veckan flyttade teamet arbetet framåt inom 8 arbetsområden — 
   4 blev klara och 4 fortsätter in i nästa vecka.
   ```
   
   **Format för varje rad:**
   ```
   🟢 #41 Target allocation — formulär, validering och sparflöde färdigställdes — Anna / Erik
   🟠 #43 API client — klientstruktur och mock-adapter påbörjades, fortsätter nästa vecka — Tomac
   ! #45 Auth schema — blockerad på Backend #48, behöver prioriteras
   ```
   
   Se WEEKLY_PROGRESS_MODEL.md för exakt instruktioner om:
   - Vilka datum räknas som "denna vecka"
   - Hur commits + PRs + issues korsrefereras
   - NPF/dyslexia-formattering (symbol + färg + text)
   - Datumformat för "klart 11 sep"

2. **📝② Sprintmål** — Big picture denna vecka

3. **📝③ Nuläge** — Övergripande status mot sprint-mål

4. **📝④ Frontend-Team** (2-3 slides — Var är vi? + Vad gör vi? + Visual Verification)
   - Slide ④A: Issues, assignees, Git-status, DoD-status
   - Slide ④B: FORTSÄTT/BEHÖVER STÄNGAS/KAN TAS NU/AGERA PÅ
   - Slide ④C: Screenshots från dev (om _memory/screenshots/01-login.png finns)
     * Visar arbetet som faktiskt gjort (login flow, dashboard, etc)

5. **📝⑤ Backend-Team** (2-3 slides — Var är vi? + Vad gör vi? + Visual Verification)
   - Slide ⑤A: Issues, assignees, Git-status, DoD-status
   - Slide ⑤B: FORTSÄTT/BEHÖVER STÄNGAS/KAN TAS NU/AGERA PÅ
   - Slide ⑤C: Screenshots från dev (om _memory/screenshots/03-api-response.png finns)
     * Visar API-svar, data-flöde, integration

6. **📝⑥ Native-Team** (2-3 slides — Var är vi? + Vad gör vi? + Visual Verification)
   - Slide ⑥A: Issues, assignees, Git-status, DoD-status
   - Slide ⑥B: FORTSÄTT/BEHÖVER STÄNGAS/KAN TAS NU/AGERA PÅ
   - Slide ⑥C: Screenshots från dev (om _memory/screenshots/04-mobile-view.png finns)
     * Visar mobile-vyn, responsive design, user experience

7. **📝⑦ Beroenden & Blockers + Integration Map** (1-3 slides)
   - Flödesdiagram: vad väntar på vad + fallback-arbete
   - Integration Map (vid behov): Frontend → API → Backend → Native kedjor med status
   - Code-review avvikelser som blockerar

8. **📝⑧ Prioritering & Scope** — Must/Next/Later

9. **📝⑨ Kapacitet & Estimering** — Tillgängligt vs Behövt

10. **📝⑩ Risker** — Risk-matrix med åtgärder + code-review risker

11. **📝⑪ Tekniska Beslut** — Arkitektur-beslut denna vecka + contracts

12. **📝⑫ Sprintplan** — Konkret vem gör vad + support/pairing

13. **📝⑬ Nästa Steg** — Action plan + Teamstöd & Hållbarhet

14. **📝⑭ Frågor till PL** — Discussion board

---

## 🔍 Git-Board Verifiering (Obligatorisk Innan Presentation)

Se **VERIFICATION_BOARD_VS_GIT.md** för detaljer.

**TL;DR:**
- Git är sanningen när Board är stale
- Status-koder: 🟢 Verifierad | 🟣 Git-verified-Board-stale | ⚪ Unverified | 🔴 Konflikt
- Märk alla Board-diskrepanser i presentationen

---

## 📚 Branschpedagogik

**Regel: Förklara bara ord som står på sliden. Aldrig introducera nya termer.**

Varje term ska förklaras simpelt när den förekommer första gången:
```
Risk Dashboard (visar risk-mått: volatilitet = prissvängningar, 
Sharpe-ratio = risk-justerad avkastning)
```

Termer markeras med 📚 för att visa att detta är lärmål.

---

## 📋 COPYABLE MEETING TEXT — Obligatorisk Renderingskrav

**Presentationen tjänar två syften: mötesstöd + sekreterarstöd.**

### Regel: All Text Måste Vara Redigerbar

```
✅ KRÄVS:
- Verklig PowerPoint-text (inte inbakad i bilder)
- Sekreteraren kan markera och kopiera text
- Formuleringarna är kompletta även när de kopieras

❌ FÖRBJUDET:
- Text inbakad i grafikbilder
- Screenshots av slides
- Rasteriserad text
- Decorative text som inte går att kopiera
```

### Användningsfall: Sekreteraren

1. Mötet går
2. Sekreteraren ser på presentationen: "✓ #52 – Portfolio (Rasha) · Gör Frontend-integration möjlig"
3. Sekreteraren markerar och kopierar: `✓ #52 – Portfolio (Rasha) · Gör Frontend-integration möjlig`
4. Sekreteraren klistrar in i mötesprotokollet
5. Protokollet har samma formulering som presentationen

### Textkvalitet

All presentationstext måste vara:
- ✅ **Kompllett** — förvänd utan visuell layout
- ✅ **Tydlig** — samma mening med eller utan farger/ikoner
- ✅ **Verifierad** — ingen stavning/grammatik-fel
- ✅ **Konsekvent** — samma format varje vecka

### Exempel på Rätt Format

```
Presentation visar:
  ✓ #52 – Portfolio health summary (Rasha)
    Gör Frontend-integration möjlig
    Merged PR #81 · 4 commits · klart 11 sep

Sekreteraren kopierar detta direkt:
  ✓ #52 – Portfolio health summary (Rasha)
  Gör Frontend-integration möjlig
  Merged PR #81 · 4 commits · klart 11 sep

Mötesprotokoll får samma text.
```

---

**Senast uppdaterad:** 2026-09-13  
**Syfte:** Canonical specification för alla presentationer  
**Status:** Source of Truth — alla andra filer fördjupar, motsäger aldrig denna
