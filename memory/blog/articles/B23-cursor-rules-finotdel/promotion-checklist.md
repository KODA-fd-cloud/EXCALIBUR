# Promotion checklist — B23 cursor-rules-finotdel

Дата публикации: 2026-07-30 (артефакты готовы; **WP publish BLOCKER** — нет FTP/SSH + ALLOW)  
Live URL: https://koda-fd.ru/blog/cursor-rules-finotdel/ (**ожидаемый**; live **404** до повторного publish)

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
Агент снова предлагает закоммитить сырую выгрузку 1С?

• AGENTS.md + 1–3 .mdc: папки data/out, запрет ПДн
• AlwaysApply security-rule — без копипаста в каждый чат
• DoD: rules в git, проверка Agent за 30–45 минут

Читать: https://koda-fd.ru/blog/cursor-rules-finotdel/
```

## Перелинковка

- [ ] Добавить ссылку на новый пост с главной blog section (если Aurora не auto)
- [ ] Обновить 1–2 старых поста → link to new (если есть)

## Метрики (7 дней)

- [ ] Metrika / GA4 — goal `blog_read` или из conversion map
- [ ] Позиция primary query (ручная проверка / Wordstat)

## Notes

- Indexer: interlinker `--apply --blog-dir memory/blog/articles --site-base https://koda-fd.ru` (CLI без `--article-dir`); **1 auto-link** — B23 → B04 (`Claude Code` → `/blog/claude-code-finotdel/`). Ручные internal: `baza-znaniy-chatgpt-cursor-finotdel`, `cursor-finansist-skript-dashbord`, `obezlichivanie-dannyh-chatgpt-finansist`, `mcp-cursor-finansist-instrumenty`.
- llms.txt / llms-full.txt обновлены в `memory/blog/` (site-base https://koda-fd.ru), B23 в индексе (19 статей).
- publish: pending.
