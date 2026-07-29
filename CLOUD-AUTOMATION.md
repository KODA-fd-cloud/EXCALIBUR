# Excalibur BLOG — Cloud Automation Setup

Настройка запуска в **Cursor Cloud Agents / Automations** по образцу [kovcheg-office-cloud](https://github.com/Horosheff/kovcheg-office-cloud).

## Что запускаем

Пайплайн одной статьи:

```text
today + research_start → research → writer → geo-qa → cover||schema → indexer → publish?
```

## Структура репозитория (как у Kovcheg Cloud)

```text
<PROJECT_ROOT>/
  AGENTS.md                          ← инструкции Cloud Agent
  CLOUD-AUTOMATION.md                ← этот файл
  .env.example
  .cursor/
    agents/                          ← Task types для Cloud
    skills/
    rules/
    excalibur-blog-handoff.md        ← runtime, не в git
    excalibur-blog-fragments/        ← cover + schema parallel
  agents/                            ← исходники плагина
  skills/
  shared/
  scripts/
  memory/
  .cursor-plugin/plugin.json
```

## Cursor docs

- [Cloud Agents setup](https://cursor.com/docs/cloud-agent/setup.md)
- [Secrets / env vars](https://cursor.com/docs/cloud-agent/setup.md#environment-variables-and-secrets)
- [Automations](https://cursor.com/docs/cloud-agent/automations.md)
- [Self-hosted pool](https://cursor.com/docs/cloud-agent/self-hosted-pool.md)
- [MCP in Cloud](https://cursor.com/docs/cloud-agent/capabilities.md#mcp-tools)

## Self-hosted worker

Нужен, если в облаке Cursor нет:

- MCP KV (`gpt-image-2` для обложек);
- FTP к WordPress;
- стабильного web search для research.

```powershell
cd "<PROJECT_ROOT>"
$env:CURSOR_API_KEY="YOUR_KEY"
$env:EXCALIBUR_PROJECT_ROOT="<PROJECT_ROOT>"
agent worker start --pool --pool-name excalibur-blog --idle-release-timeout 600
```

## Secrets / env vars

Из `.env.example` + Cloud Dashboard:

| Variable | Зачем |
|----------|-------|
| `PUBLIC_SITE_URL` | link verify, recent WP posts |
| `FTP_*` | `excalibur_blog_wp_publish.py` |
| `EXCALIBUR_BLOG_ALLOW_PUBLISH` | `yes` только когда готовы публиковать |
| `EXCALIBUR_TOPIC_ID` | опционально фиксировать тему (иначе today.py предложит P0) |
| `EXCALIBUR_PROJECT_ROOT` | корень репо на worker |

Не коммитить: `memory/site.env.local`, реальные ключи MCP.

## Automation schedule (KODA)

Cursor Automation → Schedule:

```text
0 8,15 * * *
```

- Repository: `KODA-fd-cloud/EXCALIBUR`
- Branch: `master`
- Secrets: `TELEGRAM_BOT_TOKEN`, `TELEGRAM_CHAT_ID`, FTP/WP, `EXCALIBUR_BLOG_ALLOW_PUBLISH`

## Telegram UX (обязательно)

```text
propose → ты: ок/нет
  ок  → бот: «✅ Принято, пишу…» → пайплайн → бот: «🚀 Опубликовано» + URL
  нет → бот: «⏭ Ок, пропускаю…»
```

Команды:

```bash
python3 scripts/excalibur_blog_telegram_notify.py poll --ack
python3 scripts/excalibur_blog_telegram_notify.py ack
python3 scripts/excalibur_blog_telegram_notify.py published --url "https://koda-fd.ru/blog/<slug>/"
python3 scripts/excalibur_blog_telegram_notify.py propose --topic-id B24 --h1 "..."
```

## Automation prompt (шаблон с согласованием)

```text
Ты работаешь в репозитории KODA Excalibur BLOG (KODA-fd-cloud/EXCALIBUR).

Цель: согласование темы в Telegram → статья → публикация → ссылка в Telegram.

0. Прочитай AGENTS.md и shared/agent-pipeline-pitfalls.md.
1. python3 scripts/excalibur_blog_telegram_notify.py poll --ack
   - decision=approve / status=writing → иди в пайплайн для topic_id из pending.
   - decision=reject → предложи следующую тему (шаг 11) и остановись.
   - decision=pending / none → только предложи тему (шаг 11), НЕ пиши статью.
2. Если пишем: python3 scripts/excalibur_blog_today.py + research_start для topic_id.
3. Сбрось .cursor/excalibur-blog-handoff.md; очисти fragments.
4. Task research → writer → geo-qa → cover||schema → indexer → publish.
5. После успешного publish URL:
   python3 scripts/excalibur_blog_telegram_notify.py published --url "<URL>"
6. Закоммить pending-approval.json + published-articles.md + артефакты статьи.
11. Следующая тема: возьми следующую неопубликованную P0 из memory/topics/blog-topics.md
    (не дублировать slug из shared/published-articles.md) и:
    python3 scripts/excalibur_blog_telegram_notify.py propose --topic-id ... --h1 "..." --slug ...
    (кириллица обязательна; читай h1 из blog-topics.md, не транслитом)

Fallback Task types: generalPurpose per role (AGENTS.md).
Запрещено: писать/публиковать без approve; single-agent pipeline; секреты в handoff.
```

## После каждого прогона

Проверь изменения:

- `shared/published-articles.md` (если publish)
- `memory/blog/excalibur-blog-run-log.md`
- артефакты в `memory/blog/articles/<topic_id>-<slug>/`

Если Automation через PR — merge PR, чтобы следующий run видел ledger.

## Локальная разработка плагина

Правки agents/skills делай в `agents/` и `skills/`, затем **синхронизируй в `.cursor/`**:

```powershell
Copy-Item agents\* .cursor\agents\ -Force
Copy-Item skills\* .cursor\skills\ -Recurse -Force
Copy-Item rules\* .cursor\rules\ -Force
```

Или добавь script `scripts/sync_cursor_cloud.ps1` при необходимости.
