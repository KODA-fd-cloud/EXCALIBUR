# Research notes — B92

**topic_id:** B92  
**slug:** mcp-google-sheets-cursor-reestry  
**h1:** Как подключить MCP к Google Sheets в Cursor и править реестры без копипаста  
**research_date:** 2026-09-06  
**publish_target:** koda-fd.ru/blog  
**utility_gate:** PASS (`how_to`, mode B) — подтверждено `excalibur_blog_utility_gate.py --topic-id B92`  
**author_id:** olga-kondratskaya  
**related_internal:** `/avtomatizaciya-finansov-no-code/`, `/obezlichivanie-dannyh-chatgpt-finansist/`  
**sibling_queue:** B82 (Sheets API + SA), B21 (MCP в Cursor общий), B51/B58/B83 (реестры в Sheets), B93 (ротация SA)  
**cover_scene_hint:** abstract holographic finance automation dark #0a0a0f purple #8b5cf6, no text

---

## utility_verdict

**PASS** — тема utility-only how_to. Читатель получает рабочие маршруты подключения Google Sheets к Cursor через MCP (Marketplace/OAuth-плагин **или** community `mcp-gsheets` на service account **или** remote Google `sheetsmcp.googleapis.com`), подготовку реестра под агентные правки, тестовый сценарий «найти строку → обновить статус → перечитать», чеклист безопасности для финданных и troubleshooting. Не новость «Cursor открыл Workspace», не обзор 25 MCP-серверов, не туториал «напиши свой MCP с нуля».

---

## reader_outcome

После гайда финансист сможет подключить MCP Google Sheets в Cursor, дать агенту доступ только к рабочему реестру (через service account или OAuth), попросить обновить статус строки или дописать поля без копирования таблицы в чат и проверить результат перечиткой диапазона через MCP-tool.

---

## action_outline

1. **Решить, нужен ли MCP Sheets** — реестр уже в Google Sheets (договоры, УПД, SaaS, заявки на расход), правки повторяются, устали таскать диапазоны в чат; **не** делать, если нужен жёсткий audit trail / сотни таблиц с enterprise ACL — тогда 1С/CLM, Sheets только staging.
2. **Выбрать путь подключения** — **Path A (пилот):** плагин/MCP из Cursor Marketplace или Customize → OAuth личного Google; **Path B (финконтур):** `freema/mcp-gsheets` + service account — расшарить только нужные реестры, ключ в `env`, без доступа агента ко всему Drive (см. B82, B93); **Path C (официальный remote Google, advanced):** URL `https://sheetsmcp.googleapis.com/mcp/v1` + OAuth client в GCP — для команд, готовых включать Sheets MCP API и consent screen.
3. **Подготовить реестр** — одна строка = одна сущность; стабильный `doc_key`; лист `staging` для импорта; в облако без сырых ПДн (ИНН/сумма/статус — да; паспорт, полные ФИО — нет); interlink `/obezlichivanie-dannyh-chatgpt-finansist/`.
4. **Path B: Google Cloud + SA** — проект → включить **Google Sheets API** → service account → JSON-ключ → скопировать `client_email` → «Поделиться» на файл реестра с ролью **Редактор** (без «Уведомить»).
5. **Path B: mcp.json в Cursor** — глобально `~/.cursor/mcp.json` или проектно `.cursor/mcp.json`; блок `mcp-gsheets` с `npx -y mcp-gsheets@latest` и `GOOGLE_APPLICATION_CREDENTIALS` (абсолютный путь); JSON-ключ **не** в git.
6. **Path A: Marketplace / Customize** — Customize → MCPs/Plugins → поиск Google Sheets → Add → OAuth; минимальные scopes; учесть: changelog 03.08.2026 детально описывает Drive/Gmail/Calendar; Sheets в анонсах упоминается, но витрина плагинов может меняться — проверять на дату установки.
7. **Проверить подключение** — перезапуск Cursor; Customize → MCPs → зелёный статус; Output → **MCP Logs**; tool `sheets_check_access` (Path B) или живой запрос «прочитай A1:C5 листа Реестр».
8. **Рабочий сценарий реестра** — промпт с DoD: metadata/get → найти строку по `doc_key` → update/append только в колонки статуса/комментария → get_values на ту же строку → сверка; human approval на каждый write-tool.
9. **Эксплуатация и рост** — allowlist write-tools; ротация ключа SA (B93); при >80–100 заявок/мес или audit — n8n/ERP, Sheets остаётся staging; соседние реестры B51/B58/B83.

