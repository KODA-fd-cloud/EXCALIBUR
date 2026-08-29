# Promotion checklist — B92 mcp-google-sheets-cursor-reestry

Дата публикации: 2026-08-29  
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
Реестр снова уезжает в чат Cursor кусками? MCP Google Sheets — агент сам правит строку по doc_key.

• Path A: Marketplace + OAuth (пилот)
• Path B: mcp-gsheets + service account (финконтур)
• Сценарий: найти → обновить статус → перечитать

Читать: https://koda-fd.ru/blog/mcp-google-sheets-cursor-reestry/
```

## Перелинковка

- [ ] Добавить ссылку на новый пост с главной blog section (если Aurora не auto)
- [x] Обновить 1–2 старых поста → link to new (B21 Sheets-сервер; B82 FAQ → MCP Sheets)

## Метрики (7 дней)

- [ ] Metrika / GA4 — goal `blog_read` или из conversion map
- [ ] Позиция primary query (ручная проверка / Wordstat)

## Notes

- Indexer: `excalibur_blog_interlinker.py --apply --blog-dir memory/blog/articles --site-base https://koda-fd.ru` (CLI без `--article-dir`). Opportunities 380; raw apply 30 — из них 28 spam-ссылок на год «2026» (secondary_queries B43/др.) откатил; оставлены 2 валидных (Claude Code → B04 в B23/B28).
- B92 outbound: 4 ручных (B21, B82, LEGACY no-code, B11). Inbound hub: +2 (B21, B82). Из meta B92 убран secondary «2026».
- Report: `memory/blog/articles/B92-mcp-google-sheets-cursor-reestry/interlink-suggestions.json`
- llms.txt / llms-full.txt: `memory/blog/` (44 статьи, site-base https://koda-fd.ru), B92 в индексе.
- publish: pending (secrets may be missing).
