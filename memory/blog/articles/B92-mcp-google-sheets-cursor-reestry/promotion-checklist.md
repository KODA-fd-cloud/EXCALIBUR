# Promotion checklist — B92 mcp-google-sheets-cursor-reestry

Дата публикации: 2026-09-17  
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
Снова копируешь реестр в Cursor кусками и сверяешь ячейки вручную?

• Path B: mcp-gsheets + service account — production для финотдела
• Цикл find → update status → re-read по doc_key без копипаста
• Path C (sheetsmcp.googleapis.com) пока Developer Preview

Читать: https://koda-fd.ru/blog/mcp-google-sheets-cursor-reestry/
```

## Перелинковка

- [ ] Добавить ссылку на новый пост с главной blog section (если Aurora не auto)
- [ ] Обновить 1–2 старых поста → link to new (рекомендуется: B21 mcp-cursor-finansist-instrumenty, B82 google-sheets-api-integraciya-finotdel)

## Метрики (7 дней)

- [ ] Metrika / GA4 — goal `blog_read` или из conversion map
- [ ] Позиция primary query (ручная проверка / Wordstat): `mcp google sheets cursor`

## Notes

- Indexer: CLI без `--article-dir` → `interlinker.py --apply --blog-dir memory/blog/articles --site-base https://koda-fd.ru`.
- Auto-apply дал 28 ложных ссылок на якорь `2026` (keyword pollution в secondary_queries) → откат; в B92 secondary_queries `2026` заменён на `mcp-gsheets service account`.
- B92 outbound internal links: **4** (ручные writer): mcp-cursor-finansist-instrumenty, google-sheets-api-integraciya-finotdel, avtomatizaciya-finansov-no-code, obezlichivanie-dannyh-chatgpt-finansist.
- Дополнительно сохранены 2 валидных spoke-link: «Claude Code» → claude-code-finotdel в B23 и B28.
- llms.txt / llms-full.txt обновлены в `memory/blog/` (B92 в индексе).
- publish: pending (директор → excalibur-blog-publish).
