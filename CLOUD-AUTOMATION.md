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
propose → ты: ок / нет
  ок  → «✅ Принято, пишу…» → пайплайн → «🚀 Опубликовано» + URL
  нет → «⏭ Пропускаю…» + СРАЗУ следующая тема
        (и так по кругу, пока не скажешь ок)
```

Команды:

```bash
python3 scripts/excalibur_blog_telegram_notify.py tick                 # слот по расписанию (всегда пишет в Telegram)
python3 scripts/excalibur_blog_telegram_notify.py propose --auto
python3 scripts/excalibur_blog_telegram_notify.py poll --ack
python3 scripts/excalibur_blog_telegram_notify.py published --url "https://koda-fd.ru/blog/<slug>/"
```

## Automation prompt (шаблон с согласованием)

```text
Ты работаешь в репозитории KODA Excalibur BLOG (KODA-fd-cloud/EXCALIBUR).

Цель: согласование темы в Telegram → статья → публикация → ссылка в Telegram.

0. Прочитай AGENTS.md и shared/agent-pipeline-pitfalls.md.
1. Env: TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID (иначе сразу ❌ БЛОКЕР).
2. ПЕРВЫМ делом:
   python3 scripts/excalibur_blog_telegram_notify.py tick
   JSON:
   - action=reminded|proposed + status=pending → ОСТАНОВИСЬ (жди ок; статья не пишется).
   - action=handled_reply + reject_then_next → ОСТАНОВИСЬ.
   - status=writing / continue_pipeline → пиши пайплайн для topic_id.
   - empty_queue → ОСТАНОВИСЬ.
3. Если writing: today + research_start → research → writer → geo-qa → cover||schema → indexer → publish.
4. После publish:
   python3 scripts/excalibur_blog_telegram_notify.py published --url "<URL>"
5. Закоммить/запушь pending-approval.json, published-articles.md, артефакты.

Запрещено: длинный await в начале; писать без status=writing; single-agent pipeline; секреты в ответах.
Кириллица обязательна.
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
