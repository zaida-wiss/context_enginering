# Frontend AI Instructions

This file defines **generic frontend-assistance routing** for projects registered in this context-engineering repository.

It does not own project-specific components, branding, thresholds, framework choices or coding-language requirements.

---

## Frontend request flow

For frontend assistance:

1. Read this file.
2. Resolve the selected project through `PROJECTS.yaml → selected project → PROJECT.yaml`.
3. Load the project's registered design context from `PROJECT.yaml → context.design.*` when present and relevant.
4. Resolve workflow/code standards through `CONTEXT_REGISTRY.yaml` and the active project/repository configuration.
5. Verify referenced assets before claiming they were inspected.
6. Separate:
   - verified project requirements,
   - visually verified details,
   - historical/documented context,
   - AI recommendations.

If no project is selected, do not silently use another project's frontend rules.

---

## Technology and code rules

Do not invent a mandatory language, framework, styling system or architecture.

Resolve technology requirements in this order:

1. actual project repository configuration (compiler, package manifest, formatter/linter, framework configuration)
2. registered external/course/customer requirements
3. documented project/team decisions
4. framework/language conventions as recommendations

Examples such as TypeScript, React, CSS Modules, JavaScript or another stack are binding only when the selected project's verified context establishes them.

Never promote a recommendation or historical example to a project rule.

---

## Design authority

Use the selected project's registered design context.

A design document may contain both current requirements and historical context. Preserve that distinction.

If a document references an image/mockup asset:

- verify that the asset actually exists before describing it as visually inspected;
- when the asset is missing, use only what the documentation itself establishes;
- do not infer colours, spacing, layout, interaction or component details from a missing image;
- surface uncertainty when a requirement cannot be verified.

Project-specific components, brand colours, business thresholds and UI rules belong under `projects/<project>/...`, not in this generic guide.

---

## Accessibility and usability

Treat accessibility requirements from the selected project, registered external requirements and applicable framework authorities as requirements.

When no project-specific rule exists, recommend accessible frontend practice without presenting the recommendation as a confirmed project decision.

Do not reduce readability or accessibility merely to imitate an unverified visual reference.

---

## Response structure

Adapt the answer to the user's task rather than forcing one fixed template.

For implementation help, normally make clear:

- what is verified by project context;
- what code/configuration establishes the technology choice;
- the implementation or debugging guidance;
- relevant acceptance/testing considerations;
- any uncertainty caused by unavailable sources/assets.

Use project standards through their registered logical paths instead of embedding project-specific rules here.

---

## Before answering

Check that:

- [ ] the correct project was selected;
- [ ] relevant design context was resolved through its project manifest;
- [ ] referenced assets were verified before visual claims were made;
- [ ] project facts are not being taken from another project;
- [ ] technology requirements are backed by configuration, requirement or decision;
- [ ] historical context is not being presented as a current mandatory rule;
- [ ] AI recommendations are distinguishable from verified requirements;
- [ ] relevant accessibility, testing and Definition-of-Done concerns are considered.

---

## When information is incomplete

If a missing source or asset prevents a required claim, follow the repository's source/integrity rules.

Do not guess.

A missing visual asset does not erase preserved textual design context; it only limits what can truthfully be claimed from the image itself.

---

**Version:** 2.0  
**Last updated:** 2026-09-20  
**Status:** ACTIVE — generic project-resolved frontend guidance
