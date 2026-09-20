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
        fixture_sources_text = read_text(fixture_sources)\n        no_named_project_leak = "projects/" not in fixture_text.replace("_audit/fixtures/project_b/", "") and "projects/" not in fixture_sources_text
        ok = (
            set(simulated_active) == {"project_b"}
            and simulated_active["project_b"]["manifest"] == fixture_manifest
            and fixture_paths == [fixture_sources]
            and all(os.path.exists(path.rstrip("/")) for path in fixture_paths)
            and fixture_source_data.get("PRIMARY_REPOSITORY", {}).get("source_id") == "PRIMARY_REPOSITORY"
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
            "#15182E",
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
        required = (
            "Full source labels are rendered once in the physical slide's reserved source margin/footer.",
            "slide source margin/footer deduplicates every source symbol used",
            "slide_margin_source_full_label_missing_count == 0",
            "inline_symbol_slide_margin_source_mismatch_count == 0",
            "physical slide margin/footer deduplicates the used source symbols",
        )
        joined = card + "\n" + gate
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

    print("\nINVARIANT 24: Project-Owned Presentation Geometry")
    ok = True
    try:
        visual = read_text("_ai_guides/presentations/design/VISUAL_DESIGN_MANDATORY.md")
        overflow = read_text("_ai_guides/presentations/monday_meeting/design/LAYOUT_OVERFLOW_GUARD.md")
        avanza = read_text("projects/avanza/presentation/AVANZA_PRESENTATION_SYSTEM.md")
        global_required = (
            "card capacity, slot orientation and pagination are owned by the active project presentation authority",
            "the grid/slot geometry registered by the active project presentation authority",
            "design fidelity is part of fit",
        )
        avanza_required = (
            "2 columns × 3 rows",
            "six positions are spatially reserved",
            "one ordinary card occupies one normal slot",
        )
        joined_global = visual + "\n" + overflow
        if not all(token in joined_global for token in global_required):
            print("❌ global presentation rules can override project-owned card geometry")
            ok = False
        if not all(token in avanza for token in avanza_required):
            print("❌ Avanza presentation authority lost its fixed 2-column × 3-row ordinary-card contract")
            ok = False
        stale_global = (
            "MUST first attempt a six-card `3×2` composition",
            "6 merge cards must first be rendered/tested as 3×2",
        )
        if any(token in joined_global for token in stale_global):
            print("❌ stale global 3×2 rule conflicts with project-owned geometry")
            ok = False
    except Exception as exc:
        print(f"❌ project-owned geometry inspection failed: {exc}")
        ok = False
    checks.append(result(ok, "global layout delegates card geometry while Avanza preserves its fixed 2-column × 3-row contract", "project presentation geometry can be overridden by stale global layout rules"))

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
