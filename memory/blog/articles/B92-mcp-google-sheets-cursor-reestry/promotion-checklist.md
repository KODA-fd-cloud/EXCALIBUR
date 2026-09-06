# Promotion checklist — B92 mcp-google-sheets-cursor-reestry

Дата публикации: 2026-09-06 (planned; **не опубликовано**)  
Live URL: _(нет — ❌ PUBLISH BLOCKER; expected after publish: https://koda-fd.ru/blog/mcp-google-sheets-cursor-reestry/)_

Excalibur создаёт этот файл после `✅ ARTICLE OK` (до или после WP publish).

## Сразу после publish

- [ ] Открыть live URL — title, excerpt, featured image, FAQ
- [ ] View source — JSON-LD BlogPosting + FAQPage (theme или plugin)
- [ ] Проверить internal links из статьи (200)
- [ ] Яндекс.Вебмастер / GSC — URL отправлен (если настроено)

## Publish status (2026-09-06)

- ❌ PUBLISH BLOCKER: нет `memory/site.env.local`, `EXCALIBUR_BLOG_ALLOW_PUBLISH!=yes`, FTP/PUBLIC_SITE_URL недоступны.
- Preflight OK: link-verify pass, dry-run pass. Real WP publish не выполнялся.

## Соцсети / каналы (из conversion-tracking-map)

| Канал | Действие | Статус |
|-------|----------|--------|
| Telegram | Пост: hook + ссылка + 1 факт из статьи | ☐ |
| VK / Max | Адаптировать под ЦА | ☐ |
| Email / рассылка | Если есть в conversion map | ☐ |

## Snippet для Telegram (черновик)

```
Реестр снова копипастом в чат Cursor?

• MCP Google Sheets: Path B mcp-gsheets + service account
• Сценарий find → update → re-read по doc_key
• Без сырых ПДн и без «прав на весь Drive»

Читать: https://koda-fd.ru/blog/mcp-google-sheets-cursor-reestry/
```

## Перелинковка

- [ ] Добавить ссылку на новый пост с главной blog section (если Aurora не auto)
- [ ] Обновить 1–2 старых поста → link to new (если есть)
  - Кандидаты: B21 mcp-cursor-finansist-instrumenty, B82 google-sheets-api-integraciya-finotdel

## Метрики (7 дней)

- [ ] Metrika / GA4 — goal `blog_read` или из conversion map
- [ ] Позиция primary query (ручная проверка / Wordstat)

## Notes

- Indexer 2026-09-06: dry-run interlinker = только якоря «2026» → `--apply` пропущен; 5 ручных interlink (B51/B58/B83/B82/B80). Pre-existing: B21, B82, no-code, B11.
- Primary query: mcp google sheets cursor
