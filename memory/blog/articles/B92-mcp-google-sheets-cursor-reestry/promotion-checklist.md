# Promotion checklist — B92 mcp-google-sheets-cursor-reestry

Дата публикации: 2026-08-27  
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
Реестр снова уезжает в чат Cursor кусками? MCP Google Sheets правит строку по doc_key без копипаста.

• Path B: mcp-gsheets + service account за 1–2 часа
• Сценарий find → update → re-read через MCP Logs
• Path A OAuth: Error 400 на cursor:// и обход Local/Agents

Читать: https://koda-fd.ru/blog/mcp-google-sheets-cursor-reestry/
```

## Перелинковка

- [ ] Добавить ссылку на новый пост с главной blog section (если Aurora не auto)
- [ ] Обновить 1–2 старых поста → link to new (если есть)
- [x] Indexer: year-spam срезан; в B92 4 контекстных internal links

## Метрики (7 дней)

- [ ] Metrika / GA4 — goal `blog_read` или из conversion map
- [ ] Позиция primary query `mcp google sheets cursor` (ручная проверка / Wordstat)

## Notes

- topic_id: B92
- primary_query: mcp google sheets cursor
- author_id: olga-kondratskaya
- article_mode: B
- interlink apply: 30 (скрипт); year-spam stripped: 28; B92 retained: 4 contextual
- llms: memory/blog/llms.txt, memory/blog/llms-full.txt
