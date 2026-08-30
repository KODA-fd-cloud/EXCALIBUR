# Research notes — B92

**topic_id:** B92  
**slug:** mcp-google-sheets-cursor-reestry  
**h1:** Как подключить MCP к Google Sheets в Cursor и править реестры без копипаста  
**research_date:** 2026-08-30  
**publish_target:** koda-fd.ru/blog  
**utility_gate:** PASS (`how_to`, mode B)  
**utility_verdict:** PASS  
**author_id:** olga-kondratskaya  
**related_internal:** `/avtomatizaciya-finansov-no-code/`, `/obezlichivanie-dannyh-chatgpt-finansist/`  
**sibling_queue:** B82 (Sheets API + SA), B21 (MCP в Cursor общий), B51/B58/B83 (реестры в Sheets), B93 (ротация SA)  
**cover_scene_hint:** abstract holographic finance automation dark #0a0a0f purple #8b5cf6, no text  
**wordstat_status:** UNAVAILABLE (MCP `user-mcp-kv` не в каталоге dynamic tools этой сессии)

---

## utility_verdict

**PASS** — utility-only how_to. Читатель получает: (1) выбор Path A (Marketplace/OAuth, если Sheets-плагин доступен) vs Path B (community `freema/mcp-gsheets` + service account); (2) подготовку реестра под агентные правки; (3) `mcp.json` + share на SA; (4) тестовый цикл «найти по `doc_key` → update → перечитать»; (5) security/troubleshooting. Не новость про Workspace-релиз, не обзор 25 MCP-серверов, не «напиши свой MCP с нуля».

---

## reader_outcome

После гайда финансист подключит MCP Google Sheets в Cursor, даст агенту доступ только к рабочему реестру (SA share или OAuth-плагин), попросит обновить статус/комментарий строки без копипаста таблицы в чат и сверит результат перечиткой диапазона через MCP-tool.

---

## action_outline

1. **Решить, нужен ли MCP Sheets** — реестр уже в Google Sheets (договоры, УПД, SaaS, заявки), правки повторяются, устали таскать диапазоны в чат; **не** делать, если нужен жёсткий audit trail / сотни таблиц с enterprise ACL — тогда 1С/CLM, Sheets только staging.
2. **Выбрать путь** — **Path A (пилот):** плагин из Cursor Marketplace / Customize → OAuth (если Sheets в витрине на дату публикации); **Path B (финконтур):** `freema/mcp-gsheets` + service account — расшарить только нужные реестры, ключ в `env`, без доступа ко всему Drive.
3. **Подготовить реестр** — одна строка = одна сущность; стабильный `doc_key`; лист `staging`; без сырых ПДн (ИНН/сумма/статус — да; паспорт, полные ФИО — нет); interlink `/obezlichivanie-dannyh-chatgpt-finansist/`.
4. **Path B: Google Cloud + SA** — проект → включить **Google Sheets API** → service account → JSON-ключ → `client_email` → «Поделиться» на файл с ролью **Редактор** (без «Уведомить»).
5. **Path B: mcp.json** — `~/.cursor/mcp.json` или `.cursor/mcp.json`; блок `mcp-gsheets` с `npx -y mcp-gsheets@latest` и `GOOGLE_APPLICATION_CREDENTIALS` (абсолютный путь); JSON-ключ **не** в git.
6. **Path A: Marketplace** — Customize → MCPs → Add → OAuth; минимальные scopes; честно: changelog 03.08.2026 детально описывает Drive/Gmail/Calendar; Sheets/Docs могли исчезнуть из витрины 04.08 — проверять на дату статьи, fallback = Path B.
7. **Проверить подключение** — перезапуск Cursor; Customize → MCPs → зелёный статус; Output → **MCP Logs**; `sheets_check_access` (Path B) или «прочитай A1:C5 листа Реестр».
8. **Рабочий сценарий** — DoD: metadata → найти строку по `doc_key` → `sheets_update_values` / `sheets_append_values` только в status/comment → `sheets_get_values` → сверка; human approval на каждый write-tool.
9. **Эксплуатация** — allowlist write-tools; ротация ключа (B93); при >80–100 заявок/мес или audit — n8n/ERP, Sheets = staging; соседние реестры B51/B58/B83.

