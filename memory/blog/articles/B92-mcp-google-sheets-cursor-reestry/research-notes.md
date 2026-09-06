# Research notes — B92

**topic_id:** B92  
**slug:** mcp-google-sheets-cursor-reestry  
**h1:** Как подключить MCP к Google Sheets в Cursor и править реестры без копипаста  
**research_date:** 2026-09-06  
**publish_target:** koda-fd.ru/blog  
**utility_gate:** PASS (`how_to`, mode B) — `python3 scripts/excalibur_blog_utility_gate.py --topic-id B92`  
**author_id:** olga-kondratskaya  
**related_internal:** `/avtomatizaciya-finansov-no-code/`, `/obezlichivanie-dannyh-chatgpt-finansist/`  
**sibling_queue:** B82 (Sheets API + SA), B21 (MCP в Cursor общий), B51/B58/B83 (реестры в Sheets)  
**cover_scene_hint:** abstract holographic finance automation dark #0a0a0f purple #8b5cf6, no text

---

## utility_verdict

**PASS** — тема utility-only how_to. Читатель получает два рабочих маршрута подключения Google Sheets к Cursor через MCP (официальный плагин Marketplace/OAuth **или** community-сервер `mcp-gsheets` на service account), подготовку реестра под агентные правки, тестовый сценарий «найти строку → обновить статус → перечитать», чеклист безопасности для финданных и troubleshooting (OAuth `cursor://`, 403 share, 429 quota, сериализация `values`). Не новость «Cursor открыл Workspace», не обзор 25 MCP-серверов, не туториал «напиши свой MCP с нуля».

---

## reader_outcome

После гайда финансист сможет подключить MCP Google Sheets в Cursor, дать агенту доступ только к рабочему реестру (через service account или OAuth-плагин), попросить обновить статус строки или дописать поля без копирования таблицы в чат и проверить результат перечиткой диапазона через MCP-tool.

---

## action_outline

1. **Решить, нужен ли MCP Sheets** — реестр уже в Google Sheets (договоры, УПД, SaaS, заявки на расход), правки повторяются, устали таскать диапазоны в чат; **не** делать, если нужен жёсткий audit trail / сотни таблиц с enterprise ACL — тогда 1С/CLM, Sheets только staging.
2. **Выбрать путь подключения** — **Path A (быстрый пилот):** плагин `google-sheets` из Cursor Marketplace / Customize → OAuth личного Google; **Path B (финконтур):** `freema/mcp-gsheets` + service account — расшарить только нужные реестры, ключ в `env`, без доступа агента ко всему Drive (см. B82, B93). На сентябрь 2026 Path B — основной для production: Sheets в витрине нестабилен/уходил, OAuth IDE часто ломается.
3. **Подготовить реестр** — одна строка = одна сущность; стабильный `doc_key`; лист `staging` для импорта; в облако без сырых ПДн (ИНН/сумма/статус — да; паспорт, полные ФИО — нет); interlink `/obezlichivanie-dannyh-chatgpt-finansist/`.
4. **Path B: Google Cloud + SA** — проект → включить **Google Sheets API** → service account → JSON-ключ → скопировать `client_email` → «Поделиться» на файл реестра с ролью **Редактор** (без «Уведомить»).
5. **Path B: mcp.json в Cursor** — глобально `~/.cursor/mcp.json` или проектно `.cursor/mcp.json`; блок `mcp-gsheets` с `npx -y mcp-gsheets@latest` и `GOOGLE_APPLICATION_CREDENTIALS` (абсолютный путь); JSON-ключ **не** в git.
6. **Path A: Marketplace** — Customize → MCPs → `google-sheets` → Add → OAuth; минимальные scopes; если Error 400 / `cursor://` — логин через https://cursor.com/agents (MCP Servers → Login) или Local-auth; не обещать «всегда в витрине».
7. **Проверить подключение** — перезапуск Cursor; Customize → MCPs → зелёный статус; Output → **MCP Logs**; tool `sheets_check_access` (Path B) или живой запрос «прочитай A1:C5 листа Реестр».
8. **Рабочий сценарий реестра** — промпт с DoD: `sheets_get_metadata` → найти строку по `doc_key` → `sheets_update_values` / `sheets_append_values` только в колонки статуса/комментария → `sheets_get_values` на ту же строку → сверка; human approval на каждый write-tool; для Path A: «pass values as JSON array of arrays».
9. **Эксплуатация и рост** — allowlist write-tools; ротация ключа SA (B93); при >80–100 заявок/мес или audit — n8n/ERP, Sheets остаётся staging; соседние реестры B51/B58/B83.

