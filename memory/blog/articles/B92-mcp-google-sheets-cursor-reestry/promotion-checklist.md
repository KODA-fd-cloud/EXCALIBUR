# Promotion checklist — B92 mcp-google-sheets-cursor-reestry

Дата публикации: 2026-09-08  
Live URL: https://koda-fd.ru/blog/mcp-google-sheets-cursor-reestry/ (после publish)

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
Реестр договоров снова кусками в чат Cursor? MCP Google Sheets правит строку по doc_key без копипаста.

• Path B: mcp-gsheets + service account на один файл
• Find → update status → re-read (DoD пилота)
• OAuth Marketplace — только для личного пилота

Читать: https://koda-fd.ru/blog/mcp-google-sheets-cursor-reestry/
```

## Перелинковка

- [ ] Добавить ссылку на новый пост с главной blog section (если Aurora не auto)
- [x] Обновить 1–2 старых поста → link to new (B82, B51, B21 → B92)

## Метрики (7 дней)

- [ ] Metrika / GA4 — goal `blog_read` или из conversion map
- [ ] Позиция primary query (ручная проверка / Wordstat)

## Notes

- Indexer: dry-run interlinker — 11 suggestions from B92, все junk-якоря `2026` → `--apply` не использовали.
- Manual outbound: B51, B58, B83, B59, B24, B80 (+ уже были B21, B82, no-code, обезличивание). B02/B03 не линковали (404 live).
- Reverse inbound: B82, B51, B21 → `/blog/mcp-google-sheets-cursor-reestry/`.
- llms.txt / llms-full.txt: `memory/blog/` (site-base https://koda-fd.ru), B92 в индексе.
- link-verify после interlink: PASS (13/13, failed_count=0).
