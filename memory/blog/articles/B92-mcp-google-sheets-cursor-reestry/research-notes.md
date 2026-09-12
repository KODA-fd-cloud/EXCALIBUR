# Research notes — B92

**topic_id:** B92  
**slug:** mcp-google-sheets-cursor-reestry  
**h1:** Как подключить MCP к Google Sheets в Cursor и править реестры без копипаста  
**research_date:** 2026-09-12  
**previous_research:** 2026-08-24 (сохранена структура; SERP/факты обновлены)  
**publish_target:** koda-fd.ru/blog  
**utility_gate:** PASS (`how_to`, mode B) — подтверждено `excalibur_blog_utility_gate.py --topic-id B92` 2026-09-12  
**author_id:** olga-kondratskaya  
**related_internal:** `/avtomatizaciya-finansov-no-code/`, `/obezlichivanie-dannyh-chatgpt-finansist/`  
**sibling_queue:** B82 (Sheets API + SA), B21 (MCP в Cursor общий), B51/B58/B83 (реестры в Sheets)  
**cover_scene_hint:** abstract holographic finance automation dark #0a0a0f purple #8b5cf6, no text

---

## utility_verdict

**PASS** — тема utility-only how_to. Читатель получает два рабочих маршрута подключения Google Sheets к Cursor через MCP (официальный плагин Marketplace **или** community-сервер `mcp-gsheets` на service account), подготовку реестра под агентные правки, тестовый сценарий «найти строку → обновить статус → перечитать», чеклист безопасности для финданных и troubleshooting. Не новость «Cursor открыл Workspace», не обзор 25 MCP-серверов, не туториал «напиши свой MCP с нуля».

---

## reader_outcome

После гайда финансист сможет подключить MCP Google Sheets в Cursor, дать агенту доступ только к рабочему реестру (через service account или OAuth-плагин), попросить обновить статус строки или дописать поля без копирования таблицы в чат и проверить результат перечиткой диапазона через MCP-tool.

---

## action_outline

1. **Решить, нужен ли MCP Sheets** — реестр уже в Google Sheets (договоры, УПД, SaaS, заявки на расход), правки повторяются, устали таскать диапазоны в чат; **не** делать, если нужен жёсткий audit trail / сотни таблиц с enterprise ACL — тогда 1С/CLM, Sheets только staging.
2. **Выбрать путь подключения** — **Path A (быстрый пилот):** плагин `google-sheets` из Cursor Marketplace / Customize → OAuth (Local); **Path B (финконтур):** `freema/mcp-gsheets` + service account — расшарить только нужные реестры, ключ в `env`, без доступа агента ко всему Drive (см. B82, B93). На 2026-09: Path A часто ломается на Cloud OAuth (`cursor://`) — для production финконтура приоритет Path B.
3. **Подготовить реестр** — одна строка = одна сущность; стабильный `doc_key`; лист `staging` для импорта; в облако без сырых ПДн (ИНН/сумма/статус — да; паспорт, полные ФИО — нет); interlink `/obezlichivanie-dannyh-chatgpt-finansist/`.
4. **Path B: Google Cloud + SA** — проект → включить **Google Sheets API** → service account → JSON-ключ → скопировать `client_email` → «Поделиться» на файл реестра с ролью **Редактор** (без «Уведомить»).
5. **Path B: mcp.json в Cursor** — глобально `~/.cursor/mcp.json` или проектно `.cursor/mcp.json`; блок `mcp-gsheets` с `npx -y mcp-gsheets@latest` и `GOOGLE_APPLICATION_CREDENTIALS` (абсолютный путь); JSON-ключ **не** в git.
6. **Path A: Marketplace (если доступен)** — Customize → MCPs → `google-sheets` → Add → OAuth **Local**; для Cloud — auth через https://cursor.com/agents (не in-app `cursor://`); минимальные scopes; не обещать «всегда в витрине» — changelog детально описывает Drive/Gmail/Calendar, Sheets — в анонсах/форуме.
7. **Проверить подключение** — перезапуск Cursor; Customize → MCPs → зелёный статус; Output → **MCP Logs**; tool `sheets_check_access` (Path B) или живой запрос «прочитай A1:C5 листа Реестр».
8. **Рабочий сценарий реестра** — промпт с DoD: `sheets_get_metadata` → найти строку по `doc_key` → `sheets_update_values` / `sheets_append_values` только в колонки статуса/комментария → `sheets_get_values` на ту же строку → сверка; human approval на каждый write-tool; помнить квоту **60 write/мин на user** (один SA = один «user»).
9. **Эксплуатация и рост** — allowlist write-tools; ротация ключа SA (B93); при >80–100 заявок/мес или audit — n8n/ERP, Sheets остаётся staging; соседние реестры B51/B58/B83.

