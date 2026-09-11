# 📋 Presentation Slide Requirements - Vad varje slide MÅSTE innehålla

**Du kan redigera denna fil för att specificera vad varje slide ska innehålla.**

---

## 📌 Slide 1 — Presentationsslide

```
MÅSTE INNEHÅLLA:
✅ Möte-typ (SPRINT PLANNING)
✅ Tid (09:00-10:30)
✅ Syfte (Planera, prioritera & se blockers)

VISUELLA ELEMENT:
- Minimal text (max 3 rader)
- Mycket whitespace (60% tom yta)

FORMAT: PowerPoint/Google Slides/Markdown
```

---

## 📌 Slide 2 — Veckans kommande möten Agenda

```
MÅSTE INNEHÅLLA:
✅ Vad SKOLAN vill att vi gör denna vecka
✅ Datum & tid för möte med PL, samt mötets syfte för veckan

EXEMPEL INNEHÅL:
- CTO Demo feedback & architecture
- Risk assessment för slutleverans
- Team capacity & support needs

VISUELLA ELEMENT:
⬛ Svart border (neutral info)
🔢 Numrerad lista (1, 2, 3)
```

---

## 📌 Slide 3 — Veckans Schema & Mål

```
MÅSTE INNEHÅLLA:
✅ KURSMÅL denna vecka (från KURSMAL_OCH_BETYG.md)
✅ PROJEKTMÅL denna vecka (från GitHub Project Board)
✅ VECKANS TIDSPLAN (från mötesprotokollet)

VISUELLA ELEMENT:
📚 Ikon för kursmål
🚀 Ikon för projektmål
📍 Timeline med ikoner (MON, TUE, WED, THU)
📊 Progress: från X → Y (14/17 → 16/17)

FORMAT: Två spalter (KURSMÅL | PROJEKTMÅL)
```

---

## 📌 Slides 4-7 — Övergripande Mål & Status

```
SLIDE 1: KURSEN (17 kursmål → G/VG betyg)
SLIDE 2: PROJEKTET (MVP v2)
SLIDE 3: AVANZA SOM KUND (Annas behov)
SLIDE 4: PROGRESS BOARD (Big team vs Small teams)

VARJE SLIDE MÅSTE INNEHÅLLA:
✅ 📝① Symbol
✅ Mål / Syfte
✅ Deadlines (konkreta datum + tid)
✅ Status denna vecka (🟢🟠🔴)
✅ Framsteg (tal eller %)

VISUELLA ELEMENT:
📊 Progress bars (████░░)
🔢 Tal (14/17, 75%, etc)
🟢🟠🔴 Färgad status
📅 Deadlines med tid (4 nov 15:00)
```

---

## 📌 Slides 8-10 — Team-Status (Frontend/Backend/Native)

```
SLIDE 8: 📝② FRONTEND TEAM
SLIDE 9: 📝③ BACKEND TEAM
SLIDE 10: 📝④ NATIVE TEAM

VARJE TEAM-SLIDE MÅSTE INNEHÅLLA:
✅ 📝① Symbol
✅ Team namn + Status färg (🟢 ON TRACK)
✅ Progress bar (████░░)
✅ Issues: X/Y done
✅ Klart denna vecka
✅ Pågår
✅ Blockers (med assignee)

VISUELLA ELEMENT:
🎨 Färgad border (3px solid — status-färg)
📊 Progress bar
🏷️ Status-ord (ON TRACK / SLIGHT DELAY / CRITICAL)
👥 Assignee namn
⚠️ Blocker ikon om problem
```

---

## 📌 Slide 11 — Status Sedan Förra Veckan

```
MÅSTE INNEHÅLLA:
✅ 📝③ Symbol
✅ Vad blev klart förra veckan
✅ Vad pågår denna vecka
✅ Vad är blockat

VISUELLA ELEMENT:
✅ Ikon för klart
⏳ Ikon för pågår
⚠️ Ikon för blockat
🔢 Tal (antal issues)

FORMAT: 3-5 bullets max
```

---

## 📌 Slide 12 — Blockers (SEPARAT SLIDE)

```
MÅSTE INNEHÅLLA:
✅ 📝④ Symbol
✅ Varje blocker:
   - Namn/beskrivning
   - Väntar på vad/vem
   - Blockerar vilka tasks
   - Status (🔴 CRITICAL eller 🟠 DELAY)
   - Förväntat löst: [datum tid]
   - Åtgärd nu: [konkret]

VISUELLA ELEMENT:
⬛ Svart border runt blockers (neutral info)
🔴🟠 Status-färg INOM
➡️ Pilar visar blockering (väntar på → blockerar)
📍 Konkret tid när löst
```

---

## 📌 Slide 13 — Prioritering & Scope

