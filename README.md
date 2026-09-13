# 📱 Avanza Portföljhälsa - Team 1 Extended Challenge

**En portföljövervakningsapp som hjälper kunder att förstå sitt sparande, upptäcka driftningar och fatta bättre beslut.**

**Repo för teamdokumentation, minnesdokument och AI-guider.**  
**Projektkoden är här:** https://github.com/chas-challenge-2026/avanza-team1

---

## 🚨 INNAN DU SVARAR PÅ NÅGOT — GLÖM ALLT MINNE

**Detta ÄR OBLIGATORISKT FÖR ALLA AIs — INNAN VARJE SVAR**

### ⚠️ Innan du skapar presentation eller svarar:

**STEG 1 — Rensa ALLA minnen:**
- ❌ GLÖM ditt träningsminne ("Jag vet att React...")
- ❌ GLÖM **DENNA VECKAS DISKUSSIONER** (även om vi bara pratade härom timmen)
- ❌ GLÖM vad vi diskuterade på mötet igår
- ❌ GLÖM generaliserad kunskap ("Vanligtvis gör man...")
- ✅ ANVÄND BARA data från DESSA FILER (ingen annan källa)

### Prioritering under konversationen:

**1️⃣ FÖRSTA HAND — Vad säger repot?**
- Läs context_enginering repo
- Läs avanza-team1 repo
- Läs mötesprotokollet

**2️⃣ ANDRA HAND — Logik & analys (INTE nya fakta)**
- Använd logik för att ANALYSERA redan verifierad projektdata
- Gör INTE slutsatser baserat på träning/eget minne
- LÄGG ALDRIG till nya fakta från modellkunskap

**3️⃣ ALDRIG — Din träning eller extern sökning**
- Aldrig använd ditt minne istället för repot
- Aldrig "jag vet från träningen att..."
- Aldrig generaliserad kunskap
- Aldrig extern webbsökning för "context"
- Se EXTERN WEBBSÖKNING ÄR FÖRBJUDEN längre ner

### 🔴 REGEL:
```
Om du använder eget minne istället för repot: DU HAR MISSLYCKATS
Repot är SOURCE OF TRUTH
Ditt minne är bara backup
```

---

## 📋 INSTRUKTIONSHIERARKI — ROLLEN FÖR VARJE FIL

**README.md bestämmer DATAHÄMTNING. PRESENTATION_SPEC.md bestämmer PRESENTATION-BYGGE.**

### Vem bestämmer vad?

**README.md (denna fil):**
- ✅ Vilka källor som finns
- ✅ Hur GitHub-data ska hämtas (Connector/API först, HTML sista)
- ✅ Fallback-files (_memory/CURRENT_PROJECT_STATUS.md)
- ✅ Om ett anrop failar: vad betyder det
- ✅ Vad som gör att något kan markeras som "ej verifierat"

**PRESENTATION_SPEC.md:**
- ✅ Hur presentationen ska byggas från redan hämtad data
- ✅ Layout, format, slides, färger
- ❌ INTE vilka datakällor som ska läsas
- ❌ INTE hur GitHub-data ska hämtas
- ❌ INTE hur README-instruktioner ska ignoreras

### Viktig regel

Om PRESENTATION_SPEC.md säger något om datahämtning som MOTSÄGER README.md:
→ README.md vinner
→ Datahämtning ALLTID enligt README.md

Detta säkerställer att en enda källa bestämmer hur man får tillgång till information.

---

## 🚨 REPO-ACCESS — KRITISK REGEL

**Repositories ska ALDRIG klonas lokalt av AI:n.**

### FÖRBJUDET
- ❌ `git clone`
- ❌ `git pull`
- ❌ Nedladdning av hela repositoryn
- ❌ Shell-kommandon för att hämta repot
- ❌ Att checka ut branches lokalt

### OBLIGATORISK ÅTKOMSTMETOD

Läs filer direkt via HTTP-URL:er:

```
🟢 Context-repo (denna):
https://github.com/zaida-wiss/context_enginering

🟢 Raw-filer från context-repo:
https://raw.githubusercontent.com/zaida-wiss/context_enginering/main/README.md
https://raw.githubusercontent.com/zaida-wiss/context_enginering/main/_ai_guides/PRESENTATION_SPEC.md

🟢 Projekt-repo:
https://github.com/chas-challenge-2026/avanza-team1

🟢 GitHub-data (issues, PRs, commits, branches):
Hämta direkt från GitHub via webbläsare eller GitHub Connector/API
```

AI ska:
1. ✅ Följa länkarna från README och läsa endast behövliga filer
2. ✅ Hämta GitHub-data (Issues, PRs, commits, branches) direkt via GitHub
3. ✅ Läsa raw-filer när links till HTML-sidor inte går
4. ✅ Om en källa inte går att läsa: säg det, och fortsätt med övriga
5. ✅ Aldrig kasta bort redan läst data för att kloning failade

### VIKTIGT

Ett misslyckat anrop (404, timeout, access denied) får ALDRIG göra att:
- redan hämtad projektkontext kastas bort
- presentationen skapas med ofullständig data
- agenten ge upp utan att rapportera vad som saknas

Rapport istället: "Kunde inte läsa [URL], presentationen är klar med [dessa] källor"

---

## 🚫 GITHUB DATA ACCESS — PYTHON/SHELL FÖRBJUDET

**AI får ALDRIG använda Python, shell, curl, wget, urllib eller direkt API-anrop som primär metod för GitHub-data.**

