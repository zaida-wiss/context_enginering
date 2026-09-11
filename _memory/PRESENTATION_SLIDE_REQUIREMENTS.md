# 📋 Presentation Slide Requirements - Vad varje slide MÅSTE innehålla

**Du kan redigera denna fil för att specificera vad varje slide ska innehålla.**

---

## 📌 Slide 1 — FRAMSIDA (Möte-info)

```
MÅSTE INNEHÅLLA (TRE ELEMENT):

1️⃣ VÅD ÄR DET FÖR MÖTE?
   Exempel: SPRINTPLANERING (MÅNDAGSMÖTE)

2️⃣ TIDPUNKT
   Exempel: Måndag 14 september 2026, 09:00-10:30

3️⃣ SYFTE MED MÖTET
   Exempel: "Planera denna vecka, säkerställa vi når målen"

VISUELLA ELEMENT:
✅ Möte-ikon överst (📅 eller 🎯)
✅ Datum + tid väl synlig
✅ Mycket whitespace (70% tom yta)
```

---

## 📌 Slide 2 — AGENDA (Innehållsförteckning över alla mötespunkter)

```
MÅSTE INNEHÅLLA - ALLA 12 MÖTESPUNKTER:
✅ 📝① Status sedan förra möte
✅ 📝② Övergripande mål & status
✅ 📝③ Frontend team
✅ 📝④ Backend team
✅ 📝⑤ Native team
✅ 📝⑥ Prioritering & scope
✅ 📝⑦ Estimering & risk
✅ 📝⑧ Tekniska beslut
✅ 📝⑨ Beroenden & blockers
✅ 📝⑩ Arbetsuppgifter denna vecka
✅ 📝⑪ Frågor till PL
✅ 📝⑫ Nästa steg & sammanfattning

VISUELLA ELEMENT:
✅ Numrering tydlig (1-12 eller 📝①-⑫)
✅ Lätt att scanná
```

---

## 📌 Slide 3 — 📝① Status Sedan Förra Möte (Git Progress)

```
MÅSTE INNEHÅLLA:
✅ ALLA COMMITS denna vecka — FRÅN ALLA TEAMMEDLEMMAR
✅ VAD SOM KOMMIT IN TILL DEVELOP senaste veckan
✅ VAD SOM FINNS PÅBÖRJAT I ANDRA BRANCHER
✅ Vilka branches är stale (> 3 dagar utan commit)

MEGA-REGEL 2: VERIFIERA GIT-STATUS
Kör dessa commands för faktisk data:
  git log develop --since="7 days ago" --oneline
  git log --all --since="7 days ago" --oneline
  git branch -a
  git diff develop..feature/[branch] --stat

VISUELLA ELEMENT - VISA ALLAS ARBETE:
🟢 Grön för mergade (done) — Zaida, Björn, Tomac, Rasha, Erik, Pär, Henrik
🟠 Orange för active branches (pågår)
🔴 Röd för stale branches (inte aktivt denna vecka)

EXEMPEL:
✅ MERGAT DENNA VECKA (7 commits):
   Zaida: #42 Portfolio overview
   Tomac: #45 Risk metrics
   Rasha: #51 API-spec
   Erik: #52 Risk endpoint
   Pär: #60 iOS test
   etc...
```

---

## 📌 Slide 4 — 📝② Övergripande Mål & Status (HELA TEAMET)

```
MÅSTE INNEHÅLLA:
✅ HUR GÅR DET FÖR HELA TEAMET MOT MÅLEN?
   → 🟢 ON TRACK | 🟠 SLIGHT DELAY | 🔴 CRITICAL
✅ KURSMÅL DENNA VECKA (från KURSMAL_OCH_BETYG.md)
✅ PROJEKTMÅL DENNA VECKA (från GitHub Project Board)

VISUELLA ELEMENT:
🟢 Stor färgad status-ikon
📊 Progress bar: KURSMÅL (14/17 = 82%)
📊 Progress bar: PROJEKT (75% → 85%)
```

---

## 📌 Slide 5 — 📝③ FRONTEND TEAM Fokus denna vecka

```
MÅSTE INNEHÅLLA (Frontend: Zaida, Björn, Tomac):
✅ Alla Frontend-issues denna vecka (hele teamen tillsammans)
✅ Prioriterad lista (MÅSTE-HA | BÖR-HA)
✅ Assignee: (#XX - PERSONENS NAMN) — INTE teamets namn!
✅ Risker & Blockers
✅ Status: 🟢🟠🔴

LAYOUT (MAX 5-6 issues per priority):
📌 MÅSTE-HA:
   ☐ #42 Portfolio (Zaida - 5h)
   ☐ #43 Risk calc (Tomac - 8h)
   ☐ #44 Styling (Björn - 4h)

📌 BÖR-HA:
   ☐ #45 Testing (Zaida - 6h)
   ☐ #46 Error handling (Tomac - 3h)

🔴 BLOCKERS: API-spec (#51)

VISUELLA ELEMENT:
📊 Progress bar (övergripande)
🎯 Issues + (#Namn)
➡️ Blocker-pilar
```

