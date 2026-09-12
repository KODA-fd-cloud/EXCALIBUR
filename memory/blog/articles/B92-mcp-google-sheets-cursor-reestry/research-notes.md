# Research notes — B92

**topic_id:** B92  
**slug:** mcp-google-sheets-cursor-reestry  
**h1:** Как подключить MCP к Google Sheets в Cursor и править реестры без копипаста  
**research_date:** 2026-09-12  
**run_date:** 2026-09-12 (Europe/Moscow)  
**publish_target:** koda-fd.ru/blog  
**utility_gate:** PASS (`how_to`, mode B)  
**author_id:** olga-kondratskaya  
**related_internal:** `/avtomatizaciya-finansov-no-code/`, `/obezlichivanie-dannyh-chatgpt-finansist/`  
**sibling_queue:** B82 (Sheets API + SA), B21 (MCP в Cursor общий), B51/B58/B83 (реестры в Sheets), B93 (ротация SA)  
**cover_scene_hint:** abstract holographic finance automation dark #0a0a0f purple #8b5cf6, no text  
**freshness_window:** prefer sources after 2026-06-14

---

## utility_verdict

**PASS** — тема utility-only how_to. Читатель получает практический выбор пути подключения Google Sheets к Cursor через MCP (Marketplace/OAuth-плагин **или** community `mcp-gsheets` на service account **или** официальный remote Sheets MCP Google), подготовку реестра под агентные правки, тестовый сценарий «найти строку → обновить статус → перечитать», чеклист безопасности для финданных и troubleshooting. Не новость «Cursor открыл Workspace», не обзор 25 MCP-серверов, не туториал «напиши свой MCP с нуля».

---

## reader_outcome

После гайда финансист сможет подключить MCP Google Sheets в Cursor, дать агенту доступ только к рабочему реестру (через service account или OAuth), попросить обновить статус строки или дописать поля без копирования таблицы в чат и проверить результат перечиткой диапазона через MCP-tool.

---

## action_outline

1. **Решить, нужен ли MCP Sheets** — реестр уже в Google Sheets (договоры, УПД, SaaS, заявки на расход), правки повторяются, устали таскать диапазоны в чат; **не** делать, если нужен жёсткий audit trail / сотни таблиц с enterprise ACL — тогда 1С/CLM, Sheets только staging.
2. **Выбрать путь подключения** — **Path A (быстрый пилот):** плагин `google-sheets` из Cursor Marketplace / Customize → OAuth личного Google (если карточка в витрине); **Path B (финконтур):** `freema/mcp-gsheets` + service account — расшарить только нужные реестры, ключ в `env`, без доступа агента ко всему Drive; **Path C (официальный remote Google):** `https://sheetsmcp.googleapis.com/mcp/v1` (Developer Preview) — OAuth + enable `sheetsmcp.googleapis.com`.
3. **Подготовить реестр** — одна строка = одна сущность; стабильный `doc_key`; лист `staging` для импорта; в облако без сырых ПДн (ИНН/сумма/статус — да; паспорт, полные ФИО — нет); interlink `/obezlichivanie-dannyh-chatgpt-finansist/`.
4. **Path B: Google Cloud + SA** — проект → включить **Google Sheets API** → service account → JSON-ключ → скопировать `client_email` → «Поделиться» на файл реестра с ролью **Редактор** (без «Уведомить»).
5. **Path B: mcp.json в Cursor** — глобально `~/.cursor/mcp.json` или проектно `.cursor/mcp.json`; блок `mcp-gsheets` с `npx -y mcp-gsheets@latest` и `GOOGLE_APPLICATION_CREDENTIALS` (абсолютный путь); JSON-ключ **не** в git.
6. **Path A / C: Marketplace или remote URL** — Customize → MCPs → Add / или `url` + OAuth; минимальные scopes; учесть, что в changelog 03.08.2026 детально описаны Drive/Gmail/Calendar, а Sheets/Docs в теле changelog не расписаны; 04.08.2026 Docs/Sheets временно убирали из витрины — проверять наличие на дату публикации.
7. **Проверить подключение** — перезапуск Cursor; Customize → MCPs → статус; Output → **MCP Logs**; tool `sheets_check_access` (Path B) или живой запрос «прочитай A1:C5 листа Реестр» / `get_values` (Path C).
8. **Рабочий сценарий реестра** — промпт с DoD: metadata/get → найти строку по `doc_key` → update/append только в колонки статуса/комментария → get_values на ту же строку → сверка; human approval на каждый write-tool.
9. **Эксплуатация и рост** — allowlist write-tools; ротация ключа SA (B93); при >80–100 заявок/мес или audit — n8n/ERP, Sheets остаётся staging; соседние реестры B51/B58/B83.

