# Promotion checklist — B92 mcp-google-sheets-cursor-reestry

Дата публикации: YYYY-MM-DD  
Live URL: *(unpublished — заполнить после WP publish)*

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
- [x] Inbound B03 / B21 / B51 / B82 → B92 (Indexer 2026-09-24)
- [x] Outbound B92 → B51 / B58 / B83 / B59 (+ B82 в next-steps; уже были B21/B82/no-code/обезличивание)

## Метрики (7 дней)

- [ ] Metrika / GA4 — goal `blog_read` или из conversion map
- [ ] Позиция primary query «mcp google sheets cursor» (ручная проверка / Wordstat)

## Notes

Indexer 2026-09-24: dry-run до strip показал массовые матчи по голому «2026» → **не** blind `--apply`. Strip `2026` из 13 `secondary_queries`; восстановлен фильтр `is_usable_keyword` + `--article-dir` в interlinker. Scoped `--apply` B92 → 0 авто-вставок. Curated inbound B03/B21/B51/B82 → B92; outbound реестры B51/B58/B83/B59 + B82 в next-steps. Corpus `--apply` → 2× «claude code» (B23/B28→B04). llms.txt/llms-full.txt → `memory/blog/` (B92 есть). Live URL пуст до publish.
