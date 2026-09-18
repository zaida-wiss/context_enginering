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
    ai_framework = read("_ai_guides/AI_FRAMEWORK.md")
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
    render_gate = read("_ai_guides/presentations/verification/RENDER_GATE_CHECKLIST.md")
    system_contract = read("_ai_guides/presentations/SYSTEM_CONTRACT.yaml")
    authority_registry = read("_ai_guides/presentations/AUTHORITY_REGISTRY.yaml")
    sources = read("data/SOURCES.yaml")

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
    require(
        "global AI framework is registered",
        "logical_destinations:" in registry
        and "ai_framework:" in registry
        and "_ai_guides/AI_FRAMEWORK.md" in registry,
        failures,
    )
    require(
        "global conflict gate requires user decision before resolution",
        "CONFLICT DECISION GATE — USER DECIDES" in ai_framework
        and "STOP before resolving" in ai_framework
        and "Ask the user for the intended decision" in ai_framework
        and "Wait for that decision" in ai_framework,
        failures,
    )
    require(
        "context-first correction is global",
        "CONTEXT-FIRST CORRECTION" in ai_framework
        and "update the context repository first" in ai_framework,
        failures,
    )
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
    require(
        "conditional Sprintplanering source is registered",
        "GOOGLE_SPRINT_PLANNING:" in sources
        and 'worksheet_title: "Sprintplanering"' in sources
        and "UNAVAILABLE_NOT_YET_CREATED" in sources,
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
        "authority conflicts require an explicit user decision",
        "conflict_decision_gate:" in system_contract
        and "ask the user for a decision" in system_contract
        and "ask the user to" in authority_registry.lower(),
        failures,
    )

    require(
        "meeting point 9 uses shared card grid",
        "shared responsive card/grid system" in slide
        and "2×2 grid is allowed" in slide,
        failures,
    )
    require(
        "old mandatory four-column point-9 rule is gone",
        "Every physical slide for point 9 MUST use these columns" not in slide,
        failures,
    )
    require(
        "render gate validates shared point-9 grid",
        "POINT 9 — SHARED CARD/GRID PRIORITY VIEW" in render_gate
        and "point9_shared_grid_missing_count == 0" in render_gate,
        failures,
    )
    require(
        "rendered meeting-point numbering follows user decision",
        "✏️ 1. Avklarat sedan förra mötet" in slide
        and "rendered_circled_meeting_point_number_count == 0" in render_gate,
        failures,
    )
    require(
        "shared card grid follows user decision",
        "shared responsive card/grid system" in slide
        and "SHARED CARD/GRID RULE" in read("_ai_guides/presentations/monday_meeting/design/LAYOUT_OVERFLOW_GUARD.md"),
        failures,
    )

    require(
        "team identity uses context-aware non-color cues",
        "dedicated team slide" in read("_ai_guides/presentations/design/CARD_COMPONENT_STANDARD.md").lower()
        and "mixed-team slides" in read("_ai_guides/presentations/design/CARD_COMPONENT_STANDARD.md").lower()
        and "mixed_team_card_color_only_identity_count == 0" in render_gate
        and "dedicated_team_slide_missing_text_team_context_count == 0" in render_gate,
        failures,
    )

    require(
        "NPF five-second scan gate is active",
        "Five-second scan test" in read("_ai_guides/presentations/design/VISUAL_DESIGN_MANDATORY.md")
        and "five_second_scan_failure_count == 0" in render_gate,
        failures,
    )
    require(
        "stable slide zones are an active design contract",
        "Stable slide zones" in read("_ai_guides/presentations/design/VISUAL_DESIGN_MANDATORY.md")
        and "slide_zone_predictability_failure_count == 0" in render_gate,
        failures,
    )

    require(
        "cover validator requires PL target/time/purpose",
        "pl_meeting_card_missing_target_time_purpose_count == 0" in render_gate
        and "cover_generic_status_displacing_required_content_count == 0" in render_gate,
        failures,
    )
    require(
        "point 1 validator forbids separate WIP slide",
        "point_1_separate_wip_slide_count == 0" in render_gate
        and "physical point-1 slide/subsection titled `Påbörjat men inte avklarat` is forbidden" in render_gate,
        failures,
    )
    require(
        "meeting numbers use ordinary Arabic rendering",
        "rendered_circled_meeting_point_number_count == 0" in render_gate
        and "ordinary Arabic number with period" in render_gate,
        failures,
    )
    require(
        "collection branch validation distinguishes merge from direct activity",
        "point_1_verified_collection_merge_without_own_slide_count == 0" in render_gate
        and "ordinary direct commits/branch activity are not relabeled as merges" in render_gate,
        failures,
    )
    require(
        "point 9 validates shared grid geometry",
        "point9_shared_grid_missing_count == 0" in render_gate
        and "a readable 2×2 grid is allowed" in render_gate,
        failures,
    )
    require(
        "capacity slide hides personal reasons and AI meta policy",
        "capacity_personal_reason_exposed_count == 0" in render_gate
        and "capacity_internal_ai_policy_visible_count == 0" in render_gate,
        failures,
    )
    require(
        "AI no-finding trace requires exact checked sources",
        "ai_no_finding_without_exact_checked_sources_count == 0" in render_gate
        and "actual places inspected" in provenance,
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