**Workflow:**  
`Реестр в Sheets → (SA share | OAuth plugin) → MCP в Cursor → Agent read/update по doc_key → перечитка → регламент CFO`

---

## Яндекс Wordstat (MCP user-mcp-kv)

⚠️ **WORDSTAT UNAVAILABLE:** сервер MCP `user-mcp-kv` / инструмент `wordstat_get_top_requests` в этой Cloud-сессии **не подключён** (в каталоге dynamic tools: `cursor`, `Cursor Automation Tools`, `cursor-cloud`, `cursor-subscriptions`). Точные показы/мес **не получены** и **не выдуманы**.

Если позже появится токен Wordstat: https://oauth.yandex.ru/authorize?response_type=token&client_id=c654b948515a4a07a4c89648a0831d40

### Таблица спроса (Wordstat)

| Фраза | Показы в месяц |
| --- | --- |
| mcp google sheets cursor | *не получено — MCP недоступен* |
| cursor mcp | *не получено* |
| mcp сервер для cursor | *не получено* |
| google sheets mcp | *не получено* |
| подключить mcp cursor | *не получено* |
| автоматизация финотдела | *не получено* |

**Экспертная семантика (LSI для writer, без цифр спроса):**

| Кластер | Фразы | Роль |
| --- | --- | --- |
| Primary | mcp google sheets cursor, google sheets mcp cursor | H1, title |
| Setup | mcp.json cursor, cursor marketplace google sheets, mcp-gsheets service account | H2 пошагово |
| Finance | автоматизация финотдела google sheets, реестр договоров cursor, править реестр без копипаста | угол КОДА |
| Registry | реестр upd google sheets, реестр saas, doc_key find update | кейсы |
| Security | service account json не в git, обезличивание sheets, oauth scopes минимум | FAQ |
| Ops | sheets_check_access, mcp logs cursor, unauthorized google mcp | troubleshooting |
| Adjacent | cursor google workspace plugins 2026, mcp cursor finansist | interlink B21 |

**SEO-вывод:** SERP по `mcp google sheets cursor` — EN community MCP (freema, xing5, we2go) + новости Cursor Workspace (авг 2026) + RU каталоги MCP. Почти нет RU how-to «финансист + реестр + Cursor без копипаста». Угол КОДА: правка управленческих реестров через MCP, Path B = production, Path A = пилот с оговоркой про витрину.

---

## SERP (WebSearch Cursor, 30.08.2026)

Приоритет — живой WebSearch; `research-serp.json` шаг 0 — черновик URL (query `2026 2026` нерелевантен).

### Primary: `mcp google sheets cursor` / `MCP Google Sheets Cursor 2026`

| # | URL | Тип | Пробел для КОДА |
| --- | --- | --- | --- |
| 1 | https://cursor.com/help/customization/mcp | Офиц. MCP help | Нет Sheets/реестров |
| 2 | https://cursor.com/docs/mcp | Офиц. reference | Общий протокол |
| 3 | https://github.com/freema/mcp-gsheets | Community MCP (SA, write) | EN; не CFO |
| 4 | https://github.com/xing5/mcp-google-sheets | uvx + SA/OAuth | Dev setup |
| 5 | https://github.com/mariadb-RupeshBiswas/google-sheets-mcp | Read-only ADC | Нет write для реестра |
| 6 | https://mcp-catalog.ru/tutorials/gsheets-cursor | RU: freema → Cursor | Нет finance angle |
| 7 | https://mcp-catalog.ru/tutorials/google-sheets-cursor | RU: henilcalagiya | Каталог |
| 8 | https://pastesheet.com/guides/google-sheets-mcp-cursor | Hosted URL MCP | Публичные листы |
| 9 | https://zenn.dev/icare/articles/15fe5e2ab5930c | JP how-to mcp-google-sheets | Не RU, не финансы |
| 10 | https://www.strac.io/blog/google-sheets-mcp-server | Security/DLP angle | Enterprise EN |

