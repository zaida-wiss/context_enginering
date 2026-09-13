---
name: project_board_snapshot
description: Snapshot of GitHub Project Board — FALLBACK ONLY (AI reads live board by default)
metadata:
  type: data
  snapshot_date: 2026-09-13
  snapshot_time: "08:42"
  snapshot_tz: "CEST"
  source: "GitHub Project Board (fallback only)"
  status: "OPTIONAL — not needed if live link works"
  instructions: "Only update if live Project Board link fails. Otherwise leave empty."
---

# 📊 PROJECT BOARD SNAPSHOT — Status [DATUM]

**STATUS: FALLBACK ONLY — Behövs bara om live-länken failar**

**LIVE-LÄNKEN (primär):**
https://github.com/orgs/chas-challenge-2026/projects/31/views/1

AI läser denna direkt. Denna snapshot behövs INTE om länken fungerar.

---

## Om länken failar — använd denna fallback

(Uppdatera bara om GitHub Project Board länken inte går att läsa)

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
