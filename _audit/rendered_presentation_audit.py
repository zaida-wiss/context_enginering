#!/usr/bin/env python3
"""Mechanical audit of rendered presentation artifacts.

This validator complements, but does not replace, the presentation authorities.
It inspects the actual PPTX structure and, when available, the exported PDF render.

Usage:
    python _audit/rendered_presentation_audit.py deck.pptx
    python _audit/rendered_presentation_audit.py deck.pdf
    python _audit/rendered_presentation_audit.py deck.pptx --pdf deck.pdf
    python _audit/rendered_presentation_audit.py --self-test

Exit codes:
    0 = PASS (warnings may exist)
    1 = FAIL
    2 = validator/dependency/input error
"""

from __future__ import annotations

import argparse
from collections import Counter
from dataclasses import dataclass, asdict
import json
import math
from pathlib import Path
import re
import statistics
import sys
import xml.etree.ElementTree as ET
import zipfile

EMU_PER_INCH = 914400
DEFAULT_SLIDE_W = 12192000
DEFAULT_SLIDE_H = 6858000
MIN_TEXT_PT = 11.0
MIN_TITLE_PT = 36.0
MIN_VISIBLE_CARD_GAP_IN = 0.12
MIN_VISIBLE_CARD_GAP_EMU = int(MIN_VISIBLE_CARD_GAP_IN * EMU_PER_INCH)
CIRCLED_NUMBERS = set("①②③④⑤⑥⑦⑧⑨⑩⑪⑫⑬⑭")
REPLACEMENT_GLYPHS = {"\ufffd", "□", "�"}

NS = {
    "p": "http://schemas.openxmlformats.org/presentationml/2006/main",
    "a": "http://schemas.openxmlformats.org/drawingml/2006/main",
}

TITLE_RE = re.compile(r"^\s*✏️?\s*(?:1[0-4]|[1-9])\.")


@dataclass
class Finding:
    severity: str  # FAIL | WARN | INFO
    code: str
    message: str
    artifact: str | None = None
    page: int | None = None

    def key(self) -> tuple:
        return (self.severity, self.code, self.artifact, self.page, self.message)


@dataclass
class ShapeInfo:
    text: str
    x: int
    y: int
    w: int
    h: int
    geometry: str | None
    font_sizes: list[float]
    has_gradient: bool
    explicit_text_colors: list[str]
    font_families: list[str]

    @property
    def right(self) -> int:
        return self.x + self.w

    @property
    def bottom(self) -> int:
        return self.y + self.h

    @property
    def center_x(self) -> float:
        return self.x + self.w / 2

    @property
    def center_y(self) -> float:
        return self.y + self.h / 2


def finding(severity: str, code: str, message: str, **kwargs) -> Finding:
    return Finding(severity=severity, code=code, message=message, **kwargs)


def srgb_channel(v: int) -> float:
    c = v / 255.0
    return c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4


def relative_luminance(rgb: tuple[int, int, int]) -> float:
    r, g, b = (srgb_channel(v) for v in rgb)
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def contrast_ratio(a: tuple[int, int, int], b: tuple[int, int, int]) -> float:
    la, lb = relative_luminance(a), relative_luminance(b)
    hi, lo = max(la, lb), min(la, lb)
    return (hi + 0.05) / (lo + 0.05)


def rgb_distance(a: tuple[int, int, int], b: tuple[int, int, int]) -> float:
    return math.sqrt(sum((x - y) ** 2 for x, y in zip(a, b)))


def bbox_intersection(a: tuple[float, float, float, float], b: tuple[float, float, float, float]) -> float:
    x0 = max(a[0], b[0])
    y0 = max(a[1], b[1])
    x1 = min(a[2], b[2])
    y1 = min(a[3], b[3])
    if x1 <= x0 or y1 <= y0:
        return 0.0
    return (x1 - x0) * (y1 - y0)


def cluster_count(values: list[float], tolerance: float) -> int:
    if not values:
        return 0
    values = sorted(values)
    clusters = 1
    anchor = values[0]
    for value in values[1:]:
        if abs(value - anchor) > tolerance:
            clusters += 1
            anchor = value
        else:
            anchor = (anchor + value) / 2
    return clusters