---

## 📌 Slide 6 — 📝④ BACKEND TEAM Fokus denna vecka

```
MÅSTE INNEHÅLLA (Backend: Rasha, Erik):
✅ Alla Backend-issues denna vecka (hele teamen tillsammans)
✅ Prioriterad lista (MÅSTE-HA | BÖR-HA)
✅ Assignee: (#XX - PERSONENS NAMN) — INTE teamets namn!
✅ Risker & Blockers
✅ Status: 🟢🟠🔴

LAYOUT (MAX 4-5 issues per priority):
📌 MÅSTE-HA:
   ☐ #51 API-spec (Rasha - 3h)
   ☐ #52 Risk endpoint (Erik - 8h)

📌 BÖR-HA:
   ☐ #54 Cache (Rasha - 4h)

🔴 BLOCKERS: CTO arkitektur-feedback

VISUELLA ELEMENT:
📊 Progress bar (övergripande)
🎯 Issues + (#Namn)
➡️ Blocker-pilar
```

---

## 📌 Slide 7 — 📝⑤ NATIVE/SYSTEMUTVECKLARE TEAM Fokus denna vecka

```
MÅSTE INNEHÅLLA (Native/Systemutvecklare: Pär, Henrik):
✅ Alla Native-issues denna vecka (hele teamen tillsammans)
✅ Prioriterad lista (MÅSTE-HA | BÖR-HA)
✅ Assignee: (#XX - PERSONENS NAMN) — INTE teamets namn!
✅ Risker & Blockers
✅ Status: 🟢🟠🔴

LAYOUT (MAX 4-5 issues per priority):
📌 MÅSTE-HA:
   ☐ #60 iOS test (Sofia - 5h)
   ☐ #61 Android widget (Kevin - 7h)

📌 BÖR-HA:
   ☐ #63 Offline sync (Anna - 6h)

🔴 BLOCKERS: API-spec (#51), Simulator setup

VISUELLA ELEMENT:
📊 Progress bar (övergripande)
🎯 Issues + (#Namn)
⚠️ Externa beroenden tydliga
```

---

## 📌 Slide 8 — 📝⑥ Blockers (VISUELL FLÖDESDIAGRAM)

```
MÅSTE INNEHÅLLA:
✅ ALLA BLOCKERS denna vecka
✅ VAD BLOCKERAR VAD (visuell pillar)
✅ Vem som är blockerad
✅ Förväntat löst (datum + tid)
✅ Åtgärd NU (konkret)

VISUELLA ELEMENT:
➡️ FLÖDESDIAGRAM med pilar
🔴 KRITISKA (löser IDAG)
🟠 ALLVARLIGA (löser DENNA VECKA)
```

---

## 📌 Slide 9 — 📝⑦ Prioritering & Scope denna vecka

```
MÅSTE INNEHÅLLA:
✅ MÅSTE-HA denna vecka (med #issues + assignee)
✅ BÖR-HA denna vecka
✅ "Kan vi göra allt?" → Ja/Nej
✅ Om nej: Scope cut (vad skips/väntar)

VISUELLA ELEMENT:
📊 Tabell (två spalter: MÅSTE-HA | BÖR-HA)
🟢 MÅSTE-HA in grön/bold
🟠 BÖR-HA in orange
#️⃣ Issue nummer MED assignee (#XX - Namn)
⏰ Timestimat (3h, 5h, etc)
```

---

## 📌 Slide 10 — 📝⑧ Estimering & Risk denna vecka

```
MÅSTE INNEHÅLLA:
✅ KAPACITET per team (available vs needed)
✅ "Passar det?" → Ja/Nej
✅ KÄNDA RISKER + mitigation
✅ FRAMGÅNGSKRITERIER denna vecka
✅ Support-behov (om överbelastat)

VISUELLA ELEMENT:
📊 Tabell (Team | Available | Needed | Buffer | Status)
✅/⚠️ Visuell "passar det?" indikatör
🟢🟠🔴 Kapacitet-status per team
```

---

## 📌 Slide 11 — 📝⑨ Tekniska Beslut denna vecka

```
MÅSTE INNEHÅLLA:
✅ Varje tekniskt beslut:
   - VAD är beslutet
   - VEM bestämde (team eller PL)
   - VARFÖR är det viktigt
   - IMPACT (vad ändrar, vilka påverkas)

FORMAT: 2-3 beslut max, konkreta
```

---

## 📌 Slide 12 — 📝⑩ Arbetsuppgifter denna vecka (ALLA teammedlemmar)

