# Issue Table Format

When requesting a new issue in Claude Code, AI generates it as a **structured markdown table** with standardized columns.

## Table Structure

| Column | Purpose |
|--------|---------|
| **Title** | Short, action-oriented title |
| **Body** | Full issue description following template standards |
| **Assignees** | Team member (or empty) |
| **Status** | Todo / In Progress / Review / Done |
| **Priority** | High / Medium / Low |
| **Labels** | Issue type tags (e.g., bug, feature, docs) |
| **Estimate** | Story points or time estimate |

## Body Content Requirements

The **Body** field must include:

1. **Context** — Why does this feature/fix exist? What problem does it solve?
2. **Acceptance Criteria** — Specific, testable outcomes (not vague descriptions)
   - Example: "User enters email + password → sees loading → redirects to /portfolio"
3. **Technical Decisions** — Key architectural choices
   - Which state management? Local vs centralized?
   - Who owns validation? Component vs module?
   - How are success/failure cases handled?
4. **Dependencies** — What other work must complete first? External modules?
5. **Design/UX** — Visual requirements, error states, loading states (if applicable)

## Example Table

| Column | Content |
|--------|---------|
| **Title** | Fix login redirect routing |
| **Body** | **Context:** Users cannot reach portfolio after successful login due to route mismatch.<br/><br/>**Acceptance Criteria:** User enters credentials → loading displays → redirects to `/portfolio` successfully<br/><br/>**Technical Decisions:** Route in App.tsx, Router component handles navigation<br/><br/>**Dependencies:** Auth module must be complete (Issue #42)<br/><br/>**Design/UX:** Loading spinner during redirect, error toast if redirect fails |
| **Assignees** | alice |
| **Status** | Todo |
| **Priority** | High |
| **Labels** | bug, routing, critical |
| **Estimate** | 2 pts |

## How This Helps

- **Clarity:** All required details in one place
- **Prevents bugs:** Forces critical thinking before implementation (catches routing mismatches, missing validation, etc.)
- **AI review:** Template completeness enables AI to catch issues like unused imports, wrong dependencies
- **Consistency:** All issues follow the same structure

## How to Use

1. Ask Claude: "Create an issue about [your request]"
2. Claude generates the markdown table
3. Review the table content
4. Copy the table to GitHub or your project board
5. Move to Status: "In Progress" when work starts

---

**Status:** ACTIVE  
**Last updated:** 2026-10-01
