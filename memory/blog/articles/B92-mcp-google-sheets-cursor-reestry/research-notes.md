# Research notes — B92

**topic_id:** B92  
**slug:** mcp-google-sheets-cursor-reestry  
**h1:** Как подключить MCP к Google Sheets в Cursor и править реестры без копипаста  
**research_date:** 2026-09-09  
**run_date:** 2026-09-09  
**publish_target:** koda-fd.ru/blog  
**utility_gate:** PASS (`how_to`, mode B)  
**author_id:** olga-kondratskaya  
**related_internal:** `/avtomatizaciya-finansov-no-code/`, `/obezlichivanie-dannyh-chatgpt-finansist/`, `/google-sheets-api-integraciya-finotdel/` (B82), `/mcp-cursor-finansist-instrumenty/` (B21)  
**sibling_queue / published:** B51 реестр договоров, B58 УПД, B83 SaaS, B93 ротация SA  
**cover_scene_hint:** abstract holographic finance automation dark #0a0a0f purple #8b5cf6, no text  
**utility_verdict:** PASS

---

## utility_verdict

**PASS** — utility-only how_to. Читатель получает рабочий маршрут: выбрать путь (официальный remote Sheets MCP Google **или** локальный community MCP на service account), подготовить реестр без сырых ПДн, прописать `mcp.json` в Cursor, прогнать сценарий «найти строку по `doc_key` → обновить статус → перечитать», закрепить human-approval на write. Не новость про Workspace-плагины, не обзор 25 MCP-серверов, не туториал «напиши MCP с нуля».

---

## reader_outcome

После гайда финансист сможет подключить Google Sheets к Cursor через MCP, дать агенту доступ только к нужному реестру и править статусы/комментарии по `doc_key` без копипаста таблицы в чат, с проверкой результата перечиткой диапазона.

---

## action_outline

1. **Решить, нужен ли MCP Sheets** — реестр уже в Google Sheets (договоры, УПД, SaaS, заявки), правки повторяются, устали таскать диапазоны в чат; **не** делать, если нужен жёсткий audit trail / сотни таблиц с enterprise ACL — тогда 1С/CLM, Sheets только staging.
2. **Выбрать путь** — **Path A (официальный remote):** `https://sheetsmcp.googleapis.com/mcp/v1` + OAuth (права пользователя Google); **Path B (финконтур):** community MCP (`mcp-gsheets` / `mcp-google-sheets`) + **service account** — расшарить только нужные реестры. Marketplace Cursor на 09.09.2026 подтверждает **Drive / Gmail / Calendar**, отдельного Sheets-плагина в changelog нет — на него не опираться.
3. **Подготовить реестр** — одна строка = одна сущность; стабильный `doc_key`; лист `staging` для импорта; в облако без сырых ПДн (ИНН/сумма/статус — да; паспорт, полные ФИО — нет); interlink `/obezlichivanie-dannyh-chatgpt-finansist/`.
4. **Path A: GCP + remote MCP** — проект → `gcloud services enable sheets.googleapis.com` и `sheetsmcp.googleapis.com` → OAuth consent scopes (`spreadsheets`, `drive.file` / по доке Google) → в Cursor `mcp.json` с `"url": "https://sheetsmcp.googleapis.com/mcp/v1"` (+ auth при необходимости) → пройти OAuth.
5. **Path B: SA + share** — Google Cloud project → Sheets API → service account → JSON-ключ → `client_email` → «Поделиться» на файл реестра с ролью **Редактор** (без «Уведомить»); ключ **не** в git.
6. **Path B: mcp.json** — глобально `~/.cursor/mcp.json` или проектно `.cursor/mcp.json`; пример: `npx -y mcp-gsheets@latest` + `GOOGLE_APPLICATION_CREDENTIALS`, либо `uvx mcp-google-sheets@latest` + `SERVICE_ACCOUNT_PATH` / `DRIVE_FOLDER_ID`.
7. **Проверить подключение** — перезапуск Cursor; Customize → MCPs → зелёный статус; Output → **MCP Logs**; живой read «прочитай A1:G5 листа Реестр» / `sheets_check_access` / `get_values`.
8. **Рабочий сценарий реестра** — промпт с DoD: metadata → найти строку по `doc_key` → update только колонок статуса/комментария → get_values на ту же строку → сверка; **approval на каждый write-tool**; учитывать риск indirect prompt injection в ячейках.
9. **Эксплуатация** — allowlist write-tools; квоты Sheets API (300/мин проект, 60/мин на пользователя-identity — SA = один user); ротация ключа (B93); при >80–100 заявок/мес — n8n/ERP, Sheets staging.

