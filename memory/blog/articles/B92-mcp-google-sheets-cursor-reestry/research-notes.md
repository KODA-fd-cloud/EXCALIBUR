# Research notes — B92

**topic_id:** B92  
**slug:** mcp-google-sheets-cursor-reestry  
**h1:** Как подключить MCP к Google Sheets в Cursor и править реестры без копипаста  
**research_date:** 2026-09-17  
**publish_target:** koda-fd.ru/blog  
**utility_gate:** PASS (`how_to`, mode B)  
**author_id:** olga-kondratskaya  
**related_internal:** `/avtomatizaciya-finansov-no-code/`, `/obezlichivanie-dannyh-chatgpt-finansist/`  
**sibling_queue:** B82 (Sheets API + SA), B21 (MCP в Cursor общий), B51/B58/B83 (реестры в Sheets), B93 (ротация SA)  
**cover_scene_hint:** abstract holographic finance automation dark #0a0a0f purple #8b5cf6, no text

---

## utility_verdict

**PASS** — тема utility-only how_to. Читатель получает рабочие маршруты подключения Google Sheets к Cursor через MCP: (A) плагин/OAuth Marketplace или remote URL, (B) community `mcp-gsheets` на service account для финконтура, (C опционально) официальный remote Google Sheets MCP (`sheetsmcp.googleapis.com`, Developer Preview). Дальше — подготовка реестра под агентные правки, сценарий «найти строку → обновить статус → перечитать», чеклист безопасности и troubleshooting. Не новость «Cursor открыл Workspace», не обзор 25 MCP-серверов, не туториал «напиши свой MCP с нуля».

---

## reader_outcome

После гайда финансист сможет подключить MCP Google Sheets в Cursor, дать агенту доступ только к рабочему реестру (через service account или OAuth), попросить обновить статус строки или дописать поля без копирования таблицы в чат и проверить результат перечиткой диапазона через MCP-tool.

---

## action_outline

1. **Решить, нужен ли MCP Sheets** — реестр уже в Google Sheets (договоры, УПД, SaaS, заявки), правки повторяются, устали таскать диапазоны в чат; **не** делать, если нужен жёсткий audit trail / сотни таблиц с enterprise ACL — тогда 1С/CLM, Sheets только staging.
2. **Выбрать путь подключения** — **Path A (быстрый пилот):** Marketplace / Customize → OAuth личного Google или remote URL; **Path B (финконтур):** `freema/mcp-gsheets` + service account — расшарить только нужные реестры, ключ в `env`, без доступа агента ко всему Drive (см. B82, B93); **Path C (Google remote, preview):** `https://sheetsmcp.googleapis.com/mcp/v1` + OAuth client (Developer Preview).
3. **Подготовить реестр** — одна строка = одна сущность; стабильный `doc_key`; лист `staging` для импорта; в облако без сырых ПДн (ИНН/сумма/статус — да; паспорт, полные ФИО — нет); interlink `/obezlichivanie-dannyh-chatgpt-finansist/`.
4. **Path B: Google Cloud + SA** — проект → включить **Google Sheets API** → service account → JSON-ключ → скопировать `client_email` → «Поделиться» на файл реестра с ролью **Редактор** (без «Уведомить»).
5. **Path B: mcp.json в Cursor** — глобально `~/.cursor/mcp.json` или проектно `.cursor/mcp.json`; блок `mcp-gsheets` с `npx -y mcp-gsheets@latest` и `GOOGLE_APPLICATION_CREDENTIALS` (абсолютный путь); JSON-ключ **не** в git.
6. **Path A/C: Marketplace или remote OAuth** — Customize → MCPs → Add / либо `url` + `auth` в `mcp.json`; для Google remote зарегистрировать redirect Cursor (`https://www.cursor.com/agents/mcp/oauth/callback`, desktop `http://localhost:8787/callback`); минимальные scopes; учесть, что в changelog 03.08.2026 детально описаны Drive/Gmail/Calendar, а Sheets в витрине мог пропадать — иметь Path B как запасной.
7. **Проверить подключение** — перезапуск Cursor; Customize → MCPs → зелёный статус; Output → **MCP Logs**; tool `sheets_check_access` (Path B) или живой запрос «прочитай A1:C5 листа Реестр» / `get_values`.
8. **Рабочий сценарий реестра** — промпт с DoD: metadata → найти строку по `doc_key` → update/append только в колонки статуса/комментария → get_values на ту же строку → сверка; human approval на каждый write-tool.
9. **Эксплуатация и рост** — allowlist write-tools; ротация ключа SA (B93); при >80–100 заявок/мес или audit — n8n/ERP, Sheets остаётся staging; соседние реестры B51/B58/B83.

