---
project: avanza
type: project_presentation_authority
version: 1.0
status: active
scope: projects/avanza/presentation
---

# Point 6 Dependency Layout — readable special structure

This file owns the Avanza-specific readable layout rule for meeting point ⑥
`Blockers och beroenden`.

## Purpose

Point ⑥ is a dependency/blocker map. It is not an ordinary 3×2 card page.
The slide must make direction and consequence readable in the meeting room.

## Node content budget

Each dependency node may contain only:

1. status chip with symbol + text, e.g. `🔴 Kritisk`, `🟠 Viktig`, `🟢 Stabil`;
2. one short title line;
3. one short consequence/action sentence;
4. one quiet metadata line when useful.

If a node needs more than this, the renderer must either shorten the wording or
paginate to an additional ⑥ continuation slide. It must not shrink text or stack
multiple text blocks on top of each other.

## Minimum sizes

- node title: 18 pt minimum, 20 pt preferred;
- node body: 15 pt minimum, 16 pt preferred;
- node metadata: 12 pt minimum;
- node width must be at least 25% of slide width;
- node height must be measured from the text before placing connectors.

## Layout rule

Use a spacious map with 3-5 nodes per physical slide. Prefer two horizontal
lanes or a left-to-right flow. Connectors are drawn behind nodes and must enter
node edges, not cross text.

Allowed examples:

```text
[Beslut/auth] ──> [API-kontrakt] ──> [Frontend-integration]
        └──────> [Native-kontrakt]
```

or two lanes:

```text
Frontend/auth  ──> Backend/API ──> Demo/CTO
Native-kontrakt ─────────────────────┘
```

## Fail conditions

Point ⑥ fails render review if:
- any node text overlaps another text run;
- any title/body line is visually unreadable at normal slide view;
- connectors cross through labels;
- more than five nodes are forced onto one slide;
- a node contains AI/framework instructions instead of Avanza project content;
- criticality is shown only by color without text/symbol.
