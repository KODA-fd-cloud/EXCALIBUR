# Promotion checklist — B92 mcp-google-sheets-cursor-reestry

Дата публикации: 2026-08-30  
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
Реестр договоров или УПД снова уезжает в чат Cursor кусками? MCP Google Sheets сам читает и обновляет строку по doc_key.

• Path B: mcp-gsheets + service account (production)
• DoD: find → update status/comment → re-read
• Без сырых ПДн и без Auto-run write

Читать: https://koda-fd.ru/blog/mcp-google-sheets-cursor-reestry/
```

## Перелинковка

- [x] Outbound spokes B92 → B51/B58/B83 (договоры, УПД, SaaS)
- [x] Inbound хабы B21 + B82 → B92
- [ ] Добавить ссылку на новый пост с главной blog section (если Aurora не auto)

## Метрики (7 дней)

- [ ] Metrika / GA4 — goal `blog_read` или из conversion map
- [ ] Позиция primary query (ручная проверка / Wordstat)

## Notes

- Indexer: **без** слепого `interlinker --apply` (junk-якоря «2026» из secondary_queries). Ручные contextual links: +3 outbound (B51/B58/B83) +2 inbound (B21, B82) = **5**.
- Уже были outbound на B21, B82, no-code, обезличивание — сохранены.
- llms.txt / llms-full.txt: `memory/blog/` с `--site-base https://koda-fd.ru`, 44 статьи, B92 в индексе.
- publish: pending (секреты FTP/ALLOW могут отсутствовать в cron).
