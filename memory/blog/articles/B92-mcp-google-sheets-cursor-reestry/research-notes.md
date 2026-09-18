# Research notes — B92

**topic_id:** B92  
**slug:** mcp-google-sheets-cursor-reestry  
**h1:** Как подключить MCP к Google Sheets в Cursor и править реестры без копипаста  
**research_date:** 2026-09-18  
**publish_target:** koda-fd.ru/blog  
**utility_gate:** PASS (`how_to`, mode B) — подтверждено `scripts/excalibur_blog_utility_gate.py --topic-id B92` и `utility-gate-topic.json`  
**author_id:** olga-kondratskaya  
**related_internal:** `/avtomatizaciya-finansov-no-code/`, `/obezlichivanie-dannyh-chatgpt-finansist/`  
**sibling_queue:** B82 (Sheets API + SA), B21 (MCP в Cursor общий), B51/B58/B83 (реестры в Sheets), B93 (ротация SA)  
**cover_scene_hint:** abstract holographic finance automation dark #0a0a0f purple #8b5cf6, no text

---

## utility_verdict

**PASS** — тема utility-only how_to. Читатель получает рабочий выбор пути подключения Google Sheets к Cursor через MCP (community `mcp-gsheets` на service account **или** remote Google Sheets MCP / Marketplace-плагин при доступности), подготовку реестра под агентные правки, тестовый сценарий «найти строку → обновить статус → перечитать», чеклист безопасности для финданных и troubleshooting. Не новость «Cursor открыл Workspace», не обзор 25 MCP-серверов, не туториал «напиши свой MCP с нуля».

---

## reader_outcome

После гайда финансист сможет подключить MCP Google Sheets в Cursor, дать агенту доступ только к рабочему реестру (через service account или OAuth), попросить обновить статус строки или дописать поля без копирования таблицы в чат и проверить результат перечиткой диапазона через MCP-tool.

---

## action_outline

1. **Решить, нужен ли MCP Sheets** — реестр уже в Google Sheets (договоры, УПД, SaaS, заявки на расход), правки повторяются, устали таскать диапазоны в чат; **не** делать, если нужен жёсткий audit trail / сотни таблиц с enterprise ACL — тогда 1С/CLM, Sheets только staging.
2. **Выбрать путь подключения** — **Path B (финконтур, рекомендуем):** `freema/mcp-gsheets` + service account — расшарить только нужные реестры, ключ в `env`, без доступа агента ко всему Drive (см. B82, B93). **Path A (пилот):** Cursor Marketplace / Workspace-плагин Google Sheets, если доступен в витрине (на 18.09.2026 в официальном changelog явно расписаны Drive/Gmail/Calendar; Sheets в теле changelog **не** детализирован). **Path C (эксперимент):** официальный remote Google Sheets MCP `https://sheetsmcp.googleapis.com/mcp/v1` (Developer Preview, OAuth пользователя) — через `url` в `mcp.json`.
3. **Подготовить реестр** — одна строка = одна сущность; стабильный `doc_key`; лист `staging` для импорта; в облако без сырых ПДн (ИНН/сумма/статус — да; паспорт, полные ФИО — нет); interlink `/obezlichivanie-dannyh-chatgpt-finansist/`.
4. **Path B: Google Cloud + SA** — проект → включить **Google Sheets API** → service account → JSON-ключ → скопировать `client_email` → «Поделиться» на файл реестра с ролью **Редактор** (без «Уведомить»).
5. **Path B: mcp.json в Cursor** — глобально `~/.cursor/mcp.json` или проектно `.cursor/mcp.json`; блок `mcp-gsheets` с `npx -y mcp-gsheets@latest` и `GOOGLE_APPLICATION_CREDENTIALS` (абсолютный путь); JSON-ключ **не** в git.
6. **Path A/C (OAuth)** — Marketplace Customize → Add + OAuth **или** remote URL + static OAuth/`auth` в `mcp.json` (redirect: `https://www.cursor.com/agents/mcp/oauth/callback` и desktop `http://localhost:8787/callback`); минимальные scopes; учитывать, что OAuth = права личного Google, а не least-privilege SA.
7. **Проверить подключение** — перезапуск Cursor; Customize → MCPs → зелёный статус; Output → **MCP Logs**; tool `sheets_check_access` (Path B) или живой запрос «прочитай A1:C5 листа Реестр».
8. **Рабочий сценарий реестра** — промпт с DoD: metadata/get → найти строку по `doc_key` → update/append только в колонки статуса/комментария → get_values на ту же строку → сверка; human approval на каждый write-tool.
9. **Эксплуатация и рост** — allowlist write-tools; ротация ключа SA (B93); при >80–100 заявок/мес или audit — n8n/ERP, Sheets остаётся staging; соседние реестры B51/B58/B83.

