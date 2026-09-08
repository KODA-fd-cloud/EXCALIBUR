# Research notes — B92

**topic_id:** B92  
**slug:** mcp-google-sheets-cursor-reestry  
**h1:** Как подключить MCP к Google Sheets в Cursor и править реестры без копипаста  
**research_date:** 2026-09-08  
**freshness_window:** prefer_sources_after_2026-09-01 (также ок официальные docs/changelog Aug 2026)  
**publish_target:** koda-fd.ru/blog  
**utility_gate:** PASS (`how_to`, mode B) — `utility-gate-topic.json` + `excalibur_blog_utility_gate.py --topic-id B92`  
**author_id:** olga-kondratskaya  
**related_internal:** `/avtomatizaciya-finansov-no-code/`, `/obezlichivanie-dannyh-chatgpt-finansist/`  
**sibling_queue:** B82 (Sheets API + SA), B21 (MCP в Cursor общий), B51/B58/B83 (реестры в Sheets), B93 (ротация SA)  
**cover_scene_hint:** abstract holographic finance automation dark #0a0a0f purple #8b5cf6, no text

---

## utility_verdict

**PASS** — тема utility-only how_to. Читатель получает практический выбор Path A (Marketplace Google Sheets / OAuth, если доступен) vs Path B (`freema/mcp-gsheets` + service account для финконтура), подготовку реестра под агентные правки, тестовый сценарий «найти строку по `doc_key` → обновить статус → перечитать», чеклист безопасности и troubleshooting (OAuth Cloud, MCP Logs, 429, append OVERWRITE). Не новость «Cursor открыл Workspace», не обзор 25 MCP-серверов, не туториал «напиши свой MCP с нуля».

---

## reader_outcome

После гайда финансист сможет подключить MCP Google Sheets в Cursor, дать агенту доступ только к рабочему реестру (через service account или OAuth-плагин), попросить обновить статус строки или дописать поля без копирования таблицы в чат и проверить результат перечиткой диапазона через MCP-tool.

---

## action_outline

1. **Решить, нужен ли MCP Sheets** — реестр уже в Google Sheets (договоры, УПД, SaaS, заявки на расход), правки повторяются, устали таскать диапазоны в чат; **не** делать, если нужен жёсткий audit trail / сотни таблиц с enterprise ACL — тогда 1С/CLM, Sheets только staging.
2. **Выбрать путь подключения** — **Path A (пилот):** плагин `google-sheets` из Cursor Marketplace / Customize → OAuth; **Path B (финконтур):** `freema/mcp-gsheets` + service account — расшарить только нужные реестры, ключ в `env`, без доступа агента ко всему Drive (см. B82, B93).
3. **Подготовить реестр** — одна строка = одна сущность; стабильный `doc_key`; лист `staging` для импорта; в облако без сырых ПДн (ИНН/сумма/статус — да; паспорт, полные ФИО — нет); interlink `/obezlichivanie-dannyh-chatgpt-finansist/`.
4. **Path B: Google Cloud + SA** — проект → включить **Google Sheets API** → service account → JSON-ключ → скопировать `client_email` → «Поделиться» на файл реестра с ролью **Редактор** (без «Уведомить»).
5. **Path B: mcp.json в Cursor** — глобально `~/.cursor/mcp.json` или проектно `.cursor/mcp.json`; блок `mcp-gsheets` с `npx -y mcp-gsheets@latest` и `GOOGLE_APPLICATION_CREDENTIALS` (абсолютный путь); JSON-ключ **не** в git.
6. **Path A: Marketplace** — Customize → MCPs → `google-sheets` → Add → OAuth; минимальные scopes; честно предупредить: в **официальном changelog 03.08.2026** детально расписаны Drive/Gmail/Calendar, а Sheets подтверждается Marketplace/форумом с известными OAuth-багами Cloud (см. факты).
7. **Проверить подключение** — перезапуск Cursor; Customize → MCPs → зелёный статус; Output → **MCP Logs**; tool `sheets_check_access` (Path B) или живой запрос «прочитай A1:C5 листа Реестр».
8. **Рабочий сценарий реестра** — промпт с DoD: `sheets_get_metadata` → найти строку по `doc_key` → `sheets_update_values` / `sheets_append_values` только в колонки статуса/комментария → `sheets_get_values` на ту же строку → сверка; human approval на каждый write-tool.
9. **Эксплуатация и рост** — allowlist write-tools; ротация ключа SA (B93); при >80–100 заявок/мес или audit — n8n/ERP, Sheets остаётся staging; соседние реестры B51/B58/B83.

