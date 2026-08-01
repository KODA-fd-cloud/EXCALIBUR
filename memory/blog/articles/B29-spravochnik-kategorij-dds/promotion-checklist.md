# Promotion checklist — B29 spravochnik-kategorij-dds

Дата публикации: 2026-08-01  
Live URL: — (publish blocker; ожидаемый permalink после publish: https://koda-fd.ru/blog/spravochnik-kategorij-dds/)

Excalibur создаёт этот файл после `✅ ARTICLE OK` (до или после WP publish).
Publish 2026-08-01: ❌ BLOCKER — нет EXCALIBUR_BLOG_ALLOW_PUBLISH / credentials.

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
Когда в одной таблице «Аренда», в другой «аренда офиса» — план-факт ДДС разъезжается без ошибки в сумме.

• Лист «Справочник» на 15–25 статей + data validation «отклонять ввод»
• Правила для «Прочее» (≤5% оборота) и переводов между счетами
• Один DDS_Categories на операции, план-факт и дашборд

Читать: https://koda-fd.ru/blog/spravochnik-kategorij-dds/
```

## Перелинковка

- [ ] Добавить ссылку на новый пост с главной blog section (если Aurora не auto)
- [ ] Обновить 1–2 старых поста → link to new (если есть)

## Метрики (7 дней)

- [ ] Metrika / GA4 — goal `blog_read` или из conversion map
- [ ] Позиция primary query (ручная проверка / Wordstat)

## Notes

- Indexer: interlinker `--apply --blog-dir memory/blog/articles --site-base https://koda-fd.ru` (CLI без `--article-dir`).
- B29: 0 новых auto-links — уже есть ручные hub/spoke: `disnejlend-dlya-dannyh`, `bankovskaya-vypiska-staging-google-sheets`, `ot-excel-k-fin-konturu-30-dney` → PASS.
- Корпус: применено 2 auto-links (B23→B04, B28→B04 «Claude Code»).
- llms.txt / llms-full.txt обновлены в `memory/blog/` (site-base https://koda-fd.ru), B29 в индексе.
- publish: pending после Indexer.
