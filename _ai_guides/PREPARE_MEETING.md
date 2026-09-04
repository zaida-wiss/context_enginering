# 📋 Förbered Nästa Sprintmöte

**Använd denna guide innan du startar ett möte. AI läser git-historiken och förbereder fresh data.**

---

## 🎯 Syfte

Innan du börjar ett möte (Torsdag eller Måndag), be AI att förbereda mötet genom att:
1. Läsa git-historiken denna vecka
2. Läsa aktuell status från dokumenten
3. Uppdatera fresh data
4. Presentera mötes-agenda
5. Då kan du och teamet starta mötet DIREKT efter

**Resultat:** Du har all information du behöver innan mötet börjar.

---

## 📖 Hur Det Fungerar

### Steg 1: Copy-Pasta Detta Till AI

**Kopiera länkarna och paste detta i AI-modellen tillsammans med AI_TEAMLEADER.md:**

```
PREPARE SPRINT MEETING:
=======================

Läs dessa guider:
- _ai_guides/AI_TEAMLEADER.md
- _ai_guides/PREPARE_MEETING.md

Sedan copy-pasta denna data:

1. Git log denna vecka:
[PASTE OUTPUT FRÅN: git log --since="1 week ago" --oneline --all]

2. Nuvarande status:
[PASTE INNEHÅLLET FRÅN: _sprint/CURRENT_STATUS.md]

3. Risk-register:
[PASTE INNEHÅLLET FRÅN: _sprint/RISKS.md]

4. Vilken typ av möte?
[ ] Torsdag vecko-slutabstämning (15:00-15:30)
[ ] Måndag sprintplanering (09:00-12:00)

Nu: Förbered mötet!
```

---

### Steg 2: AI Analyserar & Förbereder

**AI kommer då att:**

```
1️⃣  ANALYSERA GIT LOG
    - Vilka issues blev merged denna vecka?
    - Vilka branches är aktiva/inaktiva?
    - Vilka team jobbar på vad?
    - Identifiera blockers (inaktiva branches)

2️⃣  UPPDATERA STATUS
    - Markera merged issues som DONE
    - Notera WIP-issues med commits denna vecka
    - Flagga inactive branches som möjliga BLOCKERS
    - Se progress vs estimat

3️⃣  GRANSKA RISKER
    - Vilka risker är relevanta nu?
    - Är blockers nya risker?
    - Vilka mitigations är gjorda?

4️⃣  PRESENTERA MÖTES-AGENDA
    - "Här är vad vi gjort denna vecka"
    - "Här är status idag"
    - "Här är vilka issues vi ska diskutera"
    - "Här är vilka risker vi måste adressera"
```

---

### Steg 3: Mötet Börjar DIREKT Efter

**Du säger då till AI:**
- Torsdag: `"Kör torsdags-möte"`
- Måndag: `"Kör sprintplanering"`

**AI faciliterar mötet enligt struktur från MEETING_THURSDAY.md eller MEETING_MONDAY.md**

---

## 🔄 Hela Flödet (Exempel: Torsdag)

```
14:45 - Du ber AI: "Förbered torsdags-möte"
        [AI läser git log, CURRENT_STATUS, RISKS]
        [AI presenterar agenda]

15:00 - Du säger: "Kör torsdags-möte"
        [AI faciliterar mötet]
        [Ni avverkar punkter systematiskt]

15:30 - Mötet slutar
        [AI ger sammanfattning]
        [Du copy-pastas in i _sprint/CURRENT_STATUS.md]

Nästa vecka upprepar ni processen!
```

---

## 📊 Vad AI Analyserar Från Git Log

### Commits = Arbete Som Är Gjort

```
git log output denna vecka:
├── feat(backend): Add portfolio API (#52) ← DONE
├── feat(frontend): Connect dashboard (#54) ← WIP, commits idag
├── feat(native): FX conversion (#56) ← Inactive 2 days
└── test(backend): Integration tests (#57) ← WIP, commits igår

AI analyserar:
✅ #52 DONE - Merged denna vecka
🔄 #54 WIP - Aktiv idag
🔄 #57 WIP - Aktiv igår
⚠️ #56 BLOCKED? - Ingen commit på 2 dagar
```

