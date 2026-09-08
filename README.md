# 📱 Avanza Portföljhälsa - Team 1 Extended Challenge

**En portföljövervakningsapp som hjälper kunder att förstå sitt sparande, upptäcka driftningar och fatta bättre beslut.**

**Repo för teamdokumentation, minnesdokument och AI-guider.**  
**Projektkoden är här:** https://github.com/chas-challenge-2026/avanza-team1

---

## 🤖 Du är en AI? START HÄR

Du läser detta repo för första gången? Följ denna guide:

### **1. Läs Dessa Filer I Ordningen** (5-10 min)

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

✅ **Du MÅSTE:**
- Citera vilka filer du läst för varje påstående
- Säga "Enligt PROJEKTKONTEXT.md..." eller "Från git log..."
- Aldrig fabricera information — allt måste komma från filerna
- Om du inte vet något, säga "Jag behöver mer information från..."

✅ **Du SKA:**
- Läsa HELA filerna innan du svarar
- Ge initial sammanfattning när du startad: "Jag har läst X. Här är sammanfattningen..."
- Fråga "Vad vill du diskutera vidare?"

❌ **Du SKA INTE:**
- Fabricera deadlines, arkitektur-beslut, eller kodstandarder
- Säga "Enligt systemet" utan att cita källa
- Anta status — fråga efter: "Jag behöver git log denna vecka + GitHub Project Board för aktuell status"

### **3. Efter Du Läst — Du Kan Nu:**

- ✅ Diskutera projektet (kundens behov, arkitektur, MVP)
- ✅ Ge kodstandarder feedback
- ✅ Förklara vad är godkänt arbete
- ✅ Verifiera konsistens mellan git, GitHub, och risker
- ✅ Planera sprintar
- ✅ Mentorsk vägledning (VAT-HUR-VARFÖR)

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

---

## 💬 Exempel: Hur Du Använder Det

### **Exempel 1: AI Läser För Första Gången**

```
Du: "Läs detta repo och ge sammanfattning:
https://github.com/zaida-wiss/context_enginering"

AI: "✅ Jag har läst:
1. PROJEKTKONTEXT.md — Kundens problem är att Anna behöver...
2. TEAMSTANDARDS.md — Vi använder Java/React/C++, Git-format är...
3. DEFINITION_OF_DONE.md — Godkänt arbete kräver...

📊 Sammanfattning:
- Projektet: Portföljhälsa-app
- Kundens problem: [från PROJEKTKONTEXT]
- MVP: [lista från PROJEKTKONTEXT]
- Tech stack: [från TEAMSTANDARDS]
- Deadline: [från SPRINT_FOCUS_TIMELINE]

Vad vill du diskutera vidare?"
```

### **Exempel 2: Senare, Du Frågar Samma AI**

```
Du: "Baserat på repot: Vilka är nästa sprint-fokus?"

AI: "Enligt SPRINT_FOCUS_TIMELINE.md är denna vecka fokus på: [X]

För aktuell status denna vecka behöver jag:
- git log denna vecka
- GitHub Project Board status
- Google Sheets Risker

Kan du ge mig detta för exakt status?"
```

### **Exempel 3: Du Delar Med Annan Person**

```
Du: "Läs detta projekt-repo för kontext:
https://github.com/zaida-wiss/context_enginering

Sedan: https://github.com/chas-challenge-2026/avanza-team1

Vilka är de 3 viktigaste issue vi bör fokusera på denna vecka?"

Annan AI: [läser båda repos, svarar med full kontext]
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
