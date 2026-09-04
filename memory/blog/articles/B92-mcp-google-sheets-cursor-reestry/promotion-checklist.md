# Promotion checklist — B92 mcp-google-sheets-cursor-reestry

Дата публикации: 2026-09-04 (pending WP publish)  
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
Реестр договоров снова уезжает в чат Cursor кусками?

• Path B: mcp-gsheets + service account, share только реестра
• Сценарий: найти по doc_key → update status → перечитать diff
• Path A/C (OAuth) — только пилот с disclaimer

Читать: https://koda-fd.ru/blog/mcp-google-sheets-cursor-reestry/
```

## Перелинковка

- [ ] Добавить ссылку на новый пост с главной blog section (если Aurora не auto)
- [x] Обновить 1–2 старых поста → link to new (B82, B51, B21 → B92)
- [x] Outbound в B92: договоры, УПД, SaaS, заявки/Forms, скрипт B82 (+ уже были MCP/B82/обезличивание/no-code)

## Метрики (7 дней)

- [ ] Metrika / GA4 — goal `blog_read` или из conversion map
- [ ] Позиция primary query (ручная проверка / Wordstat)

## Notes

- Indexer: dry-run `excalibur_blog_interlinker.py --blog-dir memory/blog/articles --site-base https://koda-fd.ru` — auto-suggestions для B92 только junk-якорь «2026» → **blind `--apply` НЕ запускали**.
- Ручные interlinks: +9 outbound anchors в B92, +3 inbound (B82/B51/B21). Итого **+12** новых ссылок.
- Published slugs only (из `shared/published-articles.md`); мёртвых 404 нет.
- llms.txt / llms-full.txt: `memory/blog/llms.txt`, `memory/blog/llms-full.txt` (site-base https://koda-fd.ru), B92 в индексе.
- next: excalibur-blog-publish
