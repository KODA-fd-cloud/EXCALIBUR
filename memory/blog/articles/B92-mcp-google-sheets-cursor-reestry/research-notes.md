# Research notes — B92

**topic_id:** B92  
**slug:** mcp-google-sheets-cursor-reestry  
**h1:** Как подключить MCP к Google Sheets в Cursor и править реестры без копипаста  
**research_date:** 2026-09-07  
**publish_target:** koda-fd.ru/blog  
**utility_gate:** PASS (`how_to`, mode B) — подтверждено `excalibur_blog_utility_gate.py --topic-id B92`  
**author_id:** olga-kondratskaya  
**related_internal:** `/avtomatizaciya-finansov-no-code/`, `/obezlichivanie-dannyh-chatgpt-finansist/`  
**sibling_queue:** B82 (Sheets API + SA), B21 (MCP в Cursor общий), B51/B58/B83 (реестры в Sheets)  
**cover_scene_hint:** abstract holographic finance automation dark #0a0a0f purple #8b5cf6, no text  
**freshness_window:** prefer sources after 2026-06-09; verify versions on 2026-09-07

---

## utility_verdict

**PASS** — тема utility-only how_to. Читатель получает рабочие маршруты подключения Google Sheets к Cursor через MCP (community `freema/mcp-gsheets` + service account как основной production-путь для финконтура; опционально Marketplace/OAuth-плагин или Google remote MCP `sheetsmcp.googleapis.com`), подготовку реестра под агентные правки, тестовый сценарий «найти строку → обновить статус → перечитать», чеклист безопасности и troubleshooting. Не новость «Cursor открыл Workspace», не обзор 25 MCP-серверов, не туториал «напиши свой MCP с нуля».

---

## reader_outcome

После гайда финансист сможет подключить MCP Google Sheets в Cursor, дать агенту доступ только к рабочему реестру (через service account или OAuth), попросить обновить статус строки / дописать поля без копирования таблицы в чат и проверить результат перечиткой диапазона через MCP-tool.

---

## action_outline

1. **Решить, нужен ли MCP Sheets** — реестр уже в Google Sheets (договоры, УПД, SaaS, заявки на расход), правки повторяются, устали таскать диапазоны в чат; **не** делать, если нужен жёсткий audit trail / сотни таблиц с enterprise ACL — тогда 1С/CLM, Sheets только staging.
2. **Проверить доступность Cursor** — с ~04.09.2026 у части пользователей из РФ ошибка «not available in your region» (см. факты); статья предполагает рабочий Cursor (корпоративный доступ / допустимая юрисдикция). Без Cursor — Path B SA+`mcp-gsheets` переносится на другой MCP-клиент; обход региональных блокировок в статье **не** описывать.
3. **Выбрать путь подключения** — **Path B (финконтур, рекомендовать):** `freema/mcp-gsheets` + service account — расшарить только нужные реестры, ключ в `env`, без доступа агента ко всему Drive (B82, B93). **Path A (пилот):** плагин/MCP `google-sheets` из Marketplace / Customize → OAuth (если доступен; OAuth `cursor://` часто ломается — auth через cursor.com/agents). **Path C (advanced):** Google remote MCP `https://sheetsmcp.googleapis.com/mcp/v1` по доке Google Developers (OAuth client в GCP).
4. **Подготовить реестр** — одна строка = одна сущность; стабильный `doc_key`; лист `staging` для импорта; в облако без сырых ПДн (ИНН/сумма/статус — да; паспорт, полные ФИО — нет); interlink `/obezlichivanie-dannyh-chatgpt-finansist/`.
5. **Path B: Google Cloud + SA** — проект → включить **Google Sheets API** → service account → JSON-ключ → скопировать `client_email` → «Поделиться» на файл реестра с ролью **Редактор** (без «Уведомить»).
6. **Path B: mcp.json в Cursor** — глобально `~/.cursor/mcp.json` или проектно `.cursor/mcp.json`; блок `mcp-gsheets` с `npx -y mcp-gsheets@latest` и `GOOGLE_APPLICATION_CREDENTIALS` (абсолютный путь); JSON-ключ **не** в git.
7. **Проверить подключение** — перезапуск Cursor; Customize → MCPs → зелёный статус; Output → **MCP Logs**; tool `sheets_check_access` (Path B) или живой запрос «прочитай A1:C5 листа Реестр».
8. **Рабочий сценарий реестра** — промпт с DoD: `sheets_get_metadata` → найти строку по `doc_key` → `sheets_update_values` / `sheets_append_values` только в колонки статуса/комментария → `sheets_get_values` на ту же строку → сверка; human approval на каждый write-tool; учесть квоту **60 req/min per user** у SA.
9. **Эксплуатация и рост** — allowlist write-tools; ротация ключа SA (B93); при >80–100 заявок/мес или audit — n8n/ERP, Sheets остаётся staging; соседние реестры B51/B58/B83.

