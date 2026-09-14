---
name: presentation_structure
description: 14 mötespunkter (①-⑭) — ny logisk ordning från retrospekt till handlingsplan
metadata:
  type: reference
  critical: true
  version: 4.0
---

# 📋 PRESENTATION STRUCTURE — 14 Mötespunkter (①-⑭)

**🚨 ÖVERGRIPANDE REGEL: Presentationen Lär & Samarbetar, Rapporterar & Bygger Teamtänk**

Presentationen fyller TRE syften:

1. **TEAMTÄNK** — Inte individuell evaluering
   - Huvudansvarig får ALDRIG betyda ENSAM ansvarig
   - Presentationen ska undersöka: Hur kan teammedlemmar hjälpa, avlasta, paira eller täcka upp för varandra?
   - Fokus: **Vägen till gemensam leverans, inte individuella prestationer**

2. **BRANSCHPEDAGOGIK** — Lär domänvokabulär medan vi arbetar
   - Förklara bara ord som står på sliden
   - Varje branschterm markeras 📚 för att visa lärmål
   - Möten blir lärtillfällen, inte bara statusrapporter

3. **ACTIONBAR HANDLINGSPLAN** — Konkreta nästa steg
   - Punkt ⑬ är inte en checklista utan en faktisk **handlingsplan med ansvarig och tidsram**
   - Allt som sägs ska kunna omsättas direkt på GitHub

---

## 🚨 KRITISKA REGLER

**En mötespunkt ≠ en slide**
- En mötespunkt kan motsvaras av 1-3 (eller fler) slides
- Varje slide märks med samma 📝-symbol för mötespunkten den tillhör
- Presentationen kan ha 20-30 slides — antalet varierar per vecka

**Innan presentationen skapas: Obligatorisk Cross-Team Code & Contract Review**
- Granska actual code i alla aktiva branches/PRs
- Verifiera API-kontrakt (Frontend ↔ Backend)
- Verifiera JNA-kontrakt (Backend ↔ Native)
- Dokumentera avvikelser i relevanta mötespunkter (⑥, ⑦, ⑩)

**VIKTIGT: Team + Assignad ALLTID synlig**
- Varje issue/PR måste visa: `#XX Titel (Team: Frontend/Backend/Native) — Assignad: Namn`
- Inget arbete utan tydlig ägare och team-tillhörighet
- Fallback: Om assignad saknas → "Ej assignad — behöver ägare"

**Ingen checklista — bara faktisk data**
- Slidorna fylls med verklig GitHub-data, inte tomma checkboxes
- Se [MANDATORY_READING_ORDER.md](../../MANDATORY_READING_ORDER.md) för vilka GitHub-åtgärder som behövs

**KÄLLREFERENSER — Mycket liten text (footer), inte i fokus**
- Varje slide som visar data MÅSTE visa käll-status i 8-10pt grå text längst ner
- Exempel: `Källa: GitHub PR #95 ✅ | Mötesprotokollet ⚠️ INTE NÅBAR`
- Denna text får INTE ta fokus från innehål — den är för verifikation, inte läsning
- Placering: Footer eller margin (aldrig i slide-innehål)
- **KRITISKT:** Om någon källa INTE är nåbar → MÅSTE visas i presentationen (ej gömt)
  - Exempel: `Mötesprotokollet: ⚠️ Inte nåbar (fallback: Slack summary)`
  - Syfte: Människan kan se vad som är verifierat vs vad som är fallback
- Syfte: Möjliggör transparens utan att distrahera från innehål

**PEDAGOGISKA FÖRKLARINGAR — 📚 märkta ord & begrepp**
- Varje branschterm eller okänd term MÅSTE förklaras på samma slide
- Märka med 📚 för att visa att det är ett lärmål
- Exempel på slide ③ (Frontend):
  ```
  📝③ FRONTEND — Denna sprint
  
  | Issue | Titel | Assignad | Status | Blocker |
  |-------|-------|----------|--------|---------|
  | #88 | Critical interactions 📚 | Björn | ◐ PÅG | API-kontrakt |
  
  📚 "Critical interactions" = användares viktigaste workflows i appen
                               (login, payment, data-entry)
  ```
