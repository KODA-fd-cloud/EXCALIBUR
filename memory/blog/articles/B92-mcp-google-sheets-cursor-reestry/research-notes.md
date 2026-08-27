# Research notes — B92

**topic_id:** B92  
**slug:** mcp-google-sheets-cursor-reestry  
**h1:** Как подключить MCP к Google Sheets в Cursor и править реестры без копипаста  
**research_date:** 2026-08-27  
**publish_target:** koda-fd.ru/blog  
**utility_gate:** PASS (`how_to`, mode B)  
**author_id:** olga-kondratskaya  
**related_internal:** `/avtomatizaciya-finansov-no-code/`, `/obezlichivanie-dannyh-chatgpt-finansist/`  
**sibling_queue:** B82 (Sheets API + SA), B21 (MCP в Cursor общий), B51/B58/B83 (реестры в Sheets)  
**cover_scene_hint:** abstract holographic finance automation dark #0a0a0f purple #8b5cf6, no text

---

## utility_verdict

**PASS** — тема utility-only how_to. Читатель получает два рабочих маршрута подключения Google Sheets к Cursor через MCP (официальный плагин из Marketplace **или** community-сервер `mcp-gsheets` на service account), подготовку реестра под агентные правки, тестовый сценарий «найти строку → обновить статус → перечитать», чеклист безопасности для финданных и troubleshooting (включая известный OAuth-баг `cursor://` августа 2026). Не новость «Cursor открыл Workspace», не обзор 25 MCP-серверов, не туториал «напиши свой MCP с нуля».

---

## reader_outcome

После гайда финансист сможет подключить MCP Google Sheets в Cursor, дать агенту доступ только к рабочему реестру (через service account или OAuth-плагин), попросить обновить статус строки или дописать поля без копирования таблицы в чат и проверить результат перечиткой диапазона через MCP-tool.

---

## action_outline

1. **Решить, нужен ли MCP Sheets** — реестр уже в Google Sheets (договоры, УПД, SaaS, заявки на расход), правки повторяются, устали таскать диапазоны в чат; **не** делать, если нужен жёсткий audit trail / сотни таблиц с enterprise ACL — тогда 1С/CLM, Sheets только staging.
2. **Выбрать путь подключения** — **Path A (быстрый пилот):** плагин `google-sheets` из Cursor Marketplace / Customize → OAuth (Local); **Path B (финконтур):** `freema/mcp-gsheets` + service account — расшарить только нужные реестры, ключ в `env`, без доступа агента ко всему Drive (см. B82, B93).
3. **Подготовить реестр** — одна строка = одна сущность; стабильный `doc_key`; лист `staging` для импорта; в облако без сырых ПДн (ИНН/сумма/статус — да; паспорт, полные ФИО — нет); interlink `/obezlichivanie-dannyh-chatgpt-finansist/`.
4. **Path B: Google Cloud + SA** — проект → включить **Google Sheets API** → service account → JSON-ключ → скопировать `client_email` → «Поделиться» на файл реестра с ролью **Редактор** (без «Уведомить»).
5. **Path B: mcp.json в Cursor** — глобально `~/.cursor/mcp.json` или проектно `.cursor/mcp.json`; блок `mcp-gsheets` с `npx -y mcp-gsheets@latest` и `GOOGLE_APPLICATION_CREDENTIALS` (абсолютный путь); JSON-ключ **не** в git.
6. **Path A: Marketplace + OAuth** — Customize → MCPs → `google-sheets` → Add → аутентификация; если Cloud даёт Error 400 `invalid_request` на `cursor://` — переключить Local **или** Login через https://cursor.com/agents; минимальные scopes.
7. **Проверить подключение** — перезапуск Cursor; Customize → MCPs → зелёный статус; Output → **MCP Logs**; tool `sheets_check_access` (Path B) или живой запрос «прочитай A1:C5 листа Реестр».
8. **Рабочий сценарий реестра** — промпт с DoD: `sheets_get_metadata` → найти строку по `doc_key` → `sheets_update_values` / `sheets_append_values` только в колонки статуса/комментария → `sheets_get_values` на ту же строку → сверка; human approval на каждый write-tool.
9. **Эксплуатация и рост** — allowlist write-tools; ротация ключа SA (B93); при >80–100 заявок/мес или audit — n8n/ERP, Sheets остаётся staging; соседние реестры B51/B58/B83.

**Workflow для статьи:**  
`Реестр в Sheets → (SA share | OAuth plugin) → MCP в Cursor → Agent read/update по doc_key → перечитка диапазона → регламент CFO`