**Workflow для статьи:**  
`Реестр в Sheets → (SA share | OAuth plugin | Google remote MCP) → MCP в Cursor → Agent read/update по doc_key → перечитка диапазона → регламент CFO`

---

## Яндекс Wordstat (MCP user-mcp-kv)

⚠️ **WORDSTAT AUTH WARNING:** сервер MCP `user-mcp-kv` в этой Cloud-сессии **не подключён** (в каталоге dynamic tools доступны только `Cursor Automation Tools`, `cursor`, `cursor-cloud`, `cursor-subscriptions`). Вызов `wordstat_get_top_requests` **не выполнен**. Точные показы/мес **не получены** и **не выдуманы**.

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
| Official | sheetsmcp.googleapis.com, google workspace mcp sheets | Path C / FAQ |
| Finance | автоматизация финотдела google sheets, реестр договоров cursor, править реестр без копипаста | угол КОДА |
| Registry | реестр upd google sheets, реестр saas подписок, doc_key find update | кейсы |
| Security | service account json не в git, обезличивание sheets, oauth scopes минимум, prompt injection | FAQ |
| Ops | sheets_check_access, mcp logs cursor, 429 quota per user, unauthorized google mcp | troubleshooting |
| Access caveat | cursor not available in your region, cursor россия сентябрь 2026 | lead/disclaimer (без инструкций обхода) |
| Adjacent | cursor google workspace plugins 2026, mcp cursor finansist | interlink B21 |

**SEO-вывод:** SERP по `mcp google sheets cursor` (WebSearch 07.09.2026) — EN/каталоги community MCP (freema, henilcalagiya, PasteSheet, akchro), обзоры security (strac.io), новости Workspace-плагинов августа 2026 и региональных ограничений Cursor начала сентября. Почти нет RU how-to «финансист + реестр + Cursor + SA». Угол КОДА: **правка управленческих реестров через MCP без копипаста**, Path B как default для финконтура, honest note про статус Marketplace Sheets и доступность Cursor.

---

## SERP (WebSearch Cursor, 07.09.2026)

Приоритет — живой WebSearch; `research-serp.json` (шаг 0, 2026-09-07) использован как URL-черновик. Query `2026 2026` и календарные сниппеты **нерелевантны** — игнорировать.

### Primary: `mcp google sheets cursor 2026`

| # | URL | Тип | Пробел для КОДА |
| --- | --- | --- | --- |
| 1 | https://cursor.com/docs/mcp | Официальный reference | Нет реестров финотдела |
| 2 | https://cursor.com/help/customization/mcp | Help: mcp.json, OAuth, approvals, Cloud Agents MCP | Канон шагов; нет Sheets-кейса |
| 3 | https://github.com/freema/mcp-gsheets | Community MCP (SA), Node 20+ | EN; dev-фокус, не CFO |
| 4 | https://mcpservers.org/servers/freema/mcp-gsheets | Каталог + config | Дубль freema |
| 5 | https://mcp-catalog.ru/tutorials/gsheets-cursor | RU install freema | Нет finance/реестров |
| 6 | https://mcp-catalog.ru/tutorials/google-sheets-cursor | RU: henilcalagiya | Install-only |
| 7 | https://pastesheet.com/guides/google-sheets-mcp-cursor | Hosted URL MCP | Публичные листы; не SA |
| 8 | https://www.strac.io/blog/google-sheets-mcp-server | Security/DLP angle 2026 | Не finance registry |
| 9 | https://llmversus.com/mcp/google-sheets-mcp | npm `mcp-google-sheets` setup | Dev install |
| 10 | https://skiln.co/blog/google-sheets-mcp-review-2026 | Ecosystem review | Маркетинг; не CFO |

