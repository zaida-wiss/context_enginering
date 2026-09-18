#!/usr/bin/env python3
"""
Repository Integrity Audit — mechanical context validation

Validates:
1. Source IDs exist, match their registry key and are unique
2. Source fallback methods are compatible with allowed methods
3. Presentation acquisition delegates source-access ownership
4. Required bootstrap files exist
5. Every canonical path registered in CONTEXT_REGISTRY exists
6. Logical references used by task bundles and project router resolve
7. Retired/moved project logical IDs are not used by the active router
"""

import os
import re
import sys


def read_text(path):
    with open(path, "r", encoding="utf-8") as handle:
        return handle.read()


def read_sources_section():
    """Extract the top-level source registry with lightweight parsing."""
    content = read_text("data/SOURCES.yaml")
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
            if key and key[0].isupper():
                current_source = key
                current_list = None
                sources[current_source] = {
                    "source_id": None,
                    "allowed_access_methods": [],
                    "fallbacks": [],
                }
            continue

        if current_source is None:
            continue

        if "source_id:" in stripped:
            value = stripped.split("source_id:", 1)[1].strip().strip("\"'")
            sources[current_source]["source_id"] = value
            continue

        if stripped == "allowed_access_methods:":
            current_list = "allowed"
            continue

        if stripped == "fallbacks:":
            current_list = "fallbacks"
            continue

        if indent <= 4 and stripped.endswith(":"):
            current_list = None

        if current_list == "allowed" and stripped.startswith("- "):
            method = stripped[2:].strip().strip("\"'")
            if method:
                sources[current_source]["allowed_access_methods"].append(method)
            continue

        if current_list == "fallbacks" and stripped.startswith("- method:"):
            method = stripped.split("method:", 1)[1].strip().strip("\"'")
            if method:
                sources[current_source]["fallbacks"].append(method)

    return sources


def parse_context_registry():
    """
    Parse the simple canonical path shapes from CONTEXT_REGISTRY.yaml.

    Returns:
      logical_ids: logical_destinations.<domain>.<id> -> file path
      registries: registries.<id> -> file path
      all_paths: all path values found in the registry
      registry_text: full text
    """
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
                path_value = stripped.split("path:", 1)[1].strip().strip("\"'")
                logical_ids[f"logical_destinations.{level1}.{level2}"] = path_value
                all_paths.append(path_value)
                continue

        if section == "registries":
            if indent == 2 and stripped.endswith(":"):
                level1 = stripped[:-1]
                continue
            if indent == 4 and stripped.startswith("path:") and level1:
                path_value = stripped.split("path:", 1)[1].strip().strip("\"'")
                registries[f"registries.{level1}"] = path_value
                all_paths.append(path_value)
                continue

        if stripped.startswith("path:"):
            path_value = stripped.split("path:", 1)[1].strip().strip("\"'")
            if path_value:
                all_paths.append(path_value)

    return logical_ids, registries, all_paths, text


def collect_reference_tokens(text):
    """Collect stable logical references embedded in YAML/Markdown text."""
    return set(
        re.findall(
            r"\b(?:logical_destinations\.[A-Za-z0-9_.-]+|registries\.[A-Za-z0-9_.-]+)\b",
            text,
        )
    )


def collect_project_router_ids(text):
    """Collect human-facing shorthand project.<id> references from the router."""
    return set(re.findall(r"\bproject\.([A-Za-z0-9_-]+)\b", text))


