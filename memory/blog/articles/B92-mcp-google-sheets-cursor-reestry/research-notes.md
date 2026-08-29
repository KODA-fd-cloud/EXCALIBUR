# Research notes — B92

**topic_id:** B92  
**slug:** mcp-google-sheets-cursor-reestry  
**h1:** Как подключить MCP к Google Sheets в Cursor и править реестры без копипаста  
**research_date:** 2026-08-29  
**publish_target:** koda-fd.ru/blog  
**utility_gate:** PASS (`how_to`, mode B) — подтверждено `excalibur_blog_utility_gate.py --topic-id B92`  
**author_id:** olga-kondratskaya  
**related_internal:** `/avtomatizaciya-finansov-no-code/`, `/obezlichivanie-dannyh-chatgpt-finansist/`  
**sibling_queue:** B82 (Sheets API + SA), B21 (MCP в Cursor общий), B51/B58/B83 (реестры в Sheets)  
**cover_scene_hint:** abstract holographic finance automation dark #0a0a0f purple #8b5cf6, no text  
**freshness:** prefer sources after 2026-05-31; versions/facts verified 2026-08-29

---

## utility_verdict

**PASS** — тема utility-only how_to. Читатель получает два рабочих маршрута подключения Google Sheets к Cursor через MCP (официальный/Marketplace-плагин **или** community-сервер `freema/mcp-gsheets` на service account), подготовку реестра под агентные правки, тестовый сценарий «найти строку → обновить статус → перечитать», чеклист безопасности для финданных и troubleshooting. Не новость «Cursor открыл Workspace», не обзор 25 MCP-серверов, не туториал «напиши свой MCP с нуля».

---

## reader_outcome

После гайда финансист сможет подключить MCP Google Sheets в Cursor, дать агенту доступ только к рабочему реестру (через service account или OAuth-плагин), попросить обновить статус строки или дописать поля без копирования таблицы в чат и проверить результат перечиткой диапазона через MCP-tool.

---

## action_outline

1. **Решить, нужен ли MCP Sheets** — реестр уже в Google Sheets (договоры, УПД, SaaS, заявки на расход), правки повторяются, устали таскать диапазоны в чат; **не** делать, если нужен жёсткий audit trail / сотни таблиц с enterprise ACL — тогда 1С/CLM, Sheets только staging.
2. **Выбрать путь подключения** — **Path A (быстрый пилот):** плагин Google Sheets / Workspace из Cursor Marketplace → Customize → OAuth личного Google (удобно для пилота; на 29.08.2026 в официальном changelog детально только Drive/Gmail/Calendar — Sheets мог временно пропасть из витрины, см. факты); **Path B (финконтур):** `freema/mcp-gsheets` + service account — расшарить только нужные реестры, ключ в `env`, без доступа агента ко всему Drive (см. B82, B93).
3. **Подготовить реестр** — одна строка = одна сущность; стабильный `doc_key`; лист `staging` для импорта; в облако без сырых ПДн (ИНН/сумма/статус — да; паспорт, полные ФИО — нет); interlink `/obezlichivanie-dannyh-chatgpt-finansist/`.
4. **Path B: Google Cloud + SA** — проект → включить **Google Sheets API** → service account → JSON-ключ → скопировать `client_email` → «Поделиться» на файл реестра с ролью **Редактор** (без «Уведомить»).
5. **Path B: mcp.json в Cursor** — глобально `~/.cursor/mcp.json` или проектно `.cursor/mcp.json`; блок `mcp-gsheets` с `npx -y mcp-gsheets@latest` и `GOOGLE_APPLICATION_CREDENTIALS` (абсолютный путь); JSON-ключ **не** в git.
6. **Path A: Marketplace** — Customize → MCPs → искать `google-sheets` / Workspace → Add → OAuth; минимальные scopes; если карточки Sheets нет — не ждать новости, идти Path B.
7. **Проверить подключение** — перезапуск Cursor; Customize → MCPs → зелёный статус; Output → **MCP Logs**; tool `sheets_check_access` (Path B) или живой запрос «прочитай A1:C5 листа Реестр» (Connected ≠ authorized).
8. **Рабочий сценарий реестра** — промпт с DoD: `sheets_get_metadata` → найти строку по `doc_key` → `sheets_update_values` / `sheets_append_values` только в колонки статуса/комментария → `sheets_get_values` на ту же строку → сверка с ожиданием; human approval на каждый write-tool.
9. **Эксплуатация и рост** — allowlist write-tools; ротация ключа SA (B93); при >80–100 заявок/мес или audit — n8n/ERP, Sheets остаётся staging; соседние реестры B51/B58/B83.

