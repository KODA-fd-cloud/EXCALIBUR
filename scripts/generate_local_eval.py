#!/usr/bin/env python3
"""Локальный генератор чистого JS-инжекта для Dzen без базовой разметки Base64."""

from __future__ import annotations

import json
import os
import re
import sys
from pathlib import Path


def project_root() -> Path:
    env_root = os.environ.get("EXCALIBUR_PROJECT_ROOT", "").strip()
    if env_root:
        return Path(env_root)
    return Path(__file__).resolve().parents[1]


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--article-dir", required=True)
    args = ap.parse_args()

    root = project_root()
    article_dir = Path(args.article_dir)
    if not article_dir.is_absolute():
        article_dir = root / article_dir

    meta_path = article_dir / "article.meta.json"
    html_path = article_dir / "article.html"
    if not meta_path.is_file() or not html_path.is_file():
        print("Error: article.meta.json or article.html missing")
        return 1

    meta = json.loads(meta_path.read_text(encoding="utf-8"))
    topic_id = meta.get("topic_id", "BXX")

    html_content = html_path.read_text(encoding="utf-8")
    
    # Удаляем верхний блок cover-figure
    html_content = re.sub(
        r'<figure class="cover-quad"[^>]*>.*?</figure>\s*',
        '',
        html_content,
        count=1,
        flags=re.DOTALL,
    )

    # Заменяем относительные пути картинок на публичные пути на сервере koda-fd.ru
    for name in ("inline-01.png", "inline-02.png", "inline-03.png"):
        public_url = f"https://koda-fd.ru/blog/wp-content/uploads/dzen/{topic_id}_{name}"
        html_content = html_content.replace(f"images/{name}", public_url)
        html_content = html_content.replace(f"cover/{name}", public_url)

    # Добавляем обложку в самый конец статьи
    cover_url = f"https://koda-fd.ru/blog/wp-content/uploads/dzen/{topic_id}_cover.png"
    html_content += f'\n<p>---</p><p><b>Рекомендуемая обложка для публикации:</b></p><p><img src="{cover_url}" alt="Обложка KODA"></p>'

    # Экранируем переносы строк и кавычки для JS-строки
    clean_html = html_content.replace('\\', '\\\\').replace('`', '\\`').replace('$', '\\$')
    clean_html = re.sub(r'\s+', ' ', clean_html)  # компактность

    js_template = """
(async () => {
  const sleep = (ms) => new Promise(resolve => setTimeout(resolve, ms));
  const editors = document.querySelectorAll('.public-DraftEditor-content');
  if (editors.length < 2) return 'Error: Editor not found';
  const editor = editors[1];

  // 1. Очищаем редактор
  editor.focus();
  document.execCommand('selectAll', false, null);
  document.execCommand('delete', false, null);
  await sleep(300);

  // 2. Вставляем весь HTML статьи (включая картинки с HTTPS путями) через insertHTML
  const htmlContent = `__ARTICLE_HTML__`;
  document.execCommand('insertHTML', false, htmlContent);
  await sleep(1500);

  return 'Success: Article fully uploaded to Yandex Dzen editor!';
})();
"""
    js_code = js_template.replace("__ARTICLE_HTML__", clean_html)

    output_path = root / f"dzen_{topic_id}_eval.js"
    output_path.write_text(js_code, encoding="utf-8")
    print(f"SUCCESS: Generated local JS eval file: {output_path}")
    return 0


if __name__ == "__main__":
    import argparse
    raise SystemExit(main())
