# Research notes — B92

**topic_id:** B92  
**slug:** mcp-google-sheets-cursor-reestry  
**h1:** Как подключить MCP к Google Sheets в Cursor и править реестры без копипаста  
**research_date:** 2026-09-07  
**publish_target:** koda-fd.ru/blog  
**utility_gate:** PASS (`how_to`, mode B)  
**author_id:** olga-kondratskaya  
**related_internal:** `/avtomatizaciya-finansov-no-code/`, `/obezlichivanie-dannyh-chatgpt-finansist/`  
**sibling_queue:** B82 (Sheets API + SA), B21 (MCP в Cursor общий), B51/B58/B83 (реестры в Sheets), B93 (ротация SA)  
**cover_scene_hint:** abstract holographic finance automation dark #0a0a0f purple #8b5cf6, no text

---

## utility_verdict

**PASS** — тема utility-only how_to. Читатель получает рабочий маршрут: выбрать путь подключения Google Sheets к Cursor через MCP (community SA `mcp-gsheets` **или** remote Google `sheetsmcp.googleapis.com` / Marketplace Workspace, если доступен), подготовить реестр под агентные правки, прогнать сценарий «найти строку по `doc_key` → обновить статус → перечитать», чеклист безопасности и troubleshooting. Не новость «Cursor открыл Workspace», не обзор 25 MCP-серверов, не туториал «напиши свой MCP с нуля».

---

## reader_outcome

После гайда финансист сможет подключить MCP Google Sheets в Cursor, дать агенту доступ только к рабочему реестру (через service account или OAuth/remote MCP), попросить обновить статус строки или дописать поля без копирования таблицы в чат и проверить результат перечиткой диапазона через MCP-tool.

---

## action_outline

1. **Решить, нужен ли MCP Sheets** — реестр уже в Google Sheets (договоры, УПД, SaaS, заявки на расход), правки повторяются, устали таскать диапазоны в чат; **не** делать, если нужен жёсткий audit trail / сотни таблиц с enterprise ACL — тогда 1С/CLM, Sheets только staging.
2. **Выбрать путь подключения** — **Path A (пилот):** Marketplace Workspace / OAuth, если плагин Sheets доступен в витрине (на 2026-09-07 в официальном changelog Cursor детализированы Drive/Gmail/Calendar; Sheets — через community или remote Google MCP). **Path B (финконтур):** `freema/mcp-gsheets` + service account — расшарить только нужные реестры, ключ в `env`, без доступа агента ко всему Drive (см. B82, B93). **Path C (preview):** remote `https://sheetsmcp.googleapis.com/mcp/v1` после включения Sheets MCP API в GCP (док Google: Antigravity/Claude; в Cursor — remote `url` в `mcp.json`).
3. **Подготовить реестр** — одна строка = одна сущность; стабильный `doc_key`; лист `staging` для импорта; в облако без сырых ПДн (ИНН/сумма/статус — да; паспорт, полные ФИО — нет); interlink `/obezlichivanie-dannyh-chatgpt-finansist/`.
4. **Path B: Google Cloud + SA** — проект → включить **Google Sheets API** → service account → JSON-ключ → скопировать `client_email` → «Поделиться» на файл реестра с ролью **Редактор** (без «Уведомить»).
5. **Path B: mcp.json в Cursor** — глобально `~/.cursor/mcp.json` или проектно `.cursor/mcp.json`; блок `mcp-gsheets` с `npx -y mcp-gsheets@latest` и `GOOGLE_APPLICATION_CREDENTIALS` (абсолютный путь); JSON-ключ **не** в git. Node.js **v20+**.
6. **Path A/C: OAuth / remote** — Customize → MCPs / Marketplace **или** `url` + OAuth для `sheetsmcp.googleapis.com`; минимальные scopes (`spreadsheets` / `spreadsheets.readonly`); учесть, что Cursor Cloud Agents не наследуют локальный OAuth автоматически.
7. **Проверить подключение** — перезапуск Cursor; Customize → MCPs → зелёный статус; Output → **MCP Logs**; tool `sheets_check_access` (Path B) или живой запрос «прочитай A1:C5 листа Реестр» / `get_values`.
8. **Рабочий сценарий реестра** — промпт с DoD: metadata/list → найти строку по `doc_key` → `sheets_update_values` / `update_values` / `sheets_append_values` только в колонки статуса/комментария → перечитать ту же строку → сверка; human approval на каждый write-tool; для append в mcp-gsheets явно `INSERT_ROWS` (default `OVERWRITE`).
9. **Эксплуатация и рост** — allowlist write-tools; ротация ключа SA (B93); квоты Sheets API 300 write/мин на проект; при >80–100 заявок/мес или audit — n8n/ERP, Sheets остаётся staging; соседние реестры B51/B58/B83.