### News / Workspace (август 2026)

| # | URL | Тип | Пробел |
| --- | --- | --- | --- |
| 1 | https://cursor.com/changelog/google-workspace-plugins | Changelog 03.08.2026 | Drive/Gmail/Calendar; Sheets **не** в списке плагинов changelog |
| 2 | https://vibecoding.ru/news/2026/08/03/cursor-google-workspace-plugins | RU: 5→3 плагинов | Docs/Sheets убраны 04.08; OAuth `cursor://` bug |
| 3 | https://mayai.ru/cursor-otkryl-gmail-i-sheets-agentam/ | RU разбор | Контент-завод; мало SA |
| 4 | https://aiinsiders.net/article/cursor-plugins-let-coding-agents-write-to-gmail-docs-sheets | EN news 05.08 | Маркетинг «5 сервисов» vs факт витрины |
| 5 | https://indieseek.co/blogs/cursor-google-workspace-plugins-security-checklist/ | Security checklist | Фокус Gmail/Drive/Calendar |
| 6 | https://www.explainx.ai/blog/cursor-google-workspace-plugins-gmail-drive-calendar-august-2026 | EN gap-анализ | Sheets в changelog не детализирован |

### Secondary: `автоматизация финотдела` / реестры

| # | URL | Тип | Пробел |
| --- | --- | --- | --- |
| 1 | https://koda-fd.ru/blog/ai-dlya-finansista-2026/ | Hub КОДА | Нет MCP Cursor |
| 2 | https://dzen.ru/a/anRW32ni3D3wHjQF | Реестр договоров Sheets | Без MCP |
| 3 | https://dzen.ru/a/aoAx4V_t_ztBh5aj | Заявки Forms→Sheets | Без MCP |
| 4 | https://datalopata.ru/blog/avtomatizatsija-finansov-sistemnyj-podhod-k-uchetu-v-2026-godu/ | Приоритеты 2026 | ERP-уклон |
| 5 | https://neurinix.com/2026/06/21/podklyuchenie-mcp-cursor/ | Общий MCP RU | Не Sheets |
| 6 | https://vibecoderz.ru/blog/kak-podklyuchit-mcp-server-k-cursor-i-claude | mcp.json RU | Не finance |

### Конкурентный зазор (угол КОДА)

1. **Finance-first** — «перестань копировать реестр в чат: agent правит строку по `doc_key`».
2. **Два пути** — OAuth-плагин для пилота vs SA+mcp-gsheets для production (honest note: Sheets мог исчезнуть из Marketplace 04.08.2026).
3. **Связка с реестрами** — B51/B58/B83; MCP = слой правок поверх готовой таблицы.
4. **Security** — минимальный share, ключ вне git, approval tools, indirect prompt injection, обезличивание.
5. **Verify loop** — после write всегда `get_values`; Connected ≠ authorized.
6. **Fork от B82** — B82 = скрипт; B92 = Agent+MCP без кода.

---

## Таблица фактов