**Workflow для статьи:**  
`Реестр в Sheets → (SA share | OAuth plugin) → MCP в Cursor → Agent read/update по doc_key → перечитка диапазона → регламент CFO`

---

## Яндекс Wordstat (MCP user-mcp-kv)

⚠️ **WORDSTAT AUTH WARNING:** сервер MCP `user-mcp-kv` в этой Cloud-сессии **не подключён** (`CallDynamicTool` → `MCP server does not exist: user-mcp-kv. No MCP servers available`). Вызов `wordstat_get_top_requests` **не выполнен**. Точные показы/мес **не получены** и **не выдуманы**.

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

**Экспертная семантика (LSI для writer, без цифр спроса):**

| Кластер | Фразы | Роль |
| --- | --- | --- |
| Primary | mcp google sheets cursor, google sheets mcp cursor | H1, title |
| Setup | mcp.json cursor, cursor marketplace google sheets, mcp-gsheets service account | H2 пошагово |
| Finance | автоматизация финотдела google sheets, реестр договоров cursor, править реестр без копипаста | угол КОДА |
| Registry | реестр upd google sheets, реестр saas подписок, doc_key find update | кейсы |
| Security | service account json не в git, обезличивание sheets, oauth scopes минимум | FAQ |
| Ops | sheets_check_access, mcp logs cursor, unauthorized google mcp, update_values serialization | troubleshooting |
| Adjacent | cursor google workspace plugins 2026, mcp cursor finansist | interlink B21 |

**SEO-вывод:** SERP по `mcp google sheets cursor` — **EN how-to community MCP** (freema, we2go, spreadsheet-mcp, g-sheet-mcp) + **новости Cursor Workspace (авг 2026)** + баг-репорты форума. RU how-to «финансист + реестр + Cursor MCP» почти нет → угол КОДА свободен.

---

## SERP (WebSearch Cursor, 08.09.2026)

Приоритет — живой WebSearch + WebFetch официальных URL. `research-serp.json` (шаг 0) — черновик; query `2026 2026` нерелевантен — игнорировать.

### Primary: `mcp google sheets cursor 2026`

| # | URL | Тип | Пробел для КОДА |
| --- | --- | --- | --- |
| 1 | https://cursor.com/docs/mcp | Офиц. reference MCP | Нет реестров финотдела |
| 2 | https://cursor.com/help/customization/mcp | Help: mcp.json, OAuth, approvals, Cloud Agents | Канон шагов; нет Sheets-кейса |
| 3 | https://github.com/freema/mcp-gsheets | Community MCP (SA) | EN; dev-фокус, не CFO |
| 4 | https://github.com/we2go/google-mcp | npx wizard OAuth/SA | Sheets+Docs; не реестры |
| 5 | https://github.com/dudegladiator/spreadsheet-mcp | Python/uv, 27 tools | Установка для dev |
| 6 | https://github.com/mariadb-RupeshBiswas/google-sheets-mcp | Read-only ADC (`g-sheet-mcp`) | Нет write для статусов |
| 7 | https://composio.dev/toolkits/googlesheets | Hosted Composio (обновл. 28.08.2026) | SaaS-посредник |
| 8 | https://agenticmarket.dev/blog/mcp-server-not-working | Troubleshooting MCP (март 2026) | Общий, не finance |

