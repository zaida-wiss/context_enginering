# 🗂️ Mötesprotokoll — Sprint Planning (13 mötepunkter)

**Denna struktur är 1:1 med presentationen. Varje punkt motsvarar en mötsfunktion, inte en rapportering.**

---

## 📋 Framsida — Möte-info

```
SPRINTPLANERING · TEAM 1
Måndag [datum] · 09:00–10:30

Fokus med PL denna vecka
[Fokustext — kort och tydlig]

Underlag kontrollerat inför mötet:
[Källlista]
```

---

## 📝① Sedan Förra Mötet
**Vad blev faktiskt klart? (Done/merged-vy)**

**VIKTIG:** Visar commits från ALLA teammedlemmar (7 dagar tillbaka):
- Zaida, Björn, Tomac (Frontend)
- Rasha, Erik (Backend)
- Pär, Henrik (Native)

Git-status denna vecka:
- Mergade commits: 
  - Zaida: #[XX] [beskrivning]
  - Tomac: #[XX] [beskrivning]
  - Björn: #[XX] [beskrivning]
  - Rasha: #[XX] [beskrivning]
  - Erik: #[XX] [beskrivning]
  - Pär: #[XX] [beskrivning]
  - Henrik: #[XX] [beskrivning]

- Active branches (pågår denna vecka):
  - feature/#42-[person]
  - feature/#51-[person]
  - feature/#60-[person]

- Stale branches (>3 dagar, ingen commit):
  - [branch] — senaste commit: [datum]

---

## 📝② Sprintmål
**Vad ska denna sprint åstadkomma?**

Överordnat tema:
[Kort beskrivning av sprintens huvudsakliga fokus]

Tre huvudmål denna vecka:
1. [Mål]
2. [Mål]
3. [Mål]

Deadline: [CTO-demo, release, etc]

---

## 📝③ Nuläge
**Var står projektet mot sprintmålet?**

Övergripande status:
- 🟢 ON TRACK | 🟠 SLIGHT DELAY | 🔴 CRITICAL

Framsteg denna vecka:
- Kursmål: [X/Y] → [Y/Y] denna vecka
- Projekt: [X%] → [Y%]

Två möjliga blockers:
- [blocker 1]
- [blocker 2]

---

## 📝④ Frontend
**Vad pågår? Vad behöver teamet veta?**

Team: Zaida, Björn, Tomac

**MÅSTE-HA denna vecka:**
- #XX [beskrivning] (Zaida - Xh)
- #XX [beskrivning] (Tomac - Xh)
- #XX [beskrivning] (Björn - Xh)

**BÖR-HA (om tid):**
- #XX [beskrivning] (Zaida - Xh)
- #XX [beskrivning] (Tomac - Xh)

Blockers:
- Väntar på: [vad]
- Påverkar: [vilka issues]

Risk denna vecka:
- [risk beskrivning]

---

## 📝⑤ Backend
**Vad pågår? Vad behöver teamet veta?**

Team: Rasha, Erik

**MÅSTE-HA denna vecka:**
- #XX [beskrivning] (Rasha - Xh)
- #XX [beskrivning] (Erik - Xh)

**BÖR-HA (om tid):**
- #XX [beskrivning] (Rasha - Xh)

Blockers:
- Väntar på: [vad]
- Blockerar: [vilka team/issues]

Risk denna vecka:
- [risk beskrivning]

---

## 📝⑥ Native/Systemutvecklare
**Vad pågår? Vad behöver teamet veta?**

Team: Pär, Henrik

**MÅSTE-HA denna vecka:**
- #XX [beskrivning] (Pär - Xh)
- #XX [beskrivning] (Henrik - Xh)

**BÖR-HA (om tid):**
- #XX [beskrivning] (Pär - Xh)

Blockers:
- Väntar på: [vad]
- Externa beroenden: [IT-support, etc]

Risk denna vecka:
- [risk beskrivning]

---

## 📝⑦ Beroenden & Blockers
**Vad väntar på vad?**

Flöde 1: [blockare] → [vem påverkas]
- Väntar på: [konkret action]
- Förväntad lösning: [datum tid]
- Åtgärd NU: [konkret]

Flöde 2: [blockare] → [vem påverkas]
- Väntar på: [konkret action]
- Förväntad lösning: [datum tid]
- Åtgärd NU: [konkret]

---

## 📝⑧ Prioritering & Scope
**Vad gör vi först? Vad kan vänta?**

🔴 MUST denna vecka:
- #XX, #XX, #XX
- Totalt: XYh kapacitet
- Denna vecka: Vi gör DET HÄR

🟠 NEXT (nästa vecka eller senare):
- #XX, #XX, #XX
- Vi startar nästa vecka

⚪ LATER/SKIP:
- #XX, #XX
- Vi väljer bort detta denna sprint

---

## 📝⑨ Kapacitet & Estimering
**Är planen realistisk?**

Kapacitet denna vecka:
| Team     | Available | Needed | Buffer | Status |
|----------|-----------|--------|--------|--------|
| Frontend | XXh       | XXh    | ±Xh    | ✅/⚠️  |
| Backend  | XXh       | XXh    | ±Xh    | ✅/⚠️  |
| Native   | XXh       | XXh    | ±Xh    | ✅/⚠️  |