**Workflow для статьи:**  
`Реестр в Sheets → (SA share | OAuth plugin) → MCP в Cursor → Agent read/update по doc_key → перечитка диапазона → регламент CFO`

---

## Яндекс Wordstat (MCP user-mcp-kv)

⚠️ **WORDSTAT UNAVAILABLE:** сервер MCP `user-mcp-kv` / инструмент `wordstat_get_top_requests` в этой Cloud-сессии **не подключён** (в каталоге dynamic tools: `cursor`, `Cursor Automation Tools`, `cursor-cloud`, `cursor-subscriptions` — namespace `user-mcp-kv` отсутствует). Вызов **не выполнен**. Точные показы/мес **не получены** и **не выдуманы**.

Обновление токена / подключение MCP-KV (на случай 401 при появлении сервера): https://oauth.yandex.ru/authorize?response_type=token&client_id=c654b948515a4a07a4c89648a0831d40

### Таблица спроса (Wordstat)

| Фраза | Показы в месяц |
| --- | --- |
| mcp google sheets cursor | *не получено — WORDSTAT UNAVAILABLE* |
| cursor mcp | *не получено — WORDSTAT UNAVAILABLE* |
| mcp сервер для cursor | *не получено — WORDSTAT UNAVAILABLE* |
| автоматизация финотдела | *не получено — WORDSTAT UNAVAILABLE* |
| google sheets mcp | *не получено — WORDSTAT UNAVAILABLE* |
| подключить mcp cursor | *не получено — WORDSTAT UNAVAILABLE* |
| mcp-gsheets | *не получено — WORDSTAT UNAVAILABLE* |

**Экспертная семантика (LSI для writer, без цифр спроса):**

| Кластер | Фразы | Роль |
| --- | --- | --- |
| Primary | mcp google sheets cursor, google sheets mcp cursor | H1, title |
| Setup | mcp.json cursor, cursor marketplace google sheets, mcp-gsheets service account | H2 пошагово |
| Finance | автоматизация финотдела google sheets, реестр договоров cursor, править реестр без копипаста | угол КОДА |
| Registry | реестр upd google sheets, реестр saas подписок, doc_key find update | кейсы |
| Security | service account json не в git, обезличивание sheets, oauth scopes минимум | FAQ |
| Ops | sheets_check_access, mcp logs cursor, unauthorized google mcp | troubleshooting |
| Adjacent | cursor google workspace plugins 2026, mcp cursor finansist | interlink B21 |
| Vendors (не продвигать как must) | composio googlesheets cursor, pastesheet mcp, merge agent handler sheets | упомянуть как альтернативы Path A/B |

**SEO-вывод (29.08.2026):** SERP по `mcp google sheets cursor` — **EN-гайды** (Composio, Merge, freema/mcp-gsheets, PasteSheet, yardobr/mcp-google-sheets) + **новости Cursor + Google Workspace (03–05.08.2026)** + RU-каталоги MCP. Почти нет RU how-to «финансист + реестр + Cursor без копипаста». Угол КОДА: **правка управленческих реестров через MCP**, ветка SA для безопасности, сравнение с B82 (скрипт) и B21 (общий MCP).

---

## SERP (WebSearch Cursor + research-serp.json, 29.08.2026)

Приоритет — живой **WebSearch** Курсора (29.08.2026). `research-serp.json` обновлён тем же днём — использован как URL-черновик. Query `2026 2026` и календарные сниппеты **нерелевантны** — игнорировать.

### Primary: `mcp google sheets cursor 2026` (WebSearch)

| # | URL | Тип | Пробел для КОДА |
| --- | --- | --- | --- |
| 1 | https://composio.dev/toolkits/googlesheets/framework/cursor | Hosted MCP + OAuth (Composio) | Dev/SaaS; не реестры финотдела, не SA |
| 2 | https://www.merge.dev/blog/google-sheets-mcp-cursor | Merge Agent Handler CLI → Cursor | 4 шага для разработчиков API |
| 3 | https://llmversus.com/mcp/google-sheets-mcp | Install guide `mcp-google-sheets` npx | EN setup, не finance |
| 4 | https://github.com/yardobr/mcp-google-sheets | Python MCP Drive+Sheets, SA/OAuth | Альтернатива Path B; не CFO |
| 5 | https://github.com/freema/mcp-gsheets | Community MCP (npm `mcp-gsheets`) | Канон Path B; EN README |
| 6 | https://mcpcursor.com/server/google-sheets-mcp | Каталог MCP для Cursor | Карточка/агрегатор |
| 7 | https://pastesheet.com/guides/google-sheets-mcp-cursor | Hosted URL MCP | Публичные/платные листы |
| 8 | https://www.strac.io/blog/google-sheets-mcp-server | Security/DLP setup 2026 | Фокус Claude+DLP, не реестры |

