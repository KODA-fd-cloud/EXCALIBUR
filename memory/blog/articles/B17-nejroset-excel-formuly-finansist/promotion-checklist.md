# Promotion checklist — B17 nejroset-excel-formuly-finansist

Дата публикации: 2026-07-22  
Live URL: https://koda-fd.ru/blog/nejroset-excel-formuly-finansist/

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
Выгрузка из 1С не сходится с СУММЕСЛИМН. Нейросеть для Excel — не магия, а ускоритель: ChatGPT/Claude пишут формулы и сводные, вы сверяете контрольной суммой на обезличенном срезе.

• RU-Excel: русские имена функций и разделитель ;
• 10 промптов: СУММЕСЛИМН, XLOOKUP, сводная, дубли, даты 1С
• Чеклист проверки — без сырой первички с ФИО/ИНН в чат

Читать: https://koda-fd.ru/blog/nejroset-excel-formuly-finansist/
```

## Перелинковка

- [ ] Добавить ссылку на новый пост с главной blog section (если Aurora не auto)
- [ ] Обновить 1–2 старых поста → link to new (если есть)

## Метрики (7 дней)

- [ ] Metrika / GA4 — goal `blog_read` или из conversion map
- [ ] Позиция primary query (ручная проверка / Wordstat)

## Notes

- Indexer: interlinker `--apply --blog-dir memory/blog/articles --site-base https://koda-fd.ru` (CLI без `--article-dir`); 0 новых auto-links — B17 уже имеет ручные internal links на `ot-excel-k-fin-konturu-30-dney`, `vibe-coding-finansist`, `obezlichivanie-dannyh-chatgpt-finansist`.
- llms.txt / llms-full.txt обновлены в `memory/blog/` (site-base https://koda-fd.ru), B17 в индексе.
- publish: yes — docker `excalibur_blog_docker_publish.py` 2026-07-22, post_id=146, featured=147.