**Workflow для статьи:**  
`Реестр в Sheets → (SA share | OAuth plugin | Google remote MCP) → MCP в Cursor → Agent read/update по doc_key → перечитка диапазона → регламент CFO`

---

## Яндекс Wordstat (MCP user-mcp-kv)

⚠️ **WORDSTAT AUTH WARNING:** сервер MCP `user-mcp-kv` в этой Cloud-сессии **не подключён** (в каталоге dynamic tools доступны только `cursor`, `Cursor Automation Tools`, `cursor-cloud`, `cursor-subscriptions`). Вызов `wordstat_get_top_requests` **не выполнен**. Точные показы/мес **не получены** и **не выдуманы**.

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

**SEO-вывод:** SERP по `mcp google sheets cursor` (WebSearch 06.09.2026) — официальные docs Cursor MCP, community MCP (freema, xing5, Demontie), **новый официальный remote Google Sheets MCP** (`sheetsmcp.googleapis.com`), SaaS-посредники (Merge, CData, Composio). Почти нет RU how-to «финансист + реестр + Cursor». Угол КОДА: **правка управленческих реестров через MCP без копипаста**, с веткой SA для безопасности и явным сравнением с B82 (скрипт) и B21 (общий MCP).

---

## SERP (WebSearch Cursor, 06.09.2026)

Приоритет — живой WebSearch; `research-serp.json` (шаг 0, 06.09.2026) — черновик URL; query `2026 2026` и часть сниппетов **нерелевантны** — не копировать.

### Primary: `mcp google sheets cursor 2026`

| # | URL | Тип | Пробел для КОДА |
| --- | --- | --- | --- |
| 1 | https://cursor.com/help/customization/mcp | Help: mcp.json, OAuth, approvals, MCP Logs | Канон шагов; нет Sheets-кейса |
| 2 | https://cursor.com/docs/mcp | Официальный reference | Нет реестров финотдела |
| 3 | https://github.com/freema/mcp-gsheets | Community MCP (SA), Node 20+ | EN; dev-фокус, не CFO |
| 4 | https://developers.google.com/workspace/sheets/api/guides/configure-mcp-server | **Официальный remote Sheets MCP Google** | Antigravity/Claude; Cursor в «Others» |
| 5 | https://mcp.directory/servers/google-sheets | Каталог xing5/`uvx mcp-google-sheets` | Dev install, не finance |
| 6 | https://github.com/Demontie/mcp-google-sheets | Node MCP + Cursor config | Локальный clone, не реестры |
| 7 | https://www.merge.dev/blog/google-sheets-mcp-cursor | Merge Agent Handler → Cursor | SaaS-посредник |
| 8 | https://www.cdata.com/kb/tech/gsheets-mcp-cursor.rst | CData MCP Server | Enterprise driver |

### News / official Workspace

| # | URL | Тип | Пробел |
| --- | --- | --- | --- |
| 1 | https://cursor.com/changelog/google-workspace-plugins | Changelog 03.08.2026 | Drive/Gmail/Calendar детально; Sheets в теле changelog **не расписан** |
| 2 | https://developers.google.com/workspace/guides/configure-mcp-servers | Google Workspace MCP servers | Endpoint Sheets: `sheetsmcp.googleapis.com/mcp/v1` |
| 3 | https://mayai.ru/cursor-otkryl-gmail-i-sheets-agentam/ | RU разбор релиза | Контент-завод; мало SA/реестров |
| 4 | https://vibecoding.ru/news/2026/08/03/cursor-google-workspace-plugins | RU новость (авг) | Статус витрины Docs/Sheets мог меняться — перепроверять |
| 5 | https://mcpyet.com/mcp/google-sheets/ | Верификация official Sheets MCP | Каталог; не finance workflow |

