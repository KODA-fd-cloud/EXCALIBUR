# Research notes — B92

**topic_id:** B92  
**slug:** mcp-google-sheets-cursor-reestry  
**h1:** Как подключить MCP к Google Sheets в Cursor и править реестры без копипаста  
**research_date:** 2026-09-15  
**publish_target:** koda-fd.ru/blog  
**utility_gate:** PASS (`how_to`, mode B) — подтверждено `excalibur_blog_utility_gate.py --topic-id B92`  
**author_id:** olga-kondratskaya  
**related_internal:** `/avtomatizaciya-finansov-no-code/`, `/obezlichivanie-dannyh-chatgpt-finansist/`  
**sibling_queue:** B82 (Sheets API + SA), B21 (MCP в Cursor общий), B51/B58/B83 (реестры в Sheets), B93 (ротация SA)  
**cover_scene_hint:** abstract holographic finance automation dark #0a0a0f purple #8b5cf6, no text

---

## utility_verdict

**PASS** — utility-only how_to. Читатель получает рабочий маршрут: выбрать путь подключения Google Sheets к Cursor через MCP → подготовить реестр → настроить SA или OAuth → проверить tools → прогнать сценарий «найти строку по `doc_key` → обновить статус → перечитать» → зафиксировать регламент безопасности. Не новость про Workspace-плагины, не каталог MCP-серверов, не «напиши свой MCP с нуля».

---

## reader_outcome

После гайда финансист сможет подключить MCP Google Sheets в Cursor (рекомендуемый путь: `freema/mcp-gsheets` + service account на один реестр), попросить агента обновить статус/комментарий строки без копипаста таблицы в чат и подтвердить результат перечиткой того же диапазона.

---

## action_outline

1. **Решить, нужен ли MCP Sheets** — реестр уже в Google Sheets (договоры, УПД, SaaS, заявки), правки повторяются, копипаст диапазонов в чат мешает; **не** делать, если нужен жёсткий audit trail / сотни таблиц с enterprise ACL — тогда 1С/CLM, Sheets только staging (см. B82).
2. **Выбрать путь подключения** — **Path B (финконтур, основной):** `freema/mcp-gsheets` + service account, шаринг только нужных файлов; **Path A (пилот):** Marketplace / Customize OAuth, если Sheets-плагин реально есть в витрине (официальный changelog 03.08.2026 детально описывает только Drive/Gmail/Calendar); **Path C (опционально):** официальный remote MCP Google `https://sheetsmcp.googleapis.com/mcp/v1` (Developer Preview, OAuth, GCP) — для энтузиастов, не для первого реестра.
3. **Подготовить реестр** — одна строка = одна сущность; стабильный `doc_key`; лист `staging` для импорта; в облако без сырых ПДн (ИНН/сумма/статус — да; паспорт, полные ФИО — нет); interlink `/obezlichivanie-dannyh-chatgpt-finansist/`.
4. **Path B: Google Cloud + SA** — проект → Enable **Google Sheets API** → service account → JSON-ключ → скопировать `client_email` → «Поделиться» на файл реестра с ролью **Редактор**, без «Уведомить» (IAM Cloud ≠ доступ к Sheets).
5. **Path B: mcp.json в Cursor** — `.cursor/mcp.json` (проект) или `~/.cursor/mcp.json` (глобально); блок `mcp-gsheets` с `npx -y mcp-gsheets@latest`, `GOOGLE_PROJECT_ID`, `GOOGLE_APPLICATION_CREDENTIALS` (абсолютный путь); JSON-ключ **не** в git; Node.js **20+**.
6. **Проверить подключение** — перезапуск Cursor; Customize → MCPs → зелёный статус; Output → **MCP Logs**; tool `sheets_check_access` → живой read `A1:C5` листа `Реестр`.
7. **Рабочий сценарий реестра** — промпт с DoD: `sheets_get_metadata` / find по `doc_key` → `sheets_update_values` / `sheets_append_values` только в колонки статуса/комментария (для append явно `INSERT_ROWS`, иначе default **OVERWRITE**) → `sheets_get_values` на ту же строку → сверка; human approval на каждый write-tool.
8. **Безопасность и рост** — allowlist write-tools; ротация ключа SA (B93); не класть публичный PasteSheet на финреестр; при >80–100 заявок/мес или audit — n8n/ERP, Sheets остаётся staging; соседние реестры B51/B58/B83.