**Workflow для статьи:**  
`Реестр в Sheets → (SA share | OAuth plugin Local) → MCP в Cursor → Agent read/update по doc_key → перечитка диапазона → регламент CFO`

---

## Яндекс Wordstat (MCP user-mcp-kv)

⚠️ **WORDSTAT AUTH WARNING:** сервер MCP `user-mcp-kv` в этой Cloud-сессии **не подключён** (в каталоге dynamic tools: `cursor`, `Cursor Automation Tools`, `cursor-cloud`, `cursor-subscriptions`). Вызов `wordstat_get_top_requests` **не выполнен**. Точные показы/мес **не получены** и **не выдуманы**.

Обновление токена / подключение MCP-KV: https://oauth.yandex.ru/authorize?response_type=token&client_id=c654b948515a4a07a4c89648a0831d40

### Таблица спроса (Wordstat)

| Фраза | Показы в месяц |
| --- | --- |
| mcp google sheets cursor | *не получено — MCP user-mcp-kv недоступен* |
| cursor mcp | *не получено* |
| mcp сервер для cursor | *не получено* |
| автоматизация финотдела | *не получено* |
| google sheets mcp | *не получено* |
| подключить mcp cursor | *не получено* |

**Экспертная семантика (LSI для writer, без цифр спроса):**

| Кластер | Фразы | Роль |
| --- | --- | --- |
| Primary | mcp google sheets cursor, google sheets mcp cursor | H1, title |
| Setup | mcp.json cursor, cursor marketplace google sheets, mcp-gsheets service account | H2 пошагово |
| Finance | автоматизация финотдела google sheets, реестр договоров cursor, править реестр без копипаста | угол КОДА |
| Registry | реестр upd google sheets, реестр saas подписок, doc_key find update | кейсы |
| Security | service account json не в git, обезличивание sheets, oauth scopes минимум, cursor:// oauth bug | FAQ |
| Ops | sheets_check_access, mcp logs cursor, unauthorized google mcp, 429 sheets api | troubleshooting |
| Adjacent | cursor google workspace plugins 2026, mcp cursor finansist | interlink B21 |

**SEO-вывод:** SERP по `mcp google sheets cursor` — **EN-гайды community MCP** (freema, spreadsheet-mcp, Quadratic hosted) + **новости Cursor Workspace (авг 2026)** + **баг-репорты OAuth Sheets**. Почти нет RU how-to «финансист + реестр + Cursor без копипаста». Угол КОДА: **правка управленческих реестров через MCP**, Path B как надёжный финконтур, Path A как пилот с оговорками.

---

## SERP (WebSearch Cursor, 2026-09-12)

Приоритет — живой WebSearch; `research-serp.json` (шаг 0, 2026-09-12) — URL-черновик; query `2026 2026` и смешанные сниппеты — **не копировать**.

### Primary: `mcp google sheets cursor 2026`

| # | URL | Тип | Пробел для КОДА |
| --- | --- | --- | --- |
| 1 | https://cursor.com/docs/mcp | Официальный reference | Нет реестров финотдела |
| 2 | https://cursor.com/help/customization/mcp | Help: mcp.json, OAuth, approvals, Cloud Agents MCP | Канон шагов; нет Sheets-кейса |
| 3 | https://github.com/freema/mcp-gsheets | Community MCP (SA) — Path B канон | EN; dev-фокус, не CFO |
| 4 | https://mcpservers.org/servers/freema/mcp-gsheets | Каталог + конфиг npx | Дубль README |
| 5 | https://github.com/dudegladiator/spreadsheet-mcp | Python/uv, много tools | Установка для dev |
| 6 | https://www.quadratichq.com/ai/mcp/google-sheets | Hosted MCP; тезис «нет first-party Sheets MCP» | SaaS-посредник, не SA-финконтур |
| 7 | https://composio.dev/toolkits/googlesheets | Composio OAuth | Посредник |
| 8 | https://mcpcursor.com/server/google-sheets-mcp | Каталог Cursor MCP | Тонкая карточка |