```
MÅSTE INNEHÅLLA:
✅ 📝⑤ Symbol
✅ MÅSTE-HA denna vecka (med #issues)
✅ NICE-TO-HAVE (med #issues)
✅ "Kan vi göra allt?" → Ja/Nej
✅ Om nej: Scope cut (vad skips/väntar)

VISUELLA ELEMENT:
📊 Tabell (två spalter: MÅSTE-HA | NICE-TO-HAVE)
🟢 MÅSTE-HA in grön/bold
🟠 NICE-TO-HAVE in orange
#️⃣ Issue nummer MED assignee (#XX - Namn)
⏰ Timestimat (3h, 5h, etc)

FORMAT: ⬛ Svart border runt tabell
```

---

## 📌 Slide 14 — Estimering & Risk

```
MÅSTE INNEHÅLLA:
✅ 📝⑥ Symbol
✅ Kapacitet per team (available / needed)
✅ "Passar det?" → Ja/Nej
✅ Kända blockers + mitigation
✅ Risker + mitigation
✅ Framgångskriterier denna vecka

VISUELLA ELEMENT:
📊 Tabell (Team | Available | Needed | Buffer)
✅/❌ Visuell "passar det?" indikatör
⚠️ Risk-ikon
🎯 Framgångskriterier lista
```

---

## 📌 Slide 15 — Tekniska Beslut

```
MÅSTE INNEHÅLLA:
✅ 📝⑦ Symbol
✅ Varje tekniskt beslut:
   - Vad
   - Vem bestämde
   - Varför
   - Impact (vad ändrar)

FORMAT: 3-5 bullets max per beslut
```

---

## 📌 Slide 16 — Arbetsuppgifter (Issues denna vecka)

```
MÅSTE INNEHÅLLA:
✅ 📝⑧ Symbol
✅ Per-team boxar (Frontend / Backend / Native)
✅ Varje issue:
   - #XX nummer
   - Beskrivning
   - (#XX - Namn) ASSIGNEE OBLIGATORISK
   - Timestimat (h)

VISUELLA ELEMENT:
⬛ Svart border runt team-boxar
☐ Checkboxes för copy-paste
#️⃣ Issue nummer
👥 Assignee namn i parentes
⏰ Timestimat

FORMAT: Kan copy-pastas direkt till protokoll
```

---

## 📌 Slide 17 — Frågor till PL

```
MÅSTE INNEHÅLLA:
✅ 📝⑨ Symbol
✅ Förslag på rimliga frågor från team (eller "Inga frågor denna vecka")
✅ Vad behöver vi från PL denna vecka

FORMAT: 3-5 frågor max
```

---

## 📌 Slide 18 — Nästa Steg (SEPARAT)

```
MÅSTE INNEHÅLLA:
✅ 📝⑩ Symbol
✅ Omedelbar efter möte (idag):
   ☐ GitHub Project Board uppdaterad
   ☐ Pair sessions bokade
   ☐ Alla vet sitt jobb
   ☐ Blockers dokumenterade

✅ DENNA VECKAN - konkreta deadlines:
   🔴 MON 17:00 — [action] (KRITISK)
   📍 TUE 14:00 — [action]
   📍 WED 09:00 — [action]
   🎯 THU 15:00 — SPRINT END

VISUELLA ELEMENT:
☐ Checkboxes (copy-paste ready)
📍 Timeline med ikoner
🔴 Rött för kritisk
```

---

## 📌 Slide 19 — Sammanfattning (SEPARAT)

```
MÅSTE INNEHÅLLA:
✅ 📝⑪ Symbol
✅ DENNA VECKAS FOKUS (från mötesprotokollet)
✅ ÖVERGRIPANDE STATUS (🟢🟠🔴)
✅ FRAMSTEG (visuellt):
   • Kursmål: 14/17 → 16/17 ✅
   • Projekt: 75% → 85% MVP ✅

✅ KRITISKT ATT LÖSA (om något):
   [vad + tidline]

✅ MOTIVERANDE AVSLUT:
   "Lycka till denna vecka! Vi löser detta tillsammans."

VISUELLA ELEMENT:
📊 Statistik visuell (pil från X → Y)
🟢 Status färgad
💪 Motiverande ton
```

---

## 📌 Ändringshistorik

**Du kan ändra innehållet här utan att behöva läsa PRESENTATION_FORMAT_GUIDE.md**

Om du vill att en slide ska ha MINDRE eller MER innehål:
1. Redigera denna fil
2. Säg till AI: "Använd PRESENTATION_SLIDE_REQUIREMENTS.md för att veta vad varje slide ska innehålla"
3. AI läser denna fil ISTÄLLET för FORMAT_GUIDE för att veta vad som är required

**Senast uppdaterad:** 2026-09-11
**Status:** Editable requirements för varje slide
