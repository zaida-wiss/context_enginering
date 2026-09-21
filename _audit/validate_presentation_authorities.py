#!/usr/bin/env python3
"""Fail when the presentation authority model becomes ambiguous."""

from __future__ import annotations

from pathlib import Path
import re
import sys

import yaml


ROOT = Path(__file__).resolve().parents[1]
PRESENTATIONS = ROOT / "_ai_guides" / "presentations"
REGISTRY = PRESENTATIONS / "AUTHORITY_REGISTRY.yaml"
PROJECT_REGISTRY = ROOT / "PROJECTS.yaml"

STALE_ACTIVE_PATTERNS = {
    "legacy AI suggestion symbol": "? AI-förslag",
    "legacy AI analysis symbol": "? AI-analys",
    "old Frontend meeting point": "📝④ Frontend",
    "old Backend meeting point": "📝⑤ Backend",
    "old Native meeting point": "📝⑥ Native",
    "old team range": "④–⑥",
    "obsolete workflow columns": "Arbete | Läge | Härnäst | Vem",
    "stale 10 pt provenance footer minimum": "footer uses priority level 4 but must remain at least 10 pt",
    "stale critical-data continue rule": "mark as INCOMPLETE, but continue with available data",
    "retired solid presentation background": "slide background is `#0F1830`",
}


REFERENCE_REQUIRED_PATTERNS = {
    "monday_meeting/design/TEMPLATE_REFERENCE.html": (
        "linear-gradient(145deg, #1E274A 0%, #111A33 100%)",
        "grid-template-columns: repeat(3, minmax(0,1fr))",
        "font-size: 48px",
        "font-size: 32px",
        "✏️ 1. Avklarat sedan förra mötet",
        "Mergat till develop",
    ),
}

REFERENCE_STALE_PATTERNS = {
    "monday_meeting/design/TEMPLATE_REFERENCE.html": (
        "background: #0F1830",
        ".grid { display: grid; grid-template-columns: repeat(2, minmax(0,1fr));",
        "<h1>①",
        "Leverans: <strong>direkt commit</strong>",
    ),
}

PROJECT_PRESENTATION_STALE_PATTERNS = {
    "retired Avanza solid canvas": "#15182E",
}

REQUIRED_ACTIVE_PATTERNS = {
    "INTEGRITY_CONSTRAINT.md": (
        "pause and ask the user whether to continue without the named source",
        "PASS_WITH_USER_OVERRIDE",
    ),
    "../../data/SOURCES.yaml": (
        "PAUSE, report INCOMPLETE, name the source and ask whether to continue without it",
    ),
    "data/DATA_ACQUISITION_CONTRACT.yaml": (
        "PAUSE BEFORE RENDERING if any dataset classified REQUIRED or CRITICAL is INCOMPLETE",
        "continue_without_source",
        "PASS_WITH_USER_OVERRIDE",
        "Follow source/API pagination until ALL relevant commits",
        "Use accessible continuation slides when needed",
        "trigger the explicit incomplete-source user decision gate",
        "ordinary_direct_commit",
        "Only merge_event records are eligible for",
        "ordinary_direct_commit feeds points 3–5 planning/status",
    ),
    "design/READABILITY_HARD_RULES.md": (
        "timestamp/source/provenance/footer microcopy: **11 pt minimum**",
        "title → pedagogical explanation: **6 px minimum**, **8 px preferred**",
        "explanation → assignee/developer: **14 px minimum**",
    ),
    "design/CARD_COMPONENT_STANDARD.md": (
        "title → pedagogical explanation: **6 px minimum, 8 px preferred**",
        "explanation → bottom identity zone: **14 px minimum**",
        "inline provenance symbols stay with their factual content blocks",
        "full source names/explanations belong in the slide source margin/footer",
    ),
    "monday_meeting/design/LAYOUT_OVERFLOW_GUARD.md": (
        "title → pedagogical explanation: **6 px minimum, 8 px preferred**",
        "explanation → assignee/developer: **14 px minimum**",
    ),
    "design/PROVENANCE_AND_AI_LABELING.md": (
        "rendered_missing_glyph_count == 0",
        "minimum provenance/source text size in this deck: **11 pt**",
        "footer uses priority level 4 but must remain at least 11 pt",
        "MIXED CARDS — SYMBOL IN BLOCK, FULL LABEL AT BOTTOM",
        "card_bottom_provenance_symbol_text_mismatch_count == 0",
    ),
    "verification/RENDER_GATE_CHECKLIST.md": (
        "canonical_symbol_render_mismatch_count == 0",
        "content_block_provenance_symbol_missing_count == 0",
        "card_bottom_provenance_full_label_missing_count == 0",
        "verified_empty_state_from_incomplete_source_count == 0",
        "dedicated_team_card_repeats_team_name_count == 0",
        "point1_expected_3x2_not_attempted_count == 0",
        "points3_5_expected_3x2_not_attempted_count == 0",
        "card_gap_below_required_minimum_count == 0",
        "canonical_gradient_missing_count == 0",
        "point_1_ordinary_direct_commit_on_merged_slide_count == 0",
        "verified_direct_collection_activity_dropped_from_later_status_count == 0",
        "rendered_artifact_audit == PASS",
        "python _audit/rendered_presentation_audit.py",
    ),
    "SYSTEM_CONTRACT.yaml": (
        "minimum_text_pt: 11",
        'required_on: "every physical slide, including continuation slides"',
        "incomplete_source_override:",
        'approved_status: "PASS_WITH_USER_OVERRIDE"',
        "points 3–5 → 9 → 13 form a progressive funnel",
        "content_block_provenance_symbol_missing_count: 0",
        "All source/provenance meaning is communicated with the canonical symbol + text defined by the provenance authority.",
        "dedicated_team_card_repeats_team_name_count: 0",
        "mixed_team_card_missing_explicit_team_text_count: 0",
        "rendered_artifact_audit PASS",
        "../../_audit/rendered_presentation_audit.py",
    ),
    "design/VISUAL_DESIGN_MANDATORY.md": (
        "Every physical slide reserves a bottom footer container",
        "use a restrained gradient from approximately `#1E274A` to `#111A33`",
        "fallback — never black and never the retired `#0F1830` background",
        "Meeting point 1 — standard 3×2 work-card grid",
        "Meeting points 3–5 — standard 3×2 team/workstream grid",
        "preserve visible horizontal and vertical gaps between every card; cards must never touch",
    ),
    "monday_meeting/design/SLIDE_DETAIL_SPEC.md": (
        "Every physical slide, including continuation slides, MUST contain a reserved source footer",
        "Points ③–⑤ do not decide project-wide execution order",
        "Each selected work item appears once",
        "Progressive-funnel hard rule",
        "provide separate verified renderer fields",
        "dedicated team slide whose primary header names the team",
        "verified ordinary one-parent direct commits on a registered collection branch are mandatory evidence here",
        "they must not disappear merely because they are excluded from point 1",
    ),
    "monday_meeting/structure/COMPOSITION_ARCHITECTURE.md": (
        "This is a progressive funnel, not permission to duplicate the same content",
        "A missing, failed or incomplete source is not an empty result",
    ),
}



