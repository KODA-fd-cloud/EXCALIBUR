# Research notes — B92

**topic_id:** B92  
**slug:** mcp-google-sheets-cursor-reestry  
**h1:** Как подключить MCP к Google Sheets в Cursor и править реестры без копипаста  
**research_date:** 2026-09-08  
**publish_target:** koda-fd.ru/blog  
**utility_gate:** PASS (`how_to`, mode B) — подтверждено `utility-gate-topic.json` + `excalibur_blog_utility_gate.py --topic-id B92`  
**author_id:** olga-kondratskaya  
**related_internal:** `/avtomatizaciya-finansov-no-code/`, `/obezlichivanie-dannyh-chatgpt-finansist/`  
**sibling_queue:** B82 (Sheets API + SA), B21 (MCP в Cursor общий), B51/B58/B83 (реестры в Sheets), B93 (ротация SA)  
**cover_scene_hint:** abstract holographic finance automation dark #0a0a0f purple #8b5cf6, no text

---

## utility_verdict

**PASS** — utility-only how_to. Читатель получает рабочий маршрут: service account + community MCP `mcp-gsheets` в Cursor → правка реестра по `doc_key` без копипаста таблицы в чат → verify-loop перечиткой. Честно: официальный changelog Cursor 03.08.2026 описывает плагины **Drive / Gmail / Calendar**, не Sheets; cell-edit реестров — через community MCP (или hosted/Composio), не через «магический» Marketplace Sheets. Не новость про Workspace, не обзор 25 MCP.

---

## reader_outcome

После гайда финансист сможет подключить `mcp-gsheets` к Cursor через service account, расшарить только нужный реестр, попросить агента найти строку по `doc_key`, обновить статус/комментарий через MCP-tool и подтвердить результат перечиткой диапазона.

---

## action_outline

1. **Решить, нужен ли MCP Sheets** — реестр уже в Google Sheets (договоры, УПД, SaaS, заявки), правки повторяются, устали таскать диапазоны в чат; **не** делать, если нужен жёсткий audit trail / сотни таблиц с enterprise ACL → 1С/CLM, Sheets только staging.
2. **Выбрать путь** — **рекомендация КОДА (Path B):** `freema/mcp-gsheets` + service account + share только нужных файлов; **Path A (пилот):** OAuth/hosted MCP (we2go, Composio, PasteSheet) — удобно для личного теста, хуже blast radius для финконтура; **не обещать** официальный Marketplace Sheets-плагин: changelog 03.08.2026 его **не** перечисляет (только Drive/Gmail/Calendar).
3. **Подготовить реестр** — одна строка = одна сущность; стабильный `doc_key`; лист `staging` для импорта; в облако без сырых ПДн (ИНН/сумма/статус — да; паспорт, полные ФИО — нет); interlink `/obezlichivanie-dannyh-chatgpt-finansist/`.
4. **Google Cloud + SA** — проект → включить **Google Sheets API** → service account → JSON-ключ → скопировать `client_email` → «Поделиться» на файл реестра с ролью **Редактор** (без «Уведомить»). IAM Cloud **не заменяет** Share файла.
5. **mcp.json в Cursor** — проектно `.cursor/mcp.json` или глобально `~/.cursor/mcp.json`; блок `mcp-gsheets` с `npx -y mcp-gsheets@latest` + `GOOGLE_APPLICATION_CREDENTIALS` (абсолютный путь) + `GOOGLE_PROJECT_ID`; JSON-ключ **не** в git; при совпадении имён побеждает проектный конфиг.
6. **Проверить подключение** — сохранить → перезапуск Cursor / toggle MCP; Customize → MCPs → зелёный статус; Output → **MCP Logs**; tool `sheets_check_access` или живой запрос «прочитай A1:C5 листа Реестр».
7. **Рабочий сценарий реестра** — промпт с DoD: `sheets_get_metadata` → найти строку по `doc_key` → `sheets_update_values` / `sheets_append_values` только в колонки статуса/комментария → `sheets_get_values` на ту же строку → сверка; human approval на каждый write-tool.
8. **Эксплуатация** — allowlist write-tools; ротация ключа SA (B93); при >80–100 заявок/мес или audit — n8n/ERP, Sheets остаётся staging; соседние реестры B51/B58/B83.
9. **Fork от B82** — B82 = свой Python/Node скрипт пишет в staging; B92 = те же SA+share, но правки через Agent+MCP без написания кода.

**Workflow для статьи:**  
`Реестр в Sheets → SA share → mcp-gsheets в Cursor → Agent read/update по doc_key → перечитка диапазона → регламент CFO`

---

## Яндекс Wordstat (MCP user-mcp-kv)

