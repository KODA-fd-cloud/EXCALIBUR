#!/usr/bin/env python3
"""Генератор JS-нагрузки для полной автоматической вставки статьи в Дзен."""

from __future__ import annotations

import base64
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def file_to_base64(path: Path) -> str:
    return base64.b64encode(path.read_bytes()).decode('utf-8')


def main() -> None:
    if len(sys.argv) < 2:
        print("Usage: python scripts/excalibur_blog_dzen_generate_payload.py <article-dir>")
        sys.exit(1)

    article_dir = ROOT / sys.argv[1]
    if not article_dir.is_dir():
        print(f"Error: directory not found {article_dir}")
        sys.exit(1)

    meta_path = article_dir / 'article.meta.json'
    html_path = article_dir / 'article.html'
    if not meta_path.is_file() or not html_path.is_file():
        print("Error: article.meta.json or article.html missing")
        sys.exit(1)

    meta = json.loads(meta_path.read_text(encoding='utf-8'))
    slug = meta.get('slug', article_dir.name)
    topic_id = meta.get('topic_id', '')

    html_content = html_path.read_text(encoding='utf-8')

    # Находим изображения
    cover_src_dir = article_dir / 'cover'
    
    # Кодируем изображения в base64
    cover_b64 = file_to_base64(cover_src_dir / 'cover.png') if (cover_src_dir / 'cover.png').is_file() else ''
    inline1_b64 = file_to_base64(cover_src_dir / 'inline-01.png') if (cover_src_dir / 'inline-01.png').is_file() else ''
    inline2_b64 = file_to_base64(cover_src_dir / 'inline-02.png') if (cover_src_dir / 'inline-02.png').is_file() else ''
    inline3_b64 = file_to_base64(cover_src_dir / 'inline-03.png') if (cover_src_dir / 'inline-03.png').is_file() else ''

    # Разбираем HTML статьи на блоки, разделяя по <figure> с изображениями
    # Регулярное выражение для поиска тегов figure
    figure_regex = r'<figure class="[^"]*"(?: data-slot="([^"]*)")?>.*?</figure>'
    
    # Разобьем по figure
    parts = re.split(figure_regex, html_content, flags=re.DOTALL)
    
    blocks = []
    # parts будет чередоваться: [текст, имя_слота (или None), текст, имя_слота, ...]
    # Если figure не имела data-slot, то группа будет None.
    # Давайте сделаем более надежно: найдем все совпадения и разделим текст
    
    matches = list(re.finditer(figure_regex, html_content, flags=re.DOTALL))
    
    last_idx = 0
    for match in matches:
        # Добавляем текстовый блок перед figure
        text_before = html_content[last_idx:match.start()].strip()
        if text_before:
            blocks.append({"type": "html", "content": text_before})
            
        # Определяем, какая это картинка
        figure_tag = match.group(0)
        if 'inline-01.png' in figure_tag or 'inline_1' in figure_tag:
            blocks.append({"type": "image", "name": "inline-01.png", "b64": inline1_b64})
        elif 'inline-02.png' in figure_tag or 'inline_2' in figure_tag:
            blocks.append({"type": "image", "name": "inline-02.png", "b64": inline2_b64})
        elif 'inline-03.png' in figure_tag or 'inline_3' in figure_tag:
            blocks.append({"type": "image", "name": "inline-03.png", "b64": inline3_b64})
        elif 'cover.png' in figure_tag:
            blocks.append({"type": "image", "name": "cover.png", "b64": cover_b64})
            
        last_idx = match.end()
        
    # Добавляем финальный текстовый блок
    text_after = html_content[last_idx:].strip()
    if text_after:
        blocks.append({"type": "html", "content": text_after})

    # Добавляем обложку в самый конец статьи, чтобы Дзен позволил выбрать ее в качестве обложки публикации
    if cover_b64:
        blocks.append({"type": "html", "content": "<p>---</p><p><b>Обложка публикации (рекомендуемый вид превью):</b></p>"})
        blocks.append({"type": "image", "name": "cover.png", "b64": cover_b64})

    # Генерируем Javascript-код
    js_code = """
(async () => {
  const sleep = (ms) => new Promise(resolve => setTimeout(resolve, ms));
  const editors = document.querySelectorAll('.public-DraftEditor-content');
  if (editors.length < 2) return 'Error: Editor not found';
  const editor = editors[1];

  // Очистим редактор перед вставкой
  editor.focus();
  document.execCommand('selectAll', false, null);
  document.execCommand('delete', false, null);
  await sleep(300);

  function base64ToFile(base64, filename, mimeType) {
    const byteCharacters = atob(base64);
    const byteNumbers = new Array(byteCharacters.length);
    for (let i = 0; i < byteCharacters.length; i++) {
      byteNumbers[i] = byteCharacters.charCodeAt(i);
    }
    const byteArray = new Uint8Array(byteNumbers);
    const blob = new Blob([byteArray], {type: mimeType});
    return new File([blob], filename, {type: mimeType});
  }

  function pasteHtml(html, text) {
    const dt = new DataTransfer();
    dt.setData('text/html', html);
    dt.setData('text/plain', text);
    const pasteEvent = new ClipboardEvent('paste', {
      clipboardData: dt,
      bubbles: true,
      cancelable: true
    });
    editor.dispatchEvent(pasteEvent);
  }

  function pasteImage(file) {
    const dt = new DataTransfer();
    dt.items.add(file);
    const pasteEvent = new ClipboardEvent('paste', {
      clipboardData: dt,
      bubbles: true,
      cancelable: true
    });
    editor.dispatchEvent(pasteEvent);
  }
"""

    for idx, block in enumerate(blocks):
        if block["type"] == "html":
            # Экранируем переносы строк и кавычки для JS-строки
            clean_html = block["content"].replace('\\', '\\\\').replace('`', '\\`').replace('$', '\\$')
            # Удалим лишние переносы строк и пробелы для компактности
            clean_html = re.sub(r'\s+', ' ', clean_html)
            js_code += f"\n  // Block {idx}: HTML text\n"
            js_code += f"  pasteHtml(`{clean_html}`, '');\n"
            js_code += "  await sleep(400);\n"
        elif block["type"] == "image":
            if not block["b64"]:
                continue
            js_code += f"\n  // Block {idx}: Image {block['name']}\n"
            js_code += f"  pasteImage(base64ToFile('{block['b64']}', '{block['name']}', 'image/png'));\n"
            js_code += "  await sleep(1500);\n" # Даем больше времени на парсинг и загрузку картинки

    js_code += """
  return 'Success: Article fully inserted with images!';
})();
"""

    output_path = ROOT / "dzen_payload.js"
    output_path.write_text(js_code, encoding='utf-8')
    print(f"Generated payload size: {len(js_code)} bytes, saved to {output_path}")


if __name__ == '__main__':
    main()
