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

**PASS** — тема utility-only how_to. Читатель получает практический маршрут: выбрать способ подключения Google Sheets к Cursor через MCP (service account + `mcp-gsheets` для финконтура **или** OAuth/remote MCP для пилота), подготовить реестр под агентные правки, выполнить сценарий «найти строку по `doc_key` → обновить статус → перечитать», закрыть чеклист безопасности. Не новость «Cursor открыл Workspace», не обзор MCP-каталога, не «напиши свой MCP с нуля».

---

## reader_outcome

После гайда финансист сможет подключить MCP Google Sheets в Cursor, дать агенту доступ только к рабочему реестру (через service account или OAuth), попросить обновить статус строки / дописать поля без копирования таблицы в чат и проверить результат перечиткой диапазона через MCP-tool.

---

## action_outline

1. **Решить, нужен ли MCP Sheets** — реестр уже в Google Sheets (договоры, УПД, SaaS, заявки на расход), правки повторяются, устали таскать диапазоны в чат; **не** делать, если нужен жёсткий audit trail / сотни таблиц с enterprise ACL — тогда 1С/CLM, Sheets только staging.
2. **Выбрать путь подключения** — **Path B (рекомендуем финотделу):** `freema/mcp-gsheets` + service account — шарим только нужные реестры, ключ в `env`, blast radius минимальный. **Path A (пилот):** Cursor Marketplace / Customize OAuth-плагин Google (если доступен в витрине; в changelog 03.08.2026 детально Drive/Gmail/Calendar). **Path C (Developer Preview):** официальный remote MCP Google `https://sheetsmcp.googleapis.com/mcp/v1` + OAuth в GCP — для экспериментов, не как единственный production-контур без Human-in-the-loop.
3. **Подготовить реестр** — одна строка = одна сущность; стабильный `doc_key`; лист `staging` для импорта; в облако без сырых ПДн (ИНН/сумма/статус — да; паспорт, полные ФИО — нет); interlink `/obezlichivanie-dannyh-chatgpt-finansist/`.
4. **Path B: Google Cloud + SA** — проект → включить **Google Sheets API** → service account → JSON-ключ → скопировать `client_email` → «Поделиться» на файл реестра с ролью **Редактор** (без «Уведомить»).
5. **Path B: mcp.json в Cursor** — глобально `~/.cursor/mcp.json` или проектно `.cursor/mcp.json`; блок `mcp-gsheets` с `npx -y mcp-gsheets@latest`, `GOOGLE_PROJECT_ID`, `GOOGLE_APPLICATION_CREDENTIALS` (абсолютный путь); JSON-ключ **не** в git.
6. **Path A / C (опционально)** — Marketplace: Customize → MCPs → Add + OAuth; либо remote URL `sheetsmcp.googleapis.com/mcp/v1` (нужны Sheets API + Sheets MCP API `sheetsmcp.googleapis.com`, OAuth consent, scopes spreadsheets/drive). Для финреестров предпочитать Path B.
7. **Проверить подключение** — перезапуск Cursor; Customize → MCPs → зелёный статус; Output → **MCP Logs**; tool `sheets_check_access` (Path B) или живой запрос «прочитай A1:C5 листа Реестр».
8. **Рабочий сценарий реестра** — промпт с DoD: `sheets_get_metadata` → найти строку по `doc_key` → `sheets_update_values` / `sheets_append_values` только в колонки статуса/комментария → `sheets_get_values` на ту же строку → сверка; human approval на каждый write-tool.
9. **Эксплуатация и рост** — allowlist write-tools; ротация ключа SA (B93); при >80–100 заявок/мес или audit — n8n/ERP, Sheets остаётся staging; соседние реестры B51/B58/B83.

**Workflow для статьи:**  
`Реестр в Sheets → (SA share | OAuth plugin | Google remote MCP) → MCP в Cursor → Agent read/update по doc_key → перечитка диапазона → регламент CFO`

---

## Яндекс Wordstat (MCP user-mcp-kv)

