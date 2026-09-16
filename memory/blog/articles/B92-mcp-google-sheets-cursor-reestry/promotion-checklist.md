# Promotion checklist — B92 mcp-google-sheets-cursor-reestry

Дата публикации: YYYY-MM-DD (pending publish)  
Live URL: https://koda-fd.ru/blog/mcp-google-sheets-cursor-reestry/

Excalibur создаёт этот файл после `✅ ARTICLE OK` (до или после WP publish).

## Сразу после publish

- [ ] Открыть live URL — title, excerpt, featured image, FAQ
- [ ] View source — JSON-LD BlogPosting + FAQPage (theme или plugin)
- [ ] Проверить internal links из статьи (200)
- [ ] Яндекс.Вебмастер / GSC — URL отправлен (если настроено)

## Соцсети / каналы (из conversion-tracking-map)

| Канал | Действие | Статус |
|-------|----------|--------|
| Telegram | Пост: hook + ссылка + 1 факт из статьи | ☐ |
| VK / Max | Адаптировать под ЦА | ☐ |
| Email / рассылка | Если есть в conversion map | ☐ |

## Snippet для Telegram (черновик)

```
Реестр договоров снова уезжает в чат Cursor кусками? MCP Google Sheets — агент сам читает и обновляет строки по doc_key.

• Path B: mcp-gsheets + service account (share одного файла)
• mcp.json → зелёный статус + MCP Logs
• Сценарий: найти → update → перечитать

Читать: https://koda-fd.ru/blog/mcp-google-sheets-cursor-reestry/
```

## Перелинковка

- [ ] Добавить ссылку на новый пост с главной blog section (если Aurora не auto)
- [x] Обновить 1–2 старых поста → link to new (если есть)
  - B21 → B92 (MCP Google Sheets для реестров)
  - B82 → B92 (гайде MCP Google Sheets)
  - B51 → B92 (MCP Google Sheets)
  - B92 → B51 (реестр договоров)

## Метрики (7 дней)

- [ ] Metrika / GA4 — goal `blog_read` или из conversion map
- [ ] Позиция primary query (ручная проверка / Wordstat)

## Notes

- Indexer 2026-09-16: blind `--apply` откатан (false-positive якоря `2026`); strip secondary `2026` из 13 metas → dry-run 2 non-B92 opps (`claude code`). Curated **4** links.
- CLI: `excalibur_blog_interlinker.py --blog-dir` (нет `--article-dir`); llms: `--out-dir memory/blog --site-base https://koda-fd.ru`.
- llms.txt / llms-full.txt: 44 статьи, B92 присутствует.
- Report: `memory/blog/interlink-suggestions-B92.json`
- publish 2026-09-16: **❌ PUBLISH BLOCKER** — нет `memory/site.env.local` / `EXCALIBUR_BLOG_ALLOW_PUBLISH=yes` / FTP_* / PUBLIC_SITE_URL. Live URL выше — **planned**, не confirmed live. Ledger не обновлён.
