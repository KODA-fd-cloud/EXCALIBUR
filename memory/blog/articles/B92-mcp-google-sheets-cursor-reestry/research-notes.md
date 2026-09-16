# Research notes — B92

**topic_id:** B92  
**slug:** mcp-google-sheets-cursor-reestry  
**h1:** Как подключить MCP к Google Sheets в Cursor и править реестры без копипаста  
**research_date:** 2026-09-16  
**publish_target:** koda-fd.ru/blog  
**utility_gate:** PASS (`how_to`, mode B)  
**author_id:** olga-kondratskaya  
**related_internal:** `/avtomatizaciya-finansov-no-code/`, `/obezlichivanie-dannyh-chatgpt-finansist/`  
**sibling_queue:** B82 (Sheets API + SA), B21 (MCP в Cursor общий), B51/B58/B83 (реестры в Sheets), B93 (ротация SA)  
**cover_scene_hint:** abstract holographic finance automation dark #0a0a0f purple #8b5cf6, no text

---

## utility_verdict

**PASS** — тема utility-only how_to. Читатель получает выбор маршрута подключения Google Sheets к Cursor через MCP (рекомендуемый **Path A: `freema/mcp-gsheets` + service account** для финконтура; опциональный **Path B: официальный remote Sheets MCP Google** `https://sheetsmcp.googleapis.com/mcp/v1` в Developer Preview; честный note, что **Cursor Marketplace Sheets/Docs плагины сняты** с витрины), подготовку реестра под агентные правки, сценарий «найти строку по `doc_key` → обновить статус → перечитать», чеклист безопасности и troubleshooting. Не новость «Cursor открыл Workspace», не обзор 25 MCP-серверов, не туториал «напиши свой MCP с нуля».

---

## reader_outcome

После гайда финансист сможет подключить MCP Google Sheets в Cursor (через SA + `mcp-gsheets` или через официальный remote MCP Google при доступе к Preview), дать агенту доступ только к рабочему реестру, попросить обновить статус строки или дописать поля без копирования таблицы в чат и проверить результат перечиткой диапазона через MCP-tool.

---

## action_outline

1. **Решить, нужен ли MCP Sheets** — реестр уже в Google Sheets (договоры, УПД, SaaS, заявки на расход), правки повторяются, устали таскать диапазоны в чат; **не** делать, если нужен жёсткий audit trail / сотни таблиц с enterprise ACL — тогда 1С/CLM, Sheets только staging.
2. **Выбрать путь подключения (на 16.09.2026)** — **Path A (финконтур, рекомендуем):** `freema/mcp-gsheets` + service account — расшарить только нужные реестры, ключ в `env`, без доступа агента ко всему Drive (см. B82, B93). **Path B (pilot/OAuth):** официальный remote MCP Google `sheetsmcp.googleapis.com` (Developer Preview) — OAuth пользователя, наследует права Google-аккаунта. **Не ждать** Cursor Marketplace Sheets: Drive/Gmail/Calendar есть, Sheets/Docs **сняты** с витрины (форум Cursor, 31.08.2026).
3. **Подготовить реестр** — одна строка = одна сущность; стабильный `doc_key`; лист `staging` для импорта; в облако без сырых ПДн (ИНН/сумма/статус — да; паспорт, полные ФИО — нет); interlink `/obezlichivanie-dannyh-chatgpt-finansist/`.
4. **Path A: Google Cloud + SA** — проект → включить **Google Sheets API** → service account → JSON-ключ → скопировать `client_email` → «Поделиться» на файл реестра с ролью **Редактор** (без «Уведомить»).
5. **Path A: mcp.json в Cursor** — глобально `~/.cursor/mcp.json` или проектно `.cursor/mcp.json`; блок `mcp-gsheets` с `npx -y mcp-gsheets@latest` и `GOOGLE_APPLICATION_CREDENTIALS` (абсолютный путь); JSON-ключ **не** в git; Node.js **v20+**.
6. **Path B (если Preview доступен):** Cloud project → enable `sheets.googleapis.com` + `sheetsmcp.googleapis.com` → OAuth consent + scopes → remote MCP URL `https://sheetsmcp.googleapis.com/mcp/v1` (transport Streamable HTTP) в клиенте с поддержкой remote/`url`; tools: `get_values`, `update_values`, `get_spreadsheet`, `update_spreadsheet`, `update_formulas`, `insert_dimension`.
7. **Проверить подключение** — перезапуск Cursor; Customize → MCPs → зелёный статус; Output → **MCP Logs**; Path A: `sheets_check_access` или «прочитай A1:C5 листа Реестр»; Path B: тестовый prompt из доки Google.
8. **Рабочий сценарий реестра** — промпт с DoD: metadata/get → найти строку по `doc_key` → update/append только колонки статуса/комментария → get_values на ту же строку → сверка; human approval на каждый write-tool; не полагаться на Drive-плагин для записи ячеек.
9. **Эксплуатация и рост** — allowlist write-tools; ротация ключа SA (B93); квоты Sheets/MCP 300 read/write per min per project; при >80–100 заявок/мес или audit — n8n/ERP, Sheets остаётся staging; соседние реестры B51/B58/B83.