### Official Workspace / Google MCP

| # | URL | Тип | Пробел |
| --- | --- | --- | --- |
| 1 | https://cursor.com/changelog/google-workspace-plugins | Changelog 03.08.2026 | В тексте только Drive/Gmail/Calendar |
| 2 | https://developers.google.com/workspace/guides/configure-mcp-servers | Official remote MCP | Sheets URL `sheetsmcp.googleapis.com/mcp/v1`; клиенты Antigravity/Claude; Cursor в «Others» |
| 3 | https://mayai.ru/cursor-otkryl-gmail-i-sheets-agentam/ | RU разбор релиза | Контент-завод; мало SA/реестров |
| 4 | https://vibecoding.ru/news/2026/08/03/cursor-google-workspace-plugins | RU новость | Docs/Sheets временно убирали из витрины; OAuth `cursor://` |
| 5 | https://forum.cursor.com/t/google-workspace-plugins-oauth-fails-error-400-invalid-request-on-cursor-redirect/167402 | Bug report | Workaround: auth на cursor.com/agents |
| 6 | https://forum.cursor.com/t/google-plugins-broken-auth-2-0/167780 | Staff confirm | Known OAuth issue Aug 2026 |

### Access / region (контекст РФ, сентябрь 2026)

| # | URL | Тип | Заметка |
| --- | --- | --- | --- |
| 1 | https://habr.com/ru/articles/1078814/ | Habr | С ~04.09.2026 у РФ-пользователей ломаются agent/autocomplete; ToS export controls 03.09 |
| 2 | https://vc.ru/ai/3122016-cursor-zablokiroval-polzovateley-iz-rossii | VC | Ошибка «Cursor is not available in your region» |

Writer: **короткий disclaimer** в lead/FAQ; не превращать статью в новость про блокировку; **не** давать инструкции обхода.

### Secondary: `автоматизация финотдела` / реестры Sheets

| # | URL | Тип | Пробел |
| --- | --- | --- | --- |
| 1 | https://koda-fd.ru/blog/ai-dlya-finansista-2026/ | Hub КОДА | Нет MCP Cursor |
| 2 | https://koda-fd.ru/blog/mcp-cursor-finansist-instrumenty/ | B21 | Общий MCP, не Sheets registry |
| 3 | https://dzen.ru/a/aoAx4V_t_ztBh5aj | Forms→Sheets заявки | Без MCP; порог 80–100/мес |
| 4 | https://datalopata.ru/blog/avtomatizatsija-finansov-sistemnyj-podhod-k-uchetu-v-2026-godu/ | Приоритеты автоматизации | ERP-уклон |
| 5 | https://developers.google.com/workspace/sheets/api/limits | Quotas | 300/min project, 60/min user |

### Конкурентный зазор (угол КОДА)

1. **Finance-first** — не «подключи Sheets к Cursor», а «перестань копировать реестр в чат: agent правит строку по `doc_key`».
2. **Path B default** — SA+`mcp-gsheets` для production финконтура; Path A/C как опции с честным статусом Marketplace/OAuth.
3. **Связка с реестрами серии** — договоры (B51), УПД (B58), SaaS (B83); MCP = слой правок поверх уже спроектированной таблицы.
4. **Security block** — минимальный share, ключ вне git, approval tools, indirect prompt injection (Google MCP docs + mayai), обезличивание.
5. **Verify loop** — после write всегда `get_values`; «Connected ≠ authorized»; квота 60/min на SA.
6. **Fork от B82** — B82 = свой Python-скрипт; B92 = те же SA+share, но правки через Agent+MCP без написания кода.
7. **Access caveat** — актуальность Cursor для РФ на дату публикации; без howto обхода.

---

## Таблица фактов

