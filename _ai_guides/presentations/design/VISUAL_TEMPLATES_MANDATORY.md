---
name: visual_templates_mandatory
description: MANDATORY — Concrete visual templates for slides ③-⑦ (team status, blockers, risks)
metadata:
  type: reference
  critical: true
---

# 🎨 VISUAL TEMPLATES — Slides ③-⑦ (OBLIGATORISKA)

**🚨 DESSA TEMPLATES MÅSTE FÖLJAS. Ingen presentation utan dessa visuella format.**

---

## 📝③④⑤ TEAM STATUS — Issue Tabell

### Slide ③-⑤A: Var är vi? (Issue-status tabell)

**OBLIGATORISK STRUKTUR:**

```
Område | Verifierat | Ägare | AC | Tests | Review | Docs | Status
-------|-----------|-------|-----|-------|--------|------|--------
#42 | PR #79 m. | Erik | ✅ | ◐ | ✅ | ✕ | 🟢 Klar
#43 | PR #80 o. | Zaida | ✅ | ✅ | ✕ | ? | 🟡 Rev.
#44 | PR #81 m. | Rasha | ✅ | ✓ | ✅ | ✅ | 🟢 Klar
#45 | Open PR   | Björn | ◐ | ✕ | ? | ✕ | 🟡 Pgår
```

**Färg per status-kolumn:**
- 🟢 Grön bakgrund = ✅ AC + ✅ Tests + ✅ Review + ✅ Docs (READY)
- 🟡 Orange bakgrund = någon DoD-punkt ej klar
- 🔴 Röd bakgrund = blockerad/kritisk

**Font-size:** 12-13pt (läsbar från mötesbord)
**Radhöjd:** Minst 20px

---

## 📝⑥ BLOCKERS — Dependency Diagram

### Obligatorisk visuell format

**Visuell blockeringskedja som diagram:**

```
┌─────────────┐       ┌─────────────┐
│  FRONTEND   │       │   BACKEND   │
│  #42 Login  │       │  #55 Auth   │
│  🟡 Väntar  │  ──→  │  🔴 Blockad │
│  på Backend │       │             │
└─────────────┘       └─────────────┘

┌─────────────┐
│   NATIVE    │
│  #61 FX     │
│  🟡 Pgår    │
│  (unblocked)│
└─────────────┘

LEGEND:
  ──→ = waiting for (väntar på)
  🟡 = in progress (pågår)
  🔴 = blocked (blockerad)
  ⚪ = on track (på rätt väg)
```

**Regler:**
- Använd BOXAR för team/issue
- Använd PILAR för beroenden
- Färg-kod: 🟡 (pågår), 🔴 (blockerad), ⚪ (på rätt väg)
- Labels på pilar: "waiting for", "blocks", "depends on"
- Konkret information: vad blockerar, när lösning förväntas

**Font-size:** 11-12pt på labels
**Pilstorlek:** 2-3px (synlig men inte överväldigande)

---

## 📝⑦ RISK MATRIX — 3x3 Risk Assessment

### Obligatorisk visuell format

**Risk matrix med färgkodning:**

```
                Låg Konsekvens    Medel Konsekvens    Hög Konsekvens
            ┌──────────────┬──────────────┬──────────────┐
Låg Risk    │     🟢       │      🟡      │      🟡      │
            │   Acceptabel │   Monitora   │  Planera     │
            ├──────────────┼──────────────┼──────────────┤
Medel Risk  │     🟡       │      🟡      │      🔴      │
            │   Monitora   │  Planera     │  Åtgärd nu   │
            ├──────────────┼──────────────┼──────────────┤
Hög Risk    │     🟡       │      🔴      │      🔴      │
            │   Planera    │  Åtgärd nu   │  Kritisk     │
            └──────────────┴──────────────┴──────────────┘

Förklaring under:
  🟢 = Acceptabel risk (monitora endast)
  🟡 = Behöver åtgärd eller planering
  🔴 = Måste åtgärdas OMEDELBAR
```

**Vad som går i varje cell:**
- Risk-namn (t.ex. "Databaskrash")
- Sannolikhet: 1/10 (låg), 5/10 (medel), 9/10 (hög)
- Konsekvens: låg (delay), medel (feature miss), hög (kund-pej)
- Åtgärd: vad gör vi?
- Ansvar: vem äger det?
- Tidslinje: när löst?

**Font-size:** 11-12pt (läsbar i cell)
**Cell-storlek:** Minst 60x60px (luftig layout)
**Färg:** 🟢 grön (RGB 76, 175, 80), 🟡 orange (RGB 255, 152, 0), 🔴 röd (RGB 244, 67, 54)

---

## ✅ BEFORE RENDERING — VISUELL TEMPLATE CHECKLIST

```
Slide ③-⑤A (Team Status Table):
  ☐ Tabell har alla kolumner (Område, Verifierat, Ägare, AC, Tests, Review, Docs, Status)
  ☐ Status-kolumn har rätt färg (🟢/🟡/🔴)
  ☐ Font-size minst 13pt
  ☐ Radhöjd minst 20px
  ☐ Headers marinblå bakgrund + vit text

Slide ⑥ (Blockers Diagram):
  ☐ Diagram visat (INTE bara text-lista)
  ☐ Boxar för team/issue
  ☐ Pilar visar relationer
  ☐ Färg-kodning (🟡/🔴/⚪)
  ☐ Labels på pilar

Slide ⑦ (Risk Matrix):
  ☐ 3x3 matrix visat (INTE bara tabell)
  ☐ Färg-kodning (🟢/🟡/🔴)
  ☐ Förklaring under matrix
  ☐ Font-size 11-12pt
  ☐ Cell-storlek minst 60x60px
```

---

**Version:** 1.0  
**Senast uppdaterad:** 2026-09-13  
**Status:** MANDATORY — Ingen presentation utan dessa templates