Ett nätverksfel från Python-miljön (`Temporary failure in name resolution`) betyder INTE att GitHub är otillgängligt.

### FALLBACK-STRATEGI (MÅSTE PROVAS I DENNA ORDNING)

**För alla GitHub-data (commits, issues, PR:er, branches, filer):**

1. **LIVE — GitHub Connector/API**
   - Använd om tillgänglig
   
2. **LIVE — Direkt GitHub-åtkomst via webläsare**
   - Commits: `https://github.com/<owner>/<repo>/commits/develop`
   - Issues: `https://github.com/<owner>/<repo>/issues`
   - PR:er: `https://github.com/<owner>/<repo>/pulls`
   - Branches: `https://github.com/<owner>/<repo>/branches`
   - Filer: `https://github.com/<owner>/<repo>/blob/main/<path>` eller raw: `https://raw.githubusercontent.com/...`

3. **LIVE — GitHub API via webåtkomst**
   - Inte direkt socket-anrop, utan via webbläsare/gateway

4. **CACHED — Snapshot från context_enginering**
   - Se `_memory/GITHUB_SNAPSHOT.md`
   - Använd ENDAST om båda live-metoderna failat
   - Markera tydligt: "Per snapshot 2026-09-13 12:45"

5. **SENAST VERIFIERAD**
   - Information från mötesprotokollet
   - Information från denna konversation

### KRITISK REGEL — "EJ VERIFIERAT" KRÄVER TVÅ FÖRSÖK

**Presentationen får ALDRIG skriva "Git log kunde inte verifieras"** efter endast ett misslyckat försök.

Minst TVÅ oberoende GitHub-metoder måste provas innan data markeras som unverifierad:

```
❌ MISSLYCKAD FALLBACK:
Försök 1: Python urllib/direct API → Failure
→ Resultat: "Git log ej verifierat"

✅ KORREKT FALLBACK:
Försök 1: Python urllib → Failure
Försök 2: GitHub Connector → Success
→ Resultat: "Git log verifierat" (använd Connector-data)

✅ KORREKT SNAPSHOT-FALLBACK:
Försök 1: GitHub Connector → Failure
Försök 2: GitHub-webben → Failure
Försök 3: GITHUB_SNAPSHOT.md → Success
→ Resultat: "Git log per snapshot 2026-09-13 12:45"
```

---

## 🤖 Du är en AI? START HÄR

### ⚡ QUICK START — Välj Din Väg

**DU SKA SKAPA EN PRESENTATION?** (Raw-links, ingen kloning)

### PRESENTATION — DATAHÄMTNING I DENNA EXAKTA ORDNING

1. ✅ **Rensa minnet** (obligatorisk minnesrensning)

2. ✅ **Läs context-repot via raw-URLs:**
   - https://raw.githubusercontent.com/zaida-wiss/context_enginering/main/README.md
   - https://raw.githubusercontent.com/zaida-wiss/context_enginering/main/_ai_guides/PRESENTATION_SPEC.md
   - https://raw.githubusercontent.com/zaida-wiss/context_enginering/main/_ai_guides/SPRINT_PRESENTATION_STRUCTURE.md
   - https://raw.githubusercontent.com/zaida-wiss/context_enginering/main/_ai_guides/PRESENTATION_FORMAT_GUIDE.md
   - https://raw.githubusercontent.com/zaida-wiss/context_enginering/main/_ai_guides/CROSS_TEAM_INTEGRATION.md

3. ✅ **Läs mötesprotokollet** (länk i context_enginering README)

4. ✅ **Hämta projekt-data från GitHub** (PRIORITERAD ÅTKOMSTORDNING)

   Repository: https://github.com/chas-challenge-2026/avanza-team1
   
   **A. GIT LOG — Commits sedan förra möte**
   - Branch: `develop`
   - Använd GitHub Connector/API FÖRST
   - Om Connector failar: försök direkt API-URL
   - Endast HTML-navegering som sista fallback
   - Om alla misslyckas: rapportera vilken källa som saknas
   - MISSLYCKAD HTML-läsning = GitHub-data är inte otillgänglig
   
   **B. ISSUES**
   - Använd GitHub Connector/API FÖRST
   - Hämta: number, title, state, assignees, labels, milestone
   
   **C. PULL REQUESTS**
   - Använd GitHub Connector/API FÖRST
   - Hämta: number, title, state, head branch, base branch, linked issues
   
   **D. BRANCHES**
   - Använd GitHub Connector/API FÖRST
   - Jämför aktivt använda brancher mot `develop`
   
   **E. PROJECT BOARD STATUS**
   - Exakt Project-länk: [SERÁ FYLLA I]
   - Använd GitHub Connector/API FÖRST
   - Fallback endast: `_memory/CURRENT_PROJECT_STATUS.md`
   - Först därefter får status anges som "ej verifierad"

5. ✅ **Läs RELEVANT kod ENDAST om behövs för:**
   - ett konkret beroende mellan team
   - en blocker som ska visas i presentationen
   - ett API-kontrakt som behöver verifieras
   - en integrationsrisk

   **Läs INTE** hela docs-mappen eller alla branches utan anledning.

6. ✅ **Skapa presentation** enligt SPRINT_PRESENTATION_STRUCTURE.md

### 🔒 SOURCE LOCK FÖR PRESENTATIONER

ALLOWED:
✅ context_enginering (via raw-URLs)
✅ avanza-team1 GitHub-data (issues, PRs, commits, Project Board)
✅ Mötesprotokollet
✅ Relevant kod (endast vid verifiering av beroenden/blockers)