| # | Утверждение | Источник | Дата проверки |
| --- | --- | --- | --- |
| 1 | MCP подключает Cursor к внешним инструментам; Agent вызывает tools в чате. | https://cursor.com/help/customization/mcp | 2026-09-07 |
| 2 | Конфиг MCP: проектный `.cursor/mcp.json` + глобальный `~/.cursor/mcp.json`; при совпадении имени побеждает **проектный**. | https://cursor.com/help/customization/mcp | 2026-09-07 |
| 3 | Локальный MCP: `command`, `args`, `env`; удалённый — поле `url` (+ опционально `headers`). | https://cursor.com/help/customization/mcp | 2026-09-07 |
| 4 | One-click: Customize → MCPs → Add to Cursor; после ручного `mcp.json` — **перезапуск Cursor**. | https://cursor.com/help/customization/mcp | 2026-09-07 |
| 5 | По умолчанию Agent **запрашивает approval** перед MCP-tool; с Cursor 3.6+ — Auto-review / allowlist (`permissions.json`). | https://cursor.com/help/customization/mcp | 2026-09-07 |
| 6 | Troubleshooting: Output → **MCP Logs** (`Ctrl+Shift+U` / `Cmd+Shift+U`). | https://cursor.com/help/customization/mcp | 2026-09-07 |
| 7 | Cloud Agents поддерживают MCP из Cloud Agents dashboard; Team — shared servers в Integrations & MCP. | https://cursor.com/help/customization/mcp | 2026-09-07 |
| 8 | 03.08.2026 Cursor changelog: плагины **Drive, Gmail, Calendar** из Marketplace/Customize; Sheets в теле changelog **не детализирован**. | https://cursor.com/changelog/google-workspace-plugins | 2026-09-07 |
| 9 | Google предоставляет remote MCP для Sheets: `https://sheetsmcp.googleapis.com/mcp/v1` (нужны Sheets API + Sheets MCP API в GCP, OAuth). | https://developers.google.com/workspace/guides/configure-mcp-servers | 2026-09-07 |
| 10 | Google прямо предупреждает про **indirect prompt injection** при MCP + Workspace (письма/доки/ячейки с скрытыми инструкциями). | https://developers.google.com/workspace/guides/configure-mcp-servers | 2026-09-07 |
| 11 | Форум Cursor: OAuth Workspace-плагинов падает с Error 400 на `cursor://…/oauth/callback`; workaround — Login на https://cursor.com/agents (Cloud) или Local auth path. | https://forum.cursor.com/t/google-workspace-plugins-oauth-fails-error-400-invalid-request-on-cursor-redirect/167402 | 2026-09-07 |
| 12 | Staff Cursor (deanrie): проблема OAuth IDE→Google known; auth с dashboard с https-callback. | https://forum.cursor.com/t/google-plugins-broken-auth-2-0/167780 | 2026-09-07 |
| 13 | `freema/mcp-gsheets`: Node.js **v20+**, Sheets API, service account JSON; Cursor: `npx -y mcp-gsheets@latest` + `GOOGLE_APPLICATION_CREDENTIALS` / `GOOGLE_PROJECT_ID`. | https://github.com/freema/mcp-gsheets | 2026-09-07 |
| 14 | Ключевые tools для реестра: `sheets_get_values`, `sheets_update_values`, `sheets_append_values`, `sheets_batch_get_values`, `sheets_get_metadata`, `sheets_check_access`. | https://github.com/freema/mcp-gsheets | 2026-09-07 |
| 15 | `sheets_append_values`: default `insertDataOption` = **OVERWRITE** — для реестра явно `INSERT_ROWS`, если нужно сдвигать строки. | https://github.com/freema/mcp-gsheets | 2026-09-07 |
| 16 | Service account видит **только** таблицы, расшаренные на `client_email`; IAM Cloud **не заменяет** Share файла. | https://developers.google.com/workspace/guides/create-credentials#service-account | 2026-09-07 |
| 17 | Scope `https://www.googleapis.com/auth/spreadsheets` — read/write расшаренных таблиц; применяется ко **всему файлу**; листы — ProtectedRange. | https://developers.google.com/workspace/sheets/api/scopes | 2026-09-07 |
| 18 | Квоты Sheets API: **300** read/write req/min на проект и **60** req/min **на user** на проект; превышение → HTTP **429**; refill каждую минуту. | https://developers.google.com/workspace/sheets/api/limits | 2026-09-07 |
| 19 | Один service account = один «user» для квоты 60/min — агент с несколькими tool-calls легко упирается в per-user лимит раньше project-лимита. | https://dev.to/pastesheet/google-sheets-api-rate-limits-what-60-requestsminute-actually-means-1mim ; https://developers.google.com/workspace/sheets/api/limits | 2026-09-07 |
| 20 | Later in 2026 Google планирует биллинг за overage сверх стандартных квот Workspace API (нужен Cloud billing) — не обещать «Sheets API навсегда бесплатно без оговорок». | https://developers.google.com/workspace/sheets/api/limits | 2026-09-07 |
| 21 | Hosted MCP PasteSheet: `url` в mcp.json; публичные листы без GCP; private endpoints — paid от **$9/mo**. | https://dev.to/pastesheet/google-sheets-in-vs-code-cursor-and-windsurf-over-mcp-5467 | 2026-09-07 |
| 22 | Риск MCP+Google: агент наследует права пользователя; нужен human-in-the-loop на write. | https://mayai.ru/cursor-otkryl-gmail-i-sheets-agentam/ ; Google MCP guide | 2026-09-07 |
| 23 | «Connected» в Tools & MCP **не гарантирует** успешный Google OAuth — проверять живым read/write. | https://mayai.ru/cursor-otkryl-gmail-i-sheets-agentam/ | 2026-09-07 |
| 24 | С ~04.09.2026 у пользователей из РФ массово перестают работать agent/autocomplete Cursor; в ответах встречается «not available in your region»; ToS обновлены 03.09.2026 (export controls). Официального пресс-релиза Anysphere нет. | https://habr.com/ru/articles/1078814/ ; https://vc.ru/ai/3122016-cursor-zablokiroval-polzovateley-iz-rossii | 2026-09-07 |
| 25 | Заявки на расход Forms→Sheets: при **>80–100** заявок/мес Sheets — staging перед ERP/n8n. | https://dzen.ru/a/aoAx4V_t_ztBh5aj | 2026-09-07 |
| 26 | В 2026 финотдел автоматизирует в первую очередь классификацию платежей, сверки, управленческую отчётность — Sheets+MCP = **transport правок**, не GL. | https://koda-fd.ru/blog/ai-dlya-finansista-2026/ | 2026-09-07 |

