# 🤖 AI Guides - Instruktioner & Guider för Presentationer & Möten

**Du är i `_ai_guides/`-mappen — här finns alla instruktioner för hur AI ska agera.**

Dessa dokument innehåller **konkreta guider** för att skapa presentationer, möten och verifiering.

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

- **`TEAMSTANDARDS.md`** — Kodstandarder, Git workflow
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

**Raw-links för direkt läsning (om länk inte fungerar):**
- 🚨 MANDATORY_READING_ORDER.md: https://raw.githubusercontent.com/zaida-wiss/context_enginering/main/_ai_guides/presentations/MANDATORY_READING_ORDER.md
- 📊 SLIDE_DETAIL_SPEC.md: https://raw.githubusercontent.com/zaida-wiss/context_enginering/main/_ai_guides/presentations/monday_meeting/design/SLIDE_DETAIL_SPEC.md
- 📝 PRESENTATION_STRUCTURE.md: https://raw.githubusercontent.com/zaida-wiss/context_enginering/main/_ai_guides/presentations/monday_meeting/structure/PRESENTATION_STRUCTURE.md

---

## 📚 Referensmaterial & Guider

**Om du behöver hjälp med...**

| Vad | Fil | Syfte |
|-----|-----|-------|
| **Typiska AI-uppgifter** | [SKILLS.md](SKILLS.md) | Commit-format, arkitektur-beslut, etc. |
| **Köra möten med AI** | [HOW_TO_RUN_MEETINGS.md](HOW_TO_RUN_MEETINGS.md) | Web-based AI vs VS Code workflow |
| **Kodexempel-krav** | [ACCESSIBILITY_AND_SECURITY.md](ACCESSIBILITY_AND_SECURITY.md) | TypeScript, Accessibility, Security |
| **Presentationsfelsökning** | [presentations/TROUBLESHOOTING.md](presentations/TROUBLESHOOTING.md) | Missing team members, Wrong data, etc. |

---

## 🚀 Quick Links

👉 **Gå till:** Root `README.md` för övergripande instruktioner och två-stegs läsordning  
👉 **Gå till:** `_memory/` för minnesfiler (Definition of Done, Kursmål, etc)  
👉 **Gå till:** `mötesprotokollet` (Google Docs) för denna veckas faktiska data
