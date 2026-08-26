# Research notes — B92

**topic_id:** B92  
**slug:** mcp-google-sheets-cursor-reestry  
**h1:** Как подключить MCP к Google Sheets в Cursor и править реестры без копипаста  
**research_date:** 2026-08-26  
**publish_target:** koda-fd.ru/blog  
**utility_gate:** PASS (`how_to`, mode B) — подтверждено `excalibur_blog_utility_gate.py --topic-id B92`  
**author_id:** olga-kondratskaya  
**related_internal:** `/avtomatizaciya-finansov-no-code/`, `/obezlichivanie-dannyh-chatgpt-finansist/`  
**sibling_queue:** B82 (Sheets API + SA), B21 (MCP в Cursor общий), B51/B58/B83 (реестры в Sheets), B93 (ротация ключа SA)  
**cover_scene_hint:** abstract holographic finance automation dark #0a0a0f purple #8b5cf6, no text  
**freshness:** prefer sources after 2026-05-28; verify versions on 2026-08-26

---

## utility_verdict

**PASS** — тема utility-only how_to. Читатель получает два рабочих маршрута подключения Google Sheets к Cursor через MCP (**Path A:** официальный Workspace-плагин / OAuth, если доступен в витрине; **Path B:** community `freema/mcp-gsheets` + service account — основной для финконтура), подготовку реестра под агентные правки, тестовый сценарий «найти строку → обновить статус → перечитать», чеклист безопасности и troubleshooting. Не новость «Cursor открыл Workspace», не обзор 25 MCP-серверов, не туториал «напиши свой MCP с нуля».

---

## reader_outcome

После гайда финансист сможет подключить MCP Google Sheets в Cursor (предпочтительно через service account), дать агенту доступ только к рабочему реестру, попросить обновить статус строки или дописать поля без копирования таблицы в чат и проверить результат перечиткой диапазона через MCP-tool.

---

## action_outline

1. **Решить, нужен ли MCP Sheets** — реестр уже в Google Sheets (договоры, УПД, SaaS, заявки на расход), правки повторяются, устали таскать диапазоны в чат; **не** делать, если нужен жёсткий audit trail / сотни таблиц с enterprise ACL — тогда 1С/CLM, Sheets только staging.
2. **Выбрать путь подключения** — **Path A (пилот):** плагин Google Sheets из Cursor Marketplace / Customize → OAuth личного Google — **на 26.08.2026 карточка `cursor.com/marketplace/mcp/google-sheets` отдаёт «MCP server Not Found»**, поэтому Path A считать опциональным/нестабильным; **Path B (финконтур, рекомендовать):** `freema/mcp-gsheets` + service account — расшарить только нужные реестры, ключ в `env`, без доступа агента ко всему Drive (см. B82, B93).
3. **Подготовить реестр** — одна строка = одна сущность; стабильный `doc_key`; лист `staging` для импорта; в облако без сырых ПДн (ИНН/сумма/статус — да; паспорт, полные ФИО — нет); interlink `/obezlichivanie-dannyh-chatgpt-finansist/`.
4. **Path B: Google Cloud + SA** — проект → включить **Google Sheets API** → service account → JSON-ключ → скопировать `client_email` → «Поделиться» на файл реестра с ролью **Редактор** (без «Уведомить»).
5. **Path B: mcp.json в Cursor** — глобально `~/.cursor/mcp.json` или проектно `.cursor/mcp.json`; блок `mcp-gsheets` с `npx -y mcp-gsheets@latest` и `GOOGLE_APPLICATION_CREDENTIALS` (абсолютный путь); JSON-ключ **не** в git; альтернатива — `GOOGLE_PRIVATE_KEY` + `GOOGLE_CLIENT_EMAIL`.
6. **Path A (если витрина снова покажет Sheets)** — Customize → MCPs → Google Sheets → Add → OAuth; минимальные scopes; учесть: в официальном changelog 03.08.2026 детально только Drive/Gmail/Calendar; Docs/Sheets убраны из Marketplace 04.08.2026 (vibecoding.ru); OAuth-bug `cursor://` — обход через cursor.com/agents.
7. **Проверить подключение** — перезапуск Cursor; Customize → MCPs → зелёный статус; Output → **MCP Logs**; tool `sheets_check_access` (Path B) или живой запрос «прочитай A1:C5 листа Реестр».
8. **Рабочий сценарий реестра** — промпт с DoD: `sheets_get_metadata` → найти строку по `doc_key` → `sheets_update_values` / `sheets_append_values` только в колонки статуса/комментария → `sheets_get_values` на ту же строку → сверка; human approval на каждый write-tool; для append явно `INSERT_ROWS` (default = OVERWRITE).
9. **Эксплуатация и рост** — allowlist write-tools; ротация ключа SA (B93); при >80–100 заявок/мес или audit — n8n/ERP, Sheets остаётся staging; соседние реестры B51/B58/B83.