**Workflow для статьи:**  
`Реестр в Sheets → (SA share | OAuth/remote) → MCP в Cursor → Agent read/update по doc_key → перечитка диапазона → регламент CFO`

---

## Яндекс Wordstat (MCP user-mcp-kv)

⚠️ **WORDSTAT AUTH WARNING:** сервер MCP `user-mcp-kv` в этой Cloud-сессии **не подключён** (`CallDynamicTool` → `MCP server does not exist: user-mcp-kv`). Вызов `wordstat_get_top_requests` **не выполнен**. Точные показы/мес **не получены** и **не выдуманы**.

Обновление токена / подключение MCP-KV: https://oauth.yandex.ru/authorize?response_type=token&client_id=c654b948515a4a07a4c89648a0831d40

### Таблица спроса (Wordstat)

| Фраза | Показы в месяц |
| --- | --- |
| mcp google sheets cursor | *не получено — MCP user-mcp-kv недоступен* |
| cursor mcp | *не получено — MCP user-mcp-kv недоступен* |
| mcp сервер для cursor | *не получено — MCP user-mcp-kv недоступен* |
| автоматизация финотдела | *не получено — MCP user-mcp-kv недоступен* |
| google sheets mcp | *не получено — MCP user-mcp-kv недоступен* |
| подключить mcp cursor | *не получено — MCP user-mcp-kv недоступен* |

**Экспертная семантика (LSI для writer, без цифр спроса):**

| Кластер | Фразы | Роль |
| --- | --- | --- |
| Primary | mcp google sheets cursor, google sheets mcp cursor | H1, title |
| Setup | mcp.json cursor, mcp-gsheets service account, sheetsmcp.googleapis.com | H2 пошагово |
| Finance | автоматизация финотдела google sheets, реестр договоров cursor, править реестр без копипаста | угол КОДА |
| Registry | реестр upd google sheets, реестр saas подписок, doc_key find update | кейсы |
| Security | service account json не в git, обезличивание sheets, oauth scopes минимум, prompt injection | FAQ |
| Ops | sheets_check_access, mcp logs cursor, 429 sheets api, verify after write | troubleshooting |
| Adjacent | cursor google workspace plugins 2026, mcp cursor finansist | interlink B21 |

**SEO-вывод:** SERP по `mcp google sheets cursor` — EN-гайды community MCP (freema, we2go, henilcalagiya), каталоги MCP, новости Cursor Workspace (август 2026) и **официальный Google Sheets MCP** (`sheetsmcp.googleapis.com`). Почти нет RU how-to «финансист + реестр + Cursor + verify loop». Угол КОДА: **правка управленческих реестров через MCP без копипаста**, с веткой SA для безопасности и сравнением с B82 (скрипт) и B21 (общий MCP).

---

## SERP (WebSearch Cursor, 07.09.2026)

Приоритет — живой WebSearch 2026-09-07; `research-serp.json` от того же дня полезен как URL-черновик; query `2026 2026` и часть сниппетов (в т.ч. кликбейт «Cursor закрыт в России») **нерелевантны / неверифицированы** — не копировать в статью без отдельной проверки.

### Primary: `mcp google sheets cursor 2026`

| # | URL | Тип | Пробел для КОДА |
| --- | --- | --- | --- |
| 1 | https://cursor.com/help/customization/mcp | Официальный help | Нет реестров финотдела |
| 2 | https://cursor.com/docs/mcp | Docs MCP | Канон; нет Sheets-кейса |
| 3 | https://github.com/freema/mcp-gsheets | Community MCP (SA) | EN; dev-фокус, не CFO |
| 4 | https://mcpservers.org/servers/freema/mcp-gsheets | Каталог + конфиг | Дубль README |
| 5 | https://github.com/we2go/google-mcp | Wizard OAuth/SA | Не реестры |
| 6 | https://developers.google.com/workspace/guides/configure-mcp-servers | Official remote Sheets MCP | Antigravity/Claude first; Cursor = «Others» |
| 7 | https://developers.google.com/workspace/sheets/api/reference/mcp | Tools `get_values` / `update_values` | Не finance UX |
| 8 | https://mcp-catalog.ru/tutorials/google-sheets-cursor | RU: henilcalagiya | Без SA/финконтура |
| 9 | https://skiln.co/blog/google-sheets-mcp-review-2026 | Обзор ecosystem | Маркетинг; не finance |
| 10 | https://pastesheet.com/guides/google-sheets-mcp-cursor | Hosted MCP | Публичные/платные листы |

