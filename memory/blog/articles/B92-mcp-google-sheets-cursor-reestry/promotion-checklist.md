# Promotion checklist — B92 mcp-google-sheets-cursor-reestry

Дата публикации: — (publish blocked 2026-08-28)  
Live URL: _pending — ❌ PUBLISH BLOCKER (missing FTP/allow secrets)_

Excalibur создаёт этот файл после `✅ ARTICLE OK` (до или после WP publish).

## Сразу после publish

- [ ] Открыть live URL — title, excerpt, featured image, FAQ
- [ ] View source — JSON-LD BlogPosting + FAQPage (theme или plugin)
- [ ] Проверить internal links из статьи (200)
- [ ] Яндекс.Вебмастер / GSC — URL отправлен (если настроено)

## Соцсети / каналы (из conversion-tracking-map)

| Канал | Действие | Статус |
|-------|----------|--------|
| Telegram | Пост: hook + ссылка + 1 факт из статьи | ☐ blocked until permalink |
| VK / Max | Адаптировать под ЦА | ☐ |
| Email / рассылка | Если есть в conversion map | ☐ |

## Blocker

Нужны Cloud Secrets: `EXCALIBUR_BLOG_ALLOW_PUBLISH`, `PUBLIC_SITE_URL`, `FTP_HOST`, `FTP_USER`, `FTP_PASS`, `FTP_ROOT`.
