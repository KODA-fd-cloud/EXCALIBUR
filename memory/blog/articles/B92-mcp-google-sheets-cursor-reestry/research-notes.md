# Research notes — B92

**topic_id:** B92  
**slug:** mcp-google-sheets-cursor-reestry  
**h1:** Как подключить MCP к Google Sheets в Cursor и править реестры без копипаста  
**research_date:** 2026-08-24  
**publish_target:** koda-fd.ru/blog  
**utility_gate:** PASS (`how_to`, mode B)  
**author_id:** olga-kondratskaya  
**related_internal:** `/avtomatizaciya-finansov-no-code/`, `/obezlichivanie-dannyh-chatgpt-finansist/`  
**sibling_queue:** B82 (Sheets API + SA), B21 (MCP в Cursor общий), B51/B58/B83 (реестры в Sheets)  
**cover_scene_hint:** abstract holographic finance automation dark #0a0a0f purple #8b5cf6, no text

---

## utility_verdict

**PASS** — тема utility-only how_to. Читатель получает два рабочих маршрута подключения Google Sheets к Cursor через MCP (официальный плагин из Marketplace **или** community-сервер `mcp-gsheets` на service account), подготовку реестра под агентные правки, тестовый сценарий «найти строку → обновить статус → перечитать», чеклист безопасности для финданных и troubleshooting. Не новость «Cursor открыл Workspace», не обзор 25 MCP-серверов, не туториал «напиши свой MCP с нуля».

---

## reader_outcome

После гайда финансист сможет подключить MCP Google Sheets в Cursor, дать агенту доступ только к рабочему реестру (через service account или OAuth-плагин), попросить обновить статус строки или дописать поля без копирования таблицы в чат и проверить результат перечиткой диапазона через MCP-tool.

---

## action_outline

1. **Решить, нужен ли MCP Sheets** — реестр уже в Google Sheets (договоры, УПД, SaaS, заявки на расход), правки повторяются, устали таскать диапазоны в чат; **не** делать, если нужен жёсткий audit trail / сотни таблиц с enterprise ACL — тогда 1С/CLM, Sheets только staging.
2. **Выбрать путь подключения** — **Path A (быстрый):** плагин `google-sheets` из Cursor Marketplace / Customize → OAuth личного Google (удобно для пилота); **Path B (финконтур):** `freema/mcp-gsheets` + service account — расшарить только нужные реестры, ключ в `env`, без доступа агента ко всему Drive (см. B82, B93).
3. **Подготовить реестр** — одна строка = одна сущность; стабильный `doc_key`; лист `staging` для импорта; в облако без сырых ПДн (ИНН/сумма/статус — да; паспорт, полные ФИО — нет); interlink `/obezlichivanie-dannyh-chatgpt-finansist/`.
4. **Path B: Google Cloud + SA** — проект → включить **Google Sheets API** → service account → JSON-ключ → скопировать `client_email` → «Поделиться» на файл реестра с ролью **Редактор** (без «Уведомить»).
5. **Path B: mcp.json в Cursor** — глобально `~/.cursor/mcp.json` или проектно `.cursor/mcp.json`; блок `mcp-gsheets` с `npx -y mcp-gsheets@latest` и `GOOGLE_APPLICATION_CREDENTIALS` (абсолютный путь); JSON-ключ **не** в git.
6. **Path A: Marketplace** — Customize → MCPs → `google-sheets` → Add → OAuth; минимальные scopes; учесть, что в changelog 03.08.2026 детально описаны Drive/Gmail/Calendar, а Sheets/Docs — в анонсе X, но часть плагинов могла временно исчезнуть из витрины (см. факты ниже).
7. **Проверить подключение** — перезапуск Cursor; Customize → MCPs → зелёный статус; Output → **MCP Logs**; tool `sheets_check_access` (Path B) или живой запрос «прочитай A1:C5 листа Реестр».
8. **Рабочий сценарий реестра** — промпт с DoD: `sheets_get_metadata` → найти строку по `doc_key` → `sheets_update_values` / `sheets_append_values` только в колонки статуса/комментария → `sheets_get_values` на ту же строку → сверка с ожиданием; human approval на каждый write-tool.
9. **Эксплуатация и рост** — allowlist write-tools; ротация ключа SA (B93); при >80–100 заявок/мес или audit — n8n/ERP, Sheets остаётся staging; соседние реестры B51/B58/B83.

**Workflow для статьи:**  
`Реестр в Sheets → (SA share | OAuth plugin) → MCP в Cursor → Agent read/update по doc_key → перечитка диапазона → регламент CFO`

---

## Яндекс Wordstat (MCP user-mcp-kv)

