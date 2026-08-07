#!/usr/bin/env python3
"""Refuse covers that look like text/portrait junk (KODA abstract-only canon).

Heuristic only — not OCR. Blocks obvious album-cover / face / letterbox failures
before WordPress publish.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

try:
    from PIL import Image
except ImportError:
    print("Pillow required", file=sys.stderr)
    sys.exit(2)


def skin_ratio(img: Image.Image) -> float:
    """Rough skin-tone pixel share — high on portrait covers."""
    small = img.convert("RGB").resize((160, 90))
    pixels = list(small.getdata())
    skin = 0
    for r, g, b in pixels:
        if r > 95 and g > 40 and b > 20 and r > g and r > b and abs(r - g) > 15:
            skin += 1
    return skin / max(len(pixels), 1)


def high_contrast_edge_density(img: Image.Image) -> float:
    """Text/UI overlays often create dense hard edges vs soft abstract CGI."""
    g = img.convert("L").resize((240, 135))
    px = list(g.getdata())
    w, h = g.size
    edges = 0
    total = 0
    for y in range(h - 1):
        for x in range(w - 1):
            i = y * w + x
            d = abs(px[i] - px[i + 1]) + abs(px[i] - px[i + w])
            total += 1
            if d > 80:
                edges += 1
    return edges / max(total, 1)


def check_cover(path: Path) -> list[str]:
    problems: list[str] = []
    if not path.is_file():
        return ["missing cover.png"]
    img = Image.open(path)
    w, h = img.size
    if w < 800 or h < 400:
        problems.append(f"too small {w}x{h}")
    skin = skin_ratio(img)
    if skin >= 0.08:
        problems.append(f"likely portrait/face (skin_ratio={skin:.3f})")
    # Very high edge density often = typography/UI stickers
    dens = high_contrast_edge_density(img)
    if dens >= 0.22:
        problems.append(f"likely text/UI overlay (edge_density={dens:.3f})")
    reg = path.parent / "cover-registry.json"
    if reg.is_file():
        try:
            data = json.loads(reg.read_text(encoding="utf-8"))
            note = str(data.get("note") or data.get("scene_hint") or "").lower()
            if "no text" not in note and "без текст" not in note and "abstract" not in note:
                # soft signal only when other heuristics fire
                if problems:
                    problems.append("registry missing abstract/no-text note")
        except Exception:
            pass
    return problems


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--article-dir", type=Path, required=True)
    args = ap.parse_args()
    cover = args.article_dir / "cover" / "cover.png"
    problems = check_cover(cover)
    out = {"ok": not problems, "cover": str(cover), "problems": problems}
    print(json.dumps(out, ensure_ascii=False))
    return 0 if not problems else 1


if __name__ == "__main__":
    raise SystemExit(main())
