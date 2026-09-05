# Excalibur BLOG — WP publish log

## 2026-07-22 — B18 schet-1c-unf-telefon-http-servis — **PASS**

| Field | Value |
|-------|-------|
| topic_id | B18 |
| slug | schet-1c-unf-telefon-http-servis |
| verdict | **PASS** |
| post_id | 152 |
| featured_image_id | 156 |
| inline_images | — |
| permalink | https://koda-fd.ru/blog/schet-1c-unf-telefon-http-servis/ |
| method | ssh_docker_exec |

### Preconditions

- article-qa.md: PASS (92/100)
- link-verify.json: pass (QA); recheck SSL-noise local
- schema.jsonld: present
- cover/cover.png + alt: present
- CTA conversion-map: club×1 + TG×1, no salebot
- EXCALIBUR_BLOG_ALLOW_PUBLISH: yes

### Result

`
OK post=152 slug=schet-1c-unf-telefon-http-servis
OK featured_image=156
OK dzen_cover_url=https://koda-fd.ru/blog/wp-content/uploads/2026/07/schet-1c-unf-telefon-http-servis-dzen-cover-1.png
OK schema_meta=1
OK skip_theme_faq_meta=1
permalink=https://koda-fd.ru/blog/schet-1c-unf-telefon-http-servis/
`

---
## 2026-07-22 — B21 mcp-cursor-finansist-instrumenty — **PASS**

| Field | Value |
|-------|-------|
| topic_id | B21 |
| slug | mcp-cursor-finansist-instrumenty |
| verdict | **PASS** |
| post_id | 149 |
| featured_image_id | 150 |
| inline_images | — |
| permalink | https://koda-fd.ru/blog/mcp-cursor-finansist-instrumenty/ |
| method | ssh_docker_exec |

### Preconditions

- article-qa.md: PASS (92/100)
- link-verify.json: pass
- schema.jsonld: present
- cover/cover.png + alt: present
- CTA conversion-map: club + finance_modern, no salebot
- EXCALIBUR_BLOG_ALLOW_PUBLISH: yes

### Result

`
OK post=149 slug=mcp-cursor-finansist-instrumenty
OK featured_image=150
OK dzen_cover_url=https://koda-fd.ru/blog/wp-content/uploads/2026/07/mcp-cursor-finansist-instrumenty-dzen-cover.png
OK schema_meta=1
OK skip_theme_faq_meta=1
permalink=https://koda-fd.ru/blog/mcp-cursor-finansist-instrumenty/
`

---
## 2026-07-22 — B17 nejroset-excel-formuly-finansist — **PASS**

| Field | Value |
|-------|-------|
| topic_id | B17 |
| slug | nejroset-excel-formuly-finansist |
| verdict | **PASS** |
| post_id | 146 |
| featured_image_id | 147 |
| inline_images | — |
| permalink | https://koda-fd.ru/blog/nejroset-excel-formuly-finansist/ |
| method | ssh_docker_exec |

### Preconditions

- article-qa.md: PASS (92/100)
- link-verify.json: pass (5/5, ssl unverified recheck)
- schema.jsonld: present
- cover/cover.png + alt: present
- CTA conversion-map: TG×2 + club×1, no salebot
- EXCALIBUR_BLOG_ALLOW_PUBLISH: yes

### Result

```
OK post=146 slug=nejroset-excel-formuly-finansist
OK featured_image=147
OK dzen_cover_url=https://koda-fd.ru/blog/wp-content/uploads/2026/07/nejroset-excel-formuly-finansist-dzen-cover.png
OK schema_meta=1
OK skip_theme_faq_meta=1
permalink=https://koda-fd.ru/blog/nejroset-excel-formuly-finansist/
```

---

## 2026-07-22 — B20 cursor-finansist-skript-dashbord — **PASS**

| Field | Value |
|-------|-------|
| topic_id | B20 |
| slug | cursor-finansist-skript-dashbord |
| verdict | **PASS** |
| post_id | 142 |
| featured_image_id | 144 |
| inline_images | — |
| permalink | https://koda-fd.ru/blog/cursor-finansist-skript-dashbord/ |
| method | ssh_docker_exec |

### Preconditions

- article-qa.md: PASS (92/100)
- link-verify.json: pass (9/9, ssl unverified recheck)
- schema.jsonld: present
- cover/cover.png + alt: present
- EXCALIBUR_BLOG_ALLOW_PUBLISH: yes

### Result

```
OK post=142 slug=cursor-finansist-skript-dashbord
OK featured_image=144
OK dzen_cover_url=https://koda-fd.ru/blog/wp-content/uploads/2026/07/cursor-finansist-skript-dashbord-dzen-cover.png
OK schema_meta=1
OK skip_theme_faq_meta=1
permalink=https://koda-fd.ru/blog/cursor-finansist-skript-dashbord/
```

---