| # | Утверждение | Источник | Дата проверки |
| --- | --- | --- | --- |
| 1 | MCP подключает Cursor к внешним tools; Agent вызывает их в чате. | https://cursor.com/help/customization/mcp | 2026-08-30 |
| 2 | Конфиг: `.cursor/mcp.json` (проект) + `~/.cursor/mcp.json` (глобальный); при совпадении имени побеждает **проектный**. | https://cursor.com/help/customization/mcp | 2026-08-30 |
| 3 | Локальный MCP: `command`/`args`/`env`; удалённый — `url` (+ `headers`). После правки `mcp.json` — **перезапуск Cursor**. | https://cursor.com/help/customization/mcp | 2026-08-30 |
| 4 | One-click: Customize → MCPs → Add to Cursor (+ OAuth при необходимости). | https://cursor.com/help/customization/mcp | 2026-08-30 |
| 5 | По умолчанию Agent **спрашивает approval** перед MCP-tool; с Cursor 3.6+ — Auto-review / allowlist / `permissions.json`. | https://cursor.com/help/customization/mcp | 2026-08-30 |
| 6 | Troubleshooting: Output → **MCP Logs** (`Ctrl+Shift+U` / `Cmd+Shift+U`). | https://cursor.com/help/customization/mcp | 2026-08-30 |
| 7 | Cloud Agents поддерживают MCP из dashboard; Team — shared servers / Team Marketplace. | https://cursor.com/help/customization/mcp | 2026-08-30 |
| 8 | Changelog 03.08.2026: плагины **Google Drive, Gmail, Google Calendar** (read/write/act без выхода из Cursor); установка из Marketplace или Customize. | https://cursor.com/changelog/google-workspace-plugins | 2026-08-30 |
| 9 | В официальном changelog Sheets/Docs **не перечислены** среди установленных плагинов (только Drive/Gmail/Calendar). | https://cursor.com/changelog/google-workspace-plugins | 2026-08-30 |
| 10 | По vibecoding.ru: анонс 03.08 упоминал Docs+Sheets; 04.08 Docs/Sheets/Slides убраны из витрины; остались Gmail, Drive, Calendar; мин. Cursor **3.13.0**. | https://vibecoding.ru/news/2026/08/03/cursor-google-workspace-plugins | 2026-08-30 |
| 11 | OAuth-баг: Google не принимает callback `cursor://` → 400; обход — войти на cursor.com/agents (MCP Servers) или Local callback. | https://vibecoding.ru/news/2026/08/03/cursor-google-workspace-plugins | 2026-08-30 |
| 12 | Официальные Google Workspace MCP — **Developer Preview** (раздача через программу разработчиков). | https://vibecoding.ru/news/2026/08/03/cursor-google-workspace-plugins | 2026-08-30 |
| 13 | `freema/mcp-gsheets`: Node.js **v20+**, GCP + Sheets API + SA JSON; Cursor: `npx -y mcp-gsheets@latest` + `GOOGLE_APPLICATION_CREDENTIALS` / `GOOGLE_PRIVATE_KEY`+`GOOGLE_CLIENT_EMAIL`. | https://github.com/freema/mcp-gsheets | 2026-08-30 |
| 14 | Tools для реестра: `sheets_get_values`, `sheets_update_values`, `sheets_append_values`, `sheets_batch_get_values`, `sheets_get_metadata`, `sheets_check_access`. | https://github.com/freema/mcp-gsheets | 2026-08-30 |
| 15 | `sheets_append_values`: default `insertDataOption` = **OVERWRITE** — для реестра явно `INSERT_ROWS`, если нужно сдвигать строки. | https://github.com/freema/mcp-gsheets | 2026-08-30 |
| 16 | Перед операциями рекомендуется `sheets_check_access`. | https://github.com/freema/mcp-gsheets | 2026-08-30 |
| 17 | SA видит **только** таблицы, расшаренные на `client_email`; IAM Cloud ≠ Share файла. | https://developers.google.com/workspace/guides/create-credentials#service-account | 2026-08-30 |
| 18 | Scope `https://www.googleapis.com/auth/spreadsheets` — read/write расшаренных таблиц на уровне **файла**. | https://developers.google.com/workspace/sheets/api/scopes | 2026-08-30 |
| 19 | Квоты Sheets API: **300** read и **300** write req/min на проект; **60**/min на user; превышение → HTTP **429**; batch = 1 запрос. | https://developers.google.com/workspace/sheets/api/limits | 2026-08-30 |
| 20 | Позже в 2026 превышение квот Sheets API планируется тарифицировать (Google Workspace standardized model). | https://developers.google.com/workspace/sheets/api/limits | 2026-08-30 |
| 21 | Риск MCP+Google: агент наследует права; возможна **indirect prompt injection** из писем/ячеек — HITL на write. | https://mayai.ru/cursor-otkryl-gmail-i-sheets-agentam/ ; https://indieseek.co/blogs/cursor-google-workspace-plugins-security-checklist/ | 2026-08-30 |
| 22 | «Connected» в Tools & MCP **не гарантирует** рабочий Google OAuth — проверять живым read/write. | https://mayai.ru/cursor-otkryl-gmail-i-sheets-agentam/ | 2026-08-30 |
| 23 | Реестр договоров в Sheets уместен до **200–300** активных договоров при одном владельце; иначе CLM/1С. | https://dzen.ru/a/anRW32ni3D3wHjQF | 2026-08-30 |
| 24 | Заявки Forms→Sheets: при **>80–100**/мес — staging перед ERP/n8n. | https://dzen.ru/a/aoAx4V_t_ztBh5aj | 2026-08-30 |
| 25 | Pattern update 2026: find-by-stable-id → update else append (избегает дублей). | https://stepper.io/blog/google-sheet-update/ | 2026-08-30 |

