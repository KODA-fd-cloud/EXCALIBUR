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
Реестр снова уезжает в чат Cursor кусками? MCP Google Sheets — розетка: агент сам читает и обновляет строки по doc_key.

• Path B: mcp-gsheets + service account, share только реестра
• mcp.json → зелёный статус + проверка через MCP Logs
• Сценарий find → update status → re-read за 1–2 часа

Читать: https://koda-fd.ru/blog/mcp-google-sheets-cursor-reestry/
```

## Перелинковка

- [ ] Добавить ссылку на новый пост с главной blog section (если Aurora не auto)
- [ ] Обновить 1–2 старых поста → link to new (если есть): кандидаты B21 (`mcp-cursor-finansist-instrumenty`), B82 (`google-sheets-api-integraciya-finotdel`)

## Метрики (7 дней)

- [ ] Metrika / GA4 — goal `blog_read` или из conversion map
- [ ] Позиция primary query `mcp google sheets cursor` (ручная проверка / Wordstat)

## Notes

- Indexer: **без blind `--apply`** после strip `2026` из secondary_queries (14 metas). Accidental `--apply` до strip → откат year-anchors.
- Curated 4 links: B21→B92, B82→B92, B51→B92, B92→B51. Отчёт: `memory/blog/interlink-suggestions-B92.json`.
- В B92 также сохранены ручные links: `mcp-cursor-finansist-instrumenty`, `google-sheets-api-integraciya-finotdel`, `avtomatizaciya-finansov-no-code`, `obezlichivanie-dannyh-chatgpt-finansist`.
- llms.txt / llms-full.txt обновлены в `memory/blog/` (site-base https://koda-fd.ru), 44 статьи, B92 в индексе.
- ready_for_publish: yes (cover + schema уже PASS).
