# Promotion checklist — B92 mcp-google-sheets-cursor-reestry

Дата публикации: 2026-09-12  
Live URL: https://koda-fd.ru/blog/mcp-google-sheets-cursor-reestry/ (заполнить после publish)

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
Реестр снова копипастом в чат Cursor? MCP Google Sheets читает и обновляет строки по doc_key без ручной сверки ячеек.

• Path B: mcp-gsheets + service account за 1–2 часа
• Сценарий find → update → re-read с human approval
• Квота Sheets API 60 write/мин на user; Cloud OAuth cursor:// часто ломается

Читать: https://koda-fd.ru/blog/mcp-google-sheets-cursor-reestry/
```

## Перелинковка

- [ ] Добавить ссылку на новый пост с главной blog section (если Aurora не auto)
- [x] B21 → B92 (anchor «Sheets-сервер» в таблице стека)
- [x] B92 FAQ → B82 (anchor «B82»)
- [ ] После publish: ещё 1 inbound из реестровых постов (B51/B58/B83), если есть естественный якорь

## Метрики (7 дней)

- [ ] Metrika / GA4 — goal `blog_read` или из conversion map
- [ ] Позиция primary query «mcp google sheets cursor» (ручная проверка / Wordstat)

## Notes

Indexer 2026-09-12: CLI interlinker без `--article-dir`. Dry-run: 11 B92-matches — все false-positive keyword «2026» → auto `--apply` для B92 **не** запускали (не ломаем UX и volume). Plain B92 = **9298** (банда 8500–9500). Manual: +1 outbound FAQ→B82, +1 inbound B21→B92 (только обёртка `<a>`, plain без изменений). Writer outbound ×4 сохранены → итого outbound internal B92 = 5. `memory/blog/llms.txt` + `llms-full.txt`: 44 статьи, B92 присутствует.