**Workflow для статьи:**  
`Реестр в Sheets → (SA share | OAuth plugin*) → MCP в Cursor → Agent read/update по doc_key → перечитка диапазона → регламент CFO`  
\*Path A — только если плагин снова доступен в Marketplace.

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
| Setup | mcp.json cursor, cursor marketplace google sheets, mcp-gsheets service account | H2 пошагово |
| Finance | автоматизация финотдела google sheets, реестр договоров cursor, править реестр без копипаста | угол КОДА |
| Registry | реестр upd google sheets, реестр saas подписок, doc_key find update | кейсы |
| Security | service account json не в git, обезличивание sheets, oauth scopes минимум | FAQ |
| Ops | sheets_check_access, mcp logs cursor, unauthorized google mcp | troubleshooting |
| Adjacent | cursor google workspace plugins 2026, mcp cursor finansist | interlink B21 |

**SEO-вывод (26.08.2026):** SERP по `mcp google sheets cursor` — смесь **новостей Workspace-плагинов (авг 2026)**, **community MCP** (freema, we2go, PasteSheet, Zapier) и **общих RU-гайдов по mcp.json**. Почти нет RU how-to «финансист + реестр + Cursor без копипаста». Угол КОДА: **правка управленческих реестров через MCP**, с **Path B как default** из-за отсутствия Sheets в Marketplace на дату research, + сравнение с B82 (скрипт) и B21 (общий MCP).

---

## SERP (WebSearch Cursor, 26.08.2026)

Приоритет — живой WebSearch + WebFetch. `research-serp.json` (шаг 0, дата 2026-08-26) полезен как URL-черновик; query `2026 2026` и календарные сниппеты **нерелевантны** — не копировать.

### Primary: `mcp google sheets cursor 2026`

| # | URL | Тип | Пробел для КОДА |
| --- | --- | --- | --- |
| 1 | https://cursor.com/docs/mcp | Официальный reference | Нет реестров финотдела |
| 2 | https://cursor.com/help/customization/mcp | Help: mcp.json, OAuth, approvals, MCP Logs, Cloud Agents | Канон шагов; нет Sheets-кейса |
| 3 | https://github.com/freema/mcp-gsheets | Community MCP (SA), Node 20+, tools read/write | EN; dev-фокус, не CFO |
| 4 | https://github.com/we2go/google-mcp | npx wizard OAuth/SA, Sheets+Docs | Не реестры финотдела |
| 5 | https://github.com/abcreativ/google-suite-mcp | 82 tools Workspace | Overkill для одного реестра |
| 6 | https://dev.to/pastesheet/google-sheets-in-vs-code-cursor-and-windsurf-over-mcp-5467 | Hosted URL MCP | Публичные листы; не SA |
| 7 | https://zapier.com/blog/google-sheets-with-zapier-mcp/ | Zapier MCP → Create Spreadsheet Row | SaaS-посредник, не финконтур |
| 8 | https://mcpcursor.com/server/google-sheets-mcp | Каталог (akchro/FastMCP) | Dev OAuth tutorial |

### News / Marketplace status (август 2026) — критично для Path A

