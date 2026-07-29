#!/usr/bin/env python3
"""Упаковка статьи Excalibur для ручной/полуавтоматической публикации в Дзен."""

from __future__ import annotations

import argparse
import json
import re
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def strip_cover_figure(html: str) -> str:
    return re.sub(
        r'<figure class="cover-quad"[^>]*>.*?</figure>\s*',
        '',
        html,
        count=1,
        flags=re.DOTALL,
    )


def main() -> None:
    parser = argparse.ArgumentParser(description='Dzen export pack from article_dir')
    parser.add_argument('--article-dir', required=True, help='memory/blog/articles/B01-slug')
    args = parser.parse_args()

    article_dir = (ROOT / args.article_dir).resolve()
    if not article_dir.is_dir():
        raise SystemExit(f'article_dir not found: {article_dir}')

    meta_path = article_dir / 'article.meta.json'
    html_path = article_dir / 'article.html'
    if not meta_path.is_file() or not html_path.is_file():
        raise SystemExit('article.meta.json or article.html missing')

    meta = json.loads(meta_path.read_text(encoding='utf-8'))
    slug = meta.get('slug', article_dir.name)
    topic_id = meta.get('topic_id', '')
    export_dir = ROOT / 'memory' / 'dzen-exports' / f'{topic_id}-{slug}' if topic_id else ROOT / 'memory' / 'dzen-exports' / slug
    images_dir = export_dir / 'images'

    if export_dir.exists():
        shutil.rmtree(export_dir)
    images_dir.mkdir(parents=True)

    cover_src = article_dir / 'cover'
    for name in ('cover.png', 'inline-01.png', 'inline-02.png', 'inline-03.png'):
        src = cover_src / name
        if src.is_file():
            shutil.copy2(src, images_dir / name)

    html = html_path.read_text(encoding='utf-8')
    body = strip_cover_figure(html)
    body = body.replace('src="cover/', 'src="images/')
    body = body.replace("src='cover/", "src='images/")

    ab = meta.get('meta_ab', {})
    title = ab.get('title_ctr') or ab.get('title_seo') or slug
    description = ab.get('description_seo') or ab.get('description_ctr') or ''

    (export_dir / 'TITLE.txt').write_text(title.strip() + '\n', encoding='utf-8')
    (export_dir / 'DESCRIPTION.txt').write_text(description.strip() + '\n', encoding='utf-8')
    (export_dir / 'BODY.html').write_text(body.strip() + '\n', encoding='utf-8')
    shutil.copy2(meta_path, export_dir / 'article.meta.json')

    readme = f"""# Дзен-экспорт: {title}

Канал: https://dzen.ru/automation_koda
Редактор: https://dzen.ru/profile/editor/automation_koda/publications

## Файлы

| Файл | Назначение |
|------|------------|
| TITLE.txt | заголовок в редакторе |
| DESCRIPTION.txt | подзаголовок / лид (если поле есть) |
| BODY.html | тело статьи (вставить в редактор) |
| images/cover.png | обложка публикации |
| images/inline-*.png | картинки внутри текста (по порядку в HTML) |

## Порядок в Дзен

1. Создать статью → вставить заголовок из TITLE.txt
2. Загрузить images/cover.png как обложку
3. Вставить BODY.html (или копировать блоками из article.html)
4. Для каждого `<img src="images/...">` — вставить соответствующий файл из images/
5. Опубликовать

После 5 статей на канале можно подключить RSS с блога koda-fd.ru/blog/
"""
    (export_dir / 'README.md').write_text(readme, encoding='utf-8')

    safe_title = title.encode('ascii', 'replace').decode('ascii')
    print(f'OK dzen export: {export_dir.relative_to(ROOT)}')
    print(f'TITLE={safe_title[:80]}')


if __name__ == '__main__':
    main()