**Workflow для статьи:**  
`Реестр в Sheets → (SA share | OAuth plugin | Google remote MCP) → MCP в Cursor → Agent read/update по doc_key → перечитка диапазона → регламент CFO`

---

## Яндекс Wordstat (MCP user-mcp-kv)

⚠️ **WORDSTAT AUTH WARNING:** сервер MCP `user-mcp-kv` в этой Cloud-сессии **не подключён** (в каталоге dynamic tools: `cursor`, `Cursor Automation Tools`, `cursor-cloud`, `cursor-subscriptions`). Вызов `CallDynamicTool` → `user-mcp-kv` / `wordstat_get_top_requests` вернул: *MCP server does not exist*. Точные показы/мес **не получены** и **не выдуманы**.

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
| Ops | sheets_check_access, mcp logs cursor, unauthorized google mcp | troubleshooting |
| Adjacent | cursor google workspace plugins 2026, mcp cursor finansist | interlink B21 |

**SEO-вывод:** SERP по `mcp google sheets cursor` на 2026-09-17 — **официальный Google remote Sheets MCP** (developers.google.com), **EN community MCP** (freema, we2go, npm mcp-google-sheets), **Cursor docs/help по mcp.json**, новости Workspace plugins (август 2026). Почти нет RU how-to «финансист + реестр + Cursor». Угол КОДА: **правка управленческих реестров через MCP без копипаста**, с веткой SA для безопасности и явным сравнением с B82 (скрипт) и B21 (общий MCP).

---

## SERP (WebSearch Cursor, 17.09.2026)

Приоритет — живой WebSearch; `research-serp.json` (шаг 0) полезен как URL-черновик; query `2026 2026` и часть сниппетов **нерелевантны** — не копировать.

### Primary: `mcp google sheets cursor 2026`

| # | URL | Тип | Пробел для КОДА |
| --- | --- | --- | --- |
| 1 | https://developers.google.com/workspace/sheets/api/guides/configure-mcp-server | Официальный Google Sheets remote MCP | Antigravity/Claude; Cursor = «Others»; нет реестров финотдела |
| 2 | https://developers.google.com/workspace/guides/configure-mcp-servers | Обзор Workspace MCP servers | Product list; не finance workflow |
| 3 | https://cursor.com/docs/mcp | Официальный Cursor MCP reference | Нет Sheets-кейса |
| 4 | https://cursor.com/help/customization/mcp | Help: mcp.json, OAuth, approvals, MCP Logs | Канон шагов; нет реестра |
| 5 | https://github.com/freema/mcp-gsheets | Community MCP (SA) | EN; dev-фокус, не CFO |
| 6 | https://www.npmjs.com/package/mcp-gsheets | npm mirror freema | Установка; не finance |
| 7 | https://github.com/we2go/google-mcp | npx wizard OAuth/SA | Sheets; не реестры |
| 8 | https://www.npmjs.com/package/mcp-google-sheets | Community OAuth/SA Node MCP | Dev gateway |
| 9 | https://composio.dev/toolkits/googlesheets/framework/cursor | Composio OAuth | SaaS-посредник |
| 10 | https://llmversus.com/mcp/google-sheets-mcp | Install guide 2026 | EN setup; не CFO |

### News / official Workspace + Google MCP