### News / Workspace (актуально на сентябрь 2026)

| # | URL | Тип | Пробел |
| --- | --- | --- | --- |
| 1 | https://cursor.com/changelog/google-workspace-plugins | Changelog 03.08.2026 | Drive/Gmail/Calendar; Sheets в теле **не** расписан |
| 2 | https://mayai.ru/cursor-otkryl-gmail-i-sheets-agentam/ | RU разбор | Мало SA/реестров |
| 3 | https://vibecoding.ru/news/2026/08/03/cursor-google-workspace-plugins | RU: витрина/OAuth bug | Sheets могли убрать из витрины |
| 4 | https://indieseek.co/blogs/cursor-google-workspace-plugins-security-checklist/ | Security checklist | Drive/Gmail/Calendar endpoints; Sheets отдельно |
| 5 | https://www.explainx.ai/blog/cursor-google-workspace-plugins-gmail-drive-calendar-august-2026 | EN анализ | Gap доки по Sheets |

### Secondary: `автоматизация финотдела` + Sheets/агенты

| # | URL | Тип | Пробел |
| --- | --- | --- | --- |
| 1 | https://habr.com/ru/articles/1017260/ | Кейс AI-агентов + Sheets API | Не Cursor MCP setup; сильный verify-loop |
| 2 | https://koda-fd.ru/blog/ai-dlya-finansista-2026/ | Hub КОДА | Нет MCP Cursor |
| 3 | https://comandos.ai/blog/ai-finansovyi-otdel | Мульти-агенты / Antigravity | Не how-to Cursor+Sheets |
| 4 | https://dzen.ru/a/anRW32ni3D3wHjQF | Реестр договоров Sheets | Без MCP |

### Конкурентный зазор (угол КОДА)

1. **Finance-first** — не «подключи Sheets к Cursor», а «перестань копировать реестр в чат: agent правит строку по `doc_key`».
2. **Два–три пути с честным выбором** — SA+mcp-gsheets для production финконтура; Marketplace/OAuth для пилота (если Sheets в витрине); remote Google Sheets MCP как preview (GCP + OAuth).
3. **Связка с реестрами серии** — договоры (B51), УПД (B58), SaaS (B83); MCP = слой правок поверх уже спроектированной таблицы.
4. **Security** — минимальный share, ключ вне git, approval tools, indirect prompt injection (Google Workspace MCP docs), обезличивание.
5. **Verify loop** — после write всегда `get_values` / `sheets_get_values` (Habr: batch может «терять» строки; Connected ≠ authorized).
6. **Fork от B82** — B82 = свой Python-скрипт; B92 = те же SA+share, но правки через Agent+MCP без написания кода.

---

## Таблица фактов

