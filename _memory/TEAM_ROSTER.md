---
name: team-roster
description: Authoritative team membership list with VERIFIED GitHub identities (commit-based, not assumed)
metadata:
  type: reference
  critical: true
  verification_method: git_commit_history + github_api
---

# 👥 TEAM ROSTER — Auktoritativ Personlista (VERIFIERAD)

**🚨 VIKTIGT: GitHub-handles är VERIFIERADE från projekt-repot (git commits), inte gissade från personens namn.**

**Denna fil definierar vilka personer som tillhör vilka team. Den är OBLIGATORISK för presentation coverage validation.**

**Verification Status:** Alla handlenamn är baserade på faktiska commits från avanza-team1-repot.

---

## Frontend Team

| Display Name | Verified Email | GitHub Handle | Commit History | Status |
|--------------|----------------|---------------|-----------------|--------|
| Tomac Barin Jansson | tomacbarin@me.com | TomacBarin | ✅ Active | Active |
| Björn Boman | 1125969+bjorneboman@users.noreply.github.com | bjorneboman | ✅ Active | Active |
| Zaida Wiss | zaida.wiss@chasacademy.se | zaida-wiss | ✅ Active | Active |

**Arbetsområden:**
- Frontend & Auth (login, auth flows)
- Frontend & Design System (components, design)
- Frontend & Dashboard (UI, data visualization)

---

## Backend Team

| Display Name | Verified Email | GitHub Handle | Commit History | Status |
|--------------|----------------|---------------|-----------------|--------|
| Erik Berglund | rikexhx@gmail.com | Svartakatten | ✅ Active | Active |
| Rasha Knifdi | rasha.fi@hotmail.com | rashaknifdi | ✅ Active | Active |

**Arbetsområden:**
- Backend & Session (API, session management)
- Backend & Risk Calculations (risk engine)
- Backend & Integrations (third-party APIs)

---

## Native/System Team

| Display Name | Verified Email | GitHub Handle | Commit History | Status |
|--------------|----------------|---------------|-----------------|--------|
| Pär Lundh | lundh.par@gmail.com | lundhpargmailcom | ✅ Active | Active |
| Henrik Westerlund | henrik.w93@gmail.com | Henrik-Westerlund | ✅ Active | Active |

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
