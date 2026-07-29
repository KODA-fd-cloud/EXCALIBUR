# Promotion checklist — B13 vygruzka-1c-excel-odata

Дата публикации: 2026-07-22  
Live URL: https://koda-fd.ru/blog/vygruzka-1c-excel-odata/

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
Выгрузка из 1С в Excel через OData — не «Сохранить как» каждый понедельник, а повторный HTTP-запрос к живой базе с фильтром.

• Публикация standard.odata + read-only пользователь
• Power Query в Excel или кнопка «Обновить из 1С» в Google Sheets
• Чеклист: что не тащить в облако и когда звать 1С-ника

Читать: https://koda-fd.ru/blog/vygruzka-1c-excel-odata/
```

## Перелинковка

- [ ] Добавить ссылку на новый пост с главной blog section (если Aurora не auto)
- [ ] Обновить 1–2 старых поста → link to new (если есть)

## Метрики (7 дней)

- [ ] Metrika / GA4 — goal `blog_read` или из conversion map
- [ ] Позиция primary query (ручная проверка / Wordstat)

## Notes

- Indexer: interlinker `--apply` (CLI без `--article-dir`; прогон по `memory/blog/articles`); B13 уже имеет ручные internal links на `ot-excel-k-fin-konturu-30-dney` и `obezlichivanie-dannyh-chatgpt-finansist`.
- llms.txt / llms-full.txt обновлены в `memory/blog/` (site-base https://koda-fd.ru), B13 в индексе.
- publish: no — чеклист готов к ручному/позднему publish.