**Workflow для статьи:**  
`Реестр в Sheets → SA share (или OAuth plugin) → MCP в Cursor → Agent find/update по doc_key → перечитка диапазона → регламент CFO`

---

## Яндекс Wordstat (MCP user-mcp-kv)

⚠️ **WORDSTAT AUTH WARNING:** сервер MCP `user-mcp-kv` в этой Cloud-сессии **не подключён** (`GetDynamicTools` / `CallDynamicTool`: `MCP server does not exist: user-mcp-kv. No MCP servers available`). Вызов `wordstat_get_top_requests` для `mcp google sheets cursor` и смежных **не выполнен**. Точные показы/мес **не получены** и **не выдуманы**.

Обновление токена / подключение MCP-KV: https://oauth.yandex.ru/authorize?response_type=token&client_id=c654b948515a4a07a4c89648a0831d40

### Таблица спроса (Wordstat)

| Фраза | Показы в месяц |
| --- | --- |
| mcp google sheets cursor | *не получено — MCP-KV недоступен* |
| cursor mcp | *не получено — MCP-KV недоступен* |
| mcp сервер для cursor | *не получено — MCP-KV недоступен* |
| автоматизация финотдела | *не получено — MCP-KV недоступен* |
| google sheets mcp | *не получено — MCP-KV недоступен* |
| подключить mcp cursor | *не получено — MCP-KV недоступен* |

**Экспертная семантика (LSI для writer, без цифр спроса):**

| Кластер | Фразы | Роль |
| --- | --- | --- |
| Primary | mcp google sheets cursor, google sheets mcp cursor | H1, title |
| Setup | mcp.json cursor, mcp-gsheets service account, sheetsmcp.googleapis.com | H2 пошагово |
| Finance | автоматизация финотдела google sheets, реестр договоров cursor, править реестр без копипаста | угол КОДА |
| Registry | реестр upd google sheets, реестр saas подписок, doc_key find update | кейсы |
| Security | service account json не в git, обезличивание sheets, oauth scopes минимум, indirect prompt injection | FAQ |
| Ops | sheets_check_access, mcp logs cursor, 429 too many requests | troubleshooting |
| Adjacent | cursor google workspace plugins 2026, mcp cursor finansist, sheets api service account | interlink B21/B82 |

**SEO-вывод:** SERP по `mcp google sheets cursor` — **EN/RU гайды community MCP** (freema, PasteSheet, spreadsheet-mcp, npm `mcp-google-sheets`) + **официальный Google Sheets MCP (Developer Preview, сент. 2026)** + новости Cursor Workspace (август 2026). Почти нет RU how-to «финансист + реестр + Cursor без копипаста». Угол КОДА: правка управленческих реестров через MCP, с SA как основным безопасным путём и честным сравнением с B82 (скрипт) и B21 (общий MCP).

---

## SERP (WebSearch Cursor, 15.09.2026)

Приоритет — живой WebSearch; `research-serp.json` (шаг 0, 2026-09-15) свежий как URL-черновик; query `2026 2026` **нерелевантен** — не копировать.

### Primary: `mcp google sheets cursor 2026`

