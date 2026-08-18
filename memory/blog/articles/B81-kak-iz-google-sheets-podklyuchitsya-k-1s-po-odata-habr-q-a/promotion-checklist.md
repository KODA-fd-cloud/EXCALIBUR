# Promotion checklist — B81 kak-iz-google-sheets-podklyuchitsya-k-1s-po-odata-habr-q-a

Дата публикации: 2026-08-18  
Live URL: https://koda-fd.ru/blog/kak-iz-google-sheets-podklyuchitsya-k-1s-po-odata-habr-q-a/ (заполнить после publish)

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
Excel и браузер видят OData 1С, а Google Sheets через Apps Script пишет «Адрес недоступен» — чаще всего виновата сеть UrlFetch, не «кривая» таблица.

• Публичный HTTPS + Basic Auth в Apps Script (без credentials:include)
• Срез JSON на лист raw_* и кнопка «Обновить из 1С»
• Когда Sheets↔OData нужен финотделу, а когда лучше CSV / Power Query

Читать: https://koda-fd.ru/blog/kak-iz-google-sheets-podklyuchitsya-k-1s-po-odata-habr-q-a/
```

## Перелинковка

- [ ] Добавить ссылку на новый пост с главной blog section (если Aurora не auto)
- [ ] Обновить 1–2 старых поста → link to new (после publish; сейчас inbound на B81 не ставили — slug ещё не в published-articles.md)

## Метрики (7 дней)

- [ ] Metrika / GA4 — goal `blog_read` или из conversion map
- [ ] Позиция primary query «как из google sheets подключиться к 1с по odata хабр q a» (ручная проверка / Wordstat)

## Notes

Indexer: interlinker по корпусу (38 статей, site-base https://koda-fd.ru). Raw opportunities=212; skipped bare year «2026»=210; unpublished inbound B81=0. Applied=2 (B23→claude-code-finotdel, B28→claude-code-finotdel). B81 `article.html` без изменений — 4 outbound internal links от writer сохранены. `memory/blog/llms.txt` и `llms-full.txt` — 38 статей, B81 добавлена.
