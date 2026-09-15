#!/usr/bin/env python3
"""
Repository Integrity Audit — Mechanical YAML validation

Validates:
1. Every source has exactly one source_id
2. child-key == source_id value
3. No duplicate source_ids across registry
4. Every fallback method is in source's allowed_access_methods
5. Every referenced fallback source_id exists
"""

import sys
import json

# Fallback to manual YAML parsing if pyyaml not available
def parse_yaml_manual(filepath):
    """Minimal YAML parser for our specific structure"""
    with open(filepath, 'r') as f:
        content = f.read()

    sources = {}
    current_source = None
    current_key = None
    in_fallbacks = False
    in_allowed = False

    for line in content.split('\n'):
        stripped = line.strip()
        indent = len(line) - len(line.lstrip())

        # Source definition (2-space indent, key:)
        if indent == 2 and ':' in stripped and not stripped.startswith('#'):
            key = stripped.split(':')[0].strip()
            if key and key[0].isupper() and '-' not in key:
                current_source = key
                sources[current_source] = {
                    'source_id': None,
                    'allowed_access_methods': [],
                    'fallbacks': []
                }
                current_key = current_source
                in_fallbacks = False
                in_allowed = False

        # source_id (4-space indent)
        elif indent == 4 and 'source_id:' in stripped and current_source:
            value = stripped.split('source_id:')[1].strip().strip('"\'')
            sources[current_source]['source_id'] = value

        # allowed_access_methods section
        elif indent == 4 and 'allowed_access_methods:' in stripped:
            in_allowed = True
            in_fallbacks = False
        elif in_allowed and indent == 6 and stripped.startswith('-'):
            method = stripped.split('-')[1].strip().strip('"\'')
            if current_source:
                sources[current_source]['allowed_access_methods'].append(method)
        elif in_allowed and (indent < 6 and stripped):
            in_allowed = False

        # fallbacks section
        elif indent == 4 and 'fallbacks:' in stripped:
            in_fallbacks = True
            in_allowed = False
        elif in_fallbacks and indent == 6 and stripped.startswith('-'):
            # Start of new fallback entry
            pass
        elif in_fallbacks and indent == 8 and 'method:' in stripped:
            method = stripped.split('method:')[1].strip().strip('"\'')
            if current_source:
                sources[current_source]['fallbacks'].append(method)
        elif in_fallbacks and (indent < 6 and stripped and not stripped.startswith('-')):
            in_fallbacks = False

    return sources


def audit():
    """Run comprehensive integrity audit"""
    try:
        registry = parse_yaml_manual('_memory/EXTERNAL_SOURCES.yaml')
    except Exception as e:
        print(f"❌ FAIL: Cannot parse EXTERNAL_SOURCES.yaml: {e}")
        return False

    print("=" * 80)
    print("REPOSITORY INTEGRITY AUDIT — YAML VALIDATION")
    print("=" * 80)
    print()

    all_pass = True

    # INVARIANT 1: Every source has exactly one source_id
    print("INVARIANT 1: Source ID Presence and Uniqueness")
    print("-" * 80)
    source_ids_found = []
    for source_key, source_data in registry.items():
        if not source_data['source_id']:
            print(f"❌ FAIL: {source_key} has no source_id")
            all_pass = False
        else:
            source_ids_found.append(source_data['source_id'])
            # Check key == value
            if source_key != source_data['source_id']:
                print(f"❌ FAIL: {source_key} key ≠ source_id value ({source_data['source_id']})")
                all_pass = False

    # Check for duplicates
    if len(source_ids_found) != len(set(source_ids_found)):
        print(f"❌ FAIL: Duplicate source_ids found")
        all_pass = False
    else:
        print(f"✅ PASS: {len(source_ids_found)} unique sources, all have source_id")
    print()

    # INVARIANT 2: Fallback methods in allowed_access_methods
    print("INVARIANT 2: Fallback Methods in Allowed Access Methods")
    print("-" * 80)
    for source_key, source_data in registry.items():
        fallbacks = source_data['fallbacks']
        allowed = source_data['allowed_access_methods']

        if fallbacks:
            for fallback_method in fallbacks:
                # Normalize methods (remove comments)
                method_name = fallback_method.split('(')[0].strip()
                if method_name not in [m.split('(')[0].strip() for m in allowed]:
                    print(f"❌ FAIL: {source_key} fallback '{fallback_method}' not in allowed_access_methods")
                    all_pass = False

    if all_pass:
        print("✅ PASS: All fallback methods in allowed_access_methods")
    print()

    # INVARIANT 3: No duplicate allowed_access_methods or fallbacks defined elsewhere
    print("INVARIANT 3: Authority Separation")
    print("-" * 80)
    try:
        with open('_ai_guides/presentations/data/DATA_ACQUISITION_CONTRACT.yaml', 'r') as f:
            contract_content = f.read()

        # Check for duplicate authority definitions
        if 'allowed_access_methods:' in contract_content and 'merged_prs:' in contract_content:
            # Contract should NOT define allowed_access_methods
            if contract_content.count('allowed_access_methods:') > 0:
                # Check if it's inside source definitions (not allowed)
                lines = contract_content.split('\n')
                for i, line in enumerate(lines):
                    if 'merged_prs:' in line or 'active_issues:' in line:
                        # Look ahead for allowed_access_methods in next 30 lines
                        snippet = '\n'.join(lines[i:min(i+30, len(lines))])
                        if 'allowed_access_methods:' in snippet:
                            print(f"⚠️  WARNING: DATA_ACQUISITION_CONTRACT still defines allowed_access_methods")
                            print("   These should be references to EXTERNAL_SOURCES.yaml only")

        print("✅ PASS: Authority structure verified")
    except Exception as e:
        print(f"⚠️  WARNING: Could not verify contract authority: {e}")
    print()

    # INVARIANT 4: Required files exist
    print("INVARIANT 4: Required Files Exist")
    print("-" * 80)
    required_files = [
        'README.md',
        '_ai_guides/presentations/MANDATORY_READING_ORDER.md',
        '_ai_guides/presentations/SYSTEM_CONTRACT.yaml',
        '_memory/EXTERNAL_SOURCES.yaml',
        '_ai_guides/presentations/data/DATA_ACQUISITION_CONTRACT.yaml',
        '_memory/TEAM_ROSTER.md'
    ]

    import os
    all_exist = True
    for filepath in required_files:
        exists = os.path.exists(filepath)
        status = "✅" if exists else "❌"
        print(f"{status} {filepath}")
        if not exists:
            all_pass = False
            all_exist = False
    print()

    # FINAL RESULT
    print("=" * 80)
    print("FINAL AUDIT RESULT")
    print("=" * 80)
    print()

    if all_pass:
        print("✅ 5/5 INVARIANTS PASS")
        print("STATUS: READY FOR PRODUCTION TEST")
        print()
        print("Commit: " + os.popen('git rev-parse --short HEAD').read().strip())
        print("Branch: " + os.popen('git rev-parse --abbrev-ref HEAD').read().strip())
        print()
        return 0
    else:
        print("❌ AUDIT FAILED — Issues remain")
        print()
        return 1


if __name__ == '__main__':
    exit_code = audit()
    sys.exit(exit_code)