---

## Яндекс Wordstat (MCP user-mcp-kv)

⚠️ **WORDSTAT UNAVAILABLE / AUTH WARNING:** сервер MCP `user-mcp-kv` в этой Cloud-сессии **не подключён** (в каталоге dynamic tools: `cursor`, `Cursor Automation Tools`, `cursor-cloud`, `cursor-subscriptions`). Вызов `wordstat_get_top_requests` **не выполнен**. Точные показы/мес **не получены** и **не выдуманы**.

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
| Security | service account json не в git, обезличивание sheets, oauth scopes минимум, cursor oauth invalid_request | FAQ / troubleshooting |
| Ops | sheets_check_access, mcp logs cursor, unauthorized google mcp | troubleshooting |
| Adjacent | cursor google workspace plugins 2026, mcp cursor finansist | interlink B21 |

**SEO-вывод:** SERP по `mcp google sheets cursor` на 27.08.2026 — **EN how-to** (freema, we2go, Composio, Merge, LLMversus) + **официальные docs Cursor MCP** + **форумные треды про OAuth Google Workspace plugins**. RU how-to «финансист + реестр + Cursor» почти нет. Угол КОДА: **правка управленческих реестров через MCP без копипаста**, SA для финконтура, честный note про статус Marketplace Sheets / OAuth-баг.

---

## SERP (WebSearch Cursor, 27.08.2026)

Приоритет — живой WebSearch; `research-serp.json` (шаг 0) — черновик URL; query `2026 2026` и часть сниппетов **нерелевантны** — не копировать.

### Primary: `mcp google sheets cursor 2026`

| # | URL | Тип | Пробел для КОДА |
| --- | --- | --- | --- |
| 1 | https://cursor.com/docs/mcp | Официальный reference | Нет реестров финотдела |
| 2 | https://cursor.com/help/customization/mcp | Help: mcp.json, OAuth, approvals, Cloud Agents | Канон шагов; нет Sheets-кейса |
| 3 | https://github.com/freema/mcp-gsheets | Community MCP (SA), Node 20+ | EN; dev-фокус, не CFO |
| 4 | https://github.com/we2go/google-mcp | npx wizard OAuth/SA | Sheets+Docs; не реестры |
| 5 | https://llmversus.com/mcp/google-sheets-mcp | Install guide 2026 (mcp-google-sheets) | Generic Claude/Cursor |
| 6 | https://composio.dev/toolkits/googlesheets/framework/cursor | Composio OAuth (обновл. 26.08.2026) | SaaS-посредник |
| 7 | https://www.merge.dev/blog/google-sheets-mcp-cursor | Merge Agent Handler, 4 steps | Dev/API inspection |
| 8 | https://mcp.directory/servers/google-sheets | Directory: uvx mcp-google-sheets | Каталог, не finance |

### News / OAuth / Marketplace (август 2026)

| # | URL | Тип | Пробел |
| --- | --- | --- | --- |
| 1 | https://cursor.com/changelog/google-workspace-plugins | Changelog 03.08.2026 | Drive/Gmail/Calendar детально; Sheets в теле **не расписан** |
| 2 | https://forum.cursor.com/t/google-sheet-authentication-is-broken-atm-critical/167413 | Bug: Sheets OAuth Error 400 | Workaround Local / cursor.com/agents |
| 3 | https://forum.cursor.com/t/google-workspace-plugins-oauth-fails-error-400-invalid-request-on-cursor-redirect/167402 | Bug: `cursor://` redirect | Cloud Auth broken; Local OK |
| 4 | https://forum.cursor.com/t/google-plugins-broken-auth-2-0/167780 | Help: Google plugins Auth | Подтверждение known issue |
| 5 | https://explainx.ai/blog/cursor-google-workspace-plugins-gmail-drive-calendar-august-2026 | EN анализ | Gap официальной доки по Sheets |
| 6 | https://vibecoding.ru/news/2026/08/03/cursor-google-workspace-plugins | RU новость | Docs/Sheets временно убирали из витрины |

### Secondary: `автоматизация финотдела` / реестры Sheets

| # | URL | Тип | Пробел |
| --- | --- | --- | --- |
| 1 | https://dzen.ru/a/anRW32ni3D3wHjQF | Реестр договоров Sheets | Без MCP |
| 2 | https://dzen.ru/a/aoAqyl_t_ztBh3s7 | Реестр УПД Sheets | Без MCP |
| 3 | https://dzen.ru/a/aoAx4V_t_ztBh5aj | Forms→Sheets заявки | Без MCP |
| 4 | https://koda-fd.ru/blog/ai-dlya-finansista-2026/ | Hub КОДА | Нет MCP Cursor |
| 5 | https://ascn.ai/ru/blog-no-code/how-to-automate-contract-management | No-code договоры | Не Cursor |