⚠️ **WORDSTAT AUTH WARNING:** сервер MCP `user-mcp-kv` в этой Cloud-сессии **не подключён** (в каталоге dynamic tools: `cursor`, `Cursor Automation Tools`, `cursor-cloud`, `cursor-subscriptions`). Вызов `wordstat_get_top_requests` для `mcp google sheets cursor` и LSI **не выполнен**. Точные показы/мес **не получены** и **не выдуманы**.

Обновление токена / подключение MCP-KV: https://oauth.yandex.ru/authorize?response_type=token&client_id=c654b948515a4a07a4c89648a0831d40

### Таблица спроса (Wordstat)

| Фраза | Показы в месяц |
| --- | --- |
| mcp google sheets cursor | *не получено — MCP недоступен* |
| cursor mcp | *не получено — MCP недоступен* |
| mcp сервер для cursor | *не получено — MCP недоступен* |
| автоматизация финотдела | *не получено — MCP недоступен* |
| google sheets mcp | *не получено — MCP недоступен* |
| подключить mcp cursor | *не получено — MCP недоступен* |
| mcp-gsheets | *не получено — MCP недоступен* |

**Экспертная семантика (LSI для writer, без цифр спроса):**

| Кластер | Фразы | Роль |
| --- | --- | --- |
| Primary | mcp google sheets cursor, google sheets mcp cursor | H1, title |
| Setup | mcp.json cursor, mcp-gsheets service account, npx mcp-gsheets | H2 пошагово |
| Finance | автоматизация финотдела google sheets, реестр договоров cursor, править реестр без копипаста | угол КОДА |
| Registry | реестр upd google sheets, реестр saas подписок, doc_key find update | кейсы |
| Security | service account json не в git, обезличивание sheets, oauth scopes минимум | FAQ |
| Ops | sheets_check_access, mcp logs cursor, 403 share sa | troubleshooting |
| Adjacent | cursor google workspace plugins 2026, mcp cursor finansist | interlink B21; честный note про отсутствие Sheets в changelog |

**SEO-вывод:** SERP по `mcp google sheets cursor` — EN-гайды community MCP (freema, we2go, spreadsheet-mcp) + новости Workspace (август 2026, часто **переоценивают** Sheets). Почти нет RU how-to «финансист + реестр + Cursor + SA». Угол КОДА: правка управленческих реестров через MCP без копипаста, с SA и verify-loop.

---

## SERP (WebSearch Cursor, 08.09.2026)

Приоритет — живой WebSearch/WebFetch; `research-serp.json` от research_start — черновик URL; query `2026 2026` и часть утиных сниппетов **нерелевантны**.

### Primary: `mcp google sheets cursor 2026`

| # | URL | Тип | Пробел для КОДА |
| --- | --- | --- | --- |
| 1 | https://cursor.com/help/customization/mcp | Официальный help | Канон mcp.json/approvals; нет Sheets-кейса |
| 2 | https://cursor.com/docs/mcp | Official reference | Marketplace/one-click; нет реестров |
| 3 | https://github.com/freema/mcp-gsheets | Community MCP (SA) | EN; npm `mcp-gsheets` 1.10.2 |
| 4 | https://www.npmjs.com/package/mcp-gsheets | npm package | Конфиг Cursor; tools list |
| 5 | https://github.com/we2go/google-mcp | npx wizard OAuth/SA | Sheets; не CFO-реестры |
| 6 | https://github.com/dudegladiator/spreadsheet-mcp | Python/uv, 27 tools | Dev-установка |
| 7 | https://github.com/g3na8/google-sheets-mcp | SA + GOOGLE_APPLICATION_CREDENTIALS | Альтернатива Path B |
| 8 | https://designrevision.com/blog/add-mcp-server-to-cursor | How-to MCP 2026 | Общий setup, не Sheets |

### Official Workspace (август 2026) — сверка 08.09.2026

| # | URL | Тип | Что писать в статье |
| --- | --- | --- | --- |
| 1 | https://cursor.com/changelog/google-workspace-plugins | Changelog 03.08.2026 | **Только** Drive, Gmail, Calendar |
| 2 | https://aicatchup.com/news/cursor-google-workspace-plugins | Correction | Убрали ложные Docs/Sheets из разбора changelog |
| 3 | https://pondero.ai/news/2026-08-04-cursor-google-workspace/ | Secondary news | Перечисляет 5 плагинов — **не опираться** без сверки с changelog |
| 4 | https://developers.google.com/workspace/sheets/api/limits | Google quotas | 300 read/write per min/project; Sheets MCP toolset quotas |

### Secondary / finance angle