| # | Утверждение | Источник | Дата проверки |
| --- | --- | --- | --- |
| 1 | MCP подключает Cursor к внешним инструментам; Agent вызывает tools в чате. | https://cursor.com/help/customization/mcp | 2026-09-07 |
| 2 | Конфиг: проектный `.cursor/mcp.json` + глобальный `~/.cursor/mcp.json`; one-click через Customize → MCPs. | https://cursor.com/help/customization/mcp | 2026-09-07 |
| 3 | Локальный MCP: `command`/`args`/`env`; удалённый — `url` (+ опционально `headers`). После ручного `mcp.json` — перезапуск Cursor. | https://cursor.com/help/customization/mcp | 2026-09-07 |
| 4 | По умолчанию Agent запрашивает approval перед MCP-tool; с Cursor 3.6+ — Auto-review / allowlist (`permissions.json`). | https://cursor.com/help/customization/mcp | 2026-09-07 |
| 5 | Troubleshooting: Output → **MCP Logs**. | https://cursor.com/help/customization/mcp | 2026-09-07 |
| 6 | Cloud Agents поддерживают MCP, настроенные в Cloud Agents dashboard / Team Integrations — не «магическое» наследование локального OAuth. | https://cursor.com/help/customization/mcp | 2026-09-07 |
| 7 | 03.08.2026 Cursor анонсировал Google Workspace plugins: в changelog явно **Drive, Gmail, Calendar** (Marketplace / Customize). | https://cursor.com/changelog/google-workspace-plugins | 2026-09-07 |
| 8 | Sheets/Docs в тексте changelog Cursor **не детализированы** как отдельные marketplace-плагины в этом релизе. | https://cursor.com/changelog/google-workspace-plugins | 2026-09-07 |
| 9 | Google публикует remote Workspace MCP, в т.ч. Sheets: `https://sheetsmcp.googleapis.com/mcp/v1`; нужны GCP project, Sheets API + Sheets MCP API (`sheetsmcp.googleapis.com`), OAuth. | https://developers.google.com/workspace/guides/configure-mcp-servers | 2026-09-07 |
| 10 | Официальные примеры клиентов в доке Google: Antigravity и Claude; раздел **Others** описывает remote HTTP + OAuth для прочих MCP-клиентов (в т.ч. Cursor через `url`). | https://developers.google.com/workspace/guides/configure-mcp-servers | 2026-09-07 |
| 11 | Test prompt Google для Sheets: «Read sheet Sheet1…» → tool `sheets.get_values`. | https://developers.google.com/workspace/guides/configure-mcp-servers | 2026-09-07 |
| 12 | Google прямо предупреждает про **indirect prompt injection** при чтении писем/документов через Workspace MCP — review всех write/delete. | https://developers.google.com/workspace/guides/configure-mcp-servers | 2026-09-07 |
| 13 | Sheets MCP toolset (офиц.): `get_values`, `get_spreadsheet`, `update_spreadsheet`, `update_values`, `update_formulas`, `insert_dimension` — каждый tool = 1 read или 1 write request к квоте. | https://developers.google.com/workspace/sheets/api/limits | 2026-09-07 |
| 14 | Квоты Sheets API / Sheets MCP: **300** read и **300** write запросов/мин на проект; **60**/мин на user per project; превышение → HTTP **429**. | https://developers.google.com/workspace/sheets/api/limits | 2026-09-07 |
| 15 | Batch request считается **одним** API-запросом; вызовы SA считаются одним user account. | https://developers.google.com/workspace/sheets/api/limits | 2026-09-07 |
| 16 | Превышение quota limits планируется тарифицироваться в Google Cloud billing **later in 2026** (standardized model for agent tools). | https://developers.google.com/workspace/sheets/api/limits | 2026-09-07 |
| 17 | `freema/mcp-gsheets`: Node.js **v20+**, Sheets API, service account JSON; Cursor: Settings → MCP → New MCP Server; `npx -y mcp-gsheets@latest` + `GOOGLE_APPLICATION_CREDENTIALS`. | https://github.com/freema/mcp-gsheets | 2026-09-07 |
| 18 | npm-пакет `mcp-gsheets` (реестр): версия **1.10.0** (на момент research). | https://www.getdrio.com/mcp/io-github-freema-mcp-gsheets | 2026-09-07 |
| 19 | Ключевые tools mcp-gsheets: `sheets_get_values`, `sheets_update_values`, `sheets_append_values`, `sheets_batch_get_values`, `sheets_get_metadata`, `sheets_check_access`. | https://github.com/freema/mcp-gsheets | 2026-09-07 |
| 20 | `sheets_append_values`: default `insertDataOption` = **OVERWRITE** — для реестра указывать `INSERT_ROWS`. | https://github.com/freema/mcp-gsheets | 2026-09-07 |
| 21 | Альт. auth mcp-gsheets: `GOOGLE_SERVICE_ACCOUNT_KEY` (JSON string) или `GOOGLE_PRIVATE_KEY` + `GOOGLE_CLIENT_EMAIL` (newlines как `\\n`). | https://github.com/freema/mcp-gsheets | 2026-09-07 |
| 22 | Service account видит **только** таблицы, расшаренные на `client_email`; IAM Cloud ≠ Share файла. | https://developers.google.com/workspace/guides/create-credentials#service-account | 2026-09-07 |
| 23 | Scope `https://www.googleapis.com/auth/spreadsheets` — read/write всех расшаренных таблиц SA; применяется ко **всему файлу**. | https://developers.google.com/workspace/sheets/api/scopes | 2026-09-07 |
| 24 | `we2go/google-mcp`: wizard `npx google-sheet-mcp init` (SA) / `--auth oauth`; tools read/update/append. | https://github.com/we2go/google-mcp | 2026-09-07 |
| 25 | Практика финотдела: после записи в Sheets API обязательно перечитывать и сверять — batch может молча «недоложить» строки. | https://habr.com/ru/articles/1017260/ | 2026-09-07 |
| 26 | Реестр договоров в Sheets уместен до **200–300** активных договоров при одном владельце; иначе CLM/1С. | https://dzen.ru/a/anRW32ni3D3wHjQF | 2026-09-07 |
| 27 | Заявки на расход Forms→Sheets: при **>80–100** заявок/мес Sheets — staging перед ERP/n8n. | https://dzen.ru/a/aoAx4V_t_ztBh5aj | 2026-09-07 |

