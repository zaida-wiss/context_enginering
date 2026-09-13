# 📋 Presentation Slide Requirements - Sprint Planning Structure (13 mötepunkter)

**OBS: Denna struktur motsvarar mötesprotokollet 1:1. Varje mötepunkt kan ha 1-3 slides beroende på innehål.**

---

## 🎬 FRAMSIDA — Extremt enkel & ren

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

## 📌 Slide 1 — 📝① Sedan Förra Mötet (Done/Merged-vy)

```
MÅSTE INNEHÅLLA:
✅ Vad blev FAKTISKT klart och mergat till develop denna vecka?
✅ Konkreta commits från ALLA teammedlemmar
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

EXEMPEL:
✅ MERGAT DENNA VECKA (7 commits):
   Zaida: #42 Portfolio overview
   Tomac: #45 Risk metrics
   Björn: #44 Dashboard styling
   Rasha: #51 API-spec
   Erik: #52 Risk endpoint
   Pär: #60 iOS test
   Henrik: #61 Android widget
```

---

## 📌 Slide 2 — 📝② Sprintmål (Stor målbild, få element)

```
MÅSTE INNEHÅLLA:
✅ Vad ska denna sprint åstadkomma?
✅ Tydligt fokus (1-3 större mål)
✅ Ingen detaljering — bara målbilden

EXEMPEL:
🎯 Sprint: "Säkra kärnflödet & integration mot CTO-demo"

MÅL DENNA VECKA:
1. Portfolio end-to-end (Frontend + Backend)
2. Risk-dashboard integrerad
3. Mobile-appen synkroniserad med API

VISUELLA ELEMENT:
🎯 Stort, tydligt
📅 Deadline synlig (CTO-demo 24 sept)
Mycket whitespace
```

---

## 📌 Slide 3 — 📝③ Nuläge (Samlad statusbild)

```
MÅSTE INNEHÅLLA:
✅ Var står projektet MOT sprintmålet?
✅ Övergripande status: 🟢 ON TRACK | 🟠 DELAY | 🔴 CRITICAL
✅ Framsteg denna vecka: från X → Y

EXEMPEL:
🟢 ÖVERGRIPANDE: ON TRACK

Kursmål:  14/17 → 16/17 denna vecka (82% → 94%)
Projekt:  75% → 85% MVP denna vecka
Risk:     Två möjliga blockers (API-spec, simulator)

VISUELLA ELEMENT:
📊 Progress bars (████░░)
🟢🟠🔴 Stor färgad status-ikon
Minimal text
```

---

## 📌 Slide 4 — 📝④ Frontend (Team-status)

