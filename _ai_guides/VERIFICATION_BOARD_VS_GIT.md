# 🔍 Verifiering: GitHub Project Board vs Git History

**Git är SANNINGEN när källor motsäger varandra.**

## Problemet: Board Kan Stale

GitHub Project Board uppdateras manuellt. Det kan bli gammalt:
- Issue står "In Progress" men PR redan är mergad till develop
- Issue står "Done" men ingen commit finns
- Assignee är tom men Git visar vem som faktiskt jobbar
- Issue på Board som inte matchas av någon branch/PR

Git är autentisk: Varje commit är dateringad, signerad av utvecklaren, och kan verifieras tekniskt.

## Verifieringskedja

**Ordningen när du verifierar issue-status:**

```
1. Issue på GitHub — börjar här
   ↓
2. Länkad PR (om någon) — är det en PR?
   ↓
3. PR-status — är den approved?
   ↓
4. Merge-status — är den mergad till develop?
   ↓
5. Git log develop — finns commiten?
   ↓
6. Project Board — uppdaterar Board enligt Git-sanningen
```

## Statuskoder

Använd dessa när du rapporterar status i presentationer:

### 🟢 Verifierad — Git och Board överens
```
#42 Portfolio overview — KLAR ✓
Verifierat: PR mergad → finns på develop (commit 3a7f8c)
Status på Board: Done ✓
```

### 🟣 Git-Verifierad, Board Stale
```
#45 Risk metrics — FAKTISKT KLAR (Git visar mergad)
⚠️ Git bevis: PR mergad → finns på develop (commit 9e2b5d)
⚠️ Board visar: "In Progress" → behöver uppdateras
Förslag: Flytta till Done på Board
```

### ⚪ Board-Status, Ej Git-Verifierad
```
#51 Authentication — Status oklar
Board visar: "In Progress"
Git hittar: Ingen branch, ingen PR, ingen commit
Möjliga orsaker:
  - Arbete ej startad ännu
  - Arbete på annan branch som inte är uppkopplad
  - Board-status är gammal från tidigare vecka
Åtgärd: Bekräfta status med issueägare
```

### 🔴 Konflikt — Git och Board motsäger varandra
```
#40 Database schema — KONFLIKT
Board visar: "Done"
Git visar: Ingen PR, ingen commit (arbete ej påbörjat)
Möjliga orsaker:
  - Board uppdaterades av misstag
  - Arbetet pausades utan att uppdatera Board
  - Duplikat issue
Åtgärd: Förtydliga på mötet innan presentation
```

## Regler för Presentationer

### ✅ Du MÅSTE göra detta:

1. **Verifiera innan du presenterar**
   - Kör `git log --since="7 days ago" --oneline develop`
   - Kollar vilka issues faktiskt är mergade denna vecka
   - Jämför med Project Board

2. **Om Git och Board motsäger**
   - Git väger tyngre (Git är autentisk)
   - Märk Board-diskrepans i presentationen
   - Föreslå uppdateringar

3. **När du föreslår assignee för issue**
   - Kolla faktiskt Git-ägande (vem commitar?)
   - Kolla Project Board assignee
   - Om de motsäger: preferera Git-bevis

4. **För belastningsanalys**
   - Räkna bara faktiskt mergade/pågående arbete (Git)
   - Ignorera "In Progress" issues på Board utan Git-bevis
   - Risken: någon ser överbelastad i Board men är faktiskt nära färdigt

### ❌ Du SKA INTE:

- ❌ Presentera Board-status utan Git-verifiering
- ❌ Anta att "In Progress" på Board = faktiskt pågående arbete
- ❌ Basera belastning bara på Board-assignees
- ❌ Ignorera Git-bevis för att Board säger något annat

## Exempel: Belastningsanalys

**DÅLIG ANALYS (bara Board):**
```
Zaida: Assignee på 5 "In Progress"-issues
→ "Zaida är överbelastad"
```

**BRA ANALYS (Board + Git):**
```
Zaida: Assignee på 5 "In Progress"-issues
Git visar: 2 av dem är faktiskt mergade denna vecka
→ "Zaida har kvar 3 issues, 2 är faktiskt klara denna vecka"
Board-action: Flytta de 2 till Done
Belastning: Faktisk (inte överbelastad)
```

## För Nästa Sprintplanering

Innan presentationen:
1. Läs git log denna vecka
2. Jämför mot Project Board denna vecka
3. Märk var Board behöver uppdateras
4. Presentera Git-verifierad status
5. Ge konkreta Board-uppdateringsförslag

Detta gör att presentationen visar **FAKTISKA framsteg**, inte **vad Boarden påstår**.

---

**Senast uppdaterad:** 2026-09-13  
**Syfte:** Garantera att presentationen använder Git som källa av sanning när Board kan stale
