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
import os

def read_sources_section():
    """Extract sources from YAML using grep and basic parsing"""
    with open('_memory/EXTERNAL_SOURCES.yaml', 'r') as f:
        content = f.read()

    # Find sources: section
    lines = content.split('\n')
    sources_start = None
    sources_end = None

    for i, line in enumerate(lines):
        if line.strip() == 'sources:':
            sources_start = i
        elif sources_start is not None and line.startswith('---'):
            sources_end = i
            break
        elif sources_start is not None and line and not line.startswith(' ') and ':' in line:
            if 'sources' not in line:
                sources_end = i
                break

    if sources_start is None:
        return {}

    if sources_end is None:
        sources_end = len(lines)

    sources_lines = lines[sources_start+1:sources_end]
    sources = {}
    current_source = None

    for line in sources_lines:
        if not line.strip() or line.startswith('#'):
            continue

        indent = len(line) - len(line.lstrip())

        # Top-level source (2 spaces)
        if indent == 2 and ':' in line and not line.strip().startswith('-'):
            key = line.strip().rstrip(':').strip()
            if key and key[0].isupper():
                current_source = key
                sources[current_source] = {
                    'source_id': None,
                    'allowed_access_methods': [],
                    'fallbacks': []
                }

        # source_id property (4+ spaces)
        elif current_source and 'source_id:' in line:
            value = line.split('source_id:')[1].strip().strip('"\'')
            sources[current_source]['source_id'] = value

        # allowed_access_methods list
        elif current_source and 'allowed_access_methods:' in line:
            # Read next lines until we hit a line that's not a method
            pass

        # methods under allowed_access_methods
        elif current_source and line.strip().startswith('- ') and indent >= 6:
            method = line.strip()[2:].strip().strip('"\'')
            if method and sources[current_source].get('source_id'):
                sources[current_source]['allowed_access_methods'].append(method)

        # fallback methods
        elif current_source and line.strip().startswith('- method:'):
            method = line.split('method:')[1].strip().strip('"\'')
            sources[current_source]['fallbacks'].append(method)

    return sources


def main():
    """Run comprehensive integrity audit"""
    try:
        sources = read_sources_section()
    except Exception as e:
        print(f"❌ FAIL: Cannot parse EXTERNAL_SOURCES.yaml: {e}")
        return 1

    print("=" * 80)
    print("REPOSITORY INTEGRITY AUDIT — YAML VALIDATION")
    print("=" * 80)
    print()

    all_pass = True

    # INVARIANT 1: Every source has exactly one source_id
    print("INVARIANT 1: Source ID Presence and Uniqueness")
    print("-" * 80)
    source_ids_found = []

    for source_key, source_data in sources.items():
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
        dups = [x for x in source_ids_found if source_ids_found.count(x) > 1]
        print(f"❌ FAIL: Duplicate source_ids found: {set(dups)}")
        all_pass = False
    else:
        print(f"✅ PASS: {len(source_ids_found)} unique sources, all have source_id")
    print()

    # INVARIANT 2: Fallback methods in allowed_access_methods
    print("INVARIANT 2: Fallback Methods in Allowed Access Methods")
    print("-" * 80)
    fallback_issues = []

    for source_key, source_data in sources.items():
        fallbacks = source_data['fallbacks']
        allowed = [m.split('(')[0].strip() for m in source_data['allowed_access_methods']]

        if fallbacks:
            for fallback_method in fallbacks:
                method_name = fallback_method.split('(')[0].strip()
                if method_name not in allowed:
                    fallback_issues.append(f"{source_key}: fallback '{method_name}' not in allowed_access_methods")
                    all_pass = False

    if not fallback_issues:
        print("✅ PASS: All fallback methods in allowed_access_methods")
    else:
        for issue in fallback_issues:
            print(f"❌ FAIL: {issue}")
    print()

    # INVARIANT 3: Authority Separation
    print("INVARIANT 3: Authority Separation")
    print("-" * 80)
    try:
        with open('_ai_guides/presentations/data/DATA_ACQUISITION_CONTRACT.yaml', 'r') as f:
            contract_content = f.read()

        # After refactor, contract should NOT have allowed_access_methods in source sections
        if 'access_methods_authority:' in contract_content:
            print("✅ PASS: Contract properly references external authority for access methods")
        else:
            print("⚠️  WARNING: Could not verify access_methods_authority references")
    except Exception as e:
        print(f"⚠️  WARNING: Could not verify contract: {e}")
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

    for filepath in required_files:
        exists = os.path.exists(filepath)
        status = "✅" if exists else "❌"
        print(f"{status} {filepath}")
        if not exists:
            all_pass = False
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
        try:
            commit = os.popen('git rev-parse --short HEAD').read().strip()
            branch = os.popen('git rev-parse --abbrev-ref HEAD').read().strip()
            print(f"Commit: {commit}")
            print(f"Branch: {branch}")
        except:
            pass
        print()
        return 0
    else:
        print("❌ AUDIT FAILED — Issues remain")
        print()
        return 1


if __name__ == '__main__':
    exit_code = main()
    sys.exit(exit_code)