| # | URL | Тип | Пробел для КОДА |
| --- | --- | --- | --- |
| 1 | https://developers.google.com/workspace/sheets/api/guides/configure-mcp-server | Official Google remote MCP (Preview) | Antigravity/Claude; нет финреестра Cursor |
| 2 | https://github.com/freema/mcp-gsheets | Community MCP (SA) | EN; dev-фокус |
| 3 | https://cursor.com/help/customization/mcp | Официальный Cursor MCP help | Канон mcp.json; нет Sheets-кейса |
| 4 | https://cursor.com/changelog/google-workspace-plugins | Changelog 03.08.2026 | Drive/Gmail/Calendar; Sheets **не** в теле |
| 5 | https://dev.to/pastesheet/google-sheets-in-vs-code-cursor-and-windsurf-over-mcp-5467 | Hosted URL MCP | Публичные листы; не SA |
| 6 | https://github.com/dudegladiator/spreadsheet-mcp | Python/uv, 27 tools | Установка для dev |
| 7 | https://www.npmjs.com/package/mcp-google-sheets | npm OAuth gateway | Не finance |
| 8 | https://mcp-catalog.ru/tutorials/gsheets-cursor | RU: freema → Cursor | Каталог; без CFO-регламента |
| 9 | https://mcp-catalog.ru/tutorials/google-sheets-cursor | RU: henilcalagiya variant | Дубль setup |

### News / official Workspace (авг–сент 2026)

| # | URL | Тип | Пробел |
| --- | --- | --- | --- |
| 1 | https://cursor.com/changelog/google-workspace-plugins | Official | Sheets в changelog **не расписан** |
| 2 | https://aicatchup.com/news/cursor-google-workspace-plugins | EN correction | Честно снимает Docs/Sheets с changelog |
| 3 | https://mayai.ru/cursor-otkryl-gmail-i-sheets-agentam/ | RU разбор | Контент-завод; мало SA/реестров |
| 4 | https://vibecoding.ru/news/2026/08/03/cursor-google-workspace-plugins | RU новость | Витрина/OAuth-баги августа |
| 5 | https://developers.google.com/workspace/sheets/api/guides/configure-mcp-server | Google Preview | Updated **2026-09-14** |

### Secondary: `автоматизация финотдела` + Sheets

| # | URL | Тип | Пробел |
| --- | --- | --- | --- |
| 1 | https://dzen.ru/a/aoV6BGni3D3wS-su | КОДА/Дзен: Sheets API + SA | Скрипт (B82), не MCP Agent |
| 2 | https://mybotn8nflow.ru/osnovy-ii-i-automation/n8n-automation-google-sheets-integration/ | n8n + Sheets | Не Cursor |
| 3 | https://sky.pro/wiki/python/rabota-s-google-sheets-api-na-python/ | Python API | Dev tutorial |
| 4 | https://koda-fd.ru/blog/ai-dlya-finansista-2026/ | Hub КОДА | Нет MCP Cursor |

### Конкурентный зазор (угол КОДА)

1. **Finance-first** — не «подключи Sheets к Cursor», а «перестань копировать реестр: agent правит строку по `doc_key`».
2. **Path B как default** — SA+mcp-gsheets для production финконтура; Marketplace Sheets — только если плагин реально в витрине (changelog подтверждает лишь Drive/Gmail/Calendar).
3. **Упомянуть Path C кратко** — официальный Google Sheets MCP Preview (сент. 2026), но не делать им основной маршрут (OAuth consent, gcloud, Antigravity/Claude-инструкции).
4. **Связка с реестрами серии** — договоры / УПД / SaaS; MCP = слой правок поверх таблицы.
5. **Security** — минимальный share, ключ вне git, approval на write, indirect prompt injection (Google docs + mayai), обезличивание.
6. **Verify loop** — после write всегда `get_values`; Connected ≠ authorized.
7. **Fork от B82** — B82 = скрипт пишет в staging; B92 = Agent+MCP без кода.

---

## Таблица фактов

