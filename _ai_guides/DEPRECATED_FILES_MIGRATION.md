# ⚠️ Deprecated Files - Migrationsguide

**Dessa filer refererar till det gamla systemet (CURRENT_STATUS.md, RISKS.md) som inte längre existerar.**

---

## 📋 Deprecated Files

| Fil | Varför Deprecated | Ersätts Av | Status |
|-----|---|---|---|
| `UPDATE_SCHEDULE.md` | Enbart för uppdatering av gamla filer | `VERIFICATION_SYSTEM.md` | 🔴 DELETE |
| `PREPARE_MEETING.md` | Instruktioner baserade på gamla kopiera-paste | `VERIFICATION_SYSTEM.md` | 🔴 DELETE |
| `HOW_TO_RUN_MEETINGS.md` | Copy-paste av gamla filer | Direct instructions i mötes-filerna | 🟡 UPDATE |

---

## ✅ Migration Summary

### OLD SYSTEM:
```
📝 CURRENT_STATUS.md (lokal fil)
📝 RISKS.md (lokal fil)
⚠️ Manual copy-paste mellan möte och filer
⚠️ Risk för outdated data
```

### NEW SYSTEM:
```
GitHub Project Board (primär källa för issues)
Google Sheets Risker (primär källa för risker)
Mötesprotokollet (primär källa för decisions)
git log (primär källa för commits)
VERIFICATION_SYSTEM.md (hur man verifierar consistency)
```

---

## 🔄 Vad Ändrades?

| Gammal Fråga | Gå Till | Ny Källa |
|---|---|---|
| "Vad är status denna vecka?" | `CURRENT_STATUS.md` | GitHub Project Board + git log |
| "Vilka risker finns?" | `RISKS.md` | Google Sheets Risker |
| "Vilka action items från möte?" | `UPDATE_SCHEDULE.md` | Mötesprotokollet |
| "Hur verifierar vi consistency?" | (Ingen guide) | `VERIFICATION_SYSTEM.md` |

---

## 📋 Files to Delete (SAFE TO REMOVE):
- [ ] `UPDATE_SCHEDULE.md` — Helt obsolet
- [ ] `PREPARE_MEETING.md` — Helt obsolet

---

## 🔄 Files to Keep But Update:
- [ ] `HOW_TO_RUN_MEETINGS.md` — Ta bort all referens till CURRENT_STATUS.md/RISKS.md
- [ ] `AI_TEAMLEADER.md` — Uppdatera data sources
- [ ] `MEETING_THURSDAY.md` — Uppdatera för nya sources
- [ ] `MEETING_MONDAY.md` — Uppdatera för nya sources

---

**Senast uppdaterad:** 2026-09-08