**Workflow для статьи:**  
`Реестр в Sheets → (SA share | OAuth plugin | Google remote MCP) → MCP в Cursor → Agent read/update по doc_key → перечитка диапазона → регламент CFO`

---

## Яндекс Wordstat (MCP user-mcp-kv)

⚠️ **WORDSTAT AUTH WARNING:** сервер MCP `user-mcp-kv` в этой Cloud-сессии **не подключён** (в каталоге dynamic tools: `cursor`, `Cursor Automation Tools`, `cursor-cloud`, `cursor-subscriptions`). Вызов `wordstat_get_top_requests` **не выполнен**. Точные показы/мес **не получены** и **не выдуманы**.

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
| Ops | sheets_check_access, mcp logs cursor, unauthorized google mcp, get_values | troubleshooting |
| Adjacent | cursor google workspace plugins 2026, mcp cursor finansist | interlink B21 |

**SEO-вывод:** SERP по `mcp google sheets cursor` — **EN-гайды community MCP** (freema, we2go, Composio), **официальный Google Sheets MCP** (Developer Preview, сентябрь 2026), **новости Cursor + Google Workspace (август 2026)**. Почти нет RU how-to «финансист + реестр + Cursor». Угол КОДА: **правка управленческих реестров через MCP без копипаста**, с веткой SA для безопасности и явным сравнением с B82 (скрипт) и B21 (общий MCP).

---

## SERP (WebSearch Cursor, 12.09.2026)

Приоритет — живой WebSearch; `research-serp.json` (шаг 0, сегодня) — черновик URL. Query `2026 2026` и часть сниппетов **нерелевантны** — не копировать.

### Primary: `mcp google sheets cursor` / setup 2026

| # | URL | Тип | Пробел для КОДА |
| --- | --- | --- | --- |
| 1 | https://developers.google.com/workspace/sheets/api/guides/configure-mcp-server | Official Google Sheets remote MCP | Dev Preview; Antigravity/Claude; нет финреестров |
| 2 | https://cursor.com/docs/mcp | Официальный MCP reference Cursor | Нет Sheets-кейса |
| 3 | https://cursor.com/help/customization/mcp | Help: mcp.json, OAuth, approvals | Канон шагов; нет реестров |
| 4 | https://github.com/freema/mcp-gsheets | Community MCP (SA) | EN; dev-фокус, не CFO |
| 5 | https://github.com/we2go/google-mcp | npx wizard OAuth/SA | Sheets+Docs; не реестры |
| 6 | https://composio.dev/toolkits/googlesheets/framework/cursor | Composio OAuth | SaaS-посредник |
| 7 | https://llmversus.com/mcp/google-sheets-mcp | Install guide 2026 (`mcp-google-sheets`) | Другой пакет; не finance |
| 8 | https://www.merge.dev/blog/google-sheets-mcp-cursor | Merge Agent Handler | Vendor lock-in |

### News / official Workspace (август–сентябрь 2026)

