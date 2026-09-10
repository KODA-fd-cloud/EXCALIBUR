# Promotion checklist — B92 mcp-google-sheets-cursor-reestry

Дата публикации: 2026-09-10 (pending — ❌ PUBLISH BLOCKER: нет credentials / ALLOW_PUBLISH)  
Live URL: — (ожидаемый: https://koda-fd.ru/blog/mcp-google-sheets-cursor-reestry/)

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
Реестр договоров или УПД снова уезжает в чат Cursor кусками — а после правки вы вручную сверяете ячейки?

• MCP Google Sheets + mcp-gsheets / service account за 1–2 часа
• Сценарий: найти строку по doc_key → обновить статус → перечитать
• Path B для финконтура: share только рабочего файла, без копипаста ПДн

Читать: https://koda-fd.ru/blog/mcp-google-sheets-cursor-reestry/
```

## Перелинковка

- [ ] Добавить ссылку на новый пост с главной blog section (если Aurora не auto)
- [ ] Обновить 1–2 старых поста → link to new (если есть)

## Метрики (7 дней)

- [ ] Metrika / GA4 — goal `blog_read` или из conversion map
- [ ] Позиция primary query «mcp google sheets cursor» (ручная проверка / Wordstat)

## Notes

Indexer: interlinker `--apply` по корпусу (44 статьи, site-base https://koda-fd.ru). B92 `article.html` без изменений — 4 internal links от writer сохранены. 29 входящих возможностей (anchor «2026» из secondary_queries) не применены / откатаны: ложный якорь-год. Hub: +2 исходящих Claude Code в B23/B28. `memory/blog/llms.txt` и `llms-full.txt` — 44 статьи, B92 добавлена.