- ADHD/Dyslektiker sparar tid — kan läsa ordet OCH förklaringen tillsammans
- Mötet blir lärmöte, inte bara statusrapport

---

## 🎬 FRAMSIDA (Ingen 📝-symbol)

**Syfte:** Mötet börjar här. Rena fokus.

**MÅSTE INNEHÅLLA:**
- ✅ Möte-header: "SPRINTPLANERING · TEAM 1" + datum/tid
- ✅ PL-fokus denna vecka (1-2 meningar)
- ✅ Footer: Underlag kontrollerat inför mötet (context_engineering, avanza-team1, Git-status, Issues & PRs, Project Board, Code review-status, Mötesprotokollet)

**FORMAT:**
```
HEADER: SPRINTPLANERING · TEAM 1 | Måndag 14 september · 09:00–10:30

MAIN (70% tom yta):

Fokus denna vecka:
Säkerställa veckans prioriteringar, beroenden
och vägen mot CTO-demo.

FOOTER (litet, 10-12pt):
Underlag: context_engineering ✓ | avanza-team1 ✓ | Git-status ✓ |
Issues & PRs ✓ | Project Board ✓ | Code review: [status] |
Mötesprotokollet: [status]
```

**DESIGN:**
- ✅ 70% tom yta
- ✅ Max 3 textblock
- ✅ Ingen agenda, inga kort, ingen extra info
- ✅ Fokus ligger på PL-fokus-texten

---

## 📝① AVKLARAT SEDAN FÖRRA MÖTET (1-2 slides)

**Syfte:** Vad blev FAKTISKT klart denna vecka? Retrospekt.

**MÅSTE INNEHÅLLA:**
- ✅ Konkreta merged PRs denna vecka (alla team)
- ✅ Commits per team-medlem (5-7 dagar tillbaka)
- ✅ Active branches (brancher med aktivitet senaste veckan)
- ✅ **ALLA 7 team-medlemmar måste synas** — antingen med arbete eller "Ingen issue denna vecka"

**DATA-KILDER (MANDATORY):**
- 📊 [Merged PRs denna vecka](../../data/DATA_SOURCES.md) — GitHub
- 📊 [Commits denna vecka](../../data/DATA_SOURCES.md) — GitHub
- 📊 [Branches develop + active](../../data/DATA_SOURCES.md) — GitHub

**Se [SLIDE_DETAIL_SPEC.md](../design/SLIDE_DETAIL_SPEC.md) för exakt format och exempel.**

---

## 📝② NULÄGE & DEADLINE (1 slide)

**Syfte:** Var står vi nu? Vad är deadlines denna vecka?

**MÅSTE INNEHÅLLA:**
- ✅ Procent-färdig per team-område
- ✅ Tidsplan (är vi i tid?)
- ✅ Vad saknas?
- ✅ Kritiska deadlines denna vecka
- ✅ Blocker-status (snabb översikt)

**Se [SLIDE_DETAIL_SPEC.md](../design/SLIDE_DETAIL_SPEC.md) för exakt format och exempel.**

---

## 📝③ FRONTEND (1-3 slides)

**Syfte:** Vad jobbar Frontend på denna sprint? Vad behövs härnäst?

**MÅSTE INNEHÅLLA:**
- ✅ Issues denna sprint per medlem
- ✅ Blockad-status (väntar på vad?)
- ✅ Nästa steg
- ✅ API-kontrakt-beroenden

**Se [SLIDE_DETAIL_SPEC.md](../design/SLIDE_DETAIL_SPEC.md) för exakt format och exempel.**

---

## 📝④ BACKEND (1-3 slides)

**Syfte:** Vad jobbar Backend på denna sprint? Vad är blockerande andra teams?

**MÅSTE INNEHÅLLA:**
- ✅ Issues denna sprint per medlem
- ✅ Blockad-status (väntar på vad?)
- ✅ API-kontrakt-status (definierat? Dokumenterat?)
- ✅ Nästa steg

**Se [SLIDE_DETAIL_SPEC.md](../design/SLIDE_DETAIL_SPEC.md) för exakt format och exempel.**

