#!/usr/bin/env python3
"""Validate and summarize fresh-session agent behavior evaluation results.

This runner is intentionally harness-agnostic. A model/tool harness executes the
prompts from AGENT_BEHAVIOR_EVAL_CASES.yaml and writes one JSON result per case.
This script validates that evidence and scoring are complete and reports the
suite outcome. It never infers a behavioral pass from response text alone.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys

import yaml

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_SPEC = ROOT / "_audit" / "AGENT_BEHAVIOR_EVAL_CASES.yaml"

VALID_RESULTS = {"pass", "fail", "not_applicable"}
REQUIRED_EVIDENCE = {
    "response_text",
    "repository_ref_used",
    "sources_or_locations_actually_checked",
    "tool_or_connector_failures_when_material",
}


def load_yaml(path: Path) -> dict:
    return yaml.safe_load(path.read_text(encoding="utf-8"))


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def validate_case(case_id: str, case_spec: dict, result: dict, declared_ref: str) -> list[str]:
    failures: list[str] = []

    if result.get("case_id") != case_id:
        failures.append(f"{case_id}: case_id mismatch")

    evidence = result.get("evidence")
    if not isinstance(evidence, dict):
        failures.append(f"{case_id}: evidence must be an object")
        evidence = {}

    missing_evidence = sorted(REQUIRED_EVIDENCE - set(evidence))
    if missing_evidence:
        failures.append(f"{case_id}: missing evidence fields: {', '.join(missing_evidence)}")

    if evidence.get("repository_ref_used") != declared_ref:
        failures.append(
            f"{case_id}: repository_ref_used must be {declared_ref!r}, "
            f"got {evidence.get('repository_ref_used')!r}"
        )

    response = evidence.get("response_text")
    if not isinstance(response, str) or not response.strip():
        failures.append(f"{case_id}: response_text must be non-empty")

    checked = evidence.get("sources_or_locations_actually_checked")
    if not isinstance(checked, list):
        failures.append(f"{case_id}: sources_or_locations_actually_checked must be a list")

    tool_failures = evidence.get("tool_or_connector_failures_when_material")
    if not isinstance(tool_failures, list):
        failures.append(f"{case_id}: tool_or_connector_failures_when_material must be a list")

    scores = result.get("criteria")
    if not isinstance(scores, dict):
        failures.append(f"{case_id}: criteria must be an object")
        scores = {}

    expected = {
        **{criterion: "required" for criterion in case_spec.get("required", [])},
        **{criterion: "forbidden" for criterion in case_spec.get("forbidden", [])},
    }

    missing_scores = sorted(set(expected) - set(scores))
    extra_scores = sorted(set(scores) - set(expected))
    if missing_scores:
        failures.append(f"{case_id}: missing criterion scores: {', '.join(missing_scores)}")
    if extra_scores:
        failures.append(f"{case_id}: unknown criterion scores: {', '.join(extra_scores)}")

    for criterion, kind in expected.items():
        entry = scores.get(criterion)
        if not isinstance(entry, dict):
            continue
        outcome = entry.get("result")
        if outcome not in VALID_RESULTS:
            failures.append(f"{case_id}/{criterion}: invalid result {outcome!r}")
            continue
        rationale = entry.get("rationale")
        if not isinstance(rationale, str) or not rationale.strip():
            failures.append(f"{case_id}/{criterion}: rationale is required")
        if outcome == "fail":
            failures.append(f"{case_id}/{criterion}: {kind} criterion failed")

    return failures


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("results", type=Path, help="JSON file containing fresh-session eval results")
    parser.add_argument("--spec", type=Path, default=DEFAULT_SPEC)
    args = parser.parse_args()

    spec = load_yaml(args.spec)
    payload = load_json(args.results)

    declared_ref = spec["evaluation_contract"]["repository_ref"]
    expected_cases = spec["cases"]
    actual_cases = payload.get("cases")

    failures: list[str] = []
    if not isinstance(actual_cases, dict):
        failures.append("results: cases must be an object")
        actual_cases = {}

    missing_cases = sorted(set(expected_cases) - set(actual_cases))
    extra_cases = sorted(set(actual_cases) - set(expected_cases))
    if missing_cases:
        failures.append(f"results: missing cases: {', '.join(missing_cases)}")
    if extra_cases:
        failures.append(f"results: unknown cases: {', '.join(extra_cases)}")

    metadata = payload.get("metadata")
    if not isinstance(metadata, dict):
        failures.append("results: metadata must be an object")
        metadata = {}
    for field in ("model_or_harness", "run_timestamp", "repository_ref"):
        if not metadata.get(field):
            failures.append(f"results: metadata.{field} is required")
    if metadata.get("repository_ref") != declared_ref:
        failures.append(
            f"results: metadata.repository_ref must be {declared_ref!r}, "
            f"got {metadata.get('repository_ref')!r}"
        )

    for case_id, case_spec in expected_cases.items():
        if case_id in actual_cases:
            failures.extend(validate_case(case_id, case_spec, actual_cases[case_id], declared_ref))

    print("=" * 72)
    print("AGENT BEHAVIOR EVALUATION")
    print("=" * 72)
    print(f"Spec: {args.spec}")
    print(f"Results: {args.results}")
    print(f"Cases expected: {len(expected_cases)}")
    print(f"Cases supplied: {len(actual_cases)}")

    if failures:
        print(f"\nFAIL — {len(failures)} validation/scoring problem(s)")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print("\nPASS — all cases contain complete evidence and passing explicit scores")
    return 0


if __name__ == "__main__":
    sys.exit(main())
