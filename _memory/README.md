# 📚 Memory - Statisk Referens

**Denna mapp innehåller STATISKA referensdokument som uppdateras sällan.**

Dessa är kunskaps-dokument som läses för förståelse och kontext.

---

## 📁 Fil-Index

| Fil | Syfte | Uppdateras |
|-----|-------|----------|
| **PROJEKTKONTEXT.md** | Kundens behov (Anna), vad vi bygger, MVP | Vid scope-ändringar |
| **TEAMSTANDARDS.md** | Kodstandarder, Git workflow, commit-format | Vid process-ändringar |
| **DEFINITION_OF_DONE.md** | Vad är godkänt? Acceptance criteria | Vid DoD-ändringar |
| **DECISIONS.md** | Arkitektur-beslut (varför gjorde vi det så?) | Vid nya arkitektur-beslut |
| **UI_DESIGN_REFERENCE.md** | Design-specifications, mockups, guidelines | Vid design-ändringar |
| **SCHEDULE.md** | Skolans officiella tidslinje/schema (KOPIA) | Sällan (årlig) |
| **SPRINT_FOCUS_TIMELINE.md** | Sprint-fokus väg & milestones (KOPIA) | Sällan (årlig) |

---

## 🎯 Vad Är Vad?

### **PROJEKTKONTEXT.md**
Läs denna för att förstå:
- ❓ Vad är projektets problem? (Annas behov)
- 🎯 Vad bygger vi?
- 📊 Vilka är MVP-features?
- 👥 Vem är användaren?
- 💰 Vad är värdet?

### **TEAMSTANDARDS.md**
Läs denna för att förstå:
- 📝 Git commit-format: `type(scope): message (#ISSUE)`
- 🌿 Branch-naming: `type/#ISSUE-description`
- 💻 Kod-standard per språk (Java, React, C++)
- ✅ PR-process och code review
- 🚫 Vad är NOT allowed (console.log, TODO, etc)

### **DEFINITION_OF_DONE.md**
Läs denna för att förstå:
- ✅ Acceptanskriterier
- 🧪 Test-krav (70% backend, 60% frontend)
- 📚 Dokumentation-krav
- 👀 Code review-process
- 🎯 Kursmål som måste uppfyllas

### **DECISIONS.md**
Läs denna för att förstå:
- 🏗️ Arkitektur-val: Varför Java? React? C++?
- 📊 Database: PostgreSQL, Flyway-migrations
- 🔐 Security: JWT, SQL injection prevention
- ⚡ Performance: Back-testing < 2 sec, FX < 100ms
- 🌍 Andra arkitektur-beslut

### **UI_DESIGN_REFERENCE.md**
Läs denna för att förstå:
- 🎨 Design-system och komponenter
- 📐 Figma-mockups
- 🎯 UI-guidelines
- ♿ Accessibility-krav
- 📱 Responsive-design

### **SCHEDULE.md**
En kopia av skolans officiella tidslinje:
- 📅 Kurschema
- ⏰ Tidsplan per vecka
- 🎓 Kursmål
- 📍 Sällan uppdaterad

### **SPRINT_FOCUS_TIMELINE.md**
En kopia av vecko-fokus och milestones:
- 📊 V2-V12 fokus
- 🎯 Vad fokuseras på denna vecka?
- 📍 Kritiska deadlines
- ⚠️ Risk-områden per vecka

---

## 🔗 Hur Dessa Länkas Till Projektet

| Projekt-Fråga | Läs Denna Fil |
|---|---|
| "Vad är projektets problem?" | PROJEKTKONTEXT.md |
| "Vilka är kodstandarder?" | TEAMSTANDARDS.md |
| "Vad är godkänt arbete?" | DEFINITION_OF_DONE.md |
| "Varför gjorde vi det så?" | DECISIONS.md |
| "Hur ska UI se ut?" | UI_DESIGN_REFERENCE.md |
| "Vilka är kursmål?" | PROJEKTKONTEXT.md + DEFINITION_OF_DONE.md |
| "Vad är nästa deadline?" | SPRINT_FOCUS_TIMELINE.md |

---

## ⚠️ Viktigt

Dessa filer är **NOT** uppdaterade regelbundet.

**För aktuell status, läs från:**
- GitHub Project Board (issue status)
- Google Sheets Risker (risker & mitigations)
- Mötesprotokollet (decisions & action items)
- git log (commits & branches)

Se `_ai_guides/VERIFICATION_SYSTEM.md` för hur man verifierar konsistens.

---

**Senast uppdaterad:** 2026-09-08