⚠️ **WORDSTAT AUTH WARNING / unavailable:** сервер MCP `user-mcp-kv` в этой Cloud-сессии **не подключён** (в каталоге dynamic tools: `cursor`, `Cursor Automation Tools`, `cursor-cloud`, `cursor-subscriptions`). Вызов `wordstat_get_top_requests` **не выполнен**. Точные показы/мес **не получены** и **не выдуманы**.

Обновление токена / подключение MCP-KV: https://oauth.yandex.ru/authorize?response_type=token&client_id=c654b948515a4a07a4c89648a0831d40

### Таблица спроса (Wordstat)

| Фраза | Показы в месяц |
| --- | --- |
| mcp google sheets cursor | *не получено — MCP unavailable* |
| cursor mcp | *не получено — MCP unavailable* |
| mcp сервер для cursor | *не получено — MCP unavailable* |
| автоматизация финотдела | *не получено — MCP unavailable* |
| google sheets mcp | *не получено — MCP unavailable* |
| подключить mcp cursor | *не получено — MCP unavailable* |
| mcp-gsheets | *не получено — MCP unavailable* |

**Экспертная семантика (LSI для writer, без цифр спроса):**

| Кластер | Фразы | Роль |
| --- | --- | --- |
| Primary | mcp google sheets cursor, google sheets mcp cursor | H1, title |
| Setup | mcp.json cursor, cursor marketplace google sheets, mcp-gsheets service account, sheetsmcp.googleapis.com | H2 пошагово |
| Finance | автоматизация финотдела google sheets, реестр договоров cursor, править реестр без копипаста | угол КОДА |
| Registry | реестр upd google sheets, реестр saas подписок, doc_key find update | кейсы |
| Security | service account json не в git, обезличивание sheets, oauth scopes минимум, indirect prompt injection | FAQ |
| Ops | sheets_check_access, mcp logs cursor, unauthorized google mcp, HTTP 429 sheets quota | troubleshooting |
| Adjacent | cursor google workspace plugins 2026, mcp cursor finansist | interlink B21 |

**SEO-вывод:** SERP 17.09.2026 по `mcp google sheets cursor` — смесь **EN-гайдов community MCP** (freema/mcp-gsheets, we2go, PasteSheet), **официальной доки Google remote Sheets MCP** (Developer Preview, last updated 2026-09-14) и **новостей Cursor + Google Workspace (август 2026)**. Почти нет RU how-to «финансист + реестр + Cursor + без копипаста». Угол КОДА: правка управленческих реестров через MCP, с Path B (SA) как основным и честным сравнением с B82 (скрипт) и B21 (общий MCP).

---

## SERP (WebSearch Cursor, 17.09.2026)

Приоритет — живой WebSearch; `research-serp.json` (шаг 0, 17.09.2026) использован как URL-черновик. Query `2026 2026` и часть сниппетов **нерелевантны** — не копировать. Свежий WebSearch выявил важный апдейт: **официальный Google Sheets remote MCP**.

### Primary: `MCP Google Sheets Cursor` / `mcp-gsheets` / service account

| # | URL | Тип | Пробел для КОДА |
| --- | --- | --- | --- |
| 1 | https://developers.google.com/workspace/sheets/api/guides/configure-mcp-server | Official Google remote MCP (Preview) | Нет реестров финотдела; OAuth/GCP тяжёлый |
| 2 | https://github.com/freema/mcp-gsheets | Community MCP + SA | EN; dev-фокус, не CFO |
| 3 | https://www.npmjs.com/package/mcp-gsheets | npm package docs | Нет finance angle |
| 4 | https://cursor.com/docs/mcp | Официальный MCP reference Cursor | Нет Sheets-кейса |
| 5 | https://cursor.com/help/customization/mcp | Help: mcp.json, OAuth, approvals | Канон шагов |
| 6 | https://github.com/we2go/google-mcp | npx wizard OAuth/SA | Sheets+Docs; не реестры |
| 7 | https://dev.to/pastesheet/google-sheets-in-vs-code-cursor-and-windsurf-over-mcp-5467 | Hosted URL MCP | Публичные листы; не SA |
| 8 | https://llmversus.com/mcp/google-sheets-mcp | Community install guide 2026 | Общий setup |
| 9 | https://mcpcursor.com/server/google-sheets-mcp | Каталог MCP | Тонкий listing |
| 10 | https://mcp-catalog.ru/tutorials/gsheets-cursor | RU: freema → Cursor | Нет финреестров |