**Workflow:**  
`Реестр в Sheets → (OAuth remote | SA share) → mcp.json в Cursor → Agent read/update по doc_key → перечитка → регламент CFO`

---

## Яндекс Wordstat (MCP user-mcp-kv)

⚠️ **WORDSTAT AUTH WARNING:** сервер MCP `user-mcp-kv` в этой Cloud-сессии **не подключён** (в каталоге dynamic tools: `cursor`, `Cursor Automation Tools`, `cursor-cloud`, `cursor-subscriptions`). Вызов `wordstat_get_top_requests` **не выполнен**. Точные показы/мес **не получены** и **не выдуманы**.

Обновление токена / подключение MCP-KV: https://oauth.yandex.ru/authorize?response_type=token&client_id=c654b948515a4a07a4c89648a0831d40

### Таблица спроса (Wordstat)

| Фраза | Показы в месяц |
| --- | --- |
| mcp google sheets cursor | *не получено — MCP недоступен* |
| google sheets mcp | *не получено — MCP недоступен* |
| cursor mcp | *не получено — MCP недоступен* |
| подключить mcp cursor | *не получено — MCP недоступен* |
| автоматизация финотдела | *не получено — MCP недоступен* |
| mcp сервер google sheets | *не получено — MCP недоступен* |

**Экспертная семантика (LSI для writer, без цифр спроса):**

| Кластер | Фразы | Роль |
| --- | --- | --- |
| Primary | mcp google sheets cursor, google sheets mcp cursor | H1, title |
| Official | sheetsmcp.googleapis.com, google sheets mcp server configure | Path A |
| Setup | mcp.json cursor, uvx mcp-google-sheets, mcp-gsheets service account | H2 пошагово |
| Finance | автоматизация финотдела google sheets, реестр без копипаста cursor | угол КОДА |
| Registry | реестр договоров / УПД / saas sheets, doc_key update | кейсы + interlink |
| Security | service account json не в git, oauth scopes минимум, prompt injection sheets | FAQ |
| Ops | MCP Logs cursor, 429 sheets api, sheets_check_access | troubleshooting |

**SEO-вывод:** живой SERP 09.09.2026 по `mcp google sheets cursor` — официальные доки Cursor MCP + **новая официальная дока Google Sheets MCP** + EN community setup (uvx / npx). RU how-to «финансист + реестр + Cursor» почти нет. Угол КОДА: правка управленческих реестров через MCP без копипаста, с выбором Path A vs Path B и fork от B82 (скрипт) / B21 (общий MCP).

---

## SERP (WebSearch Cursor, 2026-09-09)

`research-serp.json` шаг 0: **urls=0**, SSL timeout DuckDuckGo — **игнорировать**. Источник SERP ниже — нативный WebSearch.

### Primary: `mcp google sheets cursor 2026` / how-to connect

| # | URL | Тип | Пробел для КОДА |
| --- | --- | --- | --- |
| 1 | https://developers.google.com/workspace/sheets/api/guides/configure-mcp-server | Официальный Google Sheets MCP | Нет реестров финотдела / SA |
| 2 | https://cursor.com/docs/mcp | Cursor MCP reference | Общий протокол |
| 3 | https://cursor.com/help/customization/mcp | Help: mcp.json, OAuth, approvals | Нет Sheets-кейса |
| 4 | https://mcpyet.com/mcp/google-sheets/ | Каталог: remote URL + Cursor snippet | Без finance angle |
| 5 | https://github.com/mariadb-RupeshBiswas/google-sheets-mcp/blob/main/docs/EDITOR_SETUP.md | Community: uvx `g-sheet-mcp` в Cursor | EN, не CFO |
| 6 | https://www.truefoundry.com/blog/mcp-servers-in-cursor-setup-configuration-and-security-guide | Security/setup 2026 | Общий MCP |
| 7 | https://pypi.org/project/mcp-google-sheets/ | xing5 `mcp-google-sheets` v0.6.3 | SA + tool filter |
| 8 | https://zenn.dev/icare/articles/15fe5e2ab5930c | JP how-to Cursor×Sheets MCP | Не RU finance |

### Marketplace / Workspace plugins (важно для честного Path A)

