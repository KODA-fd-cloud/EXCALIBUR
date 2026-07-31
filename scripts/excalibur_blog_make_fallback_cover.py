#!/usr/bin/env python3
"""KODA fallback cover: abstract gradient + Montserrat Cyrillic (когда MCP gpt-image недоступен).

Usage:
  python scripts/excalibur_blog_make_fallback_cover.py --article-dir memory/blog/articles/B24-...
  python scripts/excalibur_blog_make_fallback_cover.py --missing-published
"""
from __future__ import annotations

import argparse
import json
import random
import re
from datetime import datetime, timezone
from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter, ImageFont

ROOT = Path(__file__).resolve().parents[1]
PUBLISHED = ROOT / "shared" / "published-articles.md"
ARTICLES = ROOT / "memory" / "blog" / "articles"
FONT = ROOT / "Montserrat-ExtraBold.ttf"

# Short 3-line overlays (UPPER) — clickable, not full H1 dump
LINES: dict[str, tuple[str, str, str]] = {
    "B19": ("PYTHON ДЛЯ ФИНАНСИСТА", "СВЕРКА ДВУХ CSV", "ЗА 15 МИНУТ"),
    "B22": ("GOOGLE APPS SCRIPT", "КНОПКА ОБНОВИТЬ", "ДАННЫЕ В SHEETS"),
    "B23": ("CURSOR RULES", "ДЛЯ ФИНОТДЕЛА", "БЕЗ ХАОСА В ЧАТЕ"),
    "B24": ("ПЛАТЁЖНЫЙ КАЛЕНДАРЬ", "GOOGLE SHEETS + n8n", "БЕЗ КАССОВОГО РАЗРЫВА"),
    "B25": ("ВЫПИСКА В STAGING", "БЕЗ КОПИПАСТА", "HASH И ДЕДУП"),
}


def draw_youtube_text(
    draw: ImageDraw.ImageDraw,
    text: str,
    position: tuple[int, int],
    font: ImageFont.FreeTypeFont,
    text_color: tuple[int, int, int, int],
    stroke_color: tuple[int, int, int, int] = (10, 10, 15, 255),
    stroke_width: int = 10,
    shadow_color: tuple[int, int, int, int] = (0, 0, 0, 200),
    shadow_offset: tuple[int, int] = (5, 5),
    shadow_radius: int = 4,
) -> None:
    x, y = position
    left, top, right, bottom = draw.textbbox((0, 0), text, font=font)
    text_w, text_h = right - left, bottom - top
    margin = max(shadow_radius * 2, stroke_width) + 10
    w, h = text_w + margin * 2, text_h + margin * 2
    shadow_img = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    s_draw = ImageDraw.Draw(shadow_img)
    s_draw.text(
        (margin - left, margin - top),
        text,
        font=font,
        fill=shadow_color,
        stroke_width=stroke_width,
        stroke_fill=shadow_color,
    )
    shadow_blurred = shadow_img.filter(ImageFilter.GaussianBlur(shadow_radius))
    draw._image.paste(shadow_blurred, (x - margin + shadow_offset[0], y - margin + shadow_offset[1]), shadow_blurred)
    draw.text((x, y), text, font=font, fill=text_color, stroke_width=stroke_width, stroke_fill=stroke_color)


def abstract_bg(seed: str, w: int = 1200, h: int = 675) -> Image.Image:
    rng = random.Random(seed)
    # Fast vertical gradient via resized 1px strip
    strip = Image.new("RGB", (1, h))
    sp = strip.load()
    for y in range(h):
        t = y / max(1, h - 1)
        sp[0, y] = (
            int(8 + 35 * t),
            int(8 + 18 * t),
            int(18 + 95 * t),
        )
    img = strip.resize((w, h), Image.Resampling.BILINEAR).convert("RGBA")

    overlay = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    d = ImageDraw.Draw(overlay)
    # glow blobs (few, then blur once)
    glow = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    gd = ImageDraw.Draw(glow)
    for _ in range(6):
        cx, cy = rng.randint(0, 620), rng.randint(0, h)
        rad = rng.randint(90, 200)
        gd.ellipse((cx - rad, cy - rad, cx + rad, cy + rad), fill=(139, 92, 246, 70))
    overlay = Image.alpha_composite(overlay, glow.filter(ImageFilter.GaussianBlur(28)))

    d = ImageDraw.Draw(overlay)
    nodes = [(rng.randint(40, 520), rng.randint(60, h - 60)) for _ in range(14)]
    for i, (x1, y1) in enumerate(nodes):
        for j in range(i + 1, len(nodes)):
            x2, y2 = nodes[j]
            if (x1 - x2) ** 2 + (y1 - y2) ** 2 < 180**2 and rng.random() < 0.45:
                d.line([(x1, y1), (x2, y2)], fill=(139, 92, 246, 100), width=2)
    for x, y in nodes:
        r = rng.randint(6, 16)
        d.ellipse(
            (x - r, y - r, x + r, y + r),
            fill=(147, 197, 253, 170),
            outline=(196, 181, 253, 230),
            width=2,
        )

    base = Image.alpha_composite(img, overlay)
    shade = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    sd = ImageDraw.Draw(shade)
    for x in range(480, w):
        alpha = int(175 * ((x - 480) / 720))
        sd.line([(x, 0), (x, h)], fill=(5, 5, 10, alpha))
    return Image.alpha_composite(base, shade)