**Workflow для статьи:**  
`Реестр в Sheets → (SA share | Google remote MCP OAuth) → MCP в Cursor → Agent read/update по doc_key → перечитка диапазона → регламент CFO`

---

## Яндекс Wordstat (MCP user-mcp-kv)

⚠️ **WORDSTAT AUTH WARNING:** сервер MCP `user-mcp-kv` в этой Cloud-сессии **не подключён** (в каталоге dynamic tools: `cursor`, `Cursor Automation Tools`, `cursor-cloud`, `cursor-subscriptions`). Вызов `wordstat_get_top_requests` **не выполнен** (не 401, а отсутствие namespace). Точные показы/мес **не получены** и **не выдуманы**.

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
| Setup | mcp.json cursor, mcp-gsheets service account, sheetsmcp.googleapis.com | H2 пошагово |
| Finance | автоматизация финотдела google sheets, реестр договоров cursor, править реестр без копипаста | угол КОДА |
| Registry | реестр upd google sheets, реестр saas подписок, doc_key find update | кейсы |
| Security | service account json не в git, обезличивание sheets, oauth scopes минимум, indirect prompt injection | FAQ |
| Ops | sheets_check_access, mcp logs cursor, marketplace sheets сняли | troubleshooting |
| Adjacent | cursor google workspace plugins 2026, mcp cursor finansist | interlink B21 |

**SEO-вывод:** живой WebSearch 16.09.2026 по `mcp google sheets cursor` — **официальная дока Google Sheets MCP** (сент. 2026), **EN community MCP** (freema, dudegladiator, we2go) и **Cursor MCP help**. Почти нет RU how-to «финансист + реестр + Cursor». Угол КОДА: **правка управленческих реестров через MCP без копипаста**, с веткой SA для безопасности и сравнением с B82 (скрипт) / B21 (общий MCP).

---

## SERP (WebSearch Cursor, 16.09.2026)

Приоритет — живой WebSearch. `research-serp.json` от шага 0 **пуст** (SSL handshake timeout на все queries) — **игнорируем** как источник конкурентов.

### Primary: `mcp google sheets cursor 2026`

| # | URL | Тип | Пробел для КОДА |
| --- | --- | --- | --- |
| 1 | https://developers.google.com/workspace/sheets/api/guides/configure-mcp-server | Official Google Sheets remote MCP (Developer Preview) | Клиенты Antigravity/Claude; Cursor = «Others» remote URL; нет реестров финотдела |
| 2 | https://developers.google.com/workspace/guides/configure-mcp-servers | Official Google Workspace MCP family | Общий enable `sheetsmcp.googleapis.com` |
| 3 | https://cursor.com/docs/mcp | Официальный Cursor MCP reference | Нет Sheets-кейса |
| 4 | https://cursor.com/help/customization/mcp | Help: mcp.json, OAuth, approvals, Cloud Agents | Канон шагов Cursor |
| 5 | https://github.com/freema/mcp-gsheets | Community MCP (SA), npm `mcp-gsheets` | EN; Node 20+; не CFO |
| 6 | https://llmversus.com/mcp/google-sheets-mcp | Install guide `mcp-google-sheets` (апр. 2026) | Dev setup; не реестры |
| 7 | https://github.com/dudegladiator/spreadsheet-mcp | Python/uv, 27 tools | Установка для dev |
| 8 | https://composio.dev/toolkits/googlesheets/framework/cursor | Composio OAuth-посредник | SaaS middleman |

