# Promotion checklist — B92 mcp-google-sheets-cursor-reestry

Дата публикации: _(не опубликовано — ❌ PUBLISH BLOCKER 2026-09-17)_  
Live URL: _(ожидаемый)_ https://koda-fd.ru/blog/mcp-google-sheets-cursor-reestry/  
Blockers (env names only): EXCALIBUR_BLOG_ALLOW_PUBLISH, PUBLIC_SITE_URL, FTP_HOST/FTP_USER/FTP_PASS/FTP_ROOT (или SSH_HOST), memory/site.env.local

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
Реестр снова уезжает в чат Cursor кусками? MCP Google Sheets — агент сам читает и обновляет строки по doc_key без копипаста.

• Path B: mcp-gsheets + service account за 1–2 часа
• Сценарий find → update → re-read через MCP Logs
• Без сырых ПДн в облако; Path A/C — когда не брать в production

Читать: https://koda-fd.ru/blog/mcp-google-sheets-cursor-reestry/
```

## Перелинковка

- [ ] Добавить ссылку на новый пост с главной blog section (если Aurora не auto)
- [ ] После publish — inbound из B21 (MCP Cursor) / B82 (Sheets API) на упоминаниях Sheets+MCP (не через якорь «2026»)

## Метрики (7 дней)

- [ ] Metrika / GA4 — goal `blog_read` или из conversion map
- [ ] Позиция primary query «mcp google sheets cursor» (ручная проверка / Wordstat)

## Notes

- Indexer: CLI без `--article-dir`; `--apply` по `memory/blog/articles`, site-base `https://koda-fd.ru`.
- B92 `article.html`: **0 новых auto-links** — сохранены 4 ручных outbound: `mcp-cursor-finansist-instrumenty`, `google-sheets-api-integraciya-finotdel`, `avtomatizaciya-finansov-no-code`, `obezlichivanie-dannyh-chatgpt-finansist`.
- Raw opportunities: 380; skipped keyword `2026` (378) — pollution из `secondary_queries`; B92 inbound meaningful (anchor_variants/primary): **0**.
- Корпус: +2 валидных auto-link (`Claude Code` → `claude-code-finotdel` в B23 и B28).
- Из meta B92 убран secondary `2026`, чтобы не плодить спам-inbound.
- `memory/blog/llms.txt` + `llms-full.txt`: 44 статьи, B92 в индексе.
- Report: `interlink-suggestions.json` в article_dir.
