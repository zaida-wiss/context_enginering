# 📅 Uppdaterings-Schema för Levande Dokument

**Denna guide visar EXAKT när och hur du uppdaterar de levande dokumenten (_sprint/).**

Utan detta schema blir dokumenten förvirrat och systemet fungerar inte.

---

## 🎯 Levande & Stabila Dokument

**Levande dokument (uppdateras regelbundet):**
```
_sprint/
├── CURRENT_STATUS.md      ← Uppdateras OFTA (efter varje möte)
├── RISKS.md               ← Uppdateras VECKOVIS
└── SPRINT_PLANNING.md     ← Uppdateras SÄLLAN (grundläggande guide)
```

**Stabila referensdokument:**
```
_memory/
├── SCHEDULE.md            ← Referens: Kursschemat (uppdateras sällan)
├── TEAMSTANDARDS.md
├── DECISIONS.md
└── ...
```

---

## 📊 Uppdaterings-Cadence

### **CURRENT_STATUS.md** (MEST KRITISK)

| Tid | Vad | Vem | Källa |
|-----|-----|-----|-------|
| **Torsdag 15:30-16:00** | Efter vecko-slutabstämning | Team Lead | AI:s mötes-sammanfattning |
| | Copy-pasta AI:s sammanfattning | Team Lead | MEETING_THURSDAY resultat |
| | - Vad blev klart denna vecka? | | git log |
| | - Vilka issues är WIP? | | GitHub Project |
| | - Vilka blockers finns? | | Sprint möte discussion |
| | - Plan för nästa vecka | | Sprint möte beslut |
| **Måndag före 09:00** | Uppdatera för ny sprint | Team Lead | MEETING_MONDAY resultat |
| | - Nya issues tilldelad | | Sprint meeting |
| | - Nya blockers identifierade | | Sprint meeting |
| | - Uppdaterad risk-status | | RISKS.md |

**Resultat:** CURRENT_STATUS.md är ALLTID aktuell (max 2h gammal)

**Du behöver:** 5-10 min efter varje sprintmöte för uppdatering

---

### **RISKS.md** (VIKTIG)

| Tid | Vad | Vem | Källa |
|-----|-----|-----|-------|
| **Torsdag efter möte** | Uppdatera risk-status | Team Lead | Möte-diskussion |
| | Nya risker identifierade? | | Möte-resultat |
| | Mitigations gjorda denna vecka? | | Möte-resultat |
| | Risk-prioritering förändrad? | | Möte-diskussion |
| **Veckovis (tisdag)** | Granska risk-register | Team Lead | CURRENT_STATUS.md |
| | Något nytt som är risk? | | Daily work |
| | Något som är löst? | | Daily work |

**Resultat:** RISKS.md är aktuell (uppdaterad 1x per vecka minimum)

**Du behöver:** 5 min efter möte + 5 min på tisdag

---

### **SCHEDULE.md** (REFERENSDOKUMENT - I _memory/)

| Tid | Vad | Vem | Källa |
|-----|-----|-----|-------|
| **Vid sprintstart (Måndag)** | Verifierar denna veckas fokus | Team Lead | _memory/SCHEDULE.md |
| | Finns det nya workshops/blockers? | | Canvas-kalender |
| | Deadlines denna vecka? | | Canvas-kalender |
| **Vid deadline-ändringar** | Uppdatera _memory/SCHEDULE.md | Team Lead | Externa ändringar |
| **Sällan** | Uppdateras bara om plan ändras | | |

**Resultat:** SCHEDULE.md är "baseline" plan, sällan ändrad (ligger i _memory som referens)

**Du behöver:** 2 min vid sprintstart

---

### **SPRINT_PLANNING.md** (REFERENSMATERIAL)

| Tid | Vad | Vem | Källa |
|-----|-----|-----|-------|
| **Sällan** | Uppdateras bara om process ändras | Team Lead | Retro-feedback |
| | T.ex. "Vi börjar pair-program från nästa vecka" | | Team möte |
| | "Vi ändrar estimat-format" | | Feedback |

**Resultat:** SPRINT_PLANNING.md är stabil och fungerar som guide

**Du behöver:** 0 min (uppdateras mycket sällan)

---

## 🔄 Vecko-Cykel Konkret

### **TORSDAG 15:00-15:30**
```
Sprint-möte (Vecko-slutabstämning)
↓
15:30 AI ger sammanfattning
↓
15:30-16:00 Du:
  1. Copy-pasta AI:s sammanfattning → _sprint/CURRENT_STATUS.md
  2. Uppdatera "Completed This Week" sektion
  3. Uppdatera "WIP" sektion
  4. Uppdatera "Blockers" sektion
  5. Notera "Plan för nästa vecka"
  6. Granska RISKS.md - några nya risker?
  7. Uppdatera risk-status
  
RESULTAT: CURRENT_STATUS.md och RISKS.md är FRESH
```

