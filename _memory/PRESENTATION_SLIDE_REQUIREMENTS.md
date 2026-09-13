# 📋 Presentation Slide Requirements - Sprint Planning Structure (13 mötepunkter)

**🚨 KRITISK REGEL: En mötespunkt ≠ en slide**

En mötespunkt kan motsvaras av 1-3 (eller fler) slides.
Varje slide märks med samma 📝-symbol för den mötespunkt den tillhör.
Slide-numreringen behöver INTE följa mötespunktens numrering.

**Exempel:**
- 📝④ Frontend kan bli Slide 5, 6, 7 (alla märkta 📝④)
- 📝⑦ Beroenden & blockers kan bli två slides (båda märkta 📝⑦)
- Sedan går vi vidare till 📝⑤ Backend

Det viktiga är **mötespunktssymbolen**, inte slide-numret.

---

## 📋 FRAMSIDA — Extremt enkel & ren (ingen/📝⓪)

```
HEADER:
  Vänster: "SPRINTPLANERING · TEAM 1"
  Höger: "Måndag 14 september · 09:00–10:30"

MAIN CONTENT (mycket whitespace):

Fokus med PL denna vecka

Säkerställa veckans prioriteringar, beroenden 
och vägen mot CTO-demo.

FOOTER (litet, 10-12pt, diskret):
Underlag kontrollerat inför mötet:
context_enginering · avanza-team1 · Git-status · Issues & PRs · Project Board
Mötesprotokoll: [kontrolleras före möte]

DESIGN:
✅ 70% tom yta
✅ Max 3 textblock
✅ Ingen agenda, inga kort, ingen extra info
✅ Fokus ligger på PL-fokus-texten
```

---

## 📌 📝① Sedan Förra Mötet (Done/Merged-vy)

```
MÅSTE INNEHÅLLA:
✅ Vad blev FAKTISKT klart och mergat till develop denna vecka?
✅ Konkreta commits från ALLA teammedlemmar (7 dagar)
✅ Issues som är Done
✅ Active branches (pågår denna vecka)

MEGA-REGEL 2: Verifiera git-status med commands:
  git log develop --since="7 days ago" --oneline
  git log --all --since="7 days ago" --oneline
  git branch -a

VISUELLA ELEMENT:
✅ Grön för mergad (done)
✅ Orange för pågår
✅ Röd för stale (>3 dagar utan commit)

ALLA TEAMMEDLEMMAR MÅSTE SYNAS:
Zaida, Björn, Tomac (Frontend)
Rasha, Erik (Backend)
Pär, Henrik (Native)
```

---

## 📌 📝② Sprintmål (Big picture, få element)

```
MÅSTE INNEHÅLLA:
✅ Vad ska denna sprint åstadkomma?
✅ Tydligt fokus (1-3 större mål)
✅ Ingen detaljering — bara målbilden

VISUELLA ELEMENT:
🎯 Stort, tydligt
📅 Deadline synlig
Mycket whitespace
```

---

## 📌 📝③ Nuläge (Samlad statusbild — Dashboard)

```
MÅSTE INNEHÅLLA:
✅ Var står projektet MOT sprintmålet?
✅ Övergripande status: 🟢 ON TRACK | 🟠 DELAY | 🔴 CRITICAL
✅ Framsteg denna vecka: från X → Y

VISUELLA ELEMENT:
📊 Progress bars
🟢🟠🔴 Färgad status-ikon
Minimal text
```

---

## 📌 📝④ Frontend (Team-status — kan vara 1-3 slides)

```
MÅSTE INNEHÅLLA (Team: Zaida, Björn, Tomac):
✅ Vad pågår och vad behöver teamet veta?
✅ Prioriterad issue-lista (MÅSTE-HA | BÖR-HA)
✅ Assignee: (#XX - PERSONENS NAMN)
✅ Risker & Blockers
✅ Status: 🟢🟠🔴

OBS: Kan behöva flera slides
- Slide X: 📝④ Frontend — nuläge
- Slide Y: 📝④ Frontend — prioriterade issues
- Slide Z: 📝④ Frontend — blockers

Alla märkta 📝④ så det är tydligt de tillhör samma mötespunkt.
```

---

## 📌 📝⑤ Backend (Team-status — kan vara 1-3 slides)

```
MÅSTE INNEHÅLLA (Team: Rasha, Erik):
✅ Vad pågår och vad behöver teamet veta?
✅ Prioriterad issue-lista (MÅSTE-HA | BÖR-HA)
✅ Assignee: (#XX - PERSONENS NAMN)
✅ Risker & Blockers
✅ Status: 🟢🟠🔴

OBS: Kan behöva flera slides, alla märkta 📝⑤
```

---

## 📌 📝⑥ Native/Systemutvecklare (Team-status — kan vara 1-3 slides)

```
MÅSTE INNEHÅLLA (Team: Pär, Henrik):
✅ Vad pågår och vad behöver teamet veta?
✅ Prioriterad issue-lista (MÅSTE-HA | BÖR-HA)
✅ Assignee: (#XX - PERSONENS NAMN)
✅ Risker & Blockers
✅ Status: 🟢🟠🔴

OBS: Kan behöva flera slides, alla märkta 📝⑥
```

---

## 📌 📝⑦ Beroenden & Blockers (Flödesdiagram — kan vara 1-2 slides)

```
MÅSTE INNEHÅLLA:
✅ Vad väntar på vad? (VAD BLOCKERAR VAD)
✅ Flödesschema med pilar
✅ Förväntad lösning + tid
✅ Åtgärd NU (konkret)

OBS: Kan behöva två slides:
- Slide X: 📝⑦ Integrationsberoenden
- Slide Y: 📝⑦ Kritiska blockers

Båda märkta 📝⑦
```