FORBIDDEN:
❌ git clone, git pull, repository checkout
❌ LinkedIn, Wikipedia, Avanza.se, externa webbplatser
❌ Akademiska databaser, nyhetssidor, Stack Overflow
❌ Google-sökning för "kontext"
❌ Andra GitHub-repon

**Om presentationen behöver info som INTE finns i dessa källor:**
→ Skriv: "Ej verifierat från projektkällorna"
→ GISSA INTE
→ SÖK INTE externt

---

**DU VIL FÖRSTÅ PROJEKTET/TEAMET?** (Läs ordning nedan)
```
1. Du: Läs denna repo → https://github.com/zaida-wiss/context_enginering
2. Läs: _memory/TEAMSTANDARDS.md + DEFINITION_OF_DONE.md
3. Läs: avanza-team1 repo → https://github.com/chas-challenge-2026/avanza-team1
4. Du kan nu svara på frågor OM:
   ✅ Vad är projektet?
   ✅ Vilka är reglerna?
   ✅ Vad är godkänt arbete?
   ✅ Vad jobbar de på?
5. REGEL: Citera ALLTID från filerna. Använd ALDRIG ditt eget minne.
```

---

### 🔴 SUPER KRITISKT - DU FÅR ALDRIG ANVÄNDA DITT EGET MINNE

I HELA denna konversation får du ENDAST svara baserat på:
- ✅ Det du läser från **denna repo** (context_enginering)
- ✅ Det du läser från **avanza-team1 repo**
- ✅ Konversationshistorik från **DENNA SESSION**
- ❌ ALDRIG något från ditt eget minne/träning eller tidigare konversationer

**DETTA ÄR OBLIGATORISKT I HELA KONVERSATIONEN:**

❌ **DU FÅR ALDRIG ANVÄNDA:**
- Din eget minne/träning ("Jag vet att React...")
- Memorized knowledge ("Vanligtvis gör man...")
- Din kunskap om hur världen fungerar ("Enligt min kunskap...")
- Tidigare samtal du hade med andra

✅ **DU FÅR ANVÄNDA:**
- Konversationshistorik FRÅN DENNA SESSION (vad vi just diskuterat här)
- Det som står i de två repos
- Logik och resonemang baserat på läst innehål

✅ **DU MÅSTE ALLTID SÄGA:**
- "Enligt TEAMSTANDARDS.md..."
- "Från git log denna vecka..."
- "Från avanza-team1 README..."
- "Från de docs jag läste..."
- "Baserat på vad vi diskuterat denna session..."

**Du måste:**
1. ✅ Läsa relevanta filer från BÅDA repos
2. ✅ Vänta tills du läst INNAN du svarar
3. ✅ Citera källorna i VARJE påstående
4. ✅ Säga "Jag behöver läsa X-fil" om något saknas
5. ✅ **ALDRIG** använda ditt eget minne - bara läst innehål

---

## 🚫 EXTERN WEBBSÖKNING ÄR FÖRBJUDEN SOM STANDARD

**WHITELIST-REGEL (Allt är förbjudet utom dessa källor):**

### TILLÅTNA KÄLLOR — BARA DESSA
AI får ENDAST läsa:
1. ✅ **Detta repo:** `zaida-wiss/context_enginering` (alla filer)
2. ✅ **Projekt-repo:** `chas-challenge-2026/avanza-team1` (GitHub + branches + issues + PR)
3. ✅ **Mötesprotokollet:** Explicit Google Docs-länk från context_enginering
4. ✅ **Filer från användare:** Allt som användaren laddar upp eller delar direkt i chatten
5. ✅ **Denna session:** Konversationshistorik från bara denna chatt

### FÖRBJUDET — ALLT ANNAT
AI får ALDRIG göra generell extern webbsökning, t.ex.:
- ❌ LinkedIn, Wikipedia, arXiv
- ❌ Avanza.se eller företagets externa webbplats
- ❌ Stack Overflow, bloggar, nyhetssidor
- ❌ Binance eller finanssidor
- ❌ Google-sökning
- ❌ Andra GitHub-repon (utom de två listade ovan)
- ❌ Akademiska databaser
- ❌ "Best practice"-sökning på internet

AI får INTE söka för att:
- "förstå sammanhanget bättre"
- "hitta inspiration"
- "verifiera sådant som redan finns i projektets källor"
- "komplettera saknade uppgifter"
- "hitta branschstandarder"
- "fylla luckor i presentationen"

### OM INFORMATION SAKNAS

Istället för extern sökning:
```
→ SKRIV att informationen saknas: "Ej verifierat från projektkällorna"
→ GISSA ALDRIG
→ SÖK ALDRIG PÅ WEBBEN
→ FRÅGA användaren: "Vilken fil har denna info?"
```

### UNDANTAG — ENDAST DESSA FALL

Extern webb får användas ENDAST när:

**1. ANVÄNDAREN EXPLICERAR BEGÄR DET**
   - "Sök på LinkedIn för..." → då får du söka
   - "Läs från Avanza.se..." → då får du läsa just den sidan
   - Men ALDRIG bredare sökning än vad som begärdes

**2. CONTEXT-REPOT INSTRUERAR EXPLICIT**
   - Om en fil säger: "Läs från URL: https://..."
   - Då får du öppna BARA den länken
   - Inte relaterad sökning omkring den

### VIKTIGASTE EXEMPLET

