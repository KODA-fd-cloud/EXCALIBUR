#!/usr/bin/env python3
"""Скрипт для скачивания и установки готовой обложки от Flux."""

from __future__ import annotations

import argparse
import io
import os
import sys
import urllib.request
from pathlib import Path
from PIL import Image


def project_root() -> Path:
    env_root = os.environ.get("EXCALIBUR_PROJECT_ROOT", "").strip()
    if env_root:
        return Path(env_root)
    return Path(__file__).resolve().parents[1]


def download_image(url: str) -> Image.Image:
    print(f"Downloading {url}...")
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req, timeout=60) as response:
        data = response.read()
    return Image.open(io.BytesIO(data))


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--article-dir", required=True, help="Путь к директории статьи")
    ap.add_argument("--url", required=True, help="URL готовой обложки от Flux 2 Pro")
    args = ap.parse_args()

    root = project_root()
    article_dir = Path(args.article_dir)
    if not article_dir.is_absolute():
        article_dir = root / article_dir

    cover_dir = article_dir / "cover"
    cover_dir.mkdir(parents=True, exist_ok=True)

    # Скачиваем изображение
    img = download_image(args.url).convert("RGB")

    # Сохраняем в папку статьи
    final_cover_path = cover_dir / "cover.png"
    img.save(final_cover_path, "PNG")
    print(f"OK final cover: {final_cover_path}")

    # Сохраняем в папку Dzen-экспорта, если она существует
    topic_id = article_dir.name.split("-")[0]
    slug = "-".join(article_dir.name.split("-")[1:])
    export_dir = root / "memory" / "dzen-exports" / f"{topic_id}-{slug}"
    if export_dir.exists():
        images_dir = export_dir / "images"
        images_dir.mkdir(parents=True, exist_ok=True)
        img.save(images_dir / "cover.png", "PNG")
        print(f"OK cover updated in Dzen export: {images_dir / 'cover.png'}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