### Secondary: `автоматизация финотдела` / реестры

| # | URL | Тип | Пробел |
| --- | --- | --- | --- |
| 1 | https://koda-fd.ru/blog/ai-dlya-finansista-2026/ | Hub КОДА | Нет MCP Cursor |
| 2 | https://dzen.ru/a/anRW32ni3D3wHjQF | Реестр договоров Sheets | Без MCP |
| 3 | https://mcpservers.org/ru/servers/dudegladiator/spreadsheet-mcp | RU каталог spreadsheet-mcp | Dev setup |
| 4 | https://cursor.com/ru/help/customization/mcp | RU help MCP | Без Sheets |

### H1-aligned / RU setup

| # | URL | Заметка |
| --- | --- | --- |
| 1 | https://mcp-catalog.ru/tutorials/gsheets-cursor | RU: freema/mcp-gsheets в Cursor |
| 2 | https://neurinix.com/2026/06/21/podklyuchenie-mcp-cursor/ | Общий MCP setup RU |
| 3 | https://dzen.ru/a/ak6DMsDdYlsmEkki | Plugins vs mcp.json (дубли) |

### Конкурентный зазор (угол КОДА)

1. **Finance-first** — не «подключи Sheets к Cursor», а «перестань копировать реестр в чат: agent правит строку по `doc_key`».
2. **Три пути с выбором** — OAuth-плагин для пилота vs SA+mcp-gsheets для production финконтура vs Google remote MCP (GCP OAuth) для advanced; honest note про статус Marketplace Sheets.
3. **Связка с реестрами серии** — договоры (B51), УПД (B58), SaaS (B83); MCP = слой правок поверх уже спроектированной таблицы.
4. **Security block** — минимальный share, ключ вне git, approval tools, indirect prompt injection (Google docs), обезличивание.
5. **Verify loop** — после write всегда get_values; «Connected ≠ authorized».
6. **Fork от B82** — B82 = свой Python-скрипт; B92 = те же SA+share, но правки через Agent+MCP без написания кода.

---

## Таблица фактов

