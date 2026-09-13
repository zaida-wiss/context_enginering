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
| zaida-wiss | Zaida | Frontend Developer | Active |
| janstrom | Jan | Frontend Developer | Active |
| marcodev | Marco | Frontend Developer | Active |

**Arbetsområden:**
- Frontend – Auth & Login
- Frontend – Dashboard & UI
- Frontend – Design System & Components

---

## Backend Team

| GitHub | Namn | Roll | Status |
|--------|------|------|--------|
| anna-backend | Anna | Backend Developer | Active |
| kiran-dev | Kiran | Backend Developer | Active |
| tomac | Tomac | Backend Developer | Active |

**Arbetsområden:**
- Backend – API & Integration
- Backend – Risk Calculations
- Backend – FX & Portfolio Logic

---

## System/Native Team

| GitHub | Namn | Roll | Status |
|--------|------|------|--------|
| björnb | Björn | System/Native Developer | Active |
| sam-native | Sam | System/Native Developer | Active |

**Arbetsområden:**
- System/Native – Risk Motor
- System/Native – Native App
- System/Native – JNA Integration

---

## Coverage Validation Rule

**Innan Slide ①A och ①B kan skapas:**

```
FRONTEND COVERAGE CHECK:
  ☐ Zaida — commits/PRs denna vecka: [ ] found / [ ] not found
  ☐ Jan — commits/PRs denna vecka: [ ] found / [ ] not found
  ☐ Marco — commits/PRs denna vecka: [ ] found / [ ] not found

BACKEND COVERAGE CHECK:
  ☐ Anna — commits/PRs denna vecka: [ ] found / [ ] not found
  ☐ Kiran — commits/PRs denna vecka: [ ] found / [ ] not found
  ☐ Tomac — commits/PRs denna vecka: [ ] found / [ ] not found

SYSTEM/NATIVE COVERAGE CHECK:
  ☐ Björn — commits/PRs denna vecka: [ ] found / [ ] not found
  ☐ Sam — commits/PRs denna vecka: [ ] found / [ ] not found
```

**RULE:** Om någon medlem INTE har verifierbar aktivitet → presentationen måste uttryckligt rapportera det:
- `Zaida — ✅ 4 commits + PR #90 (Login) + PR #91 (Auth)`
- `Jan — ⏳ 3 commits (Dashboard) + PR #92 (mockdata)`
- `Marco — ❌ Ingen aktivitet denna vecka`

**Presentationen får INTE bara utelämna Marco.** Den måste visa att Marco inte hade verifierbar GitHub-aktivitet denna vecka.

---

## Why This File Exists

Gamla problemet: Björn's design system arbete försvann från presentationen för att modellen fokuserade på "issues" istället för att systematiskt gå genom alla team-medlemmar.

Denna fil säger: **Dessa 8 personer måste alla kontrolleras innan presentationen är klar.**

Om Björn saknas från presentationen = PROBLEM. Presentationen är inte komplett.

---

**Senast uppdaterad:** 2026-09-13