### Official docs / MCP setup

| # | URL | Тип | Пробел |
| --- | --- | --- | --- |
| 1 | https://cursor.com/help/customization/mcp | Help: mcp.json, OAuth, approvals, MCP Logs | Канон шагов; нет Sheets-кейса |
| 2 | https://cursor.com/docs/mcp | Reference MCP | Нет реестров |
| 3 | https://cursor.com/ru/help/customization/mcp | RU help MCP | То же |

### News / Workspace (август 2026)

| # | URL | Тип | Пробел |
| --- | --- | --- | --- |
| 1 | https://cursor.com/changelog/google-workspace-plugins | Changelog **03.08.2026** | В теле: только **Drive, Gmail, Calendar**; Sheets/Docs **не расписаны** |
| 2 | https://vibecoding.ru/news/2026/08/03/cursor-google-workspace-plugins | RU: из 5 плагинов через день 3 | Docs/Sheets убрали 04.08; OAuth `cursor://`; мин. Cursor **3.13.0** |
| 3 | https://mayai.ru/cursor-otkryl-gmail-i-sheets-agentam/ | RU разбор 04.08.2026 | Connected≠authorized; prompt injection; Cloud OAuth |
| 4 | https://www.explainx.ai/blog/cursor-google-workspace-plugins-gmail-drive-calendar-august-2026 | EN анализ gap доки | Sheets в анонсе X vs changelog |
| 5 | https://ai-watch-blog.vercel.app/en/posts/2026-08-03-cursor-google-workspace-plugins/ | Сводка анонса | Вторичный; сверять с changelog |

### Secondary: автоматизация финотдела / реестры

| # | URL | Тип | Пробел |
| --- | --- | --- | --- |
| 1 | https://koda-fd.ru/blog/ai-dlya-finansista-2026/ | Hub КОДА | Нет MCP Cursor |
| 2 | https://datalopata.ru/blog/avtomatizatsija-finansov-sistemnyj-podhod-k-uchetu-v-2026-godu/ | Приоритеты автомат. 2026 | ERP-уклон |
| 3 | https://znaj.org/ru/6-luchshikh-reshenii-2026-goda-avtomatizacii-upravleniya-finansami/ | Обзор решений | Не Cursor |
| 4 | https://dzen.ru/a/anRW32ni3D3wHjQF | Реестр договоров Sheets | Без MCP (из prior research) |

### H1-aligned (RU how-to)

| # | URL | Заметка |
| --- | --- | --- |
| 1 | https://mcp-catalog.ru/tutorials/gsheets-cursor | RU: freema/mcp-gsheets в Cursor |
| 2 | https://mcp-catalog.ru/tutorials/google-sheets-cursor | RU: henilcalagiya variant |
| 3 | https://neurinix.com/2026/06/21/podklyuchenie-mcp-cursor/ | Общий MCP setup RU |
| 4 | https://khar-ag.ru/docs/cursor-mcp-guide/ | mcp.json RU |
| 5 | https://shtruzel.ru/articles/mcp-v-cursor-podklyuchenie-i-luchshie-servery-2026 | MCP Cursor 3.1 топ-серверы |

### Конкурентный зазор (угол КОДА) — актуально 29.08.2026

1. **Finance-first** — не «подключи Sheets к Cursor», а «перестань копировать реестр в чат: agent правит строку по `doc_key`».
2. **Два пути с честным статусом Marketplace** — OAuth-плагин для пилота (если Sheets в витрине) vs **SA+mcp-gsheets как надёжный Path B** (changelog официально детализирует только Drive/Gmail/Calendar).
3. **Не путать вендоров** — Composio/Merge/PasteSheet/Quadratic — посредники; для финконтура КОДА рекомендует self-hosted SA, не чужой SaaS-прокси.
4. **Связка с реестрами серии** — договоры (B51), УПД (B58), SaaS (B83); MCP = слой правок поверх таблицы.
5. **Security** — минимальный share, ключ вне git, approval tools, indirect prompt injection, обезличивание.
6. **Verify loop** — после write всегда `get_values`; «Connected ≠ authorized».
7. **Fork от B82** — B82 = Python-скрипт; B92 = Agent+MCP без кода.
8. **Cloud Agents** — в help обновлено: MCP через Dashboard; локальный Google OAuth всё равно не переезжает автоматически (mayai) — для облака SA/team MCP.