| # | Утверждение | Источник | Дата проверки |
| --- | --- | --- | --- |
| 1 | MCP подключает Cursor к внешним инструментам; Agent вызывает tools в чате. | https://cursor.com/help/customization/mcp | 2026-09-06 |
| 2 | Конфиг MCP: проектный `.cursor/mcp.json` + глобальный `~/.cursor/mcp.json`; при совпадении имени побеждает **проектный**. | https://cursor.com/help/customization/mcp | 2026-09-06 |
| 3 | Локальный MCP: `command`, `args`, `env`; удалённый — поле `url` (+ опционально `headers`). | https://cursor.com/help/customization/mcp | 2026-09-06 |
| 4 | One-click: Customize → MCPs → Add to Cursor; после ручного `mcp.json` — **перезапуск Cursor**. | https://cursor.com/help/customization/mcp | 2026-09-06 |
| 5 | По умолчанию Agent **запрашивает approval** перед MCP-tool; с Cursor 3.6+ — Auto-review / allowlist (`permissions.json`). | https://cursor.com/help/customization/mcp | 2026-09-06 |
| 6 | Troubleshooting: Output → **MCP Logs** (`Ctrl+Shift+U` / `Cmd+Shift+U`). | https://cursor.com/help/customization/mcp | 2026-09-06 |
| 7 | Cloud Agents поддерживают MCP из Cloud Agents dashboard / Team Integrations & MCP. | https://cursor.com/help/customization/mcp | 2026-09-06 |
| 8 | 03.08.2026 Cursor анонсировал Google Workspace plugins: Drive, Gmail, Calendar из Marketplace/Customize. | https://cursor.com/changelog/google-workspace-plugins | 2026-09-06 |
| 9 | В changelog 03.08.2026 Sheets/Docs **не детализированы** (перечислены Drive, Gmail, Calendar). | https://cursor.com/changelog/google-workspace-plugins | 2026-09-06 |
| 10 | Google публикует **официальный remote Sheets MCP**: endpoint `https://sheetsmcp.googleapis.com/mcp/v1`; нужны Sheets API + `sheetsmcp.googleapis.com`, OAuth 2.0. | https://developers.google.com/workspace/sheets/api/guides/configure-mcp-server | 2026-09-06 |
| 11 | Tools официального Google Sheets MCP: `get_values`, `get_spreadsheet`, `update_spreadsheet`, `update_values`, `update_formulas`, `insert_dimension`. | https://developers.google.com/workspace/sheets/api/guides/configure-mcp-server | 2026-09-06 |
| 12 | Google явно предупреждает об **indirect prompt injection** при MCP+Sheets; рекомендует human review действий и не кормить агента неtrusted таблицами. | https://developers.google.com/workspace/sheets/api/guides/configure-mcp-server | 2026-09-06 |
| 13 | Scopes для Google Sheets MCP (consent): `drive.readonly`, `drive.file`, `spreadsheets.readonly`, `spreadsheets`. | https://developers.google.com/workspace/sheets/api/guides/configure-mcp-server | 2026-09-06 |
| 14 | `freema/mcp-gsheets`: Node.js **v20+**, Sheets API, SA JSON; установка `npx -y mcp-gsheets@latest` + `GOOGLE_APPLICATION_CREDENTIALS`. | https://github.com/freema/mcp-gsheets | 2026-09-06 |
| 15 | Ключевые tools mcp-gsheets для реестра: `sheets_get_values`, `sheets_update_values`, `sheets_append_values`, `sheets_batch_get_values`, `sheets_get_metadata`, `sheets_check_access`. | https://github.com/freema/mcp-gsheets | 2026-09-06 |
| 16 | Альтернативный auth mcp-gsheets: `GOOGLE_PRIVATE_KEY` + `GOOGLE_CLIENT_EMAIL` (без файла ключа). | https://github.com/freema/mcp-gsheets | 2026-09-06 |
| 17 | Service account видит **только** таблицы, расшаренные на `client_email`; IAM Cloud **не заменяет** Share файла. | https://developers.google.com/workspace/guides/create-credentials#service-account | 2026-09-06 |
| 18 | Scope `https://www.googleapis.com/auth/spreadsheets` — read/write расшаренных таблиц; применяется ко **всему файлу**. | https://developers.google.com/workspace/sheets/api/scopes | 2026-09-06 |
| 19 | Квота Sheets API write: **300 запросов/мин** на проект; превышение → HTTP **429**. | https://developers.google.com/workspace/sheets/api/limits | 2026-09-06 |
| 20 | xing5/`mcp-google-sheets`: Python/`uvx mcp-google-sheets@latest`; tools `get_sheet_data`, `update_cells`; SA или OAuth. | https://mcp.directory/servers/google-sheets | 2026-09-06 |
| 21 | «Connected» в Tools & MCP **не гарантирует** успешный Google OAuth — проверять живым read/write. | https://mayai.ru/cursor-otkryl-gmail-i-sheets-agentam/ | 2026-09-06 |
| 22 | Cloud Agents **не наследуют** интерактивный Google OAuth с локального Cursor автоматически — нужен отдельный коннектор/SA/dashboard MCP. | https://mayai.ru/cursor-otkryl-gmail-i-sheets-agentam/ ; https://cursor.com/help/customization/mcp | 2026-09-06 |
| 23 | Реестр договоров в Sheets уместен до **200–300** активных договоров при одном владельце таблицы; иначе CLM/1С. | https://dzen.ru/a/anRW32ni3D3wHjQF | 2026-09-06 |
| 24 | Заявки на расход через Forms→Sheets: при **>80–100** заявок/мес Sheets — staging перед ERP/n8n. | https://dzen.ru/a/aoAx4V_t_ztBh5aj | 2026-09-06 |
| 25 | В 2026 финотдел автоматизирует классификацию платежей, сверки, УО — Sheets+MCP как **transport правок**, не GL. | https://koda-fd.ru/blog/ai-dlya-finansista-2026/ | 2026-09-06 |