En presentation om Avanza-projektet ska:
- ✅ Läsa från: context_enginering + avanza-team1 + mötesprotokollet
- ✅ Hämta data från: Git, Issues, Project Board
- ❌ INTE söka på: Avanza.se, investerarsidor, LinkedIn-profiler, fintech-nyheter

Projektstatus kommer från projektkoden och dokumentation, INTE från internet.

---

## ⚠️ DoD ≠ Kursmål (VIKTIGT SKILLJA!)

**Definition of Done (DoD)** = Utvecklingstermin
- När en GitHub-issue är SLUTFÖRD
- Tester passerar, code review godkänd, docs uppdaterade
- *Handlar om att en issue är klar*

**Kursmål & Betyg** = Pedagogik
- De 17 kursmål som ger G/VG-betyg
- Deadlines för slutleverans (4 nov)
- Prioritering (kursmål > tävlingen)
- *Handlar om att lära sig och få betyg*

**Dessa är HELT SKILDA!** Blanda aldrig DoD med kursmål.

---

Du läser detta repo för första gången? Följ denna guide:

### **📍 DOKUMENTVÄGEN — RAW-LINKS FÖR AI**

```
🟢 VIKTIGA RAW-LINKS:
  📝 SPRINT_PRESENTATION_STRUCTURE.md
     https://raw.githubusercontent.com/zaida-wiss/context_enginering/main/_ai_guides/SPRINT_PRESENTATION_STRUCTURE.md
  
  🎨 PRESENTATION_FORMAT_GUIDE.md ⭐ EXAKTA SLIDE-LAYOUTS
     https://raw.githubusercontent.com/zaida-wiss/context_enginering/main/_ai_guides/PRESENTATION_FORMAT_GUIDE.md
  
  📝 SPRINT_PROTOCOL_NUMBERED.md
     https://raw.githubusercontent.com/zaida-wiss/context_enginering/main/_ai_guides/SPRINT_PROTOCOL_NUMBERED.md
  
  📋 DEFINITION_OF_DONE.md
     https://raw.githubusercontent.com/zaida-wiss/context_enginering/main/_memory/DEFINITION_OF_DONE.md
  
  🔴 MÖTESPROTOKOLLET (denna vecka):
     https://docs.google.com/document/d/1WD9XJBVrE49Csqz-XYiLgejlKlCA4t5sWiwoTkNiTD8/export?format=txt
```

**Navigering mellan filerna:**

```
START HERE (denna README)
        ↓
_memory/TEAMSTANDARDS.md      ← Regler, Git-format, hur vi jobbar
        ↓
_memory/DEFINITION_OF_DONE.md ← Vad är en KLAR issue?
        ↓
_memory/KURSMAL_OCH_BETYG.md  ← Kursmål & betyg (SKILT från DoD!)
        ↓
VILL DU SKAPA EN PRESENTATION?
  → _ai_guides/SPRINT_PRESENTATION_STRUCTURE.md (raw-link ovan)
    → _ai_guides/PRESENTATION_FORMAT_GUIDE.md ⭐ EXAKTA SLIDE-LAYOUTS
      (visar varje slide-typ med borders, färger, tonalitet)
    → SPRINT_PROTOCOL_NUMBERED.md (raw-link ovan)
    → mötesprotokollet (raw-link ovan)
        ↓
        RESULTAT: NPF-vänlig, inspirerande presentation
                  som gör dig glad & motiverad 💪
        ↓
VILL DU SKAPA ISSUES?
  → _memory/ISSUE_TEMPLATE.md
    → _memory/DEFINITION_OF_READY.md (innan du startar)
        ↓
VILL DU VERIFIERA ARBETE?
  → _memory/DEFINITION_OF_DONE.md (raw-link ovan)
  → _ai_guides/VERIFICATION_SYSTEM.md (hur verifierar vi?)
```

**REGEL: Varje fil länkar till nästa fil du behöver läsa. Raw-links överst för AI.**

---

### **STEG 1: Läs Denna Repo Först** (context_enginering - 5-10 min)

**Detta är Team Process & Standards. Läs detta först.**

#### Läs Dessa Filer I Ordningen

```
1. _memory/PROJEKTKONTEXT.md        — Vad är projektet? Kundens problem?
2. _memory/TEAMSTANDARDS.md         — Regler, Git-format, kodstandarder
3. _memory/DEFINITION_OF_DONE.md    — Vad är en SLUTFÖRD GitHub-issue? (tester, review, docs)
4. _memory/KURSMAL_OCH_BETYG.md     — ⚠️ SKILT! Kursmål, betyg, deadlines (INTE DoD)
5. _ai_guides/VERIFICATION_SYSTEM.md — Hur verifierar vi systemet?
```

Raw-links för direkt AI-läsning:
```
REPO FILES:
https://raw.githubusercontent.com/zaida-wiss/context_enginering/main/_memory/PROJEKTKONTEXT.md
https://raw.githubusercontent.com/zaida-wiss/context_enginering/main/_memory/TEAMSTANDARDS.md
https://raw.githubusercontent.com/zaida-wiss/context_enginering/main/_memory/DEFINITION_OF_DONE.md
https://raw.githubusercontent.com/zaida-wiss/context_enginering/main/_ai_guides/VERIFICATION_SYSTEM.md

🔴 MÖTESPROTOKOLLET (RAW-LÄNK - öppen för alla med länken):
https://docs.google.com/document/d/1WD9XJBVrE49Csqz-XYiLgejlKlCA4t5sWiwoTkNiTD8/export?format=txt
```

**🟢 OPTIMAL WAY TO SHARE WITH AI:**

