# Promotion checklist — B92 mcp-google-sheets-cursor-reestry

Дата публикации: 2026-08-29 (pending publish)  
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
Реестр снова уезжает в чат Cursor кусками, а ячейки сверяете вручную?

• MCP Google Sheets + mcp-gsheets на service account за 1–2 часа
• Сценарий: найти строку по doc_key → update status → перечитать
• Path B для production; Path A OAuth — только пилот

Читать: https://koda-fd.ru/blog/mcp-google-sheets-cursor-reestry/
```

## Перелинковка

- [ ] Добавить ссылку на новый пост с главной blog section (если Aurora не auto)
- [x] Обновить 1–2 старых поста → link to new (B21 hub, B82 Sheets API)

## Метрики (7 дней)

- [ ] Metrika / GA4 — goal `blog_read` или из conversion map
- [ ] Позиция primary query «mcp google sheets cursor» (ручная проверка / Wordstat)

## Notes

- Indexer: CLI без `--article-dir`; dry-run `--blog-dir memory/blog/articles --site-base https://koda-fd.ru`. Full `--apply` **не** запускали: auto-матчи B92→* только по secondary `2026` (junk).
- Исходящие из B92: **+3** контекстных (B51 договоры, B58 УПД, B83 SaaS) в next-steps; уже были B21, B82, no-code, обезличивание.
- Входящие на B92: **+2** (B21 next-steps, B82 next-steps).
- `memory/blog/llms.txt` + `llms-full.txt` обновлены (44 статьи, site-base https://koda-fd.ru), B92 в индексе.
- publish: pending (после Indexer).
