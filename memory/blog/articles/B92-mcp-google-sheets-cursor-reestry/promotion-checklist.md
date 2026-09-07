# Promotion checklist — B92 mcp-google-sheets-cursor-reestry

Дата публикации: 2026-09-07  
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
Реестр в чат — снова копипаст?

MCP Google Sheets в Cursor: mcp-gsheets + service account, share только рабочего файла, сценарий find → update → re-read по doc_key.

• Path B за 1–2 часа (Node 20+, mcp.json, зелёный MCP)
• Без сырых ПДн в облаке
• Квота SA: 60 req/min на user

Читать: https://koda-fd.ru/blog/mcp-google-sheets-cursor-reestry/
```

## Перелинковка

- [ ] Добавить ссылку на новый пост с главной blog section (если Aurora не auto)
- [ ] Обновить 1–2 старых поста → link to new (если есть)
  - кандидаты: B21 mcp-cursor-finansist-instrumenty, B82 google-sheets-api-integraciya-finotdel

## Метрики (7 дней)

- [ ] Metrika / GA4 — goal `blog_read` или из conversion map
- [ ] Позиция primary query (ручная проверка / Wordstat)

## Notes

- Indexer: dry-run interlinker → все 11 suggestions для B92 = junk anchor «2026»; **`--apply` не запускали**.
- Ручные contextual interlinks (+4): `mcp-1c-cursor-ostatki-oboroty`, `reestr-dogovorov-google-sheets`, `reestr-upd-google-sheets`, `platezhnyj-kalendar-google-sheets-n8n` (B24; B02 404 заменён). Уже были: B21, B82, B11. B03 не линковали (404).
- llms.txt / llms-full.txt: `memory/blog/` (`--site-base https://koda-fd.ru`).
- publish: next после Indexer.
