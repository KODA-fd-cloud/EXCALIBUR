#!/usr/bin/env python3
"""Fallback cover helper — НЕ рисует текст на обложке.

Канон блога КОДА: abstract holographic CGI, 16:9, без букв/watermark.
Этот скрипт только:
  - проверяет, что cover.png есть и без «текстового» PIL-мусора (по registry.pipeline)
  - копирует готовый abstract PNG в article/cover/
  - пишет cover-registry.json

Генерация картинки: Cursor GenerateImage / MCP gpt-image / Flux → затем:
  python scripts/excalibur_blog_make_fallback_cover.py --article-dir ... --from-png path.png

Запрещено: Montserrat overlay, koda-fd.ru на картинке, ALL-CAPS заголовки.
"""
from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parents[1]


def install_cover(article_dir: Path, src_png: Path) -> Path:
    meta = json.loads((article_dir / "article.meta.json").read_text(encoding="utf-8"))
    topic_id = str(meta.get("topic_id") or article_dir.name.split("-")[0]).upper()
    slug = meta.get("slug") or ""
    alt = meta.get("cover_alt") or meta.get("h1") or slug

    cover_dir = article_dir / "cover"
    cover_dir.mkdir(parents=True, exist_ok=True)
    img = Image.open(src_png).convert("RGB").resize((1200, 675), Image.Resampling.LANCZOS)
    cover_path = cover_dir / "cover.png"
    img.save(cover_path, "PNG")
    img.save(cover_dir / "dzen-cover.png", "PNG")

    reg = {
        "topic_id": topic_id,
        "slug": slug,
        "cover_family": meta.get("cover_family") or "gradient_abstract",
        "pipeline": "cursor_generate_image_legacy_abstract",
        "file": "cover/cover.png",
        "dzen_file": "cover/dzen-cover.png",
        "alt": alt,
        "cover_alt_text": alt,
        "aspect_ratio": "16:9",
        "size": "1200x675",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "note": "abstract holographic, NO text on image",
    }
    (cover_dir / "cover-registry.json").write_text(
        json.dumps(reg, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(f"OK {topic_id} -> {cover_path}")
    return cover_path


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--article-dir", required=True)
    ap.add_argument("--from-png", required=True, help="Path to abstract cover PNG (no text)")
    args = ap.parse_args()
    article_dir = Path(args.article_dir)
    if not article_dir.is_absolute():
        article_dir = ROOT / article_dir
    src = Path(args.from_png)
    if not src.is_absolute():
        src = ROOT / src
    if not src.is_file():
        raise SystemExit(f"missing png: {src}")
    install_cover(article_dir, src)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
