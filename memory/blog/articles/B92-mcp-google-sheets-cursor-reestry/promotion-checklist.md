# Promotion checklist — B92 mcp-google-sheets-cursor-reestry

Дата публикации: 2026-08-24  
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
Реестр договоров снова уезжает в чат Cursor кусками? MCP Google Sheets даёт агенту tools: найти строку по doc_key, обновить статус, перечитать — без копипаста.

• Path B: mcp-gsheets + service account (финконтур)
• Share только рабочего файла, ключ вне git
• Verify: MCP Logs → find → update → re-read

Читать: https://koda-fd.ru/blog/mcp-google-sheets-cursor-reestry/
```

## Перелинковка

- [ ] Добавить ссылку на новый пост с главной blog section (если Aurora не auto)
- [ ] Обновить 1–2 старых поста → link to new (если есть)

## Метрики (7 дней)

- [ ] Metrika / GA4 — goal `blog_read` или из conversion map
- [ ] Позиция primary query (ручная проверка / Wordstat)

## Notes

- Indexer CLI: `python3 scripts/excalibur_blog_interlinker.py --apply --blog-dir memory/blog/articles --site-base https://koda-fd.ru` (флаг `--article-dir` в CLI нет).
- B92: 0 новых auto-links — уже есть ручные internal на `mcp-cursor-finansist-instrumenty`, `google-sheets-api-integraciya-finotdel`, `avtomatizaciya-finansov-no-code`, `obezlichivanie-dannyh-chatgpt-finansist`. Auto-match по слову `2026` откатан (spam).
- Corpus: оставлены 2 валидных auto-link (`Claude Code` → `/blog/claude-code-finotdel/` в B23, B28); 28 year-spam `2026` → B83 откатены.
- llms.txt / llms-full.txt: `memory/blog/` (site-base https://koda-fd.ru, КОДА branding), B92 в индексе.
- publish: pending после Indexer.