⚠️ **WORDSTAT AUTH WARNING:** сервер MCP `user-mcp-kv` в этой Cloud-сессии **не подключён** (в каталоге dynamic tools доступны только `cursor`, `cursor-cloud`, `cursor-subscriptions`). Вызов `wordstat_get_top_requests` **не выполнен**. Точные показы/мес **не получены** и **не выдуманы**.

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
| Ops | sheets_check_access, mcp logs cursor, unauthorized google mcp | troubleshooting |
| Adjacent | cursor google workspace plugins 2026, mcp cursor finansist | interlink B21 |

**SEO-вывод:** SERP по `mcp google sheets cursor` — **EN-гайды по community MCP** (freema, we2go, spreadsheet-mcp) и **новости Cursor + Google Workspace (август 2026)**. Почти нет RU how-to «финансист + реестр + Cursor». Угол КОДА: **правка управленческих реестров через MCP без копипаста**, с веткой SA для безопасности и явным сравнением с B82 (скрипт) и B21 (общий MCP).

---

## SERP (WebSearch Cursor, 24.08.2026)

Приоритет — живой WebSearch; `research-serp.json` (шаг 0) полезен как URL-черновик; query `2026 2026` и часть сниппетов **нерелевантны** — не копировать.

### Primary: `mcp google sheets cursor 2026`

| # | URL | Тип | Пробел для КОДА |
| --- | --- | --- | --- |
| 1 | https://cursor.com/docs/mcp | Официальный reference | Нет реестров финотдела |
| 2 | https://cursor.com/help/customization/mcp | Help: mcp.json, OAuth, approvals | Канон шагов; нет Sheets-кейса |
| 3 | https://github.com/freema/mcp-gsheets | Community MCP (SA) | EN; dev-фокус, не CFO |
| 4 | https://github.com/we2go/google-mcp | npx wizard OAuth/SA | Sheets+Docs; не реестры |
| 5 | https://github.com/dudegladiator/spreadsheet-mcp | Python/uv, 27 tools | Установка для dev |
| 6 | https://skiln.co/blog/google-sheets-mcp-review-2026 | Обзор ecosystem | Маркетинг Smithery; не finance |
| 7 | https://dev.to/pastesheet/google-sheets-in-vs-code-cursor-and-windsurf-over-mcp-5467 | Hosted URL MCP | Публичные листы; не SA |
| 8 | https://composio.dev/toolkits/googlesheets/framework/cursor | Composio OAuth | SaaS-посредник |

### News / official Workspace (август 2026)

| # | URL | Тип | Пробел |
| --- | --- | --- | --- |
| 1 | https://cursor.com/changelog/google-workspace-plugins | Changelog 03.08.2026 | Drive/Gmail/Calendar детально; Sheets в теле changelog **не расписан** |
| 2 | https://mayai.ru/cursor-otkryl-gmail-i-sheets-agentam/ | RU разбор релиза | Контент-завод; мало SA/реестров |
| 3 | https://vibecoding.ru/news/2026/08/03/cursor-google-workspace-plugins | RU новость | Баг OAuth `cursor://`; Sheets убрали из витрины 04.08 |
| 4 | https://explainx.ai/blog/cursor-google-workspace-plugins-gmail-drive-calendar-august-2026 | EN анализ | Gap официальной доки по Sheets |
| 5 | https://github.com/cursor/plugins | Official plugins repo | google-drive в third_party; отдельного google-sheets в README таблице нет |

### Secondary: `автоматизация финотдела Google Sheets реестры 2026`

| # | URL | Тип | Пробел |
| --- | --- | --- | --- |
| 1 | https://koda-fd.ru/blog/ai-dlya-finansista-2026/ | Hub КОДА | Нет MCP Cursor |
| 2 | https://dzen.ru/a/anRW32ni3D3wHjQF | Реестр договоров Sheets | Без MCP |
| 3 | https://dzen.ru/a/aoAqyl_t_ztBh3s7 | Реестр УПД Sheets | Без MCP |
| 4 | https://datalopata.ru/blog/avtomatizatsija-finansov-sistemnyj-podhod-k-uchetu-v-2026-godu/ | Приоритеты автоматизации | ERP-уклон |
| 5 | https://znaj.org/ru/6-luchshikh-reshenii-2026-goda-avtomatizacii-upravleniya-finansami/ | Обзор решений 2026 | Не Cursor |

### H1-aligned

| # | URL | Заметка |
| --- | --- | --- |
| 1 | https://mcp-catalog.ru/tutorials/gsheets-cursor | RU: freema/mcp-gsheets в Cursor |
| 2 | https://mcp-catalog.ru/tutorials/google-sheets-cursor | RU: henilcalagiya variant |
| 3 | https://neurinix.com/2026/06/21/podklyuchenie-mcp-cursor/ | Общий MCP setup RU |
| 4 | https://khar-ag.ru/docs/cursor-mcp-guide/ | mcp.json RU |