**Google Docs är redan öppen för länk-läsning** ✅  
(Du har den inställd på "vem som helst med länken kan redigera")

**DELA DIREKT MED AI:**
```
Du: "Läs mötesprotokollet från denna raw-länk:
https://docs.google.com/document/d/1WD9XJBVrE49Csqz-XYiLgejlKlCA4t5sWiwoTkNiTD8/export?format=txt

Sedan: Förbered FÖR mandagsmötet"
```

**RESULTAT:**
✅ AI läser mötesprotokollet direkt (ingen autentisering)
✅ Ingen copy-pasta behövs
✅ Alltid aktuell (senaste versionen)
✅ Snabbt & enkelt
✅ Öppen för vilken AI som helst (ChatGPT, Gemini, Claude, etc)

### **2. Regler Medan Du Läser**

✅ **Du MÅSTE (KRITISKT):**
- 🔴 **LÄS FILERNA FÖRST innan du svarar på något**
- 🔴 **CITERA alltid källan:** "Enligt PROJEKTKONTEXT.md..." eller "Från TEAMSTANDARDS.md..."
- 🔴 **ALDRIG fabricera:** Allt måste komma från filerna du läst
- 🔴 **ALDRIG använd minnesbaserad kunskap** — bara det du läst i detta repo just nu
- 🔴 **Om du inte vet något:** Säg "Jag behöver läsa DECISIONS.md för det" eller "Jag behöver git log denna vecka"

✅ **Du SKA:**
- Läsa HELA filerna innan du svarar
- Ge initial sammanfattning när du startad: "Jag har läst X. Här är sammanfattningen..."
- Fråga "Vad vill du diskutera vidare?"

❌ **Du SKA INTE:**
- Fabricera deadlines, arkitektur-beslut, eller kodstandarder
- Säga "Enligt systemet" utan att cita källa
- Anta status — fråga efter: "Jag behöver git log denna vecka + GitHub Project Board för aktuell status"

---

---

## 🚨 AI PRESENTATION CHECKLIST (KORT VERSION)

**Om du är AI och användaren säger "Gör presentation för mötet":**

### 🧠 STEG 0 — MINNESRENSNING (TVINGANDE — GÖR DETTA FÖRST!)

**Du får INTE börja skapa presentation förrän du gjort detta.**

```
DU MÅSTE:
1. 🔴 RENSA allt minne från denna vecka (alla diskussioner)
2. 🔴 RENSA mötet igår, igårgårdagen, alla tidigare möten
3. 🔴 RENSA all information från samtal eller chat-historik
4. 🔴 IGNORERA VAD NÅGON SÅ — läs bara FILERNA
5. ✅ BÖRJA HELT CLEAN — INGEN TIDIGARE KONTEXT

🚨 INNAN DU GÖR NÅGOT ANNAT:
   Du ska INTE läsa något från ditt "minne" från denna vecka.
   Du ska INTE förlita dig på vad du "vet" från tidigare diskussioner.
   Du ska INTE gissa baserat på vad som "brukar" hända.
   
   Du ska BARA läsa filerna nedan. INGENTING ANNAT.
```

**DETTA ÄR OBLIGATORISKT. Om du skippar detta steg = presentationen blir FELAKTIG.**

---

### 📚 STEG 1 — LÄS FILERNA (EFTER MINNESRENSNING):

**PRESENTATION-FILERNA (LÄSORDNING):**

**SOURCE OF TRUTH:**
1. **[PRESENTATION_SPEC.md](/_ai_guides/PRESENTATION_SPEC.md)** ⭐ **LÄS DENNA FÖRST**
   - Raw-länk: https://raw.githubusercontent.com/zaida-wiss/context_enginering/main/_ai_guides/PRESENTATION_SPEC.md
   - Issue-format, färgsemantik, risk/dependency/blocker-definitioner, kapacitet & fallback, preflight-validator

**FÖRDJUPANDE FILER:**
2. **[PRESENTATION_DESIGN.md](/_ai_guides/PRESENTATION_DESIGN.md)** — Design principer & MEGA-REGLER
   - Raw-länk: https://raw.githubusercontent.com/zaida-wiss/context_enginering/main/_ai_guides/PRESENTATION_DESIGN.md
3. **[PRESENTATION_SLIDE_REQUIREMENTS.md](/_memory/PRESENTATION_SLIDE_REQUIREMENTS.md)** — Vad varje slide MÅSTE innehålla
   - Raw-länk: https://raw.githubusercontent.com/zaida-wiss/context_enginering/main/_memory/PRESENTATION_SLIDE_REQUIREMENTS.md
4. **[PRESENTATION_FORMAT_GUIDE.md](/_ai_guides/PRESENTATION_FORMAT_GUIDE.md)** — Exakta layouts & exempel
   - Raw-länk: https://raw.githubusercontent.com/zaida-wiss/context_enginering/main/_ai_guides/PRESENTATION_FORMAT_GUIDE.md
5. **[SPRINT_PRESENTATION_STRUCTURE.md](/_ai_guides/SPRINT_PRESENTATION_STRUCTURE.md)** — Struktur & ordning
   - Raw-länk: https://raw.githubusercontent.com/zaida-wiss/context_enginering/main/_ai_guides/SPRINT_PRESENTATION_STRUCTURE.md

**DATA ATT SAMLA:**
5. **Mötesprotokollet denna vecka:** https://docs.google.com/document/d/1WD9XJBVrE49Csqz-XYiLgejlKlCA4t5sWiwoTkNiTD8/export?format=txt
6. **Git log denna vecka** (vad blev gjort)
7. **GitHub Project Board status denna vecka**
8. **Vilka issues är klara/pågår/blockerade**

