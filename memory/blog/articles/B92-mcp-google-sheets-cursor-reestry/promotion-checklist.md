# Promotion checklist — B92 mcp-google-sheets-cursor-reestry

Дата публикации: YYYY-MM-DD  
Live URL: https://koda-fd.ru/blog/mcp-google-sheets-cursor-reestry/

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
Реестр договоров снова уезжает в чат Cursor кусками? MCP Google Sheets убирает копипаст: Agent правит строку по doc_key через mcp-gsheets + service account.

• Path B: SA + Share + mcp.json за 1–2 часа
• Цикл find → update → re-read без «официального» Marketplace Sheets
• Без сырых ПДн и без Auto-run write

Читать: https://koda-fd.ru/blog/mcp-google-sheets-cursor-reestry/
```

## Перелинковка

- [ ] Добавить ссылку на новый пост с главной blog section (если Aurora не auto)
- [ ] Обновить 1–2 старых поста → link to new (если есть)

## Метрики (7 дней)

- [ ] Metrika / GA4 — goal `blog_read` или из conversion map
- [ ] Позиция primary query (ручная проверка / Wordstat)

## Notes

- Indexer: dry-run interlinker → 11 outbound на keyword «2026» (junk) — `--apply` не запускали.
- Ручные contextual links (HEAD 200): B80 mcp-1c, B51 reestr-dogovorov, B58 reestr-upd, B24 platezhnyj-kalendar, усиление B82; writer уже имел B21 / B82 / no-code / обезличивание.
- B02/B03 не линковали (live 404).
- llms.txt / llms-full.txt: `memory/blog/` (site-base https://koda-fd.ru), 44 статьи, B92 в индексе.
- link-verify: pass, failed_count=0 (unique internal+CTA).
- ❌ PUBLISH BLOCKER 2026-09-08: нет FTP_*/PUBLIC_SITE_URL/ALLOW_PUBLISH — Live URL выше = ожидаемый slug, **не подтверждён publish**.