| # | URL | Тип | Вывод |
| --- | --- | --- | --- |
| 1 | https://cursor.com/changelog/google-workspace-plugins | Changelog 03.08.2026 | Только **Drive, Gmail, Calendar** |
| 2 | https://aicatchup.com/news/cursor-google-workspace-plugins | Re-verify | Docs/Sheets **не** в официальном changelog |
| 3 | https://forum.cursor.com/t/grok-bot-drive-mcp-should-write-google-docs-body-and-sheet-cells-not-only-file-metadata/169971 | Forum 08.2026 | Drive MCP **не** пишет ячейки Sheet |
| 4 | https://composio.dev/toolkits/googlesheets/framework/cursor | SaaS-посредник | Альтернатива, не рекомендуем как default |

### Secondary RU: автоматизация финотдела / реестры

| # | URL | Тип | Пробел |
| --- | --- | --- | --- |
| 1 | https://dzen.ru/a/aoAx4V_t_ztBh5aj | Forms→реестр Sheets (КОДА) | Без MCP |
| 2 | https://mcp-catalog.ru/servers/google-sheets | RU каталог community MCP | Установка, не реестр |
| 3 | https://mcp-catalog.ru/servers/gsheets | freema/mcp-gsheets | Dev-фокус |
| 4 | https://koda-fd.ru/blog/google-sheets-api-integraciya-finotdel/ | B82 published | Скрипт, не Agent+MCP |
| 5 | https://koda-fd.ru/blog/mcp-cursor-finansist-instrumenty/ | B21 published | Общий MCP, не Sheets |

### Конкурентный зазор (угол КОДА)

1. **Finance-first** — «перестань копировать реестр в чат: agent правит строку по `doc_key`».
2. **Два пути с честным статусом Marketplace** — официальный remote Sheets MCP (OAuth) vs SA+community для production финконтура; **не** обещать нативный Sheets-плагин Cursor Marketplace.
3. **Связка с реестрами серии** — B51/B58/B83; MCP = слой правок поверх уже спроектированной таблицы.
4. **Security** — минимальный share, ключ вне git, approval write-tools, Google warning про indirect prompt injection.
5. **Verify loop** — после write всегда get_values; Connected ≠ authorized.
6. **Fork от B82** — те же SA+share, но правки через Agent+MCP без написания скрипта.

---

## Таблица фактов

