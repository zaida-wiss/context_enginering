#!/usr/bin/env python3
"""Dev-current routing audit for presentation context.

This audit intentionally inspects only files that exist on the checked-out ref.
It does not recover or compare historical branches.

Goals:
- every current presentation-system file is classified by the active registry;
- every active project presentation authority resolves through its manifest;
- every declared project team visual identity resolves through its manifest;
- the Monday-meeting task bundle explicitly loads project presentation + visual identity;
- moved/localized files cannot silently fall out of the active route.
"""

from __future__ import annotations

from pathlib import Path
import sys
import yaml

ROOT = Path(__file__).resolve().parents[1]
PRESENTATIONS = ROOT / "_ai_guides" / "presentations"
REGISTRY = PRESENTATIONS / "AUTHORITY_REGISTRY.yaml"
CONTEXT_REGISTRY = ROOT / "CONTEXT_REGISTRY.yaml"
PROJECTS = ROOT / "PROJECTS.yaml"

IGNORED_PRESENTATION_PREFIXES = (
    "fixtures/",
)

def load_yaml_documents(path: Path) -> dict:
    merged: dict = {}
    for doc in yaml.safe_load_all(path.read_text(encoding="utf-8")):
        if isinstance(doc, dict):
            merged.update(doc)
    return merged

def rel_presentation_files() -> list[str]:
    files: list[str] = []
    for path in PRESENTATIONS.rglob("*"):
        if not path.is_file():
            continue
        rel = path.relative_to(PRESENTATIONS).as_posix()
        if rel.startswith(IGNORED_PRESENTATION_PREFIXES):
            continue
        files.append(rel)
    return sorted(files)

def registry_mentions(registry_text: str, rel: str) -> bool:
    # Registry entries are stored relative to _ai_guides/presentations.
    return rel in registry_text

def main() -> int:
    errors: list[str] = []

    if not REGISTRY.exists():
        print("Presentation routing audit: FAIL")
        print("- missing AUTHORITY_REGISTRY.yaml")
        return 1

    registry_text = REGISTRY.read_text(encoding="utf-8")
    context_text = CONTEXT_REGISTRY.read_text(encoding="utf-8")

    # Current presentation files must be classified/routed.
    for rel in rel_presentation_files():
        # Navigation files are still explicitly listed in bootstrap_and_navigation.
        if not registry_mentions(registry_text, rel):
            errors.append(f"current presentation file is not classified in authority registry: {rel}")

    # Monday meeting must load project-scoped presentation and visual identity routes.
    required_context_routes = (
        "project_presentation_authority:",
        "logical_destinations.selected_project.presentation_authority",
        "project_team_visual_identity:",
        "logical_destinations.selected_project.team_visual_identity",
        "design_authorities:",
        "_ai_guides/presentations/design/ACCESSIBILITY_NEURODIVERSITY.md",
        "_ai_guides/presentations/design/VISUAL_DESIGN_MANDATORY.md",
        "_ai_guides/presentations/design/READABILITY_HARD_RULES.md",
        "_ai_guides/presentations/design/CARD_COMPONENT_STANDARD.md",
    )
    for token in required_context_routes:
        if token not in context_text:
            errors.append(f"Monday presentation task route missing current dependency: {token}")

    projects = load_yaml_documents(PROJECTS)
    for project_id, project in (projects.get("projects") or {}).items():
        if project.get("status") != "active":
            continue

        manifest_rel = project.get("manifest")
        if not manifest_rel:
            errors.append(f"active project {project_id} has no manifest")
            continue

        manifest_path = ROOT / manifest_rel
        if not manifest_path.exists():
            errors.append(f"active project {project_id} manifest missing: {manifest_rel}")
            continue

        manifest = load_yaml_documents(manifest_path)
        context = manifest.get("context") or {}

        authority_rel = (((context.get("presentation") or {}).get("authority") or {}).get("path"))
        if not authority_rel:
            errors.append(f"active project {project_id} has no presentation authority route")
        elif not (ROOT / authority_rel).exists():
            errors.append(f"active project {project_id} presentation authority missing: {authority_rel}")

        visual_rel = (((context.get("design") or {}).get("team_visual_identity") or {}).get("path"))
        if not visual_rel:
            errors.append(f"active project {project_id} has no team visual identity route")
        elif not (ROOT / visual_rel).exists():
            errors.append(f"active project {project_id} team visual identity missing: {visual_rel}")

        source_rel = (((context.get("sources") or {}).get("path")))
        if not source_rel:
            errors.append(f"active project {project_id} has no source registry route")
        elif not (ROOT / source_rel).exists():
            errors.append(f"active project {project_id} source registry missing: {source_rel}")

    # The presentation authority registry itself must expose project-resolved routes.
    for token in (
        "project_resolved: presentation_authority",
        "project_resolved: source_registry",
        "project_resolved: team_visual_identity",
    ):
        if token not in registry_text:
            errors.append(f"authority registry missing project-resolved route: {token}")

    if errors:
        print("Presentation routing audit: FAIL")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Presentation routing audit: PASS")
    print(f"- current presentation files classified: {len(rel_presentation_files())}")
    active_projects = [
        pid for pid, p in (projects.get("projects") or {}).items()
        if p.get("status") == "active"
    ]
    print(f"- active projects checked: {len(active_projects)}")
    return 0

if __name__ == "__main__":
    sys.exit(main())