### Конкурентный зазор (угол КОДА)

1. **Finance-first** — не «подключи Sheets к Cursor», а «перестань копировать реестр в чат: agent правит строку по `doc_key`».
2. **Два пути с выбором** — OAuth-плагин для пилота (с honest note про OAuth 400) vs SA+mcp-gsheets для production финконтура.
3. **Связка с реестрами серии** — договоры (B51), УПД (B58), SaaS (B83); MCP = слой правок поверх уже спроектированной таблицы.
4. **Security block** — минимальный share, ключ вне git, approval tools, indirect prompt injection, обезличивание.
5. **Verify loop** — после write всегда `get_values`; «Connected ≠ authorized».
6. **Fork от B82** — B82 = свой Python-скрипт; B92 = те же SA+share, но правки через Agent+MCP без написания кода.

---

## Таблица фактов

| # | Утверждение | Источник | Дата проверки |
| --- | --- | --- | --- |
| 1 | MCP подключает Cursor к внешним инструментам; Agent вызывает tools в чате. | https://cursor.com/help/customization/mcp | 2026-08-27 |
| 2 | Конфиг: проектный `.cursor/mcp.json` + глобальный `~/.cursor/mcp.json`; при совпадении имени побеждает **проектный**. | https://cursor.com/help/customization/mcp | 2026-08-27 |
| 3 | Локальный MCP: `command`/`args`/`env`; удалённый — поле `url` (+ опционально `headers`). | https://cursor.com/docs/mcp | 2026-08-27 |
| 4 | One-click: Customize → MCPs → Add to Cursor; после ручного `mcp.json` — **перезапуск Cursor**. | https://cursor.com/help/customization/mcp | 2026-08-27 |
| 5 | По умолчанию Agent **запрашивает approval** перед MCP-tool; с Cursor 3.6+ — Auto-review / allowlist / `permissions.json`. | https://cursor.com/help/customization/mcp | 2026-08-27 |
| 6 | Troubleshooting: Output → **MCP Logs** (`Ctrl+Shift+U` / `Cmd+Shift+U`). | https://cursor.com/docs/mcp | 2026-08-27 |
| 7 | Cloud Agents поддерживают MCP, настроенные в Cloud Agents dashboard / Team Integrations & MCP — **не** наследуют автоматически локальный интерактивный OAuth desktop. | https://cursor.com/help/customization/mcp | 2026-08-27 |
| 8 | OAuth redirect URLs Cursor для MCP: `https://www.cursor.com/agents/mcp/oauth/callback` и `http://localhost:8787/callback`. | https://cursor.com/docs/mcp | 2026-08-27 |
| 9 | 03.08.2026 Cursor анонсировал Google Workspace plugins; в changelog детально Drive/Gmail/Calendar; Sheets/Docs в документе **не детализированы**. | https://cursor.com/changelog/google-workspace-plugins | 2026-08-27 |
| 10 | На форуме Cursor (авг. 2026): Google Sheets / Workspace plugins OAuth с desktop Cloud даёт **Error 400: invalid_request** — Google отклоняет `cursor://anysphere.cursor-mcp/oauth/callback`. | https://forum.cursor.com/t/google-sheet-authentication-is-broken-atm-critical/167413 | 2026-08-27 |
| 11 | Workaround от Cursor staff: **Local** auth работает; для Cloud — Login через https://cursor.com/agents → MCP Servers (HTTPS callback). | https://forum.cursor.com/t/google-workspace-plugins-oauth-fails-error-400-invalid-request-on-cursor-redirect/167402 | 2026-08-27 |
| 12 | `freema/mcp-gsheets`: Node.js **v20+**, Google Cloud + Sheets API + service account JSON; `npx -y mcp-gsheets@latest` + `GOOGLE_APPLICATION_CREDENTIALS` + `GOOGLE_PROJECT_ID`. | https://github.com/freema/mcp-gsheets | 2026-08-27 |
| 13 | Ключевые tools для реестра: `sheets_get_values`, `sheets_update_values`, `sheets_append_values`, `sheets_batch_get_values`, `sheets_get_metadata`, `sheets_check_access`. | https://github.com/freema/mcp-gsheets/blob/main/README.md | 2026-08-27 |
| 14 | `sheets_append_values`: default `insertDataOption` = **OVERWRITE** — для реестра явно указывать `INSERT_ROWS`, если нужно сдвигать строки. | https://github.com/freema/mcp-gsheets/blob/main/README.md | 2026-08-27 |
| 15 | Перед write рекомендуется `sheets_check_access` для проверки прав SA на spreadsheetId. | https://github.com/freema/mcp-gsheets/blob/main/README.md | 2026-08-27 |
| 16 | Service account видит **только** таблицы, расшаренные на `client_email` из JSON; IAM-роли Cloud **не заменяют** Share файла. | https://developers.google.com/workspace/guides/create-credentials#service-account | 2026-08-27 |
| 17 | Scope `https://www.googleapis.com/auth/spreadsheets` — read/write всех расшаренных таблиц SA; применяется ко **всему файлу**. | https://developers.google.com/workspace/sheets/api/scopes | 2026-08-27 |
| 18 | Квота Sheets API write: **300 запросов/мин** на проект; превышение → HTTP **429**; batch = один запрос. | https://developers.google.com/workspace/sheets/api/limits | 2026-08-27 |
| 19 | `we2go/google-mcp`: `npx google-mcp init` — wizard SA или OAuth; tools `sheets_read_range`, `sheets_update_range`, `sheets_append_row`. | https://github.com/we2go/google-mcp | 2026-08-27 |
| 20 | Альтернативы: Composio (hosted OAuth, mcp.json + Connect), Merge Agent Handler (CLI + `.cursorrules`), `mcp-google-sheets` / uvx. | https://composio.dev/toolkits/googlesheets/framework/cursor ; https://www.merge.dev/blog/google-sheets-mcp-cursor | 2026-08-27 |
| 21 | Реестр договоров в Sheets уместен до **200–300** активных договоров при одном владельце; иначе CLM/1С. | https://dzen.ru/a/anRW32ni3D3wHjQF | 2026-08-27 |
| 22 | Заявки на расход Forms→Sheets: при **>80–100** заявок/мес Sheets — staging перед ERP/n8n. | https://dzen.ru/a/aoAx4V_t_ztBh5aj | 2026-08-27 |
| 23 | С 01.01.2026 ЭДО: формат УПД 5.03; с 01.04.2026 новая печатная форма (строка 5б, НДС 22%) — учитывать в колонках реестра УПД. | https://dzen.ru/a/aoAqyl_t_ztBh3s7 | 2026-08-27 |

