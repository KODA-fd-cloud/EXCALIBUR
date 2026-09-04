# Research notes — B92

**topic_id:** B92  
**slug:** mcp-google-sheets-cursor-reestry  
**h1:** Как подключить MCP к Google Sheets в Cursor и править реестры без копипаста  
**research_date:** 2026-09-04  
**publish_target:** koda-fd.ru/blog  
**utility_gate:** PASS (`how_to`, mode B)  
**author_id:** olga-kondratskaya  
**related_internal:** `/avtomatizaciya-finansov-no-code/`, `/obezlichivanie-dannyh-chatgpt-finansist/`  
**sibling_queue:** B82 (Sheets API + SA), B21 (MCP в Cursor общий), B51/B58/B83 (реестры в Sheets), B93 (ротация SA)  
**cover_scene_hint:** abstract holographic finance automation dark #0a0a0f purple #8b5cf6, no text

---

## utility_verdict

**PASS** — тема utility-only how_to. Читатель получает рабочие маршруты подключения Google Sheets к Cursor через MCP (community `mcp-gsheets` на service account — основной финконтур; Marketplace/OAuth-плагин — пилот; опционально официальный remote Sheets MCP Google), подготовку реестра под агентные правки, тестовый сценарий «найти строку → обновить статус → перечитать», чеклист безопасности и troubleshooting. Не новость «Cursor открыл Workspace», не обзор 25 MCP-серверов, не туториал «напиши свой MCP с нуля».

---

## reader_outcome

После гайда финансист сможет подключить MCP Google Sheets в Cursor, дать агенту доступ только к рабочему реестру (через service account или OAuth), попросить обновить статус строки или дописать поля без копирования таблицы в чат и проверить результат перечиткой диапазона через MCP-tool.

---

## action_outline