def resolve_active_project_presentation_authorities() -> list[Path]:
    """Resolve active project presentation-authority files from PROJECTS.yaml."""
    if not PROJECT_REGISTRY.exists():
        return []

    docs = list(yaml.safe_load_all(PROJECT_REGISTRY.read_text(encoding="utf-8")))
    data = {}
    for doc in docs:
        if isinstance(doc, dict):
            data.update(doc)

    resolved: list[Path] = []

    for project_id, project in (data.get("projects") or {}).items():
        if project.get("status") != "active":
            continue

        manifest_rel = project.get("manifest")
        if not manifest_rel:
            continue

        manifest_path = ROOT / manifest_rel
        if not manifest_path.exists():
            continue

        manifest_docs = list(yaml.safe_load_all(manifest_path.read_text(encoding="utf-8")))
        manifest = {}
        for doc in manifest_docs:
            if isinstance(doc, dict):
                manifest.update(doc)

        authority_rel = (
            (((manifest.get("context") or {}).get("presentation") or {}).get("authority") or {}).get("path")
        )
        if authority_rel:
            resolved.append(ROOT / authority_rel)

    return resolved


def resolve_active_project_team_visual_identities() -> list[Path]:
    """Resolve active project team-visual-identity files from PROJECTS.yaml."""
    if not PROJECT_REGISTRY.exists():
        return []

    docs = list(yaml.safe_load_all(PROJECT_REGISTRY.read_text(encoding="utf-8")))
    data = {}
    for doc in docs:
        if isinstance(doc, dict):
            data.update(doc)

    resolved: list[Path] = []

    for project_id, project in (data.get("projects") or {}).items():
        if project.get("status") != "active":
            continue

        manifest_rel = project.get("manifest")
        if not manifest_rel:
            continue

        manifest_path = ROOT / manifest_rel
        if not manifest_path.exists():
            continue

        manifest_docs = list(yaml.safe_load_all(manifest_path.read_text(encoding="utf-8")))
        manifest = {}
        for doc in manifest_docs:
            if isinstance(doc, dict):
                manifest.update(doc)

        identity_rel = (
            (((manifest.get("context") or {}).get("design") or {}).get("team_visual_identity") or {}).get("path")
        )
        if identity_rel:
            resolved.append(ROOT / identity_rel)

    return resolved


