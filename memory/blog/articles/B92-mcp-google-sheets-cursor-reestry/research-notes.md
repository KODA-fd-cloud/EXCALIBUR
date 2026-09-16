# Research notes — B92

**topic_id:** B92  
**slug:** mcp-google-sheets-cursor-reestry  
**h1:** Как подключить MCP к Google Sheets в Cursor и править реестры без копипаста  
**research_date:** 2026-09-16  
**publish_target:** koda-fd.ru/blog  
**utility_gate:** PASS (`how_to`, mode B) — подтверждено `python3 scripts/excalibur_blog_utility_gate.py --topic-id B92`  
**author_id:** olga-kondratskaya  
**related_internal:** `/avtomatizaciya-finansov-no-code/`, `/obezlichivanie-dannyh-chatgpt-finansist/`  
**sibling_queue:** B82 (Sheets API + SA), B21 (MCP в Cursor общий), B51/B58/B83 (реестры в Sheets), B93 (ротация ключа SA)  
**cover_scene_hint:** abstract holographic finance automation dark #0a0a0f purple #8b5cf6, no text  
**freshness:** prefer sources after 2026-06-18; versions checked 2026-09-16

---

## utility_verdict

**PASS** — utility-only how_to. Читатель получает рабочий маршрут: выбрать путь подключения Google Sheets к Cursor через MCP → подготовить реестр (без сырых ПДн) → настроить auth (service account **или** OAuth-плагин) → прогнать сценарий «найти строку по `doc_key` → обновить статус → перечитать» → зафиксировать регламент безопасности. Не новость «Cursor открыл Workspace», не обзор десятка MCP-серверов, не туториал «напиши свой MCP с нуля».

---

## reader_outcome

После гайда финансист сможет подключить MCP Google Sheets в Cursor, дать агенту доступ только к рабочему реестру (через service account или OAuth), попросить обновить статус/комментарий строки без копипаста таблицы в чат и проверить результат перечиткой диапазона через MCP-tool.

---

## action_outline

1. **Решить, нужен ли MCP Sheets** — реестр уже в Google Sheets (договоры, УПД, SaaS, заявки), правки повторяются, устали таскать диапазоны в чат; **не** делать, если нужен жёсткий audit trail / сотни таблиц с enterprise ACL — тогда 1С/CLM, Sheets только staging.
2. **Выбрать путь подключения (сравнение)** — **Path A (пилот):** плагин Google Sheets из Cursor Marketplace / Customize → OAuth; **Path B (финконтур, рекомендовать):** `freema/mcp-gsheets` + service account — расшарить только нужные реестры, ключ в `env`, без доступа агента ко всему Drive; **Path C (опционально, Developer Preview):** официальный remote MCP Google `https://sheetsmcp.googleapis.com/mcp/v1` (OAuth в своём GCP-проекте) — для продвинутых, не основной путь статьи.
3. **Подготовить реестр** — одна строка = одна сущность; стабильный `doc_key`; лист `staging` для импорта; в облако без сырых ПДн (ИНН/сумма/статус — да; паспорт, полные ФИО — нет); interlink `/obezlichivanie-dannyh-chatgpt-finansist/`.
4. **Path B: Google Cloud + SA** — проект → включить **Google Sheets API** → service account → JSON-ключ → скопировать `client_email` → «Поделиться» на файл реестра с ролью **Редактор** (без «Уведомить»).
5. **Path B: mcp.json в Cursor** — глобально `~/.cursor/mcp.json` или проектно `.cursor/mcp.json`; блок `mcp-gsheets` с `npx -y mcp-gsheets@latest` и `GOOGLE_APPLICATION_CREDENTIALS` (абсолютный путь); JSON-ключ **не** в git.
6. **Path A: Marketplace / OAuth** — Customize → MCPs → Google Sheets → Add → OAuth; если IDE даёт Error 400 на `cursor://` — логин через https://cursor.com/agents → MCP Servers → Login (известный баг OAuth, сентябрь 2026); Local auth часто работает, Cloud/SSH — нет без обхода.
7. **Проверить подключение** — перезапуск Cursor после ручного `mcp.json`; Customize → MCPs → статус; Output → **MCP Logs**; Path B: tool `sheets_check_access` + «прочитай A1:C5 листа Реестр».
8. **Рабочий сценарий реестра** — промпт с DoD: metadata/доступ → найти строку по `doc_key` → update/append только в колонки статуса/комментария → перечитка той же строки → сверка; human approval на каждый write-tool.
9. **Эксплуатация и рост** — allowlist write-tools; ротация ключа SA (B93); при >80–100 заявок/мес или audit — n8n/ERP, Sheets остаётся staging; соседние реестры B51/B58/B83.

**Workflow для статьи:**  
`Реестр в Sheets → (SA share | OAuth plugin) → MCP в Cursor → Agent read/update по doc_key → перечитка диапазона → регламент CFO`

