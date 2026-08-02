# Promotion checklist — B36 dashbord-dds-looker-studio

Дата публикации: 2026-08-02  
Live URL: https://koda-fd.ru/blog/dashbord-dds-looker-studio/

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
Собственник просит экран ДДС, а у вас свод в Sheets и скрины в чат? За час собирается дашборд в Looker Studio из того же листа операций.

• Long-лист Операции_DDS + коннектор Sheets
• Scorecards приток / отток / чистый поток, freshness от 15 минут
• Проверка сходимости без программиста

Читать: https://koda-fd.ru/blog/dashbord-dds-looker-studio/
```

## Перелинковка

- [ ] Добавить ссылку на новый пост с главной blog section (если Aurora не auto)
- [ ] Обновить 1–2 старых поста → link to new (если есть)

## Метрики (7 дней)

- [ ] Metrika / GA4 — goal `blog_read` или из conversion map
- [ ] Позиция primary query (ручная проверка / Wordstat)

## Notes

- Indexer: interlinker `--apply --blog-dir memory/blog/articles --site-base https://koda-fd.ru` (CLI без `--article-dir`); opportunities=2 применены в B23/B28 → B04; для B36 новых auto-links=0 — writer уже вставил ручные hub/spoke (`disnejlend-dlya-dannyh`, `spravochnik-kategorij-dds`, `obezlichivanie-dannyh-chatgpt-finansist`, `bankovskaya-vypiska-staging-google-sheets`, `google-apps-script-finansist-obnovit-dannye`, `avtomatizaciya-finansov-no-code`) → PASS.
- llms.txt / llms-full.txt обновлены в `memory/blog/` (site-base https://koda-fd.ru), B36 в индексе.
- publish: pending после Indexer.