def parse_color_hex(value: str) -> tuple[int, int, int] | None:
    value = value.strip().lstrip("#")
    if len(value) != 6 or any(ch not in "0123456789abcdefABCDEF" for ch in value):
        return None
    return tuple(int(value[i:i+2], 16) for i in (0, 2, 4))


def _shape_xfrm(sp: ET.Element) -> tuple[int, int, int, int]:
    xfrm = sp.find(".//a:xfrm", NS)
    if xfrm is None:
        return (0, 0, 0, 0)
    off = xfrm.find("a:off", NS)
    ext = xfrm.find("a:ext", NS)
    if off is None or ext is None:
        return (0, 0, 0, 0)
    return (
        int(off.attrib.get("x", 0)),
        int(off.attrib.get("y", 0)),
        int(ext.attrib.get("cx", 0)),
        int(ext.attrib.get("cy", 0)),
    )


def _shape_text(sp: ET.Element) -> str:
    parts = []
    for node in sp.findall(".//a:t", NS):
        if node.text:
            parts.append(node.text)
    return "".join(parts).strip()


def _font_sizes(sp: ET.Element) -> list[float]:
    sizes: list[float] = []
    for tag in ("a:rPr", "a:defRPr", "a:endParaRPr"):
        for node in sp.findall(f".//{tag}", NS):
            raw = node.attrib.get("sz")
            if raw and raw.isdigit():
                sizes.append(int(raw) / 100.0)
    return sizes


def _explicit_text_colors(sp: ET.Element) -> list[str]:
    colors: list[str] = []
    for node in sp.findall(".//a:rPr/a:solidFill/a:srgbClr", NS):
        val = node.attrib.get("val")
        if val:
            colors.append(val.upper())
    for node in sp.findall(".//a:defRPr/a:solidFill/a:srgbClr", NS):
        val = node.attrib.get("val")
        if val:
            colors.append(val.upper())
    return colors


def _font_families(sp: ET.Element) -> list[str]:
    families: list[str] = []
    for tag in ("a:rPr", "a:defRPr", "a:endParaRPr"):
        for latin in sp.findall(f".//{tag}/a:latin", NS):
            face = (latin.attrib.get("typeface") or "").strip()
            if face and not face.startswith("+"):
                families.append(face)
    return families


def _geometry(sp: ET.Element) -> str | None:
    node = sp.find(".//a:prstGeom", NS)
    return node.attrib.get("prst") if node is not None else None


def _has_gradient(sp: ET.Element) -> bool:
    return sp.find(".//a:gradFill", NS) is not None


def _pptx_slide_size(zf: zipfile.ZipFile) -> tuple[int, int]:
    try:
        root = ET.fromstring(zf.read("ppt/presentation.xml"))
        node = root.find("p:sldSz", NS)
        if node is not None:
            return int(node.attrib["cx"]), int(node.attrib["cy"])
    except Exception:
        pass
    return DEFAULT_SLIDE_W, DEFAULT_SLIDE_H


def _slide_number_from_name(name: str) -> int:
    match = re.search(r"slide(\d+)\.xml$", name)
    return int(match.group(1)) if match else 0


def _extract_shapes(root: ET.Element) -> list[ShapeInfo]:
    shapes: list[ShapeInfo] = []
    for sp in root.findall(".//p:sp", NS):
        text = _shape_text(sp)
        x, y, w, h = _shape_xfrm(sp)
        shapes.append(
            ShapeInfo(
                text=text,
                x=x,
                y=y,
                w=w,
                h=h,
                geometry=_geometry(sp),
                font_sizes=_font_sizes(sp),
                has_gradient=_has_gradient(sp),
                explicit_text_colors=_explicit_text_colors(sp),
                font_families=_font_families(sp),
            )
        )
    return shapes


def _looks_like_card(shape: ShapeInfo, slide_w: int, slide_h: int) -> bool:
    if shape.w <= 0 or shape.h <= 0:
        return False
    if shape.y < slide_h * 0.15:
        return False
    if shape.w < slide_w * 0.16 or shape.w > slide_w * 0.42:
        return False
    if shape.h < slide_h * 0.15 or shape.h > slide_h * 0.55:
        return False
    if shape.geometry in {"roundRect", "round2SameRect", "round1Rect"}:
        return True
    # Some generators emit normal rectangles for glass cards.
    return bool(shape.text) and shape.w >= slide_w * 0.20 and shape.h >= slide_h * 0.18