### News / Marketplace status (авг–сент 2026)

| # | URL | Тип | Пробел |
| --- | --- | --- | --- |
| 1 | https://cursor.com/changelog/google-workspace-plugins | Changelog 03.08.2026 | Только Drive, Gmail, Calendar |
| 2 | https://aicatchup.com/news/cursor-google-workspace-plugins | Коррекция: Docs/Sheets **не** в changelog | Честный status |
| 3 | https://forum.cursor.com/t/grok-bot-drive-mcp-should-write-google-docs-body-and-sheet-cells-not-only-file-metadata/169971 | Staff: Sheets/Docs connectors **pulled** (31.08.2026) | Drive ≠ cell write |
| 4 | https://developers.google.com/workspace/sheets/api/limits | Quotas + Sheets MCP tool costs | Обновлено 03.09.2026 |

### Secondary: `автоматизация финотдела` / реестры Sheets

| # | URL | Тип | Пробел |
| --- | --- | --- | --- |
| 1 | https://dzen.ru/a/aoV6BGni3D3wS-su | Sheets API + SA (КОДА/Дзен) | Без MCP Cursor |
| 2 | https://dzen.ru/a/anRW32ni3D3wHjQF | Реестр договоров Sheets | Без MCP |
| 3 | https://monuchet.ru/spravochnik/dds-dlya-sobstvennika-na-1-liste/ | ДДС в Sheets | Не Cursor |
| 4 | https://pohodu.media/kak-ja-perestal-vruchnuju-zapolnjat-tablicu-dds/ | Make → Sheets ДДС | No-code, не MCP |
| 5 | https://github.com/we2go/google-mcp/blob/main/docs/quickstart-ru.md | RU quickstart SA+wizard | Dev, не finance angle |

### H1-aligned RU

| # | URL | Заметка |
| --- | --- | --- |
| 1 | https://mcp-catalog.ru/servers/gsheets | RU карточка freema/mcp-gsheets |
| 2 | https://cursor.com/ru/help/customization/mcp | RU help MCP |
| 3 | https://mcpservers.org/ru/servers/dudegladiator/spreadsheet-mcp | RU mirror spreadsheet-mcp |

### Конкурентный зазор (угол КОДА)

1. **Finance-first** — не «подключи Sheets к Cursor», а «перестань копировать реестр в чат: agent правит строку по `doc_key`».
2. **Два рабочих пути + честный статус Marketplace** — SA+mcp-gsheets для production; Google remote MCP Preview для OAuth-пилота; Marketplace Sheets **не обещать**.
3. **Связка с реестрами серии** — договоры (B51), УПД (B58), SaaS (B83); MCP = слой правок поверх уже спроектированной таблицы.
4. **Security block** — минимальный share, ключ вне git, approval tools, indirect prompt injection (Google docs + MCP), обезличивание.
5. **Verify loop** — после write всегда get_values; Drive-плагин **не** пишет ячейки.
6. **Fork от B82** — B82 = свой Python-скрипт; B92 = те же SA+share, но правки через Agent+MCP без написания кода.

---

## Таблица фактов

