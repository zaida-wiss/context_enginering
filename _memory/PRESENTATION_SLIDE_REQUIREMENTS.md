# 📋 Presentation Slide Requirements - Sprint Planning (14 mötepunkter)

**🚨 KRITISK REGEL: En mötespunkt ≠ en slide**

En mötespunkt kan motsvaras av 1-3 (eller fler) slides.
Varje slide märks med samma 📝-symbol för den mötespunkt den tillhör.
Presentationen kan ha 20-30 slides — antalet varierar per vecka.

**Innan presentationen skapas: Obligatorisk Cross-Team Code & Contract Review**
- Granska actual code i alla aktiva branches/PRs
- Verifiera API-kontrakt (Frontend ↔ Backend)
- Verifiera JNA-kontrakt (Backend ↔ Native)
- Kontrollera Auth-flow, datamodeller, felhantering
- Dokumentera avvikelser i relevanta mötespunkter

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
context_engineering · avanza-team1 · Git-status · Issues & PRs · Project Board
Code review: [status — kontrakt verifierade]
Mötesprotokoll: [status]

DESIGN:
✅ 70% tom yta
✅ Max 3 textblock
✅ Ingen agenda, inga kort, ingen extra info
✅ Fokus ligger på PL-fokus-texten
```

---

## 📌 📝① Sedan Förra Mötet (Done/Merged — 1-2 slides)

```
MÅSTE INNEHÅLLA:
✅ Vad blev FAKTISKT klart denna vecka?
✅ Konkreta commits från ALLA (7 dagar)
✅ Active branches
✅ Stale branches

ALLA TEAMMEDLEMMAR MÅSTE SYNAS:
- Zaida, Björn, Tomac (Frontend)
- Rasha, Erik (Backend)
- Pär, Henrik (Native)

VISUELLA ELEMENT:
✅ Grön för mergad (done)
✅ Orange för pågår
✅ Röd för stale (>3 dagar)
```

---

## 📌 📝② Sprintmål (Big picture — 1 slide)

```
MÅSTE INNEHÅLLA:
✅ Vad ska denna sprint åstadkomma?
✅ 1-3 tydliga fokusområden
✅ Deadline synlig

VISUELLA ELEMENT:
🎯 Stort, tydligt
📅 Deadline
Mycket whitespace
```

---

## 📌 📝③ Nuläge (Dashboard — 1 slide)

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

## 📌 📝④ Frontend (Team-status — 1-3 slides)

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

## 📌 📝⑤ Backend (Team-status — 1-3 slides)

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

## 📌 📝⑥ Native/Systemutvecklare (Team-status — 1-3 slides)

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

## 📌 📝⑦ Beroenden & Blockers (Flödesdiagram — 1-2 slides)

```
MÅSTE INNEHÅLLA:
✅ Vad väntar på vad? (VAD BLOCKERAR VAD)
✅ Flödesschema med pilar
✅ Förväntad lösning + tid
✅ Åtgärd NU (konkret)

FROM CODE REVIEW (MÅSTE INKLUDERAS):
✅ API-avvikelser som blockerar
✅ Kontrakt-missmatchningar
✅ Vilka är påverkade

VISUELLA ELEMENT:
➡️ Flödesdiagram med pilar
🔴🟠 Färgad prioritet
Tydlig konsekvens
```

---

## 📌 📝⑧ Prioritering & Scope (Must/Next/Later — 1 slide)

```
MÅSTE INNEHÅLLA:
✅ Vad gör vi FÖRST denna vecka (MUST)?
✅ Vad kommer nästa vecka (NEXT)?
✅ Vad kan vi inte göra nu (LATER)?

VISUELLA ELEMENT:
📊 Kort/kolumner för varje kategori
Färgad prioritet
```

---

## 📌 📝⑨ Kapacitet & Estimering (Kapacitetsvy — 1 slide)

```
MÅSTE INNEHÅLLA:
✅ Är mängden planerat arbete realistisk?
✅ Kapacitet per team (available vs needed)
✅ "Passar det?" → Ja/Nej/Knapp

