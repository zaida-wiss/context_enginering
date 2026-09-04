# 🚀 Hur Du Kör Möten Med AI (Två Metoder)

**Välj metod beroende på var du använder AI.**

---

## 🌐 METOD 1: Web-Based AI (ChatGPT, Claude.ai, Gemini, etc.)

**Använd när:** Du använder AI i webbläsaren

**Workflow:**
```
1. Öppna AI i webbläsaren (ChatGPT, claude.ai, etc.)

2. Copy-pasta dessa länkar/innehål:
   - _ai_guides/AI_TEAMLEADER.md
   - _ai_guides/MEETING_THURSDAY.md (eller MEETING_MONDAY.md)
   - _sprint/CURRENT_STATUS.md (innehål)
   - _sprint/RISKS.md (innehål)

3. Säg: "Kör torsdags-möte" eller "Kör sprintplanering"

4. AI faciliterar mötet

5. AI ger sammanfattning (stora textblock)

6. Du:
   ✅ Copy-pastas sammanfattning
   ✅ Öppnar _sprint/CURRENT_STATUS.md lokalt
   ✅ Fyller in enligt UPDATE_SCHEDULE.md
   ✅ Sparar
```

**Fördel:** Fungerar överallt, vilken AI som helst
**Nackdel:** Manual copy-pasta, tar lite längre tid (5-10 min extra)

---

## 💻 METOD 2: VS Code + Claude Code (Lokal)

**Använd när:** Du är i VS Code med Claude Code, på rätt branch

**Workflow:**
```
1. Öppna projekt i VS Code
2. Säkerställ att du är på rätt branch (normalt "main" eller "team-prompt")
3. Öppna Claude Code (Alt+K eller via extension)

4. Copy-pasta dessa:
   - _ai_guides/AI_TEAMLEADER.md
   - _ai_guides/MEETING_THURSDAY.md (eller MEETING_MONDAY.md)
   - _sprint/CURRENT_STATUS.md (innehål)
   - _sprint/RISKS.md (innehål)

5. Säg: "Kör torsdags-möte" eller "Kör sprintplanering"

6. AI faciliterar mötet

7. AI FRÅGAR vid slutet:
   "✅ Mötet är klart! Vill du att jag uppdaterar:
    [ ] CURRENT_STATUS.md
    [ ] RISKS.md
    Eller båda?"

8. Du svarar: "Ja, uppdatera båda"

9. AI:
   ✅ Läser nuvarande filer
   ✅ Uppdaterar CURRENT_STATUS.md automatiskt
   ✅ Uppdaterar RISKS.md automatiskt
   ✅ Skapar commit (eller du gör det själv)
   ✅ Du är klar på 2 minuter
```

**Fördel:** Helt automatiserad, ingen manual copy-pasta, direkt till repo
**Nackdel:** Kräver VS Code + Claude Code

---

## 🤖 Vad AI Ska Göra (Beroende på Metod)

### **I Web-Based AI:**
```
AI säger:
"🎉 Mötet är klart!

Kopiera denna text och paste in i _sprint/CURRENT_STATUS.md:
[Längre textblock]

Sedan uppdatera RISKS.md med detta:
[Längre textblock]"
```

### **I VS Code/Claude Code:**
```
AI säger:
"✅ Mötet är klart!

Jag ser att du är i VS Code på rätt branch.
Vill du att jag uppdaterar dokumenten direkt?

[ ] Ja, uppdatera CURRENT_STATUS.md
[ ] Ja, uppdatera RISKS.md
[ ] Ja, uppdatera båda
[ ] Nej, jag gör det själv
[ ] Visa sammanfattningen (jag copy-pastas själv)"

[Om du klickar "Ja, uppdatera båda"]

Uppdaterar nu:
1. Läser _sprint/CURRENT_STATUS.md
2. Uppdaterar "Completed This Week" sektion
3. Uppdaterar "WIP" status
4. Uppdaterar "Blockers" sektion
5. Sparar

6. Läser _sprint/RISKS.md
7. Uppdaterar risk-status
8. Sparar

Klart! ✅
"
```

---

## 📋 Instruktioner för AI (Två Versioner)

### **Version 1: Web-Based (I prompt innan möte)**

```
Du kör möten för detta projekt.

Efter mötet: VISA SAMMANFATTNINGEN som text
(Användaren copy-pastas själv till filerna)

Säg EXAKT vilka sektioner de ska uppdatera och VAR.
```