def _meeting_point(text: str) -> int | None:
    for line in text.splitlines():
        m = TITLE_RE.match(line.strip())
        if m:
            number = re.search(r"(1[0-4]|[1-9])\.", line)
            if number:
                return int(number.group(1))
    return None


def audit_pptx(path: Path, project: str | None = None) -> list[Finding]:
    results: list[Finding] = []
    try:
        zf = zipfile.ZipFile(path)
    except Exception as exc:
        return [finding("FAIL", "pptx_open_failed", f"Could not open PPTX: {exc}", artifact=str(path))]

    with zf:
        slide_w, slide_h = _pptx_slide_size(zf)
        slide_names = sorted(
            [n for n in zf.namelist() if re.fullmatch(r"ppt/slides/slide\d+\.xml", n)],
            key=_slide_number_from_name,
        )
        if not slide_names:
            return [finding("FAIL", "pptx_no_slides", "No slides found in PPTX.", artifact=str(path))]

        meeting_title_positions: list[tuple[float, float]] = []
        primary_font_counts: Counter[str] = Counter()

        for idx, name in enumerate(slide_names, 1):
            root = ET.fromstring(zf.read(name))
            shapes = _extract_shapes(root)
            visible_text = "\n".join(s.text for s in shapes if s.text)
            mp = _meeting_point(visible_text)

            if any(ch in visible_text for ch in CIRCLED_NUMBERS):
                results.append(finding(
                    "FAIL", "rendered_circled_meeting_point_number",
                    "Visible circled meeting-point numbering found; active rule requires ordinary Arabic numbering.",
                    artifact=str(path), page=idx,
                ))

            if any(g in visible_text for g in REPLACEMENT_GLYPHS):
                results.append(finding(
                    "FAIL", "replacement_glyph",
                    "Replacement/missing-glyph character found in slide text.",
                    artifact=str(path), page=idx,
                ))

            explicit_sizes = [size for s in shapes for size in s.font_sizes]
            too_small = [size for size in explicit_sizes if size < MIN_TEXT_PT - 0.01]
            if too_small:
                results.append(finding(
                    "FAIL", "font_below_11pt",
                    f"Explicit PPTX text size below {MIN_TEXT_PT:g} pt found (min {min(too_small):.1f} pt).",
                    artifact=str(path), page=idx,
                ))

            title_shapes = [
                s for s in shapes
                if s.text and (TITLE_RE.match(s.text.strip()) or (s.y < slide_h * 0.16 and s.font_sizes and max(s.font_sizes) >= 28))
            ]
            meeting_titles = [s for s in title_shapes if TITLE_RE.match(s.text.strip())]
            for title in meeting_titles:
                meeting_title_positions.append((
                    title.x / max(slide_w, 1),
                    title.y / max(slide_h, 1),
                ))

            for title in title_shapes:
                if title.font_sizes and max(title.font_sizes) < MIN_TITLE_PT - 0.01:
                    results.append(finding(
                        "FAIL", "slide_title_below_36pt",
                        f"Slide title is {max(title.font_sizes):.1f} pt; minimum is {MIN_TITLE_PT:g} pt.",
                        artifact=str(path), page=idx,
                    ))

            for shape in shapes:
                if not re.search(r"[A-Za-zÅÄÖåäö]", shape.text):
                    continue
                for family in set(shape.font_families):
                    primary_font_counts[family] += 1

            if any("000000" == c for s in shapes for c in s.explicit_text_colors):
                results.append(finding(
                    "WARN", "explicit_black_text",
                    "Explicit black text color exists; verify it is not used on a dark/glass surface.",
                    artifact=str(path), page=idx,
                ))

            gradient_present = b"a:gradFill" in zf.read(name)
            if not gradient_present:
                results.append(finding(
                    "WARN", "pptx_gradient_not_detected",
                    "No slide-level gradient fill detected in slide XML. PDF audit must verify canonical gradient or registered fallback.",
                    artifact=str(path), page=idx,
                ))

            cards = [s for s in shapes if _looks_like_card(s, slide_w, slide_h)]
            # Deduplicate near-identical nested/overlaid shapes.
            dedup: list[ShapeInfo] = []
            for card in sorted(cards, key=lambda s: (s.y, s.x, -s.w * s.h)):
                if any(
                    abs(card.x - d.x) < 0.01 * slide_w
                    and abs(card.y - d.y) < 0.01 * slide_h
                    and abs(card.w - d.w) < 0.02 * slide_w
                    and abs(card.h - d.h) < 0.02 * slide_h
                    for d in dedup
                ):
                    continue
                dedup.append(card)
            cards = dedup

            # Header/content-zone separation: cards may never intrude into the
            # meeting-point title region.
            for title in meeting_titles:
                for card in cards:
                    if bbox_intersection(
                        (title.x, title.y, title.right, title.bottom),
                        (card.x, card.y, card.right, card.bottom),
                    ) > 0:
                        results.append(finding(
                            "FAIL", "npf_header_content_overlap",
                            "A card overlaps the meeting-point header zone.",
                            artifact=str(path), page=idx,
                        ))

            # Card overlap / visible gap checks.
            for i, a in enumerate(cards):
                for b in cards[i + 1:]:
                    ib = bbox_intersection((a.x, a.y, a.right, a.bottom), (b.x, b.y, b.right, b.bottom))
                    if ib > 0:
                        results.append(finding(
                            "FAIL", "card_overlap",
                            "Card candidate bounding boxes overlap.",
                            artifact=str(path), page=idx,
                        ))
                        continue
                    vertical_overlap = max(0, min(a.bottom, b.bottom) - max(a.y, b.y))
                    horizontal_overlap = max(0, min(a.right, b.right) - max(a.x, b.x))
                    if vertical_overlap > 0.45 * min(a.h, b.h):
                        gap = max(b.x - a.right, a.x - b.right)
                        if 0 <= gap < MIN_VISIBLE_CARD_GAP_EMU:
                            results.append(finding(
                                "FAIL", "card_horizontal_gap_too_small",
                                f"Horizontal card gap below {MIN_VISIBLE_CARD_GAP_IN:.2f} in.",
                                artifact=str(path), page=idx,
                            ))
                    if horizontal_overlap > 0.45 * min(a.w, b.w):
                        gap = max(b.y - a.bottom, a.y - b.bottom)
                        if 0 <= gap < MIN_VISIBLE_CARD_GAP_EMU:
                            results.append(finding(
                                "FAIL", "card_vertical_gap_too_small",
                                f"Vertical card gap below {MIN_VISIBLE_CARD_GAP_IN:.2f} in.",
                                artifact=str(path), page=idx,
                            ))

            if mp in {1, 3, 4, 5} and 5 <= len(cards) <= 6:
                cols = cluster_count([c.center_x for c in cards], slide_w * 0.08)
                rows = cluster_count([c.center_y for c in cards], slide_h * 0.10)
                if cols != 3 or rows != 2:
                    results.append(finding(
                        "FAIL", "expected_3x2_not_rendered",
                        f"Meeting point {mp} has {len(cards)} ordinary card candidates but geometry clusters as {cols} columns × {rows} rows.",
                        artifact=str(path), page=idx,
                    ))

            if project == "avanza" and mp in {1, 3, 4, 5} and 1 <= len(cards) < 5:
                too_wide = [c for c in cards if c.w > slide_w * 0.36]
                if too_wide:
                    results.append(finding(
                        "FAIL", "avanza_card_expanded_into_empty_slots",
                        "Avanza ordinary card expanded beyond one six-slot column while empty slots exist.",
                        artifact=str(path), page=idx,
                    ))

        if len(meeting_title_positions) >= 2:
            xs = [x for x, _ in meeting_title_positions]
            ys = [y for _, y in meeting_title_positions]
            if max(xs) - min(xs) > 0.055 or max(ys) - min(ys) > 0.055:
                results.append(finding(
                    "FAIL", "npf_meeting_title_position_inconsistent",
                    "Meeting-point title position varies by more than 5.5% of slide width/height across PPTX slides.",
                    artifact=str(path),
                ))

        significant_fonts = {
            family: count for family, count in primary_font_counts.items()
            if count >= 2
        }
        if len(significant_fonts) > 1:
            results.append(finding(
                "FAIL", "inconsistent_primary_font_family",
                "Multiple primary Latin font families are used repeatedly: "
                + ", ".join(f"{family} ({count})" for family, count in sorted(significant_fonts.items())),
                artifact=str(path),
            ))

    if not results:
        results.append(finding("INFO", "pptx_checks_passed", "PPTX structural checks passed.", artifact=str(path)))
    return results


