# Promotion checklist — B24 n8n-finotdel-ustanovka-pervyj-workflow

Дата публикации: 2026-07-31 (planned; WP publish blocked — secrets)  
Live URL: _(pending)_ — ожидаемый: https://koda-fd.ru/blog/n8n-finotdel-ustanovka-pervyj-workflow/

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
Выписки в Sheets, собственник ждёт дайджест в Telegram – руками ломается в первый отпуск.

• Self-hosted n8n на Docker + Traefik HTTPS и WEBHOOK_URL
• Первый workflow: Sheets Trigger → фильтр → Telegram
• Сырые выписки не на чужой SaaS – свой контур под 152-ФЗ

Читать: https://koda-fd.ru/blog/n8n-finotdel-ustanovka-pervyj-workflow/
```

## Перелинковка

- [ ] Добавить ссылку на новый пост с главной blog section (если Aurora не auto)
- [ ] Обновить 1–2 старых поста → link to new (если есть)

## Метрики (7 дней)

- [ ] Metrika / GA4 — goal `blog_read` или из conversion map
- [ ] Позиция primary query (ручная проверка / Wordstat)

## Notes

- Indexer: interlinker `--apply --blog-dir memory/blog/articles --site-base https://koda-fd.ru` (CLI без `--article-dir`); применено 2 auto-links по корпусу: B14→B24 (`n8n self-hosted`), B23→B04 (`Claude Code`). В B24 новых auto-links = 0 — writer уже вставил 4 hub/spoke (PASS).
- llms.txt / llms-full.txt обновлены в `memory/blog/` (site-base https://koda-fd.ru), B24 в индексе.
- publish: pending (indexer не запускает publish).