### News / Workspace (август 2026) + официальный Sheets MCP (сент. 2026)

| # | URL | Тип | Пробел |
| --- | --- | --- | --- |
| 1 | https://cursor.com/changelog/google-workspace-plugins | Changelog 03.08.2026 | Drive/Gmail/Calendar; Sheets в теле **не расписан** |
| 2 | https://mayai.ru/cursor-otkryl-gmail-i-sheets-agentam/ | RU разбор релиза | Мало SA/реестров |
| 3 | https://vibecoding.ru/news/2026/08/03/cursor-google-workspace-plugins | RU новость | Docs/Sheets могли пропасть из витрины 04.08 |
| 4 | https://github.com/cursor/plugins | Official plugins repo | Проверять наличие google-sheets на дату публикации |

### Secondary: `автоматизация финотдела` + реестры

| # | URL | Тип | Пробел |
| --- | --- | --- | --- |
| 1 | https://koda-fd.ru/blog/ai-dlya-finansista-2026/ | Hub КОДА | Нет MCP Cursor |
| 2 | https://datalopata.ru/blog/avtomatizatsija-finansov-sistemnyj-podhod-k-uchetu-v-2026-godu/ | Приоритеты автоматизации | ERP-уклон |
| 3 | https://znaj.org/ru/6-luchshikh-reshenii-2026-goda-avtomatizacii-upravleniya-finansami/ | Обзор решений 2026 | Не Cursor |

### Конкурентный зазор (угол КОДА)

1. **Finance-first** — не «подключи Sheets к Cursor», а «перестань копировать реестр в чат: agent правит строку по `doc_key`».
2. **Три пути с выбором** — SA+mcp-gsheets (production финконтур) vs OAuth Marketplace (пилот) vs Google remote MCP Preview (эксперимент); honest note про статус Marketplace Sheets и Preview.
3. **Связка с реестрами серии** — договоры (B51), УПД (B58), SaaS (B83); MCP = слой правок поверх уже спроектированной таблицы.
4. **Security block** — минимальный share, ключ вне git, approval tools, indirect prompt injection (Google docs + Sheets MCP), обезличивание.
5. **Verify loop** — после write всегда `get_values` / `sheets_get_values`; «Connected ≠ authorized».
6. **Fork от B82** — B82 = свой Python-скрипт; B92 = те же SA+share, но правки через Agent+MCP без написания кода.

---

## Таблица фактов

