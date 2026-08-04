# Promotion checklist — B43 limity-rashodov-telegram-alert

Дата публикации: 2026-08-04  
Live URL: https://koda-fd.ru/blog/limity-rashodov-telegram-alert/

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
Перерасход по рекламе узнаёте в пятницу из чата — а не в день, когда статья пересекла 80%?

• Реестр лимитов в Google Sheets (порог + last_alert)
• n8n/Make → Telegram при 80% бюджета
• Антиспам: одно сообщение, не пуш на каждую проводку

Читать: https://koda-fd.ru/blog/limity-rashodov-telegram-alert/
```

## Перелинковка

- [ ] Добавить ссылку на новый пост с главной blog section (если Aurora не auto)
- [ ] Обновить 1–2 старых поста → link to new (если есть)

## Метрики (7 дней)

- [ ] Metrika / GA4 — goal `blog_read` или из conversion map
- [ ] Позиция primary query (ручная проверка / Wordstat)

## Notes

- Indexer: interlinker `--apply --blog-dir memory/blog/articles --site-base https://koda-fd.ru` (CLI без `--article-dir`).
- Из meta B43 убран secondary_query `2026` (иначе auto-link «2026» → unpublished B43).
- Auto-apply: 2 ссылки published→published (`B23`/`B28` → `claude-code-finotdel`); inbound на unpublished B43 не создавался.
- Manual outbound в B43 (только published): `daydzhest-sobstvenniku-n8n-telegram`, `spravochnik-kategorij-dds`, `bankovskaya-vypiska-staging-google-sheets`, `platezhnyj-kalendar-google-sheets-n8n` + уже были `obezlichivanie-dannyh-chatgpt-finansist`, `avtomatizaciya-finansov-no-code`.
- llms.txt / llms-full.txt: `memory/blog/` (site-base https://koda-fd.ru, КОДА), B43 в индексе.
- publish: pending после indexer.
