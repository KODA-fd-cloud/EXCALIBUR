# Promotion checklist — B92 mcp-google-sheets-cursor-reestry

Дата публикации: YYYY-MM-DD  
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
Реестр договоров снова уезжает в чат Cursor кусками? MCP Google Sheets — розетка: агент сам читает и обновляет строки по doc_key.

• Path B: mcp-gsheets + service account, share только реестра
• mcp.json → MCP Logs → find / update / re-read
• 1–2 часа до первого рабочего сценария без копипаста

Читать: https://koda-fd.ru/blog/mcp-google-sheets-cursor-reestry/
```

## Перелинковка

- [ ] Добавить ссылку на новый пост с главной blog section (если Aurora не auto)
- [x] Обновить 1–2 старых поста → link to new (если есть)
  - inbound: B03, B21, B51, B82 → B92
  - outbound: B92 → B21, B82, no-code, обезличивание, реестры договоров/УПД/SaaS/заявок

## Метрики (7 дней)

- [ ] Metrika / GA4 — goal `blog_read` или из conversion map
- [ ] Позиция primary query (ручная проверка / Wordstat)

## Notes

- Indexer: interlinker CLI без `--article-dir` → `--blog-dir memory/blog/articles --apply`.
- Первый прогон дал ложные анкоры на «2026» (secondary_queries); год убран из meta 13 статей, year-links откачены.
- Повторный `--apply`: 0 auto-матчей по фразам; inbound/outbound добавлены вручную (см. выше).
- Побочный валидный auto-link: «Claude Code» → B04 в B23 и B28.
- llms.txt / llms-full.txt: `--out-dir memory/blog --site-base https://koda-fd.ru`; запись B92 есть.
- publish: pending (secrets unset на момент indexer).
