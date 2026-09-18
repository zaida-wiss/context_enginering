#!/usr/bin/env python3
"""
Context workflow smoke tests.

These tests verify that the four main task bundles still load the intended
authorities and preserve the core behavior contracts after repository changes.

This is a contract-level smoke test. It does not replace end-to-end testing with
a real model/tool session.
"""

from pathlib import Path
import sys


def read(path):
    return Path(path).read_text(encoding="utf-8")


def require(label, condition, failures):
    if condition:
        print(f"✅ {label}")
    else:
        print(f"❌ {label}")
        failures.append(label)


def main():
    failures = []

    registry = read("CONTEXT_REGISTRY.yaml")
    router = read("_ai_guides/project/PROJECT_CONTEXT_ROUTER.md")
    dod = read("_ai_guides/project/DEFINITION_OF_DONE.md")
    issue_template = read("_ai_guides/project/templates/ISSUE_BODY.md")
    testing = read("_ai_guides/project/TESTING.md")
    goals = read("_ai_guides/project/GOALS_AND_SPRINT_PLANNING.md")
    risk = read("_ai_guides/project/RISK_MANAGEMENT.md")
    deps = read("_ai_guides/project/DEPENDENCIES_AND_CAPACITY.md")
    cross = read("_ai_guides/project/CROSS_LAYER_AWARENESS.yaml")
    debt = read("_ai_guides/project/TECHNICAL_DEBT.md")
    tone = read("_ai_guides/project/TEAM_TONE_AND_COLLABORATION.yaml")
    slide = read("_ai_guides/presentations/monday_meeting/design/SLIDE_DETAIL_SPEC.md")
    provenance = read("_ai_guides/presentations/design/PROVENANCE_AND_AI_LABELING.md")

    print("=" * 80)
    print("SMOKE TEST 1 — CODING ASSISTANCE")
    print("=" * 80)

    coding_refs = [
        "logical_destinations.project.team_standards",
        "logical_destinations.project.testing",
        "logical_destinations.project.goals_and_sprint_planning",
        "logical_destinations.project.risk_management",
        "logical_destinations.project.dependencies_and_capacity",
        "logical_destinations.project.cross_layer_awareness",
        "logical_destinations.project.technical_debt",
        "logical_destinations.project.team_tone_and_collaboration",
    ]
    require("coding_assistance task exists", "coding_assistance:" in registry, failures)
    for ref in coding_refs:
        require(f"coding bundle loads {ref}", ref in registry, failures)

    require(
        "active relevant branches are part of cross-layer analysis",
        "active work branches" in cross or "active branches" in cross,
        failures,
    )
    require(
        "coding help checks integration context",
        "solve the user's local coding problem" in cross
        and "relevant boundary" in cross,
        failures,
    )
    require(
        "technical debt distinguishes unfinished work",
        "Normal unfinished work" in debt,
        failures,
    )

    print()
    print("=" * 80)
    print("SMOKE TEST 2 — ISSUE CREATION")
    print("=" * 80)

    issue_refs = [
        "logical_destinations.project.testing",
        "logical_destinations.project.definition_of_done",
        "logical_destinations.project.issue_body_template",
        "logical_destinations.project.risk_management",
        "logical_destinations.project.dependencies_and_capacity",
        "logical_destinations.project.cross_layer_awareness",
    ]
    require("issue_creation task exists", "issue_creation:" in registry, failures)
    for ref in issue_refs:
        require(f"issue bundle loads {ref}", ref in registry, failures)

    require(
        "issue template contains Applicable Definition of Done",
        "## Applicable Definition of Done" in issue_template,
        failures,
    )
    require(
        "DoD selection is issue-specific",
        "Issue-specific application" in dod
        and "omit non-applicable criteria" in dod,
        failures,
    )
    require(
        "README criterion is conditional",
        "**README**" in dod
        and "If none of these areas is affected" in dod,
        failures,
    )
    require(
        "router uses current issue_body_template logical ID",
        "project.issue_body_template" in router
        and "project.definition_of_done_template" not in router,
        failures,
    )

    print()
    print("=" * 80)
    print("SMOKE TEST 3 — SPRINT PLANNING")
    print("=" * 80)

    require("sprint_planning task exists", "sprint_planning:" in registry, failures)
    require(
        "planning bundle loads goals authority",
        "logical_destinations.project.goals_and_sprint_planning" in registry,
        failures,
    )
    require(
        "current planning state must be source-backed",
        "does not infer missing cells" in goals
        and "GitHub project evidence" in goals,
        failures,
    )
    require(
        "future state may be proposed explicitly",
        "⭐ AI-förslag" in goals and "Proposal contract" in goals,
        failures,
    )
    require(
        "unknown capacity stays unknown",
        'capacity_state: "unknown"' in deps
        and "Do not assume normal/full availability" in deps,
        failures,
    )
    require(
        "numeric estimates are not invented",
        "does not present an invented hour/day estimate" in deps,
        failures,
    )
    require(
        "risk reasoning uses canonical project workbook method",
        "Identify" in risk and "Assess" in risk and "Mitigate" in risk and "Monitor" in risk,
        failures,
    )

    print()
    print("=" * 80)
    print("SMOKE TEST 4 — MONDAY MEETING PRESENTATION")
    print("=" * 80)

    presentation_refs = [
        "planning_authority:",
        "risk_authority:",
        "dependency_capacity_authority:",
        "cross_layer_authority:",
        "technical_debt_authority:",
    ]
    require(
        "monday_meeting_presentation task exists",
        "monday_meeting_presentation:" in registry,
        failures,
    )
    for ref in presentation_refs:
        require(f"presentation bundle contains {ref}", ref in registry, failures)

    require(
        "meeting point 9 uses vertical priority model",
        'Meeting point 9 is **not** a four-column team board' in slide
        and "vertically stacked" in slide,
        failures,
    )
    require(
        "old mandatory four-column point-9 rule is gone",
        "Every physical slide for point 9 MUST use these columns" not in slide,
        failures,
    )
    require(
        "four-team perspective is preserved as coverage, not layout",
        "Four-perspective planning coverage" in slide
        and "coverage requirement" in slide,
        failures,
    )
    require(
        "AI no-finding checks expose exact inspected sources",
        "AI CHECK TRACE — EXACT SOURCES CHECKED" in provenance
        and "actual places inspected" in provenance,
        failures,
    )
    require(
        "analysis and proposals remain distinct",
        "🔎 AI-analys" in provenance and "⭐ AI-förslag" in provenance,
        failures,
    )

    print()
    print("=" * 80)
    if failures:
        print(f"❌ SMOKE TEST FAILED — {len(failures)} checks failed")
        for failure in failures:
            print(f"  - {failure}")
        return 1

    print("✅ ALL FOUR CONTEXT WORKFLOW SMOKE TESTS PASS")
    print("STATUS: READY FOR END-TO-END FRESH-CHAT TESTS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