### News / official Workspace + auth bugs (авг–сен 2026)

| # | URL | Тип | Пробел |
| --- | --- | --- | --- |
| 1 | https://cursor.com/changelog/google-workspace-plugins | Changelog | **Только** Drive, Gmail, Calendar в теле; Sheets/Docs **не** детализированы |
| 2 | https://pondero.ai/news/2026-08-04-cursor-google-workspace/ | EN разбор 04.08 | Sheets capabilities в обзоре; не SA |
| 3 | https://aiinsiders.net/article/cursor-plugins-let-coding-agents-write-to-gmail-docs-sheets | EN 05.08 | Мало security/реестров |
| 4 | https://forum.cursor.com/t/google-sheet-authentication-is-broken-atm-critical/167413 | Forum 04.08 | OAuth Sheets: Local OK, Cloud/SSH — `cursor://` rejected |
| 5 | https://forum.cursor.com/t/google-workspace-plugins-oauth-fails-error-400-invalid-request-on-cursor-redirect/167402 | Forum | Workaround: cursor.com/agents Login |
| 6 | https://mayai.ru/cursor-otkryl-gmail-i-sheets-agentam/ | RU разбор | Контент-завод; мало SA/реестров |
| 7 | https://vibecoding.ru/news/2026/08/03/cursor-google-workspace-plugins | RU новость | Витрина/OAuth-баги |

### Secondary: `автоматизация финотдела` + реестры Sheets

| # | URL | Тип | Пробел |
| --- | --- | --- | --- |
| 1 | https://dzen.ru/a/aoAx4V_t_ztBh5aj | Forms→Sheets заявки | Без MCP |
| 2 | https://dzen.ru/a/anRW32ni3D3wHjQF | Реестр договоров Sheets | Без MCP |
| 3 | https://spark.ru/startup/695cee6bd9851/blog/292172/shablon-ucheta-finansov-s-kotorogo-stoit-nachinat-god-v-biznese | Шаблон учёта в Sheets | Без Cursor |
| 4 | https://koda-fd.ru/blog/ai-dlya-finansista-2026/ | Hub КОДА | Нет MCP Cursor |
| 5 | https://comandos.ai/blog/ai-finansovyi-otdel | AI-агенты финотдела | Не Cursor MCP Sheets |

### H1-aligned (RU setup)

| # | URL | Заметка |
| --- | --- | --- |
| 1 | https://mcp-catalog.ru/tutorials/gsheets-cursor | RU: freema/mcp-gsheets в Cursor |
| 2 | https://mcp-catalog.ru/tutorials/google-sheets-cursor | RU: henilcalagiya variant |
| 3 | https://neurinix.com/2026/06/21/podklyuchenie-mcp-cursor/ | Общий MCP setup RU |

### Конкурентный зазор (угол КОДА)

1. **Finance-first** — не «подключи Sheets к Cursor», а «перестань копировать реестр в чат: agent правит строку по `doc_key`».
2. **Два пути с честным выбором** — OAuth-плагин для пилота (Local + оговорка Cloud bug) vs SA+mcp-gsheets для production финконтура.
3. **Связка с реестрами серии** — договоры (B51), УПД (B58), SaaS (B83); MCP = слой правок поверх уже спроектированной таблицы.
4. **Security block** — минимальный share, ключ вне git, approval tools, indirect prompt injection, обезличивание, квота 60/user.
5. **Verify loop** — после write всегда `get_values`; «Connected ≠ authorized».
6. **Fork от B82** — B82 = свой Python-скрипт; B92 = те же SA+share, но правки через Agent+MCP без написания кода.

---

## Таблица фактов