| # | URL | Тип | Пробел |
| --- | --- | --- | --- |
| 1 | https://cursor.com/changelog/google-workspace-plugins | Changelog 03.08.2026 | Drive/Gmail/Calendar детально; Sheets в теле changelog **не расписан** |
| 2 | https://mayai.ru/cursor-otkryl-gmail-i-sheets-agentam/ | RU разбор релиза 04.08.2026 | Контент-завод; мало SA/реестров |
| 3 | https://vibecoding.ru/news/2026/08/03/cursor-google-workspace-plugins | RU новость | Баг OAuth `cursor://`; Sheets убрали из витрины 04.08 |
| 4 | https://developers.google.com/workspace/guides/configure-mcp-servers | Google Workspace MCP suite | Preview; не Cursor-howto |

### Secondary: автоматизация финотдела / реестры

| # | URL | Тип | Пробел |
| --- | --- | --- | --- |
| 1 | https://koda-fd.ru/blog/ai-dlya-finansista-2026/ | Hub КОДА | Нет MCP Cursor |
| 2 | https://datalopata.ru/blog/avtomatizatsija-finansov-sistemnyj-podhod-k-uchetu-v-2026-godu/ | Приоритеты автоматизации | ERP-уклон |
| 3 | https://mcp-catalog.ru/tutorials/gsheets-cursor | RU: freema/mcp-gsheets | Нет finance angle |
| 4 | https://mcp-catalog.ru/tutorials/google-sheets-cursor | RU: henilcalagiya variant | Каталог, не CFO |

### Конкурентный зазор (угол КОДА)

1. **Finance-first** — не «подключи Sheets к Cursor», а «перестань копировать реестр в чат: agent правит строку по `doc_key`».
2. **Три пути с выбором** — OAuth-плагин (пилот) vs SA+mcp-gsheets (production финконтур) vs официальный remote Google MCP (Preview) — с honest note про статус Marketplace Sheets в августе 2026.
3. **Связка с реестрами серии** — договоры (B51), УПД (B58), SaaS (B83); MCP = слой правок поверх уже спроектированной таблицы.
4. **Security block** — минимальный share, ключ вне git, approval tools, indirect prompt injection (Google/MCP), обезличивание.
5. **Verify loop** — после write всегда `get_values` / `sheets_get_values`; «Connected ≠ authorized».
6. **Fork от B82** — B82 = свой Python-скрипт; B92 = те же SA+share, но правки через Agent+MCP без написания кода.

---

## Таблица фактов