---

## Яндекс Wordstat (MCP user-mcp-kv)

⚠️ **WORDSTAT AUTH WARNING / MCP UNAVAILABLE:** сервер MCP `user-mcp-kv` в этой Cloud-сессии **не подключён** (в каталоге dynamic tools: `cursor`, `Cursor Automation Tools`, `cursor-cloud`, `cursor-subscriptions`). Вызов `wordstat_get_top_requests` **не выполнен**. Точные показы/мес **не получены** и **не выдуманы**.

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
| Official | sheetsmcp.googleapis.com, google sheets mcp server | FAQ / Path C |
| Finance | автоматизация финотдела google sheets, реестр договоров cursor, править реестр без копипаста | угол КОДА |
| Registry | реестр upd google sheets, реестр saas подписок, doc_key find update | кейсы |
| Security | service account json не в git, обезличивание sheets, oauth scopes минимум, indirect prompt injection | FAQ |
| Ops | sheets_check_access, mcp logs cursor, google oauth error 400 cursor | troubleshooting |
| Adjacent | cursor google workspace plugins 2026, mcp cursor finansist | interlink B21 |

**SEO-вывод:** SERP по `mcp google sheets cursor` — EN community MCP (freema, we2go, spreadsheet-mcp), официальная дока Google remote MCP (сент. 2026), новости Cursor Workspace (авг. 2026) и баги OAuth. Почти нет RU how-to «финансист + реестр + Cursor без копипаста». Угол КОДА: **правка управленческих реестров через MCP**, с веткой SA для безопасности и сравнением с B82 (скрипт) / B21 (общий MCP).

---

## SERP (WebSearch Cursor, 16.09.2026)

Приоритет — живой WebSearch; `research-serp.json` (шаг 0) — черновик URL; query `2026 2026` **игнорировать**; сниппеты иногда перепутаны между URL.

### Primary: `mcp google sheets cursor 2026`

| # | URL | Тип | Пробел для КОДА |
| --- | --- | --- | --- |
| 1 | https://developers.google.com/workspace/sheets/api/guides/configure-mcp-server | Official remote Sheets MCP (Developer Preview) | Нет реестров финотдела; примеры Antigravity/Claude |
| 2 | https://github.com/we2go/google-mcp | Community: wizard SA/OAuth, `npx google-sheet-mcp` | EN; не CFO |
| 3 | https://github.com/freema/mcp-gsheets | Community SA MCP (Node 20+) | EN; лучший Path B |
| 4 | https://github.com/dudegladiator/spreadsheet-mcp | Python/uv, 27 tools | Dev-установка |
| 5 | https://cursor.com/docs/mcp | Официальный reference Cursor MCP | Нет Sheets-кейса |
| 6 | https://cursor.com/help/customization/mcp | Help: mcp.json, approvals, MCP Logs | Канон шагов |
| 7 | https://forum.cursor.com/t/google-sheet-authentication-is-broken-atm-critical/167413 | Bug: OAuth Error 400 | Troubleshooting Path A |
| 8 | https://pastesheet.com/guides/google-sheets-mcp-cursor | Hosted/community guide | Не SA-финконтур |

### News / Workspace / OAuth (авг–сент 2026)

| # | URL | Тип | Пробел |
| --- | --- | --- | --- |
| 1 | https://cursor.com/changelog/google-workspace-plugins | Changelog 03.08.2026 | Drive/Gmail/Calendar детально |
| 2 | https://mayai.ru/cursor-otkryl-gmail-i-sheets-agentam/ | RU разбор | Мало SA/реестров |
| 3 | https://vibecoding.ru/news/2026/08/03/cursor-google-workspace-plugins | RU новость | Витрина/OAuth `cursor://` |
| 4 | https://forum.cursor.com/t/google-plugins-broken-auth-2-0/167780 | Forum: workaround cursor.com/agents | Актуально на сент. 2026 |

### Secondary: автоматизация финотдела / реестры

| # | URL | Тип | Пробел |
| --- | --- | --- | --- |
| 1 | https://koda-fd.ru/blog/ai-dlya-finansista-2026/ | Hub КОДА | Нет MCP Cursor |
| 2 | https://datalopata.ru/blog/avtomatizatsija-finansov-sistemnyj-podhod-k-uchetu-v-2026-godu/ | Приоритеты 2026 | ERP-уклон |
| 3 | https://mcp-catalog.ru/tutorials/gsheets-cursor | RU: freema в Cursor | Нет finance DoD |
| 4 | https://mcp-catalog.ru/tutorials/google-sheets-cursor | RU: henilcalagiya | Альтернатива |
| 5 | https://neurinix.com/2026/06/21/podklyuchenie-mcp-cursor/ | Общий MCP RU | Без Sheets-реестра |

