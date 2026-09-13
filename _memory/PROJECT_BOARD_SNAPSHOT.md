---
name: project_board_snapshot
description: Snapshot of GitHub Project Board — AI reads this when Board API is not directly accessible
metadata:
  type: data
  snapshot_date: 2026-09-13
  snapshot_time: "08:42"
  snapshot_tz: "CEST"
  source: "GitHub Project Board export"
  instructions: "Update by: 1) Visit board URL, 2) Screenshot or copy column status, 3) Paste here organized by column"
---

# 📊 PROJECT BOARD SNAPSHOT — Status [DATUM]

**STATUS: TEMPLATE — FYLLA IN FÖRE MÖTET**

Använd denna process:
1. Öppna: https://github.com/orgs/chas-challenge-2026/projects/31/views/1
2. För varje kolumn: kopiera issues (eller screenshot)
3. Organisera efter kolumn nedan
4. Spara denna fil
5. Commit & push

---

## 📋 BOARD STATUS — [DATUM HH:MM CEST]

### 📥 BACKLOG

```
Issues i backlog (oplanerat arbete):
[Exempel: #XX — Titel (assignee)]
```

**Count:** [X issues]

---

### 🟦 READY

```
Issues redo att börja denna sprint:
[Exempel: #XX — Titel (assignee)]
```

**Count:** [X issues]

---

### 🟨 IN PROGRESS

```
Issues pågår denna vecka:
[Exempel: #XX — Titel (assignee - X% done)]
```

**Count:** [X issues]

---

### 🟪 IN REVIEW

```
Issues i code review / väntar på godkännande:
[Exempel: #XX — Titel (assignee)]
```

**Count:** [X issues]

---

### ✅ DONE

```
Issues färdiga denna vecka:
[Exempel: #XX — Titel (assignee - merged/closed datum)]
```

**Count:** [X issues]

---

## 📊 SAMMANFATTNING

| Kolumn | Count | % av Total |
|--------|-------|-----------|
| Backlog | [X] | [%] |
| Ready | [X] | [%] |
| In Progress | [X] | [%] |
| In Review | [X] | [%] |
| Done (denna vecka) | [X] | [%] |

**Totalt:** [X] issues

**Burndown denna vecka:** [X issues done av Y planerat]

---

## 🔧 TEKNISK INFO

**Denna fil uppdateras:**
- Före varje möte (board-status snappas här)
- Manuellt (ingen automatisk synk)

**AI läser denna fil när:**
- GitHub Project Board API inte är åtkomlig
- GitHub Connector inte fungerar
- Org-level project inte kan nås

**Tidsstämpel:** `[Datum] [Tid] [Tidszon]` — visar när snapshot är från

---

**Senast uppdaterad:** 2026-09-13