def main() -> int:
    registry = yaml.safe_load(REGISTRY.read_text(encoding="utf-8"))
    errors: list[str] = []

    registry_text = REGISTRY.read_text(encoding="utf-8")
    context_registry_text = (ROOT / "CONTEXT_REGISTRY.yaml").read_text(encoding="utf-8")
    if "project_resolved: team_visual_identity" not in registry_text:
        errors.append("presentation authority registry does not route project team visual identity")
    if "project_team_visual_identity:" not in context_registry_text:
        errors.append("Monday presentation task does not load project team visual identity")
    category_owner: dict[str, str] = {}

    for authority in registry["active_authorities"]:
        category = authority["category"]
        filename = authority.get("file")
        project_resolved = authority.get("project_resolved")

        owner_label = filename or f"project_resolved:{project_resolved}"
        if category in category_owner:
            errors.append(
                f"duplicate owner for {category}: "
                f"{category_owner[category]} and {owner_label}"
            )
        category_owner[category] = owner_label

        # Project-resolved authorities are validated through the selected project
        # manifest below. They intentionally do not have a static presentation file.
        if project_resolved:
            if not authority.get("resolve_via"):
                errors.append(
                    f"project-resolved authority {project_resolved} is missing resolve_via"
                )
            continue

        if not filename:
            errors.append(f"active authority for {category} has neither file nor project_resolved")
            continue

        authority_path = (PRESENTATIONS / filename).resolve()
        if not authority_path.exists():
            errors.append(f"missing active authority: {filename}")
            continue

        text = authority_path.read_text(encoding="utf-8", errors="replace")
        for label, pattern in STALE_ACTIVE_PATTERNS.items():
            if pattern in text:
                errors.append(f"{label} in active authority {filename}: {pattern}")

        if re.search(r"(?<!👥 )✅ Mötesprotokoll", text):
            errors.append(
                f"meeting protocol missing meeting symbol in active authority {filename}"
            )

        for required_pattern in REQUIRED_ACTIVE_PATTERNS.get(filename, ()):
            if required_pattern not in text:
                errors.append(
                    f"missing required presentation regression pattern in {filename}: "
                    f"{required_pattern}"
                )

    # Project-resolved presentation authorities are active production inputs too.
    for project_authority in resolve_active_project_presentation_authorities():
        if not project_authority.exists():
            errors.append(f"missing project presentation authority: {project_authority}")
            continue
        project_text = project_authority.read_text(encoding="utf-8", errors="replace")
        for label, pattern in PROJECT_PRESENTATION_STALE_PATTERNS.items():
            if pattern in project_text:
                errors.append(
                    f"{label} in project presentation authority {project_authority}: {pattern}"
                )

    # Project-resolved visual-identity files are active production inputs too.
    for visual_identity in resolve_active_project_team_visual_identities():
        if not visual_identity.exists():
            errors.append(f"missing project team visual identity: {visual_identity}")
            continue
        identity_text = visual_identity.read_text(encoding="utf-8", errors="replace")
        required_identity_tokens = (
            "color:",
            "display_name:",
            "Color is supplementary.",
        )
        for token in required_identity_tokens:
            if token not in identity_text:
                errors.append(
                    f"project team visual identity missing required token in {visual_identity}: {token}"
                )

    # Reference examples do not own rules, but they must not demonstrate retired
    # visuals or stale semantics that can pull generation away from active authorities.
    for filename, patterns in REFERENCE_REQUIRED_PATTERNS.items():
        ref_path = PRESENTATIONS / filename
        if not ref_path.exists():
            errors.append(f"missing reference file: {filename}")
            continue
        ref_text = ref_path.read_text(encoding="utf-8", errors="replace")
        for pattern in patterns:
            if pattern not in ref_text:
                errors.append(
                    f"reference missing current regression pattern in {filename}: {pattern}"
                )
        for pattern in REFERENCE_STALE_PATTERNS.get(filename, ()):
            if pattern in ref_text:
                errors.append(f"stale reference pattern in {filename}: {pattern}")

    for group in ("validators", "references"):
        for filename in registry[group]:
            if not (PRESENTATIONS / filename).exists():
                errors.append(f"missing {group} file: {filename}")

    active_files = {item["file"] for item in registry["active_authorities"] if item.get("file")}
    retired_files = set(registry["retired_guides"])
    overlap = active_files & retired_files
    if overlap:
        errors.append(f"files classified as both active and retired: {sorted(overlap)}")

    if errors:
        print("Presentation authority audit: FAIL")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Presentation authority audit: PASS")
    print(f"- active authorities: {len(active_files)}")
    print(f"- unique categories: {len(category_owner)}")
    print(f"- retired guides: {len(retired_files)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
