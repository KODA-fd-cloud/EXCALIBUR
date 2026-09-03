# Promotion checklist — B92 mcp-google-sheets-cursor-reestry

Дата публикации: YYYY-MM-DD  
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
Реестр в Sheets снова уезжает в Cursor кусками? MCP Google Sheets убирает копипаст.

• Path B: mcp-gsheets + service account, share одного файла
• Сценарий find → update → re-read по doc_key
• MCP Logs, allowlist write-tools, без сырых ПДн

Читать: https://koda-fd.ru/blog/mcp-google-sheets-cursor-reestry/
```

## Перелинковка

- [ ] Добавить ссылку на новый пост с главной blog section (если Aurora не auto)
- [ ] Обновить 1–2 старых поста → link to new (если есть): кандидаты B03 / B21 / B82

## Метрики (7 дней)

- [ ] Metrika / GA4 — goal `blog_read` или из conversion map
- [ ] Позиция primary query «mcp google sheets cursor» (ручная проверка / Wordstat)

## Notes

Indexer: dry-run interlinker — 11 outbound из B92 и десятки inbound по корпусу с keyword «2026» (junk из secondary_queries). `--apply` не запускали. Ручные outbound в B92: уже были B21/B82/no-code/обезличивание; добавлены B03 (`/blog/podklyuchenie-mcp-cursor/`) и B51 (`/blog/reestr-dogovorov-google-sheets/`). `memory/blog/llms.txt` + `llms-full.txt` — 44 статьи, B92 в индексе (site-base https://koda-fd.ru).
