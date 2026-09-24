# AGENTS.md — Agent entrypoint

Use this file as a map, not as a second policy system.

## Execution path

1. Read `README.md` from the same branch, tag, or commit ref selected for the task.
2. Load `_ai_guides/AI_FRAMEWORK.yaml`.
3. Resolve the task through `CONTEXT_REGISTRY.yaml`.
4. Resolve a project through `PROJECTS.yaml` when project-specific context is required.
5. Load only the authorities and project context registered for the resolved task.
6. Validate the result with the registered audit, test, or completion gate when one exists.

## Context discipline

- Keep all internal `context_enginering` reads on the selected ref for the entire execution.
- Retrieve the smallest sufficient high-signal context instead of loading the repository indiscriminately.
- Treat repository authorities as the system of record; do not recreate their rules here.
- Re-check live source and connector availability for each new task that depends on them.
- Distinguish verified facts, source evidence, AI reasoning, and recommendations.
- When active authorities genuinely require incompatible outcomes, follow the conflict gate in `AI_FRAMEWORK.yaml` before mutation.

## Change discipline

- Identify the semantic owner before changing durable context or instructions.
- Make the smallest coherent change and update dependent validators when behavior changes.
- Keep project-specific facts and examples under the selected project's registered root.
- Prefer mechanical validation over claims that a change is correct.
- Preserve human decision authority for material architecture choices and genuine conflicts.

## Specialized routes

- Presentation work: `_ai_guides/presentations/MANDATORY_READING_ORDER.md`
- Project work: `_ai_guides/project/PROJECT_CONTEXT_ROUTER.md`
- Context placement: `_ai_guides/context/CONTEXT_PLACEMENT_CONTRACT.yaml`
- Best-practice evidence: `_ai_guides/AI_BEST_PRACTICE_EVIDENCE_POLICY.yaml`

If a route above delegates to another authority, follow that authority rather than expanding this file.