## 2026-06-11 — B02 avtomatizaciya-n8n-ai-agents

| Field | Value |
|-------|-------|
| topic_id | B02 |
| slug | avtomatizaciya-n8n-ai-agents |
| verdict | **FAIL** |
| post_id | — |
| permalink | — |

### Preconditions

- article-qa.md: PASS (93/100)
- link-verify.json: pass
- schema.jsonld: present
- cover/cover.png + alt: present
- EXCALIBUR_BLOG_ALLOW_PUBLISH: yes

### Attempt

```bash
python scripts/excalibur_blog_wp_publish.py --article-dir memory/blog/articles/B02-avtomatizaciya-n8n-ai-agents --dry-run  # OK
python scripts/excalibur_blog_wp_publish.py --article-dir memory/blog/articles/B02-avtomatizaciya-n8n-ai-agents       # FAIL
```

### Blockers

1. **Network:** HTTPS к `mayai.ru:443` недоступен из локальной среды (WinError 10060). FTP (порт 21) работает, HTTP-триггер bootstrap — нет.
2. **FTP path:** аккаунт `***_blog` видит только `/index.php` + `/cgi-bin/`, **без** `wp-load.php`. WordPress на `https://mayai.ru/blog/` — другой document root.
3. **Bootstrap 404:** загруженный `excalibur-blog-publish-once.php` (и тестовый `excalibur-test-once.php`) отдают HTTP 404 снаружи, хотя `index.php` в том же FTP root отдаётся на главной.

### Cleanup

Временные bootstrap-файлы удалены с FTP после диагностики.

### Next steps (для оператора)

1. Обновить `memory/site.env.local`: FTP_USER/FTP_PASS + `FTP_ROOT=/` (корень FTP после login, где `wp-load.php`). Путь панели хостинга: `FTP_PANEL_PATH=/your-account.beget.tech/public_html/`.
2. Либо запустить publish с машины/сети, где `curl https://mayai.ru` отвечает < 5 с.
3. Альтернатива: WP Application Password + REST API / MCP WordPress blob publish.

---

## 2026-06-11 (retry) — B02 avtomatizaciya-n8n-ai-agents — **PASS**

| Field | Value |
|-------|-------|
| topic_id | B02 |
| slug | avtomatizaciya-n8n-ai-agents |
| verdict | **PASS** |
| post_id | 13324 |
| featured_image_id | 13325 |
| permalink | https://mayai.ru/avtomatizaciya-n8n-ai-agents/ |
| FTP_ROOT | `/` |

### Fix applied

- Обновлены FTP credentials в `memory/site.env.local` (локально, не в git)
- `FTP_ROOT=/` (wp-load.php в корне аккаунта после login)
- `excalibur_blog_wp_publish.py` — поддержка `FTP_ROOT` из env

### Result

```
OK post=13324 slug=avtomatizaciya-n8n-ai-agents
OK featured_image=13325
OK schema_meta=1
permalink=https://mayai.ru/avtomatizaciya-n8n-ai-agents/
```

---

## 2026-06-11 — B03 podklyuchenie-mcp-cursor — **PASS**

| Field | Value |
|-------|-------|
| topic_id | B03 |
| slug | podklyuchenie-mcp-cursor |
| verdict | **PASS** |
| post_id | 13335 |
| featured_image_id | 13336 |
| inline_images | 13337, 13338, 13339 |
| permalink | https://mayai.ru/podklyuchenie-mcp-cursor/ |
| trigger | `/excalibur-blog-run topic_id: B03 publish: yes` (publish вручную после fix оркестратора) |

### Result

```
OK post=13335 slug=podklyuchenie-mcp-cursor
OK featured_image=13336
OK schema_meta=1
OK inline_image_upload=13337 src=cover/inline-01.png
OK inline_image_upload=13338 src=cover/inline-02.png
OK inline_image_upload=13339 src=cover/inline-03.png
permalink=https://mayai.ru/podklyuchenie-mcp-cursor/
```

---

## 2026-06-11 — B04 geo-optimizaciya-sajta-2026 — **PASS**

| Field | Value |
|-------|-------|
| topic_id | B04 |
| slug | geo-optimizaciya-sajta-2026 |
| verdict | **PASS** |
| post_id | 13361 |
| featured_image_id | 13362 |
| inline_images | 13363, 13364, 13365 |
| permalink | https://mayai.ru/geo-optimizaciya-sajta-2026/ |
| trigger | `/excalibur-blog-run topic_id: B04 publish: yes` |

### Preconditions

- article-qa.md: PASS (94/100)
- link-verify.json: pass (5/5)
- schema.jsonld: present
- cover/cover.png + alt: present
- EXCALIBUR_BLOG_ALLOW_PUBLISH: yes

### Result