def _int_color_to_rgb(value: int) -> tuple[int, int, int]:
    return ((value >> 16) & 255, (value >> 8) & 255, value & 255)


def _pixel_rgb(samples: bytes, n: int, x: int, y: int, width: int) -> tuple[int, int, int]:
    i = (y * width + x) * n
    return tuple(samples[i:i+3])  # type: ignore[return-value]


def _sample_background(pix, rect) -> tuple[tuple[int, int, int] | None, bool]:
    # Sample around span perimeter. Stable samples indicate a sufficiently uniform local surface.
    width, height, n = pix.width, pix.height, pix.n
    if n < 3:
        return None, False
    points = []
    x0 = max(0, min(width - 1, int(rect.x0)))
    y0 = max(0, min(height - 1, int(rect.y0)))
    x1 = max(0, min(width - 1, int(rect.x1)))
    y1 = max(0, min(height - 1, int(rect.y1)))
    xm, ym = (x0 + x1) // 2, (y0 + y1) // 2
    candidates = [
        (x0, y0), (x1, y0), (x0, y1), (x1, y1),
        (xm, y0), (xm, y1), (x0, ym), (x1, ym),
    ]
    for x, y in candidates:
        points.append(_pixel_rgb(pix.samples, n, x, y, width))
    if not points:
        return None, False
    med = tuple(int(statistics.median([p[i] for p in points])) for i in range(3))
    stable = max(rgb_distance(p, med) for p in points) < 55
    return med, stable


