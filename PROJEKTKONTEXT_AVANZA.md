---
name: projektkontext_avanza
description: KRITISK instruktion för vilken AI som helst som arbetar med Avanza-projektet
metadata:
  type: instruction
  required: true
  audience: all_ai_models
---

# 🎯 PROJEKTKONTEXT — AVANZA

**DENNA INSTRUKTION MÅSTE FÖLJAS av vilken AI-modell som helst som arbetar med Avanza-projektet.**

---

## TVÅ STEG — ALLTID I DENNA ORDNING

### STEG 1 — Läs styrningen från context-repot

Läs först aktuell projektkontext från:

**https://github.com/zaida-wiss/context_enginering**

Om repository-sidan inte ger filinnehållet, läs raw-versionen:

**https://raw.githubusercontent.com/zaida-wiss/context_enginering/main/README.md**

**README.md i context_enginering är den primära styrande källan.**

Den bestämmer:
- ✅ Vilka ytterligare context-filer som ska läsas
- ✅ Vilken läsordning som gäller
- ✅ Vilka projektkällor som ska användas
- ✅ Hur GitHub-data ska hämtas (Connector/Web, aldrig shell/git-kommandon)
- ✅ Fallback-strategier
- ✅ Källhierarki
- ✅ Presentations-, verifierings- och kvalitetsregler

**Följ README:s instruktioner innan projektdata hämtas.**

---

### STEG 2 — Hämta aktuell projektdata från Avanza-repot

När relevant styrning i context-repot har lästs ska aktuell projektspecifik fakta hämtas från de källor som context-repot anger.

**Huvudkälla för aktuell projektdata är:**

**https://github.com/chas-challenge-2026/avanza-team1**

Beroende på uppgiften ska detta omfatta relevanta delar av:

- Commits denna vecka
- Branches (develop + active features)
- Issues (open + closed denna vecka)
- Pull Requests (open + merged denna vecka)
- PR reviews och approvals
- Project Board status
- Aktuella filer i projekt-repot
- Mötesprotokoll
- Övriga källor som context-repot anger

**Context-repot anger HUR och VAR data ska hämtas.**
**Avanza-repot och dess associerade projektkällor innehåller den AKTUELLA projektfaktan.**

---

## KRITISK REGEL

**Läs INTE bara context-repot och dra därefter slutsatser om projektets nuläge.**

Aktuella påståenden om vad teamet HAR gjort, vad som PÅGÅR, vem som arbetar med vad, status på issues, PRs, blockers, sprintläge eller liknande **MÅSTE verifieras mot aktuell projektdata från Avanza-repot.**

### För presentationer — SPECIELL REGEL

**För presentationer gäller en obligatorisk läs- och datainsamlingssekvens:**

1. Läs **MANDATORY_READING_ORDER.md** från context-repot
2. Följ dess **RENDER_GATE_CHECKLIST** — presentationen stoppar om någon av 11 checkpoints missas
3. Hämta ALLA 9 datakällor som MANDATORY_READING_ORDER kräver
4. Verifiera IDENTITY för alla 7 team-medlemmar
5. Kör TEAM_COVERAGE_CHECK (alla 7 måste vara representerade)
6. Kör UNKNOWN_NAME_CHECK (bara faktiska namn, ingen example-data)
7. **Presentationen får INTE renderas utan att alla checks passeras**

---

## KÄLLHIERARKI

Vid konflikt mellan sources gäller denna ordning:

1. **Context-repot** (styrning, regler, format)
   - README.md (entry point)
   - MANDATORY_READING_ORDER.md (presentations-sekvens)
   - DATA_SOURCES.md (var data hämtas)
   - Övriga context-filer per område

2. **Avanza-repot + live-data** (aktuell projektfakta)
   - GitHub Issues + PRs (live-status)
   - Commits och branches (git-historia)
   - Project Board (board-status)
   - Mötesprotokoll (beslut, åtgärder)
   - Filer i projektet

3. **Fallback-strategier** (om live-data inte går att läsa)
   - Se DATA_SOURCES.md för fallback-hierarki per datatyp

4. **Modellens generella kunskap** (resonemang + förklaring ENDAST)
   - **ALDRIG** som källa för projektspecifika fakta
   - **KAN** användas för att förklara begrepp, struktur, best practices

---

## ÅTKOMST TILL GITHUB — KRITISK REGEL

**Följ alltid den access- och fallback-strategi som anges i context-repots README.**

**Använd ALDRIG:**
- ❌ `git clone`
- ❌ `git pull`
- ❌ `git fetch`
- ❌ `git ls-remote`
- ❌ Repository-ZIP
- ❌ Python-baserade nätverksanrop (urllib, requests)
- ❌ Shell-kommandon mot GitHub

**Använd ISTÄLLET:**
- ✅ GitHub Connector/API (om tillgänglig)
- ✅ GitHub webåtkomst (via WebFetch eller webbläsare)
- ✅ raw.githubusercontent.com för filer
- ✅ Fallback enligt README

Om en GitHub-källa inte går att läsa ska **fallback-strategin i README följas innan information markeras som ej verifierad.**

---

## TRANSPARENS — KRITISK REGEL

**Säg aldrig att en källa har kontrollerats om den inte faktiskt har lästs inför det aktuella svaret.**

### Om context-repot inte kan läsas:
- Säg det tydligt i början av svaret
- Ange vilka alternativa källor svaret bygger på
- Fortsätt med bästa tillgängliga projektunderlag enligt fallback-strategin

### Om en relevant projektkälla inte kunde verifieras:
- Framgå tydligt att informationen inte kunde verifieras
- Lägg INTE till projektspecifika fakta som inte stöds av de lästa källorna
- Om underlaget inte räcker, säg att informationen inte kunde verifieras

---

## VID NY CHATT

Vid början av en ny chatt eller ny uppgift ska projektkontext läsas på nytt från context-repot.

**Tidigare projektkontext från tidigare chattar får INTE användas som källa.**

Information som uppkommer inom den pågående konversationen får användas tillsammans med aktuell repo-kontext, så länge den inte motsäger en nyare eller mer auktoritativ källa.

---

**Version:** 1.0  
**Skapad:** 2026-09-14  
**Status:** KRITISK INSTRUKTION — Måste följas av alla AI-modeller