**Не выдумывать:** показы Wordstat; «Sheets-плагин всегда в Marketplace»; что SA = доступ ко всему Drive; цифры installs Smithery как факт; обещание «без программиста» для Path B без GCP/SA; инструкции обхода региональной блокировки Cursor; утверждение, что Google remote MCP «официально one-click в Cursor Marketplace» (дока Google ориентирована на Antigravity/Claude; Cursor — generic remote MCP).

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

- **Можно ли без программиста?** — Path A (Marketplace+OAuth): да для пилота, если плагин/auth доступны; Path B (SA+mcp.json): по инструкции B82/B92, Cursor поможет с JSON; production — 1–2 ч первый реестр.
- **Сколько займёт внедрение?** — SA + mcp.json + один тестовый update: **~1–2 ч**; OAuth-плагин быстрее, если auth проходит.
- **Какие риски для данных?** — OAuth = права вашего Google; SA-ключ = все расшаренные файлы; не класть ПДн; подтверждать write-tools; indirect injection из писем/ячеек.
- **OAuth или service account?** — OAuth для личного пилота; SA для командного реестра, cron, минимального blast radius.
- **Чем отличается от B82?** — B82 = Python/Node скрипт пишет в staging; B92 = Agent в Cursor правит через MCP без скрипта.
- **Работает ли в Cloud Agents?** — да, если MCP настроен в Cloud Agents dashboard; локальный IDE OAuth не переезжает автоматически.
- **Cursor недоступен в регионе?** — проверить ошибку region; статья про MCP-паттерн; обход блокировок не описываем; Path B переносим на другой MCP-клиент при необходимости.

---

## CTA / interlink

- Internal: `/avtomatizaciya-finansov-no-code/`, `/obezlichivanie-dannyh-chatgpt-finansist/`, `/google-sheets-api-integraciya-finotdel/` (B82), `/mcp-cursor-finansist-instrumenty/` (B21)
- Соседние реестры: B51, B58, B83
- CTA: `https://club.koda-fd.ru/?utm_source=blog&utm_medium=article&utm_campaign=mcp-google-sheets-cursor-reestry` (≤2), `https://t.me/finance_modern?utm_source=blog&utm_medium=article` (≤2)

---

## Handoff marker

`=== EXCALIBUR BLOG RESEARCH ===` — см. `.cursor/excalibur-blog-handoff.md`