```
MÅSTE INNEHÅLLA (Team: Zaida, Björn, Tomac):
✅ Vad pågår och vad behöver teamet veta?
✅ Prioriterad issue-lista (MÅSTE-HA | BÖR-HA)
✅ Assignee: (#XX - PERSONENS NAMN) — INTE teamets namn!
✅ Risker & Blockers
✅ Status: 🟢🟠🔴

LAYOUT (max 4-5 issues per priority):
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

## 📌 Slide 5 — 📝⑤ Backend (Team-status)

```
MÅSTE INNEHÅLLA (Team: Rasha, Erik):
✅ Vad pågår och vad behöver teamet veta?
✅ Prioriterad issue-lista (MÅSTE-HA | BÖR-HA)
✅ Assignee: (#XX - PERSONENS NAMN) — INTE teamets namn!
✅ Risker & Blockers
✅ Status: 🟢🟠🔴

LAYOUT (max 4-5 issues per priority):
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

## 📌 Slide 6 — 📝⑥ Native/Systemutvecklare (Team-status)

```
MÅSTE INNEHÅLLA (Team: Pär, Henrik):
✅ Vad pågår och vad behöver teamet veta?
✅ Prioriterad issue-lista (MÅSTE-HA | BÖR-HA)
✅ Assignee: (#XX - PERSONENS NAMN) — INTE teamets namn!
✅ Risker & Blockers
✅ Status: 🟢🟠🔴

LAYOUT (max 4-5 issues per priority):
📌 MÅSTE-HA:
   ☐ #60 iOS test (Pär - 5h)
   ☐ #61 Android widget (Henrik - 7h)

📌 BÖR-HA:
   ☐ #63 Offline sync (Pär - 6h)

🔴 BLOCKERS: API-spec (#51), Simulator setup

VISUELLA ELEMENT:
📊 Progress bar (övergripande)
🎯 Issues + (#Namn)
⚠️ Externa beroenden tydliga
```

---

## 📌 Slide 7 — 📝⑦ Beroenden & Blockers (Flödesdiagram)

```
MÅSTE INNEHÅLLA:
✅ Vad väntar på vad? (VAD BLOCKERAR VAD)
✅ Flödesschema med pilar
✅ Förväntad lösning + tid
✅ Åtgärd NU (konkret)

VISUELLA ELEMENT:
➡️ FLÖDESDIAGRAM:
   Backend API-spec → blockerar Frontend #42, #43
   Simulator setup → blockerar Native all dev
   CTO feedback → blockerar Backend #51

🔴 KRITISKA (löses IDAG):
   🔴 Backend API-spec (löses TUE 14:00)

🟠 ALLVARLIGA (löses DENNA VECKA):
   🟠 Simulator setup (löses WED 09:00)

Pillarna ska visa tydligt vad som blockerar vad.
```

---

## 📌 Slide 8 — 📝⑧ Prioritering & Scope (Must/Next/Later)

```
MÅSTE INNEHÅLLA:
✅ Vad gör vi FÖRST denna vecka (MUST)?
✅ Vad kommer nästa vecka (NEXT)?
✅ Vad kan vi inte göra nu (LATER/SKIP)?

LAYOUT - TRE KATEGORIER:
🔴 MUST (denna vecka):
   #42, #43, #51, #52, #60, #61
   (18 timmar kapacitet)

🟠 NEXT (nästa vecka eller senare):
   #44, #45, #54, #63
   (14 timmar)

⚪ LATER (kan skjutas):
   #46, #62, #70
   (släpper vi denna sprint)

VISUELLA ELEMENT:
📊 Kort/kolumner för varje kategori
Färgad prioritet (🔴 MUST = rött/bold)
```

---

## 📌 Slide 9 — 📝⑨ Kapacitet & Estimering (Kapacitetsvy)

```
MÅSTE INNEHÅLLA:
✅ Är mängden planerat arbete realistisk?
✅ Kapacitet per team (available vs needed)
✅ "Passar det?" → Ja/Nej
✅ Buffer/risk?

LAYOUT - TABELL:
Team      | Available | Needed | Buffer | Status
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Frontend  | 40h       | 42h    | -2h    | ⚠️  (stretch)
Backend   | 32h       | 30h    | +2h    | ✅  (OK)
Native    | 24h       | 28h    | -4h    | 🔴 (under)

VISUELLA ELEMENT:
📊 Kapacitetsstapling
✅/⚠️/🔴 Status per team
Konkreta timmar
```

---

## 📌 Slide 10 — 📝⑩ Risker (Risk → konsekvens → hantering)

```
MÅSTE INNEHÅLLA:
✅ Vilka risker kan göra att sprintplanen misslyckas?
✅ Konsekvens av risk
✅ Hantering/mitigation

LAYOUT - RISKORT:
🔴 RISK 1: API-spec inte klar på tid
   Konsekvens: Frontend + Native blockerad, 4 dagar förlorad
   Hantering: Rasha börjar TIE morgon, daily standup kl 10:00

🟠 RISK 2: Simulator-setup-problem
   Konsekvens: Native kan inte testa på enhet
   Hantering: IT-support redan kontaktad, fallback: CI-testing

⚠️ RISK 3: CTO-demo feedback på arkitektur
   Konsekvens: Kan kräva omarbete vecka 3
   Hantering: Pre-demo-möte THU 14:00

VISUELLA ELEMENT:
🔴🟠⚠️ Risk-kort
Tydlig konsekvens
Konkret hantering
```

---

## 📌 Slide 11 — 📝⑪ Tekniska Beslut (Beslutskort)

```
MÅSTE INNEHÅLLA:
✅ Vilka beslut behöver tas eller dokumenteras?

EN RUTA PER BESLUT:
┌──────────────────────────────┐
│ 🔧 BESLUT 1: React Router v6 │
│ Beslutad av: Frontend team   │
│ Varför: Modernare API        │
│ Impact: #42, #44             │
│ Approved av: PL (TUE)        │
└──────────────────────────────┘

┌──────────────────────────────┐
│ 🔧 BESLUT 2: PostgreSQL pool │
│ Beslutad av: Backend team    │
│ Varför: Connection mgmt      │
│ Impact: #51, #52             │
│ Approved av: CTO             │
└──────────────────────────────┘

REGEL: En ruta = ett beslut. Fyll inte ut mallen,
        visa bara de beslut som faktiskt finns.
```

---

## 📌 Slide 12 — 📝⑫ Sprintplan (Vem gör vad, i vilken ordning?)

```
MÅSTE INNEHÅLLA:
✅ Per-team boxar (Frontend / Backend / Native)
✅ ALLA teammedlemmar har minst EN uppgift
✅ Issues + assignee + timmar

LAYOUT - TRE TEAMBOXAR:
┌─ FRONTEND ──────────────────┐
│ ☐ #42 Portfolio (Zaida - 5h)│
│ ☐ #43 Risk calc (Tomac - 8h)│
│ ☐ #44 Styling (Björn - 4h)  │
│ ☐ #45 Testing (Zaida - 6h)  │
└─────────────────────────────┘

┌─ BACKEND ───────────────────┐
│ ☐ #51 API-spec (Rasha - 3h) │
│ ☐ #52 Risk endpoint (Erik)  │
│ ☐ #54 Cache (Rasha - 4h)    │
└─────────────────────────────┘

┌─ NATIVE ────────────────────┐
│ ☐ #60 iOS test (Pär - 5h)   │
│ ☐ #61 Android (Henrik - 7h) │
│ ☐ #63 Offline (Pär - 6h)    │
└─────────────────────────────┘

VISUELLA ELEMENT:
⬛ Svart border per team-box
☐ Checkboxes (copy-paste till protokoll)
👥 ALLA medlemmar måste finnas
⏰ Konkreta timmar
```

---

## 📌 Slide 13 — 📝⑬ Nästa Steg (Omedelbar handlingsplan)

```
MÅSTE INNEHÅLLA:
✅ Vad händer DIREKT efter mötet (idag)?
✅ Vad händer under veckan (konkreta deadlines)?

LAYOUT:
🔴 IDAG (efter möte):
   ☐ GitHub Project Board uppdaterad
   ☐ Pair sessions bokade
   ☐ Alla vet sitt jobb
   ☐ Blockers dokumenterade

📍 DENNA VECKA - konkreta deadlines:
   🔴 TUE 14:00 — Backend pushes API-spec (KRITISK)
   📍 WED 09:00 — Simulator setup OK
   📍 THU 14:00 — Pre-demo-möte med CTO
   🎯 FRI 16:00 — Sprint end review

VISUELLA ELEMENT:
☐ Checkboxes (copy-paste ready)
📍 Tydlig timeline
🔴 Kritiska deadlines markerade
```

---

## 📌 Slide 14 — 📝⑬ Frågor till PL (Sista slide — diskussionsarbetsyta)

```
MÅSTE INNEHÅLLA:
✅ Vad behöver teamet få SVAR/BESLUT på från PL?
✅ Stor, enkel layout (denna slide ligger kvar under diskussion)

LAYOUT - FRÅGOR MED PLATS FÖR SVAR:

❓ FRÅGA 1: Arkitektur-feedback före CTO-demo?
   Behöver vi pre-review eller kan vi presentera torsdag?
   SVAR: ____________________________________

❓ FRÅGA 2: Scope-justering om simulator inte fixas?
   Kan vi skippa Native-testning eller behövs det?
   SVAR: ____________________________________

❓ FRÅGA 3: Resurs-support för underbelastad team?
   Native är 4 timmar under. Kan de ta extra från todo-listan?
   SVAR: ____________________________________

VISUELLA ELEMENT:
❓ Stor fråge-symbol
Mycket whitespace för anteckningar
En fråga per rad
Denna slide LIGGER KVAR medan ni diskuterar
```

---

## 📌 SLIDE STRUCTURE SUMMARY (14 slides totalt)

```
🎬 FRAMSIDA — Fokus med PL denna vecka (extrem enkel)

📝① Sedan förra mötet (Done/merged-vy)
📝② Sprintmål (Stor målbild)
📝③ Nuläge (Samlad statusbild — dashboard)
📝④ Frontend (Team-status)
📝⑤ Backend (Team-status)
📝⑥ Native (Team-status)
📝⑦ Beroenden & Blockers (Flödesdiagram)
📝⑧ Prioritering & Scope (Must/Next/Later)
📝⑨ Kapacitet & Estimering (Kapacitetsvy)
📝⑩ Risker (Risk-kort)
📝⑪ Tekniska Beslut (Beslutskort)
📝⑫ Sprintplan (Vem gör vad)
📝⑨ Frågor till PL (SISTA SLIDE — LÄMNAS UPPE)

REGEL: Varje mötepunkt = en tydlig funktion
       Slides varierar beroende på innehål (1-3 per punkt)
       Presentationen leder: Bakåt → Nuläge → Problem → Plan → PL
```

---

**Senast uppdaterad:** 2026-09-13  
**Status:** 13 mötepunkter, 1:1 med mötesprotokollet  
**Teammedlemmar:** Zaida, Björn, Tomac (Frontend), Rasha, Erik (Backend), Pär, Henrik (Native)
