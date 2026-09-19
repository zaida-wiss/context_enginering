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

STALE_ACTIVE_PATTERNS = {
    "legacy AI suggestion symbol": "? AI-förslag",
    "legacy AI analysis symbol": "? AI-analys",
    "old Frontend meeting point": "📝④ Frontend",
    "old Backend meeting point": "📝⑤ Backend",
    "old Native meeting point": "📝⑥ Native",
    "old team range": "④–⑥",
    "obsolete workflow columns": "Arbete | Läge | Härnäst | Vem",
}

REQUIRED_ACTIVE_PATTERNS = {
    "INTEGRITY_CONSTRAINT.md": (
        "pause and ask the user whether to continue without the named source",
        "PASS_WITH_USER_OVERRIDE",
    ),
    "data/DATA_ACQUISITION_CONTRACT.yaml": (
        "PAUSE BEFORE RENDERING if any dataset classified REQUIRED or CRITICAL is INCOMPLETE",
        "continue_without_source",
        "PASS_WITH_USER_OVERRIDE",
    ),
    "design/READABILITY_HARD_RULES.md": (
        "timestamp/source/provenance/footer microcopy: **11 pt minimum**",
        "title → pedagogical explanation: **6 px minimum**, **8 px preferred**",
        "explanation → assignee/developer: **14 px minimum**",
    ),
    "design/CARD_COMPONENT_STANDARD.md": (
        "title → pedagogical explanation: **6 px minimum, 8 px preferred**",
        "explanation → bottom identity zone: **14 px minimum**",
    ),
    "monday_meeting/design/LAYOUT_OVERFLOW_GUARD.md": (
        "title → pedagogical explanation: **6 px minimum, 8 px preferred**",
        "explanation → assignee/developer: **14 px minimum**",
    ),
    "design/PROVENANCE_AND_AI_LABELING.md": (
        "rendered_missing_glyph_count == 0",
        "minimum provenance/source text size in this deck: **11 pt**",
    ),
    "verification/RENDER_GATE_CHECKLIST.md": (
        "canonical_symbol_render_mismatch_count == 0",
    ),
    "SYSTEM_CONTRACT.yaml": (
        "minimum_text_pt: 11",
        'required_on: "every physical slide, including continuation slides"',
        "incomplete_source_override:",
        'approved_status: "PASS_WITH_USER_OVERRIDE"',
    ),
    "design/VISUAL_DESIGN_MANDATORY.md": (
        "Every physical slide reserves a bottom footer container",
    ),
    "monday_meeting/design/SLIDE_DETAIL_SPEC.md": (
        "Every physical slide, including continuation slides, MUST contain a reserved source footer",
    ),
}


def main() -> int:
    registry = yaml.safe_load(REGISTRY.read_text(encoding="utf-8"))
    errors: list[str] = []
    category_owner: dict[str, str] = {}

    for authority in registry["active_authorities"]:
        category = authority["category"]
        filename = authority["file"]

        if category in category_owner:
            errors.append(
                f"duplicate owner for {category}: "
                f"{category_owner[category]} and {filename}"
            )
        category_owner[category] = filename

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

    for group in ("validators", "references", "retired_guides"):
        for filename in registry[group]:
            if not (PRESENTATIONS / filename).exists():
                errors.append(f"missing {group} file: {filename}")

    active_files = {item["file"] for item in registry["active_authorities"]}
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