| # | URL | Факт на 26.08.2026 | Пробел |
| --- | --- | --- | --- |
| 1 | https://cursor.com/changelog/google-workspace-plugins | Changelog 03.08.2026: **Drive, Gmail, Calendar**; Sheets в теле **не расписан** | Нет how-to реестра |
| 2 | https://cursor.com/marketplace/mcp/google-sheets | WebFetch 26.08.2026: **«MCP server Not Found»** | Плагин Sheets в витрине недоступен |
| 3 | https://vibecoding.ru/news/2026/08/03/cursor-google-workspace-plugins | 04.08: Docs/Sheets/Slides убраны; остались Gmail/Drive/Calendar; мин. Cursor **3.13.0**; OAuth bug `cursor://` | Новость, не гайд |
| 4 | https://mayai.ru/cursor-otkryl-gmail-i-sheets-agentam/ | RU разбор: OAuth под аккаунтом Google, prompt injection, Connected ≠ authorized | Контент-завод; мало SA |
| 5 | https://www.explainx.ai/blog/cursor-google-workspace-plugins-gmail-drive-calendar-august-2026 | EN: gap официальной доки по Sheets | Не finance |

### Secondary: `автоматизация финотдела 2026`

| # | URL | Тип | Пробел |
| --- | --- | --- | --- |
| 1 | https://koda-fd.ru/blog/ai-dlya-finansista-2026/ | Hub КОДА | Нет MCP Cursor |
| 2 | https://datalopata.ru/blog/avtomatizatsija-finansov-sistemnyj-podhod-k-uchetu-v-2026-godu/ | Приоритеты автоматизации | ERP-уклон |
| 3 | https://znaj.org/ru/6-luchshikh-reshenii-2026-goda-avtomatizacii-upravleniya-finansami/ | Обзор решений | Не Cursor |
| 4 | https://dzen.ru/a/anRW32ni3D3wHjQF | Реестр договоров Sheets | Без MCP |
| 5 | https://dzen.ru/a/aoAqyl_t_ztBh3s7 | Реестр УПД Sheets | Без MCP |

### H1-aligned / RU setup

| # | URL | Заметка |
| --- | --- | --- |
| 1 | https://mcp-catalog.ru/tutorials/gsheets-cursor | RU: freema/mcp-gsheets в Cursor |
| 2 | https://mcp-catalog.ru/tutorials/google-sheets-cursor | RU: henilcalagiya variant |
| 3 | https://vibecoderz.ru/blog/kak-podklyuchit-mcp-server-k-cursor-i-claude | mcp.json global/project, зелёный индикатор |
| 4 | https://neurinix.com/2026/06/21/podklyuchenie-mcp-cursor/ | Общий MCP setup RU |
| 5 | https://khar-ag.ru/docs/cursor-mcp-guide/ | mcp.json + allowlist |

### Конкурентный зазор (угол КОДА)

1. **Finance-first** — не «подключи Sheets к Cursor», а «перестань копировать реестр в чат: agent правит строку по `doc_key`».
2. **Два пути с честной витриной** — Path B (SA) как **default на 26.08.2026**; Path A — «если снова появится в Marketplace».
3. **Связка с реестрами серии** — договоры (B51), УПД (B58), SaaS (B83); MCP = слой правок поверх уже спроектированной таблицы.
4. **Security block** — минимальный share, ключ вне git, approval tools, indirect prompt injection, обезличивание.
5. **Verify loop** — после write всегда `get_values`; «Connected ≠ authorized».
6. **Fork от B82** — B82 = свой Python-скрипт; B92 = те же SA+share, но правки через Agent+MCP без написания кода.

---

## Таблица фактов

