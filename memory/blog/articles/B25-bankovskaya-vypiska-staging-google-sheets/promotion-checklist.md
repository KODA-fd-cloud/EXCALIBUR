# Promotion checklist — B25 bankovskaya-vypiska-staging-google-sheets

Дата публикации: 2026-07-31  
Live URL: — (ожидаемый: https://koda-fd.ru/blog/bankovskaya-vypiska-staging-google-sheets/)  
Publish status: ❌ PUBLISH BLOCKER — нет FTP_*/SSH_* и EXCALIBUR_BLOG_ALLOW_PUBLISH=yes

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
Скачали выписку — и снова копипаст в «мастер» ДДС? Нужен staging-слой.

• CSV/Excel → raw_import → staging с каноном колонок
• row_hash + сверка Σ приход/расход с банком
• Без PDF-SaaS и без подмены 1С:ДиректБанк

Читать: https://koda-fd.ru/blog/bankovskaya-vypiska-staging-google-sheets/
```

## Перелинковка

- [ ] Добавить ссылку на новый пост с главной blog section (если Aurora не auto)
- [ ] Обновить 1–2 старых поста → link to new (если есть)

## Метрики (7 дней)

- [ ] Metrika / GA4 — goal `blog_read` или из conversion map
- [ ] Позиция primary query (ручная проверка / Wordstat)

## Notes

- Indexer: interlinker `--apply --blog-dir memory/blog/articles --site-base https://koda-fd.ru` (CLI без `--article-dir`); применено **1** auto-link (B23 → B04, keyword «claude code»). Для B25 новых auto-links **0** — уже есть ручные internal links на `ot-excel-k-fin-konturu-30-dney`, `google-apps-script-finansist-obnovit-dannye`, `python-finansist-sverka-csv`.
- llms.txt / llms-full.txt обновлены в `memory/blog/` (site-base https://koda-fd.ru, 21 статья), B25 в индексе.
- publish: pending.