| # | URL | Тип | Пробел |
| --- | --- | --- | --- |
| 1 | https://cursor.com/changelog/google-workspace-plugins | Changelog 03.08.2026 | Drive/Gmail/Calendar детально; Sheets в теле changelog **не расписан** |
| 2 | https://authorityaitools.com/blog/cursor-google-workspace-plugins-august-2026 | EN разбор релиза | Перечисляет Sheets как capability плагинов; мало SA |
| 3 | https://mayai.ru/cursor-otkryl-gmail-i-sheets-agentam/ | RU разбор | Контент-завод; мало SA/реестров |
| 4 | https://vibecoding.ru/news/2026/08/03/cursor-google-workspace-plugins | RU новость | Баг OAuth; Sheets могли исчезнуть из витрины |

### Secondary: `автоматизация финотдела` + реестры

| # | URL | Тип | Пробел |
| --- | --- | --- | --- |
| 1 | https://habr.com/ru/articles/1017260/ | AI-агенты + Sheets API + MCP БД | Не Cursor MCP Sheets; полезен verify-loop |
| 2 | https://dzen.ru/a/anPc-pP-tkHrn2ln | Подотчётные в Sheets (КОДА) | Без MCP |
| 3 | https://dzen.ru/a/anRW32ni3D3wHjQF | Реестр договоров Sheets | Без MCP |
| 4 | https://koda-fd.ru/blog/ai-dlya-finansista-2026/ | Hub КОДА | Нет MCP Cursor Sheets |

### Конкурентный зазор (угол КОДА)

1. **Finance-first** — не «подключи Sheets к Cursor», а «перестань копировать реестр в чат: agent правит строку по `doc_key`».
2. **Три пути с выбором** — OAuth/Marketplace для пилота vs SA+mcp-gsheets для production vs Google remote MCP (preview) с честным статусом Developer Preview.
3. **Связка с реестрами серии** — договоры (B51), УПД (B58), SaaS (B83); MCP = слой правок поверх уже спроектированной таблицы.
4. **Security block** — минимальный share, ключ вне git, approval tools, indirect prompt injection (Google docs 2026-09-14), обезличивание.
5. **Verify loop** — после write всегда `get_values` / `sheets_get_values`; «Connected ≠ authorized».
6. **Fork от B82** — B82 = свой Python-скрипт; B92 = те же SA+share, но правки через Agent+MCP без написания кода.

---

## Таблица фактов