VISUELLA ELEMENT:
📊 Kapacitetsstapling
✅/⚠️/🔴 Status per team
Konkreta timmar
```

---

## 📌 📝⑩ Risker (Risk-kort — 1-2 slides)

```
MÅSTE INNEHÅLLA:
✅ Vilka risker kan göra att sprintplanen misslyckas?
✅ Konsekvens av risk
✅ Hantering/mitigation

FROM CODE REVIEW (MÅSTE INKLUDERAS):
✅ Dubbelarbete-risk (teamen jobbar olika)
✅ Ohålbar riktning
✅ Framtida tech-skuld

VISUELLA ELEMENT:
🔴🟠⚠️ Risk-kort
Tydlig konsekvens
Konkret hantering
```

---

## 📌 📝⑪ Tekniska Beslut (Beslutskort — 1 slide)

```
MÅSTE INNEHÅLLA:
✅ Vilka beslut behöver tas eller dokumenteras?

EN RUTA PER BESLUT

FROM CODE REVIEW (MÅSTE INKLUDERAS):
✅ API-kontrakt som behöver fastslås
✅ JNA-kontrakt som behöver dokumenteras
✅ Auth-flow som behöver vara samma överallt
✅ Datamodell-avvikelser som behöver lösas

REGEL: Fyll inte ut mallen bara för att.
Visa bara de beslut som faktiskt finns denna vecka.
```

---

## 📌 📝⑫ Sprintplan (Vem gör vad — 1-2 slides)

```
MÅSTE INNEHÅLLA:
✅ Per-team boxar (Frontend / Backend / Native)
✅ ALLA teammedlemmar har minst EN uppgift
✅ Issues + assignee + timmar

VISUELLA ELEMENT:
⬛ Svart border per team-box
☐ Checkboxes (copy-paste till protokoll)
👥 ALLA medlemmar måste finnas
⏰ Konkreta timmar

REGEL: ENDAST vem gör vad.
Nästa steg ingår INTE här — det är egen mötespunkt.
```

---

## 📌 📝⑬ Nästa Steg (Konkret handlingsplan — 2 slides)

```
🚨 DENNA PUNKT ÄR INTE EN CHECKLISTA — DET ÄR HANDLINGSPLAN

MÅSTE INNEHÅLLA:

1. TILLDELNING — Vem tar vilken issue?
   - #XX → Zaida
   - #XX → Tomac
   - etc

2. NYA ISSUES SOM BEHÖVER SKAPAS
   - Ny issue: [namn] — [varför]
   - Ny issue: [namn] — [varför]

3. BEFINTLIGA ISSUES SOM BEHÖVER UPPDATERAS
   - #XX → förtydliga AC
   - #XX → lägg till dependency på #YY
   - #XX → uppdatera scope

4. ISSUES SOM MÅSTE PAUSAS/FLYTTAS
   - #XX flyttas från MUST till NEXT — [varför]
   - #XX pausas — [väntar på vad]

5. BLOCKERS — LÖSES HUR, NÄR, AV VEM
   - [Blocker] löses av [namn], [dag tid]
   - [Blocker] löses av [namn], [dag tid]

6. PAIRING/SUPPORT SOM BEHÖVER BOKAS
   - [namn] + [namn] pair prog på #XX — [dag tid]
   - [namn] mentorerar [namn] på #XX — [dag tid]

7. HÅLLBARHET — BEHÖVER PLANEN JUSTERAS?
   ✅ Arbetsbelastning per person/team — någon överbelastad? → flytta/pausa
   ✅ Beroenden — skapar väntetid? → prioritera först
   ✅ Single point of failure — någon är enda expert? → pairing/mentoring
   ✅ Framtida risker — skapar detta tech-skuld? → justera scope
   ✅ Åtgärder — alla poster har **ansvarig** och **tidsram**
   
   **Resultat: Planen är genomförbar utan att bryta ner teamet.**