**Не выдумывать:** показы Wordstat; «Sheets-плагин всегда в Marketplace»; SA = доступ ко всему Drive; цифры Smithery installs; «без программиста» для Path B без GCP/SA.

**fact-bank.md:** прямых фактов MCP+Sheets нет — опираться на таблицу выше. ROI контент-завода из fact-bank **не тянуть**.

---

## Структура H2 для writer (карточка B92)

1. Когда это нужно финотделу (и когда нет)  
2. Подготовка данных и безопасность (без сырых ПДн в облако)  
3. Пошаговая настройка / скрипт / сценарий  
4. Проверка результата и типичные ошибки  
5. Что автоматизировать дальше  

**Пример mcp.json (Path B):**

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

**Тестовый промпт агента:**

> Подключись к таблице `{SPREADSHEET_ID}`. На листе `Реестр` найди строку, где `doc_key` = `DOG-2026-014`. Прочитай `status` и `comment`. Если `status` ≠ «Оплачен», предложи «На согласовании» и дату в `comment`. После write перечитай строку и покажи diff.

---

## FAQ-кандидаты

- **Без программиста?** — Path A: да для пилота (если плагин в витрине); Path B: по инструкции + Cursor с JSON; ~1–2 ч первый реестр.
- **Сколько внедрение?** — SA + mcp.json + тестовый update: **~1–2 ч**.
- **Риски данных?** — OAuth = права Google-аккаунта; SA-ключ = все расшаренные файлы; не класть ПДн; подтверждать write; injection из ячеек.
- **OAuth или SA?** — OAuth = личный пилот; SA = командный реестр, минимальный blast radius, Cloud Agents.
- **Vs B82?** — B82 = скрипт пишет в staging; B92 = Agent правит через MCP.
- **Cloud Agents?** — локальный OAuth не переезжает автоматически; использовать SA / dashboard MCP.

---

## CTA / interlink

- Internal: `/avtomatizaciya-finansov-no-code/`, `/obezlichivanie-dannyh-chatgpt-finansist/`, `/google-sheets-api-integraciya-finotdel/` (B82), `/mcp-cursor-finansist-instrumenty/` (B21)
- Соседние: B51, B58, B83, B93
- CTA: `https://club.koda-fd.ru/?utm_source=blog&utm_medium=article&utm_campaign=mcp-google-sheets-cursor-reestry` (≤2), `https://t.me/finance_modern?utm_source=blog&utm_medium=article` (≤2)

---

## Handoff marker

`=== EXCALIBUR BLOG RESEARCH ===` — см. `.cursor/excalibur-blog-handoff.md`