| # | Утверждение | Источник | Дата проверки |
| --- | --- | --- | --- |
| 1 | MCP подключает Cursor к внешним инструментам; установка из Customize / Marketplace или через `mcp.json`. | https://cursor.com/docs/mcp | 2026-09-17 |
| 2 | Транспорты Cursor MCP: `stdio`, `SSE`, `Streamable HTTP` (remote + OAuth). | https://cursor.com/docs/mcp | 2026-09-17 |
| 3 | Конфиг: проектный `.cursor/mcp.json` + глобальный `~/.cursor/mcp.json`; при совпадении имени побеждает **проектный**. | https://cursor.com/help/customization/mcp | 2026-09-17 |
| 4 | Локальный MCP: `command`/`args`/`env`; удалённый — поле `url` (+ опционально `headers` / static `auth`). | https://cursor.com/docs/mcp ; https://cursor.com/help/customization/mcp | 2026-09-17 |
| 5 | Static OAuth для remote: `auth.CLIENT_ID` (обяз.), `CLIENT_SECRET` (опц.), `scopes` (опц.); redirect: `https://www.cursor.com/agents/mcp/oauth/callback` и `http://localhost:8787/callback`. | https://cursor.com/docs/mcp | 2026-09-17 |
| 6 | One-click: Customize → MCPs → Add to Cursor; после ручного `mcp.json` — **перезапуск Cursor**. | https://cursor.com/help/customization/mcp | 2026-09-17 |
| 7 | По умолчанию Agent **запрашивает approval** перед MCP-tool; с Cursor 3.6+ — Auto-review / allowlist / `permissions.json`. | https://cursor.com/help/customization/mcp | 2026-09-17 |
| 8 | Troubleshooting: Output → **MCP Logs** (`Ctrl+Shift+U` / `Cmd+Shift+U`). | https://cursor.com/docs/mcp | 2026-09-17 |
| 9 | Cloud Agents поддерживают MCP из Dashboard → Integrations & MCP (Team); локальный интерактивный OAuth не «переезжает» сам. | https://cursor.com/help/customization/mcp | 2026-09-17 |
| 10 | 03.08.2026 Cursor анонсировал Google Workspace plugins: Drive, Gmail, Calendar в changelog; установка из Marketplace/Customize. | https://cursor.com/changelog/google-workspace-plugins | 2026-09-17 |
| 11 | В changelog 03.08.2026 Sheets/Docs **не детализированы** в списке «Install plugins»; сторонние разборы добавляют Sheets как capability. | https://cursor.com/changelog/google-workspace-plugins ; https://authorityaitools.com/blog/cursor-google-workspace-plugins-august-2026 | 2026-09-17 |
| 12 | Google Sheets remote MCP: endpoint `https://sheetsmcp.googleapis.com/mcp/v1`; статус **Developer Preview** (Google Workspace Developer Preview Program). Документ обновлён **2026-09-14**. | https://developers.google.com/workspace/sheets/api/guides/configure-mcp-server | 2026-09-17 |
| 13 | Для Google Sheets MCP нужно включить `sheets.googleapis.com` и MCP-сервис `sheetsmcp.googleapis.com`. | https://developers.google.com/workspace/sheets/api/guides/configure-mcp-server | 2026-09-17 |
| 14 | OAuth scopes Google Sheets MCP: `drive.readonly`, `drive.file`, `spreadsheets.readonly`, `spreadsheets`. | https://developers.google.com/workspace/sheets/api/guides/configure-mcp-server | 2026-09-17 |
| 15 | Tools официального Sheets MCP: `get_values`, `get_spreadsheet`, `update_spreadsheet`, `update_values`, `update_formulas`, `insert_dimension`. | https://developers.google.com/workspace/sheets/api/guides/configure-mcp-server | 2026-09-17 |
| 16 | Transport для «Others» клиентов: Streamable HTTP + OAuth 2.0; server name `sheets`, URL `https://sheetsmcp.googleapis.com/mcp/v1`. | https://developers.google.com/workspace/sheets/api/guides/configure-mcp-server | 2026-09-17 |
| 17 | Google предупреждает про **indirect prompt injection** при чтении недоверенных spreadsheets; рекомендовать human review write-actions и Model Armor / аналог. | https://developers.google.com/workspace/sheets/api/guides/configure-mcp-server | 2026-09-17 |
| 18 | `freema/mcp-gsheets`: Node.js **v20+**, Sheets API, service account JSON; `npx -y mcp-gsheets@latest` + `GOOGLE_APPLICATION_CREDENTIALS` (+ `GOOGLE_PROJECT_ID`). | https://github.com/freema/mcp-gsheets | 2026-09-17 |
| 19 | Ключевые tools mcp-gsheets для реестра: `sheets_get_values`, `sheets_update_values`, `sheets_append_values`, `sheets_batch_get_values`, `sheets_get_metadata`, `sheets_check_access`. | https://github.com/freema/mcp-gsheets | 2026-09-17 |
| 20 | `sheets_append_values`: по умолчанию `insertDataOption` = **OVERWRITE** — для реестра явно указывать `INSERT_ROWS`, если нужно сдвигать строки. | https://github.com/freema/mcp-gsheets | 2026-09-17 |
| 21 | Service account видит **только** таблицы, расшаренные на `client_email` из JSON; IAM-роли Cloud **не заменяют** Share файла. | https://developers.google.com/workspace/guides/create-credentials#service-account | 2026-09-17 |
| 22 | `we2go/google-mcp`: `npx google-sheet-mcp init` — wizard SA или OAuth; tools read/write/append range. | https://github.com/we2go/google-mcp | 2026-09-17 |
| 23 | Реестр договоров в Sheets уместен до **200–300** активных договоров при одном владельце таблицы; иначе CLM/1С. | https://dzen.ru/a/anRW32ni3D3wHjQF | 2026-09-17 |
| 24 | Заявки на расход через Forms→Sheets: при **>80–100** заявок/мес Sheets — staging перед ERP/n8n. | https://dzen.ru/a/aoAx4V_t_ztBh5aj | 2026-09-17 |
| 25 | Практика AI+Sheets: после batch-записи **перечитывать** и сверять (API не атомарен) — совпадает с verify-loop MCP. | https://habr.com/ru/articles/1017260/ | 2026-09-17 |

