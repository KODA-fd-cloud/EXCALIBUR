# KODA × Excalibur BLOG — SEO/GEO машина

Блог: https://koda-fd.ru/blog/  
Telegram: https://t.me/finance_modern  
Клуб: https://koda-fd.ru/club  
Клуб: https://club.koda-fd.ru/  

## Быстрый старт

Уже сделано автоматически:
- Плагин: `C:\Users\Ольга\.cursor\plugins\local\koda-excalibur-blog` (junction на эту папку)
- `memory/site.env.local` — доступы koda-fd.ru
- CTA в теме WP — `node scripts/deploy-blog-theme.mjs` из корня `d:\Сайт`

**Тебе:** Cursor → Settings → Plugins → убедись что **KODA Excalibur BLOG** включён (Reload если не видишь).

### 1. Секреты

Файл `memory/site.env.local` уже создан. Меняй только если сменился пароль VPS.

В чате Cursor (проект `koda-blog-pipeline`):

```
Прочитай AGENTS.md и shared/agent-pipeline-pitfalls.md.
Запусти пайплайн Excalibur BLOG для темы B01.
EXCALIBUR_BLOG_ALLOW_PUBLISH=no — только артефакты в memory/blog/.
```

### 4. Публикация

Когда GEO QA = PASS:

```
EXCALIBUR_BLOG_ALLOW_PUBLISH=yes
python scripts/excalibur_blog_wp_publish.py --article-dir memory/blog/articles/B01-<slug>
```

### 5. Деплой CTA в тему WP

Скопируй из `d:\Сайт\deploy\` на хостинг темы `koda-blog`:

- `koda-blog-cta.php` → `functions.php`: `require_once get_template_directory() . '/koda-blog-cta.php';`
- `single.php`, `style-patch.css` (дополнить существующий)

## Пайплайн

```
today.py → research → writer → geo-qa → cover||schema → indexer → publish
```

Темы: `memory/topics/blog-topics.md`  
CTA/офферы: `memory/brief/conversion-map.md`  
Автор: `shared/authors-registry.json` (olga-kondratskaya)

## Автоматизация (позже)

См. `CLOUD-AUTOMATION.md` — Cursor Automation 2×/день после 3–5 ручных статей.
