# Promotion checklist — B92 mcp-google-sheets-cursor-reestry

Дата публикации: 2026-09-05  
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
Реестр снова в чат кусками? MCP Google Sheets в Cursor читает и обновляет строки по doc_key без копипаста.

• Path B: mcp-gsheets + service account, share одного файла
• Сценарий find → update → re-read за 1–2 часа
• Path A OAuth — только пилот; production держите на SA

Читать: https://koda-fd.ru/blog/mcp-google-sheets-cursor-reestry/
```

## Перелинковка

- [ ] Добавить ссылку на новый пост с главной blog section (если Aurora не auto)
- [x] Обновить 1–2 старых поста → link to new (B21, B82, B83)

## Метрики (7 дней)

- [ ] Metrika / GA4 — goal `blog_read` или из conversion map
- [ ] Позиция primary query «mcp google sheets cursor» (ручная проверка / Wordstat)

## Notes

- Indexer: dry-run interlinker → все auto-suggestions B92 = junk anchor `2026` (из secondary_queries); `--apply` не запускали.
- Manual outbound: 12 unique `/blog/` slugs (15 href; B51/B58/B83 ×2). Published only; B03 не линковали.
- Inbound: B21, B82, B83 → `mcp-google-sheets-cursor-reestry`.
- Meta: secondary_queries `2026` заменён на `mcp-gsheets service account`.
- llms.txt / llms-full.txt: `--out-dir memory/blog`, B92 в индексе (44 articles).