| # | Утверждение | Источник | Дата проверки |
| --- | --- | --- | --- |
| 1 | MCP подключает Cursor к внешним инструментам; Agent вызывает tools в чате. | https://cursor.com/help/customization/mcp | 2026-09-16 |
| 2 | Конфиг: проектный `.cursor/mcp.json` + глобальный `~/.cursor/mcp.json`; при совпадении имени побеждает **проектный**. | https://cursor.com/help/customization/mcp | 2026-09-16 |
| 3 | Локальный MCP: `command`/`args`/`env`; удалённый — поле `url` (+ опционально `headers`). | https://cursor.com/help/customization/mcp | 2026-09-16 |
| 4 | One-click: Customize → MCPs → Add to Cursor; после ручного `mcp.json` — **перезапуск Cursor**. | https://cursor.com/help/customization/mcp | 2026-09-16 |
| 5 | По умолчанию Agent **запрашивает approval** перед MCP-tool; с Cursor 3.6+ — Auto-review / allowlist / `permissions.json`. | https://cursor.com/help/customization/mcp | 2026-09-16 |
| 6 | Troubleshooting: Output → **MCP Logs** (`Ctrl+Shift+U` / `Cmd+Shift+U`). | https://cursor.com/help/customization/mcp | 2026-09-16 |
| 7 | Cloud Agents поддерживают MCP, настроенные в Cloud Agents dashboard; на Team — shared servers в Dashboard → Integrations & MCP. | https://cursor.com/help/customization/mcp | 2026-09-16 |
| 8 | 03.08.2026 Cursor анонсировал Workspace plugins: **Drive, Gmail, Calendar** (не Sheets/Docs в changelog). | https://cursor.com/changelog/google-workspace-plugins | 2026-09-16 |
| 9 | Staff Cursor (31.08.2026): Google Docs и Google Sheets connectors были кратко доступны в начале августа, затем **сняты** «пока дорабатываем»; вернуть «скоро» — без даты. | https://forum.cursor.com/t/grok-bot-drive-mcp-should-write-google-docs-body-and-sheet-cells-not-only-file-metadata/169971 | 2026-09-16 |
| 10 | Drive connector не пишет тело Docs / ячейки Sheets — только file-level операции. | тот же forum thread | 2026-09-16 |
| 11 | Google Sheets remote MCP: URL `https://sheetsmcp.googleapis.com/mcp/v1`, статус **Developer Preview**, last updated **2026-09-14**. | https://developers.google.com/workspace/sheets/api/guides/configure-mcp-server | 2026-09-16 |
| 12 | Для Google Sheets MCP нужно enable: `sheets.googleapis.com` + `sheetsmcp.googleapis.com`. | там же | 2026-09-16 |
| 13 | OAuth scopes для Sheets MCP: `drive.readonly`, `drive.file`, `spreadsheets.readonly`, `spreadsheets`. | там же | 2026-09-16 |
| 14 | Tools официального Sheets MCP: `get_values`, `get_spreadsheet`, `update_spreadsheet`, `update_values`, `update_formulas`, `insert_dimension`. | там же | 2026-09-16 |
| 15 | Google предупреждает об **indirect prompt injection** при MCP + Sheets; рекомендует human review actions / Model Armor. | там же | 2026-09-16 |
| 16 | Квоты Sheets API / Sheets MCP: **300** read и **300** write req/min на проект; **60**/min на user+project; превышение → HTTP **429**. | https://developers.google.com/workspace/sheets/api/limits | 2026-09-16 |
| 17 | Каждый tool Sheets MCP стоит 1 read или 1 write request (см. таблицу toolset quotas). | там же (обновлено 2026-09-03) | 2026-09-16 |
| 18 | Позже в **2026** превышение quota Sheets API планируется тарифицировать (standardized model for agent tools). | там же | 2026-09-16 |
| 19 | `freema/mcp-gsheets`: Node.js **v20+**, SA JSON, `npx -y mcp-gsheets@latest`, env `GOOGLE_PROJECT_ID` + `GOOGLE_APPLICATION_CREDENTIALS`. | https://github.com/freema/mcp-gsheets | 2026-09-16 |
| 20 | Ключевые tools mcp-gsheets: `sheets_get_values`, `sheets_update_values`, `sheets_append_values`, `sheets_batch_get_values`, `sheets_get_metadata`, `sheets_check_access`. | https://github.com/freema/mcp-gsheets | 2026-09-16 |
| 21 | `sheets_append_values`: default `insertDataOption` = **OVERWRITE** — для реестра явно `INSERT_ROWS`. | https://github.com/freema/mcp-gsheets | 2026-09-16 |
| 22 | Service account видит **только** таблицы, расшаренные на `client_email`; IAM Cloud **не заменяет** Share файла. | https://developers.google.com/workspace/guides/create-credentials#service-account ; https://dzen.ru/a/aoV6BGni3D3wS-su | 2026-09-16 |
| 23 | Scope `https://www.googleapis.com/auth/spreadsheets` — read/write всех расшаренных таблиц SA; лист-level ACL через ProtectedRange. | https://developers.google.com/workspace/sheets/api/scopes | 2026-09-16 |
| 24 | `dudegladiator/spreadsheet-mcp`: **27 tools**, auth через service-account JSON. | https://github.com/dudegladiator/spreadsheet-mcp | 2026-09-16 |
| 25 | Реестр договоров в Sheets уместен до **200–300** активных договоров при одном владельце таблицы; иначе CLM/1С. | https://dzen.ru/a/anRW32ni3D3wHjQF | 2026-09-16 |
| 26 | Sheets API для финотдела — transport в staging, не замена главной книги 1С. | https://dzen.ru/a/aoV6BGni3D3wS-su | 2026-09-16 |

