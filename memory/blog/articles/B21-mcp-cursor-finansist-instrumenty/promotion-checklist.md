# Promotion checklist — B21 mcp-cursor-finansist-instrumenty

Дата публикации: 2026-07-22  
Live URL: https://koda-fd.ru/blog/mcp-cursor-finansist-instrumenty/

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
Пять CSV в папке выгрузок — снова копируете куски в чат Cursor? MCP даёт агенту инструменты: читает папку без копипаста.

• Первый сервер: filesystem на узкий path data/
• Tools & MCP / mcp.json → зелёный статус + approve tool
• Сценарий: summary по CSV за 20–40 минут

Читать: https://koda-fd.ru/blog/mcp-cursor-finansist-instrumenty/
```

## Перелинковка

- [ ] Добавить ссылку на новый пост с главной blog section (если Aurora не auto)
- [ ] Обновить 1–2 старых поста → link to new (если есть)

## Метрики (7 дней)

- [ ] Metrika / GA4 — goal `blog_read` или из conversion map
- [ ] Позиция primary query (ручная проверка / Wordstat)

## Notes

- Indexer: interlinker `--apply --blog-dir memory/blog/articles --site-base https://koda-fd.ru` (CLI без `--article-dir`); 0 новых auto-links — B21 уже имеет ручные internal links на `cursor-finansist-skript-dashbord`, `cursor-ai-agenty-finotchetnost` и др.
- llms.txt / llms-full.txt обновлены в `memory/blog/` (site-base https://koda-fd.ru), B21 в индексе.
- publish: pending docker (`excalibur_blog_docker_publish.py`).
