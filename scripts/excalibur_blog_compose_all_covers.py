#!/usr/bin/env python3
"""Генерация пакетного набора профессиональных обложек для Дзена в стиле Артура (KODA edition).

Яркие, сочные, высококонтрастные фоны с узнаваемыми 3D-символами инструментов
и крупная, сочная, профессионально сверстанная типографика (крупные цветные заголовки,
аккуратные обводки, мягкие тени).
"""

from __future__ import annotations

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
    print(f"Downloading background from {url}...")
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
    stroke_color: tuple[int, int, int, int] = (15, 15, 25, 255),
    stroke_width: int = 6,
    shadow_color: tuple[int, int, int, int] = (0, 0, 0, 220),
    shadow_offset: tuple[int, int] = (4, 4),
    shadow_radius: int = 5,
) -> None:
    """Отрисовывает сочный текст с аккуратным тонким темным контуром и красивой мягкой размытой тенью."""
    x, y = position
    left, top, right, bottom = draw.textbbox((0, 0), text, font=font)
    text_w = right - left
    text_h = bottom - top
    
    margin = max(shadow_radius * 2, stroke_width) + 10
    w = text_w + margin * 2
    h = text_h + margin * 2
    
    # Рисуем тень на отдельном прозрачном слое
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
    
    # Размываем тень для реалистичности
    shadow_blurred = shadow_img.filter(ImageFilter.GaussianBlur(shadow_radius))
    
    # Накладываем тень на основной фон с небольшим смещением
    paste_x = x - margin + shadow_offset[0]
    paste_y = y - margin + shadow_offset[1]
    draw._image.paste(shadow_blurred, (paste_x, paste_y), shadow_blurred)
    
    # Рисуем основной текст с тонкой обводкой сверху
    draw.text(
        (x, y),
        text,
        font=font,
        fill=text_color,
        stroke_width=stroke_width,
        stroke_fill=stroke_color,
    )


def draw_text_plate(
    draw: ImageDraw.ImageDraw,
    text: str,
    font: ImageFont.FreeTypeFont,
    pos_x: int,
    pos_y: int,
    text_color: tuple[int, int, int, int],
    bg_color: tuple[int, int, int, int],
    padding_x: int = 15,
    padding_y: int = 8,
    border_radius: int = 6,
    has_shadow: bool = True,
) -> int:
    """Отрисовывает аккуратный закругленный бейдж (плашку) над текстом."""
    left, top, right, bottom = draw.textbbox((0, 0), text, font=font)
    text_w = right - left
    text_h = bottom - top

    plate_w = text_w + padding_x * 2
    plate_h = text_h + padding_y * 2

    plate_x1 = pos_x
    plate_y1 = pos_y
    plate_x2 = pos_x + plate_w
    plate_y2 = pos_y + plate_h

    text_x = pos_x + padding_x - left
    text_y = pos_y + padding_y - top

    if has_shadow:
        shadow_radius = 6
        margin = shadow_radius * 2
        shadow_img = Image.new("RGBA", (plate_w + margin * 2, plate_h + margin * 2), (0, 0, 0, 0))
        s_draw = ImageDraw.Draw(shadow_img)
        s_draw.rounded_rectangle(
            (margin, margin, margin + plate_w, margin + plate_h),
            radius=border_radius,
            fill=(10, 10, 20, 150),
        )
        shadow_blurred = shadow_img.filter(ImageFilter.GaussianBlur(shadow_radius))
        draw._image.paste(
            shadow_blurred,
            (plate_x1 - margin + 3, plate_y1 - margin + 3),
            shadow_blurred,
        )

    draw.rounded_rectangle(
        (plate_x1, plate_y1, plate_x2, plate_y2),
        radius=border_radius,
        fill=bg_color,
    )

    draw.text((text_x, text_y), text, font=font, fill=text_color)
    return plate_h + 15


