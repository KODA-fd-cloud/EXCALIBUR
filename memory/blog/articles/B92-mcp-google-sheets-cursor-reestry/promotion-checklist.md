# Promotion checklist — B92 mcp-google-sheets-cursor-reestry

Дата публикации: 2026-09-04 (pending WP)  
Live URL: https://koda-fd.ru/blog/mcp-google-sheets-cursor-reestry/ (заполнить после publish)

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
Реестр снова копипастите в Cursor кусками? MCP Google Sheets правит строку по doc_key без диапазонов.

• Path B (mcp-gsheets + SA) — production-default
• Share файла → mcp.json → find → update → перечитка
• Path A OAuth — только пилот (cursor:// часто ломается)

Читать: https://koda-fd.ru/blog/mcp-google-sheets-cursor-reestry/
```

## Перелинковка

- [ ] Добавить ссылку на новый пост с главной blog section (если Aurora не auto)
- [ ] Обновить 1–2 старых поста → link to new (если есть): кандидаты B21, B82, B51

## Метрики (7 дней)

- [ ] Metrika / GA4 — goal `blog_read` или из conversion map
- [ ] Позиция primary query «mcp google sheets cursor» (ручная проверка / Wordstat)

## Notes

- Indexer **safe mode**: dry-run interlinker (11 suggestions для B92 — все junk-якорь `2026` из secondary_queries) → `--apply` по корпусу **не** запускался.
- Manual outbound добавлены на published slugs: B13, B51, B58, B83, B59, B23 (уже были B21, B82, B11, LEGACY no-code). B03 не линковать (404 live).
- `memory/blog/llms.txt` + `llms-full.txt` обновлены (`--out-dir memory/blog`, site-base https://koda-fd.ru); B92 в индексе.
- publish: pending (после Indexer).