**Workflow для статьи:**  
`Реестр в Sheets → (SA share | OAuth plugin/remote) → MCP в Cursor → Agent read/update по doc_key → перечитка диапазона → регламент CFO`

---

## Яндекс Wordstat (MCP user-mcp-kv)

⚠️ **WORDSTAT AUTH WARNING / MCP UNAVAILABLE:** сервер MCP `user-mcp-kv` в этой Cloud-сессии **не подключён** (в каталоге dynamic tools: `cursor`, `Cursor Automation Tools`, `cursor-cloud`, `cursor-subscriptions`). Вызов `wordstat_get_top_requests` **не выполнен**. Точные показы/мес **не получены** и **не выдуманы**.

Обновление токена / подключение MCP-KV: https://oauth.yandex.ru/authorize?response_type=token&client_id=c654b948515a4a07a4c89648a0831d40

### Таблица спроса (Wordstat)

| Фраза | Показы в месяц |
| --- | --- |
| mcp google sheets cursor | *не получено — MCP Wordstat недоступен* |
| cursor mcp | *не получено — MCP Wordstat недоступен* |
| mcp сервер для cursor | *не получено — MCP Wordstat недоступен* |
| автоматизация финотдела | *не получено — MCP Wordstat недоступен* |
| google sheets mcp | *не получено — MCP Wordstat недоступен* |
| подключить mcp cursor | *не получено — MCP Wordstat недоступен* |

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

**SEO-вывод:** SERP по `mcp google sheets cursor` — **EN-гайды community MCP** (freema, we2go, xing5, spreadsheet-mcp), **официальный Google Sheets remote MCP** (Developer Preview, сент. 2026) и **новости Cursor Workspace (авг. 2026)**. RU how-to «финансист + реестр + Cursor» почти нет. Угол КОДА: **правка управленческих реестров через MCP без копипаста**, с веткой SA для безопасности и явным сравнением с B82 (скрипт) и B21 (общий MCP).

---

## SERP (WebSearch Cursor, 18.09.2026)

Приоритет — живой WebSearch; `research-serp.json` (шаг 0) — черновик URL; query `2026 2026` и часть сниппетов **нерелевантны** — не копировать.

### Primary: `mcp google sheets cursor 2026`

| # | URL | Тип | Пробел для КОДА |
| --- | --- | --- | --- |
| 1 | https://developers.google.com/workspace/sheets/api/guides/configure-mcp-server | Официальный Google Sheets remote MCP | Dev Preview; нет реестров финотдела |
| 2 | https://cursor.com/docs/mcp | Официальный reference Cursor MCP | Нет Sheets-кейса |
| 3 | https://cursor.com/help/customization/mcp | Help: mcp.json, OAuth, approvals, Cloud Agents | Канон шагов |
| 4 | https://github.com/freema/mcp-gsheets | Community MCP (SA) — канон Path B | EN; dev-фокус, не CFO |
| 5 | https://github.com/we2go/google-mcp | npx wizard OAuth/SA | Sheets; не реестры |
| 6 | https://github.com/xing5/mcp-google-sheets | Python/uvx, SA/OAuth | EN setup |
| 7 | https://github.com/dudegladiator/spreadsheet-mcp | Python/uv, 27 tools | Установка для dev |
| 8 | https://mcp-catalog.ru/tutorials/google-sheets-cursor | RU туториал community | Нет finance/SA-регламента |
| 9 | https://www.strac.io/blog/google-sheets-mcp-server | EN secure setup 2026 | Security-угол, не реестры |