### **Version 2: VS Code/Claude Code (I prompt innan möte)**

```
Du kör möten för detta projekt.

Du är i VS Code. Efter mötet:

1. FRÅGA: "Vill du att jag uppdaterar dokumenten direkt?"
   
2. Om JA:
   - Läs _sprint/CURRENT_STATUS.md
   - Uppdatera enligt mötes-resultat
   - Läs _sprint/RISKS.md
   - Uppdatera enligt mötes-resultat
   - Spara båda filerna
   
3. Om NEJ:
   - Visa sammanfattningen som text
   - Användaren copy-pastas själv

VIKTIGT: Bara uppdatera om du är säker på:
✅ Du är på rätt branch
✅ Filerna existerar
✅ Du är i rätt VS Code workspace
```

---

## 🎯 Rekommendation

### **För Sprint-Möten (Torsdag/Måndag):**
- **Web-based:** Ok, men manual copy-pasta tar tid
- **VS Code:** 👍 Rekommenderat - helt automatiserat

### **För Team-Möten (Backend/Frontend/Native):**
- **Web-based:** Ok, inte samma tidspress
- **VS Code:** 👍 Rekommenderat - snabbare

### **För Ad-Hoc Möten:**
- **Web-based:** Bäst - ingen setup behövs
- **VS Code:** Också ok

---

## ⚠️ Viktigt: VS Code-Uppdateringar

**AI ska ENDAST uppdatera automatiskt om:**

✅ Du är i VS Code med Claude Code
✅ Du är på rätt branch (main/team-prompt)
✅ Du har frågat AI att uppdatera
✅ AI är 100% säker på vilka filer att ändra

**AI ska ALDRIG:**
❌ Uppdatera utan att fråga först
❌ Uppdatera om den inte är säker på filen
❌ Skapa nya filer utan att fråga
❌ Göra commits utan att fråga

---

## 📝 Template: Två Prompts Du Kan Använda

### **Web-Based (Copy-Pasta Denna):**
```
Läs dessa guider:
- _ai_guides/AI_TEAMLEADER.md
- _ai_guides/MEETING_THURSDAY.md (eller _MONDAY.md)

Använd dessa dokument:
[Paste CURRENT_STATUS.md innehål]
[Paste RISKS.md innehål]

Nu: Kör torsdags-möte!

OBS: Efter mötet - visa sammanfattning som TEXT
(Jag copy-pastas själv till filerna)
```

### **VS Code/Claude Code (Copy-Pasta Denna):**
```
Läs dessa guider:
- _ai_guides/AI_TEAMLEADER.md
- _ai_guides/MEETING_THURSDAY.md (eller _MONDAY.md)

Använd dessa dokument:
[Paste CURRENT_STATUS.md innehål]
[Paste RISKS.md innehål]

Jag är i VS Code på branch "main"
Jag vill att du uppdaterar dokumenten direkt efter mötet

Nu: Kör torsdags-möte!

Fråga före uppdatering - OK eller nej?
```

---

## 🚀 Snabbversion: Vilken Metod Är Snabbast?

| Möte-Typ | Web-Based | VS Code | Vinnare |
|----------|-----------|---------|---------|
| Sprintmöte | 40 min + 10 min = 50 min | 40 min + 2 min = 42 min | VS Code 🎯 |
| Team-möte | 30 min + 5 min = 35 min | 30 min + 1 min = 31 min | VS Code 🎯 |
| Ad-hoc | 20 min + 3 min = 23 min | 20 min + 30 sec = 20.5 min | VS Code 🎯 |

**VS Code sparar tid & minskar felkällor (copy-pasta-missöden).**

---

## ✅ Checklista Innan Möte

### **Web-Based:**
- [ ] Öppna AI i webbläsare
- [ ] Copy-pasta alla guider + dokument
- [ ] Säg vilket möte du ska köra
- [ ] Förbered på att copy-pasta efter

### **VS Code:**
- [ ] Öppna VS Code
- [ ] Öppna Claude Code (Alt+K)
- [ ] Säkerställ rätt branch (`git branch`)
- [ ] Copy-pasta guider + dokument
- [ ] Säg vilket möte du ska köra
- [ ] AI uppdaterar automatiskt

---

*Last Updated: 2026-09-04*  
*Purpose: Clear instructions for two meeting workflows*  
*Recommendation: Use VS Code + Claude Code for automation*
