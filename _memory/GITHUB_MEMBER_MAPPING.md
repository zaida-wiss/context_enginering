---
name: github_member_mapping
description: Maps Team Avanza members to their GitHub usernames for activity tracking
metadata:
  type: reference
  updated: 2026-09-15
---

# GitHub Member Mapping

Maps team member names to GitHub usernames for commit/PR/issue tracking.

**VERIFIED 2026-09-16 — All usernames confirmed against GitHub activity data.**

| Team | Team Member | GitHub Username | Verified | Notes |
|---|---|---|---|---|
| Frontend | Zaida Wiss | zaida-wiss | ✅ | Display name: "Zaida Wiss" |
| Frontend | Tomac Barin Jansson | TomacBarin | ✅ | Display name: "Tomac Barin Jansson" |
| Frontend | Björn Boman | bjorneboman | ✅ | Display name: "Björn Boman" |
| Backend | Rasha Knifdi | rashaknifdi | ✅ | Display name: "rashaknifdi" |
| Backend | Erik Berglund | Svartakatten | ✅ | Display name: "Erik Berglund" |
| Native | Henrik Westerlund | Henrik-Westerlund | ✅ | Display name: "Henrik Westerlund" |
| Native | Pär Lundh | lundhpargmailcom | ✅ | Display name: "lundhpargmailcom" (email-based username) |
| External | Max Guclu | Max-comerit | ✅ | External contributor (Comerit) |

**Usage:** Use this mapping to:
- Query GitHub API per person: `/search/issues?q=assignee:[username]` or `/search/issues?q=author:[username]`
- Attribute issues/PRs/commits to correct team member
- Ensure ALL 7 team members appear in presentations (even with zero activity)
- Display both display_name and @github_username in presentations for full traceability
