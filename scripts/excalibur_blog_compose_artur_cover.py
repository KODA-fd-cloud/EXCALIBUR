#!/usr/bin/env python3
"""Генерация премиальной обложки Дзена в профессиональном стиле.

Использует сгенерированную базу (3D персонаж на левой стороне) и накладывает
высокодетализированную, супер-контрастную типографику с жирным черным контуром,
светящимися акцентами и подписью koda-fd.ru.
"""

from __future__ import annotations

import argparse
import io
import os
import sys
import urllib.request
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageFilter


def project_root() -> Path:
    env_root = os.environ.get("EXCALIBUR_PROJECT_ROOT", "").strip()
    if env_root:
        return Path(env_root)
    return Path(__file__).resolve().parents[1]


def download_image(url: str) -> Image.Image:
    print(f"Downloading {url}...")
    headers = {"User-Agent": "Mozilla/5.0"}
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req, timeout=60) as response:
        data = response.read()
    return Image.open(io.BytesIO(data))


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
    """Отрисовывает текст с толстым черным контуром и глубокой размытой тенью."""
    x, y = position
    
    # 1. Сначала рассчитываем размеры текста
    left, top, right, bottom = draw.textbbox((0, 0), text, font=font)
    text_w = right - left
    text_h = bottom - top
    
    # 2. Создаем отдельный холст для тени
    margin = max(shadow_radius * 2, stroke_width) + 10
    w = text_w + margin * 2
    h = text_h + margin * 2
    
    shadow_img = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    s_draw = ImageDraw.Draw(shadow_img)
    
    # Рисуем контур тени
    s_draw.text(
        (margin - left, margin - top),
        text,
        font=font,
        fill=shadow_color,
        stroke_width=stroke_width,
        stroke_fill=shadow_color,
    )
    
    # Размываем тень
    shadow_blurred = shadow_img.filter(ImageFilter.GaussianBlur(shadow_radius))
    
    # Накладываем размытую тень на основной холст со смещением
    paste_x = x - margin + shadow_offset[0]
    paste_y = y - margin + shadow_offset[1]
    draw._image.paste(shadow_blurred, (paste_x, paste_y), shadow_blurred)
    
    # 3. Рисуем основной текст со stroke_width
    draw.text(
        (x, y),
        text,
        font=font,
        fill=text_color,
        stroke_width=stroke_width,
        stroke_fill=stroke_color,
    )


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--article-dir", required=True)
    ap.add_argument("--bg-url", required=True)
    ap.add_argument("--cutout-url", required=False, default="")
    args = ap.parse_args()

    root = project_root()
    article_dir = Path(args.article_dir)
    if not article_dir.is_absolute():
        article_dir = root / article_dir

    cover_dir = article_dir / "cover"
    cover_dir.mkdir(parents=True, exist_ok=True)

    # 1. Загружаем сгенерированную базу (3D персонаж + премиальный фон)
    bg = download_image(args.bg_url).convert("RGBA")
    bg = bg.resize((1200, 675), Image.Resampling.LANCZOS)
    
    # 2. Создаем холст для рисования
    draw = ImageDraw.Draw(bg)
    font_path = str(root / "Montserrat-ExtraBold.ttf")
    
    # Размеры шрифтов под стиль YouTube / Dzen
    font_main = ImageFont.truetype(font_path, 68)     # Основной крупный текст
    font_brand = ImageFont.truetype(font_path, 28)    # Ссылка на сайт
    
    # Координаты начала текста (смещено вправо, где находится темная градиентная зона)
    start_y = 165
    x_pos = 550  
    
    # Отрисовываем заголовок в 3 строки по правилам Клода
    # Строка 1: "СЧЕТА ИЗ ПОЧТЫ" (Белый с толстой черной обводкой)
    draw_youtube_text(
        draw,
        "СЧЕТА ИЗ ПОЧТЫ",
        (x_pos, start_y),
        font_main,
        text_color=(255, 255, 255, 255),
        stroke_color=(10, 10, 15, 255),
        stroke_width=12,
        shadow_radius=8,
    )
    start_y += 95
    
    # Строка 2: "ЗА ВЕЧЕР" (Белый с толстой черной обводкой)
    draw_youtube_text(
        draw,
        "ЗА ВЕЧЕР",
        (x_pos, start_y),
        font_main,
        text_color=(255, 255, 255, 255),
        stroke_color=(10, 10, 15, 255),
        stroke_width=12,
        shadow_radius=8,
    )
    start_y += 95
    
    # Строка 3: "БЕЗ КОДА!" (Яркий неоново-желтый акцент с толстой обводкой)
    draw_youtube_text(
        draw,
        "БЕЗ КОДА!",
        (x_pos, start_y),
        font_main,
        text_color=(254, 240, 138, 255),  # #fef08a
        stroke_color=(10, 10, 15, 255),
        stroke_width=12,
        shadow_radius=8,
    )
    start_y += 115
    
    # Фирменная подпись: koda-fd.ru (мелкий чистый шрифт под заголовком)
    draw_youtube_text(
        draw,
        "koda-fd.ru",
        (x_pos + 10, start_y),
        font_brand,
        text_color=(196, 181, 253, 220),  # Светло-фиолетовый с прозрачностью #c4b5fd
        stroke_color=(10, 10, 15, 200),
        stroke_width=6,
        shadow_radius=4,
    )
    
    # Сохраняем готовую обложку в PNG
    final_cover_path = cover_dir / "cover.png"
    bg.convert("RGB").save(final_cover_path, "PNG")
    print(f"OK final cover: {final_cover_path}")

    # Сохраняем также в папку экспорта Дзена
    topic_id = article_dir.name.split("-")[0]
    slug = "-".join(article_dir.name.split("-")[1:])
    export_dir = root / "memory" / "dzen-exports" / f"{topic_id}-{slug}"
    if export_dir.exists():
        images_dir = export_dir / "images"
        images_dir.mkdir(parents=True, exist_ok=True)
        bg.convert("RGB").save(images_dir / "cover.png", "PNG")
        print(f"OK cover updated in Dzen export: {images_dir / 'cover.png'}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
