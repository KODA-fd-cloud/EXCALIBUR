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

**PASS** — тема utility-only how_to. Читатель получает выбор пути (OAuth-плагин Marketplace **или** community `mcp-gsheets` / аналог на service account), подготовку реестра под агентные правки, тест «найти строку по `doc_key` → обновить статус → перечитать», чеклист безопасности и troubleshooting OAuth/`cursor://`. Не новость «Cursor открыл Workspace», не обзор 25 MCP-серверов, не туториал «напиши свой MCP с нуля».

---

## reader_outcome

После гайда финансист сможет подключить MCP Google Sheets в Cursor, дать агенту доступ только к рабочему реестру (через service account или OAuth-плагин), попросить обновить статус строки или дописать поля без копирования таблицы в чат и проверить результат перечиткой диапазона через MCP-tool.

---

## action_outline

1. **Решить, нужен ли MCP Sheets** — реестр уже в Google Sheets (договоры, УПД, SaaS, заявки), правки повторяются, устали таскать диапазоны в чат; **не** делать, если нужен жёсткий audit trail / сотни таблиц с enterprise ACL — тогда 1С/CLM, Sheets только staging.
2. **Выбрать путь подключения** — **Path A (пилот):** плагин Google Sheets из Cursor Marketplace / Customize → OAuth; **Path B (финконтур):** `freema/mcp-gsheets` (или `we2go/google-mcp`) + service account — расшарить только нужные реестры, ключ в `env`, без доступа агента ко всему Drive (см. B82, B93).
3. **Подготовить реестр** — одна строка = одна сущность; стабильный `doc_key`; лист `staging` для импорта; в облако без сырых ПДн (ИНН/сумма/статус — да; паспорт, полные ФИО — нет); interlink `/obezlichivanie-dannyh-chatgpt-finansist/`.
4. **Path B: Google Cloud + SA** — проект → включить **Google Sheets API** → service account → JSON-ключ → скопировать `client_email` → «Поделиться» на файл реестра с ролью **Редактор** (без «Уведомить»).
5. **Path B: mcp.json в Cursor** — глобально `~/.cursor/mcp.json` или проектно `.cursor/mcp.json`; блок `mcp-gsheets` с `npx -y mcp-gsheets@latest` и `GOOGLE_APPLICATION_CREDENTIALS` (абсолютный путь); JSON-ключ **не** в git.
6. **Path A: Marketplace** — Customize → MCPs / Marketplace → Google Sheets → Add → OAuth; минимальные scopes; на 2026-09-04 учитывать: официальный changelog 03.08.2026 детально описывает только Drive/Gmail/Calendar; Sheets в анонсах/форуме есть, но OAuth с `cursor://` часто ломается — fallback: Login через https://cursor.com/agents или сразу Path B.
7. **Проверить подключение** — перезапуск Cursor; Customize → MCPs → зелёный статус; Output → **MCP Logs**; tool `sheets_check_access` (Path B) или живой запрос «прочитай A1:C5 листа Реестр».
8. **Рабочий сценарий реестра** — промпт с DoD: metadata → найти строку по `doc_key` → update/append только колонки статуса/комментария → get_values на ту же строку → сверка; human approval на каждый write-tool.
9. **Эксплуатация и рост** — allowlist write-tools; ротация ключа SA (B93); при >80–100 заявок/мес или audit — n8n/ERP, Sheets остаётся staging; соседние реестры B51/B58/B83.

**Workflow для статьи:**  
`Реестр в Sheets → (SA share | OAuth plugin) → MCP в Cursor → Agent read/update по doc_key → перечитка диапазона → регламент CFO`

---

## Яндекс Wordstat (MCP user-mcp-kv)

⚠️ **WORDSTAT AUTH WARNING:** сервер MCP `user-mcp-kv` в этой Cloud-сессии **не подключён** (в каталоге dynamic tools доступны только `Cursor Automation Tools`, `cursor`, `cursor-cloud`, `cursor-subscriptions`). Вызов `wordstat_get_top_requests` **не выполнен**. Точные показы/мес **не получены** и **не выдуманы**.

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
| Ops | sheets_check_access, mcp logs cursor, unauthorized google mcp, cursor:// oauth | troubleshooting |
| Adjacent | cursor google workspace plugins 2026, mcp cursor finansist | interlink B21 |