### ✅ PRESENTATION MÅSTE INNEHÅLLA EXAKT DESSA 13 MÖTESPUNKTER:

| Slide | Mötespunkt | Innehål |
|-------|-----------|---------|
| 0 | 📝⓪ | Presentationsslide + Agenda |
| 1-4 | 📝① | Tre målsystem (Kursen + Projektet + Avanza) + Progress Board |
| 5-7 | 📝② | Frontend/Backend/Native team status (per team 1-2 slides) |
| 8 | 📝③ | Status sedan förra möte |
| 9 | 📝④ | Beroenden & Risker |
| 10 | 📝⑤ | Team-support förslag |
| 11-12 | 📝⑥-⑦ | Prioritering & Estimering |
| 13+ | 📝⑧-⑫ | Tekniska beslut, Arbetsuppgifter, Nästa steg |

**TOTALT: 14-16 slides** (flera slides kan tillhöra samma mötespunkt 📝)

### ✅ VARJE SLIDE MÅSTE HA:
- [ ] Symbol **📝① eller 📝②** etc till **VÄNSTER**
- [ ] Copy-paste-friendly text (max 3-5 bullets per slide)
- [ ] Status-färger där relevant: 🟢🟠🔴
- [ ] Läsbar kontrast (WCAG AA 4.5:1 minimum)
- [ ] Tillräckligt med padding (ingen text-overlap)

### ❌ MISSLYCKAD PRESENTATION OM:
- [ ] Saknar någon 📝-punkt (⓪ och ①-⑫)
- [ ] Färre än 14 slides
- [ ] Symbol INTE till vänster
- [ ] Hoppar över någon sektion
- [ ] Text kan inte copy-pastas direkt till mötesprotokollet
- [ ] Saknar tre målsystem på första 📝①-slidorna
- [ ] Dålig kontrast eller text överlappar

**INNAN DU LEVERERAR: Verifiera denna checklist. En misslyckad presentation = alla items MÅSTE fixas.**

### 🚨 MINNESRENSNING MÅ INGÅ I PRESENTATIONEN

**Användaren behöver INTE copy-pasta något.** Minnesrensningen ska vara en **obligatorisk del** av presentation-processen som AI MÅSTE följa automatiskt.

**När användaren säger "Gör en presentation":**
1. AI läser denna README
2. AI ser STEG 0 (MINNESRENSNING)
3. AI MÅSTE rensa sitt minne innan något annat
4. AI läser sedan FILERNA (inte sitt minne)
5. AI skapar presentation bara från fil-data

**Minnesrensningen är INTE frivillig — den är TVINGANDE.**

---

### **STEG 2: Läs Även Projekt-Repot (avanza-team1)**

**Efter du läst context_enginering, hämta projekt-data från:**

```
https://github.com/chas-challenge-2026/avanza-team1
```

KLONA INTE REPOT. Hämta istället direkt från GitHub:
- README.md (projekt-överblick)
- Git log denna vecka (commits & branches status)
- GitHub Project Board denna vecka (aktuell status)
- Issues denna vecka (se Issues-fliken)
- PR:er och branches (se PR-fliken)

**Läs ENDAST relevant kod när du behöver verifiera:**
- Ett konkret beroende mellan team
- En blocker eller integrationsproblem
- Ett API-kontrakt som saknas

**NU har du FULL kontext från båda repos och kan svara!**

---

### **3. AI Som Senior Tech Lead — Innan Mötet**

⚠️ **DETTA CONTEXT-REPO ÄR INTE BARA EN PRESENTATIONSMALL**

Innan varje sprintmöte läser AI **verklig kod i pågående brancher** för att:

- **Upptäcka integrationsproblem** innan teamet springer in i dem
- **Läsa API-kontrakt** från båda sidor (Frontend skickar vad? Backend förväntar vad?)
- **Visualisera integrations-kedjor** som konkreta mensen + branch-namn, inte abstrakt arkitektur
- **Klassificera status** för varje kedja: VERIFIERAD MATCH, TROLIG MATCH, BEHÖVER SYNKAS, MISMATCH, KAN INTE VERIFIERAS
- **Identifiera branch-divergence** — vilka ligger långt efter develop? Modifierar två brancher samma filer?

**Resultatet:** En integration-slide i presentationen som visar verkligt arbete från verkliga människor.

Se **[CROSS_TEAM_INTEGRATION.md](_ai_guides/CROSS_TEAM_INTEGRATION.md)** för detaljer.

---

### **4. Efter Du Läst Båda Repos — MENTORSHIP MODELL**

⚠️ **DETTA ÄR HANDS OFF — AI GUIDER, DU BYGGER!**

**AI är INTE en kodgenerator.** AI är en SENIOR MENTOR som:
- Ställer frågor för att du ska tänka igenom arkitekturen
- Guider dig genom decisions (VAD, HUR, VARFÖR)
- Reviewar din implementation mot acceptance criteria
- Förklarar trade-offs och lärdomspunkter

**FLÖDE:**
```
1. Du presenterar issue/problem
2. AI frågar: "Vilken arkitektur? Vilken state? Vilka beroenden?"
3. DU tänker igenom designen & svarar
4. AI säger: "Bra tänk. Här är några tankar..."
5. DU implementerar (AI visar exempel bara om du behöver)
6. AI reviewar: "Bra! Märkte du detta mönster?"
```

