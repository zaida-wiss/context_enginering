---
name: team-roster
description: Authoritative team membership list for presentation coverage validation
metadata:
  type: reference
  critical: true
---

# 👥 TEAM ROSTER — Auktoritativ Personlista

**Denna fil definierar vilka personer som tillhör vilka team. Den är OBLIGATORISK för presentation coverage validation.**

---

## Frontend Team

| GitHub | Namn | Roll | Status |
|--------|------|------|--------|
| tomac | Tomac | Frontend Developer | Active |
| björnb | Björn | Frontend Developer | Active |
| zaida-wiss | Zaida | Frontend Developer | Active |

**Arbetsområden:**
- Frontend & Auth (login, auth flows)
- Frontend & Design System (components, design)
- Frontend & Dashboard (UI, data visualization)

---

## Backend Team

| GitHub | Namn | Roll | Status |
|--------|------|------|--------|
| erik-backend | Erik | Backend Developer | Active |
| rasha-dev | Rasha | Backend Developer | Active |

**Arbetsområden:**
- Backend & Session (API, session management)
- Backend & Risk Calculations (risk engine)
- Backend & Integrations (third-party APIs)

---

## Native/System Team

| GitHub | Namn | Roll | Status |
|--------|------|------|--------|
| pär-native | Pär | Native Developer | Active |
| henrik-system | Henrik | Native Developer | Active |

**Arbetsområden:**
- Native & Risk Motor (JNA, risk calculations)
- Native & App Integration (native modules)
- System & Performance (optimization)

---

## Coverage Validation Rule

**Innan Slide ①A, ①B, ①C kan skapas:**

```
FRONTEND COVERAGE CHECK:
  ☐ Tomac — commits/PRs denna vecka: [ ] found / [ ] not found
  ☐ Björn — commits/PRs denna vecka: [ ] found / [ ] not found
  ☐ Zaida — commits/PRs denna vecka: [ ] found / [ ] not found

BACKEND COVERAGE CHECK:
  ☐ Erik — commits/PRs denna vecka: [ ] found / [ ] not found
  ☐ Rasha — commits/PRs denna vecka: [ ] found / [ ] not found

NATIVE/SYSTEM COVERAGE CHECK:
  ☐ Pär — commits/PRs denna vecka: [ ] found / [ ] not found
  ☐ Henrik — commits/PRs denna vecka: [ ] found / [ ] not found
```

**RULE:** Om någon medlem INTE har verifierbar aktivitet → presentationen måste uttryckligt rapportera det:
- `Tomac — ✅ 4 commits + PR #80 (Frontend)`
- `Björn — ⏳ 3 commits (Design System) + Review PR #90`
- `Zaida — ❌ Ingen aktivitet denna vecka`

**Presentationen får INTE bara utelämna Zaida.** Den måste visa att Zaida inte hade verifierbar GitHub-aktivitet denna vecka.

---

## Why This File Exists

Gamla problemet: Björn's design system arbete försvann från presentationen för att modellen fokuserade på "issues" istället för att systematiskt gå genom alla team-medlemmar.

Denna fil säger: **Dessa 7 personer måste alla kontrolleras innan presentationen är klar.**

| Team | Members |
|------|---------|
| Frontend | Tomac, Björn, Zaida |
| Backend | Erik, Rasha |
| Native/System | Pär, Henrik |

Om någon saknas från presentationen = PROBLEM. Presentationen måste visa varför (aktivitet eller ingen aktivitet denna vecka).

Presentation är INTE komplett utan att alla 7 har blivit kontrollerade.

---

**Senast uppdaterad:** 2026-09-13
