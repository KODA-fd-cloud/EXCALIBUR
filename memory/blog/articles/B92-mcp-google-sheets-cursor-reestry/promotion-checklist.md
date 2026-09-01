# Promotion checklist — B92 mcp-google-sheets-cursor-reestry

Дата публикации: _(pending — ❌ PUBLISH BLOCKER)_  
Live URL: _(нет — credentials missing)_

Excalibur: preflight + dry-run OK; live WP publish blocked (no `site.env.local` / FTP_* / ALLOW / PUBLIC_SITE_URL).

## Сразу после publish

- [ ] Открыть live URL — title, excerpt, featured image, FAQ
- [ ] View source — JSON-LD BlogPosting + FAQPage
- [ ] Проверить internal links из статьи (200)
- [ ] Яндекс.Вебмастер / GSC — URL отправлен (если настроено)

## Соцсети / каналы

| Канал | Действие | Статус |
|-------|----------|--------|
| Telegram | Пост: hook + ссылка + 1 факт | ☐ blocked (no permalink) |
| VK / Max | Адаптировать под ЦА | ☐ |
| Email / рассылка | Если есть в conversion map | ☐ |

## Перелинковка

- [ ] После успешного publish — interlinker `--apply` для inbound
- [ ] Live URL проставить в этот чеклист

## Notes

- dry-run PASS (PHP ~4.0MB)
- link-verify: QA pass preserved; live SSL timeout egress к koda-fd.ru → ssl_note
- Для разблокировки: Cloud Secrets `EXCALIBUR_BLOG_ALLOW_PUBLISH=yes`, `PUBLIC_SITE_URL`, `FTP_HOST`, `FTP_USER`, `FTP_PASS`, `FTP_ROOT` и/или `memory/site.env.local`