### Official / Workspace news

| # | URL | Тип | Пробел |
| --- | --- | --- | --- |
| 1 | https://cursor.com/changelog/google-workspace-plugins | Changelog (проверка 18.09.2026) | Drive/Gmail/Calendar; **Sheets в теле не расписан** |
| 2 | https://developers.google.com/workspace/guides/configure-mcp-servers | Google Workspace MCP hub | Remote endpoints; не Cursor finance |
| 3 | https://pondero.ai/news/2026-08-04-cursor-google-workspace/ | Вторичный обзор 04.08.2026 | Утверждает Sheets в пяти плагинах — сверять с primary changelog |
| 4 | https://mayai.ru/cursor-otkryl-gmail-i-sheets-agentam/ | RU разбор | Мало SA/реестров |
| 5 | https://vibecoding.ru/news/2026/08/03/cursor-google-workspace-plugins | RU новость 04.08 | Docs/Sheets могли временно пропасть из витрины |

### Secondary: `автоматизация финотдела` + Sheets/реестры

| # | URL | Тип | Пробел |
| --- | --- | --- | --- |
| 1 | https://dzen.ru/a/aoAx4V_t_ztBh5aj | Заявки Forms→Sheets | Без MCP |
| 2 | https://dzen.ru/a/aoV6BGni3D3wS-su | Sheets API + SA (B82-линия) | Скрипт, не Agent+MCP |
| 3 | https://bpadevelop.ru/blog/avtomatizaciya-platezhnogo-kalendarya/ | Платёжный календарь 2026 | ERP-уклон |
| 4 | https://adesk.ru/blog/platezhnyi-kalendar-dlia-it-kompanii-zachem-nuzhen-i-kak-sostavit/ | Шаблон ПК в Sheets | Без Cursor |
| 5 | https://koda-fd.ru/blog/ai-dlya-finansista-2026/ | Hub КОДА | Нет MCP Cursor |

### Конкурентный зазор (угол КОДА)

1. **Finance-first** — не «подключи Sheets к Cursor», а «перестань копировать реестр в чат: agent правит строку по `doc_key`».
2. **Три пути с честным выбором** — SA+mcp-gsheets (production) vs OAuth Marketplace/remote Google MCP (пилот/preview) vs «не сейчас» (ERP).
3. **Связка с реестрами серии** — договоры (B51), УПД (B58), SaaS (B83); MCP = слой правок поверх уже спроектированной таблицы.
4. **Security block** — минимальный share, ключ вне git, approval tools, indirect prompt injection (Google docs 2026-09-14), обезличивание.
5. **Verify loop** — после write всегда get_values; «Connected ≠ authorized».
6. **Fork от B82** — B82 = свой Python-скрипт; B92 = те же SA+share, но правки через Agent+MCP без написания кода.

---

## Таблица фактов