### Конкурентный зазор (угол КОДА)

1. **Finance-first** — не «подключи Sheets к Cursor», а «перестань копировать реестр в чат: agent правит строку по `doc_key`».
2. **Три пути с честным выбором** — OAuth-плагин (пилот, баги auth) vs SA+mcp-gsheets (production финконтур) vs official remote MCP Google (Developer Preview).
3. **Связка с реестрами серии** — договоры (B51), УПД (B58), SaaS (B83); MCP = слой правок поверх таблицы.
4. **Security** — минимальный share, ключ вне git, approval tools, indirect prompt injection (Google docs), обезличивание.
5. **Verify loop** — после write всегда get_values; «Connected ≠ authorized».
6. **Fork от B82** — B82 = свой скрипт; B92 = те же SA+share, правки через Agent+MCP без кода.

---

## Таблица фактов

| # | Утверждение | Источник | Дата проверки |
| --- | --- | --- | --- |
| 1 | MCP подключает Cursor к внешним инструментам; Agent вызывает tools в чате. | https://cursor.com/help/customization/mcp | 2026-09-16 |
| 2 | Конфиг: проектный `.cursor/mcp.json` + глобальный `~/.cursor/mcp.json`; при совпадении имени побеждает **проектный**. | https://cursor.com/help/customization/mcp | 2026-09-16 |
| 3 | Локальный MCP: `command`/`args`/`env`; удалённый — поле `url` (+ опционально `headers`). | https://cursor.com/help/customization/mcp | 2026-09-16 |
| 4 | One-click: Customize → MCPs → Add to Cursor; после ручного `mcp.json` — **перезапуск Cursor**. | https://cursor.com/help/customization/mcp | 2026-09-16 |
| 5 | По умолчанию Agent **запрашивает approval** перед MCP-tool; в Cursor 3.6+ — Auto-review / allowlist / `permissions.json`. | https://cursor.com/help/customization/mcp | 2026-09-16 |
| 6 | Troubleshooting: Output → **MCP Logs** (`Ctrl+Shift+U` / `Cmd+Shift+U`). | https://cursor.com/help/customization/mcp | 2026-09-16 |
| 7 | Cloud Agents поддерживают MCP из Cloud Agents dashboard / Team Integrations & MCP — не наследуют локальный интерактивный OAuth автоматически. | https://cursor.com/help/customization/mcp | 2026-09-16 |
| 8 | Google предлагает **remote** Sheets MCP (Developer Preview): URL `https://sheetsmcp.googleapis.com/mcp/v1`, transport Streamable HTTP, auth OAuth 2.0. | https://developers.google.com/workspace/sheets/api/guides/configure-mcp-server | 2026-09-16 (док. updated 2026-09-14) |
| 9 | Для official MCP нужно enable `sheets.googleapis.com` и `sheetsmcp.googleapis.com` в GCP-проекте. | https://developers.google.com/workspace/sheets/api/guides/configure-mcp-server | 2026-09-16 |
| 10 | Tools official Sheets MCP: `get_values`, `get_spreadsheet`, `update_spreadsheet`, `update_values`, `update_formulas`, `insert_dimension`. | https://developers.google.com/workspace/sheets/api/guides/configure-mcp-server | 2026-09-16 |
| 11 | OAuth scopes для official Sheets MCP включают drive.readonly, drive.file, spreadsheets.readonly, spreadsheets. | https://developers.google.com/workspace/sheets/api/guides/configure-mcp-server | 2026-09-16 |
| 12 | Google прямо предупреждает про **indirect prompt injection** при MCP+Sheets: агент может читать/менять/удалять данные; нужен review действий. | https://developers.google.com/workspace/sheets/api/guides/configure-mcp-server | 2026-09-16 |
| 13 | Квоты Sheets API / Sheets MCP: read **300**/мин/проект и **60**/мин/user; write те же; превышение → HTTP **429**. | https://developers.google.com/workspace/sheets/api/limits | 2026-09-16 (updated 2026-09-03) |
| 14 | Batch request (включая subrequests) считается **одним** API request к квоте. | https://developers.google.com/workspace/sheets/api/limits | 2026-09-16 |
| 15 | Превышение quota request limits планируется тарифицироваться в Google Cloud **later in 2026** (стандартная модель agent tools). | https://developers.google.com/workspace/sheets/api/limits | 2026-09-16 |
| 16 | `freema/mcp-gsheets`: Node.js **v20+**; Cursor config `npx -y mcp-gsheets@latest` + `GOOGLE_PROJECT_ID` + `GOOGLE_APPLICATION_CREDENTIALS` (абсолютный путь). | https://github.com/freema/mcp-gsheets | 2026-09-16 |
| 17 | Ключевые tools mcp-gsheets для реестра: `sheets_get_values`, `sheets_update_values`, `sheets_append_values`, `sheets_batch_get_values`, `sheets_get_metadata`, `sheets_check_access`. | https://github.com/freema/mcp-gsheets | 2026-09-16 |
| 18 | `sheets_append_values`: default `insertDataOption` = **OVERWRITE** — для реестра явно указывать `INSERT_ROWS`, если нужно сдвигать строки. | https://github.com/freema/mcp-gsheets | 2026-09-16 |
| 19 | npm-пакет `mcp-gsheets` (пример версии в CDN: **1.10.2**) — ориентир актуальности community-сервера. | https://cdn.jsdelivr.net/npm/mcp-gsheets@1.10.2/README.md | 2026-09-16 |
| 20 | `we2go/google-mcp`: `npx google-sheet-mcp init` (SA) или `init --auth oauth`; генерирует `.cursor/mcp.json`; tools `sheets_read_range`, `sheets_update_range` / `sheets_write_range`, `sheets_append_row`. | https://github.com/we2go/google-mcp | 2026-09-16 |
| 21 | Service account видит **только** таблицы, расшаренные на `client_email`; IAM Cloud **не заменяет** Share файла. | https://developers.google.com/workspace/guides/create-credentials#service-account | 2026-09-16 |
| 22 | Scope `https://www.googleapis.com/auth/spreadsheets` — read/write расшаренных таблиц; применяется к **файлу**; листы — ProtectedRange. | https://developers.google.com/workspace/sheets/api/scopes | 2026-09-16 |
| 23 | 03.08.2026 Cursor анонсировал Google Workspace plugins (агенты в Drive/Gmail/Calendar без выхода из редактора). | https://cursor.com/changelog/google-workspace-plugins | 2026-09-16 |
| 24 | На форуме Cursor (сент. 2026): Google Sheets/Workspace OAuth из IDE ломается (Error 400, `cursor://` redirect); Local auth может работать; Cloud — логин через https://cursor.com/agents → MCP Servers → Login. | https://forum.cursor.com/t/google-sheet-authentication-is-broken-atm-critical/167413 ; https://forum.cursor.com/t/google-plugins-broken-auth-2-0/167780 | 2026-09-16 |
| 25 | В 2026 финотдел автоматизирует классификацию платежей, сверки, управленческую отчётность — Sheets+MCP = **transport правок**, не GL. | https://koda-fd.ru/blog/ai-dlya-finansista-2026/ | 2026-09-16 |