### Official / Workspace (перепроверено 08.09.2026)

| # | URL | Тип | Пробел |
| --- | --- | --- | --- |
| 1 | https://cursor.com/changelog/google-workspace-plugins | Changelog 03.08.2026 | В теле **только** Drive, Gmail, Calendar |
| 2 | https://forum.cursor.com/t/google-sheet-authentication-is-broken-atm-critical/167413 | Forum 04.08.2026 | Sheets **есть** в Marketplace; OAuth Cloud broken |
| 3 | https://forum.cursor.com/t/google-workspace-plugins-oauth-fails-error-400-invalid-request-on-cursor-redirect/167402 | Forum | `cursor://` redirect rejected; workaround cursor.com/agents |
| 4 | https://forum.cursor.com/t/bug-google-sheets-mcp-update-values-fails-with-serialization-error-nested-arrays-converted-to-strings/169687 | Forum | баг `update_values` serialization |
| 5 | https://developers.google.com/workspace/sheets/api/limits | Google Sheets API + **Sheets MCP quotas** | Офиц. лимиты 300/60; toolset sheetsmcp |
| 6 | https://aicatchup.com/news/cursor-google-workspace-plugins | Коррекция медиа | Docs/Sheets **не** в changelog |

### Secondary: автоматизация финотдела / реестры Sheets

| # | URL | Тип | Пробел |
| --- | --- | --- | --- |
| 1 | https://dzen.ru/a/anRW32ni3D3wHjQF | Реестр договоров Sheets | Без MCP |
| 2 | https://dzen.ru/a/aoAx4V_t_ztBh5aj | Forms→реестр заявок | Без MCP; порог 80–100/мес |
| 3 | https://alpray.com/finance-approval-workflow-google-sheets-apps-script.html | Approval workflow Apps Script (05.06.2026) | Без Cursor |
| 4 | https://koda-fd.ru/blog/ai-dlya-finansista-2026/ | Hub КОДА | Нет MCP Sheets |

### Конкурентный зазор (угол КОДА)

1. **Finance-first** — не «подключи Sheets к Cursor», а «перестань копировать реестр в чат: agent правит строку по `doc_key`».
2. **Два пути с честным статусом на 08.09.2026** — OAuth-плагин для пилота (есть в Marketplace, но Cloud OAuth/serialization баги) vs SA+mcp-gsheets для production финконтура.
3. **Связка с реестрами серии** — договоры (B51), УПД (B58), SaaS (B83); MCP = слой правок поверх уже спроектированной таблицы.
4. **Security** — минимальный share, ключ вне git, approval tools, indirect prompt injection, обезличивание.
5. **Verify loop** — после write всегда `get_values`; «Connected ≠ authorized».
6. **Fork от B82** — B82 = свой Python-скрипт; B92 = те же SA+share, но правки через Agent+MCP без написания кода.

---

## Таблица фактов

