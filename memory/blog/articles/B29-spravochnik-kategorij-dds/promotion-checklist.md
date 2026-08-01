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
В одной таблице «Аренда», в другой «аренда офиса» — план-факт разъезжается на сотни тысяч без ошибки в сумме.

• Лист «Справочник» на 15–25 статей + data validation
• Запрет свободного ввода и правила для «Прочее»/переводов
• Один код категории на операции, план-факт и дашборд

Читать: https://koda-fd.ru/blog/spravochnik-kategorij-dds/
```

## Перелинковка

- [ ] Добавить ссылку на новый пост с главной blog section (если Aurora не auto)
- [ ] Обновить 1–2 старых поста → link to new (если есть)

## Метрики (7 дней)

- [ ] Metrika / GA4 — goal `blog_read` или из conversion map
- [ ] Позиция primary query (ручная проверка / Wordstat)

## Notes

- Indexer: interlinker `--apply --blog-dir memory/blog/articles --site-base https://koda-fd.ru` (CLI без `--article-dir`); 2 auto-links: B23→B04 и B28→B04 (anchor «Claude Code»). B29 уже имеет ручные internal на `disnejlend-dlya-dannyh` и `bankovskaya-vypiska-staging-google-sheets`; B26 `/plan-fakt-dds-google-sheets/` — plain text, без href.
- llms.txt / llms-full.txt обновлены в `memory/blog/` (site-base https://koda-fd.ru), B29 в индексе.
- publish: pending после Indexer.