| # | Утверждение | Источник | Дата проверки |
| --- | --- | --- | --- |
| 1 | MCP подключает Cursor к внешним инструментам; Agent вызывает tools в чате. | https://cursor.com/help/customization/mcp | 2026-09-17 |
| 2 | Конфиг: проектный `.cursor/mcp.json` + глобальный `~/.cursor/mcp.json`; оба мержатся; при совпадении имени побеждает **проектный**. | https://cursor.com/help/customization/mcp | 2026-09-17 |
| 3 | Локальный MCP: `command`/`args`/`env`; удалённый — поле `url` (+ опционально `headers` / static OAuth `auth`). | https://cursor.com/docs/mcp ; https://cursor.com/help/customization/mcp | 2026-09-17 |
| 4 | Transports в Cursor: stdio, SSE, Streamable HTTP. | https://cursor.com/docs/mcp | 2026-09-17 |
| 5 | One-click: Customize → MCPs → Add to Cursor; после ручного `mcp.json` — **перезапуск Cursor**. | https://cursor.com/help/customization/mcp | 2026-09-17 |
| 6 | По умолчанию Agent **запрашивает approval** перед MCP-tool; с Cursor 3.6+ — Auto-review / allowlist. | https://cursor.com/help/customization/mcp | 2026-09-17 |
| 7 | Troubleshooting: Output → **MCP Logs** (`Ctrl+Shift+U` / `Cmd+Shift+U`). | https://cursor.com/help/customization/mcp | 2026-09-17 |
| 8 | 03.08.2026 Cursor анонсировал Google Workspace plugins: агенты работают с Drive, Gmail, Calendar из редактора; установка из Marketplace / Customize. | https://cursor.com/changelog/google-workspace-plugins | 2026-09-17 |
| 9 | В changelog 03.08.2026 детально перечислены Drive, Gmail, Calendar; Sheets в этом документе **не расписан**. | https://cursor.com/changelog/google-workspace-plugins | 2026-09-17 |
| 10 | По отчёту vibecoding.ru (04.08.2026): Docs/Sheets могли временно исчезнуть из витрины; мин. версия Cursor **3.13.0**; OAuth-bug с callback `cursor://`. | https://vibecoding.ru/news/2026/08/03/cursor-google-workspace-plugins | 2026-09-17 |
| 11 | Google предлагает **remote** Sheets MCP (Developer Preview): URL `https://sheetsmcp.googleapis.com/mcp/v1`, transport Streamable HTTP, auth OAuth 2.0; last updated **2026-09-14**. | https://developers.google.com/workspace/sheets/api/guides/configure-mcp-server | 2026-09-17 |
| 12 | Для official Sheets MCP в GCP нужно включить Sheets API (`sheets.googleapis.com`) и Sheets MCP API (`sheetsmcp.googleapis.com`). | https://developers.google.com/workspace/sheets/api/guides/configure-mcp-server | 2026-09-17 |
| 13 | Tools official Sheets MCP (документированный минимум): `get_values`, `get_spreadsheet`, `update_spreadsheet`, `update_values`, `update_formulas`, `insert_dimension`. | https://developers.google.com/workspace/sheets/api/guides/configure-mcp-server | 2026-09-17 |
| 14 | Google явно предупреждает про **indirect prompt injection** при MCP+Sheets: агент может читать/менять/удалять данные; нужен review действий. | https://developers.google.com/workspace/sheets/api/guides/configure-mcp-server | 2026-09-17 |
| 15 | `freema/mcp-gsheets`: Node.js **v20+**, Google Cloud project, Sheets API, service account JSON; `npx -y mcp-gsheets@latest` + `GOOGLE_APPLICATION_CREDENTIALS` (+ `GOOGLE_PROJECT_ID`). | https://github.com/freema/mcp-gsheets | 2026-09-17 |
| 16 | Ключевые tools mcp-gsheets для реестра: `sheets_get_values`, `sheets_update_values`, `sheets_append_values`, `sheets_batch_get_values`, `sheets_get_metadata`, `sheets_check_access`. | https://github.com/freema/mcp-gsheets | 2026-09-17 |
| 17 | `sheets_append_values`: по умолчанию `insertDataOption` = **OVERWRITE** — для реестра явно указывать `INSERT_ROWS`, если нужно сдвигать строки. | https://github.com/freema/mcp-gsheets | 2026-09-17 |
| 18 | Service account видит **только** таблицы, расшаренные на `client_email` из JSON; IAM-роли Cloud **не заменяют** Share файла. | https://developers.google.com/workspace/guides/create-credentials#service-account | 2026-09-17 |
| 19 | Scope `https://www.googleapis.com/auth/spreadsheets` — read/write расшаренных таблиц; применяется ко **всему файлу**. | https://developers.google.com/workspace/sheets/api/scopes | 2026-09-17 |
| 20 | Квоты Sheets API: read/write **300/мин на проект** и **60/мин на user/project**; превышение → HTTP **429**; refill каждую минуту. | https://developers.google.com/workspace/sheets/api/limits | 2026-09-17 |
| 21 | Стандартное использование Sheets API сейчас без доп. платы; Google планирует биллинг превышений квот **later in 2026**. | https://developers.google.com/workspace/sheets/api/limits | 2026-09-17 |
| 22 | `we2go/google-mcp`: `npx google-sheet-mcp init` — wizard SA или OAuth для Cursor/VS Code. | https://github.com/we2go/google-mcp | 2026-09-17 |
| 23 | Hosted MCP (PasteSheet): подключение по `url` в `mcp.json`; без GCP для публичных листов («Anyone with the link»). | https://dev.to/pastesheet/google-sheets-in-vs-code-cursor-and-windsurf-over-mcp-5467 | 2026-09-17 |
| 24 | Риск MCP+Google: агент наследует права пользователя; в письмах/ячейках возможна indirect prompt injection — human-in-the-loop на write. | https://mayai.ru/cursor-otkryl-gmail-i-sheets-agentam/ ; https://developers.google.com/workspace/sheets/api/guides/configure-mcp-server | 2026-09-17 |
| 25 | «Connected» в Tools & MCP **не гарантирует** успешный Google OAuth — проверять живым read/write. | https://mayai.ru/cursor-otkryl-gmail-i-sheets-agentam/ | 2026-09-17 |
| 26 | Cloud Agents: MCP настраивается отдельно в dashboard (Team → Integrations & MCP); локальный интерактивный OAuth **не переезжает** автоматически. | https://cursor.com/help/customization/mcp ; https://mayai.ru/cursor-otkryl-gmail-i-sheets-agentam/ | 2026-09-17 |
| 27 | В 2026 финотдел автоматизирует в первую очередь классификацию платежей, сверки, управленческую отчётность — Sheets+MCP = **transport правок**, не GL. | https://koda-fd.ru/blog/ai-dlya-finansista-2026/ | 2026-09-17 |