def main():
    all_pass = True
    invariant_results = []

    print("=" * 80)
    print("REPOSITORY INTEGRITY AUDIT")
    print("=" * 80)
    print()

    # INVARIANT 1
    print("INVARIANT 1: Source ID Presence and Uniqueness")
    print("-" * 80)
    try:
        sources = read_sources_section()
        source_ids = []
        local_pass = True

        for source_key, source_data in sources.items():
            source_id = source_data["source_id"]
            if not source_id:
                print(f"❌ FAIL: {source_key} has no source_id")
                local_pass = False
                continue

            source_ids.append(source_id)
            if source_key != source_id:
                print(f"❌ FAIL: {source_key} key ≠ source_id value ({source_id})")
                local_pass = False

        duplicates = sorted({x for x in source_ids if source_ids.count(x) > 1})
        if duplicates:
            print(f"❌ FAIL: Duplicate source_ids: {duplicates}")
            local_pass = False

        if local_pass:
            print(f"✅ PASS: {len(source_ids)} unique source IDs")
    except Exception as exc:
        print(f"❌ FAIL: Cannot parse SOURCES.yaml: {exc}")
        local_pass = False

    invariant_results.append(local_pass)
    all_pass &= local_pass
    print()

    # INVARIANT 2
    print("INVARIANT 2: Fallback Methods Respect Allowed Access")
    print("-" * 80)
    local_pass = True
    for source_key, source_data in sources.items():
        allowed = {m.split("(")[0].strip() for m in source_data["allowed_access_methods"]}
        for fallback_method in source_data["fallbacks"]:
            method_name = fallback_method.split("(")[0].strip()
            if method_name and method_name not in allowed:
                print(
                    f"❌ FAIL: {source_key}: fallback '{method_name}' "
                    "not in allowed_access_methods"
                )
                local_pass = False

    if local_pass:
        print("✅ PASS: fallback methods are compatible with allowed access methods")
    invariant_results.append(local_pass)
    all_pass &= local_pass
    print()

    # INVARIANT 3
    print("INVARIANT 3: Source Access Authority Separation")
    print("-" * 80)
    try:
        contract = read_text(
            "_ai_guides/presentations/data/DATA_ACQUISITION_CONTRACT.yaml"
        )
        local_pass = (
            "access_methods_authority:" in contract
            or "source_registry" in contract
            or "SOURCES.yaml" in contract
        )
        if local_pass:
            print("✅ PASS: acquisition contract delegates source-access ownership")
        else:
            print("❌ FAIL: acquisition contract does not expose source authority")
    except Exception as exc:
        print(f"❌ FAIL: cannot inspect acquisition contract: {exc}")
        local_pass = False

    invariant_results.append(local_pass)
    all_pass &= local_pass
    print()

    # INVARIANT 4
    print("INVARIANT 4: Required Bootstrap Files Exist")
    print("-" * 80)
    required_files = [
        "README.md",
        "CONTEXT_REGISTRY.yaml",
        "_ai_guides/project/PROJECT_CONTEXT_ROUTER.md",
        "_ai_guides/presentations/MANDATORY_READING_ORDER.md",
        "_ai_guides/presentations/AUTHORITY_REGISTRY.yaml",
        "_ai_guides/presentations/INTEGRITY_CONSTRAINT.md",
        "_ai_guides/presentations/SYSTEM_CONTRACT.yaml",
        "data/SOURCES.yaml",
        "_memory/TEAM_ROSTER.md",
    ]
    local_pass = True
    for filepath in required_files:
        exists = os.path.exists(filepath)
        print(f"{'✅' if exists else '❌'} {filepath}")
        local_pass &= exists

    invariant_results.append(local_pass)
    all_pass &= local_pass
    print()

    # INVARIANT 5
    print("INVARIANT 5: Registered Canonical Paths Exist")
    print("-" * 80)
    try:
        logical_ids, registries, registered_paths, registry_text = parse_context_registry()
        local_pass = True
        for filepath in sorted(set(registered_paths)):
            # Directory registrations intentionally end with '/'.
            target = filepath.rstrip("/")
            exists = os.path.exists(target)
            if not exists:
                print(f"❌ FAIL: registered path missing: {filepath}")
                local_pass = False

        if local_pass:
            print(f"✅ PASS: {len(set(registered_paths))} registered paths resolve")
    except Exception as exc:
        print(f"❌ FAIL: cannot parse CONTEXT_REGISTRY.yaml: {exc}")
        local_pass = False
        logical_ids, registries, registry_text = {}, {}, ""

    invariant_results.append(local_pass)
    all_pass &= local_pass
    print()

    # INVARIANT 6
    print("INVARIANT 6: Task and Router Logical References Resolve")
    print("-" * 80)
    local_pass = True

    known_refs = set(logical_ids) | set(registries)
    registry_refs = collect_reference_tokens(registry_text)

    unresolved_registry_refs = sorted(ref for ref in registry_refs if ref not in known_refs)
    for ref in unresolved_registry_refs:
        print(f"❌ FAIL: unresolved registry/task ref: {ref}")
        local_pass = False

    try:
        router_text = read_text("_ai_guides/project/PROJECT_CONTEXT_ROUTER.md")
        project_ids = collect_project_router_ids(router_text)
        known_project_ids = {
            ref.split(".", 2)[2]
            for ref in logical_ids
            if ref.startswith("logical_destinations.project.")
        }

        unresolved_router = sorted(project_ids - known_project_ids)
        for item in unresolved_router:
            print(f"❌ FAIL: unresolved router shorthand: project.{item}")
            local_pass = False
    except Exception as exc:
        print(f"❌ FAIL: cannot inspect project router: {exc}")
        local_pass = False

    if local_pass:
        print("✅ PASS: task and project-router logical references resolve")

    invariant_results.append(local_pass)
    all_pass &= local_pass
    print()

    # INVARIANT 7
    print("INVARIANT 7: Retired Project Logical IDs Are Not Active")
    print("-" * 80)
    retired_project_ids = {
        "definition_of_done_template",
    }

    local_pass = True
    try:
        router_text = read_text("_ai_guides/project/PROJECT_CONTEXT_ROUTER.md")
        registry_text = read_text("CONTEXT_REGISTRY.yaml")

        for retired in sorted(retired_project_ids):
            patterns = [
                f"project.{retired}",
                f"logical_destinations.project.{retired}",
            ]
            for pattern in patterns:
                if pattern in router_text or pattern in registry_text:
                    print(f"❌ FAIL: retired logical ID still active: {pattern}")
                    local_pass = False

        if local_pass:
            print("✅ PASS: no retired project logical IDs are active")
    except Exception as exc:
        print(f"❌ FAIL: retired-ID check failed: {exc}")
        local_pass = False

    invariant_results.append(local_pass)
    all_pass &= local_pass
    print()

    # FINAL RESULT
    passed = sum(1 for result in invariant_results if result)
    total = len(invariant_results)

    print("=" * 80)
    print("FINAL AUDIT RESULT")
    print("=" * 80)
    print()

    if all_pass:
        print(f"✅ {passed}/{total} INVARIANTS PASS")
        print("STATUS: READY FOR SMOKE TEST")
        try:
            commit = os.popen("git rev-parse --short HEAD").read().strip()
            branch = os.popen("git rev-parse --abbrev-ref HEAD").read().strip()
            if commit:
                print(f"Commit: {commit}")
            if branch:
                print(f"Branch: {branch}")
        except Exception:
            pass
        return 0

    print(f"❌ {passed}/{total} INVARIANTS PASS")
    print("STATUS: AUDIT FAILED — resolve issues before smoke test")
    return 1


if __name__ == "__main__":
    sys.exit(main())
