#!/usr/bin/env python3
"""Скрипт для сборки красивой HTML-страницы предпросмотра статьи, которую пользователь может открыть, скопировать и вставить в Дзен."""

from __future__ import annotations

import os
import re
import json
from pathlib import Path
import paramiko


def project_root() -> Path:
    env_root = os.environ.get("EXCALIBUR_PROJECT_ROOT", "").strip()
    if env_root:
        return Path(env_root)
    return Path(__file__).resolve().parents[1]


def main() -> int:
    root = project_root()
    article_dir = root / "memory/blog/articles/B01-n8n-pervichka-iz-pochty-finansist"
    html_path = article_dir / "article.html"
    meta_path = article_dir / "article.meta.json"

    if not html_path.is_file() or not meta_path.is_file():
        print("Error: article files not found")
        return 1

    meta = json.loads(meta_path.read_text(encoding="utf-8"))
    topic_id = meta.get("topic_id", "B01")

    # Читаем HTML
    raw_html = html_path.read_text(encoding="utf-8")

    # Удаляем верхний блок cover-figure
    clean_html = re.sub(
        r'<figure class="cover-quad"[^>]*>.*?</figure>\s*',
        '',
        raw_html,
        count=1,
        flags=re.DOTALL,
    )

    # Заменяем относительные пути картинок на публичные пути на сервере koda-fd.ru
    for name in ("inline-01.png", "inline-02.png", "inline-03.png"):
        public_url = f"https://koda-fd.ru/blog/wp-content/uploads/dzen/{topic_id}_{name}"
        clean_html = clean_html.replace(f"images/{name}", public_url)
        clean_html = clean_html.replace(f"cover/{name}", public_url)

    # Добавляем обложку в самый конец статьи
    cover_url = f"https://koda-fd.ru/blog/wp-content/uploads/dzen/{topic_id}_cover.png"
    clean_html += f'\n<p>---</p><p><b>Рекомендуемая обложка для публикации (скачай её и установи в Дзене):</b></p><p><img src="{cover_url}" alt="Обложка KODA"></p>'

    # Оборачиваем в шаблон страницы с кнопкой быстрого копирования
    preview_template = f"""<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <title>Предпросмотр статьи {topic_id} для Дзена</title>
    <style>
        body {{
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
            line-height: 1.6;
            color: #333;
            max-width: 800px;
            margin: 40px auto;
            padding: 0 20px;
            background-color: #f9f9fb;
        }}
        .header-panel {{
            background-color: #2e1065;
            color: white;
            padding: 20px;
            border-radius: 12px;
            margin-bottom: 30px;
            box-shadow: 0 4px 12px rgba(0,0,0,0.1);
        }}
        .header-panel h1 {{
            margin-top: 0;
            font-size: 24px;
        }}
        .header-panel p {{
            margin-bottom: 15px;
            font-size: 15px;
            opacity: 0.9;
        }}
        .copy-btn {{
            background-color: #10b981;
            color: white;
            border: none;
            padding: 12px 24px;
            font-size: 16px;
            font-weight: bold;
            border-radius: 8px;
            cursor: pointer;
            transition: background-color 0.2s;
            display: inline-block;
        }}
        .copy-btn:hover {{
            background-color: #059669;
        }}
        .content-area {{
            background-color: white;
            padding: 40px;
            border-radius: 12px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.05);
            border: 1px solid #e5e7eb;
        }}
        img {{
            max-width: 100%;
            height: auto;
            border-radius: 8px;
            margin: 20px 0;
            display: block;
        }}
        table {{
            width: 100%;
            border-collapse: collapse;
            margin: 20px 0;
        }}
        th, td {{
            border: 1px solid #e5e7eb;
            padding: 12px;
            text-align: left;
        }}
        th {{
            background-color: #f3f4f6;
        }}
        blockquote {{
            border-left: 4px solid #8b5cf6;
            padding-left: 20px;
            margin: 20px 0;
            font-style: italic;
            color: #4b5563;
        }}
        h2 {{
            color: #111827;
            margin-top: 40px;
            font-size: 22px;
            border-bottom: 2px solid #f3f4f6;
            padding-bottom: 8px;
        }}
        h3 {{
            color: #1f2937;
            margin-top: 30px;
            font-size: 18px;
        }}
    </style>
    <script>
        function selectAndCopy() {{
            const range = document.createRange();
            range.selectNode(document.getElementById('article-content'));
            window.getSelection().removeAllRanges();
            window.getSelection().addRange(range);
            try {{
                document.execCommand('copy');
                alert('Статья успешно скопирована со всем форматированием и картинками! Теперь перейди в Дзен, нажми Ctrl+A, затем Delete, и затем Ctrl+V.');
            }} catch (err) {{
                alert('Не удалось скопировать автоматически. Пожалуйста, просто выдели текст на странице (Ctrl+A), скопируй его (Ctrl+C) и вставь в Дзен.');
            }}
        }}
    </script>
</head>
<body>

    <div class="header-panel">
        <h1>Инструкция по копированию статьи для Дзена</h1>
        <p>Для того чтобы статья перенеслась со 100% сохранением жирного шрифта, заголовков, таблиц и картинок:</p>
        <ol style="margin-bottom: 20px; padding-left: 20px; line-height: 1.5;">
            <li>Нажми зеленую кнопку <b>«Скопировать статью со всем форматированием»</b> ниже.</li>
            <li>Или просто выдели всё содержимое белого блока вручную (Ctrl+A) и скопируй его (Ctrl+C).</li>
            <li>Перейди во вкладку редактора Дзена, кликни в тело статьи, очисти старый текст (Ctrl+A -> Delete) и нажми вставить <b>(Ctrl+V)</b>.</li>
        </ol>
        <button class="copy-btn" onclick="selectAndCopy()">Скопировать статью со всем форматированием</button>
    </div>

    <div class="content-area" id="article-content">
        {clean_html}
    </div>

</body>
</html>
"""

    # Сохраняем локально
    preview_local_path = article_dir / "preview_dzen.html"
    preview_local_path.write_text(preview_template, encoding="utf-8")
    print(f"Generated local preview: {preview_local_path}")

    # Загружаем на сервер через SFTP
    host = "45.11.93.42"
    port = 22
    user = "root"
    password = "#X8R~mJp2hTr"

    print(f"Connecting to SSH {host}:{port}...")
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(host, port, user, password)
    sftp = ssh.open_sftp()
    print("Logged in successfully!")

    remote_path = f"/var/lib/docker/volumes/blog_blog_wp/_data/wp-content/uploads/dzen/preview_B01.html"
    print(f"Uploading preview to remote: {remote_path}")
    sftp.put(str(preview_local_path), remote_path)

    sftp.close()
    ssh.close()
    print("Done! Preview page is now live!")
    print("URL: https://koda-fd.ru/blog/wp-content/uploads/dzen/preview_B01.html")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