### Конкурентный зазор (угол КОДА)

1. **Finance-first** — не «подключи Sheets к Cursor», а «перестань копировать реестр в чат: agent правит строку по `doc_key`».
2. **Два пути с выбором** — OAuth-плагин для пилота vs SA+mcp-gsheets для production финконтура (с honest note про статус Marketplace Sheets в августе 2026).
3. **Связка с реестрами серии** — договоры (B51), УПД (B58), SaaS (B83); MCP = слой правок поверх уже спроектированной таблицы.
4. **Security block** — минимальный share, ключ вне git, approval tools, indirect prompt injection (Google/MCP), обезличивание.
5. **Verify loop** — после write всегда `get_values`; «Connected ≠ authorized» (форум/mayai).
6. **Fork от B82** — B82 = свой Python-скрипт; B92 = те же SA+share, но правки через Agent+MCP без написания кода.

---

## Таблица фактов

| # | Утверждение | Источник | Дата |
| --- | --- | --- | --- |
| 1 | MCP (Model Context Protocol) подключает Cursor к внешним инструментам; Agent вызывает tools в чате. | https://cursor.com/help/customization/mcp | 2026-08-24 |
| 2 | Конфиг MCP: проектный `.cursor/mcp.json` + глобальный `~/.cursor/mcp.json`; при совпадении имени побеждает **проектный**. | https://cursor.com/help/customization/mcp | 2026-08-24 |
| 3 | Локальный MCP: `command`, `args`, `env`; удалённый — поле `url` (+ опционально `headers`). | https://cursor.com/help/customization/mcp | 2026-08-24 |
| 4 | One-click: Customize → MCPs → Add to Cursor; после ручного `mcp.json` — **перезапуск Cursor**. | https://cursor.com/help/customization/mcp | 2026-08-24 |
| 5 | По умолчанию Agent **запрашивает approval** перед MCP-tool; с Cursor 3.6+ — Auto-review / allowlist. | https://cursor.com/help/customization/mcp | 2026-08-24 |
| 6 | Troubleshooting: Output → **MCP Logs** (`Ctrl+Shift+U` / `Cmd+Shift+U`). | https://cursor.com/help/customization/mcp | 2026-08-24 |
| 7 | 03.08.2026 Cursor анонсировал Google Workspace plugins: агенты читают/пишут Drive, Gmail, Calendar **без выхода из редактора**; установка из Marketplace или Customize. | https://cursor.com/changelog/google-workspace-plugins | 2026-08-24 |
| 8 | В changelog 03.08.2026 перечислены возможности **Drive, Gmail, Calendar**; Sheets/Docs в этом документе **не детализированы** (хотя в анонсе X упоминаются Docs и Sheets). | https://cursor.com/changelog/google-workspace-plugins ; https://explainx.ai/blog/cursor-google-workspace-plugins-gmail-drive-calendar-august-2026 | 2026-08-24 |
| 9 | По отчёту vibecoding.ru (04.08.2026): из пяти обещанных Workspace-плагинов в витрине остались **Gmail, Drive, Calendar**; Docs/Sheets/Slides временно убраны; мин. версия Cursor **3.13.0**; OAuth-bug с callback `cursor://` (обход через cursor.com/agents). | https://vibecoding.ru/news/2026/08/03/cursor-google-workspace-plugins | 2026-08-24 |
| 10 | Официальные Workspace MCP Google — **Developer Preview**; доступ через программу разработчиков. | https://vibecoding.ru/news/2026/08/03/cursor-google-workspace-plugins | 2026-08-24 |
| 11 | `freema/mcp-gsheets`: Node.js **v20+**, Google Cloud project, Sheets API, service account JSON; установка в Cursor через `npx -y mcp-gsheets@latest` + env `GOOGLE_APPLICATION_CREDENTIALS`. | https://github.com/freema/mcp-gsheets | 2026-08-24 |
| 12 | Ключевые tools mcp-gsheets для реестра: `sheets_get_values`, `sheets_update_values`, `sheets_append_values`, `sheets_batch_get_values`, `sheets_get_metadata`, `sheets_check_access`. | https://github.com/freema/mcp-gsheets | 2026-08-24 |
| 13 | `sheets_append_values`: по умолчанию `insertDataOption` = **OVERWRITE** — для реестра явно указывать `INSERT_ROWS`, если нужно сдвигать строки. | https://github.com/freema/mcp-gsheets | 2026-08-24 |
| 14 | Service account видит **только** таблицы, расшаренные на `client_email` из JSON; IAM-роли Cloud **не заменяют** Share файла. | https://developers.google.com/workspace/guides/create-credentials#service-account | 2026-08-24 |
| 15 | Scope `https://www.googleapis.com/auth/spreadsheets` — read/write всех расшаренных таблиц SA; применяется ко **всему файлу**; листы защищают ProtectedRange. | https://developers.google.com/workspace/sheets/api/scopes | 2026-08-24 |
| 16 | Квота Sheets API write: **300 запросов/мин** на проект; превышение → HTTP **429**; batch считается одним запросом. | https://developers.google.com/workspace/sheets/api/limits | 2026-08-24 |
| 17 | `we2go/google-mcp`: `npx google-mcp init` — wizard SA или OAuth; tools `sheets_read_range`, `sheets_update_range`, `sheets_append_row`. | https://github.com/we2go/google-mcp | 2026-08-24 |
| 18 | `dudegladiator/spreadsheet-mcp`: **27 tools**, auth через service-account JSON в `credentials/`. | https://github.com/dudegladiator/spreadsheet-mcp | 2026-08-24 |
| 19 | Hosted MCP (PasteSheet): подключение по `url` в `mcp.json`; без GCP/OAuth для публичных листов; приватные endpoints — платный план от **$9/mo**. | https://dev.to/pastesheet/google-sheets-in-vs-code-cursor-and-windsurf-over-mcp-5467 | 2026-08-24 |
| 20 | Риск MCP+Google: агент наследует права пользователя; в письмах/документах возможна **indirect prompt injection** — нужен human-in-the-loop на write/send. | https://mayai.ru/cursor-otkryl-gmail-i-sheets-agentam/ | 2026-08-24 |
| 21 | «Connected» в Tools & MCP **не гарантирует** успешный Google OAuth — проверять живым read/write запросом. | https://mayai.ru/cursor-otkryl-gmail-i-sheets-agentam/ | 2026-08-24 |
| 22 | Cloud Agents **не наследуют** интерактивный Google OAuth с локального Cursor — для облака нужен отдельный коннектор/SA. | https://mayai.ru/cursor-otkryl-gmail-i-sheets-agentam/ | 2026-08-24 |
| 23 | Реестр договоров в Sheets уместен до **200–300** активных договоров при одном владельце таблицы; иначе CLM/1С. | https://dzen.ru/a/anRW32ni3D3wHjQF | 2026-08-24 |
| 24 | Заявки на расход через Forms→Sheets: при **>80–100** заявок/мес Sheets — staging перед ERP/n8n. | https://dzen.ru/a/aoAx4V_t_ztBh5aj | 2026-08-24 |
| 25 | В 2026 финотдел автоматизирует в первую очередь классификацию платежей, сверки, управленческую отчётность — Sheets+MCP подходит как **transport правок**, не GL. | https://koda-fd.ru/blog/ai-dlya-finansista-2026/ | 2026-08-24 |