### **MÅNDAG 09:00-12:00**
```
Sprint-möte (Sprintplanering)
↓
12:00 AI ger sammanfattning
↓
12:00-12:30 Du:
  1. Copy-pasta AI:s sammanfattning → _sprint/CURRENT_STATUS.md
  2. Uppdatera "Sprint Backlog" tabell
  3. Uppdatera "Issues Planned This Sprint"
  4. Notera nya blockers
  5. Uppdatera risk-status baserat på ny sprint
  
RESULTAT: CURRENT_STATUS.md och RISKS.md är READY för veckan
```

### **TISDAG**
```
10:00 Snabb review:
  1. Läs RISKS.md
  2. Någon ny risk identifierad från idag?
  3. Uppdatera risk-status
  
RESULTAT: RISKS.md är aktuell
```

---

## ✅ Checklista: Vad Uppdateras När?

### **Efter Torsdag-Möte (15:30-16:00):**
- [ ] CURRENT_STATUS.md - "Completed This Week" uppdaterad
- [ ] CURRENT_STATUS.md - "WIP" uppdaterad
- [ ] CURRENT_STATUS.md - "Blockers" uppdaterad
- [ ] RISKS.md - Nya risker identifierade?
- [ ] RISKS.md - Risk-status uppdaterad

### **Efter Måndag-Möte (12:00-12:30):**
- [ ] CURRENT_STATUS.md - "Sprint Backlog" uppdaterad
- [ ] CURRENT_STATUS.md - Nya issues noterad
- [ ] RISKS.md - Risk-status för ny sprint
- [ ] SCHEDULE.md - Denna veckas fokus verifierad

### **Tisdag (10:00):**
- [ ] RISKS.md - Någon ny risk från idag?
- [ ] Uppdaterad risk-status

---

## 🚀 Total Uppdaterings-Tid Per Vecka

```
Torsdag efter möte:   10 min (copy-pasta + risk update)
Måndag efter möte:    10 min (copy-pasta + new sprint)
Tisdag:                5 min (risk review)
Övriga dagar:          0 min (system kör själv)

TOTAL: ~25 min per vecka för att hålla dokumenten fresh
```

---

## ⚠️ Vad Händer Om Du INTE Uppdaterar?

```
❌ CURRENT_STATUS.md är gammal
  → Nästa möte startar med förvirad data
  → AI kan inte ge korrekt analys
  → Mötet blir ineffektivt

❌ RISKS.md är gammal
  → Nya risker missas
  → Mitigations spåras inte
  → Överraskningar inträffar under sprinten

❌ SCHEDULE.md är felaktig
  → Fokus är oklart
  → Deadlines glöms
  → Sprint blir hafsig
```

**Utan uppdateringar = Systemet hasar!**

---

## 📝 Template: Post-Möte Uppdatering

**Torsdag efter möte:**

```markdown
# Copy-Pasta Denna Mall Till CURRENT_STATUS.md

## 🟢 Completed This Week (V37)
✅ Issue #52: Portfolio API - DONE
✅ Issue #57: Integration Tests - DONE

## 🟡 In Progress (WIP)
🔄 Issue #54: Dashboard Connection - 60% (väntar på #52's API)
🔄 Issue #56: FX Module - 50% (active commits idag)

## 🚨 Blockers & Risks This Week
- Blocker #1: None currently
- Risk #1: FX-modul langsam (update: benchmarking this week)
- Risk #2: Test coverage low (update: 40% now, target 70% by V6)

## 📅 Next Week Focus (V38)
- Priority 1: Complete #54 (Dashboard)
- Priority 2: Complete #56 (FX Module)
- Priority 3: Hit 60% test coverage
```

---

## 🎯 Summa Summarum

**Systemet fungerar bara om dokumenten är aktuella.**

**Uppdaterings-regel:**
- ✅ Efter TORSDAG-möte → CURRENT_STATUS.md + RISKS.md
- ✅ Efter MÅNDAG-möte → CURRENT_STATUS.md + RISKS.md
- ✅ Tisdag → RISKS.md quick check
- ✅ Total: 25 min/vecka

**Utan uppdateringar = Systemet kraschar.**

---

*Last Updated: 2026-09-04*  
*Purpose: Keep living documents fresh*  
*Owner: Team Lead*
