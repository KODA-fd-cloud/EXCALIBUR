# Promotion checklist — B25 bankovskaya-vypiska-staging-google-sheets

Дата публикации: 2026-07-31  
Live URL: https://koda-fd.ru/blog/bankovskaya-vypiska-staging-google-sheets/

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
CSV из банка в Google Sheets без копипаста в отчёт: сырой слой, staging и row_hash.

• Колонки date / amount / counterparty / purpose / account_id / row_hash
• Импорт: разделитель, 1251, «не преобразовывать текст»
• Дедуп и сверка оборотов до ДДС

Читать: https://koda-fd.ru/blog/bankovskaya-vypiska-staging-google-sheets/
```

## Перелинковка

- [ ] Добавить ссылку на новый пост с главной blog section (если Aurora не auto)
- [ ] Обновить 1–2 старых поста → link to new (если есть)
- Manual hub/spoke в body: 6 (ot-excel, minimalizm, obezlichivanie, python-sverka, apps-script, platezhnyj-kalendar)
- Auto-interlinker по B25: 0 (PASS — writer уже закрыл spoke); corpus apply: 1 (B23→B04)

## Метрики (7 дней)

- [ ] Metrika / GA4 — goal `blog_read` или из conversion map
- [ ] Позиция primary query (ручная проверка / Wordstat): банковская выписка в excel автоматически

## Notes

- Indexer: 2026-07-31; llms.txt / llms-full.txt обновлены (21 статей).
- Cover + schema готовы до publish.