### Branches = WIP Status

```
Branches denna vecka:
├── feature/#52-portfolio-api → MERGED (DONE)
├── feature/#54-dashboard-connection → Active commits (WIP)
├── feature/#56-fx-module → Last commit 2 days ago (BLOCKED?)
└── feature/#57-integration-tests → Active commits (WIP)

AI flaggar:
- #52: Completed this week ✅
- #54, #57: On track 🔄
- #56: No progress today ⚠️
```

---

## 🎯 Pre-Möte Agenda (Vad AI Presenterar)

**Innan mötet börjar, AI presenterar:**

```
📋 MÖTES-AGENDA FÖR TORSDAG 15:00

DENNA VECKA GJORDE VI:
✅ Issue #52: Portfolio API completed and merged
✅ Issue #57: Integration tests written (in progress)

DENNA VECKA WIP:
🔄 Issue #54: Dashboard connection (active today)
🔄 Issue #56: FX module (last commit 2 days ago - CHECK IF BLOCKED)

🚨 FLAGGADE RISKER:
- Risk #1: FX-modul langsam (update: no progress this week?)
- Risk #2: BE-FE integration (update: #54 on track)

💡 MÖTES-FOKUS:
1. Bekräfta #52 är fully done
2. Diskutera #54 framsteg
3. Ask: Why is #56 inactive? Blocker?
4. Uppdatera risk status

Är ni redo att börja mötet? Säg "Kör torsdags-möte"
```

---

## ⚡ Snabbversion: Copy-Paste Commands

**Använd dessa commands för att snabbt förbered mötet:**

### Terminal:
```bash
# Copy denna veckas commits (med diff)
git log --since="1 week ago" --oneline --stat --all | pbcopy

# Eller se full detalj med vad som ändrades
git log --since="1 week ago" -p --all | pbcopy

# Enkelt: bara commits
git log --since="1 week ago" --oneline --all
```

**Varför `--stat` eller `-p`?**
- `--stat` = hur många filer/linjer ändrades per commit
- `-p` = visa faktisk kod som ändrades (mer detalj)
- AI kan då se VÅRDEN på arbetet, inte bara "commitmessage"

### Sedan i AI:
```
Förbered mötet med denna data:
[PASTE GIT LOG OUTPUT HÄR]

Läs även:
_sprint/CURRENT_STATUS.md
_sprint/RISKS.md

Möte typ: [ ] Torsdag [ ] Måndag
```

---

## 🚨 Red Flags AI Bör Leta Efter

### I Git Log:
- ❌ Branch med NO commits på > 2 dagar → Möjlig blocker
- ❌ Massa commits på samma issue → Scope creep?
- ✅ Regular commits → On track
- ✅ Merged PRs → Completed work

### Bör Säga Till Teamet:
```
"Jag noterade att #56 har ingen commit på 2 dagar.
Är vi blockad? Behöver vi pair-program för att unblock?"
```

---

## 📚 Relaterade Filer

- **AI_TEAMLEADER.md** - Huvudinstruktion för AI
- **MEETING_THURSDAY.md** - Torsdags-möte struktur
- **MEETING_MONDAY.md** - Måndags-möte struktur
- **_sprint/CURRENT_STATUS.md** - Uppdateras efter möte

---

## ✅ Checklista: Innan Du Säger "Förbered Mötet"

- [ ] Git log är uppdaterad (alla commits pushad)
- [ ] CURRENT_STATUS.md är senaste version
- [ ] RISKS.md är aktuell
- [ ] Du vet vilken typ av möte det är (Torsdag/Måndag)
- [ ] Du har 5 min innan mötet börjar

**Då:** Ber du AI att förbered mötet.

---

*Last Updated: 2026-09-04*  
*Purpose: Pre-meeting preparation using git history*  
*Workflow: Git Log → AI Analysis → Fresh Agenda → Meeting Starts*