```
OK post=13361 slug=geo-optimizaciya-sajta-2026
OK featured_image=13362
OK schema_meta=1
OK skip_theme_faq_meta=1
OK inline_image_upload=13363 src=cover/inline-01.png url=https://mayai.ru/wp-content/uploads/2026/06/geo-optimizaciya-sajta-2026-inline-01.jpg
OK inline_image_upload=13364 src=cover/inline-02.png url=https://mayai.ru/wp-content/uploads/2026/06/geo-optimizaciya-sajta-2026-inline-02.jpg
OK inline_image_upload=13365 src=cover/inline-03.png url=https://mayai.ru/wp-content/uploads/2026/06/geo-optimizaciya-sajta-2026-inline-03.jpg
permalink=https://mayai.ru/geo-optimizaciya-sajta-2026/
```

### Post-publish

- interlinker --apply: 0 new opportunities (B01 inbound already applied at indexer step)

---

## 2026-06-11 — B05 avtonomnyj-kontent-zavod-nejroseti — **PASS**

| Field | Value |
|-------|-------|
| topic_id | B05 |
| slug | avtonomnyj-kontent-zavod-nejroseti |
| verdict | **PASS** |
| post_id | 13369 |
| featured_image_id | 13370 |
| inline_images | 13371, 13372, 13373 |
| permalink | https://mayai.ru/avtonomnyj-kontent-zavod-nejroseti/ |
| trigger | `/excalibur-blog-run topic_id: B05 publish: yes` |

### Preconditions

- article-qa.md: PASS (95/100)
- link-verify.json: pass (5/5)
- schema.jsonld: present
- cover/cover.png + alt: present
- EXCALIBUR_BLOG_ALLOW_PUBLISH: yes

### Result

```
OK post=13369 slug=avtonomnyj-kontent-zavod-nejroseti
OK featured_image=13370
OK schema_meta=1
OK skip_theme_faq_meta=1
OK inline_image_upload=13371 src=cover/inline-01.png url=https://mayai.ru/wp-content/uploads/2026/06/avtonomnyj-kontent-zavod-nejroseti-inline-01.jpg
OK inline_image_upload=13372 src=cover/inline-02.png url=https://mayai.ru/wp-content/uploads/2026/06/avtonomnyj-kontent-zavod-nejroseti-inline-02.jpg
OK inline_image_upload=13373 src=cover/inline-03.png url=https://mayai.ru/wp-content/uploads/2026/06/avtonomnyj-kontent-zavod-nejroseti-inline-03.jpg
permalink=https://mayai.ru/avtonomnyj-kontent-zavod-nejroseti/
```

---

## 2026-07-22 — B14/B15/B16 docker publish — **PASS**

| topic_id | slug | post_id | permalink |
|----------|------|---------|-----------|
| B14 | upravlenie-debitorkoj-reestr-napominaniya | 134 | https://koda-fd.ru/blog/upravlenie-debitorkoj-reestr-napominaniya/ |
| B15 | ollama-finotdel-lokalnaya-nejroset | 137 | https://koda-fd.ru/blog/ollama-finotdel-lokalnaya-nejroset/ |
| B16 | baza-znaniy-chatgpt-cursor-finotdel | 140 | https://koda-fd.ru/blog/baza-znaniy-chatgpt-cursor-finotdel/ |

method: `excalibur_blog_docker_publish.py` (ssh_docker_exec)
QA: PASS; cover gradient_abstract; schema BlogPosting+FAQPage; CTA club+tg only

---

## 2026-09-05 — B92 mcp-google-sheets-cursor-reestry — **❌ PUBLISH BLOCKER**

| Field | Value |
|-------|-------|
| topic_id | B92 |
| slug | mcp-google-sheets-cursor-reestry |
| verdict | **blocker** |
| permalink | (нет) |
| trigger | continue_pipeline / telegram tick approve |

### Preconditions

- article-qa.md: PASS (91/100)
- link-verify.json: pass (6/6, site-base https://koda-fd.ru inferred)
- schema.jsonld: present
- cover/cover.png + alt: present
- EXCALIBUR_BLOG_ALLOW_PUBLISH: **MISSING** (≠ yes)
- memory/site.env.local: **absent**
- PUBLIC_SITE_URL / FTP_* / SSH_*: **MISSING**

### Steps

1. Preflight link-verify: **pass**
2. Dry-run: **pass** (Pillow installed in env for cover decode; slug/title OK)
3. Publish: **aborted** — `FileNotFoundError: No publish credentials`
4. Fallback WebFetch: not applicable (no trigger URL; no FTP bootstrap)
5. published-articles.md: **not updated** (no live URL)

### Blocker fix

Add Cloud Secrets / `memory/site.env.local`: `EXCALIBUR_BLOG_ALLOW_PUBLISH=yes`, `PUBLIC_SITE_URL`, `FTP_HOST`/`FTP_USER`/`FTP_PASS`/`FTP_ROOT` (or SSH_*), then re-run step ⑥ only.