---

## Таблица фактов

| # | Утверждение | Источник | Дата проверки |
| --- | --- | --- | --- |
| 1 | MCP подключает Cursor к внешним инструментам; Agent вызывает tools в чате. | https://cursor.com/help/customization/mcp | 2026-08-29 |
| 2 | Конфиг: проектный `.cursor/mcp.json` + глобальный `~/.cursor/mcp.json`; при совпадении имени побеждает **проектный**. | https://cursor.com/help/customization/mcp | 2026-08-29 |
| 3 | Локальный MCP: `command`, `args`, `env`; удалённый — поле `url` (+ опционально `headers`). | https://cursor.com/help/customization/mcp | 2026-08-29 |
| 4 | One-click: Customize → MCPs → Add to Cursor; после ручного `mcp.json` — **перезапуск Cursor**. | https://cursor.com/help/customization/mcp | 2026-08-29 |
| 5 | По умолчанию Agent **запрашивает approval** перед MCP-tool; с Cursor 3.6+ — Auto-review / allowlist / `permissions.json`. | https://cursor.com/help/customization/mcp | 2026-08-29 |
| 6 | Troubleshooting: Output → **MCP Logs** (`Ctrl+Shift+U` / `Cmd+Shift+U`). | https://cursor.com/help/customization/mcp | 2026-08-29 |
| 7 | Cloud Agents поддерживают MCP, настроенные в Cloud Agents dashboard; Team: Dashboard → Integrations & MCP. | https://cursor.com/help/customization/mcp | 2026-08-29 |
| 8 | Changelog **03.08.2026**: плагины Google Workspace — в теле документа детально **Drive, Gmail, Calendar**; установка из Marketplace / Customize. | https://cursor.com/changelog/google-workspace-plugins | 2026-08-29 |
| 9 | Sheets/Docs в теле официального changelog **не перечислены** (хотя в анонсе X/медиа упоминаются). | https://cursor.com/changelog/google-workspace-plugins ; https://vibecoding.ru/news/2026/08/03/cursor-google-workspace-plugins | 2026-08-29 |
| 10 | vibecoding.ru (04.08.2026): из пяти обещанных плагинов в витрине остались **Gmail, Drive, Calendar**; Docs/Sheets временно убраны; мин. версия Cursor **3.13.0**; OAuth-bug callback `cursor://` (обход через cursor.com/agents). | https://vibecoding.ru/news/2026/08/03/cursor-google-workspace-plugins | 2026-08-29 |
| 11 | Официальные MCP Google Workspace — **Developer Preview**; доступ через программу разработчиков Google. | https://vibecoding.ru/news/2026/08/03/cursor-google-workspace-plugins | 2026-08-29 |
| 12 | Google документирует квоты **Sheets MCP server** (`sheetsmcp.googleapis.com`): read/write **300/мин на проект**, **60/мин на user/project**; tools: `get_values`, `update_values` и др. | https://developers.google.com/workspace/sheets/api/limits | 2026-08-29 |
| 13 | `freema/mcp-gsheets`: Node.js **v20+**, Sheets API, service account JSON; `npx -y mcp-gsheets@latest` + `GOOGLE_APPLICATION_CREDENTIALS` / `GOOGLE_PROJECT_ID`. | https://github.com/freema/mcp-gsheets | 2026-08-29 |
| 14 | npm-пакет `mcp-gsheets` (версия **1.10.2** на npm; обновлён **2026-08-16**); ~**4700** weekly downloads (npm, на дату проверки). | https://www.npmjs.com/package/mcp-gsheets | 2026-08-29 |
| 15 | Ключевые tools mcp-gsheets для реестра: `sheets_get_values`, `sheets_update_values`, `sheets_append_values`, `sheets_batch_get_values`, `sheets_get_metadata`, `sheets_check_access`. | https://github.com/freema/mcp-gsheets | 2026-08-29 |
| 16 | `sheets_append_values`: default `insertDataOption` = **OVERWRITE** — для реестра явно указывать `INSERT_ROWS`, если нужно сдвигать строки. | https://github.com/freema/mcp-gsheets | 2026-08-29 |
| 17 | SA видит **только** таблицы, расшаренные на `client_email` из JSON; IAM Cloud **не заменяет** Share файла. | https://github.com/freema/mcp-gsheets (Share step) ; https://developers.google.com/workspace/guides/create-credentials#service-account | 2026-08-29 |
| 18 | Квота Sheets API write/read: **300 запросов/мин** на проект; превышение → HTTP **429**; batch = один запрос. | https://developers.google.com/workspace/sheets/api/limits | 2026-08-29 |
| 19 | Pricing note Google: превышение quota limits **планируется тарифицироваться later in 2026** (Workspace standardized model) — не утверждать текущую цену. | https://developers.google.com/workspace/sheets/api/limits | 2026-08-29 |
| 20 | Риск MCP+Google: агент наследует права пользователя; в письмах/ячейках возможна **indirect prompt injection** — human-in-the-loop на write. | https://mayai.ru/cursor-otkryl-gmail-i-sheets-agentam/ | 2026-08-29 |
| 21 | «Connected» в Tools & MCP **не гарантирует** успешный Google OAuth — проверять живым read/write. | https://mayai.ru/cursor-otkryl-gmail-i-sheets-agentam/ | 2026-08-29 |
| 22 | Локальный интерактивный Google OAuth **не переезжает** на Cloud Agents автоматически — нужен коннектор/SA/team MCP. | https://mayai.ru/cursor-otkryl-gmail-i-sheets-agentam/ ; https://cursor.com/help/customization/mcp | 2026-08-29 |
| 23 | Google **не** шипит first-party public Sheets MCP для всех клиентов «из коробки» в смысле community-каталогов; community/self-hosted или вендоры (Quadratic и др.). | https://www.quadratichq.com/ai/mcp/google-sheets | 2026-08-29 |
| 24 | Реестр договоров в Sheets уместен до **200–300** активных договоров при одном владельце; иначе CLM/1С. | https://dzen.ru/a/anRW32ni3D3wHjQF | 2026-08-24 (prior; не перепроверять цифру без перечитывания) |
| 25 | Заявки на расход Forms→Sheets: при **>80–100** заявок/мес Sheets — staging перед ERP/n8n. | https://dzen.ru/a/aoAx4V_t_ztBh5aj | 2026-08-24 (prior) |
| 26 | В 2026 финотдел автоматизирует классификацию платежей, сверки, УО — Sheets+MCP = **transport правок**, не GL. | https://koda-fd.ru/blog/ai-dlya-finansista-2026/ | 2026-08-29 |

