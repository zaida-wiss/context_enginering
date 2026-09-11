# 📱 Avanza Portföljhälsa - Team 1 Extended Challenge

**En portföljövervakningsapp som hjälper kunder att förstå sitt sparande, upptäcka driftningar och fatta bättre beslut.**

**Repo för teamdokumentation, minnesdokument och AI-guider.**  
**Projektkoden är här:** https://github.com/chas-challenge-2026/avanza-team1

---

## 🤖 Du är en AI? START HÄR

### ⚡ QUICK START (30 sekunder)

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

Du läser detta repo för första gången? Följ denna guide:

### **STEG 1: Läs Denna Repo Först** (context_enginering - 5-10 min)

**Detta är Team Process & Standards. Läs detta först.**

#### Läs Dessa Filer I Ordningen

```
1. _memory/PROJEKTKONTEXT.md        — Vad är projektet? Kundens problem?
2. _memory/TEAMSTANDARDS.md         — Regler, Git-format, kodstandarder
3. _memory/DEFINITION_OF_DONE.md    — Vad är godkänt arbete?
4. _ai_guides/VERIFICATION_SYSTEM.md — Hur verifierar vi systemet?
```

Raw-links för copy-pasta:
```
https://raw.githubusercontent.com/zaida-wiss/context_enginering/main/_memory/PROJEKTKONTEXT.md
https://raw.githubusercontent.com/zaida-wiss/context_enginering/main/_memory/TEAMSTANDARDS.md
https://raw.githubusercontent.com/zaida-wiss/context_enginering/main/_memory/DEFINITION_OF_DONE.md
https://raw.githubusercontent.com/zaida-wiss/context_enginering/main/_ai_guides/VERIFICATION_SYSTEM.md
```

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

### **STEG 2: Läs Även Projekt-Repot (avanza-team1)**

**Efter du läst context_enginering, gå till projekt-repot och läs:**

```
https://github.com/chas-challenge-2026/avanza-team1
```

Läs **HELA docs-mappen där** +:
- README.md (projekt-överblick)
- Git log denna vecka (commits & branches)
- GitHub Project Board denna vecka (status)

**NU har du FULL kontext från båda repos och kan svara!**

---

### **3. Efter Du Läst Båda Repos — MENTORSHIP MODELL**

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

**Format för varje beslut:**
```
## [DATUM] — [Beslut]
- Beslut: Vad beslöts?
- Varför: Reasoning bakom beslutet
- Konsekvenser: Vad betyder detta för systemet?
- Bevis: Issue #X, PR #Y
- Beslutsfattare: Namn
```

**Exempel (Frontend):**
```
## 2026-09-02 — Mock före Java-API
- Beslut: UI läser src/data/portfolio.json tills GET /api/portfolio finns
- Varför: Backend inte redo, men MVP-översikt kan byggas ändå
- Konsekvenser: Typ-kontraktet är Portfolio. Risk R-24.
- Bevis: Issue #24, PR #46
- Beslutsfattare: Tomac
```

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

## 🎯 Quick Commands För AI

**"Vad är projektet?"**  
→ Läs PROJEKTKONTEXT.md

**"Vilka är kodstandarder?"**  
→ Läs TEAMSTANDARDS.md

**"Är detta godkänt arbete?"**  
→ Läs DEFINITION_OF_DONE.md

**"Vilka är arkitektur-beslut?"**  
→ Läs DECISIONS.md

**"Hur verifierar vi systemet?"**  
→ Läs VERIFICATION_SYSTEM.md

**"Vilka är denna veckas fokus?"**  
→ Läs SPRINT_FOCUS_TIMELINE.md + ge mig git log + Project Board

**"Hjälp mig planera sprint"**  
→ Läs SPRINT_PLANNING.md

**"Kör möte"**  
→ Läs AI_TEAMLEADER.md + relevant MEETING-fil

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
