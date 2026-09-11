# Promotion checklist — B92 mcp-google-sheets-cursor-reestry

Дата публикации: 2026-09-11  
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
Реестр снова копипастом в чат Cursor? MCP Google Sheets читает и обновляет строки по doc_key без диапазонов.

• Path B: mcp-gsheets + service account, share только рабочего файла
• mcp.json → MCP Logs → find / update / re-read по doc_key
• DoD за 1–2 часа: статус сменён, результат перечитан

Читать: https://koda-fd.ru/blog/mcp-google-sheets-cursor-reestry/
```

## Перелинковка

- [ ] Добавить ссылку на новый пост с главной blog section (если Aurora не auto)
- [ ] Обновить 1–2 старых поста → link to new (если есть)

## Метрики (7 дней)

- [ ] Metrika / GA4 — goal `blog_read` или из conversion map
- [ ] Позиция primary query (ручная проверка / Wordstat)

## Notes

- Indexer: interlinker `--apply --blog-dir memory/blog/articles --site-base https://koda-fd.ru` (CLI без `--article-dir`); auto-links по secondary_query «2026» сняты (false year anchors); в B92 остаются 4 ручных hub-ссылки: `mcp-cursor-finansist-instrumenty`, `google-sheets-api-integraciya-finotdel`, `avtomatizaciya-finansov-no-code`, `obezlichivanie-dannyh-chatgpt-finansist`.
- «2026» убран из secondary_queries у B92 и 12 других meta (в т.ч. B51/B59), чтобы не повторять ложные якоря.
- llms.txt / llms-full.txt обновлены в `memory/blog/` (site-base https://koda-fd.ru), B92 в индексе.
- publish: pending (не запускался indexer'ом).