**SEO-вывод:** SERP по `mcp google sheets cursor` на 2026-09-04 — **EN how-to community MCP** (freema, we2go, spreadsheet-mcp, Composio) + **новости Workspace-плагинов августа 2026** + **форумные баги OAuth**. Почти нет RU how-to «финансист + реестр + Cursor без копипаста». Угол КОДА: **правка управленческих реестров через MCP**, с веткой SA для безопасности и честным note про статус Marketplace Sheets / OAuth.

---

## SERP (WebSearch Cursor, 04.09.2026)

Приоритет — живой WebSearch; `research-serp.json` (шаг 0, 2026-09-04) использован как URL-черновик; query `2026 2026` и часть сниппетов **нерелевантны** — не копировать.

### Primary: `mcp google sheets cursor 2026`

| # | URL | Тип | Пробел для КОДА |
| --- | --- | --- | --- |
| 1 | https://cursor.com/help/customization/mcp | Официальный help | Канон mcp.json / approvals; нет Sheets-кейса |
| 2 | https://cursor.com/docs/mcp | Official reference | Общий MCP |
| 3 | https://github.com/freema/mcp-gsheets | Community MCP (SA) | EN; dev-фокус, не CFO |
| 4 | https://github.com/we2go/google-mcp | npx wizard OAuth/SA | Sheets+Docs; не реестры |
| 5 | https://github.com/dudegladiator/spreadsheet-mcp | Python/uv, 27 tools | Установка для dev |
| 6 | https://composio.dev/toolkits/googlesheets/framework/cursor | Composio OAuth (обновл. 03.09.2026) | SaaS-посредник |
| 7 | https://mcp-catalog.ru/tutorials/google-sheets-cursor | RU: henilcalagiya variant | Нет finance-угла |
| 8 | https://pastesheet.com/guides/google-sheets-mcp-cursor | Hosted URL MCP | Публичные/hosted; не SA финконтур |

### News / official Workspace + OAuth status (авг–сен 2026)

| # | URL | Тип | Пробел / вывод |
| --- | --- | --- | --- |
| 1 | https://cursor.com/changelog/google-workspace-plugins | Changelog 03.08.2026 | В тексте **только** Drive, Gmail, Calendar — Sheets/Docs **не расписаны** |
| 2 | https://forum.cursor.com/t/google-sheet-authentication-is-broken-atm-critical/167413 | Forum 04.08.2026 | Sheets в Marketplace есть; Cloud/SSH OAuth ломается; workaround cursor.com/agents |
| 3 | https://forum.cursor.com/t/google-plugins-broken-auth-2-0/167780 | Forum 08–11.08.2026 | Google отклоняет `cursor://` redirect (Error 400) |
| 4 | https://forum.cursor.com/t/google-auth-on-cursor/169817 | Forum 28–30.08.2026 | Фиксы Google auth ожидаются в Cursor **3.19** |
| 5 | https://mayai.ru/cursor-otkryl-gmail-i-sheets-agentam/ | RU разбор релиза | Контент-завод; мало SA/реестров |
| 6 | https://authorityaitools.com/blog/cursor-google-workspace-plugins-august-2026 | EN анонс | Перечисляет Sheets/Docs/Chat шире официального changelog |

### Secondary: `автоматизация финотдела` / реестры Sheets

| # | URL | Тип | Пробел |
| --- | --- | --- | --- |
| 1 | https://koda-fd.ru/blog/ai-dlya-finansista-2026/ | Hub КОДА | Нет MCP Cursor |
| 2 | https://dzen.ru/a/aoAx4V_t_ztBh5aj | Заявки Forms→Sheets | Порог 80–100/мес; без MCP |
| 3 | https://dzen.ru/a/anAvymtbQE6qYcKj | Выписка → Sheets | Без MCP |
| 4 | https://habr.com/ru/articles/1017260/ | AI-агенты + Sheets API | Verify-after-write; не Cursor MCP how-to |
| 5 | https://stepper.io/blog/google-sheet-update/ | Update pattern 2026 | doc_key upsert; не Cursor |

### Конкурентный зазор (угол КОДА)

1. **Finance-first** — не «подключи Sheets к Cursor», а «перестань копировать реестр в чат: agent правит строку по `doc_key`».
2. **Два пути с выбором** — OAuth-плагин для пилота vs SA+mcp-gsheets для production финконтура + honest note: OAuth/`cursor://` нестабилен на сентябрь 2026 → Path B надёжнее для CFO.
3. **Связка с реестрами серии** — договоры (B51), УПД (B58), SaaS (B83); MCP = слой правок поверх уже спроектированной таблицы.
4. **Security block** — минимальный share, ключ вне git, approval tools, indirect prompt injection, обезличивание.
5. **Verify loop** — после write всегда get_values; «Connected ≠ authorized».
6. **Fork от B82** — B82 = свой скрипт; B92 = те же SA+share, но правки через Agent+MCP без кода.