**Не выдумывать:** показы Wordstat; «Sheets-плагин всегда в Marketplace» (проверять на дату публикации); что SA = доступ ко всему Drive; цифру Smithery «56k installs» как верифицированный факт; что Google remote MCP «из коробки в Cursor Marketplace» без OAuth client в GCP; обещание «без программиста» для Path B/C без упоминания GCP/SA.

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

**Пример remote Google Sheets MCP (Path C — кратко в FAQ/advanced):**

```json
{
  "mcpServers": {
    "sheets": {
      "url": "https://sheetsmcp.googleapis.com/mcp/v1"
    }
  }
}
```

(Для production Path C обычно нужны OAuth client ID/secret по гайду Google; в Cursor — поле `url` + auth flow клиента.)

**Тестовый промпт агента (реестр):**

> Подключись к таблице `{SPREADSHEET_ID}`. На листе `Реестр` найди строку, где колонка `doc_key` = `DOG-2026-014`. Прочитай текущие значения колонок `status` и `comment`. Если `status` ≠ «Оплачен», предложи обновление на «На согласовании» и допиши в `comment` сегодняшнюю дату. После write перечитай ту же строку и покажи diff.

---

## FAQ-кандидаты (из карточки)

- **Можно ли без программиста?** — Path A (Marketplace+OAuth): да для пилота; Path B (SA+mcp.json): по инструкции B82/B92, Cursor поможет с JSON; production — 1–2 ч первый реестр.
- **Сколько займёт внедрение?** — SA + mcp.json + один тестовый update: **~1–2 ч**; OAuth-плагин быстрее, если доступен в витрине.
- **Какие риски для данных?** — OAuth = права вашего Google; SA-ключ = все расшаренные файлы; не класть ПДн; подтверждать write-tools; indirect injection из писем/ячеек (Google docs).
- **OAuth или service account?** — OAuth для личного пилота; SA для командного реестра, cron, минимального blast radius.
- **Чем отличается от B82?** — B82 = Python/Node скрипт пишет в staging; B92 = Agent в Cursor правит через MCP без скрипта.
- **Работает ли в Cloud Agents?** — локальный OAuth не переезжает автоматически; настраивать MCP в Cloud Agents dashboard или SA.
- **Что такое sheetsmcp.googleapis.com?** — официальный remote MCP Google; endpoint `/mcp/v1`; для Cursor — advanced Path C, не обязателен для первого реестра.

---

## CTA / interlink

- Internal: `/avtomatizaciya-finansov-no-code/`, `/obezlichivanie-dannyh-chatgpt-finansist/`, `/google-sheets-api-integraciya-finotdel/` (B82), `/mcp-cursor-finansist-instrumenty/` (B21)
- Соседние реестры: B51, B58, B83
- CTA: `https://club.koda-fd.ru/?utm_source=blog&utm_medium=article&utm_campaign=mcp-google-sheets-cursor-reestry` (≤2), `https://t.me/finance_modern?utm_source=blog&utm_medium=article` (≤2)

---

## Источники исследования

- WebSearch Cursor 2026-09-06 по `mcp google sheets cursor 2026`, Workspace plugins, mcp-gsheets, sheetsmcp.googleapis.com
- WebFetch: https://developers.google.com/workspace/sheets/api/guides/configure-mcp-server
- WebFetch: https://cursor.com/help/customization/mcp
- `research-context.json` / `research-serp.json` шаг 0 (06.09.2026)
- `memory/brief/fact-bank.md` — прямых MCP+Sheets фактов нет
- Utility gate topic: PASS

---

=== EXCALIBUR BLOG RESEARCH ===
topic_id: B92
article_dir: memory/blog/articles/B92-mcp-google-sheets-cursor-reestry
status: ✅ PASS
utility_verdict: PASS
reader_outcome: Подключить MCP Google Sheets в Cursor и править строку реестра по doc_key без копипаста, с verify-перечиткой.
summary: Utility PASS. Wordstat MCP user-mcp-kv недоступен (WARNING, цифры не выдуманы). SERP 06.09.2026: Cursor MCP docs + freema/mcp-gsheets + официальный Google sheetsmcp.googleapis.com. 25 фактов с URL, 9 шагов action_outline, finance-first угол. Готов к writer.
===
