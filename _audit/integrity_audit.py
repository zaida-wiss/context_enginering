#!/usr/bin/env python3
"""
Repository Integrity Audit — project-aware mechanical context validation

Validates:
1. PROJECTS.yaml discovers active project manifests without hardcoded project IDs and remains valid with zero active projects.
2. Every active project manifest exists and its registered context paths resolve.
3. Every project source registry has present, matching, unique source IDs.
4. Source fallback access methods are compatible when an allowed-method contract exists.
5. Presentation acquisition delegates source-access ownership to project-resolved sources.
6. Required global bootstrap files exist without requiring legacy project copies.
7. Every canonical path registered in CONTEXT_REGISTRY exists.
8. Logical references used by task bundles and the global project router resolve.
9. Global routing/validation does not require legacy project-owned source/roster paths.
10. The reusable project template and onboarding contract exist without depending on a named project.
11. The global control plane is free of named-project dependencies; named projects belong only in PROJECTS.yaml and project roots.
12. Project manifests explicitly preserve the boundary: reusable operating methods are global; project roots own facts, configuration and confirmed project-specific decisions.\n13. Project legacy files cannot become active authorities.\n14. A synthetic empty project registry resolves to zero projects without fallback to a named project.\n15. A neutral synthetic Project B can onboard through the same generic manifest/source contract without named-project leakage.\n16. Two simultaneously active projects keep manifests and source registries isolated.

This intentionally uses a small YAML-path parser so the audit has no PyYAML dependency.
"""

import os
import re
import sys


def read_text(path):
    with open(path, "r", encoding="utf-8") as handle:
        return handle.read()


def quoted_value(text):
    return text.strip().strip("\"'")


def parse_project_registry_text(text):
    lines = text.splitlines()
    projects = {}
    in_projects = False
    current = None

    for line in lines:
        stripped = line.strip()
        if not stripped or stripped.startswith("#") or stripped == "---":
            continue
        indent = len(line) - len(line.lstrip())

        if indent == 0:
            in_projects = stripped == "projects:"
            current = None
            continue

        if not in_projects:
            continue

        if indent == 2 and stripped.endswith(":"):
            current = stripped[:-1]
            projects[current] = {"manifest": None, "status": None}
            continue

        if current and indent == 4 and ":" in stripped:
            key, value = stripped.split(":", 1)
            key = key.strip()
            value = quoted_value(value)
            if key in {"manifest", "status"}:
                projects[current][key] = value

    return projects


def parse_project_registry():
    return parse_project_registry_text(read_text("PROJECTS.yaml"))


def parse_manifest_paths(path):
    text = read_text(path)
    paths = []
    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith("path:"):
            value = quoted_value(stripped.split("path:", 1)[1])
            if value:
                paths.append(value)
    return paths


def read_sources_section(path):
    """Extract top-level source definitions with lightweight parsing."""
    content = read_text(path)
    lines = content.splitlines()
    sources_start = None
    sources_end = None

    for i, line in enumerate(lines):
        if line.strip() == "sources:":
            sources_start = i
            continue
        if sources_start is not None and line.startswith("---"):
            sources_end = i
            break
        if (
            sources_start is not None
            and line
            and not line.startswith(" ")
            and ":" in line
            and line.strip() != "sources:"
        ):
            sources_end = i
            break

    if sources_start is None:
        return {}

    if sources_end is None:
        sources_end = len(lines)

    sources = {}
    current_source = None
    current_list = None

    for line in lines[sources_start + 1 : sources_end]:
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            continue

        indent = len(line) - len(line.lstrip())

        if indent == 2 and ":" in stripped and not stripped.startswith("-"):
            key = stripped.rstrip(":").strip()
            if key:
                current_source = key
                current_list = None
                sources[current_source] = {
                    "source_id": None,
                    "allowed_access_methods": [],
                    "allowed_implementations": [],
                    "fallback_methods": [],
                }
            continue

        if current_source is None:
            continue

        if indent == 4 and stripped.startswith("source_id:"):
            value = quoted_value(stripped.split("source_id:", 1)[1])
            sources[current_source]["source_id"] = value
            continue

        if stripped == "allowed_access_methods:":
            current_list = "allowed_access_methods"
            continue
        if stripped == "allowed_implementations:":
            current_list = "allowed_implementations"
            continue
        if stripped == "fallbacks:":
            current_list = "fallbacks"
            continue

        if indent <= 4 and stripped.endswith(":"):
            current_list = None

        if current_list in {"allowed_access_methods", "allowed_implementations"} and stripped.startswith("- "):
            value = quoted_value(stripped[2:])
            if value:
                sources[current_source][current_list].append(value)
            continue

        if current_list == "fallbacks" and stripped.startswith("- method:"):
            value = quoted_value(stripped.split("method:", 1)[1])
            if value:
                sources[current_source]["fallback_methods"].append(value)

    return sources


def parse_context_registry():
    text = read_text("CONTEXT_REGISTRY.yaml")
    lines = text.splitlines()
    logical_ids = {}
    registries = {}
    all_paths = []
    section = None
    level1 = None
    level2 = None

    for line in lines:
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            continue
        indent = len(line) - len(line.lstrip())

        if indent == 0 and stripped.endswith(":"):
            section = stripped[:-1]
            level1 = None
            level2 = None
            continue

        if section == "logical_destinations":
            if indent == 2 and stripped.endswith(":"):
                level1 = stripped[:-1]
                level2 = None
                continue
            if indent == 4 and stripped.endswith(":"):
                level2 = stripped[:-1]
                continue
            if indent == 6 and stripped.startswith("path:") and level1 and level2:
                value = quoted_value(stripped.split("path:", 1)[1])
                logical_ids[f"logical_destinations.{level1}.{level2}"] = value
                all_paths.append(value)
                continue
            if indent == 6 and stripped.startswith("resolve_via:") and level1 and level2:
                logical_ids[f"logical_destinations.{level1}.{level2}"] = "<dynamic>"
                continue

        if section == "registries":
            if indent == 2 and stripped.endswith(":"):
                level1 = stripped[:-1]
                continue
            if indent == 4 and stripped.startswith("path:") and level1:
                value = quoted_value(stripped.split("path:", 1)[1])
                registries[f"registries.{level1}"] = value
                all_paths.append(value)
                continue

        if stripped.startswith("path:"):
            value = quoted_value(stripped.split("path:", 1)[1])
            if value:
                all_paths.append(value)

    return logical_ids, registries, all_paths, text


def collect_reference_tokens(text):
    return set(re.findall(r"\b(?:logical_destinations\.[A-Za-z0-9_.-]+|registries\.[A-Za-z0-9_.-]+)\b", text))


def collect_project_router_ids(text):
    return set(re.findall(r"\bproject\.([A-Za-z0-9_-]+)\b", text))


def result(ok, good, bad):
    print(("✅ PASS: " + good) if ok else ("❌ FAIL: " + bad))
    return ok