def split_lines_from_h1(h1: str) -> tuple[str, str, str]:
    words = re.sub(r"[«»\":]", "", h1).split()
    if len(words) <= 3:
        padded = (words + ["", "", ""])[:3]
        return tuple(w.upper() for w in padded)  # type: ignore
    n = len(words)
    a, b = max(1, n // 3), max(2, 2 * n // 3)
    return (
        " ".join(words[:a]).upper(),
        " ".join(words[a:b]).upper(),
        " ".join(words[b:]).upper(),
    )


def make_cover(article_dir: Path) -> Path:
    meta = json.loads((article_dir / "article.meta.json").read_text(encoding="utf-8"))
    topic_id = str(meta.get("topic_id") or article_dir.name.split("-")[0]).upper()
    slug = meta.get("slug") or ""
    alt = meta.get("cover_alt") or meta.get("h1") or slug
    lines = LINES.get(topic_id) or split_lines_from_h1(meta.get("h1") or meta.get("title") or topic_id)

    bg = abstract_bg(seed=f"{topic_id}:{slug}")
    draw = ImageDraw.Draw(bg)
    font_main = ImageFont.truetype(str(FONT), 52)
    font_brand = ImageFont.truetype(str(FONT), 26)
    # fit long lines
    colors = [
        (255, 255, 255, 255),
        (255, 255, 255, 255),
        (253, 224, 71, 255),
    ]
    y = 150
    x = 520
    for i, line in enumerate(lines[:3]):
        size = 52 if len(line) < 22 else 42 if len(line) < 30 else 34
        font = ImageFont.truetype(str(FONT), size)
        draw_youtube_text(draw, line, (x, y), font, text_color=colors[i], stroke_width=9, shadow_radius=6)
        y += size + 28
    draw_youtube_text(
        draw,
        "koda-fd.ru",
        (x + 4, y + 6),
        font_brand,
        text_color=(196, 181, 253, 220),
        stroke_width=5,
        shadow_radius=4,
    )

    cover_dir = article_dir / "cover"
    cover_dir.mkdir(parents=True, exist_ok=True)
    cover_path = cover_dir / "cover.png"
    bg.convert("RGB").save(cover_path, "PNG")
    dzen_path = cover_dir / "dzen-cover.png"
    bg.convert("RGB").save(dzen_path, "PNG")

    reg = {
        "topic_id": topic_id,
        "slug": slug,
        "cover_family": meta.get("cover_family") or "gradient_abstract",
        "pipeline": "fallback_pil_montserrat",
        "file": "cover/cover.png",
        "dzen_file": "cover/dzen-cover.png",
        "alt": alt,
        "cover_alt_text": alt,
        "aspect_ratio": "16:9",
        "size": "1200x675",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "note": "MCP gpt-image unavailable in CI fast-path; fallback branded cover",
        "lines": list(lines),
    }
    (cover_dir / "cover-registry.json").write_text(
        json.dumps(reg, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(f"OK {topic_id} -> {cover_path}")
    return cover_path


def missing_published_dirs() -> list[Path]:
    slugs: list[str] = []
    if PUBLISHED.is_file():
        for line in PUBLISHED.read_text(encoding="utf-8").splitlines():
            if not line.startswith("| 20"):
                continue
            parts = [p.strip() for p in line.strip("|").split("|")]
            if len(parts) >= 3:
                slugs.append(parts[2].lower())
    out: list[Path] = []
    for d in sorted(ARTICLES.glob("B*")):
        if not d.is_dir():
            continue
        meta = d / "article.meta.json"
        if not meta.is_file():
            continue
        slug = json.loads(meta.read_text(encoding="utf-8")).get("slug", "").lower()
        if slug not in slugs:
            continue
        if not (d / "cover" / "cover.png").is_file():
            out.append(d)
    return out


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--article-dir", default="")
    ap.add_argument("--missing-published", action="store_true")
    args = ap.parse_args()
    if not FONT.is_file():
        raise SystemExit(f"Missing font: {FONT}")

    dirs: list[Path] = []
    if args.missing_published:
        dirs = missing_published_dirs()
    elif args.article_dir:
        p = Path(args.article_dir)
        dirs = [p if p.is_absolute() else ROOT / p]
    else:
        raise SystemExit("Need --article-dir or --missing-published")

    if not dirs:
        print("Nothing to do")
        return 0
    for d in dirs:
        make_cover(d)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
