# Promotion checklist — B92 mcp-google-sheets-cursor-reestry

Дата публикации: YYYY-MM-DD  
Live URL: https://koda-fd.ru/blog/mcp-google-sheets-cursor-reestry/ (placeholder до publish)

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
Реестр снова уезжает в чат Cursor кусками — а после правки вы вручную сверяете ячейки?

• MCP Google Sheets (mcp-gsheets + SA): агент читает и обновляет строку по doc_key
• Path B за 1–2 часа: Share файла, mcp.json, MCP Logs, find → update → re-read
• Без сырых ПДн и без Auto-run на write-tools

Читать: https://koda-fd.ru/blog/mcp-google-sheets-cursor-reestry/
```

## Перелинковка

- [ ] Добавить ссылку на новый пост с главной blog section (если Aurora не auto)
- [ ] Обновить 1–2 старых поста → link to new (если есть)

## Метрики (7 дней)

- [ ] Metrika / GA4 — goal `blog_read` или из conversion map
- [ ] Позиция primary query «mcp google sheets cursor» (ручная проверка / Wordstat)

## Notes

Indexer (safe mode): `--article-dir` в CLI нет; dry-run дал 11 outbound + 29 inbound только на junk-якорь «2026» → `--apply` по корпусу НЕ запускали. Вручную в B92 `article.html`: + outbound на B51/B58/B83/B59/B82 (итого 8 уникальных /blog/). Из `article.meta.json` secondary_queries убран «2026». `memory/blog/llms.txt` + `llms-full.txt` — 44 статьи, B92 включена.