| # | Утверждение | Источник | Дата проверки |
| --- | --- | --- | --- |
| 1 | MCP подключает Cursor к внешним инструментам; Agent вызывает tools в чате. | https://cursor.com/help/customization/mcp | 2026-09-12 |
| 2 | Конфиг: проектный `.cursor/mcp.json` + глобальный `~/.cursor/mcp.json`; при совпадении имени побеждает **проектный**. | https://cursor.com/help/customization/mcp | 2026-09-12 |
| 3 | Локальный MCP: `command`, `args`, `env`; удалённый — `url` (+ опционально `headers`). | https://cursor.com/help/customization/mcp | 2026-09-12 |
| 4 | One-click: Customize → MCPs → Add to Cursor; после ручного `mcp.json` — **перезапуск Cursor**. | https://cursor.com/help/customization/mcp | 2026-09-12 |
| 5 | По умолчанию Agent **запрашивает approval** перед MCP-tool; с Cursor 3.6+ — Auto-review / allowlist / `permissions.json`. | https://cursor.com/help/customization/mcp | 2026-09-12 |
| 6 | Troubleshooting: Output → **MCP Logs** (`Ctrl+Shift+U` / `Cmd+Shift+U`). | https://cursor.com/help/customization/mcp | 2026-09-12 |
| 7 | Cloud Agents поддерживают MCP, настроенные в Cloud Agents dashboard; Team — shared servers / Team Marketplace. | https://cursor.com/help/customization/mcp | 2026-09-12 |
| 8 | Changelog Google Workspace Plugins: в теле документа перечислены **Drive, Gmail, Calendar**; Sheets/Docs **не детализированы**. | https://cursor.com/changelog/google-workspace-plugins | 2026-09-12 |
| 9 | Анонсы/обзоры 03–05.08.2026 утверждают пять плагинов, включая Docs и Sheets (read ranges, update cells). | https://pondero.ai/news/2026-08-04-cursor-google-workspace/ ; https://aiinsiders.net/article/cursor-plugins-let-coding-agents-write-to-gmail-docs-sheets | 2026-09-12 |
| 10 | Forum 04.08.2026: OAuth Google Sheets из Marketplace — Error 400 `invalid_request` на `redirect_uri=cursor://…`; **Local** auth может пройти; **Cloud/SSH** — через https://cursor.com/agents → MCP → Login. | https://forum.cursor.com/t/google-sheet-authentication-is-broken-atm-critical/167413 ; https://forum.cursor.com/t/google-workspace-plugins-oauth-fails-error-400-invalid-request-on-cursor-redirect/167402 | 2026-09-12 |
| 11 | Quadratic (маркетинг): «No first-party Google Sheets MCP server» от Google — community/hosted обёртки вокруг Sheets API. | https://www.quadratichq.com/ai/mcp/google-sheets | 2026-09-12 |
| 12 | `freema/mcp-gsheets`: Node.js **v20+**, GCP + Sheets API + SA JSON; `npx -y mcp-gsheets@latest` + `GOOGLE_APPLICATION_CREDENTIALS` / `GOOGLE_PROJECT_ID`. | https://github.com/freema/mcp-gsheets | 2026-09-12 |
| 13 | Tools для реестра: `sheets_get_values`, `sheets_update_values`, `sheets_append_values`, `sheets_batch_get_values`, `sheets_get_metadata`, `sheets_check_access`. | https://github.com/freema/mcp-gsheets | 2026-09-12 |
| 14 | `sheets_append_values`: default `insertDataOption` = **OVERWRITE** — для реестра явно `INSERT_ROWS`, если нужно сдвигать строки. | https://github.com/freema/mcp-gsheets | 2026-09-12 |
| 15 | SA видит **только** таблицы, расшаренные на `client_email`; IAM Cloud **не заменяет** Share файла. | https://developers.google.com/workspace/guides/create-credentials#service-account | 2026-08-24 / актуально |
| 16 | Scope `https://www.googleapis.com/auth/spreadsheets` — read/write всех расшаренных таблиц SA; защита листов — ProtectedRange. | https://developers.google.com/workspace/sheets/api/scopes | 2026-08-24 / актуально |
| 17 | Sheets API: read/write **300**/мин/проект и **60**/мин/user/проект; превышение → HTTP **429**; квоты refill каждую минуту. | https://developers.google.com/workspace/sheets/api/limits | 2026-09-12 |
| 18 | Один service account = один «user» для per-user квоты: агент с частыми read/write упрётся в **60/мин** раньше, чем в 300/проект. | https://dev.to/pastesheet/google-sheets-api-rate-limits-what-60-requestsminute-actually-means-1mim | 2026-09-12 |
| 19 | Google планирует billing за превышение квот Sheets API **later in 2026** (standard use пока free). | https://developers.google.com/workspace/sheets/api/limits | 2026-09-12 |
| 20 | `dudegladiator/spreadsheet-mcp`: uv + SA; Sheets+Drive API; конфиг в `~/.cursor/mcp.json`. | https://github.com/dudegladiator/spreadsheet-mcp | 2026-09-12 |
| 21 | Риск MCP+Google: агент наследует права; в письмах/ячейках — **indirect prompt injection** → human-in-the-loop на write. | https://mayai.ru/cursor-otkryl-gmail-i-sheets-agentam/ ; https://aiinsiders.net/article/cursor-plugins-let-coding-agents-write-to-gmail-docs-sheets | 2026-09-12 |
| 22 | «Connected» в Tools & MCP **не гарантирует** успешный Google OAuth — проверять живым read/write. | Forum + mayai | 2026-09-12 |
| 23 | Локальный OAuth Path A **не переносится автоматически** на Cloud Agents; для облака — dashboard MCP / SA / auth через cursor.com/agents. | https://cursor.com/help/customization/mcp ; forum threads | 2026-09-12 |
| 24 | Заявки Forms→Sheets: при **>80–100** заявок/мес Sheets — staging перед ERP/n8n. | https://dzen.ru/a/aoAx4V_t_ztBh5aj | 2026-09-12 |
| 25 | Реестр договоров в Sheets уместен до **~200–300** активных при одном владельце; иначе CLM/1С. | https://dzen.ru/a/anRW32ni3D3wHjQF | 2026-08-24 / актуально |