| # | Утверждение | Источник | Дата проверки |
| --- | --- | --- | --- |
| 1 | MCP подключает Cursor к внешним инструментам; Agent вызывает tools в чате. | https://cursor.com/help/customization/mcp | 2026-09-18 |
| 2 | Конфиг: проектный `.cursor/mcp.json` + глобальный `~/.cursor/mcp.json`; оба мержатся, при совпадении имени побеждает **проектный**. | https://cursor.com/help/customization/mcp | 2026-09-18 |
| 3 | Локальный MCP: `command`/`args`/`env`; удалённый — `url` (+ опционально `headers` / static `auth`). Транспорты: stdio, SSE, Streamable HTTP. | https://cursor.com/docs/mcp | 2026-09-18 |
| 4 | One-click: Customize → MCPs → Add to Cursor; после ручного `mcp.json` — **перезапуск Cursor**. | https://cursor.com/help/customization/mcp | 2026-09-18 |
| 5 | По умолчанию Agent **запрашивает approval** перед MCP-tool; с Cursor 3.6+ — Auto-review / allowlist / `permissions.json`. | https://cursor.com/help/customization/mcp | 2026-09-18 |
| 6 | Troubleshooting: Output → **MCP Logs** (`Ctrl+Shift+U` / `Cmd+Shift+U`). | https://cursor.com/help/customization/mcp | 2026-09-18 |
| 7 | Cloud Agents поддерживают MCP из Dashboard → Plugins & MCPs (Team); локальный интерактивный OAuth с IDE **не обязан** автоматически переехать. | https://cursor.com/help/customization/mcp ; https://cursor.com/docs/mcp | 2026-09-18 |
| 8 | Static OAuth redirect Cursor: `https://www.cursor.com/agents/mcp/oauth/callback` (web/agents) и `http://localhost:8787/callback` (desktop). | https://cursor.com/docs/mcp | 2026-09-18 |
| 9 | Официальный changelog Cursor Google Workspace plugins перечисляет **Drive, Gmail, Calendar**; Sheets/Docs в этом документе **не детализированы** (проверка 18.09.2026). | https://cursor.com/changelog/google-workspace-plugins | 2026-09-18 |
| 10 | Вторичные источники (Pondero 04.08.2026) утверждают 5 плагинов включая Sheets — для статьи опираться на primary changelog + «проверить витрину на дату публикации». | https://pondero.ai/news/2026-08-04-cursor-google-workspace/ | 2026-09-18 |
| 11 | Google Sheets remote MCP: URL `https://sheetsmcp.googleapis.com/mcp/v1`; статус **Developer Preview**; last updated **2026-09-14**. | https://developers.google.com/workspace/sheets/api/guides/configure-mcp-server | 2026-09-18 |
| 12 | Для Google Sheets MCP нужно включить Sheets API (`sheets.googleapis.com`) и Sheets MCP API (`sheetsmcp.googleapis.com`). | https://developers.google.com/workspace/sheets/api/guides/configure-mcp-server | 2026-09-18 |
| 13 | Tools official Sheets MCP: `get_values`, `get_spreadsheet`, `update_spreadsheet`, `update_values`, `update_formulas`, `insert_dimension`. | https://developers.google.com/workspace/sheets/api/guides/configure-mcp-server | 2026-09-18 |
| 14 | Google прямо предупреждает об **indirect prompt injection** при чтении недоверенных таблиц/контента через Workspace MCP. | https://developers.google.com/workspace/sheets/api/guides/configure-mcp-server | 2026-09-18 |
| 15 | `freema/mcp-gsheets`: Node.js **v20+**, Sheets API, service account JSON; `npx -y mcp-gsheets@latest` + `GOOGLE_APPLICATION_CREDENTIALS` / `GOOGLE_PROJECT_ID`. | https://github.com/freema/mcp-gsheets | 2026-09-18 |
| 16 | Ключевые tools mcp-gsheets для реестра: `sheets_get_values`, `sheets_update_values`, `sheets_append_values`, `sheets_batch_get_values`, `sheets_get_metadata`, `sheets_check_access`. | https://github.com/freema/mcp-gsheets | 2026-09-18 |
| 17 | `sheets_append_values`: default `insertDataOption` = **OVERWRITE** — для реестра явно указывать `INSERT_ROWS`, если нужно сдвигать строки. | https://github.com/freema/mcp-gsheets | 2026-09-18 |
| 18 | Service account видит **только** таблицы, расшаренные на `client_email`; IAM Cloud **не заменяет** Share файла. | https://developers.google.com/workspace/guides/create-credentials#service-account | 2026-09-18 |
| 19 | Scope `https://www.googleapis.com/auth/spreadsheets` — read/write расшаренных таблиц; доступ на уровне файла; ячейки/листы — Protected ranges. | https://developers.google.com/workspace/sheets/api/scopes | 2026-09-18 |
| 20 | Квота Sheets API write: **300 запросов/мин** на проект; превышение → HTTP **429**; batch = один запрос. | https://developers.google.com/workspace/sheets/api/limits | 2026-09-18 |
| 21 | `we2go/google-mcp`: wizard `npx google-sheet-mcp init` (SA или OAuth); tools read/write/append. | https://github.com/we2go/google-mcp | 2026-09-18 |
| 22 | Заявки на расход Forms→Sheets: при **>80–100** заявок/мес Sheets — staging перед ERP/n8n. | https://dzen.ru/a/aoAx4V_t_ztBh5aj | 2026-09-18 |
| 23 | Sheets API + SA для финотдела — transport в staging, не замена главной книги 1С. | https://dzen.ru/a/aoV6BGni3D3wS-su | 2026-09-18 |

