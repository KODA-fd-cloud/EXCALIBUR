# Promotion checklist — B59 zayavka-na-rashod-google-forms

Дата публикации: 2026-08-15  
Live URL: https://koda-fd.ru/blog/zayavka-na-rashod-google-forms/ (заполнить после publish)

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
Заявки на расход через почту и Excel теряются — сумма в одном письме, чек в другом, согласование в мессенджере.

• Google Forms + Sheets за 2–4 часа: один реестр со статусами согласования и оплатой
• Поля формы, колонки status/approved_amount/payment_date, email и Apps Script
• Отличие от кассового расхода и «заявки на расходование ДС» в 1С

Читать: https://koda-fd.ru/blog/zayavka-na-rashod-google-forms/
```

## Перелинковка

- [ ] Добавить ссылку на новый пост с главной blog section (если Aurora не auto)
- [ ] Обновить 1–2 старых поста → link to new (если есть)

## Метрики (7 дней)

- [ ] Metrika / GA4 — goal `blog_read` или из conversion map
- [ ] Позиция primary query «заявка на расход google forms» (ручная проверка / Wordstat)

## Notes

Indexer: interlinker `--apply` по корпусу (35 статей, site-base koda-fd.ru). B59 `article.html` без изменений — 4 internal links от writer сохранены. 24 входящих возможности (anchor «2026» из secondary_queries) не применены: коллизия offset с другими статьями на том же «2026». Hub: +24 исходящих ссылки в других постах. `memory/blog/llms.txt` и `llms-full.txt` — 35 статей, B59 добавлена.