def audit_pdf(path: Path) -> list[Finding]:
    results: list[Finding] = []
    try:
        import fitz  # type: ignore
    except Exception:
        return [finding(
            "FAIL", "pdf_dependency_missing",
            "PyMuPDF is required for PDF render validation. Install _audit/requirements-rendered-presentation.txt.",
            artifact=str(path),
        )]

    try:
        doc = fitz.open(path)
    except Exception as exc:
        return [finding("FAIL", "pdf_open_failed", f"Could not open PDF: {exc}", artifact=str(path))]

    title_tops: list[tuple[int, float]] = []
    title_lefts: list[tuple[int, float]] = []
    fallback = parse_color_hex("18213E")
    upper = parse_color_hex("1E274A")
    lower = parse_color_hex("111A33")

    for pageno, page in enumerate(doc, 1):
        page_rect = page.rect
        text_dict = page.get_text("dict")
        blocks = text_dict.get("blocks", [])
        all_text = page.get_text("text") or ""

        if not all_text.strip():
            results.append(finding(
                "FAIL", "pdf_no_selectable_text",
                "No selectable text detected on rendered page; required meeting text must remain native/selectable.",
                artifact=str(path), page=pageno,
            ))

        if any(g in all_text for g in REPLACEMENT_GLYPHS):
            results.append(finding(
                "FAIL", "pdf_replacement_glyph",
                "Replacement/missing-glyph character found in exported PDF text.",
                artifact=str(path), page=pageno,
            ))

        if any(ch in all_text for ch in CIRCLED_NUMBERS):
            results.append(finding(
                "FAIL", "pdf_circled_meeting_number",
                "Circled meeting-point number visible in exported PDF.",
                artifact=str(path), page=pageno,
            ))

        pix = page.get_pixmap(matrix=fitz.Matrix(1, 1), alpha=False)

        spans = []
        for block in blocks:
            if block.get("type") != 0:
                continue
            for line in block.get("lines", []):
                for span in line.get("spans", []):
                    text = (span.get("text") or "").strip()
                    if text:
                        spans.append(span)

        for span in spans:
            text = (span.get("text") or "").strip()
            size = float(span.get("size") or 0)
            bbox = fitz.Rect(span.get("bbox"))
            if size and size < MIN_TEXT_PT - 0.05:
                results.append(finding(
                    "FAIL", "pdf_font_below_11pt",
                    f"Rendered text below {MIN_TEXT_PT:g} pt: {size:.1f} pt ({text[:45]!r}).",
                    artifact=str(path), page=pageno,
                ))

            if TITLE_RE.match(text):
                title_tops.append((pageno, bbox.y0 / max(page_rect.height, 1)))
                title_lefts.append((pageno, bbox.x0 / max(page_rect.width, 1)))
                if size < MIN_TITLE_PT - 0.05:
                    results.append(finding(
                        "FAIL", "pdf_title_below_36pt",
                        f"Rendered meeting-point title is {size:.1f} pt; minimum is {MIN_TITLE_PT:g} pt.",
                        artifact=str(path), page=pageno,
                    ))

            fg = _int_color_to_rgb(int(span.get("color") or 0))
            bg, stable = _sample_background(pix, bbox)
            if bg is not None and stable:
                ratio = contrast_ratio(fg, bg)
                threshold = 3.0 if size >= 18 else 4.5
                if ratio + 0.05 < threshold:
                    results.append(finding(
                        "FAIL", "pdf_contrast_failure",
                        f"Estimated rendered contrast {ratio:.2f}:1 is below {threshold:.1f}:1 for {text[:45]!r}.",
                        artifact=str(path), page=pageno,
                    ))

        # Strong overlap proxy on independent text blocks.
        text_blocks = [b for b in blocks if b.get("type") == 0 and (b.get("bbox") is not None)]
        for i, a in enumerate(text_blocks):
            ab = tuple(a["bbox"])
            aa = max(1.0, (ab[2] - ab[0]) * (ab[3] - ab[1]))
            for b in text_blocks[i + 1:]:
                bb = tuple(b["bbox"])
                ba = max(1.0, (bb[2] - bb[0]) * (bb[3] - bb[1]))
                inter = bbox_intersection(ab, bb)
                if inter / min(aa, ba) > 0.40:
                    results.append(finding(
                        "FAIL", "pdf_text_block_overlap",
                        "Rendered selectable-text blocks overlap materially.",
                        artifact=str(path), page=pageno,
                    ))
                    break

        # Background/gradient check from quiet left margin samples.
        def sample_page(x_frac: float, y_frac: float) -> tuple[int, int, int]:
            x = max(0, min(pix.width - 1, int(pix.width * x_frac)))
            y = max(0, min(pix.height - 1, int(pix.height * y_frac)))
            return _pixel_rgb(pix.samples, pix.n, x, y, pix.width)

        top = sample_page(0.025, 0.08)
        bottom = sample_page(0.025, 0.92)
        if relative_luminance(top) < 0.012 and relative_luminance(bottom) < 0.012:
            results.append(finding(
                "FAIL", "near_black_background",
                "Rendered page background appears near-black instead of modern navy.",
                artifact=str(path), page=pageno,
            ))

        gradient_delta = rgb_distance(top, bottom)
        fallback_ok = fallback is not None and rgb_distance(top, fallback) < 28 and rgb_distance(bottom, fallback) < 28
        navy_ok = True
        for sample in (top, bottom):
            r, g, b = sample
            if not (b >= r * 0.95 and b >= g * 0.85 and max(sample) < 95):
                navy_ok = False
        if not navy_ok:
            results.append(finding(
                "WARN", "background_not_canonical_navy_family",
                f"Margin samples {top} / {bottom} do not clearly match the canonical navy family.",
                artifact=str(path), page=pageno,
            ))
        if gradient_delta < 10 and not fallback_ok:
            results.append(finding(
                "FAIL", "canonical_gradient_missing",
                "Rendered background appears effectively solid and does not match the registered solid fallback.",
                artifact=str(path), page=pageno,
            ))

    if len(title_tops) >= 2:
        vertical_positions = [pos for _, pos in title_tops]
        horizontal_positions = [pos for _, pos in title_lefts]
        if (
            max(vertical_positions) - min(vertical_positions) > 0.055
            or max(horizontal_positions) - min(horizontal_positions) > 0.055
        ):
            results.append(finding(
                "FAIL", "npf_title_zone_inconsistent",
                "Meeting-point title position varies by more than 5.5% of page width/height across rendered slides.",
                artifact=str(path),
            ))

    doc.close()
    if not results:
        results.append(finding("INFO", "pdf_checks_passed", "PDF render checks passed.", artifact=str(path)))
    return results