| # | Утверждение | Источник | Дата проверки |
| --- | --- | --- | --- |
| 1 | MCP подключает Cursor к внешним инструментам; Agent вызывает tools в чате. | https://cursor.com/help/customization/mcp | 2026-09-12 |
| 2 | Конфиг MCP: проектный `.cursor/mcp.json` + глобальный `~/.cursor/mcp.json`; при совпадении имени побеждает **проектный**. | https://cursor.com/help/customization/mcp | 2026-09-12 |
| 3 | Локальный MCP: `command`, `args`, `env`; удалённый — поле `url` (+ опционально `headers` / static OAuth `auth`). | https://cursor.com/docs/mcp | 2026-09-12 |
| 4 | One-click: Customize → MCPs → Add to Cursor; после ручного `mcp.json` — **перезапуск Cursor**. | https://cursor.com/help/customization/mcp | 2026-09-12 |
| 5 | По умолчанию Agent **запрашивает approval** перед MCP-tool; с Cursor 3.6+ — Auto-review / allowlist / `permissions.json`. | https://cursor.com/help/customization/mcp | 2026-09-12 |
| 6 | Troubleshooting: Output → **MCP Logs** (`Ctrl+Shift+U` / `Cmd+Shift+U`). | https://cursor.com/docs/mcp | 2026-09-12 |
| 7 | 03.08.2026 Cursor анонсировал Google Workspace plugins: агенты читают/пишут Drive, Gmail, Calendar без выхода из редактора; установка из Marketplace или Customize. | https://cursor.com/changelog/google-workspace-plugins | 2026-09-12 |
| 8 | В changelog 03.08.2026 перечислены Drive, Gmail, Calendar; Sheets/Docs в этом документе **не детализированы**. | https://cursor.com/changelog/google-workspace-plugins | 2026-09-12 |
| 9 | По vibecoding.ru (04.08.2026): из пяти обещанных Workspace-плагинов в витрине остались **Gmail, Drive, Calendar**; Docs/Sheets/Slides временно убраны; мин. версия Cursor **3.13.0**; OAuth-bug с callback `cursor://` (обход через cursor.com/agents). | https://vibecoding.ru/news/2026/08/03/cursor-google-workspace-plugins | 2026-09-12 |
| 10 | Официальные Workspace MCP Google — **Developer Preview**; доступ через программу разработчиков. | https://developers.google.com/workspace/sheets/api/guides/configure-mcp-server | 2026-09-12 |
| 11 | Официальный remote Sheets MCP URL: `https://sheetsmcp.googleapis.com/mcp/v1`; нужно enable `sheets.googleapis.com` и `sheetsmcp.googleapis.com`. | https://developers.google.com/workspace/sheets/api/guides/configure-mcp-server | 2026-09-12 (doc Last updated 2026-09-03) |
| 12 | Tools официального Sheets MCP: `get_values`, `get_spreadsheet`, `update_spreadsheet`, `update_values`, `update_formulas`, `insert_dimension`. | https://developers.google.com/workspace/sheets/api/guides/configure-mcp-server | 2026-09-12 |
| 13 | OAuth scopes Sheets MCP: `drive.readonly`, `drive.file`, `spreadsheets.readonly`, `spreadsheets`. | https://developers.google.com/workspace/sheets/api/guides/configure-mcp-server | 2026-09-12 |
| 14 | Квоты Sheets API / Sheets MCP: read/write **300/мин на проект**, **60/мин на user×project**; превышение → HTTP **429**; batch = 1 запрос. | https://developers.google.com/workspace/sheets/api/limits | 2026-09-12 |
| 15 | `freema/mcp-gsheets`: Node.js **v20+**, Google Cloud + Sheets API + service account JSON; `npx -y mcp-gsheets@latest` + `GOOGLE_PROJECT_ID` + `GOOGLE_APPLICATION_CREDENTIALS`. | https://github.com/freema/mcp-gsheets | 2026-09-12 |
| 16 | Ключевые tools mcp-gsheets для реестра: `sheets_get_values`, `sheets_update_values`, `sheets_append_values`, `sheets_batch_get_values`, `sheets_get_metadata`, `sheets_check_access`. | https://github.com/freema/mcp-gsheets | 2026-09-12 |
| 17 | `sheets_append_values`: по умолчанию `insertDataOption` = **OVERWRITE** — для реестра явно указывать `INSERT_ROWS`, если нужно сдвигать строки. | https://github.com/freema/mcp-gsheets | 2026-09-12 |
| 18 | Service account видит **только** таблицы, расшаренные на `client_email` из JSON; IAM-роли Cloud **не заменяют** Share файла. | https://developers.google.com/workspace/guides/create-credentials#service-account | 2026-09-12 |
| 19 | Риск MCP+Google: агент наследует права пользователя; возможна **indirect prompt injection** — нужен human-in-the-loop на write. | https://developers.google.com/workspace/sheets/api/guides/configure-mcp-server ; https://mayai.ru/cursor-otkryl-gmail-i-sheets-agentam/ | 2026-09-12 |
| 20 | «Connected» в Tools & MCP **не гарантирует** успешный Google OAuth — проверять живым read/write запросом. | https://mayai.ru/cursor-otkryl-gmail-i-sheets-agentam/ | 2026-09-12 |
| 21 | Локальный OAuth Cursor и Cloud Agents — разные контуры; интерактивный Google-логин локально **не переезжает** автоматически в облако. | https://mayai.ru/cursor-otkryl-gmail-i-sheets-agentam/ | 2026-09-12 |
| 22 | Cursor static OAuth redirect для remote MCP: `https://www.cursor.com/agents/mcp/oauth/callback` и `http://localhost:8787/callback`. | https://cursor.com/docs/mcp | 2026-09-12 |
| 23 | `we2go/google-mcp`: `npx google-sheet-mcp init` — wizard SA или OAuth; конфиг в `.cursor/mcp.json`. | https://github.com/we2go/google-mcp | 2026-09-12 |
| 24 | В 2026 финотдел автоматизирует в первую очередь классификацию платежей, сверки, управленческую отчётность — Sheets+MCP подходит как **transport правок**, не GL. | https://koda-fd.ru/blog/ai-dlya-finansista-2026/ | 2026-09-12 |
| 25 | Exceeding Sheets API quota limits планируется тарифицироваться в Google Cloud billing **later in 2026** (официальная оговорка Google). | https://developers.google.com/workspace/sheets/api/limits | 2026-09-12 |

