---
name: github_snapshot
description: Cached snapshot of GitHub live data (commits, issues, PRs, branches) — fallback when live access fails
metadata:
  type: reference
  updated: 2026-09-13
  source: "https://github.com/chas-challenge-2026/avanza-team1"
---

# GitHub Snapshot — Live Data Cache

**⚠️ DENNA FIL ÄR EN FALLBACK ENDAST**

Använd denna ENDAST om:
1. GitHub Connector/API misslyckas, OCH
2. Direkt GitHub-webåtkomst misslyckas

Om båda live-metoderna fungerar → använd live-data, INTE denna snapshot.

---

## Metadata

- **Repository:** https://github.com/chas-challenge-2026/avanza-team1
- **Branch:** develop
- **Snapshot Date:** 2026-09-13 12:45 UTC
- **Updated By:** [Vem/Process]
- **Next Update Due:** 2026-09-17

---

## Commits Denna Vecka

> Commits sedan förra sprintmöte (föregående tisdag)

```
2026-09-13 abc1234 "Add refresh token endpoint for auth flow" — Erik
2026-09-12 def5678 "Portfolio responsive layout — mobile first" — Zaida
2026-09-12 ghi9012 "Fix portfolio calculation bugs" — Anna
2026-09-11 jkl3456 "Update API documentation" — Marco
```

---

## Open Issues

> Status denna vecka

| # | Titel | Team | Assignee | Status |
|---|-------|------|----------|--------|
| #40 | Frontend auth flow integration | Frontend | Lisa | In Progress |
| #41 | Backend JWT refresh endpoint | Backend | Marco | In Progress |
| #42 | Native error handling screen | Native | Kris | Ready |
| #45 | FX calculation service | Backend | Marco | Backlog |
| #46 | Responsive portfolio view | Frontend | Unassigned | Backlog |
| #52 | Unit tests for calculations | Backend | Anna | Ready |

---

## Recent Pull Requests

| # | Titel | Status | Branch | Author |
|---|-------|--------|--------|--------|
| #88 | Add JWT refresh flow | Review | feature/auth-refresh | Erik |
| #90 | Frontend #40 auth integration | Merged | feature/frontend-auth | Lisa |
| #92 | Native error handling | Merged | feature/native-errors | Kris |

---

## Active Branches

```
main                          (production)
develop                       (base)
feature/auth-refresh          (Erik — PR #88)
feature/responsive-dashboard  (Zaida — WIP)
feature/fx-calculator         (Marco — development)
feature/native-errors         (Kris — merged to develop)
```

---

## Team Status (Inferred from Issues)

| Team | In Progress | Ready | Backlog | Blocked |
|------|-------------|-------|---------|---------|
| Frontend | #40 (Lisa) | — | #46 | — |
| Backend | #41 (Marco) | #52 (Anna) | #45 | — |
| Native | — | #42 (Kris) | — | — |

---

## Notes

- Snapshot captured at regular meeting time
- Git log covers one week (Mon-Fri)
- Issues reflect last known state before API failure
- For real-time updates: use GitHub Connector or direct GitHub access