1. **Решить, нужен ли MCP Sheets** — реестр уже в Google Sheets (договоры, УПД, SaaS, заявки на расход), правки повторяются, устали таскать диапазоны в чат; **не** делать, если нужен жёсткий audit trail / сотни таблиц с enterprise ACL — тогда 1С/CLM, Sheets только staging.
2. **Выбрать путь подключения** — **Path B (финконтур, рекомендовать):** `freema/mcp-gsheets` + service account — расшарить только нужные реестры, ключ в `env`, без доступа агента ко всему Drive; **Path A (пилот):** плагин/OAuth из Cursor Marketplace / Customize; **Path C (опционально):** официальный remote MCP Google `https://sheetsmcp.googleapis.com/mcp/v1` (OAuth пользователя, нужен GCP + Sheets MCP API) — см. docs Google; не путать с Cursor Marketplace.
3. **Подготовить реестр** — одна строка = одна сущность; стабильный `doc_key`; лист `staging` для импорта; в облако без сырых ПДн (ИНН/сумма/статус — да; паспорт, полные ФИО — нет); interlink `/obezlichivanie-dannyh-chatgpt-finansist/`.
4. **Path B: Google Cloud + SA** — проект → включить **Google Sheets API** → service account → JSON-ключ → скопировать `client_email` → «Поделиться» на файл реестра с ролью **Редактор** (без «Уведомить»).
5. **Path B: mcp.json в Cursor** — глобально `~/.cursor/mcp.json` или проектно `.cursor/mcp.json`; блок `mcp-gsheets` с `npx -y mcp-gsheets@latest` и `GOOGLE_APPLICATION_CREDENTIALS` (абсолютный путь) **или** `GOOGLE_PRIVATE_KEY` + `GOOGLE_CLIENT_EMAIL`; JSON-ключ **не** в git.
6. **Path A / Path C: OAuth** — Path A: Customize → MCPs → Google Sheets / Workspace → Add → OAuth, минимальные scopes; учесть, что в changelog 03.08.2026 детально описаны Drive/Gmail/Calendar, а Sheets/Docs — в анонсе, но витрина могла меняться. Path C: enable `sheets.googleapis.com` + `sheetsmcp.googleapis.com`, remote URL + OAuth client — по [доке Google](https://developers.google.com/workspace/sheets/api/guides/configure-mcp-server).
7. **Проверить подключение** — перезапуск Cursor после правки `mcp.json`; Customize → MCPs → зелёный статус; Output → **MCP Logs**; Path B: `sheets_check_access` / «прочитай A1:C5 листа Реестр»; Path C: `get_values` / `get_spreadsheet`.
8. **Рабочий сценарий реестра** — промпт с DoD: metadata → найти строку по `doc_key` → update/append только в колонки статуса/комментария → get_values на ту же строку → сверка; human approval на каждый write-tool; учесть quota **60 req/min на user** (SA = один «user»).
9. **Эксплуатация и рост** — allowlist write-tools; ротация ключа SA (B93); при >80–100 заявок/мес или audit — n8n/ERP, Sheets остаётся staging; соседние реестры B51/B58/B83.

**Workflow для статьи:**  
`Реестр в Sheets → (SA share | OAuth plugin | Google remote MCP) → MCP в Cursor → Agent read/update по doc_key → перечитка диапазона → регламент CFO`

---

## Яндекс Wordstat (MCP user-mcp-kv)

⚠️ **WORDSTAT AUTH WARNING:** сервер MCP `user-mcp-kv` в этой Cloud-сессии **не подключён** (`GetDynamicTools` / `CallDynamicTool`: `MCP server does not exist: user-mcp-kv`). Вызов `wordstat_get_top_requests` **не выполнен**. Точные показы/мес **не получены** и **не выдуманы**.

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
| Setup | mcp.json cursor, cursor marketplace google sheets, mcp-gsheets service account, sheetsmcp.googleapis.com | H2 пошагово |
| Finance | автоматизация финотдела google sheets, реестр договоров cursor, править реестр без копипаста | угол КОДА |
| Registry | реестр upd google sheets, реестр saas подписок, doc_key find update | кейсы |
| Security | service account json не в git, обезличивание sheets, oauth scopes минимум, indirect prompt injection | FAQ |
| Ops | sheets_check_access, mcp logs cursor, 429 quota sheets api | troubleshooting |
| Adjacent | cursor google workspace plugins 2026, mcp cursor finansist | interlink B21 |

**SEO-вывод:** SERP по `mcp google sheets cursor` — **EN-гайды по community MCP** (freema, we2go), **официальная дока Google Sheets MCP** (remote), **Cursor MCP docs**, коммерческие CData/Merge. Почти нет RU how-to «финансист + реестр + Cursor». Угол КОДА: **правка управленческих реестров через MCP без копипаста**, с веткой SA для безопасности и явным сравнением с B82 (скрипт) и B21 (общий MCP).

---

## SERP (WebSearch Cursor, 04.09.2026)

Приоритет — живой WebSearch; `research-serp.json` (шаг 0) — черновик URL; query `2026 2026` и часть сниппетов **нерелевантны** — не копировать.

### Primary: `mcp google sheets cursor 2026`

| # | URL | Тип | Пробел для КОДА |
| --- | --- | --- | --- |
| 1 | https://cursor.com/docs/mcp | Официальный reference MCP | Нет реестров финотдела |
| 2 | https://cursor.com/help/customization/mcp | Help: mcp.json, OAuth, approvals, Cloud Agents | Канон шагов; нет Sheets-кейса |
| 3 | https://github.com/freema/mcp-gsheets | Community MCP (SA) | EN; dev-фокус, не CFO |
| 4 | https://github.com/we2go/google-mcp | npx wizard OAuth/SA | Sheets+Docs; не реестры |
| 5 | https://developers.google.com/workspace/sheets/api/guides/configure-mcp-server | **Официальный** remote Sheets MCP | Antigravity/Claude; Cursor = «Others»; нет finance |
| 6 | https://www.cdata.com/kb/tech/gsheets-mcp-cursor.rst | CData commercial MCP | Vendor lock; не SA-финконтур |
| 7 | https://www.merge.dev/blog/google-sheets-mcp-cursor | Merge Agent Handler | SaaS-посредник |
| 8 | https://eastondev.com/blog/en/posts/dev/20260116-cursor-mcp-guide/ | Общий MCP setup | Workspace упомянут обзорно |

### Official Google / Workspace news

| # | URL | Тип | Пробел |
| --- | --- | --- | --- |
| 1 | https://developers.google.com/workspace/guides/configure-mcp-servers | Google Workspace MCP family | Endpoint `sheetsmcp.googleapis.com` |
| 2 | https://cursor.com/changelog/google-workspace-plugins | Changelog 03.08.2026 | Drive/Gmail/Calendar детально; Sheets в теле changelog **не расписан** |
| 3 | https://explainx.ai/blog/cursor-google-workspace-plugins-gmail-drive-calendar-august-2026 | EN анализ gap | Docs/Sheets в X, не в changelog |
| 4 | https://mcpyet.com/mcp/google-sheets/ | Каталог: Official Sheets MCP | Developer Preview note; remote URL |
| 5 | https://byteiota.com/cursor-3-google-workspace-plugins-gmail-drive-and-docs-in-your-ide/ | Secondary claim Sheets in plugins | Сверять с primary changelog |

### Secondary: реестры / автоматизация финотдела

| # | URL | Тип | Пробел |
| --- | --- | --- | --- |
| 1 | https://dzen.ru/a/anRW32ni3D3wHjQF | Реестр договоров Sheets | Без MCP |
| 2 | https://dzen.ru/a/aoAx4V_t_ztBh5aj | Заявки Forms→Sheets | Без MCP; порог 80–100 |
| 3 | https://koda-fd.ru/blog/ai-dlya-finansista-2026/ | Hub КОДА | Нет MCP Cursor |
| 4 | https://ascn.ai/ru/blog-no-code/how-to-automate-contract-management | No-code договоры | Не Cursor |

### Конкурентный зазор (угол КОДА)

1. **Finance-first** — не «подключи Sheets к Cursor», а «перестань копировать реестр в чат: agent правит строку по `doc_key`».
2. **Три пути с выбором** — SA+mcp-gsheets для production финконтура; OAuth-плагин для пилота; официальный Google remote MCP как альтернатива (honest note: дока ориентирована на Antigravity/Claude, Cursor — generic remote).
3. **Связка с реестрами серии** — договоры (B51), УПД (B58), SaaS (B83); MCP = слой правок поверх уже спроектированной таблицы.
4. **Security block** — минимальный share, ключ вне git, approval tools, indirect prompt injection (Google MCP docs + mayai), обезличивание.
5. **Verify loop** — после write всегда get_values; «Connected ≠ authorized».
6. **Quota realism** — 60 req/min per user: агент на одном SA легко упирается в 429 при «исследовании» таблицы.
7. **Fork от B82** — B82 = свой Python-скрипт; B92 = те же SA+share, но правки через Agent+MCP без написания кода.

---

## Таблица фактов

| # | Утверждение | Источник | Дата проверки |
| --- | --- | --- | --- |
| 1 | MCP подключает Cursor к внешним инструментам; Agent вызывает tools в чате. | https://cursor.com/help/customization/mcp | 2026-09-04 |
| 2 | Конфиг MCP: проектный `.cursor/mcp.json` + глобальный `~/.cursor/mcp.json`; при совпадении имени побеждает **проектный**. | https://cursor.com/help/customization/mcp | 2026-09-04 |
| 3 | Локальный MCP: `command`, `args`, `env`; удалённый — поле `url` (+ опционально `headers`). | https://cursor.com/help/customization/mcp | 2026-09-04 |
| 4 | One-click: Customize → MCPs → Add to Cursor; после ручного `mcp.json` — **перезапуск Cursor**. | https://cursor.com/help/customization/mcp | 2026-09-04 |
| 5 | По умолчанию Agent **запрашивает approval** перед MCP-tool; Cursor 3.6+ — Auto-review / allowlist / `permissions.json`. | https://cursor.com/help/customization/mcp | 2026-09-04 |
| 6 | Troubleshooting: Output → **MCP Logs** (`Ctrl+Shift+U` / `Cmd+Shift+U`). | https://cursor.com/help/customization/mcp | 2026-09-04 |
| 7 | Cloud Agents поддерживают MCP, настроенные в Cloud Agents dashboard; Team — Dashboard → Integrations & MCP / Team Marketplace. | https://cursor.com/help/customization/mcp | 2026-09-04 |
| 8 | 03.08.2026 Cursor анонсировал Google Workspace plugins: агенты работают с Drive, Gmail, Calendar **без выхода из редактора**; установка из Marketplace или Customize. | https://cursor.com/changelog/google-workspace-plugins | 2026-09-04 |
| 9 | В changelog 03.08.2026 детально перечислены **Drive, Gmail, Calendar**; Sheets/Docs в этом документе **не детализированы** (упоминаются во вторичных разборах / X). | https://cursor.com/changelog/google-workspace-plugins ; https://explainx.ai/blog/cursor-google-workspace-plugins-gmail-drive-calendar-august-2026 | 2026-09-04 |
| 10 | Google публикует **официальный remote Sheets MCP**: endpoint `https://sheetsmcp.googleapis.com/mcp/v1`; enable `sheets.googleapis.com` + `sheetsmcp.googleapis.com`; auth OAuth 2.0. | https://developers.google.com/workspace/sheets/api/guides/configure-mcp-server | 2026-09-04 |
| 11 | Tools официального Sheets MCP: `get_values`, `get_spreadsheet`, `update_spreadsheet`, `update_values`, `update_formulas`, `insert_dimension`. | https://developers.google.com/workspace/sheets/api/guides/configure-mcp-server | 2026-09-04 |
| 12 | Google прямо предупреждает про **indirect prompt injection** при MCP+Sheets: скринить входы/ответы, не обрабатывать таблицы из недоверенных источников, review всех write-действий. | https://developers.google.com/workspace/sheets/api/guides/configure-mcp-server | 2026-09-04 |
| 13 | Scopes для Google Sheets MCP (из доки): `drive.readonly`, `drive.file`, `spreadsheets.readonly`, `spreadsheets`. | https://developers.google.com/workspace/sheets/api/guides/configure-mcp-server | 2026-09-04 |
| 14 | `freema/mcp-gsheets`: Node.js **v20+**, Sheets API, service account JSON; Cursor: `npx -y mcp-gsheets@latest` + `GOOGLE_APPLICATION_CREDENTIALS` или `GOOGLE_PRIVATE_KEY` + `GOOGLE_CLIENT_EMAIL`. | https://github.com/freema/mcp-gsheets | 2026-09-04 |
| 15 | Ключевые tools mcp-gsheets для реестра: `sheets_get_values`, `sheets_update_values`, `sheets_append_values`, `sheets_batch_get_values`, `sheets_get_metadata`, `sheets_check_access`. | https://github.com/freema/mcp-gsheets | 2026-09-04 |
| 16 | `sheets_append_values`: по умолчанию `insertDataOption` = **OVERWRITE** — для реестра явно указывать `INSERT_ROWS`, если нужно сдвигать строки. | https://github.com/freema/mcp-gsheets | 2026-09-04 |
| 17 | Service account видит **только** таблицы, расшаренные на `client_email` из JSON; IAM-роли Cloud **не заменяют** Share файла. | https://developers.google.com/workspace/guides/create-credentials#service-account | 2026-09-04 |
| 18 | Scope `https://www.googleapis.com/auth/spreadsheets` — read/write всех расшаренных таблиц SA; применяется ко **всему файлу**; листы защищают ProtectedRange. | https://developers.google.com/workspace/sheets/api/scopes | 2026-09-04 |
| 19 | Квоты Sheets API: read/write **300/мин на проект** и **60/мин на user на проект**; превышение → HTTP **429**; квоты refill каждую минуту. | https://developers.google.com/workspace/sheets/api/limits | 2026-09-04 |
| 20 | Один service account = один «user» для квоты 60/мин — агент, который много раз читает диапазоны, упирается в per-user limit раньше project limit. | https://developers.google.com/workspace/sheets/api/limits ; https://dev.to/pastesheet/google-sheets-api-rate-limits-what-60-requestsminute-actually-means-1mim | 2026-09-04 |
| 21 | `we2go/google-mcp`: `npx google-mcp init` — wizard SA или OAuth; tools `sheets_read_range`, `sheets_update_range`, `sheets_append_row` / `sheets_list_tabs`. | https://github.com/we2go/google-mcp | 2026-09-04 |
| 22 | Реестр договоров в Sheets уместен до **200–300** активных договоров при одном владельце таблицы; иначе CLM/1С. | https://dzen.ru/a/anRW32ni3D3wHjQF | 2026-09-04 |
| 23 | Заявки на расход через Forms→Sheets: при **>80–100** заявок/мес Sheets — staging перед ERP/n8n. | https://dzen.ru/a/aoAx4V_t_ztBh5aj | 2026-09-04 |
| 24 | Рекомендуемый max payload Sheets API ~**2 MB**; обработка одного запроса до **180 с**. | https://developers.google.com/workspace/sheets/api/limits | 2026-09-04 |
| 25 | Стандартное использование Sheets API без доп. платы; превышение квот планируется тарифицировать в Cloud billing **later in 2026** (по формулировке Google). | https://developers.google.com/workspace/sheets/api/limits | 2026-09-04 |

**Не выдумывать:** показы Wordstat; «Sheets-плагин всегда в Marketplace» (проверять на дату публикации); что SA = доступ ко всему Drive; цифры сторонних каталогов installs; что официальный Google MCP «из коробки в Cursor» без OAuth/GCP; обещание «без программиста» для Path B без упоминания GCP/SA.

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

**Пример remote (Path C — только как опция, не основной):**

```json
{
  "mcpServers": {
    "sheets": {
      "url": "https://sheetsmcp.googleapis.com/mcp/v1"
    }
  }
}
```

(Для production OAuth clientId/secret — по доке Google; Cursor принимает `url` + headers/OAuth flow клиента.)

**Тестовый промпт агента (реестр):**

> Подключись к таблице `{SPREADSHEET_ID}`. На листе `Реестр` найди строку, где колонка `doc_key` = `DOG-2026-014`. Прочитай текущие значения колонок `status` и `comment`. Если `status` ≠ «Оплачен», предложи обновление на «На согласовании» и допиши в `comment` сегодняшнюю дату. После write перечитай ту же строку и покажи diff.

---

## FAQ-кандидаты (из карточки)

- **Можно ли без программиста?** — Path A (Marketplace+OAuth): да для пилота; Path B (SA+mcp.json): по инструкции B82/B92, Cursor поможет с JSON; production — 1–2 ч первый реестр; Path C — нужен GCP OAuth client.
- **Сколько займёт внедрение?** — SA + mcp.json + один тестовый update: **~1–2 ч**; OAuth-плагин быстрее, если доступен в витрине.
- **Какие риски для данных?** — OAuth = права вашего Google; SA-ключ = все расшаренные файлы; не класть ПДн; подтверждать write-tools; indirect injection из ячеек/внешних таблиц (дока Google).
- **OAuth или service account?** — OAuth для личного пилота; SA для командного реестра, cron, минимального blast radius.
- **Чем отличается от B82?** — B82 = Python/Node скрипт пишет в staging; B92 = Agent в Cursor правит через MCP без скрипта.
- **Работает ли в Cloud Agents?** — да, через dashboard Integrations & MCP (дока Cursor); локальный OAuth не «переезжает» сам — для облака нужен отдельный коннектор/SA.

---

## CTA / interlink

- Internal: `/avtomatizaciya-finansov-no-code/`, `/obezlichivanie-dannyh-chatgpt-finansist/`, `/google-sheets-api-integraciya-finotdel/` (B82), `/mcp-cursor-finansist-instrumenty/` (B21)
- Соседние реестры: B51, B58, B83; ротация ключа: B93
- CTA: `https://club.koda-fd.ru/?utm_source=blog&utm_medium=article&utm_campaign=mcp-google-sheets-cursor-reestry` (≤2), `https://t.me/finance_modern?utm_source=blog&utm_medium=article` (≤2)

---

## Handoff marker

`=== EXCALIBUR BLOG RESEARCH ===` — см. `.cursor/excalibur-blog-handoff.md`