**Workflow для статьи:**  
`Реестр в Sheets → (SA share | OAuth plugin) → MCP в Cursor → Agent read/update по doc_key → перечитка диапазона → регламент CFO`

---

## Яндекс Wordstat (MCP user-mcp-kv)

⚠️ **WORDSTAT AUTH WARNING:** сервер MCP `user-mcp-kv` в этой Cloud-сессии **не подключён** (в каталоге dynamic tools: `Cursor Automation Tools`, `cursor`, `cursor-cloud`, `cursor-subscriptions` — namespace `user-mcp-kv` отсутствует). Вызов `wordstat_get_top_requests` **не выполнен**. Точные показы/мес **не получены** и **не выдуманы**.

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

**SEO-вывод:** SERP по `mcp google sheets cursor` (WebSearch 06.09.2026) — **EN community MCP** (freema, we2go, spreadsheet-mcp, iota-uz) + **новости Cursor Workspace (авг 2026)** + RU-каталоги (mcp-catalog, freemcplab). Почти нет RU how-to «финансист + реестр + Cursor + SA». Угол КОДА: **правка управленческих реестров через MCP без копипаста**, с веткой SA для безопасности и явным сравнением с B82 (скрипт) и B21 (общий MCP).

---

## SERP (WebSearch Cursor, 06.09.2026)

Приоритет — живой WebSearch; `research-serp.json` (шаг 0, 2026-09-06) полезен как URL-черновик; query `2026 2026` и часть сниппетов **нерелевантны** — не копировать.

### Primary: `mcp google sheets cursor 2026`

| # | URL | Тип | Пробел для КОДА |
| --- | --- | --- | --- |
| 1 | https://cursor.com/help/customization/mcp | Help: mcp.json, OAuth, approvals, MCP Logs | Канон шагов; нет Sheets/реестров |
| 2 | https://github.com/freema/mcp-gsheets | Community MCP (SA), Node 20+, npx | EN; dev-фокус, не CFO |
| 3 | https://github.com/we2go/google-mcp | npx wizard OAuth/SA, 3 min setup | Sheets как DB; не реестры |
| 4 | https://github.com/dudegladiator/spreadsheet-mcp | Python/uv, 27 tools | Установка для dev |
| 5 | https://github.com/iota-uz/sheets-mcp | Typed Sheet API → batchUpdate | Сложно для финотдела |
| 6 | https://mcpcursor.com/server/google-sheets-mcp | Каталог MCP | Аффилиат/листинг |
| 7 | https://pastesheet.com/guides/google-sheets-mcp-cursor | Hosted + security angle | SaaS-посредник |
| 8 | https://composio.dev/toolkits/googlesheets | Composio OAuth | Посредник, не SA |

### News / official Workspace (август 2026 → статус на 06.09)

| # | URL | Тип | Пробел |
| --- | --- | --- | --- |
| 1 | https://cursor.com/changelog/google-workspace-plugins | Changelog: Drive/Gmail/Calendar | Sheets/Docs в теле changelog **не расписаны** |
| 2 | https://pondero.ai/news/2026-08-04-cursor-google-workspace/ | EN разбор 03–04.08: Sheets = read/find/update/create | Новость, не how-to реестра |
| 3 | https://vibecoding.ru/news/2026/08/03/cursor-google-workspace-plugins | RU: Docs/Sheets убраны из витрины 04.08; OAuth bug | Не SA path |
| 4 | https://mayai.ru/cursor-otkryl-gmail-i-sheets-agentam/ | RU разбор релиза | Мало SA/реестров |
| 5 | https://forum.cursor.com/t/google-workspace-plugins-oauth-fails-error-400-invalid-request-on-cursor-redirect/167402 | OAuth Error 400 `cursor://` | Troubleshooting Path A |
| 6 | https://forum.cursor.com/t/bug-google-sheets-mcp-update-values-fails-with-serialization-error-nested-arrays-converted-to-strings/169687 | Bug `update_values` (авг 2026) | Workaround для Path A |

### Secondary: `автоматизация финотдела` / реестры

| # | URL | Тип | Пробел |
| --- | --- | --- | --- |
| 1 | https://koda-fd.ru/blog/ai-dlya-finansista-2026/ | Hub КОДА | Нет MCP Cursor |
| 2 | https://dzen.ru/a/anRW32ni3D3wHjQF | Реестр договоров Sheets | Без MCP |
| 3 | https://dzen.ru/a/aoAqyl_t_ztBh3s7 | Реестр УПД Sheets | Без MCP |
| 4 | https://znaj.org/ru/6-luchshikh-reshenii-2026-goda-avtomatizacii-upravleniya-finansami/ | Обзор 2026 | ERP-уклон |