**Не выдумывать:** показы Wordstat; «Sheets-плагин всегда в Marketplace» (проверять на дату публикации); что SA = доступ ко всему Drive; цифру Smithery installs как верифицированный факт; обещание «без программиста» для Path B без упоминания GCP/SA; что Google remote MCP уже GA (это Developer Preview на 2026-09-14).

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

**Пример remote (Path C / Google preview — опциональный блок):**

```json
{
  "mcpServers": {
    "sheets": {
      "url": "https://sheetsmcp.googleapis.com/mcp/v1",
      "auth": {
        "CLIENT_ID": "${env:GOOGLE_SHEETS_MCP_CLIENT_ID}",
        "CLIENT_SECRET": "${env:GOOGLE_SHEETS_MCP_CLIENT_SECRET}",
        "scopes": [
          "https://www.googleapis.com/auth/spreadsheets",
          "https://www.googleapis.com/auth/drive.file"
        ]
      }
    }
  }
}
```

**Тестовый промпт агента (реестр):**

> Подключись к таблице `{SPREADSHEET_ID}`. На листе `Реестр` найди строку, где колонка `doc_key` = `DOG-2026-014`. Прочитай текущие значения колонок `status` и `comment`. Если `status` ≠ «Оплачен», предложи обновление на «На согласовании» и допиши в `comment` сегодняшнюю дату. После write перечитай ту же строку и покажи diff.

---

## FAQ-кандидаты (из карточки)

- **Можно ли без программиста?** — Path A (Marketplace+OAuth): да для пилота; Path B (SA+mcp.json): по инструкции B82/B92, Cursor поможет с JSON; production — 1–2 ч первый реестр.
- **Сколько займёт внедрение?** — SA + mcp.json + один тестовый update: **~1–2 ч**; OAuth-плагин быстрее, если доступен в витрине.
- **Какие риски для данных?** — OAuth = права вашего Google; SA-ключ = все расшаренные файлы; не класть ПДн; подтверждать write-tools; indirect injection из ячеек/писем (Google docs).
- **OAuth или service account?** — OAuth для личного пилота; SA для командного реестра, cron, минимального blast radius.
- **Чем отличается от B82?** — B82 = Python/Node скрипт пишет в staging; B92 = Agent в Cursor правит через MCP без скрипта.
- **Работает ли в Cloud Agents?** — да при Team MCP в Dashboard; локальный OAuth не переезжает автоматически — для облака чаще SA.
- **Что такое Google remote Sheets MCP?** — официальный endpoint `sheetsmcp.googleapis.com`, Developer Preview; для Cursor через Streamable HTTP + OAuth; для финконтура надёжнее Path B (SA), пока preview.

---

## CTA / interlink

- Internal: `/avtomatizaciya-finansov-no-code/`, `/obezlichivanie-dannyh-chatgpt-finansist/`, `/google-sheets-api-integraciya-finotdel/` (B82), `/mcp-cursor-finansist-instrumenty/` (B21)
- Соседние реестры: B51, B58, B83; ротация ключа: B93
- CTA: `https://club.koda-fd.ru/?utm_source=blog&utm_medium=article&utm_campaign=mcp-google-sheets-cursor-reestry` (≤2), `https://t.me/finance_modern?utm_source=blog&utm_medium=article` (≤2)

---

## Handoff marker

`=== EXCALIBUR BLOG RESEARCH ===` — см. `.cursor/excalibur-blog-handoff.md`