**Не выдумывать:** показы Wordstat; «Sheets-плагин всегда в Marketplace»; что SA = доступ ко всему Drive; что Google remote MCP «уже стабилен для всех» (это Developer Preview); обещание «без программиста» для Path A без упоминания GCP/SA.

**fact-bank.md:** прямых фактов про MCP+Sheets нет — опираться на таблицу выше. Контент-заводные ROI из fact-bank **не тянуть**.

**research-serp.json:** все queries 16.09.2026 упали по SSL timeout — SERP-факты только из WebSearch/WebFetch.

---

## Структура H2 для writer (из карточки B92)

1. Когда это нужно финотделу (и когда нет)  
2. Подготовка данных и безопасность (без сырых ПДн в облако)  
3. Пошаговая настройка / скрипт / сценарий  
4. Проверка результата и типичные ошибки  
5. Что автоматизировать дальше  

**Пример mcp.json (Path A — writer вставит в статью):**

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

**Path B (remote Google, если клиент поддерживает url/oauth — сверять с Cursor help на дату публикации):**

- Server URL: `https://sheetsmcp.googleapis.com/mcp/v1`
- Transport: Streamable HTTP
- Auth: OAuth 2.0 (scopes из факта #13)

**Тестовый промпт агента (реестр):**

> Подключись к таблице `{SPREADSHEET_ID}`. На листе `Реестр` найди строку, где колонка `doc_key` = `DOG-2026-014`. Прочитай текущие значения колонок `status` и `comment`. Если `status` ≠ «Оплачен», предложи обновление на «На согласовании» и допиши в `comment` сегодняшнюю дату. После write перечитай ту же строку и покажи diff.

---

## FAQ-кандидаты (из карточки)

- **Можно ли без программиста?** — Path A (SA+mcp.json): по инструкции B82/B92, Cursor поможет с JSON; production — 1–2 ч первый реестр. Path B (Google remote Preview): нужен Cloud project + OAuth. Marketplace Sheets — пока недоступен.
- **Сколько займёт внедрение?** — SA + mcp.json + один тестовый update: **~1–2 ч**; OAuth remote MCP — дольше из‑за Preview/consent.
- **Какие риски для данных?** — OAuth = права вашего Google; SA-ключ = все расшаренные файлы; не класть ПДн; подтверждать write-tools; indirect injection из ячеек/писем.
- **OAuth или service account?** — OAuth (Path B / личный пилот); SA (Path A) для командного реестра, cron, минимального blast radius.
- **Чем отличается от B82?** — B82 = Python/Node скрипт пишет в staging; B92 = Agent в Cursor правит через MCP без скрипта.
- **Работает ли в Cloud Agents?** — да, через MCP в Cloud Agents dashboard (Team shared servers); локальный интерактивный OAuth локальной IDE сам по себе не «переезжает» — проверять отдельно или использовать SA.

---

## CTA / interlink

- Internal: `/avtomatizaciya-finansov-no-code/`, `/obezlichivanie-dannyh-chatgpt-finansist/`, `/google-sheets-api-integraciya-finotdel/` (B82), `/mcp-cursor-finansist-instrumenty/` (B21)
- Соседние реестры: B51, B58, B83; ротация ключа B93
- CTA: `https://club.koda-fd.ru/?utm_source=blog&utm_medium=article&utm_campaign=mcp-google-sheets-cursor-reestry` (≤2), `https://t.me/finance_modern?utm_source=blog&utm_medium=article` (≤2)

---

## Handoff marker

`=== EXCALIBUR BLOG RESEARCH ===` — см. `.cursor/excalibur-blog-handoff.md`