---

## Таблица фактов

| # | Утверждение | Источник | Дата проверки |
| --- | --- | --- | --- |
| 1 | MCP подключает Cursor к внешним инструментам; Agent вызывает tools в чате. | https://cursor.com/help/customization/mcp | 2026-09-04 |
| 2 | Конфиг: проектный `.cursor/mcp.json` + глобальный `~/.cursor/mcp.json`; при совпадении имени побеждает **проектный**. | https://cursor.com/help/customization/mcp | 2026-09-04 |
| 3 | Локальный MCP: `command`/`args`/`env`; удалённый — `url` (+ опционально `headers`). | https://cursor.com/help/customization/mcp | 2026-09-04 |
| 4 | One-click: Customize → MCPs → Add to Cursor; после ручного `mcp.json` — **перезапуск Cursor**. | https://cursor.com/help/customization/mcp | 2026-09-04 |
| 5 | По умолчанию Agent **запрашивает approval** перед MCP-tool; с Cursor 3.6+ — Auto-review / allowlist (`permissions.json`). | https://cursor.com/help/customization/mcp | 2026-09-04 |
| 6 | Troubleshooting: Output → **MCP Logs** (`Ctrl+Shift+U` / `Cmd+Shift+U`). | https://cursor.com/help/customization/mcp | 2026-09-04 |
| 7 | Cloud Agents: MCP настраиваются в Cloud Agents dashboard / Team Integrations & MCP — **не** наследуют локальный интерактивный OAuth автоматически. | https://cursor.com/help/customization/mcp | 2026-09-04 |
| 8 | Changelog 03.08.2026: официально перечислены плагины **Drive, Gmail, Calendar**; Sheets/Docs в этом документе **не детализированы**. | https://cursor.com/changelog/google-workspace-plugins | 2026-09-04 |
| 9 | На форуме Cursor (04.08.2026) Google Sheets из Marketplace существует; OAuth для Cloud/SSH падает из‑за redirect, который Google отклоняет; Local может работать. | https://forum.cursor.com/t/google-sheet-authentication-is-broken-atm-critical/167413 | 2026-09-04 |
| 10 | Workaround OAuth: Login Google-плагинов через https://cursor.com/agents → MCP Servers (https-callback), а не из IDE (`cursor://`). | https://forum.cursor.com/t/google-plugins-broken-auth-2-0/167780 | 2026-09-04 |
| 11 | Доп. фиксы Google auth в Cursor ожидаются в релизе **3.19** (сообщение staff 30.08.2026). | https://forum.cursor.com/t/google-auth-on-cursor/169817 | 2026-09-04 |
| 12 | `freema/mcp-gsheets`: Node.js **v20+**, GCP + Sheets API + SA JSON; Cursor: `npx -y mcp-gsheets@latest` + `GOOGLE_APPLICATION_CREDENTIALS`. | https://github.com/freema/mcp-gsheets | 2026-09-04 |
| 13 | Ключевые tools mcp-gsheets для реестра: `sheets_get_values`, `sheets_update_values`, `sheets_append_values`, `sheets_batch_get_values`, `sheets_get_metadata`, `sheets_check_access`. | https://github.com/freema/mcp-gsheets | 2026-09-04 |
| 14 | `sheets_append_values`: default `insertDataOption` = **OVERWRITE** — для реестра явно указывать `INSERT_ROWS`, если нужно сдвигать строки. | https://github.com/freema/mcp-gsheets | 2026-09-04 |
| 15 | SA видит **только** таблицы, расшаренные на `client_email`; IAM Cloud **не заменяет** Share файла. | https://developers.google.com/workspace/guides/create-credentials#service-account | 2026-09-04 |
| 16 | Sheets API: **300** read и **300** write req/min на проект; **60**/min на user/project; превышение → HTTP **429**; batch = один запрос. | https://developers.google.com/workspace/sheets/api/limits | 2026-09-04 |
| 17 | Google документирует отдельный **Sheets MCP server** (`sheetsmcp.googleapis.com`) с tools `get_values`, `update_values` и т.п. (квоты те же 300/60). | https://developers.google.com/workspace/sheets/api/limits | 2026-09-04 |
| 18 | Превышение quota Sheets API планируется тарифицироваться в Google Cloud **later in 2026** (стандартная модель agent tools). | https://developers.google.com/workspace/sheets/api/limits | 2026-09-04 |
| 19 | `we2go/google-mcp`: `npx google-mcp` / `init` wizard SA или OAuth; tools `sheets_read_range`, `sheets_write_range`, `sheets_append_row`. | https://github.com/we2go/google-mcp | 2026-09-04 |
| 20 | Composio: hosted MCP URL в `mcp.json` для Google Sheets ↔ Cursor (страница обновлена 03.09.2026). | https://composio.dev/toolkits/googlesheets/framework/cursor | 2026-09-04 |
| 21 | Риск MCP+Google: агент наследует права аккаунта; в письмах/ячейках возможна **indirect prompt injection** — human-in-the-loop на write. | https://mayai.ru/cursor-otkryl-gmail-i-sheets-agentam/ | 2026-09-04 |
| 22 | «Connected» ≠ успешный OAuth — проверять живым read/write. | https://mayai.ru/cursor-otkryl-gmail-i-sheets-agentam/ ; forum Cursor | 2026-09-04 |
| 23 | Заявки на расход Forms→Sheets: при **>80–100** заявок/мес Sheets — staging перед ERP/n8n. | https://dzen.ru/a/aoAx4V_t_ztBh5aj | 2026-09-04 |
| 24 | Практический паттерн агентов со Sheets API: после записи **перечитать и сверить** (verify loop). | https://habr.com/ru/articles/1017260/ | 2026-09-04 |
| 25 | Scope spreadsheets = read/write всех расшаренных таблиц SA; применяется ко **всему файлу**. | https://developers.google.com/workspace/sheets/api/scopes | 2026-09-04 |