✅ **AI GÖR DETTA:**
- Ställer arkitektur-frågor FÖRE kod
- Guider tänkandet (VAD-HUR-VARFÖR)
- Reviewar implementering
- Diskutera trade-offs & design-beslut
- Förklara kodstandarder & best practices
- Besvara frågor baserat på läst innehål
- Verifiera konsistens mellan git, GitHub, och risker
- Planera sprintar & ge rekommendationer

❌ **AI GÖR INTE DETTA:**
- Generera komplett kod för dig
- Uppdaterar filer automatiskt
- Gör commits eller PRs
- Pushar kod till GitHub
- Tar beslut åt dig
- Gör ändringar utan godkännande

---

## 📚 Mappar & Innehål

### `_memory/` — Statisk Referens (Läs För Kontext)

| Fil | Syfte |
|-----|-------|
| **PROJEKTKONTEXT.md** | Kundens problem (Anna), MVP-features, varför vi bygger |
| **TEAMSTANDARDS.md** | Kodstandarder, Git workflow, commit-format, regler |
| **DEFINITION_OF_DONE.md** | Vad är godkänt arbete? Tests, dokumentation, review |
| **DECISIONS.md** | Arkitektur-beslut — varför Java? React? C++? |
| **UI_DESIGN_REFERENCE.md** | Design-system, mockups, Figma-guidelines |
| **SPRINT_FOCUS_TIMELINE.md** | Sprint-veckor & fokus (V2-V12), deadlines |

### `_ai_guides/` — Instruktioner & Guider

| Fil | Syfte |
|-----|-------|
| **VERIFICATION_SYSTEM.md** | Hur verifierar vi systemet? Veckovis checklist |
| **SPRINT_PLANNING.md** | Guide för sprintplanering |
| **AI_TEAMLEADER.md** | Universal mötesfacilitator-prompt |
| **WHAT_CAN_I_HELP_WITH.md** | Meny — vad kan AI göra? |
| **MEETING_THURSDAY.md** | Torsdag vecko-slutabstämning |
| **MEETING_MONDAY.md** | Måndag sprintplanering |

---

## 🎯 Team Decisions (BESLUT)

**Varje team dokumenterar sina arkitektur-beslut:**