---

## 📝⑤ NATIVE (1-3 slides)

**Syfte:** Vad jobbar Native på denna sprint? Är de blockerade?

**MÅSTE INNEHÅLLA:**
- ✅ Issues denna sprint per medlem
- ✅ Blockad-status (väntar på vad?)
- ✅ Nästa steg
- ✅ JNA-kontrakt-status (Backend ↔ Native)

**Se [SLIDE_DETAIL_SPEC.md](../design/SLIDE_DETAIL_SPEC.md) för exakt format och exempel.**

---

## 📝⑥ BLOCKERS & DEPENDENCIES (1-2 slides, inkl. code-review)

**Syfte:** Vilka är blockade? Vilka är kritiska? Vilka risker finns i koden?

**MÅSTE INNEHÅLLA:**
- ✅ Alla aktiva blockers (röd lista)
- ✅ Alla deldependenser (gult — kan lösas denna vecka)
- ✅ Code-review-resultat från alla aktiva branches
- ✅ Visuell blockerträd eller tabell

**DATA-SOURCES:**
- 📊 GitHub Project Board
- 🔍 Code review från alla aktiva branches/PRs

**Se [SLIDE_DETAIL_SPEC.md](../design/SLIDE_DETAIL_SPEC.md) för exakt format och exempel.**

---

## 📝⑦ RISKER (1-2 slides, inkl. code-review)

**Syfte:** Vilka risker kan göra sprintplanen misslyckas? Vad kan gå fel?

**MÅSTE INNEHÅLLA:**
- ✅ Risken (vad kan gå fel?)
- ✅ Sannolikhet & konsekvens
- ✅ Hantering/mitigation (vad gör vi åt det?)
- ✅ Code-review-fynd som klassificeras som risker

**DATA-KILDER:**
- 🔍 Code review findings (från punkt ⑥)
- 📊 GitHub Project Board divergens (Board status ≠ faktisk Git-status)

**Se [SLIDE_DETAIL_SPEC.md](../design/SLIDE_DETAIL_SPEC.md) för exakt format och exempel.**

---

## 📝⑧ KAPACITET & ESTIMERING (1 slide)

**Syfte:** Passar detta i veckans tid? Är vi överbelastade?

**MÅSTE INNEHÅLLA:**
- ✅ Tillgänglig kapacitet per team
- ✅ Planerat arbete denna vecka
- ✅ Bild: OK? Stramt? Överbelastat?
- ✅ Rekommendation om justering behövs

**Se [SLIDE_DETAIL_SPEC.md](../design/SLIDE_DETAIL_SPEC.md) för exakt format och exempel.**

---

## 📝⑨ PRIORITERING & SCOPE (1-2 slides) — FAS-BASERAD ORDNING

**Syfte:** Vad gör vi FÖRST denna vecka? Vad kommer senare? Vem gör vad? I VILKEN ORDNING?

**MÅSTE INNEHÅLLA:**
- ✅ Fas-baserad ordning (Fas 1 → 2 → 3 osv)
- ✅ **VARJE ITEM: Team + Assignad person**
- ✅ **Varför denna ordning?** (blockers, beroenden, konfliktrisker)
- ✅ Teamregel: "Max 1 aktiv + 1 queued per person"

**Se [SLIDE_DETAIL_SPEC.md](../design/SLIDE_DETAIL_SPEC.md) för exakt format och exempel.**

---

## 📝⑩ TEKNISKA BESLUT (1 slide, inkl. code-review)

**Syfte:** Vilka arkitektur-beslut behövs denna vecka? Vad fastslår vi?

**MÅSTE INNEHÅLLA:**
- ✅ Beslut som måste fattas denna vecka
- ✅ Var beslut påverkar design/scope
- ✅ Code-review-fynd som driver beslut
- ✅ Ägare för varje beslut

**Se [SLIDE_DETAIL_SPEC.md](../design/SLIDE_DETAIL_SPEC.md) för exakt format och exempel.**

---

## 📝⑪ SPRINTMÅL (1 slide)

**Syfte:** Vad är målet för denna sprint? Vad löser vi denna vecka?