| # | Утверждение | Источник | Дата проверки |
| --- | --- | --- | --- |
| 1 | MCP подключает Cursor к внешним tools; Agent вызывает их в чате. | https://cursor.com/help/customization/mcp | 2026-09-09 |
| 2 | Конфиг: `.cursor/mcp.json` (проект) и `~/.cursor/mcp.json` (глобальный); при совпадении имени побеждает **проектный**. | https://cursor.com/help/customization/mcp | 2026-09-09 |
| 3 | Локальный сервер: `command`/`args`/`env`; удалённый: поле `url` (+ опционально `headers` / static OAuth `auth`). | https://cursor.com/docs/mcp ; https://cursor.com/help/customization/mcp | 2026-09-09 |
| 4 | После ручного `mcp.json` — сохранить и **перезапустить Cursor**. | https://cursor.com/help/customization/mcp | 2026-09-09 |
| 5 | По умолчанию Agent запрашивает approval перед MCP-tool; с Cursor 3.6+ — Auto-review / allowlist / `permissions.json`. | https://cursor.com/help/customization/mcp | 2026-09-09 |
| 6 | Troubleshooting: Output → **MCP Logs** (`Ctrl+Shift+U` / `Cmd+Shift+U`). | https://cursor.com/help/customization/mcp | 2026-09-09 |
| 7 | Cloud Agents поддерживают MCP из Cloud Agents dashboard / Team Integrations & MCP. | https://cursor.com/help/customization/mcp | 2026-09-09 |
| 8 | Официальный remote Google Sheets MCP: URL `https://sheetsmcp.googleapis.com/mcp/v1`, transport HTTP, auth OAuth 2.0. | https://developers.google.com/workspace/sheets/api/guides/configure-mcp-server | 2026-09-09 |
| 9 | Нужно включить API: `sheets.googleapis.com` и MCP-сервис `sheetsmcp.googleapis.com`. | https://developers.google.com/workspace/sheets/api/guides/configure-mcp-server | 2026-09-09 |
| 10 | Tools официального Sheets MCP: `get_values`, `get_spreadsheet`, `update_spreadsheet`, `update_values`, `update_formulas`, `insert_dimension`. | https://developers.google.com/workspace/sheets/api/guides/configure-mcp-server | 2026-09-09 |
| 11 | Scopes OAuth для Sheets MCP включают `spreadsheets`, `spreadsheets.readonly`, `drive.file`, `drive.readonly` (по доке Google). | https://developers.google.com/workspace/sheets/api/guides/configure-mcp-server | 2026-09-09 |
| 12 | Google предупреждает про **indirect prompt injection**: MCP host может читать/менять/удалять данные Google Account — только trusted tools, review write-действий. | https://developers.google.com/workspace/sheets/api/guides/configure-mcp-server | 2026-09-09 |
| 13 | Changelog Cursor 03.08.2026: плагины **Drive, Gmail, Calendar**; Sheets в этом документе **не расписан**. | https://cursor.com/changelog/google-workspace-plugins | 2026-09-09 |
| 14 | Re-verify (aicatchup): упоминания Docs/Sheets в сторонних статьях ошибочно атрибутировали changelog; в официальном тексте их нет. | https://aicatchup.com/news/cursor-google-workspace-plugins | 2026-09-09 |
| 15 | Drive MCP / connector пишет file-level операции; **не** заменяет Sheets cell update (forum / product feedback). | https://forum.cursor.com/t/grok-bot-drive-mcp-should-write-google-docs-body-and-sheet-cells-not-only-file-metadata/169971 | 2026-09-09 |
| 16 | `mcp-google-sheets` (PyPI) актуальная версия **0.6.3** (2026-05-14); запуск через `uvx mcp-google-sheets@latest`; рекомендуют Service Account. | https://pypi.org/project/mcp-google-sheets/ | 2026-09-09 |
| 17 | Env для SA: `SERVICE_ACCOUNT_PATH` (+ опционально `DRIVE_FOLDER_ID`); альтернативы: `CREDENTIALS_CONFIG` (base64), ADC/`GOOGLE_APPLICATION_CREDENTIALS`. | https://pypi.org/project/mcp-google-sheets/ ; https://github.com/xing5/mcp-google-sheets | 2026-09-09 |
| 18 | По умолчанию ~**19 tools** (~13K tokens); фильтр `--include-tools` / `ENABLED_TOOLS` (например `get_sheet_data,update_cells,list_spreadsheets,list_sheets`). | https://pypi.org/project/mcp-google-sheets/ | 2026-09-09 |
| 19 | Community Cursor setup: `uvx` + `g-sheet-mcp` / зелёный статус в MCP panel / verify list sheets. | https://github.com/mariadb-RupeshBiswas/google-sheets-mcp/blob/main/docs/EDITOR_SETUP.md | 2026-09-09 |
| 20 | `freema/mcp-gsheets`: Node 20+, `npx -y mcp-gsheets@latest`, env `GOOGLE_APPLICATION_CREDENTIALS`; tools `sheets_get_values`, `sheets_update_values`, `sheets_append_values`, `sheets_check_access` и др. | https://github.com/freema/mcp-gsheets | 2026-09-09 |
| 21 | Квоты Sheets API / Sheets MCP: **300** req/min на проект и **60** req/min на user per project (read и write отдельно); превышение → HTTP **429**; batch = 1 запрос. | https://developers.google.com/workspace/sheets/api/limits | 2026-09-09 |
| 22 | Стоимость query у Sheets MCP tools: каждый listed tool = 1 read или 1 write request. | https://developers.google.com/workspace/sheets/api/limits | 2026-09-09 |
| 23 | Standard Sheets API сейчас без доп. платы; превышение квот **планируется тарифицировать later in 2026**. | https://developers.google.com/workspace/sheets/api/limits | 2026-09-09 |
| 24 | Рекомендуемый max payload ~**2 MB**; таймаут обработки запроса **180 с**. | https://developers.google.com/workspace/sheets/api/limits | 2026-09-09 |
| 25 | Вызовы от service account считаются одним user/account для per-user quota. | https://developers.google.com/workspace/sheets/api/limits | 2026-09-09 |
| 26 | Заявки Forms→Sheets: при **>80–100** заявок/мес Sheets — staging перед ERP/n8n. | https://dzen.ru/a/aoAx4V_t_ztBh5aj | 2026-09-09 |
| 27 | Cursor static OAuth redirect URLs для MCP: `https://www.cursor.com/agents/mcp/oauth/callback` и `http://localhost:8787/callback` (desktop). | https://cursor.com/docs/mcp | 2026-09-09 |

