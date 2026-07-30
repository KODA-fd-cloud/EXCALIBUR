# Promotion checklist — B23 cursor-rules-finotdel

Дата публикации: 2026-07-30 (publish blocked — credentials/allow flag)  
Live URL: _(pending)_ expected https://koda-fd.ru/blog/cursor-rules-finotdel/

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
Агент снова предлагает закоммитить сырую выгрузку 1С? Cursor Rules для финотдела – устав в файлах проекта.

• AGENTS.md + 2 .mdc (security always + scripts globs)
• data/raw в .gitignore, в чат только clean
• Проверка: Active Rules + тест-промпт на отказ коммита raw

Читать: https://koda-fd.ru/blog/cursor-rules-finotdel/
```

## Перелинковка

- [ ] Добавить ссылку на новый пост с главной blog section (если Aurora не auto)
- [ ] Обновить 1–2 старых поста → link to new (если есть)

## Метрики (7 дней)

- [ ] Metrika / GA4 — goal `blog_read` или из conversion map
- [ ] Позиция primary query (ручная проверка / Wordstat)

## Notes

- Indexer: interlinker `--apply --blog-dir memory/blog/articles --site-base https://koda-fd.ru` (CLI без `--article-dir`); 0 новых auto-links — B23 уже имеет ручные internal links на `baza-znaniy-chatgpt-cursor-finotdel`, `cursor-finansist-skript-dashbord`, `obezlichivanie-dannyh-chatgpt-finansist`, `mcp-cursor-finansist-instrumenty` (4).
- Report: `memory/blog/articles/B23-cursor-rules-finotdel/interlink-report.json` (opportunities_found=0).
- llms.txt / llms-full.txt обновлены в `memory/blog/` (site-base https://koda-fd.ru), B23 в индексе.
- publish: pending (не зона indexer).
