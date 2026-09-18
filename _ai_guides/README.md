# 🤖 AI Guides - Instruktioner & Guider för Presentationer & Möten

**Du är i `_ai_guides/`-mappen — här finns alla instruktioner för hur AI ska agera.**

Dessa dokument innehåller **konkreta guider** för att skapa presentationer, möten och verifiering.

## 🚨 GLOBALT AI-RAMVERK — LÄS FÖRST

[`AI_FRAMEWORK.yaml`](AI_FRAMEWORK.yaml) är det **normativa kontraktet** för alla AI-uppgifter i repot. [`AI_FRAMEWORK.md`](AI_FRAMEWORK.md) är endast en mänsklig förklaring.

Särskilt: om två aktiva regler motsäger varandra får AI inte välja själv. Den
måste stoppa, visa konflikten och konsekvenserna och be användaren om beslut
innan regler ändras eller arbetet fortsätter.

---

## 📍 DOKUMENTVÄGEN — Läsordning

```
VILL DU SKAPA EN PRESENTATION?
        ↓
🟢 START HÄR: presentations/MANDATORY_READING_ORDER.md ← ENDA ORDNINGEN
   (hela systemet från datahämtning till leverans)
        ↓
RESULTAT: Live GitHub-data + verifierad design = presentationen är klar
```

---

## ⚠️ INNAN DU BÖRJAR: LÄS `_memory/`

**`_memory/` innehåller PROJEKTKONTEXT som AI måste förstå:**

- **`TEAM_STANDARDS.md`** — Kodstandarder, Git workflow
- **`DEFINITION_OF_DONE.md`** — Vad är "DONE" för en GitHub-issue?
- **`COURSE_DEADLINES.md`** — Kurs-deadlines (CTO Feed Forward, etc)
- **`SCHEDULE.md`** — Kurschema & vecko-fokus

👉 **Läs denna först:** [`_memory/README.md`](../_memory/README.md)

---

## 📁 Presentation-Guider (Läsordning)

| Fil | Syfte | Läs när... |
|-----|-------|-----------|
| **presentations/MANDATORY_READING_ORDER.md** 🚨 | **MÅSTE LÄSAS** — 4 steg från start till klar presentation | Du ska bygga en presentation |
| **presentations/monday_meeting/design/SLIDE_DETAIL_SPEC.md** ⭐ | **EXAKTA SLIDE-SPEC** — format, kolumner, regler, datakällor för varje slide ①-⑭ | Du designar slidorna |
| **presentations/design/VISUAL_DESIGN_MANDATORY.md** | Symbol + Färg + Text — NPF/dyslexia-vänlig, konkret PowerPoint-implementering | Innan du renderar |
| **presentations/monday_meeting/structure/PRESENTATION_STRUCTURE.md** | 14 mötespunkter (①-⑭) — vad varje punkt MÅSTE innehålla | Du ska förstå struktur |
| **presentations/verification/RENDER_GATE_CHECKLIST.md** | Korrekt render-gate — 13 checkpoints innan rendering | Innan du renderar |
| presentations/data/DATA_SOURCES.md | Vilka GitHub-URLs + fallback-strategier | Du hämtar data |

---

## 🎯 Om Du Är En Extern AI

**Om någon säger: "Läs detta repo och skapa en presentation"**

1. ✅ Läs root `README.md` först
2. ✅ Läs **`_memory/`-mappen** (projektkontexten)
3. ✅ Läs **presentations/MANDATORY_READING_ORDER.md** (ENDA körordningen för presentation)
4. ✅ Föl ordningen → slutligen render presentation
5. ✅ Verifiera mot render-gate checklist före leverans

**Branch Inheritance Policy:**
Do NOT use raw.githubusercontent.com links that hard-code `/main/`. 
Read files from the same branch/ref as your entry README (see repository_ref_policy in SYSTEM_CONTRACT.yaml).

---

## 📚 Referensmaterial & Guider

**Om du behöver hjälp med...**

| Vad | Fil | Syfte |
|-----|-----|-------|
| **Typiska AI-uppgifter** | [SKILLS.md](SKILLS.md) | Commit-format, arkitektur-beslut, etc. |
| **Köra möten med AI** | [HOW_TO_RUN_MEETINGS.md](HOW_TO_RUN_MEETINGS.md) | Web-based AI vs VS Code workflow |
| **Kodexempel-krav** | [ACCESSIBILITY_AND_SECURITY.md](ACCESSIBILITY_AND_SECURITY.md) | TypeScript, Accessibility, Security |
| **Presentationsfelsökning** | [presentations/TROUBLESHOOTING.md](presentations/TROUBLESHOOTING.md) | Missing team members, Wrong data, etc. |
| **Ordbok & Terminologi** | [ORDBOK.md](ORDBOK.md) | Förklaringar av begrepp (NPF, møtespunkter, etc.) |
| **Navigationshjalp** | [NAVIGATION.md](NAVIGATION.md) | Överblick över repo-struktur och filvägar |
| **Vad kan AI hjälpa med** | [WHAT_CAN_I_HELP_WITH.md](WHAT_CAN_I_HELP_WITH.md) | Exempelprompts och vanliga AI-uppgifter |
| **Frontend AI-instruktioner** | [FRONTEND_AI_INSTRUCTIONS.md](FRONTEND_AI_INSTRUCTIONS.md) | Specifika regler för Frontend-arbete |
| **PR-uppdateringar** | [PR_UPDATES.md](PR_UPDATES.md) | Hur man förbereder och presenterar PR:er |
| **Team-ledning med AI** | [AI_TEAMLEADER.md](AI_TEAMLEADER.md) | 🎙️ MÖTE-FACILITATION (interaktiv i chat, copy-paste data) — INTE presentation |
| **Cross-team integration** | [CROSS_TEAM_INTEGRATION.md](CROSS_TEAM_INTEGRATION.md) | Beroenden mellan Frontend/Backend/Native |
| **Backlog-template** | [BACKLOG_TEMPLATE.md](BACKLOG_TEMPLATE.md) | Hur man skriver och strukturerar GitHub-issues |
| **Pedagogiska riktlinjer** | [PEDAGOGICAL_GUIDANCE.md](PEDAGOGICAL_GUIDANCE.md) | Lärande & feedback-filosofi för möten |
| **Presenter guide** | [PRESENTER_GUIDE.md](PRESENTER_GUIDE.md) | Tips för att presentera resultaten |
| **Rutiner & levande dokument** | [ROUTINE_LIVING_DOCS.md](ROUTINE_LIVING_DOCS.md) | Hur man uppdaterar dokumenten över tid |
| **Deprecated files** | [DEPRECATED_FILES_MIGRATION.md](DEPRECATED_FILES_MIGRATION.md) | Gamla system & migrationsvägar |

---

## 🚀 Quick Links

👉 **Gå till:** Root `README.md` för övergripande instruktioner och två-stegs läsordning  
👉 **Gå till:** `_memory/` för minnesfiler (Definition of Done, Kursmål, etc)  
👉 **Gå till:** `mötesprotokollet` (Google Docs) för denna veckas faktiska data