| # | URL | Тип | Пробел |
| --- | --- | --- | --- |
| 1 | https://koda-fd.ru/blog/ai-dlya-finansista-2026/ | Hub КОДА | Нет MCP Cursor |
| 2 | https://docs.gspread.org/en/latest/oauth2.html | SA share канон | Не Cursor |
| 3 | https://composio.dev/toolkits/googlesheets/framework/cursor | Hosted OAuth | SaaS-посредник |

### Конкурентный зазор (угол КОДА)

1. **Finance-first** — не «подключи Sheets к Cursor», а «перестань копировать реестр: agent правит строку по `doc_key`».
2. **Честный статус Marketplace** — Drive/Gmail/Calendar есть в changelog; cell-edit Sheets → community MCP + SA.
3. **Связка с реестрами серии** — B51/B58/B83; MCP = слой правок поверх уже спроектированной таблицы.
4. **Security** — минимальный share, ключ вне git, approval tools, обезличивание.
5. **Verify loop** — после write всегда `get_values`; Connected ≠ authorized.
6. **Fork от B82** — тот же SA, другой клиент (Agent tools vs скрипт).

---

## Таблица фактов

| # | Утверждение | Источник | Дата проверки |
| --- | --- | --- | --- |
| 1 | MCP подключает Cursor к внешним tools; Agent вызывает их в чате. | https://cursor.com/help/customization/mcp | 2026-09-08 |
| 2 | Конфиг: проектный `.cursor/mcp.json` + глобальный `~/.cursor/mcp.json`; при совпадении имени побеждает **проектный**. | https://cursor.com/help/customization/mcp | 2026-09-08 |
| 3 | Локальный MCP: `command`/`args`/`env`; удалённый — `url` (+ опционально `headers`). | https://cursor.com/help/customization/mcp | 2026-09-08 |
| 4 | One-click: Customize → MCPs → Add to Cursor; после ручного `mcp.json` — **перезапуск Cursor**. | https://cursor.com/help/customization/mcp | 2026-09-08 |
| 5 | По умолчанию Agent **запрашивает approval** перед MCP-tool; Cursor 3.6+ — Auto-review / allowlist / `permissions.json`. | https://cursor.com/help/customization/mcp | 2026-09-08 |
| 6 | Troubleshooting: Output → **MCP Logs** (`Ctrl+Shift+U` / `Cmd+Shift+U`). | https://cursor.com/help/customization/mcp | 2026-09-08 |
| 7 | Cloud Agents поддерживают MCP, настроенные в Cloud Agents dashboard / Team Integrations & MCP — не автоматически копируют локальный OAuth. | https://cursor.com/help/customization/mcp | 2026-09-08 |
| 8 | Changelog 03.08.2026: плагины **Google Drive, Gmail, Google Calendar**; Sheets/Docs в этом документе **не перечислены**. | https://cursor.com/changelog/google-workspace-plugins | 2026-09-08 |
| 9 | Сторонние обзоры, приписывающие changelog «5 плагинов incl. Sheets», требуют сверки; aicatchup снял Docs/Sheets как ошибку атрибуции. | https://aicatchup.com/news/cursor-google-workspace-plugins | 2026-09-08 |
| 10 | `mcp-gsheets` (npm): MIT; Node.js **v20+**; актуальная версия **1.10.2** (обновление 16.08.2026); установка `npx -y mcp-gsheets@latest`. | https://www.npmjs.com/package/mcp-gsheets ; https://github.com/freema/mcp-gsheets | 2026-09-08 |
| 11 | Конфиг Cursor для mcp-gsheets: `GOOGLE_PROJECT_ID` + `GOOGLE_APPLICATION_CREDENTIALS` (абсолютный путь к JSON SA). | https://www.npmjs.com/package/mcp-gsheets | 2026-09-08 |
| 12 | Ключевые tools: `sheets_get_values`, `sheets_update_values`, `sheets_append_values`, `sheets_batch_get_values`, `sheets_get_metadata`, `sheets_check_access`. | https://www.npmjs.com/package/mcp-gsheets | 2026-09-08 |
| 13 | Service account по умолчанию **не видит** таблицы, пока файл не расшарен на `client_email` из JSON (как обычный Google-аккаунт). | https://docs.gspread.org/en/latest/oauth2.html | 2026-09-08 |
| 14 | Scope `https://www.googleapis.com/auth/spreadsheets` — read/write расшаренных таблиц; для create/share файлов часто нужен Drive scope. | https://github.com/theoephraim/node-google-spreadsheet/ ; docs.gspread | 2026-09-08 |
| 15 | Квота Sheets API: **300** read и **300** write запросов/мин на проект; **60**/мин на user/project; превышение → HTTP **429**; batch = 1 запрос. | https://developers.google.com/workspace/sheets/api/limits | 2026-09-08 |
| 16 | Google документирует отдельный Sheets MCP toolset (`get_values`, `update_values`, …) с теми же per-minute квотами — Developer/MCP путь Google, не Cursor Marketplace. | https://developers.google.com/workspace/sheets/api/limits | 2026-09-08 |
| 17 | Превышение quota Sheets API позже в 2026 планируется тарифицировать в Cloud billing (стандартизация agent tools) — следить за политикой Google, не обещать «бесплатно навсегда». | https://developers.google.com/workspace/sheets/api/limits | 2026-09-08 |
| 18 | `we2go/google-mcp`: wizard `npx google-mcp init` (SA или OAuth); tools read/update/append. | https://github.com/we2go/google-mcp | 2026-09-08 |
| 19 | Альтернативы Path B: `dudegladiator/spreadsheet-mcp` (uv, 27 tools), `g3na8/google-sheets-mcp` (Node + SA JSON). | GitHub repos выше | 2026-09-08 |
| 20 | Hosted/Composio: OAuth через посредника; удобно для пилота, данные идут через сторонний коннектор — для финреестров предпочитать self-hosted SA. | https://composio.dev/toolkits/googlesheets/framework/cursor | 2026-09-08 |

