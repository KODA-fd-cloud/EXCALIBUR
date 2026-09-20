# Promotion checklist — B92 mcp-google-sheets-cursor-reestry

Дата публикации: — (publish blocker 2026-09-20)  
Live URL: — (ожидает publish; целевой slug: /blog/mcp-google-sheets-cursor-reestry/)

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
Реестр снова уезжает в чат Cursor кусками? MCP Google Sheets — розетка: агент сам читает и обновляет строки по doc_key.

• Path B: mcp-gsheets + service account, share только рабочего файла
• DoD: найти строку → обновить status → перечитать через MCP Logs
• 1–2 часа на setup без копипаста диапазонов

Читать: https://koda-fd.ru/blog/mcp-google-sheets-cursor-reestry/
```

## Перелинковка

- [ ] Добавить ссылку на новый пост с главной blog section (если Aurora не auto)
- [ ] Обновить 1–2 старых поста → link to new (если есть)

## Метрики (7 дней)

- [ ] Metrika / GA4 — goal `blog_read` или из conversion map
- [ ] Позиция primary query (ручная проверка / Wordstat)

## Notes

- Indexer: CLI interlinker без `--article-dir` → `python3 scripts/excalibur_blog_interlinker.py --apply --blog-dir memory/blog/articles`.
- Auto-apply дал ложные якоря «2026» (из secondary_queries B92) → откат всех HTML-диффов; оставлены ручные internal links в B92: `mcp-cursor-finansist-instrumenty`, `google-sheets-api-integraciya-finotdel`, `avtomatizaciya-finansov-no-code`, `obezlichivanie-dannyh-chatgpt-finansist`.
- Рекомендация: убрать `"2026"` из `secondary_queries` в meta (не indexer-зона rewrite).
- llms.txt / llms-full.txt обновлены в `memory/blog/` (site-base https://koda-fd.ru), B92 в индексе.
- interlink-report: `memory/blog/articles/B92-mcp-google-sheets-cursor-reestry/interlink-report.json`
- publish: ❌ PUBLISH BLOCKER 2026-09-20 — нет site.env.local / EXCALIBUR_BLOG_ALLOW_PUBLISH / PUBLIC_SITE_URL / FTP_*|SSH_*; link-verify pass + dry-run OK; Live URL не выставлен.
