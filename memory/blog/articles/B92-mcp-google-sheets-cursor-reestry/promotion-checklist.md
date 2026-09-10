# Promotion checklist — B92 mcp-google-sheets-cursor-reestry

Дата публикации: 2026-09-10  
Live URL: _(не опубликовано — ❌ PUBLISH BLOCKER: нет site.env.local / ALLOW_PUBLISH / FTP_* / PUBLIC_SITE_URL)_  
Planned URL (после publish): https://koda-fd.ru/blog/mcp-google-sheets-cursor-reestry/

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
Реестр снова уезжает в чат Cursor кусками? MCP Google Sheets — розетка: агент сам читает и обновляет строки по doc_key.

• Path B: mcp-gsheets + service account, share только рабочего файла
• mcp.json → MCP Logs → сценарий find → update → re-read
• Без сырых ПДн: staging-лист и ProtectedRange

Читать: https://koda-fd.ru/blog/mcp-google-sheets-cursor-reestry/
```

## Перелинковка

- [ ] Добавить ссылку на новый пост с главной blog section (если Aurora не auto)
- [ ] Обновить 1–2 старых поста → link to new (если есть)
  - Кандидаты: `mcp-cursor-finansist-instrumenty`, `google-sheets-api-integraciya-finotdel`, `podklyuchenie-mcp-cursor` (ручные inbound после publish; auto «2026» отклонены)

## Метрики (7 дней)

- [ ] Metrika / GA4 — goal `blog_read` или из conversion map
- [ ] Позиция primary query (ручная проверка / Wordstat)

## Notes

- Indexer: interlinker CLI без `--article-dir` → `--apply --blog-dir memory/blog/articles --site-base https://koda-fd.ru`.
- Auto-apply дал false-positive анкоры `2026` (из secondary_queries соседних статей) — все такие правки в `article.html` откачены; body B92 не переписывался.
- Из `article.meta.json` B92 убран secondary `2026` (не анкор).
- Ручные internal links B92 сохранены: `mcp-cursor-finansist-instrumenty`, `google-sheets-api-integraciya-finotdel`, `avtomatizaciya-finansov-no-code`, `obezlichivanie-dannyh-chatgpt-finansist`.
- llms.txt / llms-full.txt обновлены в `memory/blog/` (site-base https://koda-fd.ru), B92 в индексе.
- publish: pending (шаг ⑥).
