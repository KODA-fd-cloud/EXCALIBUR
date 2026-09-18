# Promotion checklist — B92 mcp-google-sheets-cursor-reestry

Дата публикации: 2026-09-18  
Live URL: https://koda-fd.ru/blog/mcp-google-sheets-cursor-reestry/ (после publish)

> ⚠️ 2026-09-18: publish **BLOCKER** (нет credentials / ALLOW flag). Live URL выше — плановый permalink, пост на WP ещё не создан.

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
Реестр снова уезжает в чат Cursor кусками, а статус правите руками в Sheets?

• Path B: mcp-gsheets + service account под финконтур
• Сценарий: найти по doc_key → обновить → перечитать
• Без сырых ПДн и без копипаста диапазонов

Читать: https://koda-fd.ru/blog/mcp-google-sheets-cursor-reestry/
```

## Перелинковка

- [ ] Добавить ссылку на новый пост с главной blog section (если Aurora не auto)
- [ ] Обновить 1–2 старых поста → link to new (если есть)

## Метрики (7 дней)

- [ ] Metrika / GA4 — goal `blog_read` или из conversion map
- [ ] Позиция primary query (ручная проверка / Wordstat)

## Notes

- Indexer: `excalibur_blog_interlinker.py --apply --blog-dir memory/blog/articles --site-base https://koda-fd.ru` (CLI без `--article-dir`).
- Opportunities: 380 (44 статьи); почти все — junk-анкор `2026` из secondary_queries.
- Applied raw: 30 → после QA оставлены **2** quality auto-links (`claude code`: B23→B04, B28→B04); 28 junk `2026` откачены.
- B92: **0** новых auto inbound/outbound; сохранены **4** writer outbound: `mcp-cursor-finansist-instrumenty`, `google-sheets-api-integraciya-finotdel`, `avtomatizaciya-finansov-no-code`, `obezlichivanie-dannyh-chatgpt-finansist`.
- Report: `interlink-suggestions.json` в article_dir.
- llms.txt / llms-full.txt: `memory/blog/` (site-base https://koda-fd.ru), 44 статьи, B92 в индексе.
- publish: pending (Indexer не публикует).