| # | Утверждение | Источник | Дата проверки |
| --- | --- | --- | --- |
| 1 | MCP подключает Cursor к внешним tools; Agent вызывает их в чате. | https://cursor.com/help/customization/mcp | 2026-09-15 |
| 2 | Конфиг: проектный `.cursor/mcp.json` + глобальный `~/.cursor/mcp.json`; при совпадении имени побеждает **проектный**. | https://cursor.com/help/customization/mcp | 2026-09-15 |
| 3 | Локальный MCP: `command`/`args`/`env`; удалённый — поле `url` (+ опционально `headers`). | https://cursor.com/help/customization/mcp | 2026-09-15 |
| 4 | One-click: Customize → MCPs → Add to Cursor; после ручного `mcp.json` — **перезапуск Cursor**. | https://cursor.com/help/customization/mcp | 2026-09-15 |
| 5 | По умолчанию Agent **запрашивает approval** перед MCP-tool; с Cursor 3.6+ — Auto-review / allowlist / `permissions.json`. | https://cursor.com/help/customization/mcp | 2026-09-15 |
| 6 | Troubleshooting: Output → **MCP Logs** (`Ctrl+Shift+U` / `Cmd+Shift+U`). | https://cursor.com/help/customization/mcp | 2026-09-15 |
| 7 | Cloud Agents поддерживают MCP через Cloud Agents dashboard; на Team — shared servers под Integrations & MCP. | https://cursor.com/help/customization/mcp | 2026-09-15 |
| 8 | Changelog 03.08.2026: плагины **Drive, Gmail, Calendar**; установка из Marketplace / Customize. Sheets/Docs в этом документе **не детализированы**. | https://cursor.com/changelog/google-workspace-plugins | 2026-09-15 |
| 9 | Сторонние пересказы «5 плагинов включая Sheets» не равны официальному changelog; aicatchup снял Docs/Sheets с атрибуции changelog. | https://aicatchup.com/news/cursor-google-workspace-plugins | 2026-09-15 |
| 10 | Google Sheets remote MCP: URL `https://sheetsmcp.googleapis.com/mcp/v1`, transport Streamable HTTP, OAuth 2.0; статус **Developer Preview** (Workspace Developer Preview Program). Last updated **2026-09-14**. | https://developers.google.com/workspace/sheets/api/guides/configure-mcp-server | 2026-09-15 |
| 11 | Для official Sheets MCP нужно enable `sheets.googleapis.com` и `sheetsmcp.googleapis.com`; tools: `get_values`, `get_spreadsheet`, `update_spreadsheet`, `update_values`, `update_formulas`, `insert_dimension`. | https://developers.google.com/workspace/sheets/api/guides/configure-mcp-server | 2026-09-15 |
| 12 | Google прямо предупреждает про **indirect prompt injection** при MCP+Sheets: review actions, не кормить агента неtrusted spreadsheets. | https://developers.google.com/workspace/sheets/api/guides/configure-mcp-server | 2026-09-15 |
| 13 | `freema/mcp-gsheets`: Node.js **v20+**, Sheets API, service account JSON; `npx -y mcp-gsheets@latest` + `GOOGLE_APPLICATION_CREDENTIALS` / `GOOGLE_PROJECT_ID`. npm версия **1.10.2** (updated 2026-08-16). | https://github.com/freema/mcp-gsheets ; https://www.npmjs.com/package/mcp-gsheets | 2026-09-15 |
| 14 | Ключевые tools mcp-gsheets для реестра: `sheets_get_values`, `sheets_update_values`, `sheets_append_values`, `sheets_batch_get_values`, `sheets_get_metadata`, `sheets_check_access`. | https://github.com/freema/mcp-gsheets | 2026-09-15 |
| 15 | `sheets_append_values`: default `insertDataOption` = **OVERWRITE** — для реестра явно указывать `INSERT_ROWS`. | https://github.com/freema/mcp-gsheets | 2026-09-15 |
| 16 | Service account видит **только** таблицы, расшаренные на `client_email`; IAM Cloud **не заменяет** Share файла; Notify people — снять. | https://developers.google.com/workspace/guides/create-credentials | 2026-09-15 |
| 17 | Квоты Sheets API / Sheets MCP: read **300**/мин на проект, write **300**/мин на проект; per user/project **60**/мин; превышение → HTTP **429**; batch = 1 request. | https://developers.google.com/workspace/sheets/api/limits | 2026-09-15 |
| 18 | Hosted PasteSheet: `url` в `mcp.json`; публичные endpoints без GCP; private — платный план от **$9/mo** — **не** рекомендовать для закрытого финреестра. | https://dev.to/pastesheet/google-sheets-in-vs-code-cursor-and-windsurf-over-mcp-5467 | 2026-09-15 |
| 19 | Риск MCP+Google: агент наследует права пользователя; indirect injection из писем/ячеек — human-in-the-loop на write. | https://mayai.ru/cursor-otkryl-gmail-i-sheets-agentam/ ; Google MCP security note | 2026-09-15 |
| 20 | «Connected» в Tools & MCP **не гарантирует** успешный Google OAuth — проверять живым read/write. | https://mayai.ru/cursor-otkryl-gmail-i-sheets-agentam/ | 2026-09-15 |
| 21 | Sheets API + SA для финотдела — transport в staging, не замена главной книги 1С; типичные кейсы: ДДС, SaaS-реестр, платежный календарь, статусы сверок. | https://dzen.ru/a/aoV6BGni3D3wS-su | 2026-09-15 |
| 22 | Альтернативы community: `dudegladiator/spreadsheet-mcp` (27 tools, uv), `we2go/google-mcp` / `npx google-sheet-mcp init`, npm `mcp-google-sheets` (OAuth env). Для статьи — один канон Path B (freema), остальное — «если уже используете». | GitHub/npm SERP 2026-09-15 | 2026-09-15 |