**Не выдумывать:** показы Wordstat; «Sheets-плагин всегда в Marketplace»; что SA = доступ ко всему Drive; цифры «installs» с каталогов; обещание «без программиста» для Path B без GCP/SA; что Cloud OAuth «просто работает» без workaround.

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

- **Можно ли без программиста?** — Path A (Marketplace+OAuth): да для пилота, если Local auth проходит; Path B (SA+mcp.json): по инструкции, Cursor поможет с JSON; production — 1–2 ч первый реестр.
- **Сколько займёт внедрение?** — SA + mcp.json + один тестовый update: **~1–2 ч**; OAuth-плагин быстрее, если auth не упирается в Error 400.
- **Какие риски для данных?** — OAuth = права вашего Google; SA-ключ = все расшаренные файлы; не класть ПДн; подтверждать write-tools; indirect injection из ячеек/писем.
- **OAuth или service account?** — OAuth для личного пилота; SA для командного реестра, cron, минимального blast radius; при Cloud OAuth-баге Path B надёжнее.
- **Чем отличается от B82?** — B82 = Python/Node скрипт пишет в staging; B92 = Agent в Cursor правит через MCP без скрипта.
- **Работает ли в Cloud Agents?** — локальный desktop OAuth не переезжает автоматически; для облака — dashboard MCP / SA / Login через cursor.com/agents.

---

## CTA / interlink

- Internal: `/avtomatizaciya-finansov-no-code/`, `/obezlichivanie-dannyh-chatgpt-finansist/`, `/google-sheets-api-integraciya-finotdel/` (B82), `/mcp-cursor-finansist-instrumenty/` (B21)
- Соседние реестры: B51, B58, B83
- CTA: `https://club.koda-fd.ru/?utm_source=blog&utm_medium=article&utm_campaign=mcp-google-sheets-cursor-reestry` (≤2), `https://t.me/finance_modern?utm_source=blog&utm_medium=article` (≤2)

---

## Handoff marker

`=== EXCALIBUR BLOG RESEARCH ===` — см. `.cursor/excalibur-blog-handoff.md`