**Не выдумывать:** показы Wordstat; «Sheets-плагин всегда стабилен в Marketplace»; что SA = доступ ко всему Drive; ROI из fact-bank контент-заводов; «официальный first-party Sheets MCP от Google».

**fact-bank.md:** прямых фактов про MCP+Sheets нет — опираться на таблицу выше. Контент-заводные ROI из fact-bank **не тянуть**.

---

## Структура H2 для writer (из карточки B92)

1. Когда это нужно финотделу (и когда нет)  
2. Подготовка данных и безопасность (без сырых ПДн в облако)  
3. Пошаговая настройка / сценарий (Path A vs Path B)  
4. Проверка результата и типичные ошибки (OAuth `cursor://`, 429, Connected≠auth)  
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

- **Можно ли без программиста?** — Path A (Marketplace+OAuth Local): да для пилота; Path B (SA+mcp.json): по инструкции, Cursor поможет с JSON; production — 1–2 ч первый реестр.
- **Сколько займёт внедрение?** — SA + mcp.json + один тестовый update: **~1–2 ч**; OAuth-плагин быстрее, если Local auth проходит.
- **Какие риски для данных?** — OAuth = права вашего Google; SA-ключ = все расшаренные файлы; не класть ПДн; подтверждать write-tools; indirect injection.
- **OAuth или service account?** — OAuth для личного пилота (Local); SA для командного реестра и стабильного Cloud/финконтура.
- **Чем отличается от B82?** — B82 = Python/Node скрипт пишет в staging; B92 = Agent в Cursor правит через MCP без скрипта.
- **Работает ли в Cloud Agents?** — да через dashboard MCP / Team MCP; локальный OAuth Path A не переезжает сам; для Sheets плагина Cloud — auth через cursor.com/agents.
- **Почему 429 при правках реестра?** — один SA бьёт в лимит **60 req/min/user**; batch + backoff; не поллить весь лист в цикле.

---

## CTA / interlink

- Internal: `/avtomatizaciya-finansov-no-code/`, `/obezlichivanie-dannyh-chatgpt-finansist/`, `/google-sheets-api-integraciya-finotdel/` (B82), `/mcp-cursor-finansist-instrumenty/` (B21)
- Соседние реестры: B51, B58, B83
- CTA: `https://club.koda-fd.ru/?utm_source=blog&utm_medium=article&utm_campaign=mcp-google-sheets-cursor-reestry` (≤2), `https://t.me/finance_modern?utm_source=blog&utm_medium=article` (≤2)

---

## Handoff marker

`=== EXCALIBUR BLOG RESEARCH ===` — см. `.cursor/excalibur-blog-handoff.md`