```
MÅSTE INNEHÅLLA:
✅ Per-team boxar (Frontend / Backend / Native)
✅ ALLA teammedlemmar har minst EN uppgift tilldelad
✅ Varje issue:
   - #XX nummer
   - Beskrivning
   - (#XX - PERSONENS NAMN) OBLIGATORISK — ALLA ska synas!
   - Timestimat (h)

TEAMMEDLEMMAR (säkerställ alla är representerade):
Frontend: Zaida, Björn, Tomac
Backend: Rasha, Erik
Native: Pär, Henrik

VISUELLA ELEMENT:
⬛ Svart border runt team-boxar
☐ Checkboxes för copy-paste
#️⃣ Issue nummer
👥 Assignee namn i parentes — ALLA medlemmar!
⏰ Timestimat

FORMAT: Kan copy-pastas direkt till protokoll
```

---

## 📌 Slide 13 — 📝⑪ Frågor till PL

```
MÅSTE INNEHÅLLA:
✅ Rimliga frågor från team (eller "Inga frågor denna vecka")
✅ Vad behöver vi från PL denna vecka

FORMAT: 2-4 frågor max, konkreta
```

---

## 📌 Slide 14 — 📝⑫ Nästa Steg (ACTION ITEMS — SEPARAT)

```
MÅSTE INNEHÅLLA:
✅ OMEDELBAR ACTION (efter möte IDAG):
   ☐ GitHub Project Board uppdaterad
   ☐ Pair sessions bokade
   ☐ Alla vet sitt jobb och assignee
   ☐ Blockers dokumenterade

✅ DENNA VECKA - konkreta deadlines:
   🔴 MON 17:00 — [action] (KRITISK)
   📍 TUE 14:00 — [action]
   📍 WED 09:00 — [action]
   🎯 THU 15:00 — SPRINT END

VISUELLA ELEMENT:
☐ Checkboxes (copy-paste ready)
📍 Timeline med ikoner
🔴 Rött för kritiska deadlines
```

---

## 📌 Slide 15 — 📝⑫ Sammanfattning (SEPARAT från Nästa Steg)

```
MÅSTE INNEHÅLLA:
✅ DENNA VECKAS FOKUS (från mötesprotokollet)
✅ ÖVERGRIPANDE STATUS (🟢🟠🔴)
✅ FRAMSTEG - visuellt från X → Y:
   • Kursmål: 14/17 → 16/17 (denna vecka)
   • Projekt MVP: 75% → 85% (target denna vecka)

✅ MOTIVERANDE AVSLUT:
   "Vi gör detta tillsammans! Lycka till denna vecka!"

VISUELLA ELEMENT:
📊 Statistik visuell (pil från X → Y)
🟢 Status färgad (ON TRACK / DELAY / CRITICAL)
💪 Motiverande ton
```

---

## 📌 Slide 16 (VALFRITT) — Extra Context eller Reserve

```
VALFRITT — använd denna om behövs för:
✅ Veckans møter & deadlines
✅ Viktiga externa events
✅ Eller håll tom för framtida expansion
```

---

## 📌 SLIDE STRUCTURE SUMMARY

```
Totalt: 15 SLIDES REKOMMENDERAT (16 med reserve)

🚨 VIKTIGT: PRESENTATIONEN BÖRJAR MED SLIDE 1 (FRAMSIDA)
            ALDRIG någon "Slide 0" eller "mötespunkt 0" på presentationen!

1️⃣  FRAMSIDA (Möte-typ, tid, syfte)
2️⃣  AGENDA (alla 12 mötespunkter 📝①-⑫)
3️⃣  Status sedan förra (Git progress + branches) — 📝①
4️⃣  Övergripande status (hele teamet → 🟢🟠🔴) — 📝②
5️⃣  FRONTEND fokus denna vecka — 📝③
6️⃣  BACKEND fokus denna vecka — 📝④
7️⃣  NATIVE fokus denna vecka — 📝⑤
8️⃣  BLOCKERS (visuell flödesdiagram) — 📝⑥
9️⃣  Prioritering & Scope — 📝⑦
🔟 Estimering & Risk — 📝⑧
1️⃣1️⃣ Tekniska Beslut — 📝⑨
1️⃣2️⃣ Arbetsuppgifter (per team) — 📝⑩
1️⃣3️⃣ Frågor till PL — 📝⑪
1️⃣4️⃣ Nästa Steg (ACTION ITEMS) — 📝⑫
1️⃣5️⃣ Sammanfattning — 📝⑫
[1️⃣6️⃣ Reserve/Extra info — (ingen mötespunkt)]
```

---

**Senast uppdaterad:** 2026-09-11
**Status:** Editable requirements för 15-16 slides
**KRITISKT:** Slide 1 = FRAMSIDA, ALDRIG Slide 0 eller mötespunkt 0!
**NOTERING:** Slide 7 = NATIVE/SYSTEMUTVECKLARE team
g