**Не выдумывать:** показы Wordstat; «Sheets-плагин всегда в Marketplace» (проверять на дату публикации); что SA = доступ ко всему Drive; цифру Smithery installs как факт; обещание «без программиста» для Path B без GCP/SA; что official Google Sheets MCP уже GA (это Preview).

**fact-bank.md:** прямых фактов про MCP+Sheets **нет** — опираться на таблицу выше. Контент-заводные ROI из fact-bank **не тянуть**.

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

- **Можно ли без программиста?** — Path A (если плагин в витрине): да для пилота; Path B (SA+mcp.json): по инструкции, Cursor поможет с JSON; первый реестр ~1–2 ч.
- **Сколько займёт внедрение?** — SA + mcp.json + один тестовый update: **~1–2 ч**.
- **Какие риски для данных?** — OAuth = права вашего Google; SA-ключ = все расшаренные файлы; не класть ПДн; подтверждать write-tools; indirect injection.
- **OAuth или service account?** — OAuth для личного пилота; SA для командного реестра и минимального blast radius.
- **Чем отличается от B82?** — B82 = Python/Node скрипт пишет в staging; B92 = Agent в Cursor правит через MCP без скрипта.
- **Официальный Google Sheets MCP?** — есть как Developer Preview (`sheetsmcp.googleapis.com`); для финотдела в 2026-09 безопаснее начинать с Path B SA.
- **Работает ли в Cloud Agents?** — да через dashboard MCP (help Cursor); локальный интерактивный OAuth не «переезжает» сам — для облака планировать отдельно / SA.

---

## CTA / interlink

- Internal: `/avtomatizaciya-finansov-no-code/`, `/obezlichivanie-dannyh-chatgpt-finansist/`, `/google-sheets-api-integraciya-finotdel/` (B82), `/mcp-cursor-finansist-instrumenty/` (B21)
- Соседние реестры: B51, B58, B83; ротация ключа: B93
- CTA: `https://club.koda-fd.ru/?utm_source=blog&utm_medium=article&utm_campaign=mcp-google-sheets-cursor-reestry` (≤2), `https://t.me/finance_modern?utm_source=blog&utm_medium=article` (≤2)

---

## Handoff marker

`=== EXCALIBUR BLOG RESEARCH ===` — см. `.cursor/excalibur-blog-handoff.md`
