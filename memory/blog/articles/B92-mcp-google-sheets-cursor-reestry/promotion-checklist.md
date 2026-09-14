# Promotion checklist — B92 mcp-google-sheets-cursor-reestry

Дата публикации: 2026-09-14  
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
Реестр снова уезжает в чат Cursor кусками, а статус правите руками в Google Таблицах?

• MCP Google Sheets — агент сам читает и обновляет строки по doc_key
• Path B: mcp-gsheets + service account, без копипаста диапазонов
• За 1–2 часа: share файла → mcp.json → MCP Logs → find-update-re-read

Читать: https://koda-fd.ru/blog/mcp-google-sheets-cursor-reestry/
```

## Перелинковка

- [ ] Добавить ссылку на новый пост с главной blog section (если Aurora не auto)
- [ ] Обновить 1–2 старых поста → link to new (если есть)

## Метрики (7 дней)

- [ ] Metrika / GA4 — goal `blog_read` или из conversion map
- [ ] Позиция primary query (ручная проверка / Wordstat)

## Notes

- Indexer: CLI без `--article-dir`; прогон `excalibur_blog_interlinker.py --blog-dir memory/blog/articles --site-base https://koda-fd.ru` (отчёт `memory/blog/interlink-suggestions.json`). Полный `--apply` по корпусу не делали: 40 B92-матчей только по keyword «2026» из secondary_queries — шум. Scoped apply non-2026 для B92 → 0 вставок. `article.html` без изменений: 4 writer interlinks сохранены (`mcp-cursor-finansist-instrumenty`, `google-sheets-api-integraciya-finotdel`, `avtomatizaciya-finansov-no-code`, `obezlichivanie-dannyh-chatgpt-finansist`).
- llms.txt / llms-full.txt обновлены в `memory/blog/` (site-base https://koda-fd.ru), 44 статьи, B92 в индексе.
- publish: pending после indexer.