**Не выдумывать:** показы Wordstat; «Sheets-плагин всегда в Marketplace» (проверять на дату публикации); что SA = доступ ко всему Drive; цифру Smithery «56k installs» как верифицированный факт (только как оценка стороннего обзора skiln.co); обещание «без программиста» для Path B без упоминания GCP/SA.

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

- **Можно ли без программиста?** — Path A (Marketplace+OAuth): да для пилота; Path B (SA+mcp.json): по инструкции B82/B92, Cursor поможет с JSON; production — 1–2 ч первый реестр.
- **Сколько займёт внедрение?** — SA + mcp.json + один тестовый update: **~1–2 ч**; OAuth-плагин быстрее, если доступен в витрине.
- **Какие риски для данных?** — OAuth = права вашего Google; SA-ключ = все расшаренные файлы; не класть ПДн; подтверждать write-tools; indirect injection из писем/ячеек.
- **OAuth или service account?** — OAuth для личного пилота; SA для командного реестра, cron, минимального blast radius.
- **Чем отличается от B82?** — B82 = Python/Node скрипт пишет в staging; B92 = Agent в Cursor правит через MCP без скрипта.
- **Работает ли в Cloud Agents?** — локальный OAuth не переезжает автоматически; проверять отдельно или использовать SA.

---

## CTA / interlink

- Internal: `/avtomatizaciya-finansov-no-code/`, `/obezlichivanie-dannyh-chatgpt-finansist/`, `/google-sheets-api-integraciya-finotdel/` (B82), `/mcp-cursor-finansist-instrumenty/` (B21)
- Соседние реестры: B51, B58, B83
- CTA: `https://club.koda-fd.ru/?utm_source=blog&utm_medium=article&utm_campaign=mcp-google-sheets-cursor-reestry` (≤2), `https://t.me/finance_modern?utm_source=blog&utm_medium=article` (≤2)

---

## Handoff marker

`=== EXCALIBUR BLOG RESEARCH ===` — см. `.cursor/excalibur-blog-handoff.md`