---

## 📌 📝⑧ Prioritering & Scope (Must/Next/Later)

```
MÅSTE INNEHÅLLA:
✅ Vad gör vi FÖRST denna vecka (MUST)?
✅ Vad kommer nästa vecka (NEXT)?
✅ Vad kan vi inte göra nu (LATER/SKIP)?

VISUELLA ELEMENT:
📊 Kort/kolumner för varje kategori
Färgad prioritet
```

---

## 📌 📝⑨ Kapacitet & Estimering (Kapacitetsvy)

```
MÅSTE INNEHÅLLA:
✅ Är mängden planerat arbete realistisk?
✅ Kapacitet per team (available vs needed)
✅ "Passar det?" → Ja/Nej

VISUELLA ELEMENT:
📊 Kapacitetsstapling
✅/⚠️/🔴 Status per team
```

---

## 📌 📝⑩ Risker (Risk → konsekvens → hantering)

```
MÅSTE INNEHÅLLA:
✅ Vilka risker kan göra att sprintplanen misslyckas?
✅ Konsekvens av risk
✅ Hantering/mitigation

VISUELLA ELEMENT:
🔴🟠⚠️ Risk-kort
Tydlig konsekvens
Konkret hantering
```

---

## 📌 📝⑪ Tekniska Beslut (Beslutskort)

```
MÅSTE INNEHÅLLA:
✅ Vilka beslut behöver tas eller dokumenteras?

EN RUTA PER BESLUT:
- VAD är beslutet
- VARFÖR är det viktigt
- Impact (vilka påverkas)
- Approved av
- Dokumenterat i

REGEL: Fyll inte ut mallen bara för att.
Visa bara de beslut som faktiskt finns denna vecka.
```

---

## 📌 📝⑫ Sprintplan + Nästa Steg (Vem gör vad, omedelbara åtgärder)

```
MÅSTE INNEHÅLLA:
✅ Per-team boxar (Frontend / Backend / Native)
✅ ALLA teammedlemmar har minst EN uppgift
✅ Issues + assignee + timmar
✅ OMEDELBARA NÄSTA STEG:
   ☐ GitHub Project Board uppdaterad
   ☐ Pair sessions bokade
   ☐ Alla vet sitt jobb och assignee
   ☐ Blockers dokumenterade

✅ DENNA VECKA - konkreta deadlines:
   🔴 TUE 14:00 — [action]
   📍 WED 09:00 — [action]
   📍 THU 14:00 — [action]
   🎯 FRI 16:00 — Sprint end

VISUELLA ELEMENT:
⬛ Svart border per team-box
☐ Checkboxes (copy-paste till protokoll)
👥 ALLA medlemmar måste finnas
⏰ Konkreta timmar
📍 Timeline med deadlines

REGEL: Nästa steg ingår INTE i egen punkt.
Det är den naturliga avslutningen på sprintplanen.
```

---

## 📌 📝⑬ Frågor till PL (Sista slide — diskussionsarbetsyta)

```
🚨 DENNA SLIDE ÄR ABSOLUT SISTA.

MÅSTE INNEHÅLLA:
✅ Vad behöver teamet få SVAR/BESLUT på från PL?
✅ Stor, enkel layout (denna slide ligger kvar under diskussion)

LAYOUT:
❓ FRÅGA 1: [kort fråga]
   Kontext: [varför frågar vi]
   SVAR: ____________________________________

❓ FRÅGA 2: [kort fråga]
   Kontext: [varför frågar vi]
   SVAR: ____________________________________

❓ FRÅGA 3: [kort fråga]
   Kontext: [varför frågar vi]
   SVAR: ____________________________________

VISUELLA ELEMENT:
❓ Stor fråge-symbol
Mycket whitespace för anteckningar
En fråga per rad

DENNA SLIDE LIGGER KVAR under mötet.
Det är arbetsytan för PL-diskussionen.
```

---

## 📌 STRUKTUR SUMMARY (13 mötepunkter, variabel slidantal)

```
🎬 FRAMSIDA (ingen mötespunktssymbol eller 📝⓪)
   Fokus med PL denna vecka

📝① Sedan förra mötet (1-2 slides)
📝② Sprintmål (1 slide)
📝③ Nuläge (1 slide)
📝④ Frontend (1-3 slides)
📝⑤ Backend (1-3 slides)
📝⑥ Native (1-3 slides)
📝⑦ Beroenden & Blockers (1-2 slides)
📝⑧ Prioritering & Scope (1 slide)
📝⑨ Kapacitet & Estimering (1 slide)
📝⑩ Risker (1-2 slides)
📝⑪ Tekniska Beslut (1 slide)
📝⑫ Sprintplan + Nästa Steg (1-2 slides)
📝⑬ Frågor till PL (1 slide — SISTA)

TOTALT: ~18-25 slides (varierar per vecka)

MÖTESLOGIK:
Framsida → ① Bakåt → ② Målbild → ③ Nuläge 
→ ④-⑥ Teamstatus → ⑦ Beroenden → ⑧ Prioritering 
→ ⑨ Kapacitet → ⑩ Risker → ⑪ Beslut → ⑫ Plan+Action 
→ ⑬ PL-Frågor

REGEL:
- Mötespunkt = informationskategori (inte slide)
- Kan ha 1-3+ slides beroende på innehål
- ALLA slides som tillhör samma punkt märks med samma symbol
- Symbolen är navigering genom mötet
```

---

**Senast uppdaterad:** 2026-09-13  
**Status:** 13 mötepunkter (①-⑬), variabel slidantal  
**KRITISKT:** ① MÅSTE visa commits från ALLA (7 dagar)  
**REGEL:** En mötespunkt kan ha flera slides — symbolen märker tillhörigheten
