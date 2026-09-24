# Repository instructions for GitHub Copilot

Treat `AGENTS.md` as the cross-agent entry map and `README.md` as the repository task router.

- Load `_ai_guides/AI_FRAMEWORK.yaml` before material repository work.
- Resolve task dependencies through `CONTEXT_REGISTRY.yaml`; resolve project-specific context through `PROJECTS.yaml`.
- Keep all internal reads on the task's selected ref.
- Retrieve only the context needed for the task; do not duplicate authority content in this file.
- Before a durable repository change, identify the semantic owner and follow the placement/conflict rules already registered by the repository.
- Prefer small reviewable changes and run the relevant registered validation before considering work complete.
- Separate verified repository facts from inference or recommendation.
- For presentation tasks, start at `_ai_guides/presentations/MANDATORY_READING_ORDER.md`.
