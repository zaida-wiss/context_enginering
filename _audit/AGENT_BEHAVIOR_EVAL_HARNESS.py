#!/usr/bin/env python3
"""Execute agent behavior eval cases in isolated subprocess trials.

The harness is provider-neutral: --agent-command identifies an executable that
accepts one JSON request on stdin and returns one JSON object on stdout.

Each case starts a NEW subprocess, so conversation/process state is not reused
between trials. The agent adapter owns model/provider authentication and tool
access. This harness never stores provider secrets.

Agent adapter input:
{
  "case_id": "...",
  "prompt": "...",
  "repository_ref": "dev",
  "required": [...],
  "forbidden": [...]
}

Agent adapter output:
{
  "response_text": "...",
  "repository_ref_used": "dev",
  "sources_or_locations_actually_checked": [...],
  "tool_or_connector_failures_when_material": [...]
}

This harness captures raw evidence only. It does NOT infer semantic criterion
scores from text. Reviewers/graders add explicit criterion scores before the
result is passed to AGENT_BEHAVIOR_EVAL_RUNNER.py.
"""

from __future__ import annotations

import argparse
from datetime import datetime, timezone
import json
from pathlib import Path
import shlex
import subprocess
import sys
from typing import Any

import yaml

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_SPEC = ROOT / "_audit" / "AGENT_BEHAVIOR_EVAL_CASES.yaml"
REQUIRED_AGENT_FIELDS = {
    "response_text",
    "repository_ref_used",
    "sources_or_locations_actually_checked",
    "tool_or_connector_failures_when_material",
}


def load_spec(path: Path) -> dict[str, Any]:
    return yaml.safe_load(path.read_text(encoding="utf-8"))


def run_isolated_trial(
    command: list[str],
    request: dict[str, Any],
    timeout_seconds: int,
) -> dict[str, Any]:
    """Run exactly one case in a new process and parse its JSON evidence."""
    completed = subprocess.run(
        command,
        input=json.dumps(request, ensure_ascii=False),
        text=True,
        capture_output=True,
        timeout=timeout_seconds,
        check=False,
    )
    if completed.returncode != 0:
        raise RuntimeError(
            f"agent command exited {completed.returncode}: "
            f"{completed.stderr.strip() or '<no stderr>'}"
        )
    try:
        result = json.loads(completed.stdout)
    except json.JSONDecodeError as exc:
        raise RuntimeError("agent command stdout was not valid JSON") from exc

    if not isinstance(result, dict):
        raise RuntimeError("agent command must return one JSON object")

    missing = sorted(REQUIRED_AGENT_FIELDS - set(result))
    if missing:
        raise RuntimeError(f"agent result missing fields: {', '.join(missing)}")

    if not isinstance(result["response_text"], str) or not result["response_text"].strip():
        raise RuntimeError("agent result response_text must be non-empty")
    for field in (
        "sources_or_locations_actually_checked",
        "tool_or_connector_failures_when_material",
    ):
        if not isinstance(result[field], list):
            raise RuntimeError(f"agent result {field} must be a list")

    return result


def blank_criteria(case_spec: dict[str, Any]) -> dict[str, dict[str, str]]:
    criteria: dict[str, dict[str, str]] = {}
    for criterion in case_spec.get("required", []):
        criteria[criterion] = {"result": "", "rationale": ""}
    for criterion in case_spec.get("forbidden", []):
        criteria[criterion] = {"result": "", "rationale": ""}
    return criteria


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--agent-command",
        required=True,
        help="Executable command for one isolated agent trial; quote when it has arguments",
    )
    parser.add_argument("--spec", type=Path, default=DEFAULT_SPEC)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--model-or-harness", required=True)
    parser.add_argument("--timeout-seconds", type=int, default=600)
    args = parser.parse_args()

    if args.timeout_seconds <= 0:
        parser.error("--timeout-seconds must be greater than zero")

    command = shlex.split(args.agent_command)
    if not command:
        parser.error("--agent-command must not be empty")

    spec = load_spec(args.spec)
    declared_ref = spec["evaluation_contract"]["repository_ref"]
    cases = spec["cases"]

    output: dict[str, Any] = {
        "metadata": {
            "model_or_harness": args.model_or_harness,
            "run_timestamp": datetime.now(timezone.utc).isoformat(),
            "repository_ref": declared_ref,
            "execution_mode": "fresh_subprocess_per_case",
            "scoring_status": "pending_explicit_grading",
        },
        "cases": {},
    }

    for case_id, case_spec in cases.items():
        request = {
            "case_id": case_id,
            "prompt": case_spec["prompt"],
            "repository_ref": declared_ref,
            "required": case_spec.get("required", []),
            "forbidden": case_spec.get("forbidden", []),
        }
        print(f"RUN {case_id}", file=sys.stderr)
        try:
            evidence = run_isolated_trial(command, request, args.timeout_seconds)
        except (RuntimeError, subprocess.TimeoutExpired) as exc:
            print(f"FAIL {case_id}: {exc}", file=sys.stderr)
            return 2

        if evidence["repository_ref_used"] != declared_ref:
            print(
                f"FAIL {case_id}: adapter used ref "
                f"{evidence['repository_ref_used']!r}, expected {declared_ref!r}",
                file=sys.stderr,
            )
            return 2

        output["cases"][case_id] = {
            "case_id": case_id,
            "evidence": evidence,
            "criteria": blank_criteria(case_spec),
        }

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(output, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(f"WROTE {args.output}", file=sys.stderr)
    print(
        "Evidence capture complete. Explicit grading is still required before "
        "AGENT_BEHAVIOR_EVAL_RUNNER.py can pass the suite.",
        file=sys.stderr,
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