**Не выдумывать:** показы Wordstat; «Sheets-плагин всегда в Marketplace Cursor» (проверять на дату; changelog фиксирует Drive/Gmail/Calendar); что SA = доступ ко всему Drive; ROI/цифры контент-заводов из fact-bank; слухи «Cursor закрыт в РФ» без первоисточника; обещание «без программиста» для Path B/C без GCP/OAuth.

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

**Remote Google Sheets MCP (Path C, sketch для продвинутых — не основной путь статьи):**

```json
{
  "mcpServers": {
    "google-sheets": {
      "url": "https://sheetsmcp.googleapis.com/mcp/v1"
    }
  }
}
```

(OAuth/client credentials — по доке Google + возможностям Cursor remote MCP; не обещать one-click без проверки витрины.)

**Тестовый промпт агента (реестр):**

> Подключись к таблице `{SPREADSHEET_ID}`. На листе `Реестр` найди строку, где колонка `doc_key` = `DOG-2026-014`. Прочитай текущие значения колонок `status` и `comment`. Если `status` ≠ «Оплачен», предложи обновление на «На согласовании» и допиши в `comment` сегодняшнюю дату. После write перечитай ту же строку и покажи diff.

---

## FAQ-кандидаты (из карточки)

- **Можно ли без программиста?** — Path A (Marketplace+OAuth), если Sheets в витрине: да для пилота; Path B (SA+mcp.json): по инструкции, Cursor поможет с JSON; production — 1–2 ч первый реестр.
- **Сколько займёт внедрение?** — SA + mcp.json + один тестовый update: **~1–2 ч**; OAuth/Marketplace быстрее, если доступен.
- **Какие риски для данных?** — OAuth = права вашего Google; SA-ключ = все расшаренные файлы; не класть ПДн; подтверждать write-tools; indirect injection из ячеек/писем.
- **OAuth или service account?** — OAuth для личного пилота; SA для командного реестра, cron, минимального blast radius.
- **Чем отличается от B82?** — B82 = Python/Node скрипт пишет в staging; B92 = Agent в Cursor правит через MCP без скрипта.
- **Официальный Google Sheets MCP?** — remote `sheetsmcp.googleapis.com` есть в доке Google (preview-контур); в Cursor надёжный путь финотдела на сентябрь 2026 — community SA `mcp-gsheets`, пока Marketplace Sheets не подтверждён changelog’ом.
- **Работает ли в Cloud Agents?** — локальный OAuth не переезжает автоматически; Team/Cloud MCP dashboard или SA.

---

## CTA / interlink

- Internal: `/avtomatizaciya-finansov-no-code/`, `/obezlichivanie-dannyh-chatgpt-finansist/`, `/google-sheets-api-integraciya-finotdel/` (B82), `/mcp-cursor-finansist-instrumenty/` (B21)
- Соседние реестры: B51, B58, B83; ротация ключа: B93
- CTA: `https://club.koda-fd.ru/?utm_source=blog&utm_medium=article&utm_campaign=mcp-google-sheets-cursor-reestry` (≤2), `https://t.me/finance_modern?utm_source=blog&utm_medium=article` (≤2)

---

## Handoff marker

`=== EXCALIBUR BLOG RESEARCH ===` — см. `.cursor/excalibur-blog-handoff.md`