def main():
    checks = []
    print("=" * 80)
    print("REPOSITORY INTEGRITY AUDIT")
    print("=" * 80)

    print("\nINVARIANT 1: Active Project Discovery")
    try:
        projects = parse_project_registry()
        active = {k: v for k, v in projects.items() if v.get("status") == "active"}
        ok = all(v.get("manifest") for v in active.values())
        checks.append(result(ok, f"{len(active)} active project manifest(s) discovered; zero is valid", "active project entries contain unresolved manifests"))
    except Exception as exc:
        active = {}
        checks.append(result(False, "", f"PROJECTS.yaml parse failed: {exc}"))

    print("\nINVARIANT 1B: Zero-Project Deletion Simulation")
    try:
        simulated = parse_project_registry_text("projects:\n")
        simulated_active = {k: v for k, v in simulated.items() if v.get("status") == "active"}
        ok = simulated == {} and simulated_active == {}
        checks.append(result(ok, "empty project registry resolves to zero projects with no fallback", "empty project registry creates or assumes a project"))
    except Exception as exc:
        checks.append(result(False, "", f"zero-project simulation failed: {exc}"))

    print("\nINVARIANT 1C: Neutral Project B Onboarding Simulation")
    try:
        fixture_manifest = "_audit/fixtures/project_b/PROJECT.yaml"
        fixture_sources = "_audit/fixtures/project_b/sources/SOURCES.yaml"
        fixture_presentation = "_audit/fixtures/project_b/presentation/PRESENTATION_SYSTEM.md"
        synthetic_registry = """projects:
  project_b:
    status: active
    manifest: "_audit/fixtures/project_b/PROJECT.yaml"
"""
        simulated = parse_project_registry_text(synthetic_registry)
        simulated_active = {k: v for k, v in simulated.items() if v.get("status") == "active"}
        fixture_text = read_text(fixture_manifest)
        fixture_paths = parse_manifest_paths(fixture_manifest)
        fixture_source_data = read_sources_section(fixture_sources)
        fixture_sources_text = read_text(fixture_sources)
        no_named_project_leak = "projects/" not in fixture_text.replace("_audit/fixtures/project_b/", "") and "projects/" not in fixture_sources_text
        ok = (
            set(simulated_active) == {"project_b"}
            and simulated_active["project_b"]["manifest"] == fixture_manifest
            and set(fixture_paths) == {fixture_sources, fixture_presentation}
            and all(os.path.exists(path.rstrip("/")) for path in fixture_paths)
            and fixture_source_data.get("PRIMARY_REPOSITORY", {}).get("source_id") == "PRIMARY_REPOSITORY"
            and fixture_presentation in fixture_paths
            and os.path.exists(fixture_presentation)
            and no_named_project_leak
        )
        checks.append(result(ok, "neutral Project B resolves through the generic project contract without named-project leakage", "neutral Project B cannot onboard through the generic project contract"))
    except Exception as exc:
        checks.append(result(False, "", f"Project B simulation failed: {exc}"))

    print("\nINVARIANT 1D: Multi-Project Context Isolation")
    try:
        synthetic_registry = """projects:
  project_b:
    status: active
    manifest: "_audit/fixtures/project_b/PROJECT.yaml"
  project_c:
    status: active
    manifest: "_audit/fixtures/project_c/PROJECT.yaml"
"""
        simulated = parse_project_registry_text(synthetic_registry)
        simulated_active = {k: v for k, v in simulated.items() if v.get("status") == "active"}
        expected = {
            "project_b": ("_audit/fixtures/project_b/PROJECT.yaml", "_audit/fixtures/project_b/sources/SOURCES.yaml"),
            "project_c": ("_audit/fixtures/project_c/PROJECT.yaml", "_audit/fixtures/project_c/sources/SOURCES.yaml"),
        }
        resolved = {}
        for project_id, (manifest, expected_source) in expected.items():
            manifest_text = read_text(manifest)
            match = re.search(r"""context:\s*.*?sources:\s*.*?path:\s*["']?([^"'\n]+)""", manifest_text, re.S)
            resolved[project_id] = match.group(1).strip() if match else None
        distinct_manifests = len({entry.get("manifest") for entry in simulated_active.values()}) == 2
        distinct_sources = len(set(resolved.values())) == 2
        correct_routing = all(
            simulated_active.get(project_id, {}).get("manifest") == manifest
            and resolved.get(project_id) == source
            for project_id, (manifest, source) in expected.items()
        )
        cross_leak = (
            "project_c" in read_text(expected["project_b"][0]).lower()
            or "project_b" in read_text(expected["project_c"][0]).lower()
            or "project_c" in read_text(expected["project_b"][1]).lower()
            or "project_b" in read_text(expected["project_c"][1]).lower()
        )
        ok = set(simulated_active) == set(expected) and distinct_manifests and distinct_sources and correct_routing and not cross_leak
        checks.append(result(ok, "two neutral synthetic projects resolve to distinct manifests and source registries without cross-project leakage", "multi-project routing mixes or leaks project context"))
    except Exception as exc:
        checks.append(result(False, "", f"multi-project isolation simulation failed: {exc}"))

    print("\nINVARIANT 1E: Named Project Deletion Independence Simulation")
    try:
        # Simulate removal of every registered project from project discovery.
        # Global framework files must remain resolvable without reading a named
        # project root. Project-specific validators belong to the project itself.
        simulated = parse_project_registry_text("projects:\n")
        global_required = [
            "README.md",
            "CONTEXT_REGISTRY.yaml",
            "_ai_guides/AI_FRAMEWORK.yaml",
            "_ai_guides/project/PROJECT_CONTEXT_ROUTER.md",
            "_ai_guides/presentations/MANDATORY_READING_ORDER.md",
            "_ai_guides/presentations/AUTHORITY_REGISTRY.yaml",
            "_ai_guides/presentations/INTEGRITY_CONSTRAINT.md",
            "_ai_guides/presentations/SYSTEM_CONTRACT.yaml",
            "projects/_template/README.md",
            "projects/_template/PROJECT.yaml",
        ]
        files_exist = all(os.path.exists(path) for path in global_required)
        no_project_selected = simulated == {}
        registry_text = read_text("CONTEXT_REGISTRY.yaml")
        abstract_project_routing = (
            "logical_destinations.selected_project.source_registry" in registry_text
            and "logical_destinations.selected_project.presentation_authority" in registry_text
            and "selected project manifest -> context.presentation.authority.path" in registry_text
        )
        ok = files_exist and no_project_selected and abstract_project_routing
        checks.append(result(
            ok,
            "global framework remains resolvable with zero named projects and keeps selected-project routing abstract",
            "global framework still requires a named project to resolve core routing",
        ))
    except Exception as exc:
        checks.append(result(False, "", f"named-project deletion simulation failed: {exc}"))

    print("\nINVARIANT 2: Project Manifest Paths Exist")
    ok = True
    project_sources = {}
    for project_id, entry in active.items():
        manifest = entry["manifest"]
        if not os.path.exists(manifest):
            print(f"❌ {project_id}: manifest missing: {manifest}")
            ok = False
            continue
        paths = parse_manifest_paths(manifest)
        for target in paths:
            if not os.path.exists(target.rstrip("/")):
                print(f"❌ {project_id}: manifest target missing: {target}")
                ok = False
        manifest_text = read_text(manifest)
        match = re.search(r"""context:\s*.*?sources:\s*\n\s*path:\s*["']?([^"'\n]+)""", manifest_text, re.S)
        if match:
            project_sources[project_id] = match.group(1).strip()
        else:
            print(f"❌ {project_id}: context.sources.path missing")
            ok = False
    checks.append(result(ok, "all active project manifest paths resolve", "one or more project manifest paths are invalid"))

    print("\nINVARIANT 3: Project Source IDs")
    ok = True
    for project_id, source_path in project_sources.items():
        try:
            sources = read_sources_section(source_path)
            ids = []
            for key, data in sources.items():
                source_id = data["source_id"]
                if not source_id:
                    print(f"❌ {project_id}/{key}: source_id missing")
                    ok = False
                    continue
                ids.append(source_id)
                if key != source_id:
                    print(f"❌ {project_id}/{key}: key != source_id ({source_id})")
                    ok = False
            duplicates = sorted({x for x in ids if ids.count(x) > 1})
            if duplicates:
                print(f"❌ {project_id}: duplicate source IDs: {duplicates}")
                ok = False
            print(f"   {project_id}: {len(ids)} source IDs inspected")
        except Exception as exc:
            print(f"❌ {project_id}: source registry failed: {exc}")
            ok = False
    checks.append(result(ok, "project source IDs are present, matching and unique", "project source registry validation failed"))

    print("\nINVARIANT 4: Fallback Access Compatibility")
    ok = True
    for project_id, source_path in project_sources.items():
        sources = read_sources_section(source_path)
        for key, data in sources.items():
            allowed = set(data["allowed_access_methods"]) | set(data["allowed_implementations"])
            if not allowed:
                continue
            for method in data["fallback_methods"]:
                if method not in allowed:
                    print(f"❌ {project_id}/{key}: fallback method {method!r} is not allowed")
                    ok = False
    checks.append(result(ok, "declared fallback methods respect declared access contracts", "fallback/access mismatch found"))

    print("\nINVARIANT 5: Presentation Source Ownership Delegation")
    try:
        contract = read_text("_ai_guides/presentations/data/DATA_ACQUISITION_CONTRACT.yaml")
        ok = "source_registry" in contract or "project manifest" in contract or "selected project" in contract
        checks.append(result(ok, "acquisition delegates source ownership", "acquisition contract does not delegate source ownership"))
    except Exception as exc:
        checks.append(result(False, "", f"acquisition contract unavailable: {exc}"))

    print("\nINVARIANT 6: Required Global Bootstrap Files Exist")
    required = [
        "README.md",
        "PROJECTS.yaml",
        "CONTEXT_REGISTRY.yaml",
        "_ai_guides/AI_FRAMEWORK.yaml",
        "_ai_guides/project/PROJECT_CONTEXT_ROUTER.md",
        "_ai_guides/presentations/MANDATORY_READING_ORDER.md",
        "_ai_guides/presentations/AUTHORITY_REGISTRY.yaml",
        "_ai_guides/presentations/INTEGRITY_CONSTRAINT.md",
        "_ai_guides/presentations/SYSTEM_CONTRACT.yaml",
    ]
    ok = True
    for target in required:
        exists = os.path.exists(target)
        print(f"{'✅' if exists else '❌'} {target}")
        ok &= exists
    checks.append(ok)

    print("\nINVARIANT 7: Registered Canonical Paths Exist")
    try:
        logical_ids, registries, paths, registry_text = parse_context_registry()
        missing = [p for p in sorted(set(paths)) if not os.path.exists(p.rstrip("/"))]
        for target in missing:
            print(f"❌ missing: {target}")
        ok = not missing
        checks.append(result(ok, f"{len(set(paths))} registered paths resolve", "registered canonical paths are missing"))
    except Exception as exc:
        logical_ids, registries, registry_text = {}, {}, ""
        checks.append(result(False, "", f"CONTEXT_REGISTRY parse failed: {exc}"))

    print("\nINVARIANT 8: Logical References Resolve")
    known = set(logical_ids) | set(registries)
    unresolved = sorted(ref for ref in collect_reference_tokens(registry_text) if ref not in known)
    for ref in unresolved:
        print(f"❌ unresolved: {ref}")
    ok = not unresolved
    try:
        router = read_text("_ai_guides/project/PROJECT_CONTEXT_ROUTER.md")
        # Project selection is registry-driven. Literal project.<id> shorthands in
        # the generic router are treated as legacy leakage, not required routing.
        leaked_ids = collect_project_router_ids(router)
        if leaked_ids:
            print(f"❌ generic router contains literal project IDs: {sorted(leaked_ids)}")
            ok = False
    except Exception as exc:
        print(f"❌ router inspection failed: {exc}")
        ok = False
    checks.append(result(ok, "logical references and generic router resolve", "unresolved refs or project-ID leakage found"))

    print("\nINVARIANT 9: Legacy Project-Owned Global Copies Are Not Required")
    legacy_required = {
        "data/SOURCES.yaml",
        "_memory/TEAM_ROSTER.md",
    }
    active_control_files = [
        "CONTEXT_REGISTRY.yaml",
        "_ai_guides/presentations/SYSTEM_CONTRACT.yaml",
        "_ai_guides/presentations/AUTHORITY_REGISTRY.yaml",
        "_ai_guides/project/PROJECT_CONTEXT_ROUTER.md",
    ]
    ok = True
    for control in active_control_files:
        text = read_text(control)
        for legacy in legacy_required:
            if legacy in text:
                print(f"❌ {control} still requires legacy project-owned path {legacy}")
                ok = False
    checks.append(result(ok, "global control plane no longer requires legacy source/roster copies", "legacy project-owned paths are still active"))

    print("\nINVARIANT 10: Reusable Project Onboarding Contract")
    template_required = [
        "projects/_template/README.md",
        "projects/_template/PROJECT.yaml",
        "projects/_template/sources/SOURCES.yaml",
    ]
    ok = True
    for target in template_required:
        exists = os.path.exists(target)
        print(f"{'✅' if exists else '❌'} {target}")
        ok &= exists
    try:
        template_manifest = read_text("projects/_template/PROJECT.yaml")
        template_guide = read_text("projects/_template/README.md")
        placeholder_missing = "<project_id>" not in template_manifest
        if placeholder_missing:
            print("❌ project template lacks project_id placeholder routing")
            ok = False
        presentation_capability_missing = (
            "presentation:" not in template_manifest
            or "projects/<project_id>/presentation/PRESENTATION_SYSTEM.md" not in template_manifest
        )
        if presentation_capability_missing:
            print("❌ project template lacks optional project presentation authority capability")
            ok = False
    except Exception as exc:
        print(f"❌ project template inspection failed: {exc}")
        ok = False
    checks.append(result(ok, "project onboarding template is present and project-neutral", "project onboarding contract is incomplete or project-specific"))

    print("\nINVARIANT 11: Named-Project Deletion Independence")
    global_control_files = [
        "CONTEXT_REGISTRY.yaml",
        "_ai_guides/AI_FRAMEWORK.yaml",
        "_ai_guides/project/PROJECT_CONTEXT_ROUTER.md",
        "_ai_guides/presentations/MANDATORY_READING_ORDER.md",
        "_ai_guides/presentations/AUTHORITY_REGISTRY.yaml",
        "_ai_guides/presentations/INTEGRITY_CONSTRAINT.md",
        "_ai_guides/presentations/SYSTEM_CONTRACT.yaml",
        "projects/_template/README.md",
        "projects/_template/PROJECT.yaml",
    ]
    # PROJECTS.yaml is intentionally excluded: it is the one global registry
    # allowed to name registered projects. This audit must not hardcode any
    # current project name, otherwise adding/removing projects would require
    # editing the global validator itself.
    registry = read_text("PROJECTS.yaml")
    registered_roots = set(re.findall(r'^\\s*context_root:\\s*["\\\']?([^"\\\'\\n]+)', registry, re.M))
    registered_repositories = set(re.findall(r'^\\s*github_repository:\\s*["\\\']?([^"\\\'\\n]+)', registry, re.M))
    forbidden_literals = sorted(registered_roots | registered_repositories)
    ok = True
    for control in global_control_files:
        text = read_text(control)
        for literal in forbidden_literals:
            if literal and literal in text:
                print(f"❌ {control} depends on registered-project literal: {literal}")
                ok = False
    checks.append(result(ok, "global control plane has no registered-project path/repository dependencies", "named-project dependency remains in global control plane"))

    print("\nINVARIANT 12: Global-Method / Project-Fact Boundary")
    required_global_methods = [
        "_ai_guides/project/TEAM_STANDARDS.md",
        "_ai_guides/project/TEAM_TONE_AND_COLLABORATION.yaml",
        "_ai_guides/project/HR_AND_TEAM_SUPPORT.yaml",
        "_ai_guides/project/DEFINITION_OF_DONE.md",
        "_ai_guides/project/TESTING.md",
        "_ai_guides/project/GOALS_AND_SPRINT_PLANNING.md",
        "_ai_guides/project/RISK_MANAGEMENT.md",
        "_ai_guides/project/DEPENDENCIES_AND_CAPACITY.md",
    ]
    ok = True
    for target in required_global_methods:
        if not os.path.exists(target):
            print(f"❌ missing reusable global method: {target}")
            ok = False
    for project_id, entry in active.items():
        manifest = entry.get("manifest")
        if not manifest or not os.path.exists(manifest):
            continue
        manifest_text = read_text(manifest)
        lower_manifest = manifest_text.lower()
        preserves_fact_boundary = ("specific facts" in lower_manifest or "project-specific facts" in lower_manifest)
        preserves_global_boundary = "generic framework" in lower_manifest
        if not (preserves_fact_boundary and preserves_global_boundary):
            print(f"❌ {project_id}: manifest does not state the reusable-method/project-fact ownership boundary")
            ok = False
    checks.append(result(ok, "reusable team/project methods are globally owned and project manifests preserve the boundary", "global method ownership or project boundary is incomplete"))

    print("\nINVARIANT 13: Project Legacy Files Cannot Become Active Authorities")
    ok = True
    try:
        registry_text = read_text("CONTEXT_REGISTRY.yaml")
        for project_id, entry in active.items():
            manifest = entry.get("manifest")
            if not manifest or not os.path.exists(manifest):
                continue
            project_root = os.path.dirname(manifest)
            legacy_root = os.path.join(project_root, "legacy")
            legacy_prefix = legacy_root.replace(os.sep, "/") + "/"
            if legacy_prefix in registry_text:
                print(f"❌ {project_id}: global context registry references project legacy path {legacy_prefix}")
                ok = False
            if os.path.isdir(legacy_root):
                for name in os.listdir(legacy_root):
                    if not name.endswith((".md", ".yaml", ".yml")):
                        continue
                    legacy_path = os.path.join(legacy_root, name)
                    legacy_text = read_text(legacy_path).lower()
                    if "archived" not in legacy_text or "not generic framework authority" not in legacy_text:
                        print(f"❌ {project_id}: legacy file lacks explicit non-authority marker: {legacy_path}")
                        ok = False
    except Exception as exc:
        print(f"❌ legacy-authority inspection failed: {exc}")
        ok = False
    checks.append(result(ok, "project legacy files are explicitly non-authoritative and absent from the global registry", "project legacy content can leak into active authority routing"))

    print("\nINVARIANT 14: Progressive Minimum-Sufficient Task Context")
    ok = True
    try:
        registry_text = read_text("CONTEXT_REGISTRY.yaml")
        coding_match = re.search(r"(?ms)^  coding_assistance:\n(.*?)(?=^  [a-zA-Z0-9_]+:\n|^path_change_process:)", registry_text)
        coding = coding_match.group(1) if coding_match else ""
        required_markers = (
            "strategy: progressive_minimum_sufficient",
            "required_core:",
            "conditional:",
            "Load conditional authorities only when their domain can materially change the answer or action.",
        )
        if not coding or not all(marker in coding for marker in required_markers):
            print("❌ coding_assistance does not encode progressive minimum-sufficient loading")
            ok = False
        legacy_load = re.search(r"(?m)^    load:\s*$", coding)
        if legacy_load:
            print("❌ coding_assistance still exposes a monolithic mandatory load list")
            ok = False
        core_match = re.search(r"(?ms)required_core:\n(.*?)(?=^      conditional:)", coding)
        core = core_match.group(1) if core_match else ""
        forbidden_core = (
            "goals_and_sprint_planning",
            "risk_management",
            "dependencies_and_capacity",
            "cross_layer_awareness",
            "technical_debt",
            "team_tone_and_collaboration",
        )
        leaked = [name for name in forbidden_core if name in core]
        if leaked:
            print(f"❌ conditional domains leaked into required coding core: {leaked}")
            ok = False
    except Exception as exc:
        print(f"❌ progressive-context inspection failed: {exc}")
        ok = False
    checks.append(result(ok, "coding task bundle encodes progressive minimum-sufficient context loading", "coding task bundle can force unrelated context into every coding task"))

    print("\nINVARIANT 15: Progressive Planning Context + Presentation Safety Core")
    ok = True
    try:
        registry_text = read_text("CONTEXT_REGISTRY.yaml")
        for task_name in ("issue_creation", "sprint_planning"):
            task_match = re.search(rf"(?ms)^  {task_name}:\n(.*?)(?=^  [a-zA-Z0-9_]+:\n|^path_change_process:)", registry_text)
            task = task_match.group(1) if task_match else ""
            if "strategy: progressive_minimum_sufficient" not in task or "required_core:" not in task or "conditional:" not in task:
                print(f"❌ {task_name} does not encode progressive minimum-sufficient loading")
                ok = False
            if re.search(r"(?m)^    load:\s*$", task):
                print(f"❌ {task_name} still exposes a monolithic mandatory load list")
                ok = False
        presentation_router = read_text("_ai_guides/presentations/MANDATORY_READING_ORDER.md")
        required_bootstrap = ("AI_FRAMEWORK.yaml", "AUTHORITY_REGISTRY.yaml", "INTEGRITY_CONSTRAINT.md", "SYSTEM_CONTRACT.yaml")
        if not all(name in presentation_router for name in required_bootstrap):
            print("❌ presentation bootstrap lost a mandatory safety/execution authority")
            ok = False
        presentation_task = re.search(r"(?ms)^  monday_meeting_presentation:\n(.*?)(?=^path_change_process:)", registry_text)
        presentation = presentation_task.group(1) if presentation_task else ""
        required_delivery = ("design_authorities:", "verification:", "default_delivery:")
        if not all(name in presentation for name in required_delivery):
            print("❌ Monday presentation task lost design, verification or delivery gates")
            ok = False
    except Exception as exc:
        print(f"❌ planning/presentation context inspection failed: {exc}")
        ok = False
    checks.append(result(ok, "issue and sprint tasks load progressively while presentation safety/delivery core remains mandatory", "task context optimization weakens planning relevance or presentation safety gates"))

    print("\nINVARIANT 16: Project-Aware Context Ingestion Routing")
    ok = True
    try:
        routing = read_text("_ai_guides/context/CONTEXT_ROUTING.yaml")
        stale_project_routes = (
            "data.course_schedule",
            "data.course_milestones",
            "data.course_roadmap",
            "memory.current_sprint_schema",
            "memory.team_roster",
        )
        leaked = [route for route in stale_project_routes if route in routing]
        if leaked:
            print(f"❌ context ingestion still routes project facts through global legacy shorthands: {leaked}")
            ok = False
        required = ("selected_project.manifest", "selected_project.team_roster", "selected_project.source_registry", "Resolve the selected project")
        if not all(token in routing for token in required):
            print("❌ context ingestion does not consistently resolve project-owned facts through selected-project context")
            ok = False
    except Exception as exc:
        print(f"❌ context-ingestion routing inspection failed: {exc}")
        ok = False
    checks.append(result(ok, "new project facts route through selected-project capabilities rather than global legacy domains", "context ingestion can leak project facts into global memory/data domains"))

    print("\nINVARIANT 17: Presentation Readability + Semantic Visual Grammar")
    ok = True
    try:
        visual = read_text("_ai_guides/presentations/design/VISUAL_DESIGN_MANDATORY.md")
        access = read_text("_ai_guides/presentations/design/ACCESSIBILITY_NEURODIVERSITY.md")
        visual_required = (
            "#1E274A",
            "#111A33",
            "never black",
            "More slides are preferred to smaller text.",
            "20 pt or larger",
            "18 pt or larger",
            "🎯 task · 🕒 time · 📍 place · 💡 purpose · 🛠 method",
            "#EF4444",
            "#F59E0B",
            "#22C55E",
        )
        if not all(token in visual for token in visual_required):
            print("❌ global presentation authority lost navy/readability/symbol/priority semantics")
            ok = False
        access_required = ("Shared-screen readability", "20 pt", "18 pt", "paginate before compressing")
        if not all(token in access for token in access_required):
            print("❌ accessibility authority lost shared-screen readability targets")
            ok = False
    except Exception as exc:
        print(f"❌ presentation visual grammar inspection failed: {exc}")
        ok = False
    checks.append(result(ok, "presentation authorities preserve navy background, readable type, five-symbol grammar and semantic priority colors", "presentation rendering can regress to black/small text or lose semantic visual cues"))

    print("\nINVARIANT 18: Meeting-Point Geometry Precedes Global Grid")
    ok = True
    try:
        visual = read_text("_ai_guides/presentations/design/VISUAL_DESIGN_MANDATORY.md")
        detail = read_text("_ai_guides/presentations/monday_meeting/design/SLIDE_DETAIL_SPEC.md")
        composition = read_text("_ai_guides/presentations/monday_meeting/structure/COMPOSITION_ARCHITECTURE.md")
        required_visual = (
            "Meeting-point geometry precedence — hard rule",
            "meeting-point-specific geometry",
            "true chronological course/project timeline",
            "A timeline remains a timeline",
            "vertical priority sequence remains vertical",
        )
        if not all(token in visual for token in required_visual):
            print("❌ global visual authority can flatten registered meeting-point geometry")
            ok = False
        forbidden_point2 = (
            "Meeting point 2 uses the same responsive card/grid language as the rest of the deck.",
            "Do not require a full-slide timeline.",
        )
        if any(token in visual for token in forbidden_point2):
            print("❌ stale point-2 generic-grid rule conflicts with chronological timeline authority")
            ok = False
        if "Primary visual: chronological course/project timeline — mandatory" not in detail:
            print("❌ point-2 detail authority lost mandatory chronological timeline")
            ok = False
        if "②: a chronological course/project timeline with an explicit current-week marker" not in composition:
            print("❌ composition architecture lost point-2 timeline contract")
            ok = False
        if "⑨ uses vertically stacked execution groups" not in composition:
            print("❌ composition architecture lost point-9 vertical execution contract")
            ok = False
    except Exception as exc:
        print(f"❌ meeting-point geometry inspection failed: {exc}")
        ok = False
    checks.append(result(ok, "meeting-point-specific geometry overrides the global grid fallback", "generic visual rules can erase timeline/dependency/priority/planning formats"))

    print("\nINVARIANT 19: Point 2 Covers the Full Course Period")
    ok = True
    try:
        detail = read_text("_ai_guides/presentations/monday_meeting/design/SLIDE_DETAIL_SPEC.md")
        gate = read_text("_ai_guides/presentations/verification/RENDER_GATE_CHECKLIST.md")
        detail_required = (
            "entire registered",
            "course/project period",
            "from course start to final delivery",
            "current-week marker",
        )
        gate_required = (
            "point2_full_course_period_missing_count == 0",
            "point2_course_start_anchor_missing_count == 0",
            "point2_final_delivery_anchor_missing_count == 0",
            "point2_current_position_marker_missing_count == 0",
            "point2_near_term_only_timeline_count == 0",
            "near-term-only timeline",
        )
        if not all(token in detail for token in detail_required):
            print("❌ point-2 content authority no longer requires full-period chronology")
            ok = False
        if not all(token in gate for token in gate_required):
            print("❌ render gate can accept a truncated point-2 course timeline")
            ok = False
    except Exception as exc:
        print(f"❌ full-course timeline inspection failed: {exc}")
        ok = False
    checks.append(result(ok, "point 2 must span course start through final delivery and mark the current position", "point 2 can regress to a near-term-only timeline"))

    print("\nINVARIANT 20: Compact Developer + Delivery Activity Row")
    ok = True
    try:
        card = read_text("_ai_guides/presentations/design/CARD_COMPONENT_STANDARD.md")
        gate = read_text("_ai_guides/presentations/verification/RENDER_GATE_CHECKLIST.md")
        required = (
            "developer and assignee are one presentation concept",
            "same row",
            "PR submission/open timestamp",
            "latest verified commit/push timestamp",
            "MUST NOT add a per-card `MERGAD`, `Merged`, checkmark badge, pill, stamp or equivalent merge label",
            "redundant_merge_badge_or_stamp_count == 0",
            "separate_developer_and_assigned_row_count == 0",
            "developer_activity_time_detached_from_identity_count == 0",
            "unrequested_tag_comment_reaction_metadata_count == 0",
        )
        joined = card + "\n" + gate
        if not all(token in joined for token in required):
            print("❌ card model can duplicate ownership/activity metadata or repeat merge status")
            ok = False
    except Exception as exc:
        print(f"❌ compact developer/activity inspection failed: {exc}")
        ok = False
    checks.append(result(ok, "issue/PR cards keep one developer identity with delivery time and no redundant merge badge", "cards can regress to duplicated Assigned/developer rows, detached timestamps or noisy merge/tags metadata"))

    print("\nINVARIANT 21: Source Symbol Inline + Full Explanation in Slide Margin")
    ok = True
    try:
        card = read_text("_ai_guides/presentations/design/CARD_COMPONENT_STANDARD.md")
        gate = read_text("_ai_guides/presentations/verification/RENDER_GATE_CHECKLIST.md")
        contract = read_text("_ai_guides/presentations/SYSTEM_CONTRACT.yaml")
        required = (
            "Full source labels are rendered once in the physical slide's reserved source margin/footer.",
            "slide source margin/footer deduplicates every source symbol used",
            "slide_margin_source_full_label_missing_count == 0",
            "inline_symbol_slide_margin_source_mismatch_count == 0",
            "physical slide margin/footer deduplicates the used source symbols",
        )
        joined = card + "\n" + gate + "\n" + contract
        if not all(token in joined for token in required):
            print("❌ provenance contract does not preserve inline symbol → full slide-margin explanation")
            ok = False
        stale = (
            "each card repeats every used symbol with its full text label",
            "card_bottom_provenance_full_label_missing_count == 0",
            "card_bottom_provenance_symbol_text_mismatch_count == 0",
        )
        if any(token in joined for token in stale):
            print("❌ stale card-level long provenance labels conflict with slide-margin source explanation")
            ok = False
    except Exception as exc:
        print(f"❌ source-symbol/margin inspection failed: {exc}")
        ok = False
    checks.append(result(ok, "source symbols stay inline while full source explanations live in the slide margin/footer", "long source labels can crowd cards or source symbols can lose their explanation"))

    print("\nINVARIANT 22: Meeting Protocol Is Decision Evidence, Not Priority Truth")
    ok = True
    try:
        planning = read_text("_ai_guides/project/GOALS_AND_SPRINT_PLANNING.md")
        detail = read_text("_ai_guides/presentations/monday_meeting/design/SLIDE_DETAIL_SPEC.md")
        gate = read_text("_ai_guides/presentations/verification/RENDER_GATE_CHECKLIST.md")
        required = (
            "Meeting protocol is decision evidence, not priority truth",
            "independently cross-check it against available verified evidence",
            "🔎 AI-analys — HEADS-UP",
            "Mandatory priority sanity check against team decisions",
            "team_priority_without_independent_sanity_check_count == 0",
            "material_priority_misalignment_without_ai_headsup_count == 0",
            "meeting_decision_silently_rewritten_by_ai_count == 0",
        )
        joined = planning + "\n" + detail + "\n" + gate
        if not all(token in joined for token in required):
            print("❌ meeting protocol can become automatic priority truth or suppress AI heads-up")
            ok = False
    except Exception as exc:
        print(f"❌ priority sanity-check inspection failed: {exc}")
        ok = False
    checks.append(result(ok, "meeting decisions are preserved as evidence while AI independently checks priority alignment", "team protocol can be mistaken for optimal priority truth"))

    print("\nINVARIANT 23: AI Senior Team-Member Posture")
    ok = True
    try:
        framework = read_text("_ai_guides/AI_FRAMEWORK.yaml")
        analysis = read_text("_ai_guides/PROJECT_WORK_ANALYSIS.md")
        required = (
            "senior_team_member_posture:",
            "independently_validate_team_assumptions_against_current_verified_evidence",
            "challenge_a_team_priority_when_verified_evidence_indicates_a_materially_better_or_safer_order",
            'material_concern_label: "🔎 AI-analys — HEADS-UP"',
            "user_and_team_retain_decision_authority: true",
            "ai_does_not_claim_formal_team_role_or_human_experience: true",
            "## Senior engineering posture",
            "ask whether the team is solving the right problem",
            "exception-driven",
        )
        joined = framework + "\n" + analysis
        if not all(token in joined for token in required):
            print("❌ global AI behavior lost senior engineering challenge/orientation contract")
            ok = False
    except Exception as exc:
        print(f"❌ senior-posture inspection failed: {exc}")
        ok = False
    checks.append(result(ok, "AI contributes with senior engineering bird's-eye judgment while humans retain decisions", "AI can regress to passive execution/status repetition or overclaim human authority"))

    print("\nINVARIANT 24: Global Baseline + Explicit Project Geometry Override")
    ok = True
    try:
        visual = read_text("_ai_guides/presentations/design/VISUAL_DESIGN_MANDATORY.md")
        overflow = read_text("_ai_guides/presentations/monday_meeting/design/LAYOUT_OVERFLOW_GUARD.md")
        joined_global = visual + "\n" + overflow

        global_required = (
            "Global presentation design is the default for every project.",
            "ask the user an explicit control question",
            "Without explicit approval, the global design wins by default.",
            "Meeting point 1 — standard 3×2 work-card grid",
            "Meeting points 3–5 — standard 3×2 team/workstream grid",
            "the active global geometry baseline from `VISUAL_DESIGN_MANDATORY.md`",
            "project-specific geometry only through the registered project authority",
            "explicit conflict/override gate when it differs from the global baseline",
            "design fidelity is part of fit",
        )
        if not all(token in joined_global for token in global_required):
            print("❌ presentation geometry lost either the global 3×2 baseline or explicit project-override gate")
            ok = False

        stale_unconditional_delegation = (
            "card capacity, slot orientation and pagination are owned by the active project presentation authority",
        )
        if any(token in joined_global for token in stale_unconditional_delegation):
            print("❌ stale unconditional project-geometry delegation can bypass the active global baseline")
            ok = False
    except Exception as exc:
        print(f"❌ global/project geometry inspection failed: {exc}")
        ok = False
    checks.append(result(
        ok,
        "global 3×2 baseline remains active while project-specific geometry requires the registered override path",
        "presentation geometry can silently bypass either the global baseline or project-specific override contract",
    ))

    print("\nINVARIANT 24B: Project Presentation Authority Routing")
    ok = True
    try:
        registry = read_text("_ai_guides/presentations/AUTHORITY_REGISTRY.yaml")
        required_registry = (
            "project_resolved: presentation_authority",
            "context.presentation.authority.path",
            "category: project_presentation",
        )
        if not all(token in registry for token in required_registry):
            print("❌ presentation authority registry does not resolve project-owned presentation rules")
            ok = False
        for project_id, entry in active.items():
            manifest = entry.get("manifest")
            if not manifest or not os.path.exists(manifest):
                continue
            manifest_text = read_text(manifest)
            match = re.search(r"""presentation:\s*.*?authority:\s*.*?path:\s*["']?([^"'\n]+)""", manifest_text, re.S)
            # Project presentation authority is optional. Global presentation
            # rules remain the default when the capability is not declared.
            if not match:
                continue
            authority_path = match.group(1).strip()
            if not os.path.exists(authority_path):
                print(f"❌ {project_id}: declared presentation authority missing: {authority_path}")
                ok = False
    except Exception as exc:
        print(f"❌ project presentation authority routing inspection failed: {exc}")
        ok = False
    checks.append(result(ok, "declared project presentation authorities resolve through the selected project manifest while undeclared projects inherit global defaults", "declared project presentation rules can exist without being loaded by the presentation router"))

    print("\nINVARIANT 25: Presentation Visual Fidelity Gate")
    ok = True
    try:
        visual = read_text("_ai_guides/presentations/design/VISUAL_DESIGN_MANDATORY.md")
        gate = read_text("_ai_guides/presentations/verification/RENDER_GATE_CHECKLIST.md")
        required = (
            "Rendered card-surface fidelity — hard gate",
            "design fidelity is part of fit",
            "VISUAL FIDELITY — CARD SURFACE + RESPONSIVENESS",
            "flat_card_surface_regression_count == 0",
            "card_corner_rounding_missing_count == 0",
            "card_depth_treatment_missing_count == 0",
            "card_text_outside_rounded_bounds_count == 0",
            "responsive_card_geometry_failure_count == 0",
            "density_fit_achieved_by_design_degradation_count == 0",
            "actual slide image/PDF appearance",
        )
        joined = visual + "\n" + gate
        if not all(token in joined for token in required):
            print("❌ presentation can pass while losing rounded glass cards or responsive visual fidelity")
            ok = False
    except Exception as exc:
        print(f"❌ visual-fidelity inspection failed: {exc}")
        ok = False
    checks.append(result(ok, "render gate preserves navy background, rounded glass cards and responsive in-card fit", "visual design can regress while geometry-only tests stay green"))

    print("\nINVARIANT 26: Developer Identity + Latest Delivery Activity")
    ok = True
    try:
        card = read_text("_ai_guides/presentations/design/CARD_COMPONENT_STANDARD.md")
        gate = read_text("_ai_guides/presentations/verification/RENDER_GATE_CHECKLIST.md")
        required = (
            "developer and assignee are one presentation concept",
            "{FIRST_NAME} · PR {D MMM · HH:MM}",
            "{FIRST_NAME} · commit {D MMM · HH:MM}",
            "separate_developer_and_assignee_row_count == 0",
            "developer_activity_row_missing_count == 0",
            "developer_activity_timestamp_detached_from_name_count == 0",
            "active_pr_wrong_activity_timestamp_type_count == 0",
        )
        joined = card + "\n" + gate
        if not all(token in joined for token in required):
            print("❌ active issue/PR cards can split developer/assignee or detach latest delivery activity from the developer")
            ok = False
    except Exception as exc:
        print(f"❌ developer/activity inspection failed: {exc}")
        ok = False
    checks.append(result(ok, "active issue/PR cards unify developer/assignee and show latest delivery activity on the same row", "ownership/activity metadata can regress to duplicate or detached rows"))

    print("\nINVARIANT 27: Presentation Support Files Are Registered and Routed")
    ok = True
    try:
        authority_registry = read_text("_ai_guides/presentations/AUTHORITY_REGISTRY.yaml")
        context_registry = read_text("CONTEXT_REGISTRY.yaml")
        retired_redirect = read_text("_ai_guides/presentations/monday_meeting/data/DATA_COLLECTION_MANDATORY.md")
        required_registered = (
            "../COGNITIVE_ACCESSIBILITY_NEUROINCLUSIVE_DESIGN.md",
            "../AI_BEST_PRACTICE_EVIDENCE_POLICY.yaml",
            "data/CURRENT_SPRINT_SCHEMA.yaml",
            "data/DATA_COLLECTION_MANDATORY.md",
            "data/ACTIVE_WORK_DETECTION_MODEL.md",
            "monday_meeting/structure/COMPOSITION_ARCHITECTURE.md",
            "monday_meeting/data/DATA_COLLECTION_MANDATORY.md",
        )
        if not all(token in authority_registry for token in required_registered):
            print("❌ one or more important presentation support files are not classified in AUTHORITY_REGISTRY")
            ok = False

        required_task_routes = (
            "logical_destinations.presentation_processes.composition",
            "logical_destinations.presentation_schemas.current_sprint",
            "logical_destinations.presentation_processes.data_collection",
            "logical_destinations.presentation_processes.active_work_detection",
        )
        if not all(token in context_registry for token in required_task_routes):
            print("❌ Monday presentation task does not route through all critical support processes/schemas")
            ok = False

        retired_required = (
            "status: retired",
            "RETIRED_NON_AUTHORITY",
            "_ai_guides/presentations/data/DATA_COLLECTION_MANDATORY.md",
        )
        if not all(token in retired_redirect for token in retired_required):
            print("❌ stale Monday data-collection duplicate is not safely retired/redirected")
            ok = False

        presentation_root = "_ai_guides/presentations"
        classified_extensions = (".md", ".yaml", ".yml", ".html")
        orphaned = []
        for root, _, names in os.walk(presentation_root):
            for name in names:
                if not name.endswith(classified_extensions):
                    continue
                full_path = os.path.join(root, name).replace(os.sep, "/")
                relative = full_path[len(presentation_root) + 1 :]
                if relative not in authority_registry:
                    orphaned.append(relative)
        if orphaned:
            print(f"❌ presentation files are not classified by AUTHORITY_REGISTRY: {sorted(orphaned)}")
            ok = False
    except Exception as exc:
        print(f"❌ presentation support registration inspection failed: {exc}")
        ok = False
    checks.append(result(
        ok,
        "important presentation support files are classified, routed and protected from orphaning",
        "presentation support files can become orphaned, duplicated or silently inactive",
    ))

    print("\nINVARIANT 28: Recovered Friday Presentation Capabilities")
    ok = True
    try:
        contract = read_text("_ai_guides/presentations/SYSTEM_CONTRACT.yaml")
        readability = read_text("_ai_guides/presentations/design/READABILITY_HARD_RULES.md")
        detail = read_text("_ai_guides/presentations/monday_meeting/design/SLIDE_DETAIL_SPEC.md")
        gate = read_text("_ai_guides/presentations/verification/RENDER_GATE_CHECKLIST.md")

        copyable_required = (
            "Required meeting text remains native/editable presentation text",
            "required meeting text is native/selectable/copyable text",
            "required_text_rasterized_count == 0",
            "required_text_not_selectable_or_copyable_count == 0",
        )
        if not all(token in contract + "\n" + gate for token in copyable_required):
            print("❌ copyable meeting-text contract can regress or disappear")
            ok = False

        terminology_required = (
            "DOMAIN TERMINOLOGY SHOULD TEACH, NOT DECODE",
            "keep the real industry term visible",
            "explain only terms that actually appear on the slide",
            "unexplained_material_domain_term_count == 0",
        )
        if not all(token in readability + "\n" + gate for token in terminology_required):
            print("❌ domain-terminology pedagogy can regress or disappear")
            ok = False

        dependency_map_required = (
            "Dependency / blocker relationship map — mandatory",
            "visible directional connector(s)",
            "generic 2×N card grid",
            "point6_relational_dependency_rendered_as_unconnected_cards_count == 0",
            "point6_missing_directional_connector_count == 0",
        )
        if not all(token in detail + "\n" + gate for token in dependency_map_required):
            print("❌ point 6 can regress from dependency map to unrelated cards")
            ok = False
    except Exception as exc:
        print(f"❌ recovered Friday capability inspection failed: {exc}")
        ok = False
    checks.append(result(
        ok,
        "copyable text, domain pedagogy and blocker/dependency map remain protected",
        "Friday presentation capabilities can silently disappear during refactoring",
    ))

    print("\nINVARIANT 29: Friday Special Layouts Stay Special")
    ok = True
    try:
        visual = read_text("_ai_guides/presentations/design/VISUAL_DESIGN_MANDATORY.md")
        composition = read_text("_ai_guides/presentations/monday_meeting/structure/COMPOSITION_ARCHITECTURE.md")
        detail = read_text("_ai_guides/presentations/monday_meeting/design/SLIDE_DETAIL_SPEC.md")
        gate = read_text("_ai_guides/presentations/verification/RENDER_GATE_CHECKLIST.md")

        point9_required = (
            "compact full-width",
            "compact full-width work rows/bands",
            "point9_large_card_component_count == 0",
            "point9_vertically_stretched_row_count == 0",
        )
        if not all(token in visual + "\n" + composition + "\n" + gate for token in point9_required):
            print("❌ point 9 can regress from Friday compact priority rows to large generic cards")
            ok = False

        point6_required = (
            "Dependency / blocker relationship map — mandatory",
            "visible directional connector(s)",
            "point6_relational_dependency_rendered_as_unconnected_cards_count == 0",
            "point6_missing_directional_connector_count == 0",
        )
        if not all(token in detail + "\n" + gate for token in point6_required):
            print("❌ point 6 can regress from blocker/dependency map to unrelated cards")
            ok = False
    except Exception as exc:
        print(f"❌ Friday special-layout inspection failed: {exc}")
        ok = False
    checks.append(result(
        ok,
        "timeline/blocker/priority special layouts remain semantically distinct from ordinary cards",
        "special meeting-point layouts can be flattened into the ordinary card grid",
    ))

    print("\nINVARIANT 30: Project-Specific Ordinary Card Geometry")
    ok = True
    try:
        for project_id, entry in active.items():
            manifest = entry.get("manifest")
            if not manifest or not os.path.exists(manifest):
                continue
            manifest_text = read_text(manifest)
            match = re.search(
                r"""presentation:\s*.*?authority:\s*.*?path:\s*["']?([^"'\n]+)""",
                manifest_text,
                re.S,
            )
            if not match:
                continue
            authority_path = match.group(1).strip()
            if not os.path.exists(authority_path):
                print(f"❌ {project_id}: presentation authority missing: {authority_path}")
                ok = False
                continue
            project_text = read_text(authority_path)
            if "stable SIX-SLOT geometry" not in project_text:
                continue
            required = (
                "3 columns × 2 rows",
                "stable SIX-SLOT geometry",
                "ordinary card page not preserving the 3×2 six-slot geometry",
            )
            if not all(token in project_text for token in required):
                print(f"❌ {project_id}: fixed-slot presentation geometry is incomplete")
                ok = False
            stale = ("2 columns × 3 rows", "2×3 six-slot geometry")
            if any(token in project_text for token in stale):
                print(f"❌ {project_id}: stale 2×3 fixed-slot geometry remains active")
                ok = False
    except Exception as exc:
        print(f"❌ project-specific card geometry inspection failed: {exc}")
        ok = False
    checks.append(result(
        ok,
        "project-specific fixed-slot card contracts preserve their registered 3×2 geometry",
        "a project-specific fixed-slot card contract can silently regress",
    ))

    print("\nINVARIANT 31: Deterministic Context Placement Governance")
    ok = True
    try:
        registry = read_text("CONTEXT_REGISTRY.yaml")
        routing = read_text("_ai_guides/context/CONTEXT_ROUTING.yaml")
        placement = read_text("_ai_guides/context/CONTEXT_PLACEMENT_CONTRACT.yaml")
        readme = read_text("README.md")

        required_registry = (
            "context_placement:",
            "_ai_guides/context/CONTEXT_PLACEMENT_CONTRACT.yaml",
            "context_ingestion:",
            "emit a user-visible placement receipt before canonical mutation",
        )
        if not all(token in registry for token in required_registry):
            print("❌ context registry does not register the exact-placement contract/task")
            ok = False

        required_routing = (
            "split mixed input into atomic information units",
            "resolve exact canonical owner + exact file through CONTEXT_PLACEMENT_CONTRACT",
            "emit placement receipt to user",
        )
        if not all(token in routing for token in required_routing):
            print("❌ context router can write without exact placement resolution")
            ok = False

        required_contract = (
            "Placement hierarchy",
            "Atomic-information rule",
            "Destination matrix",
            "New capability gate",
            "Placement receipt — mandatory before mutation",
            "Clarification gate",
            "Propagation contract",
            "canonical_write_without_exact_owner_count > 0",
            "canonical_write_without_exact_target_count > 0",
            "mixed_input_unsplit_count > 0",
            "new_canonical_file_unregistered_count > 0",
            "placement_receipt_missing_before_canonical_mutation_count > 0",
        )
        if not all(token in placement for token in required_contract):
            print("❌ exact-placement contract is missing deterministic ownership/routing protections")
            ok = False

        readme_required = (
            "CONTEXT_PLACEMENT_CONTRACT.yaml",
            "Mixed user text is split into separate information units before routing.",
            "exact target file",
        )
        if not all(token in readme for token in readme_required):
            print("❌ repository entrypoint does not explain deterministic placement behavior")
            ok = False

    except Exception as exc:
        print(f"❌ context placement governance inspection failed: {exc}")
        ok = False

    checks.append(result(
        ok,
        "new information resolves scope, semantic owner, exact target and propagation before canonical writes",
        "AI can still place new context ambiguously or create unregistered canonical destinations",
    ))

    print("\nINVARIANT 32: Project Context Isolation")
    ok = True
    try:
        text_extensions = {
            ".md", ".yaml", ".yml", ".json", ".html", ".txt", ".py", ".js",
            ".jsx", ".ts", ".tsx", ".css", ".scss", ".toml", ".ini", ".cfg"
        }

        for project_id, entry in active.items():
            manifest = entry.get("manifest")
            if not manifest or not os.path.exists(manifest):
                continue

            manifest_text = read_text(manifest)
            marker_match = re.search(
                r"""isolation_markers:\s*\n\s*path:\s*["']?([^"'\n]+)""",
                manifest_text,
                re.S,
            )
            if not marker_match:
                print(f"❌ {project_id}: active project manifest has no context.isolation_markers.path")
                ok = False
                continue

            marker_path = marker_match.group(1).strip()
            if not os.path.exists(marker_path):
                print(f"❌ {project_id}: isolation marker file missing: {marker_path}")
                ok = False
                continue

            marker_text = read_text(marker_path)
            root_match = re.search(r"""^project_root:\s*["']?([^"'\n]+)""", marker_text, re.M)
            if not root_match:
                print(f"❌ {project_id}: isolation marker file has no project_root")
                ok = False
                continue
            project_root = root_match.group(1).strip().rstrip("/")

            markers = []
            in_markers = False
            for line in marker_text.splitlines():
                stripped = line.strip()
                if stripped == "markers:":
                    in_markers = True
                    continue
                if in_markers:
                    if line and not line.startswith(" "):
                        break
                    if stripped.startswith("- "):
                        marker = quoted_value(stripped[2:])
                        if marker:
                            markers.append(marker)

            allowed_paths = set()
            in_allowed = False
            for line in marker_text.splitlines():
                stripped = line.strip()
                if stripped == "allowed_outside_project_root:":
                    in_allowed = True
                    continue
                if in_allowed:
                    if line and not line.startswith(" "):
                        break
                    if stripped.startswith("- path:"):
                        allowed_paths.add(quoted_value(stripped.split("path:", 1)[1]))

            if not markers:
                print(f"❌ {project_id}: isolation marker list is empty")
                ok = False
                continue

            leaks = []
            for root, dirs, files in os.walk("."):
                rel_root = root[2:] if root.startswith("./") else root
                if rel_root == ".git" or rel_root.startswith(".git/"):
                    dirs[:] = []
                    continue
                if rel_root == project_root or rel_root.startswith(project_root + "/"):
                    dirs[:] = []
                    continue

                for name in files:
                    rel = os.path.join(rel_root, name).replace(os.sep, "/")
                    if rel.startswith("./"):
                        rel = rel[2:]
                    if rel in allowed_paths:
                        continue
                    ext = os.path.splitext(name)[1].lower()
                    if ext not in text_extensions:
                        continue
                    try:
                        text_value = read_text(rel)
                    except (UnicodeDecodeError, OSError):
                        continue
                    for marker in markers:
                        if marker and marker in text_value:
                            leaks.append((rel, marker))

            if leaks:
                for rel, marker in sorted(set(leaks)):
                    print(f"❌ {project_id}: project marker leaked outside project root: {marker!r} in {rel}")
                ok = False

            # Project-specific binary assets must also remain under project_root.
            # The marker file may name known project asset filenames; path-level
            # leakage is caught by scanning repository paths, not binary contents.
            tree_paths = []
            for root, dirs, files in os.walk("."):
                rel_root = root[2:] if root.startswith("./") else root
                if rel_root == ".git" or rel_root.startswith(".git/"):
                    dirs[:] = []
                    continue
                if rel_root == project_root or rel_root.startswith(project_root + "/"):
                    dirs[:] = []
                    continue
                for name in files:
                    rel = os.path.join(rel_root, name).replace(os.sep, "/")
                    if rel.startswith("./"):
                        rel = rel[2:]
                    tree_paths.append(rel)

            for marker in markers:
                if "." not in marker:
                    continue
                for rel in tree_paths:
                    if marker in rel and rel not in allowed_paths:
                        print(f"❌ {project_id}: project asset/path marker leaked outside project root: {marker!r} in {rel}")
                        ok = False

    except Exception as exc:
        print(f"❌ project-context isolation inspection failed: {exc}")
        ok = False

    checks.append(result(
        ok,
        "project-owned markers, examples, facts and assets stay under each project root",
        "project-specific context can still leak into global instructions, data, docs, audits or assets",
    ))

    print("\nINVARIANT 33: Safe Path Migration Governance")
    ok = True
    try:
        registry = read_text("CONTEXT_REGISTRY.yaml")
        placement = read_text("_ai_guides/context/CONTEXT_PLACEMENT_CONTRACT.yaml")
        migration = read_text("_ai_guides/context/PATH_MIGRATION_PLAN.yaml")
        template = read_text("projects/_template/PROJECT.yaml")

        required_registry = (
            "path_migration:",
            "_ai_guides/context/PATH_MIGRATION_PLAN.yaml",
            "path_change_process:",
            'authority: "_ai_guides/context/PATH_MIGRATION_PLAN.yaml"',
            "decision_records:",
            "context.decisions.records.path",
        )
        if not all(token in registry for token in required_registry):
            print("❌ registry does not fully route migration governance or project decision records")
            ok = False

        required_placement = (
            "## Path migration authority",
            "PATH_MIGRATION_PLAN.yaml",
            "A path-migration receipt is mandatory before mutation",
        )
        if not all(token in placement for token in required_placement):
            print("❌ placement contract does not delegate moves to the migration authority")
            ok = False

        required_plan = (
            "A move is a dependency migration, not a filesystem operation.",
            "## Phase 1 — Preflight",
            "## Phase 2 — Consumer discovery",
            "## Phase 3 — Destination creation",
            "## Phase 4 — Routing and consumer update",
            "## Phase 5 — Stale-path verification",
            "## Phase 6 — Delete old source",
            "unresolved_consumer_count == 0",
            "stale_active_old_path_reference_count == 0",
            "manifest_registry_target_missing_count == 0",
            "consumer_render_scope_changed_unintentionally_count == 0",
            "post_move_integrity_failure_count == 0",
        )
        if not all(token in migration for token in required_plan):
            print("❌ migration plan is missing one or more preflight/update/delete safety gates")
            ok = False

        required_template = (
            'authority: "_ai_guides/context/PATH_MIGRATION_PLAN.yaml"',
            "decisions:",
            "index:",
            "records:",
        )
        if not all(token in template for token in required_template):
            print("❌ reusable project template cannot express safe migrations and exact decision paths")
            ok = False

        # Every active project that declares decisions must expose a records path.
        for project_id, entry in active.items():
            manifest = entry.get("manifest")
            if not manifest or not os.path.exists(manifest):
                continue
            manifest_text = read_text(manifest)
            if "decisions:" in manifest_text:
                if not re.search(
                    r"""decisions:\s*.*?records:\s*\n\s*path:\s*["']?([^"'\n]+)""",
                    manifest_text,
                    re.S,
                ):
                    print(f"❌ {project_id}: decisions capability lacks context.decisions.records.path")
                    ok = False

    except Exception as exc:
        print(f"❌ path migration governance inspection failed: {exc}")
        ok = False

    checks.append(result(
        ok,
        "moves/renames require preflight, consumer propagation, stale-path cleanup and post-move validation",
        "repository paths can still be moved without updating all affected consumers",
    ))

    passed = sum(bool(x) for x in checks)
    print("\n" + "=" * 80)
    print("FINAL AUDIT RESULT")
    print("=" * 80)
    if all(checks):
        print(f"✅ {passed}/{len(checks)} INVARIANTS PASS")
        print("STATUS: READY FOR SMOKE TEST")
        return 0
    print(f"❌ {passed}/{len(checks)} INVARIANTS PASS")
    print("STATUS: AUDIT FAILED — resolve issues before smoke test")
    return 1


if __name__ == "__main__":
    sys.exit(main())