**Не выдумывать:** показы Wordstat; «Sheets-плагин всегда в Cursor Marketplace»; что SA = доступ ко всему Drive; ROI из fact-bank про контент-завод; обещание «без программиста» для Path B без GCP/SA.

**fact-bank.md:** прямых фактов MCP+Sheets нет — опираться на таблицу выше. Контент-заводные цифры **не тянуть**.

---

## Структура H2 для writer (из карточки B92)

1. Когда это нужно финотделу (и когда нет)  
2. Подготовка данных и безопасность (без сырых ПДн в облако)  
3. Пошаговая настройка / сценарий (Path A remote vs Path B SA)  
4. Проверка результата и типичные ошибки  
5. Что автоматизировать дальше  

**Пример mcp.json — Path A (официальный remote):**

```json
{
  "mcpServers": {
    "sheets": {
      "url": "https://sheetsmcp.googleapis.com/mcp/v1"
    }
  }
}
```

*(OAuth/consent по доке Google + redirect Cursor при необходимости.)*

**Пример mcp.json — Path B (SA, freema):**

```json
{
  "mcpServers": {
    "mcp-gsheets": {
      "command": "npx",
      "args": ["-y", "mcp-gsheets@latest"],
      "env": {
        "GOOGLE_APPLICATION_CREDENTIALS": "/absolute/path/to/sa-registry.json"
      }
    }
  }
}
```

**Пример mcp.json — Path B (xing5 / uvx):**

```json
{
  "mcpServers": {
    "google-sheets": {
      "command": "uvx",
      "args": ["mcp-google-sheets@latest"],
      "env": {
        "SERVICE_ACCOUNT_PATH": "/absolute/path/to/sa-registry.json",
        "DRIVE_FOLDER_ID": "optional-folder-id",
        "ENABLED_TOOLS": "get_sheet_data,update_cells,list_spreadsheets,list_sheets"
      }
    }
  }
}
```

**Тестовый промпт агента (реестр):**

> Подключись к таблице `{SPREADSHEET_ID}`. На листе `Реестр` найди строку, где колонка `doc_key` = `DOG-2026-014`. Прочитай `status` и `comment`. Если `status` ≠ «Оплачен», предложи обновление на «На согласовании» и допиши в `comment` дату 2026-09-09. После write перечитай ту же строку и покажи diff.

---

## FAQ-кандидаты

- **Можно ли без программиста?** — Path A (remote OAuth): ближе к «да» для пилота; Path B (SA+mcp.json): по чеклисту GCP ~1–2 ч первый реестр.
- **Сколько займёт внедрение?** — SA + mcp.json + один тестовый update: **~1–2 ч**.
- **Какие риски для данных?** — OAuth = права вашего Google; SA-ключ = все расшаренные файлы; не класть ПДн; подтверждать write; prompt injection из ячеек.
- **OAuth или service account?** — OAuth (Path A) для личного пилота; SA (Path B) для командного реестра и минимального blast radius.
- **Чем отличается от B82?** — B82 = скрипт пишет в staging; B92 = Agent в Cursor через MCP без скрипта.
- **Есть ли плагин Sheets в Cursor Marketplace?** — на 09.09.2026 официальный changelog подтверждает Drive/Gmail/Calendar; для ячеек — Sheets MCP (Google remote или community).
- **Работает ли в Cloud Agents?** — да при отдельной настройке MCP в dashboard; локальный интерактивный OAuth не «переезжает» сам.

---

## CTA / interlink

- Internal: `/avtomatizaciya-finansov-no-code/`, `/obezlichivanie-dannyh-chatgpt-finansist/`, `/google-sheets-api-integraciya-finotdel/` (B82), `/mcp-cursor-finansist-instrumenty/` (B21), реестры B51/B58/B83  
- CTA: `https://club.koda-fd.ru/?utm_source=blog&utm_medium=article&utm_campaign=mcp-google-sheets-cursor-reestry` (≤2), `https://t.me/finance_modern?utm_source=blog&utm_medium=article` (≤1–2)

---

## Handoff marker

`=== EXCALIBUR BLOG RESEARCH ===` — см. `.cursor/excalibur-blog-handoff.md`