| Team | Beslut-logg | Format |
|------|-------------|--------|
| **Frontend** | [docs/frontend/BESLUT.md](https://github.com/chas-challenge-2026/avanza-team1/blob/main/docs/frontend/BESLUT.md) | ✅ Aktivt |
| **Backend (Java)** | `backend/BESLUT.md` | ⚠️ Behöver skapas |
| **Native (C/C++)** | `native/docs/BESLUT.md` | ⚠️ Behöver skapas |

**Format för varje beslut (TEAMNEUTRALT EXEMPEL):**
```
## [DATUM] — [Beslut]
- Beslut: Vad beslöts?
- Varför: Reasoning bakom beslutet
- Konsekvenser: Vad betyder detta för systemet?
- Bevis: Issue #X, PR #Y
- Beslutsfattare: Namn
```

**Notering:** Varderas faktiska beslut hittar du i respektive teams BESLUT.md-fil  
(Frontend, Backend, Native — läs den relevanta för ditt arbete).

---

## 🔗 Projekt-Relaterade Länker

**Projektets Kod (avanza-team1):**
- Repo: https://github.com/chas-challenge-2026/avanza-team1
- Issues: https://github.com/chas-challenge-2026/avanza-team1/issues
- Pull Requests: https://github.com/chas-challenge-2026/avanza-team1/pulls
- Project Board: https://github.com/orgs/chas-challenge-2026/projects/31

**Real-Time Data (Inte I Denna Repo):**
- GitHub Project Board (issue status) — uppdateras real-time
- Google Sheets Risker (risker & assets) — uppdateras efter möten
- git log (commits & branches) — uppdateras per commit
- Mötesprotokollet (decisions) — uppdateras efter möten
- **Team Decision Logs (BESLUT.md)** — uppdateras när arkitektur-beslut tas

---

## 💬 Exempel: Hur Du (Användaren) Använder Det

### **Du vill fråga en AI om projektet:**

```
Du: "Läs detta repo och svara på mina frågor:
https://github.com/zaida-wiss/context_enginering
Sedan läs även: https://github.com/chas-challenge-2026/avanza-team1

Vilka är de 3 viktigaste saker vi måste förhålla oss till denna vecka?"

AI: "✅ Jag har läst båda repos.

Enligt SPRINT_FOCUS_TIMELINE.md + GitHub Project Board:
1. CTO-feedback deadline (24 sep) — Vi måste ha risk-metrics klara
2. Kvaldemo (15 okt) — UI måste vara polerad
3. Slutleverans (4 nov) — All dokumentation måste vara klar

Från DEFINITION_OF_DONE.md vet jag att godkänt arbete kräver:
- Acceptance criteria uppfyllda
- Tests skrivna (70%+ coverage)
- Code reviewed
- Dokumentation uppdaterad

Vad vill du diskutera vidare?"
```

### **Du vill få hjälp med en issue:**

```
Du: "Jag jobbar på denna issue [kopiera issue-body från GitHub].
Hjälp mig tänka igenom arkitekturen.

Enligt våra regler (DEFINITION_OF_DONE.md):
- Vilken state behöver komponenten?
- Vad bör ligga i modulen vs komponenten?
- Vilka tester behövs?"

AI: "Enligt din issue-body:
- Problem: [från issue]
- AC: [från issue]
- Technical details: [från issue]

Fundera på dessa frågor:
1. State: Du säger [från issue] — är det rätt?
2. Module vs component: Enligt TEAMSTANDARDS.md...
3. Tests: Enligt DEFINITION_OF_DONE.md måste du ha [X]"
```

### **Du vill ha en presentation:**

```
Du: "Förbered FÖR tisdagsmötet
Länk: https://github.com/zaida-wiss/context_enginering"

AI: "✅ Jag har läst repos.
Vilka punkter vill du fokusera på denna tisdag?
- Deadlines?
- Blockers?
- PRs under review?
- Performance metrics?

Efter du svarar: [skapar visuell 11-slide presentation]"
```

### **Du delar länken med en helt annan AI:**

```
Du (till ChatGPT/Gemini/etc): "Läs detta repo och svara på mina frågor:
https://github.com/zaida-wiss/context_enginering

Vilka är kodstandarder för frontend?"

Annan AI: [läser TEAMSTANDARDS.md]
"Enligt TEAMSTANDARDS.md för Frontend:
- TypeScript: interfaces för alla props
- CSS: .module.css per komponent
- Naming: PascalCase för komponenter, camelCase för variabler
- Linting: ESLint + Prettier måste passa
- [citerar mer från filen]"
```

---

## 🎯 VAD KAN JAG FRÅGA AI:N OM?

### Snabb Status-check
```
"Hur går det för oss?"
→ AI läser GitHub + Mötesprotokollet + Risker → Nulägesrapport (30 sek!)
   Visar: Progress per team | Deadlines | Blockers | Nästa prioriteringar

"Vad är läget?"
"Team status check"
"Hur ligger vi till?"
→ Samma resultat — kort & fokuserad visuell rapport
```

### Grundläggande Frågor
```
"Vad är projektet?"
→ AI läser PROJEKTKONTEXT.md → Förklarar Annas problem + MVP

"Vilka är kodstandarder?"
→ AI läser TEAMSTANDARDS.md → Visar Git-format, kodregler, branch-naming

"Vad är godkänt arbete?"
→ AI läser DEFINITION_OF_DONE.md → Visar AC vs DoD, test-krav, dokumentation

"Vilka arkitektur-beslut tog ni?"
→ AI läser DECISIONS.md → Varför Java? React? C++?

"Hur verifierar vi systemet?"
→ AI läser VERIFICATION_SYSTEM.md → Veckovisa checkpoints
```

### Issue-hjälp
```
"Hjälp mig med denna issue [copypaste från GitHub]"
→ AI läser issue → Ställer arkitektur-frågor → Guider tänkandet

"Är min implementering klar?"
→ AI jämför mot DEFINITION_OF_DONE.md → Checkar AC, tests, dokumentation

"Ge mig en presentation av denna veckas status"
→ AI läser git log + GitHub Project Board → Skapar 11 visuella slides
```

### Möten
```
"Förbered FÖR tisdagsmötet"
→ AI läser git + deadlines → Presenterar status mot CTO deadline

"Förbered FÖR mandagsmötet"
→ AI läser denna veckas fokus → Planerar nästa vecka

"Kör sprint review möte"
→ AI läser vad blev klart denna vecka → Presenterar lärdomar
```

### Backlog & Planering
```
"Vilka är de viktigaste issues denna vecka?"
→ AI läser GitHub Project Board + SPRINT_FOCUS_TIMELINE.md

"Vilka issues är blockade?"
→ AI läser Project Board + git branches → Identifierar blockers

"Skapa nya issues enligt vår format"
→ AI läser WHAT_CAN_I_HELP_WITH.md → Presenterar [Category] format + DoR/DoD
```

### Performance & Feedback
```
"Vilka är Lighthouse-scores denna vecka?"
→ AI läser CI/CD reports + MEETING_STATUS_SYNC.md

"Ge feedback på denna kod"
→ AI läser TEAMSTANDARDS.md + DEFINITION_OF_DONE.md → Reviewar mot regler
```

---

### 🤔 Om Du Inte Vet Vad Du Vill Fråga:
```
"Hur går det för oss?" ← START HÄR! (Snabb nulägesbild)
→ AI presenterar progress, deadlines, blockers, nästa prioriteringar

"Vad kan jag be om?"
→ AI presenterar denna lista

"Vad är viktigt denna vecka?"
→ AI läser SPRINT_FOCUS_TIMELINE.md + GitHub Project Board

"Vad bör vi fokusera på?"
→ AI läser deadlines + Git-status → Presenterar prioriteringar
```

---

## 📊 Två Repos, En Vision

```
THIS REPO (context_enginering)
├── Team process dokumentation
├── AI-instruktioner & guider
├── Minnesdokument (statisk referens)
└── Verifikationssystem

PROJECT REPO (avanza-team1)
├── Projektets kod (Java, React, C++)
├── GitHub Issues & Project Board
├── Pull Requests & Code Reviews
└── Git commit history
```

**Du behöver förstå båda för att kunna hjälpa!**

---

## 🚀 Nästa Steg

1. **Du är AI:** Läs filerna ovan och ge sammanfattning ✅
2. **Du är människa:** Dela denna länk med AI: `https://github.com/zaida-wiss/context_enginering` ✅
3. **Diskutera:** AI har nu samma kontext som du ✅

---

**Senast uppdaterad:** 2026-09-08  
**Repos:**
- Team Process: https://github.com/zaida-wiss/context_enginering
- Projekt Kod: https://github.com/chas-challenge-2026/avanza-team1