**Не выдумывать:** показы Wordstat; «Sheets-плагин всегда стабилен в Marketplace»; что SA = доступ ко всему Drive; ROI из fact-bank; обещание «без программиста» для Path B без GCP/SA; что официальный changelog гарантирует Sheets наравне с Drive/Gmail/Calendar.

**fact-bank.md:** прямых фактов про MCP+Sheets нет — опираться на таблицу выше. Контент-заводные ROI **не тянуть**.

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

**Заметка writer (re-fit):** предыдущий `article.html` ~10889 символов — целевой диапазон **8500–9500**; усилить Path B как production-default из‑за OAuth-багов; Path A — пилот с disclaimer.

---

## FAQ-кандидаты (из карточки)

- **Можно ли без программиста?** — Path A (Marketplace+OAuth): да для пилота, если OAuth проходит; Path B (SA+mcp.json): по инструкции B82/B92, Cursor поможет с JSON; production — 1–2 ч первый реестр.
- **Сколько займёт внедрение?** — SA + mcp.json + один тестовый update: **~1–2 ч**; OAuth-плагин быстрее *если* auth работает.
- **Какие риски для данных?** — OAuth = права вашего Google; SA-ключ = все расшаренные файлы; не класть ПДн; подтверждать write-tools; indirect injection.
- **OAuth или service account?** — OAuth для личного пилота; SA для командного реестра и минимального blast radius; на 2026-09-04 SA предпочтительнее из‑за нестабильного OAuth.
- **Чем отличается от B82?** — B82 = Python/Node скрипт пишет в staging; B92 = Agent в Cursor правит через MCP без скрипта.
- **Работает ли в Cloud Agents?** — локальный OAuth не переезжает автоматически; dashboard MCP / SA; Auth через cursor.com/agents.

---

## CTA / interlink

- Internal: `/avtomatizaciya-finansov-no-code/`, `/obezlichivanie-dannyh-chatgpt-finansist/`, `/google-sheets-api-integraciya-finotdel/` (B82), `/mcp-cursor-finansist-instrumenty/` (B21)
- Соседние реестры: B51, B58, B83; ротация ключа: B93
- CTA: `https://club.koda-fd.ru/?utm_source=blog&utm_medium=article&utm_campaign=mcp-google-sheets-cursor-reestry` (≤2), `https://t.me/finance_modern?utm_source=blog&utm_medium=article` (≤2)

---

## Handoff marker

`=== EXCALIBUR BLOG RESEARCH ===` — см. `.cursor/excalibur-blog-handoff.md`
