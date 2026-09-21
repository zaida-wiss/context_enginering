---
project: avanza
type: project_presentation_readability_contract
version: 1.0
status: active
scope: projects/avanza/presentation
---

# Dependency map readability contract

This file specializes Avanza meeting point ⑥ so dependency/blocker diagrams stay readable.

## Ownership

Meeting point ⑥ may use a dependency map only when the diagram can remain readable at meeting scale.

The dependency-map structure owns relationships. It does not own permission to shrink text below the normal card/body readability limits.

## Hard rendering hierarchy

For each dependency node, preserve in this order:

1. criticality chip with symbol + text (`🔴 Kritisk`, `🟠 Viktig`, `🟢 Stabil`)
2. short node title
3. one sentence explaining what is blocked or unlocked
4. explicit team/owner cue using `TEAM_VISUAL_IDENTITY.yaml`
5. connector direction

If all five cannot fit, reduce the number of nodes per physical slide or paginate the dependency map. Do not solve fit by shrinking text until it overlaps.

## Readability requirements

- Each dependency node uses a minimum 18 pt title and 14 pt body text.
- Text boxes inside the same node must never overlap.
- Node titles are short labels, not full paragraphs.
- A connector must never cross text.
- When more than four nodes or three connectors are required, split the map into continuation slides.
- If relationship direction is unclear, render a readable evidence list instead of a graph.

## Failure examples

A render fails if:

- node title and body text overlap;
- text becomes too small to read in PDF or mobile preview;
- connectors pass through labels;
- multiple dependency facts are compressed into one illegible node;
- team identity or criticality is carried only by color.

## Fallback structure

When the map cannot fit, use two physical slides:

1. `✏️ 6. Blockers och beroenden — beroendekarta`
   - maximum four readable nodes
   - only the strongest verified relationships
2. `✏️ 6. Blockers och beroenden — åtgärdslista`
   - one readable card per blocker/action
   - no connector graphics
   - each card states blocker, affected team, consequence, owner/next step and criticality