def self_test() -> int:
    failures: list[str] = []
    if contrast_ratio((255, 255, 255), (17, 26, 51)) < 10:
        failures.append("contrast_ratio")
    if contrast_ratio((0, 0, 0), (10, 10, 10)) > 1.2:
        failures.append("low_contrast")
    if bbox_intersection((0, 0, 10, 10), (5, 5, 15, 15)) != 25:
        failures.append("bbox_intersection")
    if cluster_count([1, 1.1, 5, 5.1, 9, 9.1], 0.5) != 3:
        failures.append("cluster_count")
    if _meeting_point("✏️ 4. Backend\nVar är vi?") != 4:
        failures.append("meeting_point")
    if _meeting_point("① Backend") is not None:
        failures.append("circled_number_not_parsed_as_active_header")
    if cluster_count([1, 1.1, 5, 5.1, 9, 9.1], 0.5) != 3:
        failures.append("npf_cluster_regression")
    if failures:
        print("Rendered presentation audit self-test: FAIL")
        for item in failures:
            print(f"- {item}")
        return 1
    print("Rendered presentation audit self-test: PASS")
    return 0


def summarize(results: list[Finding]) -> int:
    unique = []
    seen = set()
    for item in results:
        if item.key() not in seen:
            seen.add(item.key())
            unique.append(item)

    counts = Counter(item.severity for item in unique)
    print("RENDERED PRESENTATION AUDIT")
    print("=" * 72)
    for item in unique:
        where = ""
        if item.artifact:
            where += f" [{item.artifact}"
            if item.page is not None:
                where += f" · page {item.page}"
            where += "]"
        print(f"{item.severity}: {item.code}{where} — {item.message}")
    print("-" * 72)
    print(f"FAIL={counts['FAIL']} WARN={counts['WARN']} INFO={counts['INFO']}")
    return 1 if counts["FAIL"] else 0


