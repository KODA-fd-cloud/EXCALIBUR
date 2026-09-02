# Promotion checklist — B92 mcp-google-sheets-cursor-reestry

Дата публикации: — (publish blocked)  
Live URL: —

Excalibur: статья готова (QA/cover/schema/indexer PASS), WP publish заблокирован отсутствием credentials.

## Сразу после publish

- [ ] Открыть live URL — title, excerpt, featured image, FAQ
- [ ] View source — JSON-LD BlogPosting + FAQPage
- [ ] Проверить internal links из статьи (200)
- [ ] Яндекс.Вебмастер / GSC — URL отправлен (если настроено)

## Blocker (2026-09-02)

- ❌ `EXCALIBUR_BLOG_ALLOW_PUBLISH` unset
- ❌ нет `memory/site.env.local` / FTP_*/SSH_*/PUBLIC_SITE_URL
- dry-run OK; link-verify pass (6/6, https://koda-fd.ru)

## Соцсети / каналы

| Канал | Действие | Статус |
|-------|----------|--------|
| Telegram | Пост: hook + ссылка + 1 факт | ☐ pending Live URL |
| VK / Max | Адаптировать под ЦА | ☐ |
| Email / рассылка | Если есть в conversion map | ☐ |

## Перелинковка

- [ ] Inbound с хабов после live permalink
- [ ] Обновить Live URL в этом файле после успешного publish