**Не выдумывать:** показы Wordstat; что Marketplace Sheets «всегда стабильно работает» (проверять OAuth на дату публикации); что SA = доступ ко всему Drive; цифры installs Smithery без верификации; обещание «без программиста» для Path B без упоминания GCP/SA; что official remote MCP — «кнопка в Cursor» без GCP OAuth client.

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

## FAQ-кандидаты (из карточки)

- **Можно ли без программиста?** — Path A (Marketplace+OAuth): да для пилота, если auth проходит; Path B (SA+mcp.json): по инструкции B82/B92, Cursor поможет с JSON; первый реестр ~1–2 ч.
- **Сколько займёт внедрение?** — SA + mcp.json + один тестовый update: **~1–2 ч**; OAuth-плагин быстрее *если* витрина и OAuth живы.
- **Какие риски для данных?** — OAuth = права вашего Google; SA-ключ = все расшаренные файлы; не класть ПДн; подтверждать write-tools; indirect injection из ячеек/писем.
- **OAuth или service account?** — OAuth для личного пилота; SA для командного реестра и минимального blast radius (рекомендация КОДА).
- **Чем отличается от B82?** — B82 = Python/Node скрипт пишет в staging; B92 = Agent в Cursor правит через MCP без скрипта.
- **Работает ли в Cloud Agents?** — локальный OAuth не переезжает автоматически; Team MCP / SA отдельно; известны баги Google OAuth в IDE.
- **Что такое official Sheets MCP Google?** — remote `sheetsmcp.googleapis.com` (Developer Preview); для статьи — FAQ/сравнение, не основной путь финконтура.

---

## CTA / interlink

- Internal: `/avtomatizaciya-finansov-no-code/`, `/obezlichivanie-dannyh-chatgpt-finansist/`, `/google-sheets-api-integraciya-finotdel/` (B82), `/mcp-cursor-finansist-instrumenty/` (B21)
- Соседние реестры: B51, B58, B83; ротация ключа: B93
- CTA: `https://club.koda-fd.ru/?utm_source=blog&utm_medium=article&utm_campaign=mcp-google-sheets-cursor-reestry` (≤2), `https://t.me/finance_modern?utm_source=blog&utm_medium=article` (≤2)

---

## Handoff marker

`=== EXCALIBUR BLOG RESEARCH ===` — см. `.cursor/excalibur-blog-handoff.md`
