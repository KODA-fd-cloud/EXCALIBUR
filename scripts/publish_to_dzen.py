#!/usr/bin/env python3
"""Скрипт для полной автоматической публикации статьи в Яндекс.Дзен через WordPress Uploads SFTP."""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
from pathlib import Path
import paramiko


def project_root() -> Path:
    env_root = os.environ.get("EXCALIBUR_PROJECT_ROOT", "").strip()
    if env_root:
        return Path(env_root)
    return Path(__file__).resolve().parents[1]


def sftp_upload(local_path: Path, remote_path: str, sftp: paramiko.SFTPClient) -> None:
    print(f"Uploading {local_path.name} to remote {remote_path}...")
    sftp.put(str(local_path), remote_path)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--article-dir", required=True, help="Путь к папке статьи, например, memory/blog/articles/B01-...")
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
    slug = meta.get("slug", article_dir.name)

    # 1. SSH/SFTP Подключение
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

    # Создаем папку dzen внутри WordPress uploads
    remote_base_dir = "/var/lib/docker/volumes/blog_blog_wp/_data/wp-content/uploads/dzen"
    try:
        sftp.mkdir(remote_base_dir)
    except Exception:
        pass # Уже существует

    # 2. Загружаем изображения статьи на сервер
    cover_src_dir = article_dir / "cover"
    
    # Справочник имен файлов на сервере
    remote_images = {}
    for name in ("cover.png", "inline-01.png", "inline-02.png", "inline-03.png"):
        local_img = cover_src_dir / name
        if local_img.is_file():
            remote_name = f"{topic_id}_{name}"
            remote_path = f"{remote_base_dir}/{remote_name}"
            sftp_upload(local_img, remote_path, sftp)
            remote_images[name] = f"https://koda-fd.ru/blog/wp-content/uploads/dzen/{remote_name}"

    # 3. Читаем и парсим html статьи, заменяя картинки на публичные HTTPS ссылки
    html_content = html_path.read_text(encoding="utf-8")
    
    # Удаляем верхний блок cover-figure
    html_content = re.sub(
        r'<figure class="cover-quad"[^>]*>.*?</figure>\s*',
        '',
        html_content,
        count=1,
        flags=re.DOTALL,
    )

    # Заменяем inline картинки на их публичные пути
    for local_name, public_url in remote_images.items():
        if "inline" in local_name:
            html_content = html_content.replace(f"images/{local_name}", public_url)
            html_content = html_content.replace(f"cover/{local_name}", public_url)

    # Добавляем обложку в самый конец статьи, чтобы Дзен распознал ее и позволил выбрать при публикации
    if "cover.png" in remote_images:
        html_content += f'\n<p>---</p><p><b>Рекомендуемая обложка для публикации:</b></p><p><img src="{remote_images["cover.png"]}" alt="Обложка KODA"></p>'

    # 4. Генерируем Javascript-код для вставки текста и картинок в Дзен
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

    # Загружаем JS-код на сервер как dzen_payload.js в папку dzen
    remote_js_path = f"{remote_base_dir}/dzen_payload.js"
    print(f"Uploading dzen_payload.js to {remote_js_path}...")
    with sftp.open(remote_js_path, "w") as f:
        f.write(js_code)

    sftp.close()
    ssh.close()
    print("Done! All assets uploaded successfully.")
    
    # Ссылка на файл скрипта
    eval_command = "fetch('https://koda-fd.ru/blog/wp-content/uploads/dzen/dzen_payload.js').then(r => r.text()).then(eval)"
    print("\nФИНАЛЬНЫЙ КОМАНДНЫЙ СТРОК ДЛЯ ИНЖЕКТА В БРАУЗЕРЕ:")
    print(eval_command)
    
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
