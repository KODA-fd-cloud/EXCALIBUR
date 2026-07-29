# Promotion checklist — B20 cursor-finansist-skript-dashbord

Дата публикации: 2026-07-22  
Live URL: https://koda-fd.ru/blog/cursor-finansist-skript-dashbord/

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
Два CSV на столе: банк и 1С. В Excel сверка съедает вечер, в веб-чате — риск слить ФИО. В Cursor за вечер: скрипт расхождений + локальный дашборд.

• Папка data/ + .gitignore, без сырых ПДн в чат
• Промпт сверки → out/mismatches.csv
• Мини-дашборд Streamlit/HTML на localhost

Читать: https://koda-fd.ru/blog/cursor-finansist-skript-dashbord/
```

## Перелинковка

- [ ] Добавить ссылку на новый пост с главной blog section (если Aurora не auto)
- [ ] Обновить 1–2 старых поста → link to new (если есть)

## Метрики (7 дней)

- [ ] Metrika / GA4 — goal `blog_read` или из conversion map
- [ ] Позиция primary query (ручная проверка / Wordstat)

## Notes

- Indexer: interlinker `--apply --blog-dir memory/blog/articles --site-base https://koda-fd.ru` (CLI без `--article-dir`); 0 новых auto-links — B20 уже имеет ручные internal links на `cursor-ai-agenty-finotchetnost`, `obezlichivanie-dannyh-chatgpt-finansist`, `vibe-coding-finansist`, `claude-code-finotdel`.
- llms.txt / llms-full.txt обновлены в `memory/blog/` (site-base https://koda-fd.ru), B20 в индексе.
- publish: yes — docker (`excalibur_blog_docker_publish.py`), post_id=142, featured=144, verdict pass.
