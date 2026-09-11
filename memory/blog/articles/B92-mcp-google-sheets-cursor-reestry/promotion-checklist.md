# Promotion checklist — B92 mcp-google-sheets-cursor-reestry

Дата публикации: 2026-09-11 (planned; **не опубликовано**)  
Live URL: ❌ не опубликован — PUBLISH BLOCKER (нет site.env.local / ALLOW / FTP_*)  
Плановый permalink (после успешного publish): https://koda-fd.ru/blog/mcp-google-sheets-cursor-reestry/

Excalibur создаёт этот файл после `✅ ARTICLE OK` (до или после WP publish).

## Сразу после publish

- [ ] Открыть live URL — title, excerpt, featured image, FAQ — **blocked: нет live URL**
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
Реестр снова уезжает в чат Cursor кусками? MCP Google Sheets читает и обновляет строки по doc_key без копипаста.

• Path B: mcp-gsheets + service account на один файл
• Сценарий find → update → re-read через Agent
• Пилот за 1–2 часа, ключ в env вне git

Читать: https://koda-fd.ru/blog/mcp-google-sheets-cursor-reestry/
```

## Перелинковка

- [ ] Добавить ссылку на новый пост с главной blog section (если Aurora не auto)
- [ ] Обновить 1–2 старых поста → link to new (если есть)

## Метрики (7 дней)

- [ ] Metrika / GA4 — goal `blog_read` или из conversion map
- [ ] Позиция primary query (ручная проверка / Wordstat)

## Notes

- Indexer: interlinker `--apply --blog-dir memory/blog/articles --site-base https://koda-fd.ru` (CLI без `--article-dir`).
- Apply: 30 auto-links; из них 28 ложных year-anchors `<a>2026</a>` откатили; в B92 осталось 4 смысловых internal links (writer): `mcp-cursor-finansist-instrumenty`, `google-sheets-api-integraciya-finotdel`, `avtomatizaciya-finansov-no-code`, `obezlichivanie-dannyh-chatgpt-finansist`.
- Убран secondary_query `2026` из `article.meta.json` (причина ложных якорей).
- llms.txt / llms-full.txt обновлены в `memory/blog/` (site-base https://koda-fd.ru), B92 в индексе.
- publish: ❌ PUBLISH BLOCKER 2026-09-11 — нет credentials; ledger не обновлён; dry-run OK; link-verify pass.
