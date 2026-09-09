# Promotion checklist — B92 mcp-google-sheets-cursor-reestry

Дата публикации: 2026-09-09 (черновик — WP publish blocked)  
Live URL: — (❌ PUBLISH BLOCKER: нет FTP/ALLOW/PUBLIC_SITE_URL; ожидаемый permalink после secrets: https://koda-fd.ru/blog/mcp-google-sheets-cursor-reestry/)

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
Реестр договоров снова копируете в чат Cursor кусками?

• Path A: remote Sheets MCP Google + OAuth
• Path B: service account + mcp-gsheets — blast radius на один файл
• Сценарий: найти по doc_key → update status → перечитать

Читать: https://koda-fd.ru/blog/mcp-google-sheets-cursor-reestry/
```

## Перелинковка

- [ ] Добавить ссылку на новый пост с главной blog section (если Aurora не auto)
- [x] Обновить 1–2 старых поста → link to new (B82, B21, B80 inbound ручные)

## Метрики (7 дней)

- [ ] Metrika / GA4 — goal `blog_read` или из conversion map
- [ ] Позиция primary query (ручная проверка / Wordstat)

## Notes

- Indexer 2026-09-09: auto `--apply` SKIPPED (junk якоря «2026»); manual 10 interlinks.
- Dead B02/B03 (404) не линковались.
- llms: `memory/blog/llms.txt`, `memory/blog/llms-full.txt`
- link-verify post-apply: pass 15/15, failed=0