**Не выдумывать:** показы Wordstat; «Sheets-плагин всегда в Marketplace»; что SA = доступ ко всему Drive; цифры «N installs» с каталогов; обещание «без программиста» для Path B/C без GCP; что official Google MCP уже GA (это Developer Preview на 2026-09-14).

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

**Пример remote (Path C — только как опция Preview, не как основной финконтур):**

```json
{
  "mcpServers": {
    "googlesheets": {
      "url": "https://sheetsmcp.googleapis.com/mcp/v1"
    }
  }
}
```

(Для production Preview потребуется OAuth client/scopes по доке Google; для реестров КОДА — Path B.)

**Тестовый промпт агента (реестр):**

> Подключись к таблице `{SPREADSHEET_ID}`. На листе `Реестр` найди строку, где колонка `doc_key` = `DOG-2026-014`. Прочитай текущие значения колонок `status` и `comment`. Если `status` ≠ «Оплачен», предложи обновление на «На согласовании» и допиши в `comment` сегодняшнюю дату. После write перечитай ту же строку и покажи diff.

---

## FAQ-кандидаты (из карточки)

- **Можно ли без программиста?** — Path A (Marketplace+OAuth): да для пилота, если плагин в витрине; Path B (SA+mcp.json): по инструкции, Cursor поможет с JSON; Path C — нужен GCP Preview. Production Path B: 1–2 ч на первый реестр.
- **Сколько займёт внедрение?** — SA + mcp.json + один тестовый update: **~1–2 ч**; OAuth-плагин быстрее, если доступен.
- **Какие риски для данных?** — OAuth = права вашего Google; SA-ключ = все расшаренные файлы; не класть ПДн; подтверждать write-tools; indirect injection из писем/ячеек.
- **OAuth или service account?** — OAuth для личного пилота; SA для командного реестра и минимального blast radius.
- **Чем отличается от B82?** — B82 = Python/Node скрипт пишет в staging; B92 = Agent в Cursor правит через MCP без скрипта.
- **Работает ли в Cloud Agents?** — локальный OAuth не переезжает автоматически; Team MCP / SA настраивать отдельно.
- **Official Google MCP вместо mcp-gsheets?** — можно для эксперимента (Preview); для финреестров с ограниченным доступом предпочитать SA+mcp-gsheets.

---

## CTA / interlink

- Internal: `/avtomatizaciya-finansov-no-code/`, `/obezlichivanie-dannyh-chatgpt-finansist/`, `/google-sheets-api-integraciya-finotdel/` (B82), `/mcp-cursor-finansist-instrumenty/` (B21)
- Соседние реестры: B51, B58, B83; ротация ключа: B93
- CTA: `https://club.koda-fd.ru/?utm_source=blog&utm_medium=article&utm_campaign=mcp-google-sheets-cursor-reestry` (≤2), `https://t.me/finance_modern?utm_source=blog&utm_medium=article` (≤2)

---

## Handoff marker

`=== EXCALIBUR BLOG RESEARCH ===` — см. `.cursor/excalibur-blog-handoff.md`
