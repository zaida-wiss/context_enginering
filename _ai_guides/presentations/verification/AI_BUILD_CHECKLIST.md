---
name: ai_build_checklist
description: AI-instruktioner — obligatoriska regler innan presentation byggs
metadata:
  type: ai_instructions
  critical: true
  version: 1.0
---

# 🤖 AI BUILD CHECKLIST — Obligatoriska Regler Före Presentationsbygning

**DENNA FIL GÖR ALDRIG VAL PÅ PRESENTATIONEN.**

**Denna fil talar till AI:n om VAD som måste kollas INNAN presentation byggs.**

---

## 🚨 OBLIGATORISK REGEL 1 — MÖTESPUNKTSMARKÖRER

**VARJE slide MÅSTE märkas med mötespunktsymbol överst vänster.**

```
RÄTT:
  ✅ 📝① SEDAN FÖRRA MÖTET — Levererat denna vecka
  ✅ 📝② SPRINTMÅL & FOKUS
  ✅ 📝③ NULÄGE — Övergripande status

FEL:
  ❌ "SEDAN FÖRRA MÖTET — Levererat denna vecka" (ingen symbol)
  ❌ "Nuläge" (saknas symbol, rubrik tydlig men inte märkad)

REGEL: Om presentationen har slide utan symbol = presentationen är FELBYGGD
       även om innehållet råkar matcha rätt mötespunkt

VARFÖR: Symbolerna navigerar mötet. Utan dem kan inte mötesledaren
        snabbt hitta rätt del av presentationen.
```

---

## 🚨 OBLIGATORISK REGEL 2 — DATA-KILDER ENDAST FRÅN REPO & GITHUB

**Presentationen rekonstrueras ENDAST från:**
- ✅ context_enginering repo (regler, format)
- ✅ GitHub Project data denna vecka (issues, PRs, commits)
- ✅ Meeting protocol denna vecka (Google Docs)
- ✅ Google Sheets fallback (från DATA_SOURCES.md)

**Presentationen använder ALDRIG:**
```
❌ Tidigare konversationer eller chathistorik
❌ Design-intuition från andra presentationer
❌ Personliga minnesanteckningar
❌ Antaganden utan GitHub-verifiering
❌ Uppfunna data eller nya issues
```

---

## 🚨 OBLIGATORISK REGEL 3 — TEMA-MEDLEMMAR IDENTITETSVERIFIERADE

**Före någon presentation byggs:**

```
☐ Läs TEAM_ROSTER.md
☐ Verifiera att ALLA 7 medlemmar är identitetsverifierade från git commits
☐ Noll okända namn i presentationen
☐ Varje namn som förekommer måste existera i TEAM_ROSTER
```

**Om någon medlem saknas i presentationen:**
→ STOP — undersök varför
→ Verifiering misslyckad

---

## 🚨 OBLIGATORISK REGEL 4 — KÖR RENDER_GATE_CHECKLIST

**Före presentation byggs — kör RENDER_GATE_CHECKLIST.md:**

```
☐ DATA COMPLETENESS — Alla 9 sources nåbara eller fallback?
☐ TEAM COVERAGE — Alla 7 medlemmar representerade?
☐ DESIGN RULES UNDERSTOOD — Läst VISUAL_DESIGN_MANDATORY?
```

**Om någon check misslyckas:**
→ STOP — presentationen får inte byggas
→ Rapportera problemet

---

## 🚨 OBLIGATORISK REGEL 5 — NO META-INSTRUCTIONS ON SLIDES

**AI-regler, presentationsspecifikationer, formatteringsregler och instruktioner om hur presentationen skapas får ALDRIG visas för mötesdeltagarna.**

ENDAST resultatet av reglerna får synas.

**Exempel på vad som är INSTRUKTION (får inte på slide):**
- "Assignee på varje aktiv issue"
- "5-sekunders-testet för visual-first"
- "Render QA checklist"
- "Verifiera brancher mot develop"
- "Denna regel är tvingande"

**Exempel på vad som är MÖTESINNEHÅL (får vara på slide):**
- "#43 – API client · ?? (Beslut idag: vem tar detta?)"
- Integration-diagram med Zaida, Rasha, Pär + branches
- "🟠 Behöver synkas: login request/response"
- "Backend-branch ligger 75 commits efter develop"