| # | Утверждение | Источник | Дата проверки |
| --- | --- | --- | --- |
| 1 | MCP подключает Cursor к внешним инструментам; Agent вызывает tools в чате; транспорты: stdio / SSE / Streamable HTTP. | https://cursor.com/docs/mcp | 2026-09-08 |
| 2 | Конфиг: проектный `.cursor/mcp.json` + глобальный `~/.cursor/mcp.json`; при совпадении имени побеждает **проектный**. | https://cursor.com/help/customization/mcp | 2026-09-08 |
| 3 | Локальный MCP: `command`/`args`/`env`; удалённый — `url` (+ `headers` / static `auth`). После ручного `mcp.json` — **перезапуск Cursor**. | https://cursor.com/help/customization/mcp | 2026-09-08 |
| 4 | One-click: Customize → MCPs → Add to Cursor; Marketplace / cursor.directory. | https://cursor.com/docs/mcp | 2026-09-08 |
| 5 | По умолчанию Agent **запрашивает approval** перед MCP-tool; Cursor 3.6+ — Auto-review / allowlist / `permissions.json`. | https://cursor.com/help/customization/mcp | 2026-09-08 |
| 6 | Troubleshooting: Output → **MCP Logs** (`Ctrl+Shift+U` / `Cmd+Shift+U`). | https://cursor.com/help/customization/mcp | 2026-09-08 |
| 7 | Cloud Agents поддерживают MCP из Cloud Agents dashboard / Team Integrations & MCP. | https://cursor.com/help/customization/mcp | 2026-09-08 |
| 8 | Changelog 03.08.2026: официально детализированы **Google Drive, Gmail, Google Calendar** (Marketplace / Customize). | https://cursor.com/changelog/google-workspace-plugins | 2026-09-08 |
| 9 | Плагин **Google Sheets** присутствует в Marketplace (форум Cursor, авг 2026); OAuth Cloud часто падает с Error 400 `invalid_request` на `cursor://` callback. | https://forum.cursor.com/t/google-sheet-authentication-is-broken-atm-critical/167413 | 2026-09-08 |
| 10 | Workaround Cloud OAuth: авторизоваться через https://cursor.com/agents (MCP Servers → Login), не через in-app Authenticate; Local auth обычно работает. | https://forum.cursor.com/t/google-workspace-plugins-oauth-fails-error-400-invalid-request-on-cursor-redirect/167402 | 2026-09-08 |
| 11 | Известный баг: MCP tool `update_values` может сериализовать 2D-массив в строки → Google API 400; обход — retry / явная инструкция «JSON array of arrays». | https://forum.cursor.com/t/bug-google-sheets-mcp-update-values-fails-with-serialization-error-nested-arrays-converted-to-strings/169687 | 2026-09-08 |
| 12 | `freema/mcp-gsheets`: Node.js **v20+**, Sheets API, service account JSON; Cursor: `npx -y mcp-gsheets@latest` + `GOOGLE_PROJECT_ID` + `GOOGLE_APPLICATION_CREDENTIALS`. | https://github.com/freema/mcp-gsheets | 2026-09-08 |
| 13 | Ключевые tools Path B для реестра: `sheets_get_values`, `sheets_update_values`, `sheets_append_values`, `sheets_batch_get_values`, `sheets_get_metadata`, `sheets_check_access`. | https://github.com/freema/mcp-gsheets | 2026-09-08 |
| 14 | `sheets_append_values`: default `insertDataOption` = **OVERWRITE** — для реестра явно `INSERT_ROWS`, если нужно сдвигать строки. | https://github.com/freema/mcp-gsheets | 2026-09-08 |
| 15 | Альтернативы auth: `GOOGLE_SERVICE_ACCOUNT_KEY` (JSON-строка) или `GOOGLE_PRIVATE_KEY` + `GOOGLE_CLIENT_EMAIL`. | https://vibehackers.io/mcp/mcp-gsheets | 2026-09-08 |
| 16 | Scope `https://www.googleapis.com/auth/spreadsheets` — sensitive, read/write всех доступных таблиц; scope применяется ко **всему файлу**; листы защищают ProtectedRange. Рекомендуемый узкий Drive-scope: `drive.file`. | https://developers.google.com/workspace/sheets/api/scopes | 2026-09-08 |
| 17 | Квота Sheets API: **300 read/write req/min** на проект; **60**/min на user/project; превышение → HTTP **429**; batch = 1 запрос. | https://developers.google.com/workspace/sheets/api/limits | 2026-09-08 |
| 18 | У Google есть официальный **Sheets MCP** toolset (`sheetsmcp.googleapis.com`): `get_values`, `get_spreadsheet`, `update_spreadsheet`, `update_values`, `update_formulas`, `insert_dimension` — те же квоты 300/60. | https://developers.google.com/workspace/sheets/api/limits | 2026-09-08 |
| 19 | Планируется: превышение quota limits Sheets API → биллинг Google Cloud **later in 2026** (standardized model for agent tools). | https://developers.google.com/workspace/sheets/api/limits | 2026-09-08 |
| 20 | Service account видит **только** таблицы, расшаренные на `client_email`; IAM Cloud **не заменяет** Share файла. | https://developers.google.com/workspace/guides/create-credentials#service-account | 2026-09-08 |
| 21 | `we2go/google-mcp`: `npx google-sheet-mcp` / `init` wizard SA или OAuth; tools read/update/append. | https://github.com/we2go/google-mcp | 2026-09-08 |
| 22 | Read-only вариант: `uvx g-sheet-mcp` (ADC) — подходит для аудита без write. | https://github.com/mariadb-RupeshBiswas/google-sheets-mcp | 2026-09-08 |
| 23 | Реестр договоров в Sheets уместен до **200–300** активных договоров при одном владельце; иначе CLM/1С. | https://dzen.ru/a/anRW32ni3D3wHjQF | 2026-09-08 |
| 24 | Заявки на расход Forms→Sheets: при **>80–100** заявок/мес Sheets — staging перед ERP/n8n. | https://dzen.ru/a/aoAx4V_t_ztBh5aj | 2026-09-08 |
| 25 | Cursor MCP config key = `mcpServers` (не VS Code `servers`) — неверный ключ молча ломает подключение. | https://agenticmarket.dev/blog/mcp-server-not-working | 2026-09-08 |

