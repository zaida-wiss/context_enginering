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


def yaml_scalar(content, *path):
    """Read a scalar from the repository's simple YAML contracts without external dependencies."""
    stack = []
    for raw in content.splitlines():
        if not raw.strip() or raw.lstrip().startswith("#") or raw.strip() == "---":
            continue
        if raw.lstrip().startswith("- "):
            continue

        indent = len(raw) - len(raw.lstrip(" "))
        stripped = raw.strip()
        if ":" not in stripped:
            continue

        key, value = stripped.split(":", 1)
        key = key.strip()
        value = value.strip()

        while stack and stack[-1][0] >= indent:
            stack.pop()

        current_path = tuple(item[1] for item in stack) + (key,)

        if value == "":
            stack.append((indent, key))
            continue

        if current_path == tuple(path):
            lowered = value.lower()
            if lowered == "true":
                return True
            if lowered == "false":
                return False
            return value.strip('"').strip("'")

    return None


def require(label, condition, failures):
    if condition:
        print(f"✅ {label}")
    else:
        print(f"❌ {label}")
        failures.append(label)


def main():
    failures = []

    registry = read("CONTEXT_REGISTRY.yaml")
    ai_framework = read("_ai_guides/AI_FRAMEWORK.yaml")
    ai_framework_guide = read("_ai_guides/AI_FRAMEWORK.md")
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
    design_authority = read("_ai_guides/presentations/design/DESIGN_AUTHORITY.md")
    presentation_architecture = read("_ai_guides/presentations/ARCHITECTURE.md")
    composition = read("_ai_guides/presentations/monday_meeting/structure/COMPOSITION_ARCHITECTURE.md")

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
        "global AI framework YAML is registered",
        "logical_destinations:" in registry
        and "ai_framework:" in registry
        and "_ai_guides/AI_FRAMEWORK.yaml" in registry,
        failures,
    )
    require(
        "global AI framework YAML is normative",
        yaml_scalar(ai_framework, "metadata", "normative") is True
        and yaml_scalar(ai_framework, "metadata", "critical") is True
        and yaml_scalar(ai_framework, "metadata", "status") == "active",
        failures,
    )
    require(
        "global conflict gate requires STOP and user decision",
        yaml_scalar(ai_framework, "conflict_decision_gate", "action") == "STOP"
        and yaml_scalar(ai_framework, "conflict_decision_gate", "user_decision_required") is True,
        failures,
    )
    require(
        "authority rank cannot silently resolve a genuine conflict",
        yaml_scalar(
            ai_framework,
            "authority_order",
            "may_silently_resolve_genuine_internal_conflict",
        ) is False,
        failures,
    )
    require(
        "context-first correction is machine-readable",
        yaml_scalar(
            ai_framework,
            "context_first_correction",
            "artifact_only_patch_is_final_fix",
        ) is False,
        failures,
    )
    require(
        "Markdown framework is explanatory only",
        "normative: false" in ai_framework_guide
        and "Normative source:" in ai_framework_guide
        and "AI_FRAMEWORK.yaml" in ai_framework_guide,
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
        "router delegates canonical task paths to the context registry",
        "Canonical task routing" in router
        and "CONTEXT_REGISTRY.yaml" in router
        and "project.definition_of_done_template" not in router,
        failures,
    )

    print()
    print("=" * 80)
    print("SMOKE TEST 3 — SPRINT PLANNING")
    print("=" * 80)

    require("sprint_planning task exists", "sprint_planning:" in registry, failures)
    require(
        "sprint planning loads global AI framework",
        'sprint_planning:' in registry
        and '"logical_destinations.global.ai_framework"' in registry,
        failures,
    )
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
    require(
        "presentation task loads global AI framework",
        "global_framework:" in registry
        and 'ref: "logical_destinations.global.ai_framework"' in registry,
        failures,
    )
    for ref in presentation_refs:
        require(f"presentation bundle contains {ref}", ref in registry, failures)

    require(
        "presentation bootstrap loads global AI framework first",
        'file: "../AI_FRAMEWORK.yaml"' in system_contract
        and 'required_before_presentation_authorities: true' in system_contract
        and "../AI_FRAMEWORK.yaml" in read("_ai_guides/presentations/MANDATORY_READING_ORDER.md"),
        failures,
    )

    require(
        "presentation authority rank is ownership-only",
        "AUTHORITY OWNERSHIP ORDER" in design_authority
        and "Do **not** use it to silently resolve a genuine contradiction" in design_authority
        and "ask the user to decide" in design_authority,
        failures,
    )
    require(
        "composition authority is present in all presentation authority maps",
        "COMPOSITION_ARCHITECTURE.md" in design_authority
        and "LEVEL 9 — COMPOSITION_ARCHITECTURE.md" in presentation_architecture
        and "monday_meeting/structure/COMPOSITION_ARCHITECTURE.md" in system_contract
        and "monday_meeting/structure/COMPOSITION_ARCHITECTURE.md" in authority_registry,
        failures,
    )

    require(
        "presentation architecture delegates genuine conflicts to global framework",
        "AUTHORITY OWNERSHIP HIERARCHY" in presentation_architecture
        and "AI_FRAMEWORK.yaml" in presentation_architecture
        and "never by rank alone" in presentation_architecture,
        failures,
    )

    require(
        "authority conflicts require an explicit user decision",
        "conflict_decision_gate:" in system_contract
        and "ask the user for a decision" in system_contract.lower()
        and "ask the user to" in authority_registry.lower(),
        failures,
    )

    require(
        "system maintenance treats authority order as ownership only",
        "authority_ownership:" in system_contract
        and "must never be" in system_contract
        and "ask the user for an explicit decision" in system_contract.lower()
        and "conflict_resolution:" not in system_contract,
        failures,
    )

    require(
        "NPF and visual rules recognize registered point9 exception",
        "meeting point 9 priority uses its registered vertical execution-group exception" in read("_ai_guides/presentations/design/VISUAL_DESIGN_MANDATORY.md")
        and "meeting point 9's" in read("_ai_guides/presentations/design/ACCESSIBILITY_NEURODIVERSITY.md")
        and "vertical execution sequence is such an exception" in read("_ai_guides/presentations/design/ACCESSIBILITY_NEURODIVERSITY.md"),
        failures,
    )

    require(
        "composition authority registers vertical point9 exception",
        "Registered slide-level exception:" in read("_ai_guides/presentations/monday_meeting/structure/COMPOSITION_ARCHITECTURE.md")
        and "point9_vertical_sequence_missing_count == 0" in read("_ai_guides/presentations/monday_meeting/structure/COMPOSITION_ARCHITECTURE.md")
        and "`⑨` | vertical execution groups" in read("_ai_guides/presentations/monday_meeting/design/LAYOUT_OVERFLOW_GUARD.md"),
        failures,
    )

    require(
        "meeting point 9 uses mandatory vertical execution sequence",
        "mandatory vertical execution sequence" in slide
        and "2×2 execution-group layout" in slide,
        failures,
    )
    require(
        "old mandatory four-column point-9 rule is gone",
        "Every physical slide for point 9 MUST use these columns" not in slide,
        failures,
    )
    require(
        "render gate validates vertical point-9 layout",
        "POINT 9 — VERTICAL PRIORITY VIEW" in render_gate
        and "point9_vertical_sequence_missing_count == 0" in render_gate
        and "point9_side_by_side_group_count == 0" in render_gate,
        failures,
    )
    require(
        "rendered meeting-point numbering follows user decision",
        "✏️ 1. Avklarat sedan förra mötet" in slide
        and "rendered_circled_meeting_point_number_count == 0" in render_gate,
        failures,
    )
    require(
        "shared card system allows registered vertical point9 exception",
        "mandatory vertical execution sequence" in slide
        and "Registered exception:" in read("_ai_guides/presentations/monday_meeting/design/LAYOUT_OVERFLOW_GUARD.md"),
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
        "presentation typography keeps one primary font family",
        "One primary font family per deck" in read("_ai_guides/presentations/design/VISUAL_DESIGN_MANDATORY.md")
        and "inconsistent_primary_font_family_count == 0" in render_gate,
        failures,
    )
    require(
        "obsolete native editable/selectable text rule is absent",
        "editable_text:" not in system_contract
        and "native editable/selectable" not in system_contract
        and "required_text_rasterized_count == 0" not in render_gate,
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
        "point 1 semantic subsections do not depend on legacy fixed letters",
        "Decisions summarized in ①d" not in slide
        and "Teamsammanfattning" in composition
        and "{PRIMARY_INTEGRATION_BRANCH} → {REGISTERED_COLLECTION_BRANCHES_IN_PROJECT_ORDER} → Teamsammanfattning" in composition
        and "①d" not in composition,
        failures,
    )

    require(
        "team accent validator cannot imply color-only identity",
        "team_accent_uses_left_edge_not_full_outline == true" in read("_ai_guides/presentations/design/CARD_COMPONENT_STANDARD.md")
        and "team_color_left_accent_only == true" not in read("_ai_guides/presentations/design/CARD_COMPONENT_STANDARD.md"),
        failures,
    )
    require(
        "collection branches are loaded dynamically from registered project data",
        "Load collection branches dynamically" in read("_ai_guides/presentations/data/DATA_ACQUISITION_CONTRACT.yaml")
        and "do not hard-code team names or branch names in this framework" in read("_ai_guides/presentations/data/DATA_ACQUISITION_CONTRACT.yaml"),
        failures,
    )

    require(
        "active-work acquisition does not route WIP into point 1",
        "required for ①D–①E slides" not in read("_ai_guides/presentations/data/DATA_ACQUISITION_CONTRACT.yaml")
        and "for ①D–①E slides" not in read("_ai_guides/presentations/data/DATA_ACQUISITION_CONTRACT.yaml")
        and "slides ①D–①E" not in read("_ai_guides/presentations/data/DATA_ACQUISITION_CONTRACT.yaml"),
        failures,
    )
    require(
        "point 1 continuation letters do not define subsection meaning",
        "point-1 subsection meaning comes from its canonical subtitle/verified merge target" in read("_ai_guides/presentations/design/VISUAL_DESIGN_MANDATORY.md")
        and "meeting point 1 + any continuation pages" in read("_ai_guides/presentations/monday_meeting/design/LAYOUT_OVERFLOW_GUARD.md"),
        failures,
    )

    require(
        "point 1 follows registered integration and collection-branch order",
        "{PRIMARY_INTEGRATION_BRANCH}" in composition
        and "{REGISTERED_COLLECTION_BRANCHES_IN_PROJECT_ORDER}" in composition
        and "Teamsammanfattning" in composition
        and "separate WIP/unfinished-work slide" in presentation_architecture,
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
        "point 9 validates actual vertical geometry",
        "point9_vertical_sequence_missing_count == 0" in render_gate
        and "point9_group_vertical_order_violation_count == 0" in render_gate
        and "point9_side_by_side_group_count == 0" in render_gate,
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
