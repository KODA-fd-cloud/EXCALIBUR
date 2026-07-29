# Promotion checklist — B18 schet-1c-unf-telefon-http-servis

Дата публикации: 2026-07-22  
Live URL: https://koda-fd.ru/blog/schet-1c-unf-telefon-http-servis/

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
Клиент готов платить вечером, а бухгалтер уже недоступен — сделка остывает.

• Узкий HTTP-сервис в УНФ + PWA/Telegram вместо толстого клиента
• Документ в живой базе + PDF сразу на экране
• Пароль 1С только на бэкенде, не в телефоне

Читать: https://koda-fd.ru/blog/schet-1c-unf-telefon-http-servis/
```

## Перелинковка

- [ ] Добавить ссылку на новый пост с главной blog section (если Aurora не auto)
- [ ] Обновить 1–2 старых поста → link to new (если есть)

## Метрики (7 дней)

- [ ] Metrika / GA4 — goal `blog_read` или из conversion map
- [ ] Позиция primary query (ручная проверка / Wordstat)

## Notes

- CTA check (conversion-map): Telegram 1×, клуб KODA 1× — в лимитах; koda_salebot нет.
- Indexer: interlinker `--apply --blog-dir memory/blog/articles --site-base https://koda-fd.ru` (CLI без `--article-dir`); 0 новых auto-links — B18 уже имеет ручные internal links.
- llms.txt / llms-full.txt обновлены в `memory/blog/` (B18 в индексе).
- publish: PASS via docker (`excalibur_blog_docker_publish.py`); post_id=152, featured=156.
