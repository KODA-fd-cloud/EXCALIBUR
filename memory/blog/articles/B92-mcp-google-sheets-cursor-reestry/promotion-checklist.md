# Promotion checklist — B92 mcp-google-sheets-cursor-reestry

Дата публикации: 2026-09-13  
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
Реестр договоров снова уезжает в чат Cursor кусками? MCP Google Sheets — розетка: агент сам находит строку по doc_key и обновляет статус без копипаста.

• Path B: mcp-gsheets + service account (минимальный blast radius)
• DoD: найти → обновить → перечитать через MCP Logs
• Пилот 1–2 часа на один рабочий реестр

Читать: https://koda-fd.ru/blog/mcp-google-sheets-cursor-reestry/
```

## Перелинковка

- [ ] Добавить ссылку на новый пост с главной blog section (если Aurora не auto)
- [x] Обновить 1–2 старых поста → link to new (B21, B82, B51 → B92; B92 → B51)

## Метрики (7 дней)

- [ ] Metrika / GA4 — goal `blog_read` или из conversion map
- [ ] Позиция primary query (ручная проверка / Wordstat)

## Notes

- Indexer: CLI interlinker без `--article-dir` (`--blog-dir` + `--site-base https://koda-fd.ru`). Blind `--apply` дал false-positive якоря «2026» → откат; из 12 meta убран secondary `2026`.
- Curated **4** interlinks: inbound B21/B82/B51 → B92; outbound B92 → B51. В B92 также outbound на B21, B82, no-code, обезличивание (writer).
- llms.txt / llms-full.txt: `memory/blog/` (site-base https://koda-fd.ru), **44** статьи, B92 в индексе.
- publish: pending (после Indexer).