def main() -> int:
    root = project_root()
    font_path = str(root / "Montserrat-ExtraBold.ttf")
    
    # Набор сочных 3D фонов и ярких кликбейтных заголовочных конструкций
    covers_data = [
        {
            "id": "B01",
            "dir": "memory/blog/articles/B01-n8n-pervichka-iz-pochty-finansist",
            "bg_url": "https://tempfile.aiquickdraw.com/r/6dd458b75180b3f34de531246a671b8b_1781730488_wxu1qchc.png",
            "line1": "АВТОМАТИЗАЦИЯ БЕЗ КОДА",
            "line2": "СЧЕТА ИЗ ПОЧТЫ",
            "line3": "ЗА ВЕЧЕР В n8n!"
        },
        {
            "id": "B02",
            "dir": "memory/blog/articles/B02-avtomatizaciya-n8n-ai-agents",
            "bg_url": "https://tempfile.aiquickdraw.com/workers/images/image_1781707654943_qxpwnc.png",
            "line1": "ИИ-АГЕНТЫ В ДЕЛЕ",
            "line2": "РОБОТ ЗА ВЕЧЕР",
            "line3": "БЕЗ РАЗРАБОТЧИКОВ!"
        },
        {
            "id": "B03",
            "dir": "memory/blog/articles/B03-podklyuchenie-mcp-cursor",
            "bg_url": "https://tempfile.aiquickdraw.com/workers/images/image_1781707644335_oe03p0.png",
            "line1": "УМНЫЙ РЕДАКТОР",
            "line2": "CURSOR + MCP",
            "line3": "ПОДКЛЮЧИ ЗА 20 МИНУТ!"
        },
        {
            "id": "B04",
            "dir": "memory/blog/articles/B04-geo-optimizaciya-sajta-2026",
            "bg_url": "https://tempfile.aiquickdraw.com/workers/images/image_1781707648650_8zptqn.png",
            "line1": "SEO НОВОГО ПОКОЛЕНИЯ",
            "line2": "GEO ОПТИМИЗАЦИЯ",
            "line3": "КАК ПОПАСТЬ В AI-ОТВЕТЫ!"
        },
        {
            "id": "B05",
            "dir": "memory/blog/articles/B05-avtonomnyj-kontent-zavod-nejroseti",
            "bg_url": "https://tempfile.aiquickdraw.com/ggc/916476d790009aca2ed1a676c5cb6978_1781707694443.png",
            "line1": "ИИ-КОНТЕНТ ЗАВОД",
            "line2": "АВТОНОМНЫЕ ПОСТЫ",
            "line3": "НАПИСАНО НЕЙРОСЕТЯМИ!"
        }
    ]

    for item in covers_data:
        article_dir = root / item["dir"]
        if not article_dir.exists():
            print(f"Skipping {item['id']} - directory not found: {article_dir}")
            continue

        print(f"\nProcessing {item['id']} cover in Artur-style...")
        cover_dir = article_dir / "cover"
        cover_dir.mkdir(parents=True, exist_ok=True)

        # 1. Загружаем и масштабируем красивый 3D фон
        bg = download_image(item["bg_url"]).convert("RGBA")
        bg = bg.resize((1200, 675), Image.Resampling.LANCZOS)
        
        # Накладываем легкий темный оверлей на правую часть изображения, чтобы текст выглядел контрастно и дорого
        overlay = Image.new("RGBA", (1200, 675), (0, 0, 0, 0))
        o_draw = ImageDraw.Draw(overlay)
        for x in range(500, 1200):
            # Чем правее, тем темнее. Максимальное затемнение 150 (из 255) в самом правом углу.
            alpha = int(150 * ((x - 500) / 700))
            o_draw.line([(x, 0), (x, 675)], fill=(5, 5, 10, alpha))
            
        bg = Image.alpha_composite(bg, overlay)
        draw = ImageDraw.Draw(bg)
        
        # Шрифты: супер-жирные, крупные, сочные
        font_badge = ImageFont.truetype(font_path, 22)
        font_h2 = ImageFont.truetype(font_path, 64)
        font_h3 = ImageFont.truetype(font_path, 46)
        font_brand = ImageFont.truetype(font_path, 26)
        
        # Текст выравниваем по правому краю, оставляя левую половину под красивый 3D рендер
        start_y = 150
        x_pos = 550  
        
        # Строка 1: Изящный фиолетовый бейдж категории
        h1 = draw_text_plate(
            draw,
            item["line1"],
            font=font_badge,
            pos_x=x_pos,
            pos_y=start_y,
            text_color=(255, 255, 255, 255),
            bg_color=(139, 92, 246, 255),  # #8b5cf6 (светлый фиолетовый KODA)
            padding_x=16,
            padding_y=8,
            border_radius=6,
        )
        start_y += h1 + 15
        
        # Строка 2: Огромный чистый белый заголовок с тенью и тонким контуром
        draw_youtube_text(
            draw,
            item["line2"],
            (x_pos, start_y),
            font_h2,
            text_color=(255, 255, 255, 255), # Белый
            stroke_color=(15, 15, 25, 255),
            stroke_width=8,
            shadow_radius=6,
        )
        start_y += 88
        
        # Строка 3: Ярко-лимонный призыв к действию / ключевой инсайт
        draw_youtube_text(
            draw,
            item["line3"],
            (x_pos, start_y),
            font_h3,
            text_color=(253, 224, 71, 255), # #fde047 (Сочный лимонно-желтый)
            stroke_color=(15, 15, 25, 255),
            stroke_width=8,
            shadow_radius=6,
        )
        start_y += 82
        
        # Строка 4: Ссылка на твой бренд koda-fd.ru под заголовками
        draw_youtube_text(
            draw,
            "koda-fd.ru",
            (x_pos, start_y),
            font_brand,
            text_color=(167, 139, 250, 220), # #a78bfa (полупрозрачный нежно-фиолетовый)
            stroke_color=(15, 15, 25, 220),
            stroke_width=5,
            shadow_radius=4,
        )

        # Сохраняем обложку в папку статьи
        final_cover_path = cover_dir / "cover.png"
        bg.convert("RGB").save(final_cover_path, "PNG")
        print(f"OK cover saved: {final_cover_path}")

        # Сохраняем обложку в папку экспорта Дзена
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
