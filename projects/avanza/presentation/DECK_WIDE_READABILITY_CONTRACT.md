---
project: avanza
type: project_render_contract
version: 1.0
status: active
scope: projects/avanza/presentation
---

# Deck-wide Readable Rendering Contract

This contract exists because prior rendered decks passed source-level rules while still producing tiny text and overlapping text in the PDF. It applies to every Avanza meeting slide, not only meeting point 6.

## Core rule

Every delivered Avanza meeting slide must be readable as a PDF screenshot at normal presentation size. No slide may use dense content as a reason to shrink text below the readable minimums or allow overlap.

## Minimum rendered text sizes

For Avanza meeting decks:

- cover title: 40 pt preferred, 36 pt minimum
- meeting-point header: 34 pt preferred, 32 pt minimum
- subtitle: 18 pt preferred, 16 pt minimum
- card/node title: 20 pt preferred, 18 pt minimum
- body text: 16 pt preferred, 15 pt minimum
- metadata/owner/source inside card: 13 pt preferred, 12 pt minimum
- footer/source text: 10 pt preferred, 9 pt minimum

Any generated text below these minima is a render failure unless it is a non-user-facing hidden artifact, which must not be delivered.

## Density rule

The renderer must choose page count over compression.

If text does not fit at the readable minimums:
1. shorten wording without changing factual meaning;
2. reduce cards/nodes per slide;
3. split into continuation slides;
4. use a less dense special structure.

Never solve fit by overlapping text, reducing line spacing below 1.15, or letting a card/node keep fixed dimensions while text grows inside it.

## Universal overlap rule

No visible text may overlap another visible text block, icon, card border, connector, footer or decorative element.

The deck fails if any of these are non-zero:

```text
visible_text_overlap_count > 0
text_over_card_border_count > 0
text_over_connector_count > 0
text_clipped_by_shape_count > 0
visible_text_below_avanza_minimum_count > 0
line_spacing_below_1_15_count > 0
card_or_node_text_not_measured_before_placement_count > 0
```

## Special structures

Special structures such as dependency maps, timelines, vertical priority sequences and sprint plans must still follow the same text minima. They may use fewer nodes/cards per slide or continuation slides. They may not use smaller text than ordinary cards.

## Manual delivery gate

Before delivering PPTX/PDF, render the PDF to images and inspect the rendered pages. Delivery is allowed only when:

- all pages are readable without zooming in beyond normal slide view;
- no visible text overlaps;
- no text appears visually compressed;
- no tiny metadata is required to understand the slide.

---
status: ACTIVE
