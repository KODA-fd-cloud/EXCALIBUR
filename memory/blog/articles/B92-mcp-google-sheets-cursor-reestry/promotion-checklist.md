# Promotion checklist — B92 mcp-google-sheets-cursor-reestry

Дата публикации: 2026-09-06  
Live URL: ❌ PUBLISH BLOCKER — нет credentials (`site.env.local` / `EXCALIBUR_BLOG_ALLOW_PUBLISH` / `PUBLIC_SITE_URL` / `FTP_*`); заполнить после успешного publish

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
Реестр снова уезжает в чат Cursor кусками? MCP Google Sheets убирает копипаст.

• Path B: mcp-gsheets + service account — production-default
• Сценарий: найти по doc_key → обновить status → перечитать
• Share только нужного файла; без сырых ПДн

Читать: https://koda-fd.ru/blog/mcp-google-sheets-cursor-reestry/
```

## Перелинковка

- [ ] Добавить ссылку на новый пост с главной blog section (если Aurora не auto)
- [x] Обновить 1–2 старых поста → link to new (B21, B82)
- [x] Outbound из B92 → B51/B58/B83/B59 (+ якорь B82)

## Метрики (7 дней)

- [ ] Metrika / GA4 — goal `blog_read` или из conversion map
- [ ] Позиция primary query (ручная проверка / Wordstat)

## Notes

- Indexer 2026-09-06: dry-run → junk `2026` в secondary_queries снят (13 meta); auto `--apply` для B92 = 0 (не blind-apply Claude Code вне scope); +11 ручных якорей; B03 не линкуем.
- llms.txt / llms-full.txt: `memory/blog/` (site-base https://koda-fd.ru), B92 в индексе.
- ready_for: publish