**Publiktest för varje textrad:**
```
"Skulle en projektledare säga detta till teamet på mötet,
utan att förklara att en AI skapade presentationen?"

Om nej → Ta bort texten från sliden.
```

---

## 🚨 OBLIGATORISK REGEL 6 — PER-SLIDE DATA-VERIFIKATION

**Varje slide MÅSTE verifieras mot faktiska sources innan rendering:**

### För varitka slide som visar issue/PR/commit:
```
Verifieringslista (internt för AI, ALDRIG på slide):
  ☐ Kan jag citera GitHub-länken?
  ☐ Kan jag se issue/PR/commit-hash på GitHub?
  ☐ Kan jag visa merge-datum från GitHub?
  ☐ Är assignee korrekt från GitHub-issue?
  ☐ Är status korrekt mot Project Board?
  ☐ Är DoD-status verifierad från issue-meddelandet?
```

**Om något svar är NEJ:**
→ Datan kom från konversation eller gissning, inte repo
→ Sliden är INVALID och måste byggas om från GitHub

---

## 🚨 OBLIGATORISK REGEL 7 — SOURCE-STATUS I PRESENTATIONEN

**Om någon källa INTE är nåbar:**

```
VISA detta på SLIDE:
  ⚠️ Mötesprotokollet: Inte nåbar (fallback: Slack summary)
  ⚠️ Risk Register: Inte nåbar (data från möte)

VISA ALDRIG:
  (tomrum — där källan skulle vara)
  "käll-status gömmd" 
  "vi antar källan är OK"
```

**Placering:** Footer eller margin (8-10pt, diskret, aldrig i fokus)

**Syfte:** Möjliggör transparens utan att distrahera från innehål

---

## 📋 INNAN PRESENTATION BYGGS — CHECKLISTA

✅ **OBLIGATORISK PRE-BUILD CHECKLIST:**

```
KÄLLKRAV & SANNINGSCHECK:
  [ ] INGENTING är fabricerat — ALLT från verifierade GitHub-sources
  [ ] Data matchar mötesprotokollet (ingen feltolkningar)
  [ ] Om vi är 🔴 KRITISK → texten säger KRITISK (inte dolt)
  [ ] Om vi ligger EFTER → texten säger det klart (inte dolt)
  [ ] Alla blockers är namngivna + timeline från mötet
  [ ] Åtgärder är KONKRETA (datum, tid, person)

SYMBOL & NUMRERING:
  [ ] VARJE slide har symbol 📝① överst VÄNSTER
  [ ] Symbol är TYDLIG (inte dold eller liten)
  [ ] Symbolen matchar mötespunkter (①-⑭)

INNEHÅL-SEPARERING (INGEN AI-INSTRUKTIONER):
  [ ] Publiktest: Skulle en PL säga denna textrad på mötet?
  [ ] Ingen AI-instruktioner exponerad
  [ ] Inga presentationsregler synliga för teamet
  [ ] Endast resultat av reglerna syns, inte reglerna själva

TEAM-MEDLEMMAR:
  [ ] Alla 7 medlemmar representerade (arbete eller "ingen issue denna vecka")
  [ ] Noll okända namn
  [ ] Alla namn från TEAM_ROSTER.md

FÄRGER & STATUS:
  [ ] 🟢🟠🔴⚪ färger matchar FAKTISK status (inte design-känsla)
  [ ] Ingen status-färg för neutral information
  [ ] Färgerna är KONSISTENTA överallt

SOURCE-STATUS:
  [ ] Om källa inte nåbar → visad på slide
  [ ] Fallback använd om nöden uppstår
  [ ] Transparens över vilka sources som är verifierade
```

---

## 🚨 KRITISKA REGLER

**Denna checklist är OBLIGATORISK. INGA UNDANTAG.**

```
❌ AI får INTE bygga presentation utan att köra denna checklista
❌ AI får INTE visa presentation utan att verifiera alla rules
❌ AI får INTE lämna AI-instruktioner i presentationen
❌ Presentationen får INTE innehålla okända namn
```

---

**Version:** 1.0  
**Status:** MANDATORY  
**Senast uppdaterad:** 2026-09-14