def main() -> int:
    parser = argparse.ArgumentParser(description="Audit actual PPTX/PDF presentation artifacts.")
    parser.add_argument("artifact", nargs="?", help="PPTX or PDF artifact to validate")
    parser.add_argument("--pdf", help="Optional exported PDF corresponding to a PPTX")
    parser.add_argument("--project", help="Selected project id, e.g. avanza")
    parser.add_argument("--json", dest="json_path", help="Write machine-readable findings JSON")
    parser.add_argument("--self-test", action="store_true", help="Run validator unit self-test")
    args = parser.parse_args()

    if args.self_test:
        return self_test()

    if not args.artifact:
        parser.error("artifact is required unless --self-test is used")

    artifact = Path(args.artifact)
    if not artifact.exists():
        print(f"Artifact not found: {artifact}", file=sys.stderr)
        return 2

    results: list[Finding] = []
    suffix = artifact.suffix.lower()
    if suffix == ".pptx":
        results.extend(audit_pptx(artifact, project=args.project))
    elif suffix == ".pdf":
        results.extend(audit_pdf(artifact))
    else:
        print("Only .pptx and .pdf are supported.", file=sys.stderr)
        return 2

    if args.pdf:
        pdf = Path(args.pdf)
        if not pdf.exists():
            print(f"PDF not found: {pdf}", file=sys.stderr)
            return 2
        results.extend(audit_pdf(pdf))

    if args.json_path:
        Path(args.json_path).write_text(
            json.dumps([asdict(x) for x in results], ensure_ascii=False, indent=2),
            encoding="utf-8",
        )

    return summarize(results)


if __name__ == "__main__":
    sys.exit(main())