**Не выдумывать:** показы Wordstat; «официальный Sheets-плагин всегда в Marketplace» (changelog 03.08.2026 его не содержит); что SA = доступ ко всему Drive; ROI/«56k installs» из обзоров без первички; «без программиста» для Path B без упоминания GCP/SA.

**fact-bank.md:** прямых фактов про MCP+Sheets нет — опираться на таблицу выше. Контент-заводные ROI из fact-bank **не тянуть**.

---

## Структура H2 для writer (из карточки B92)

1. Когда это нужно финотделу (и когда нет)  
2. Подготовка данных и безопасность (без сырых ПДн в облако)  
3. Пошаговая настройка / скрипт / сценарий  
4. Проверка результата и типичные ошибки  
5. Что автоматизировать дальше  

**Пример mcp.json (Path B — writer вставит в статью):**

```json
{
  "mcpServers": {
    "mcp-gsheets": {
      "command": "npx",
      "args": ["-y", "mcp-gsheets@latest"],
      "env": {
        "GOOGLE_PROJECT_ID": "your-project-id",
        "GOOGLE_APPLICATION_CREDENTIALS": "/absolute/path/to/sa-registry.json"
      }
    }
  }
}
```

**Тестовый промпт агента (реестр):**

> Подключись к таблице `{SPREADSHEET_ID}`. На листе `Реестр` найди строку, где колонка `doc_key` = `DOG-2026-014`. Прочитай текущие значения колонок `status` и `comment`. Если `status` ≠ «Оплачен», предложи обновление на «На согласовании» и допиши в `comment` сегодняшнюю дату. После write перечитай ту же строку и покажи diff.

---

## FAQ-кандидаты

- **Можно ли без программиста?** — Path B (SA + mcp.json): по инструкции 1–2 ч, Cursor поможет с JSON; «вообще без GCP» — только hosted/OAuth пилот, не для командного финконтура.
- **Сколько займёт внедрение?** — SA + mcp.json + один тестовый update: **~1–2 ч**.
- **Какие риски для данных?** — SA-ключ = все расшаренные файлы; не класть ПДн; подтверждать write-tools; не коммитить JSON.
- **Есть ли официальный плагин Google Sheets в Cursor?** — На 08.09.2026 changelog Workspace описывает Drive/Gmail/Calendar; cell-edit реестров — community MCP (`mcp-gsheets`) или hosted.
- **OAuth или service account?** — OAuth/hosted для личного пилота; SA для командного реестра и минимального blast radius.
- **Чем отличается от B82?** — B82 = скрипт пишет в staging; B92 = Agent в Cursor правит через MCP без скрипта.
- **Работает ли в Cloud Agents?** — локальный mcp.json/OAuth не переезжает автоматически; для облака — отдельная настройка dashboard MCP или SA.
- **Почему 403 / spreadsheet not found?** — не расшарили `client_email` SA на файл; проверить ID таблицы из URL.

---

## CTA / interlink

- Internal: `/avtomatizaciya-finansov-no-code/`, `/obezlichivanie-dannyh-chatgpt-finansist/`, `/google-sheets-api-integraciya-finotdel/` (B82), `/mcp-cursor-finansist-instrumenty/` (B21)
- Соседние реестры: B51, B58, B83; ротация ключа: B93
- CTA: `https://club.koda-fd.ru/?utm_source=blog&utm_medium=article&utm_campaign=mcp-google-sheets-cursor-reestry` (≤2), `https://t.me/finance_modern?utm_source=blog&utm_medium=article` (≤2)

---

## Handoff marker

`=== EXCALIBUR BLOG RESEARCH ===` — см. `.cursor/excalibur-blog-handoff.md`
