# Promotion checklist — B37 import-1c-unf-excel-regulyarno

Дата публикации: 2026-08-03  
Live URL: https://koda-fd.ru/blog/import-1c-unf-excel-regulyarno/

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
Каждый день одно и то же: открыть отчёт в УНФ, "Сохранить как", вставить кусок в книгу. Регулярный импорт убирает эту рутину.

• Power Query refresh в Desktop или скрипт в папку / HTTP-сервис
• Узкий канал + read-only пользователь до любого расписания
• Excel Online не обновит файл, пока книга закрыта

Читать: https://koda-fd.ru/blog/import-1c-unf-excel-regulyarno/
```

## Перелинковка

- [ ] Добавить ссылку на новый пост с главной blog section (если Aurora не auto)
- [ ] Обновить 1–2 старых поста → link to new (если есть)

## Метрики (7 дней)

- [ ] Metrika / GA4 — goal `blog_read` или из conversion map
- [ ] Позиция primary query (ручная проверка / Wordstat)

## Notes

- Indexer: interlinker `--apply --blog-dir memory/blog/articles --site-base https://koda-fd.ru` (CLI без `--article-dir`); corpus auto-links=2 (B23→B04, B28→B04 Claude Code); в B37 новых auto-links=0 — уже есть ручные internal на `vygruzka-1c-excel-odata`, `obezlichivanie-dannyh-chatgpt-finansist`, `power-query-finansist-obnovlenie`, `avtomatizaciya-finansov-no-code`.
- llms.txt / llms-full.txt: 26 статей, B37 в индексе, site-base https://koda-fd.ru, out-dir `memory/blog/`.
- publish: pending.