**MÅSTE INNEHÅLLA:**
- ✅ Övergripande mål (1-2 meningar) — baserat på prioritering + kapacitet
- ✅ Koppling till projekt-roadmap
- ✅ Deadline/CTO-demo-datum
- ✅ Feasibility-check (realistiskt baserat på kapacitet?)

**Se [SLIDE_DETAIL_SPEC.md](../design/SLIDE_DETAIL_SPEC.md) för exakt format och exempel.**

---

## 📝⑫ SPRINTPLAN (1-2 slides)

**Syfte:** Timeplanen denna vecka. Möten, deadlines, milestones.

**MÅSTE INNEHÅLLA:**
- ✅ Daglig timplan (möten, kritiska milestones)
- ✅ Deadline per issue
- ✅ Demo-tidslinje

**Se [SLIDE_DETAIL_SPEC.md](../design/SLIDE_DETAIL_SPEC.md) för exakt format och exempel.**

---

## 📝⑬ NÄSTA STEG (1-2 slides — handlingsplan)

**Syfte:** Konkreta åtgärder efter mötet. Vem gör vad? Tidsram?

**MÅSTE INNEHÅLLA:**
- ✅ Konkreta GitHub-åtgärder (PR, issue, label, move-board)
- ✅ Ägare för varje åtgärd
- ✅ Deadline (samma dag/imorgon/denna vecka)
- ✅ Verifikation-punkt (hur vet vi att det är klart?)

**REGEL:** Varje punkt måste kunna verifieras på GitHub.

**Se [SLIDE_DETAIL_SPEC.md](../design/SLIDE_DETAIL_SPEC.md) för exakt format och exempel.**

---

## 📝⑭ FRÅGOR TILL PL (1 slide — SISTA)

**Syfte:** Öppna frågor som teamet behöver PL för att besvara.

**MÅSTE INNEHÅLLA:**
- ✅ Öppna frågor från teamet
- ✅ PL-beslut som saknas
- ✅ Scope-frågor ("ska vi inkludera X?")
- ✅ Tid för diskussion allokerad

**REGLER:**
- MAX 5-6 frågor per möte
- Börja med "IDAG-SVAR BEHÖVS: Ja" — de höga prioriteten
- PL måste kunna svara direkt, inte "vi återkommer"

**Se [SLIDE_DETAIL_SPEC.md](../design/SLIDE_DETAIL_SPEC.md) för exakt format och exempel.**

---

## 🔗 SYSTEMÖVERSIKT

```
FÖRE PRESENTATION BYGGS:
  1. Läs MANDATORY_READING_ORDER.md ← allt du behöver
  2. Hämta data från alla GitHub-sources (se DATA_SOURCES.md)
  3. Verifiera alla sources enligt RENDER_GATE_CHECKLIST.md
  4. Code review alla aktiva branches/PRs för punkt ⑥, ⑦, ⑩
  5. Bygg slides enligt denna struktur (①-⑭)
  6. Slutgranskning innan rendering

NÄR PRESENTATIONEN ÄR KLAR:
  ✅ Punkt ① visar ALLA 7 team-medlemmar (arbete eller "ingen issue")
  ✅ Punkt ③-⑤ visar alla issues med Team + Assignad + Blocker
  ✅ Punkt ⑥ visar både blockers OCH code-review-resultat
  ✅ Punkt ⑨ visar MUST/NEXT/LATER med Team + Assignad
  ✅ Punkt ⑦ visar risker driven av code-review-fynd
  ✅ Punkt ⑧ visar kapacitet-analys (feasible?)
  ✅ Punkt ⑪ visar sprintmål HÄRLEDD från data, inte förutfattad
  ✅ Punkt ⑬ visar konkreta GitHub-åtgärder, inte vague tasks
  ✅ Punkt ⑭ har max 5-6 frågor, prioriterade
  ✅ Alla 14 punkter uppfyllda → RENDERING OK
```

---

**Version:** 4.0 (Ny logisk ordning: retrospekt → status → plan → åtgärd)  
**Senast uppdaterad:** 2026-09-14  
**Status:** PRODUCTION — Reorganiserad enligt användarens ordning
