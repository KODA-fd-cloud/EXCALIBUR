# Promotion checklist — B92 mcp-google-sheets-cursor-reestry

Дата публикации: 2026-09-12  
Live URL: https://koda-fd.ru/blog/mcp-google-sheets-cursor-reestry/ (после publish)

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
Реестр снова копипастом в чат Cursor?

• MCP Google Sheets: Agent сам читает и обновляет строку по doc_key
• Path B (mcp-gsheets + SA) для финконтура; OAuth — только пилот
• DoD: найти → обновить статус → перечитать результат

Читать: https://koda-fd.ru/blog/mcp-google-sheets-cursor-reestry/
```

## Перелинковка

- [ ] Добавить ссылку на новый пост с главной blog section (если Aurora не auto)
- [x] Обновить 1–2 старых поста → link to new (B21, B82, B51 — inbound curated)
- [x] Outbound B92 → B51 (reestr-dogovorov) + уже были B21/B82/no-code/obezlichivanie

## Метрики (7 дней)

- [ ] Metrika / GA4 — goal `blog_read` или из conversion map
- [ ] Позиция primary query (ручная проверка / Wordstat)

## Notes

- Indexer: `excalibur_blog_interlinker.py --apply` **не** применяли вслепую — auto-suggestions = year-anchor `2026` (false positive из secondary других статей). CLI: `--blog-dir`, не `--article-dir`.
- Curated interlinks: **4** (inbound×3 B21/B82/B51 → B92; outbound×1 B92 → B51). B92 уже имел 4 outbound (B21, B82, no-code, obezlichivanie).
- Meta: secondary `2026` заменён на `правка реестра google sheets cursor`.
- llms.txt / llms-full.txt: `memory/blog/` — 44 статьи, B92 в индексе, site-base https://koda-fd.ru.