**Не выдумывать:** показы Wordstat; что Sheets детально описан в официальном changelog (нет — только Drive/Gmail/Calendar); что SA = доступ ко всему Drive; ROI/цифры content-завода из fact-bank; обещание «без программиста» для Path B без GCP/SA.

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

> Подключись к таблице `{SPREADSHEET_ID}`. На листе `Реестр` найди строку, где колонка `doc_key` = `DOG-2026-014`. Прочитай текущие значения колонок `status` и `comment`. Если `status` ≠ «Оплачен», предложи обновление на «На согласовании» и допиши в `comment` сегодняшнюю дату. После write перечитай ту же строку и покажи diff. Параметр `values` передавай как JSON-массив массивов, не как строку.

---

## FAQ-кандидаты (из карточки)

- **Можно ли без программиста?** — Path A (Marketplace+OAuth): да для пилота при живом плагине; Path B (SA+mcp.json): по инструкции, Cursor поможет с JSON; production — 1–2 ч первый реестр.
- **Сколько займёт внедрение?** — SA + mcp.json + один тестовый update: **~1–2 ч**; OAuth-плагин быстрее, если auth проходит.
- **Какие риски для данных?** — OAuth = права вашего Google; SA-ключ = все расшаренные файлы; не класть ПДн; подтверждать write-tools; indirect injection из ячеек/писем.
- **OAuth или service account?** — OAuth для личного пилота; SA для командного реестра, минимального blast radius, Cloud Agents без интерактивного OAuth.
- **Чем отличается от B82?** — B82 = Python/Node скрипт пишет в staging; B92 = Agent в Cursor правит через MCP без скрипта.
- **Работает ли в Cloud Agents?** — локальный OAuth Desktop ≠ Cloud; Cloud OAuth через cursor.com/agents или SA в Team MCP.

---

## CTA / interlink

- Internal: `/avtomatizaciya-finansov-no-code/`, `/obezlichivanie-dannyh-chatgpt-finansist/`, `/google-sheets-api-integraciya-finotdel/` (B82), `/mcp-cursor-finansist-instrumenty/` (B21)
- Соседние реестры: B51, B58, B83; ротация ключа: B93
- CTA: `https://club.koda-fd.ru/?utm_source=blog&utm_medium=article&utm_campaign=mcp-google-sheets-cursor-reestry` (≤2), `https://t.me/finance_modern?utm_source=blog&utm_medium=article` (≤2)

---

## Handoff marker

`=== EXCALIBUR BLOG RESEARCH ===` — см. `.cursor/excalibur-blog-handoff.md`
