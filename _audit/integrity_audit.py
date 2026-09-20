#!/usr/bin/env python3
"""
Repository Integrity Audit — project-aware mechanical context validation

Validates:
1. PROJECTS.yaml discovers active project manifests without hardcoded project IDs.
2. Every active project manifest exists and its registered context paths resolve.
3. Every project source registry has present, matching, unique source IDs.
4. Source fallback access methods are compatible when an allowed-method contract exists.
5. Presentation acquisition delegates source-access ownership to project-resolved sources.
6. Required global bootstrap files exist without requiring legacy project copies.
7. Every canonical path registered in CONTEXT_REGISTRY exists.
8. Logical references used by task bundles and the global project router resolve.
9. Global routing/validation does not require legacy project-owned source/roster paths.

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


def parse_project_registry():
    text = read_text("PROJECTS.yaml")
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

        if "source_id:" in stripped and not stripped.startswith("- source_id:"):
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
        ok = bool(active) and all(v.get("manifest") for v in active.values())
        checks.append(result(ok, f"{len(active)} active project manifest(s) discovered", "active projects/manifests could not be resolved"))
    except Exception as exc:
        active = {}
        checks.append(result(False, "", f"PROJECTS.yaml parse failed: {exc}"))

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
        match = re.search(r"context:\s*.*?sources:\s*\n\s*path:\s*[\\"']?([^\\"'\n]+)", manifest_text, re.S)
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
