# 📋 PRESENTATION SPECIFICATION — Source of Truth

**Denna fil är den ENDA auktoritativa specifikationen för presentationer.**  
Andra filer (DESIGN, FORMAT_GUIDE, STRUCTURE) fördjupar denna spec men motsäger aldrig den.

---

## 🔴 CRITICAL EXECUTION ORDER — DATA FÖRE DENNA FIL

**Denna fil läses ENDAST efter att all projektdata är inhämtad (se README.md PHASE 1).**

Om du läser denna fil innan PHASE 1 är klar:
→ STOP
→ Gå tillbaka till README.md
→ Slutför datainsamlingen först
→ Kom sedan tillbaka hit

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

## 📋 READING CHECKLIST — Innan Du Börjar Presentationen

**Du behöver läsa ENDAST dessa filer för att skapa presentation (sparar tokens):**

```
☐ DENNA FIL (PRESENTATION_SPEC.md) — du läser den nu
☐ CROSS_TEAM_INTEGRATION.md — för integrationsanalysen
☐ avanza-team1 projekt-repot (GitHub branches + Git log denna vecka)
☐ Mötesprotokollet (raw-export länk från mötet)
☐ GitHub Project Board status denna vecka

DU BEHÖVER INTE LÄSA:
  ✗ README.md (redan vet du vad du söker)
  ✗ DEFINITION_OF_DONE.md (du behöver inte förstå all projektkontekst)
  ✗ KURSMAL_OCH_BETYG.md (bara relevant för kursöversikt)
  ✗ TEAMSTANDARDS.md (inte relevant för presentation)
  ✗ Gamla möten/protokoll (bara denna vecka räknas)

MINNESRENSNING (obligatorisk innan punkt 1):
  1. Glöm allt minne från denna vecka
  2. Glöm möten, diskussioner, tidigare presentationer
  3. Läs ENDAST dessa filer, ingenting annat
  4. Börja helt clean
```

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

## 🎯 Presentationens Tre Syften

1. **TEAMTÄNK** — Hjälpa teamet att nå sprintmålet tillsammans, inte rapportera individuella insatser
2. **BRANSCHPEDAGOGIK** — Lära teamet domänvokabulär medan vi arbetar
3. **TEAMSTÖD** — Identifiera var hjälp behövs och omfördela kapacitet

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

INTEGRATION-ANALYS:
  ☐ Läst CROSS_TEAM_INTEGRATION.md
  ☐ Läst aktiva brancher (frontend, backend, native)
  ☐ Identifierat integrations-kedjor (Frontend API → Backend → Native)
  ☐ Klassificerat varje kedja (VERIFIERAD/TROLIG/BEHÖVER SYNKAS/MISMATCH/KAN INTE VERIFIERAS)
  ☐ Integration-slide(r) skapade med konkreta branch-namn + personerna
  ☐ Varningr om divergerade brancher (långt efter develop)
  ☐ Kritiska synk-punkter identifierade

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

### Slide A: "Var är vi?"
```
MÅSTE INNEHÅLLA:
✅ Issues med assignee (#XX – Namn)
✅ Git-status denna vecka (commits, branches, stale/active)
✅ Dependencies och blockers (vad väntar på vad)
✅ DoD-status för varje issue (AC ✓, Tests ✓, Review ✓, Docs ✓)

VISUELLT:
- Issues i kolonner (KLAR, PÅGÅR, BLOCKERAD)
- Git-verifiering synlig (commits från vem, denna vecka)
- 🔴🟠🟢 status för varje issue
```

### Slide B: "Vad gör vi åt det?" (ACTIONBAR GUIDE)
```
MÅSTE SVARA PÅ DESSA FYRA FRÅGOR TYDLIGT:

1️⃣ FORTSÄTT — Vad är nästa steg?
   Exempel: "Tomac fortsätter med #43 API-client, lämnar #42 för review"

2️⃣ BEHÖVER STÄNGAS — Vad har vi missat?
   Exempel: "#42 Drift indicator – saknar review, test, docs. Tomac: kan du stänga detta?"

3️⃣ KAN TAS NU — Vad kan vi göra oberoende?
   Exempel: "#87 Frontend test foundation – oberoende av Backend, Zaida kan ta detta"

4️⃣ AGERA PÅ — Vad kräver möte/decision?
   Exempel: "Måndagsmöte: Frontend + Backend måste komma överens om auth-kontrakt"

FORMAT:
Mycket kort, tydligt, actionbar language.
Inte lista av issues — lista av ACTIONS.
```

**5-10 sekunders regel:** Någon som precis började i teamet ska på 5-10 sekunder kunna svara:
- "Vad ska jag göra nästa?"
- "Vad kan jag ta på mig?"
- "Vad behöver ändras?"
- "Vad måste vi prata om?"

---

## 📝 Mötespunkter (Struktur)

**En mötespunkt ≠ en slide. Presentationen blir 20–30 slides.**

**14 OFFICIELLA MÖTESPUNKTER** (från SPRINT_PROTOCOL_NUMBERED.md):

1. **📝① Sedan förra mötet** — Commits från alla team (7 dagar)

2. **📝② Sprintmål** — Big picture denna vecka

3. **📝③ Nuläge** — Övergripande status mot sprint-mål

4. **📝④ Frontend-Team** (2 slides — Var är vi? + Vad gör vi?)
   - Slide ④A: Issues, assignees, Git-status, DoD-status
   - Slide ④B: FORTSÄTT/BEHÖVER STÄNGAS/KAN TAS NU/AGERA PÅ

5. **📝⑤ Backend-Team** (2 slides — Var är vi? + Vad gör vi?)
   - Slide ⑤A: Issues, assignees, Git-status, DoD-status
   - Slide ⑤B: FORTSÄTT/BEHÖVER STÄNGAS/KAN TAS NU/AGERA PÅ

6. **📝⑥ Native-Team** (2 slides — Var är vi? + Vad gör vi?)
   - Slide ⑥A: Issues, assignees, Git-status, DoD-status
   - Slide ⑥B: FORTSÄTT/BEHÖVER STÄNGAS/KAN TAS NU/AGERA PÅ

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

**Senast uppdaterad:** 2026-09-13  
**Syfte:** Canonical specification för alla presentationer  
**Status:** Source of Truth — alla andra filer fördjupar, motsäger aldrig denna
