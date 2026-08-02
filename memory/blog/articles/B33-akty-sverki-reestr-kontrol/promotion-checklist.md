# Promotion checklist — B33 akty-sverki-reestr-kontrol

Дата публикации: YYYY-MM-DD  
Live URL: https://koda-fd.ru/blog/akty-sverki-reestr-kontrol/

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
Акты уходят в почту и ЭДО, а ответы теряются в чатах: кто подписал, кто молчит, где спор.

• Реестр в Sheets/Excel: статус, срок ответа, сальдо
• Напоминания Sheets → n8n → email без CRM (лимит 2 касания)
• Связка с дебиторкой и закрытием месяца

Читать: https://koda-fd.ru/blog/akty-sverki-reestr-kontrol/
```

## Перелинковка

- [ ] Добавить ссылку на новый пост с главной blog section (если Aurora не auto)
- [ ] Обновить 1–2 старых поста → link to new (если есть)

## Метрики (7 дней)

- [ ] Metrika / GA4 — goal `blog_read` или из conversion map
- [ ] Позиция primary query (ручная проверка / Wordstat)

## Notes

- Indexer: interlinker `--apply --blog-dir memory/blog/articles --site-base https://koda-fd.ru` (CLI без `--article-dir`); auto-links applied=2 (B23→B04, B28→B04); B33 inbound auto-links=0 — у B33 уже есть ручные internal links на `upravlenie-debitorkoj-reestr-napominaniya` и `sverka-bank-1c-bez-pdn`.
- llms.txt / llms-full.txt обновлены в `memory/blog/` (site-base https://koda-fd.ru), B33 в индексе (26 статей).
- publish: pending.
