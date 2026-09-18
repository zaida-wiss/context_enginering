# Data

This directory is the canonical home for repository-held data and source registries.

## Canonical source registry

- `SOURCES.yaml` — machine-readable registry for live/external sources, IDs, access methods and fallback order.
- `SOURCES.md` — human-readable guide to the registry.

## Data categories

Repository-held data is grouped by role:

- `manual/` — manually entered source material when no live source exists.
- `snapshots/` — explicit point-in-time captures.
- `derived/` — reproducible data calculated from registered sources.

Live facts should stay connected to APIs, GitHub, Google Drive or another registered live source whenever possible. Instruction files reference source IDs instead of copying live facts.