| # | Утверждение | Источник | Дата проверки |
| --- | --- | --- | --- |
| 1 | MCP подключает Cursor к внешним инструментам; Agent вызывает tools в чате. | https://cursor.com/help/customization/mcp | 2026-08-26 |
| 2 | Конфиг: проектный `.cursor/mcp.json` + глобальный `~/.cursor/mcp.json`; при совпадении имени побеждает **проектный**. | https://cursor.com/help/customization/mcp | 2026-08-26 |
| 3 | Локальный MCP: `command`, `args`, `env`; удалённый — поле `url` (+ опционально `headers`). | https://cursor.com/help/customization/mcp | 2026-08-26 |
| 4 | One-click: Customize → MCPs → Add to Cursor; после ручного `mcp.json` — **перезапуск Cursor**. | https://cursor.com/help/customization/mcp | 2026-08-26 |
| 5 | По умолчанию Agent **запрашивает approval** перед MCP-tool; с Cursor 3.6+ — Auto-review / allowlist (`permissions.json`). | https://cursor.com/help/customization/mcp | 2026-08-26 |
| 6 | Troubleshooting: Output → **MCP Logs** (`Ctrl+Shift+U` / `Cmd+Shift+U`). | https://cursor.com/help/customization/mcp | 2026-08-26 |
| 7 | Cloud Agents поддерживают MCP, настроенные в Cloud Agents dashboard / Team Integrations — **отдельно** от локального OAuth IDE. | https://cursor.com/help/customization/mcp | 2026-08-26 |
| 8 | 03.08.2026 Cursor анонсировал Google Workspace plugins; в changelog перечислены **Drive, Gmail, Calendar** (Sheets в этом документе не детализирован). | https://cursor.com/changelog/google-workspace-plugins | 2026-08-26 |
| 9 | По vibecoding.ru: 04.08.2026 Docs/Sheets/Slides убраны из Marketplace; в строю Gmail, Drive, Calendar; мин. версия Cursor **3.13.0**; OAuth-bug callback `cursor://` (обход: cursor.com/agents). | https://vibecoding.ru/news/2026/08/03/cursor-google-workspace-plugins | 2026-08-26 |
| 10 | WebFetch 26.08.2026: `https://cursor.com/marketplace/mcp/google-sheets` → **«MCP server Not Found»** — официальный Sheets MCP в витрине недоступен. | https://cursor.com/marketplace/mcp/google-sheets | 2026-08-26 |
| 11 | Официальные Workspace MCP Google — **Developer Preview** (раздача через программу разработчиков). | https://vibecoding.ru/news/2026/08/03/cursor-google-workspace-plugins | 2026-08-26 |
| 12 | `freema/mcp-gsheets`: Node.js **v20+**, Google Cloud + Sheets API + SA JSON; `npx -y mcp-gsheets@latest` + `GOOGLE_APPLICATION_CREDENTIALS`. | https://github.com/freema/mcp-gsheets | 2026-08-26 |
| 13 | Ключевые tools для реестра: `sheets_get_values`, `sheets_update_values`, `sheets_append_values`, `sheets_batch_get_values`, `sheets_get_metadata`, `sheets_check_access`. | https://github.com/freema/mcp-gsheets | 2026-08-26 |
| 14 | `sheets_append_values`: default `insertDataOption` = **OVERWRITE** — для реестра явно указывать `INSERT_ROWS`. | https://github.com/freema/mcp-gsheets | 2026-08-26 |
| 15 | SA видит **только** таблицы, расшаренные на `client_email`; IAM Cloud **не заменяет** Share файла. | https://developers.google.com/workspace/guides/create-credentials#service-account | 2026-08-26 |
| 16 | Scope `https://www.googleapis.com/auth/spreadsheets` — read/write всех расшаренных таблиц SA; применяется ко **всему файлу**; листы — ProtectedRange. | https://developers.google.com/workspace/sheets/api/scopes | 2026-08-26 |
| 17 | Квота Sheets API write: **300 запросов/мин** на проект; превышение → HTTP **429**; batch = один запрос. | https://developers.google.com/workspace/sheets/api/limits | 2026-08-26 |
| 18 | `we2go/google-mcp`: `npx google-mcp init` — wizard SA или OAuth; tools `sheets_read_range`, `sheets_update_range`, `sheets_append_row`. | https://github.com/we2go/google-mcp | 2026-08-26 |
| 19 | Hosted PasteSheet: `url` в `mcp.json`; публичные листы без GCP; private endpoints от **$9/mo**. | https://dev.to/pastesheet/google-sheets-in-vs-code-cursor-and-windsurf-over-mcp-5467 | 2026-08-26 |
| 20 | Риск MCP+Google: агент наследует права пользователя; возможна **indirect prompt injection** — HITL на write/send. | https://mayai.ru/cursor-otkryl-gmail-i-sheets-agentam/ | 2026-08-26 |
| 21 | «Connected» в Tools & MCP **не гарантирует** успешный Google OAuth — проверять живым read/write. | https://mayai.ru/cursor-otkryl-gmail-i-sheets-agentam/ | 2026-08-26 |
| 22 | Реестр договоров в Sheets уместен до **200–300** активных договоров при одном владельце; иначе CLM/1С. | https://dzen.ru/a/anRW32ni3D3wHjQF | 2026-08-26 |
| 23 | Заявки на расход Forms→Sheets: при **>80–100** заявок/мес Sheets — staging перед ERP/n8n. | https://dzen.ru/a/aoAx4V_t_ztBh5aj | 2026-08-26 |
| 24 | В 2026 финотдел автоматизирует классификацию платежей, сверки, упр. отчётность — Sheets+MCP = **transport правок**, не GL. | https://koda-fd.ru/blog/ai-dlya-finansista-2026/ | 2026-08-26 |