### H1-aligned RU

| # | URL | Заметка |
| --- | --- | --- |
| 1 | https://mcp-catalog.ru/tutorials/google-sheets-cursor | RU: henilcalagiya variant |
| 2 | https://mcpservers.org/ru/servers/freema/mcp-gsheets | RU зеркало freema |
| 3 | https://www.freemcplab.com/i18n/ru/play/google-sheets/ | Demo configs Cursor |
| 4 | https://cursor.com/ru/help/customization/mcp | RU help MCP |

### Конкурентный зазор (угол КОДА)

1. **Finance-first** — не «подключи Sheets к Cursor», а «перестань копировать реестр в чат: agent правит строку по `doc_key`».
2. **Два пути с выбором** — OAuth-плагин для пилота vs SA+mcp-gsheets для production (honest note: витрина Sheets / OAuth IDE нестабильны с авг 2026).
3. **Связка с реестрами серии** — договоры (B51), УПД (B58), SaaS (B83); MCP = слой правок поверх уже спроектированной таблицы.
4. **Security block** — минимальный share, ключ вне git, approval tools, indirect prompt injection, обезличивание.
5. **Verify loop** — после write всегда `get_values`; «Connected ≠ authorized».
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
| 7 | 03.08.2026 Cursor анонсировал Google Workspace plugins; в официальном changelog детально: **Drive, Gmail, Calendar**; установка Marketplace / Customize. | https://cursor.com/changelog/google-workspace-plugins | 2026-09-06 |
| 8 | По разбору Pondero (04.08.2026): Sheets-плагин даёт read ranges / find values / update cells / create & edit spreadsheets (со ссылкой на changelog Cursor). | https://pondero.ai/news/2026-08-04-cursor-google-workspace/ | 2026-09-06 |
| 9 | vibecoding.ru (04.08.2026): из пяти обещанных Workspace-плагинов в витрине остались **Gmail, Drive, Calendar**; Docs/Sheets/Slides временно убраны; мин. версия Cursor **3.13.0**. | https://vibecoding.ru/news/2026/08/03/cursor-google-workspace-plugins | 2026-09-06 |
| 10 | OAuth Workspace из IDE часто падает Error 400 `invalid_request` из‑за redirect `cursor://`; обход — Login на https://cursor.com/agents (MCP Servers) или Local-auth. | https://forum.cursor.com/t/google-workspace-plugins-oauth-fails-error-400-invalid-request-on-cursor-redirect/167402 ; vibecoding.ru | 2026-09-06 |
| 11 | Официальные MCP Google Workspace — **Developer Preview** (раздача через программу разработчиков). | https://vibecoding.ru/news/2026/08/03/cursor-google-workspace-plugins | 2026-09-06 |
| 12 | `freema/mcp-gsheets`: Node.js **v20+**, Google Cloud + Sheets API + SA JSON; Cursor: `npx -y mcp-gsheets@latest` + `GOOGLE_APPLICATION_CREDENTIALS` (+ `GOOGLE_PROJECT_ID`). | https://github.com/freema/mcp-gsheets | 2026-09-06 |
| 13 | Ключевые tools для реестра: `sheets_get_values`, `sheets_update_values`, `sheets_append_values`, `sheets_batch_get_values`, `sheets_get_metadata`, `sheets_check_access`. | https://github.com/freema/mcp-gsheets | 2026-09-06 |
| 14 | `sheets_append_values`: default `insertDataOption` = **OVERWRITE** — для реестра явно `INSERT_ROWS`, если нужно сдвигать строки. | https://github.com/freema/mcp-gsheets | 2026-09-06 |
| 15 | Service account видит **только** таблицы, расшаренные на `client_email` из JSON; IAM Cloud **не заменяет** Share файла. | https://developers.google.com/workspace/guides/create-credentials#service-account | 2026-09-06 |
| 16 | Квота Sheets API: **300** read и **300** write запросов/мин на проект; **60**/мин на user; превышение → HTTP **429**; batch = 1 запрос. | https://developers.google.com/workspace/sheets/api/limits | 2026-09-06 |
| 17 | Стандартное использование Sheets API — **без доп. платы**; превышение квот планируют тарифицировать **позже в 2026**. | https://developers.google.com/workspace/sheets/api/limits | 2026-09-06 |
| 18 | Forum (28.08.2026): у Google Sheets MCP tool `update_values` 2D-массив `values` иногда сериализуется в строки → 400; workaround: retry + правило «array of arrays, never strings». | https://forum.cursor.com/t/bug-google-sheets-mcp-update-values-fails-with-serialization-error-nested-arrays-converted-to-strings/169687 | 2026-09-06 |
| 19 | `we2go/google-mcp`: `npx google-sheet-mcp` / wizard `init` (SA или OAuth); конфиг Cursor через `.cursor/mcp.json`. | https://github.com/we2go/google-mcp | 2026-09-06 |
| 20 | `dudegladiator/spreadsheet-mcp`: **27 tools**, auth через service-account JSON; Cursor config через `uv run`. | https://github.com/dudegladiator/spreadsheet-mcp | 2026-09-06 |
| 21 | Риск MCP+Google: агент наследует права пользователя; возможна **indirect prompt injection** — human-in-the-loop на write. | https://mayai.ru/cursor-otkryl-gmail-i-sheets-agentam/ | 2026-09-06 |
| 22 | «Connected» в Tools & MCP **не гарантирует** успешный Google OAuth — проверять живым read/write. | https://mayai.ru/cursor-otkryl-gmail-i-sheets-agentam/ | 2026-09-06 |
| 23 | Cloud Agents **не наследуют** интерактивный Google OAuth с локального Cursor — для облака отдельный Login / SA. | https://mayai.ru/cursor-otkryl-gmail-i-sheets-agentam/ ; forum.cursor.com | 2026-09-06 |
| 24 | Реестр договоров в Sheets уместен до **200–300** активных договоров при одном владельце; иначе CLM/1С. | https://dzen.ru/a/anRW32ni3D3wHjQF | 2026-09-06 |
| 25 | Заявки на расход Forms→Sheets: при **>80–100** заявок/мес Sheets — staging перед ERP/n8n. | https://dzen.ru/a/aoAx4V_t_ztBh5aj | 2026-09-06 |
| 26 | В 2026 финотдел автоматизирует в первую очередь классификацию платежей, сверки, управленческую отчётность — Sheets+MCP = **transport правок**, не GL. | https://koda-fd.ru/blog/ai-dlya-finansista-2026/ | 2026-09-06 |