**Не выдумывать:** показы Wordstat; «Sheets-плагин всегда в Marketplace» (проверять витрину); что SA = доступ ко всему Drive; цифры сторонних обзоров installs; обещание «без программиста» для Path B без упоминания GCP/SA; доступность Google remote MCP вне Developer Preview.

**fact-bank.md:** прямых фактов про MCP+Sheets нет — опираться на таблицу выше. Контент-заводные ROI из fact-bank **не тянуть**.

---

## Структура H2 для writer (из карточки B92)

1. Когда это нужно финотделу (и когда нет)  
2. Подготовка данных и безопасность (без сырых ПДн в облако)  
3. Пошаговая настройка / скрипт / сценарий  
4. Проверка результата и типичные ошибки  
5. Что автоматизировать дальше  

**Рекомендация угла H2.3:** основной маршрут = Path B (`mcp-gsheets` + SA); Path A/C — короткая ветка «если витрина/preview доступны».

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

**Пример remote (Path C — опционально, Developer Preview):**

```json
{
  "mcpServers": {
    "sheets": {
      "url": "https://sheetsmcp.googleapis.com/mcp/v1"
    }
  }
}
```

(OAuth/client credentials — по доке Google + Cursor static `auth` при необходимости; не хардкодить секреты.)

**Тестовый промпт агента (реестр):**

> Подключись к таблице `{SPREADSHEET_ID}`. На листе `Реестр` найди строку, где колонка `doc_key` = `DOG-2026-014`. Прочитай текущие значения колонок `status` и `comment`. Если `status` ≠ «Оплачен», предложи обновление на «На согласовании» и допиши в `comment` сегодняшнюю дату. После write перечитай ту же строку и покажи diff.

---

## FAQ-кандидаты

- **Можно ли без программиста?** — Path A (Marketplace+OAuth): да для пилота, если плагин в витрине; Path B (SA+mcp.json): по инструкции B82/B92, Cursor поможет с JSON; первый реестр ~1–2 ч.
- **Сколько займёт внедрение?** — SA + mcp.json + один тестовый update: **~1–2 ч**; OAuth-плагин быстрее при доступной витрине.
- **Какие риски для данных?** — OAuth = права вашего Google; SA-ключ = все расшаренные файлы; не класть ПДн; подтверждать write-tools; indirect injection из ячеек/писем (Google + MayAI).
- **OAuth или service account?** — OAuth для личного пилота / Google remote MCP; SA для командного реестра, cron, минимального blast radius.
- **Чем отличается от B82?** — B82 = Python/Node скрипт пишет в staging; B92 = Agent в Cursor правит через MCP без скрипта.
- **Работает ли в Cloud Agents?** — да через Team Dashboard MCP; локальный OAuth IDE не переезжает автоматически — для облака предпочтительнее SA/team connector.
- **Что с официальным Google Sheets MCP?** — Developer Preview (`sheetsmcp.googleapis.com`); подходит как эксперимент OAuth; для финконтура с least privilege — всё ещё SA + community MCP.

---

## CTA / interlink

- Internal: `/avtomatizaciya-finansov-no-code/`, `/obezlichivanie-dannyh-chatgpt-finansist/`, `/google-sheets-api-integraciya-finotdel/` (B82), `/mcp-cursor-finansist-instrumenty/` (B21)
- Соседние реестры: B51, B58, B83; ротация ключа: B93
- CTA: `https://club.koda-fd.ru/?utm_source=blog&utm_medium=article&utm_campaign=mcp-google-sheets-cursor-reestry` (≤2), `https://t.me/finance_modern?utm_source=blog&utm_medium=article` (≤2)

---

## Handoff marker

`=== EXCALIBUR BLOG RESEARCH ===` — см. `.cursor/excalibur-blog-handoff.md`
