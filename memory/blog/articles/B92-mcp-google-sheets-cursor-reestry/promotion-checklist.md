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
Реестр снова уезжает в чат Cursor кусками? Подключите MCP Google Sheets и правьте строки по doc_key без копипаста.

• Path B: mcp-gsheets + service account за 1–2 часа
• Сценарий find → update → re-read с проверкой в MCP Logs
• Share только рабочего файла, без сырых ПДн в облако

Читать: https://koda-fd.ru/blog/mcp-google-sheets-cursor-reestry/
```

## Перелинковка

- [ ] Добавить ссылку на новый пост с главной blog section (если Aurora не auto)
- [ ] Обновить 1–2 старых поста → link to B92 (B03 MCP / B82 Sheets API / B21 MCP tools), если ещё нет inbound

## Метрики (7 дней)

- [ ] Metrika / GA4 — goal `blog_read` или из conversion map
- [ ] Позиция primary query «mcp google sheets cursor» (ручная проверка / Wordstat)

## Notes

Indexer 2026-09-23: interlinker `--apply --article-dir` → 0 авто-вставок (фильтр голого «2026» + keywords других статей не матчятся в body). Добавлены 3 контекстные ссылки в next-steps (B51/B58/B83; повтор на B82). Итого 8 internal `/blog/` links; bare year anchors = 0. `secondary_queries` без «2026». llms.txt/llms-full.txt → `memory/blog/` (44 статьи, B92 есть).
