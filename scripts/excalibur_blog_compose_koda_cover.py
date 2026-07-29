#!/usr/bin/env python3
"""KODA blog cover: 3D Flux background + Montserrat Cyrillic typography (как legacy блог)."""

from __future__ import annotations

import argparse
import io
import os
import urllib.request
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont, ImageFilter


def project_root() -> Path:
    env_root = os.environ.get("EXCALIBUR_PROJECT_ROOT", "").strip()
    if env_root:
        return Path(env_root)
    return Path(__file__).resolve().parents[1]


def download_image(url: str) -> Image.Image:
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=120) as response:
        return Image.open(io.BytesIO(response.read()))


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


def compose_cover(bg_url: str, lines: list[str], line_colors: list[tuple], cover_path: Path, root: Path) -> None:
    bg = download_image(bg_url).convert("RGBA").resize((1200, 675), Image.Resampling.LANCZOS)
    overlay = Image.new("RGBA", (1200, 675), (0, 0, 0, 0))
    o_draw = ImageDraw.Draw(overlay)
    for x in range(480, 1200):
        alpha = int(170 * ((x - 480) / 720))
        o_draw.line([(x, 0), (x, 675)], fill=(5, 5, 10, alpha))
    bg = Image.alpha_composite(bg, overlay)
    draw = ImageDraw.Draw(bg)
    font_path = str(root / "Montserrat-ExtraBold.ttf")
    font_main = ImageFont.truetype(font_path, 64)
    font_brand = ImageFont.truetype(font_path, 28)
    start_y = 140
    x_pos = 520
    for i, line in enumerate(lines[:3]):
        color = line_colors[i] if i < len(line_colors) else (255, 255, 255, 255)
        draw_youtube_text(draw, line, (x_pos, start_y), font_main, text_color=color, stroke_width=11, shadow_radius=7)
        start_y += 88
    draw_youtube_text(
        draw,
        "koda-fd.ru",
        (x_pos + 8, start_y + 8),
        font_brand,
        text_color=(196, 181, 253, 220),
        stroke_width=5,
        shadow_radius=4,
    )
    cover_path.parent.mkdir(parents=True, exist_ok=True)
    bg.convert("RGB").save(cover_path, "PNG")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--article-dir", required=True)
    ap.add_argument("--bg-url", required=True)
    ap.add_argument("--line1", required=True)
    ap.add_argument("--line2", required=True)
    ap.add_argument("--line3", required=True)
    ap.add_argument("--dzen-copy", action="store_true", help="Also save to cover/dzen-cover.png")
    args = ap.parse_args()

    root = project_root()
    article_dir = Path(args.article_dir)
    if not article_dir.is_absolute():
        article_dir = root / article_dir
    cover_dir = article_dir / "cover"
    colors = [
        (255, 255, 255, 255),
        (255, 255, 255, 255),
        (254, 240, 138, 255),
    ]
    compose_cover(args.bg_url, [args.line1, args.line2, args.line3], colors, cover_dir / "cover.png", root)
    print(f"OK cover={cover_dir / 'cover.png'}")
    if args.dzen_copy:
        compose_cover(
            args.bg_url,
            [args.line1, args.line2, args.line3],
            colors,
            cover_dir / "dzen-cover.png",
            root,
        )
        print(f"OK dzen-cover={cover_dir / 'dzen-cover.png'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