Svar: 🟢 Ja, vi passar | 🟠 Knapp | 🔴 Nej

Om underbelastat team:
- Extra arbete från [lista]
- Support till [team]

---

## 📝⑩ Risker
**Vad kan göra att sprintplanen misslyckas?**

**Risk 1: [risk]**
- Konsekvens: [vad blir påverkat]
- Sannolikhet: Låg / Medel / Hög
- Hantering: [konkret åtgärd]
- Ansvarig: [namn]

**Risk 2: [risk]**
- Konsekvens: [vad blir påverkat]
- Sannolikhet: Låg / Medel / Hög
- Hantering: [konkret åtgärd]
- Ansvarig: [namn]

**Risk 3: [risk]**
- Konsekvens: [vad blir påverkat]
- Sannolikhet: Låg / Medel / Hög
- Hantering: [konkret åtgärd]
- Ansvarig: [namn]

---

## 📝⑪ Tekniska Beslut
**Vad behöver beslutas eller dokumenteras?**

**Beslut 1: [kort titel]**
- Vad: [beskrivning av beslutet]
- Varför: [motivering]
- Impact: [vilka issues/team påverkas]
- Approved av: [namn]
- Dokumenterat i: [länk]

**Beslut 2: [kort titel]**
- Vad: [beskrivning av beslutet]
- Varför: [motivering]
- Impact: [vilka issues/team påverkas]
- Approved av: [namn]
- Dokumenterat i: [länk]

---

## 📝⑫ Sprintplan
**Vem gör vad, i vilken ordning?**

### FRONTEND (Zaida, Björn, Tomac)
- ☐ #XX [beskrivning] (Zaida - 5h)
- ☐ #XX [beskrivning] (Tomac - 8h)
- ☐ #XX [beskrivning] (Björn - 4h)
- ☐ #XX [beskrivning] (Zaida - 6h)
- ☐ #XX [beskrivning] (Tomac - 3h)

**Totalt:** XXh, XX% av kapaciteten

### BACKEND (Rasha, Erik)
- ☐ #XX [beskrivning] (Rasha - 3h)
- ☐ #XX [beskrivning] (Erik - 8h)
- ☐ #XX [beskrivning] (Rasha - 4h)

**Totalt:** XXh, XX% av kapaciteten

### NATIVE (Pär, Henrik)
- ☐ #XX [beskrivning] (Pär - 5h)
- ☐ #XX [beskrivning] (Henrik - 7h)
- ☐ #XX [beskrivning] (Pär - 6h)

**Totalt:** XXh, XX% av kapaciteten

---

## 📝⑬ Nästa Steg
**Vad händer direkt efter mötet? Under veckan?**

### IDAG (efter möte)
- ☐ GitHub Project Board uppdaterad
- ☐ Pair sessions bokade (om behövs)
- ☐ Alla vet sitt jobb och assignee
- ☐ Blockers dokumenterade i GitHub

### DENNA VECKA — konkreta deadlines
- **TUE 14:00** — [action] (KRITISK)
- **WED 09:00** — [action]
- **THU 14:00** — [action]
- **FRI 16:00** — Sprint end review

### MÖTEN DENNA VECKA
- **MON 09:00** — Sprint planning (denna)
- **TUE 10:00** — Daily standup (om behövs)
- **THU 14:00** — CTO pre-demo-review
- **FRI 16:00** — Sprint review & retro

---

## 📝⑬ Frågor till PL
**Vad behöver vi få svar/beslut på från PL?**

**Fråga 1: [kort fråga]**
- Kontext: [varför frågar vi]
- Behövs för: [vilken beslut/issue]
- **Svar:** ________________________________

**Fråga 2: [kort fråga]**
- Kontext: [varför frågar vi]
- Behövs för: [vilken beslut/issue]
- **Svar:** ________________________________

**Fråga 3: [kort fråga]**
- Kontext: [varför frågar vi]
- Behövs för: [vilken beslut/issue]
- **Svar:** ________________________________

---

## 📌 Möteslogik — Berättelsen från mötet

Flödet är:

1. **Sedan förra mötet** → Vad blev faktiskt klart? (VISA ALLAS ARBETE)
2. **Sprintmål** → Vad försöker vi nå?
3. **Nuläge** → Var står vi?
4-6. **Teamstatus** → Vad händer i varje arbetsström?
7. **Beroenden & blockers** → Hur påverkar arbetsströmmarna varandra?
8. **Prioritering** → Vad prioriterar vi?
9. **Kapacitet** → Har vi tid?
10. **Risker** → Vad kan hindra oss?
11. **Tekniska beslut** → Vad måste vi bestämma?
12. **Sprintplan** → Lås planen
13. **Frågor till PL** → Det vi behöver få svar på

**Presentationen följer denna logik exakt. Varje slide motsvarar en punkt.**

---

**Senast uppdaterad:** 2026-09-13  
**Status:** 13 mötepunkter, 1:1 med PRESENTATION_SLIDE_REQUIREMENTS.md  
**VIKTIGT:** Punkt ① MÅSTE visa commits från ALLA teammedlemmar (7 dagar tillbaka)
