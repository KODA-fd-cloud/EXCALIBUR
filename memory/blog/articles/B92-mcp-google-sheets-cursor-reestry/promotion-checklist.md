# Promotion checklist — B92 mcp-google-sheets-cursor-reestry

Дата публикации: 2026-09-07 (pending WP publish)  
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
Реестр снова копипастом в чат Cursor? MCP Google Sheets даёт агенту tools к таблице по doc_key.

• Path B: mcp-gsheets + service account = production
• Share только реестра на SA, ключ вне git
• Сценарий: найти → обновить status → перечитать diff

Читать: https://koda-fd.ru/blog/mcp-google-sheets-cursor-reestry/
```

## Перелинковка

- [ ] Добавить ссылку на новый пост с главной blog section (если Aurora не auto)
- [x] Обновить 1–2 старых поста → link to new (B21×2, B82, B51; outbound B92→B51/B58/B83/B59 + B82)

## Метрики (7 дней)

- [ ] Metrika / GA4 — goal `blog_read` или из conversion map
- [ ] Позиция primary query (ручная проверка / Wordstat)

## Notes

- Indexer: **не** blind `--apply` — dry-run дал только junk-якоря «2026» (из secondary_queries). Ручные contextual links; B03 404 не линковать. CLI без `--article-dir`.
- secondary_queries: убран токен `2026` из `article.meta.json`.
- llms.txt / llms-full.txt: `memory/blog/` (`--site-base https://koda-fd.ru`), B92 в индексе.
- publish: pending (credentials / ALLOW_PUBLISH).