**Не выдумывать:** показы Wordstat; «Sheets-плагин всегда в Marketplace» (проверять на дату публикации); что SA = доступ ко всему Drive; цифры Smithery installs; обещание «без программиста» для Path B без GCP/SA; текущую платную цену Sheets API quota (только «planned later in 2026»).

**fact-bank.md:** прямых фактов про MCP+Sheets нет — опираться на таблицу выше. ROI контент-завода из fact-bank **не тянуть**.

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

## FAQ-кандидаты

- **Можно ли без программиста?** — Path A (Marketplace+OAuth): да для пилота, если Sheets в витрине; Path B (SA+mcp.json): по инструкции, Cursor поможет с JSON; production — 1–2 ч первый реестр.
- **Сколько займёт внедрение?** — SA + mcp.json + один тестовый update: **~1–2 ч**; OAuth-плагин быстрее, если доступен.
- **Какие риски для данных?** — OAuth = права вашего Google; SA-ключ = все расшаренные файлы; не класть ПДн; подтверждать write-tools; indirect injection.
- **OAuth или service account?** — OAuth для личного пилота; SA для командного реестра и минимального blast radius.
- **Чем отличается от B82?** — B82 = скрипт пишет в staging; B92 = Agent правит через MCP без скрипта.
- **Работает ли в Cloud Agents?** — MCP через Dashboard/Team Integrations; локальный Google OAuth не переносится сам — проверять отдельно или SA.
- **Почему нет Sheets в changelog?** — 03.08 анонс Workspace; в changelog детально Drive/Gmail/Calendar; Sheets мог уйти из витрины 04.08 — Path B надёжнее для продакшена.

---

## CTA / interlink

- Internal: `/avtomatizaciya-finansov-no-code/`, `/obezlichivanie-dannyh-chatgpt-finansist/`, `/google-sheets-api-integraciya-finotdel/` (B82), `/mcp-cursor-finansist-instrumenty/` (B21)
- Соседние реестры: B51, B58, B83
- CTA: `https://club.koda-fd.ru/?utm_source=blog&utm_medium=article&utm_campaign=mcp-google-sheets-cursor-reestry` (≤2), `https://t.me/finance_modern?utm_source=blog&utm_medium=article` (≤2)

---

## Handoff marker

`=== EXCALIBUR BLOG RESEARCH ===` — см. `.cursor/excalibur-blog-handoff.md`
