# Promotion checklist — B92 mcp-google-sheets-cursor-reestry

Дата публикации: YYYY-MM-DD  
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

• Path B: mcp-gsheets + service account, share только рабочего файла
• mcp.json → MCP Logs → сценарий find → update → re-read
• Без копипаста диапазонов и без сырых ПДн в истории чата

Читать: https://koda-fd.ru/blog/mcp-google-sheets-cursor-reestry/
```

## Перелинковка

- [ ] Добавить ссылку на новый пост с главной blog section (если Aurora не auto)
- [ ] Обновить 1–2 старых поста → link to new (если есть): кандидаты B03, B21, B82 (ручные анкоры, не «2026»)

## Метрики (7 дней)

- [ ] Metrika / GA4 — goal `blog_read` или из conversion map
- [ ] Позиция primary query (ручная проверка / Wordstat)

## Notes

- Indexer: `excalibur_blog_interlinker.py --apply --blog-dir memory/blog/articles --site-base https://koda-fd.ru` (CLI без `--article-dir`); opportunities=380, auto-apply дал 30 вставок анкора «2026» → `/blog/reestr-dogovorov-google-sheets/` — **откатил** (коллизия secondary_queries «2026»; как у B59).
- B92 `article.html`: сохранены ручные internal links writer → `mcp-cursor-finansist-instrumenty`, `google-sheets-api-integraciya-finotdel`, `avtomatizaciya-finansov-no-code`, `obezlichivanie-dannyh-chatgpt-finansist`. Новых полезных auto-links нет.
- Report: `interlink-report.json` в article_dir.
- `memory/blog/llms.txt` + `llms-full.txt`: 44 статьи, B92 в индексе (site-base https://koda-fd.ru).
- publish: pending после Indexer.