8. KONTRAKT & BEROENDEN FRÅN CODE REVIEW
   - API-spec för #XX → uppdatera i shared doc
   - JNA-kontrakt för #XX → fastslå och dokumentera
   - Auth-flow → dokumentera i [länk]

9. DIREKT EFTER MÖTET — GITHUB ACTIONS
   ☐ GitHub Project Board uppdaterad
   ☐ Assignees satta
   ☐ Blockers/dependencies dokumenterade
   ☐ Issues på rätt sprint
   ☐ Tekniska beslut dokumenterade

VISUELLA ELEMENT:
📋 Numrerad lista (1-8)
✅ Tydlig struktur
🔴 Kritiska åtgärder markerade
👥 Ansvarig person på varje åtgärd
⏰ Tidsram för varje åtgärd

KAN BEHÖVA TVÅ SLIDES (båda märkta 📝⑬):
- Slide X: 📝⑬ GitHub-förändringar (1-4 ovan)
- Slide Y: 📝⑬ Konkreta åtgärder (5-8 ovan)
```

---

## 📌 📝⑭ Frågor till PL (Sista slide — diskussionsarbetsyta)

```
🚨 DENNA SLIDE ÄR ABSOLUT SISTA. LIGGER KVAR UNDER MÖTET.

MÅSTE INNEHÅLLA:
✅ Vad behöver teamet få SVAR/BESLUT på från PL?
✅ Stor, enkel layout

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
Det är arbetsytan för PL-diskussionen och dokumentation av svar.
```

---

## 📌 STRUKTUR SUMMARY (14 mötepunkter, variabel slidantal)

```
🎬 FRAMSIDA (ingen symbol eller 📝⓪)

📝① Sedan förra mötet (1-2 slides)
📝② Sprintmål (1 slide)
📝③ Nuläge (1 slide)
📝④ Frontend (1-3 slides)
📝⑤ Backend (1-3 slides)
📝⑥ Native (1-3 slides)
📝⑦ Beroenden & Blockers (1-2 slides, inkl. code-review)
📝⑧ Prioritering & Scope (1 slide)
📝⑨ Kapacitet & Estimering (1 slide)
📝⑩ Risker (1-2 slides, inkl. code-review)
📝⑪ Tekniska Beslut (1 slide, inkl. code-review)
📝⑫ Sprintplan (1-2 slides)
📝⑬ Nästa Steg (1-2 slides — handlingsplan)
📝⑭ Frågor till PL (1 slide — SISTA)

TOTALT: ~20-30 slides (varierar per vecka)

MÖTESLOGIK:
Framsida → ① Bakåt → ② Målbild → ③ Nuläge 
→ ④-⑥ Teamstatus → ⑦ Beroenden (+ code-review) 
→ ⑧ Prioritering → ⑨ Kapacitet → ⑩ Risker (+ code-review)
→ ⑪ Beslut (+ code-review) → ⑫ Plan 
→ ⑬ Nästa steg (konkret handlingsplan) 
→ ⑭ PL-Frågor (diskussion & svar)

RULES:
- En mötespunkt = informationskategori (inte slide)
- Kan ha 1-3+ slides beroende på innehål
- ALLA slides märks med samma symbol
- Symbolen är navigering genom mötet
```

---

**Senast uppdaterad:** 2026-09-13  
**Status:** 14 mötepunkter (①-⑭), variabel slidantal  

**KRITISKA KRAV:**
- ① MÅSTE visa commits från ALLA (7 dagar)
- FÖRE mötet: Obligatorisk Cross-Team Code & Contract Review
- ⑦, ⑩, ⑪: MÅSTE inkludera findings från code review
- ⑬ Nästa steg = konkret handlingsplan (INTE generisk checklista)
- ⑭ Frågor till PL är ABSOLUT SISTA punkt
- En mötespunkt kan ha flera slides — symbolen märker tillhörigheten