**Не выдумывать:** показы Wordstat; «Sheets-плагин всегда в Marketplace»; что SA = доступ ко всему Drive; цифры installs со сторонних обзоров; «без программиста» для Path B без упоминания GCP/SA.

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

> Подключись к таблице `{SPREADSHEET_ID}`. На листе `Реестр` найди строку, где колонка `doc_key` = `DOG-2026-014`. Прочитай текущие значения колонок `status` и `comment`. Если `status` ≠ «Оплачен», предложи обновление на «На согласовании» и допиши в `comment` сегодняшнюю дату. После write перечитай ту же строку и покажи diff. Передавай `values` как JSON array of arrays (не строки).

---

## FAQ-кандидаты (из карточки)

- **Можно ли без программиста?** — Path A (Marketplace+OAuth): да для пилота, если плагин доступен и OAuth проходит; Path B (SA+mcp.json): по инструкции B82/B92, Cursor поможет с JSON; production — 1–2 ч первый реестр.
- **Сколько займёт внедрение?** — SA + mcp.json + один тестовый update: **~1–2 ч**; OAuth-плагин быстрее, если доступен в витрине.
- **Какие риски для данных?** — OAuth = права вашего Google; SA-ключ = все расшаренные файлы; не класть ПДн; подтверждать write-tools; indirect injection из писем/ячеек.
- **OAuth или service account?** — OAuth для личного пилота; SA для командного реестра, cron, минимального blast radius (рекомендация КОДА на сентябрь 2026).
- **Чем отличается от B82?** — B82 = Python/Node скрипт пишет в staging; B92 = Agent в Cursor правит через MCP без скрипта.
- **Работает ли в Cloud Agents?** — локальный OAuth не переезжает автоматически; Login на cursor.com/agents или SA.

---

## CTA / interlink

- Internal: `/avtomatizaciya-finansov-no-code/`, `/obezlichivanie-dannyh-chatgpt-finansist/`, `/google-sheets-api-integraciya-finotdel/` (B82), `/mcp-cursor-finansist-instrumenty/` (B21)
- Соседние реестры: B51, B58, B83
- CTA: `https://club.koda-fd.ru/?utm_source=blog&utm_medium=article&utm_campaign=mcp-google-sheets-cursor-reestry` (≤2), `https://t.me/finance_modern?utm_source=blog&utm_medium=article` (≤2)

---

## Handoff marker

`=== EXCALIBUR BLOG RESEARCH ===` — см. `.cursor/excalibur-blog-handoff.md`