**Не выдумывать:** показы Wordstat; «Sheets-плагин всегда в Marketplace» (проверять на дату публикации); что SA = доступ ко всему Drive; цифры «установок» сторонних каталогов; обещание «без программиста» для Path B без упоминания GCP/SA.

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

**Пример remote (Path C — опционально упомянуть):**

```json
{
  "mcpServers": {
    "sheets": {
      "url": "https://sheetsmcp.googleapis.com/mcp/v1"
    }
  }
}
```

(Для production Google может требовать OAuth clientId/secret — см. docs Google; Cursor поддерживает static `auth` для remote MCP.)

**Тестовый промпт агента (реестр):**

> Подключись к таблице `{SPREADSHEET_ID}`. На листе `Реестр` найди строку, где колонка `doc_key` = `DOG-2026-014`. Прочитай текущие значения колонок `status` и `comment`. Если `status` ≠ «Оплачен», предложи обновление на «На согласовании» и допиши в `comment` сегодняшнюю дату. После write перечитай ту же строку и покажи diff.

---

## FAQ-кандидаты

- **Можно ли без программиста?** — Path A (Marketplace+OAuth): да для пилота, если плагин в витрине; Path B (SA+mcp.json): по инструкции, Cursor поможет с JSON; первый реестр ~1–2 ч.
- **Сколько займёт внедрение?** — SA + mcp.json + один тестовый update: **~1–2 ч**; OAuth-плагин быстрее при доступной карточке.
- **Какие риски для данных?** — OAuth = права вашего Google; SA-ключ = все расшаренные файлы; не класть ПДн; подтверждать write-tools; indirect injection из писем/ячеек.
- **OAuth или service account?** — OAuth для личного пилота; SA для командного реестра, cron, минимального blast radius.
- **Чем отличается от B82?** — B82 = Python/Node скрипт пишет в staging; B92 = Agent в Cursor правит через MCP без скрипта.
- **Работает ли в Cloud Agents?** — локальный OAuth не переезжает автоматически; проверять отдельно или использовать SA / Team MCP dashboard.

---

## CTA / interlink

- Internal: `/avtomatizaciya-finansov-no-code/`, `/obezlichivanie-dannyh-chatgpt-finansist/`, `/google-sheets-api-integraciya-finotdel/` (B82), `/mcp-cursor-finansist-instrumenty/` (B21)
- Соседние реестры: B51, B58, B83; ротация ключа: B93
- CTA: `https://club.koda-fd.ru/?utm_source=blog&utm_medium=article&utm_campaign=mcp-google-sheets-cursor-reestry` (≤2), `https://t.me/finance_modern?utm_source=blog&utm_medium=article` (≤2)

---

## Handoff marker

`=== EXCALIBUR BLOG RESEARCH ===` — см. `.cursor/excalibur-blog-handoff.md`
