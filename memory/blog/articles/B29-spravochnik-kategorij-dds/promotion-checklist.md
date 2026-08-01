# Promotion checklist — B29 spravochnik-kategorij-dds

Дата публикации: 2026-08-01  
Live URL: https://koda-fd.ru/blog/spravochnik-kategorij-dds/

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
Когда в одной таблице «Аренда», в другой «аренда офиса», а в отчёте собственнику — «Офисные расходы», план-факт ДДС разъезжается без ошибки в сумме.

• Лист «Справочник» на 15–25 статей ДДС
• Data validation вместо свободного ввода
• Один код категории на операции, план-факт и дашборд

Читать: https://koda-fd.ru/blog/spravochnik-kategorij-dds/
```

## Перелинковка

- [ ] Добавить ссылку на новый пост с главной blog section (если Aurora не auto)
- [ ] Обновить 1–2 старых поста → link to new (если есть)
- [x] Writer hub/spoke в B29: `/disnejlend-dlya-dannyh/`, `/ot-excel-k-fin-konturu-30-dney/`, `/bankovskaya-vypiska-staging-google-sheets/`
- [x] Interlinker corpus: +2 auto-links (B23→B04, B28→B04); для B29 auto=0 (ручные hub/spoke уже есть) — PASS

## Метрики (7 дней)

- [ ] Metrika / GA4 — goal `blog_read` или из conversion map
- [ ] Позиция primary query `категории ддс справочник` (ручная проверка / Wordstat)

## Notes

- topic_id: B29
- slug: spravochnik-kategorij-dds
- article_mode: B (how_to)
- author_id: olga-kondratskaya
- llms: `memory/blog/llms.txt`, `memory/blog/llms-full.txt`
- interlink report: `memory/blog/interlink-suggestions.json`