**Не выдумывать:** показы Wordstat; что Sheets-плагин «всегда в Marketplace» (на 26.08 — Not Found); что SA = доступ ко всему Drive; цифры Smithery installs; «без программиста» для Path B без упоминания GCP/SA.

**fact-bank.md:** прямых фактов про MCP+Sheets нет — опираться на таблицу выше. Контент-заводные ROI из fact-bank **не тянуть**.

---

## Структура H2 для writer (из карточки B92)

1. Когда это нужно финотделу (и когда нет)  
2. Подготовка данных и безопасность (без сырых ПДн в облако)  
3. Пошаговая настройка / сценарий (Path B default; Path A — optional)  
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

- **Можно ли без программиста?** — Path A (если Marketplace снова покажет Sheets): OAuth-пилот; Path B (SA+mcp.json): по инструкции B82/B92, Cursor поможет с JSON; production — 1–2 ч первый реестр.
- **Сколько займёт внедрение?** — SA + mcp.json + один тестовый update: **~1–2 ч**.
- **Какие риски для данных?** — OAuth = права вашего Google; SA-ключ = все расшаренные файлы; не класть ПДн; подтверждать write-tools; indirect injection.
- **OAuth или service account?** — OAuth для личного пилота (если плагин доступен); SA для командного реестра и минимального blast radius — **рекомендация на 26.08.2026**.
- **Чем отличается от B82?** — B82 = Python/Node скрипт пишет в staging; B92 = Agent в Cursor правит через MCP без скрипта.
- **Работает ли в Cloud Agents?** — да, но MCP настраивается в Cloud Agents dashboard отдельно; локальный IDE OAuth не переезжает автоматически — для облака предпочтителен SA / team MCP.
- **Почему Path B, а не Marketplace?** — на 26.08.2026 официальная карточка google-sheets в Marketplace = Not Found; Docs/Sheets сняты 04.08 (vibecoding).

---

## CTA / interlink

- Internal: `/avtomatizaciya-finansov-no-code/`, `/obezlichivanie-dannyh-chatgpt-finansist/`, `/google-sheets-api-integraciya-finotdel/` (B82), `/mcp-cursor-finansist-instrumenty/` (B21)
- Соседние реестры: B51, B58, B83; ротация ключа: B93
- CTA: `https://club.koda-fd.ru/?utm_source=blog&utm_medium=article&utm_campaign=mcp-google-sheets-cursor-reestry` (≤2), `https://t.me/finance_modern?utm_source=blog&utm_medium=article` (≤2)

---

## Handoff marker

`=== EXCALIBUR BLOG RESEARCH ===` — см. `.cursor/excalibur-blog-handoff.md`
