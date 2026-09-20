# Data

This directory is a generic domain for repository-held data that is not owned by one selected project.

## Project-specific source registries

Project-specific live/external source registries resolve through:
`PROJECTS.yaml → selected project → PROJECT.yaml → context.sources.path`.

Do not add a global project source registry here. Project facts and project-owned manual data belong under the corresponding `projects/<project>/` root.

## Generic data categories

When genuinely cross-project data is needed, it may be grouped by role:

- `manual/` — manually entered generic source material when no live source exists.
- `snapshots/` — explicit generic point-in-time captures.
- `derived/` — reproducible generic data calculated from registered sources.

Live facts should stay connected to registered live sources whenever possible. Instruction files should resolve project-owned source IDs through the selected project manifest rather than copying live facts.
