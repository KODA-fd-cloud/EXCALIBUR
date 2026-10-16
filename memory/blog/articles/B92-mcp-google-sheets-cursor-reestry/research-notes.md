# Research notes — B92

**topic_id:** B92  
**slug:** mcp-google-sheets-cursor-reestry  
**h1:** Как подключить MCP к Google Sheets в Cursor и править реестры без копипаста  
**research_date:** 2026-08-24  
**freshness_window:** prefer_sources_after_2026-08-01  
**publish_target:** koda-fd.ru/blog  
**utility_gate:** PASS (`how_to`, mode B) — подтверждено `python3 scripts/excalibur_blog_utility_gate.py --topic-id B92`  
**author_id:** olga-kondratskaya  
**related_internal:** `/avtomatizaciya-finansov-no-code/`, `/obezlichivanie-dannyh-chatgpt-finansist/`  
**sibling_queue:** B82 (Sheets API + SA), B21 (MCP в Cursor общий), B51/B58/B83 (реестры в Sheets), B93 (ротация SA)  
**cover_scene_hint:** abstract holographic finance automation dark #0a0a0f purple #8b5cf6, no text

---

## utility_verdict

**PASS** — тема utility-only how_to. Читатель получает рабочий маршрут: подключить Google Sheets к Cursor через MCP (официальный Workspace-плагин **или** community `freema/mcp-gsheets` + service account), подготовить реестр под агентные правки, прогнать сценарий «найти строку по `doc_key` → обновить статус → перечитать», чеклист безопасности и troubleshooting (OAuth `cursor://`, Connected ≠ authorized). Не новость «Cursor открыл Workspace», не обзор 25 MCP-серверов, не «напиши MCP с нуля».

---

## reader_outcome

После гайда финансист сможет подключить MCP Google Sheets в Cursor, дать агенту доступ только к рабочему реестру (OAuth-плагин для пилота **или** service account для финконтура), попросить обновить статус строки / дописать поля без копирования таблицы в чат и проверить результат перечиткой диапазона через MCP-tool.

---

## action_outline

1. **Решить, нужен ли MCP Sheets** — реестр уже в Google Sheets (договоры, УПД, SaaS, заявки), правки повторяются, устали таскать диапазоны в чат; **не** делать, если нужен жёсткий audit trail / сотни таблиц с enterprise ACL — тогда 1С/CLM, Sheets только staging.
2. **Выбрать путь** — **Path A (пилот):** плагин Google Sheets из Cursor Marketplace / Customize → OAuth (если карточка доступна; на 24.08.2026 URL Marketplace Sheets даёт 404, а Cloud OAuth часто ломается на `cursor://` — см. факты); **Path B (финконтур):** `freema/mcp-gsheets` + service account — расшарить только нужные реестры, ключ в `env`, без доступа агента ко всему Drive (связка с B82/B93).
3. **Подготовить реестр** — одна строка = одна сущность; стабильный `doc_key`; лист `staging` для импорта; в облако без сырых ПДн (ИНН/сумма/статус — да; паспорт, полные ФИО — нет); interlink `/obezlichivanie-dannyh-chatgpt-finansist/`.
4. **Path B: Google Cloud + SA** — проект → включить **Google Sheets API** → service account → JSON-ключ → скопировать `client_email` → «Поделиться» на файл реестра с ролью **Редактор** (без «Уведомить»).
5. **Path B: mcp.json** — глобально `~/.cursor/mcp.json` или проектно `.cursor/mcp.json`; блок `mcp-gsheets` с `npx -y mcp-gsheets@latest` и `GOOGLE_APPLICATION_CREDENTIALS` (абсолютный путь); JSON-ключ **не** в git; Node.js **v20+**.
6. **Path A: Marketplace / Local auth** — Customize → MCPs → Google Sheets → Add → OAuth; для Cloud: Login через https://cursor.com/agents (MCP Servers), не in-app Authenticate с `cursor://`; либо режим **Local**; минимальные scopes; проверить живым read.
7. **Проверить подключение** — перезапуск Cursor после ручного `mcp.json`; Customize → MCPs → статус; Output → **MCP Logs**; Path B: `sheets_check_access`; живой запрос «прочитай A1:C5 листа Реестр».
8. **Рабочий сценарий реестра** — DoD-промпт: `sheets_get_metadata` → найти строку по `doc_key` → `sheets_update_values` / `sheets_append_values` только в колонки статуса/комментария → `sheets_get_values` на ту же строку → сверка; human approval на каждый write-tool; для append явно `INSERT_ROWS` (дефолт OVERWRITE).
9. **Эксплуатация** — allowlist write-tools; ротация ключа SA (B93); квота SA ≈ **60 write/min на user**; при >80–100 заявок/мес или audit — n8n/ERP, Sheets = staging; соседние реестры B51/B58/B83.

**Workflow для статьи:**  
`Реестр в Sheets → (SA share | OAuth plugin) → MCP в Cursor → Agent read/update по doc_key → перечитка диапазона → регламент CFO`

---

## Яндекс Wordstat (MCP user-mcp-kv)

⚠️ **WORDSTAT AUTH WARNING:** сервер MCP `user-mcp-kv` в этой Cloud-сессии **не подключён** (в каталоге dynamic tools: `cursor`, `Cursor Automation Tools`, `cursor-cloud`, `cursor-subscriptions`; инструментов `wordstat_*` нет). Вызов `wordstat_get_top_requests` для `mcp google sheets cursor` **не выполнен**. Точные показы/мес **не получены** и **не выдуманы**.

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
| Security | service account json не в git, обезличивание sheets, oauth scopes минимум, cursor:// oauth | FAQ |
| Ops | sheets_check_access, mcp logs cursor, unauthorized google mcp, 429 sheets api | troubleshooting |
| Adjacent | cursor google workspace plugins 2026, mcp cursor finansist | interlink B21 |

**SEO-вывод:** SERP по `mcp google sheets cursor` — EN community MCP (freema, PasteSheet, Composio) + новости Cursor Workspace (03–04.08.2026) + баг-репорты OAuth. Почти нет RU how-to «финансист + реестр + Cursor без копипаста». Угол КОДА: **правка управленческих реестров через MCP**, с честным Path A/B и сравнением с B82 (скрипт) / B21 (общий MCP).

---

## SERP (WebSearch Cursor, 24.08.2026)

Приоритет — живой WebSearch; `research-serp.json` (шаг 0) — черновик URL; query `2026 2026` **игнорировать**. Окно свежести: источники после **2026-08-01** предпочтительны.

### Primary: `mcp google sheets cursor 2026`

| # | URL | Тип | Пробел для КОДА |
| --- | --- | --- | --- |
| 1 | https://github.com/freema/mcp-gsheets | Community MCP (SA) | EN; dev-фокус, не CFO/реестры |
| 2 | https://dev.to/pastesheet/google-sheets-in-vs-code-cursor-and-windsurf-over-mcp-5467 | Hosted URL MCP | Публичные листы; не SA |
| 3 | https://composio.dev/toolkits/googlesheets | SaaS-посредник OAuth | Не финконтур |
| 4 | https://cursor.com/docs/mcp | Официальный MCP reference | Нет Sheets-кейса |
| 5 | https://cursor.com/help/customization/mcp | Help: mcp.json, OAuth, approvals | Канон шагов; нет реестров |
| 6 | https://playbooks.com/mcp/freema/mcp-gsheets | Install playbook | Дубль README |
| 7 | https://mcp-catalog.ru/tutorials/google-sheets-cursor | RU community how-to | Не finance angle |
| 8 | https://cursor.com/marketplace/mcp/google-sheets | Marketplace card | **404 Not Found** на 24.08.2026 |

### News / official Workspace (август 2026)

| # | URL | Тип | Пробел |
| --- | --- | --- | --- |
| 1 | https://cursor.com/changelog/google-workspace-plugins | Changelog 03.08.2026 | В теле только Drive/Gmail/Calendar |
| 2 | https://mayai.ru/cursor-otkryl-gmail-i-sheets-agentam/ | RU разбор релиза | Контент-завод; мало SA/реестров |
| 3 | https://vibecoding.ru/news/2026/08/03/cursor-google-workspace-plugins | RU новость 03–04.08 | Sheets убрали из витрины 04.08 |
| 4 | https://authorityaitools.com/blog/cursor-google-workspace-plugins-august-2026 | EN обзор | Заявляет Sheets/Docs/Chat шире changelog |
| 5 | https://forum.cursor.com/t/google-sheet-authentication-is-broken-atm-critical/167413 | Forum 04.08.2026 | OAuth Error 400; Local vs Cloud |
| 6 | https://forum.cursor.com/t/google-workspace-plugins-oauth-fails-error-400-invalid-request-on-cursor-redirect/167402 | Forum OAuth | Workaround: cursor.com/agents Login |

### Secondary: `автоматизация финотдела` + реестры

| # | URL | Тип | Пробел |
| --- | --- | --- | --- |
| 1 | https://koda-fd.ru/blog/ai-dlya-finansista-2026/ | Hub КОДА | Нет MCP Cursor |
| 2 | https://datalopata.ru/blog/avtomatizatsija-finansov-sistemnyj-podhod-k-uchetu-v-2026-godu/ | Автоматизация учёта | ERP-уклон |
| 3 | https://znaj.org/ru/6-luchshikh-reshenii-2026-goda-avtomatizacii-upravleniya-finansami/ | Обзор решений | Не Cursor |

### H1-aligned

| # | URL | Заметка |
| --- | --- | --- |
| 1 | https://mcp-catalog.ru/tutorials/gsheets-cursor | RU: freema/mcp-gsheets в Cursor |
| 2 | https://khar-ag.ru/docs/cursor-mcp-guide/ | mcp.json RU |
| 3 | https://mayai.ru/cursor-mcp-podklyuchenie/ | Общий MCP setup + tool call |

### Конкурентный зазор (угол КОДА)

1. **Finance-first** — не «подключи Sheets к Cursor», а «перестань копировать реестр в чат: agent правит строку по `doc_key`».
2. **Два пути с честным статусом на август 2026** — OAuth-плагин для пилота (с оговорками Marketplace/OAuth) vs SA+mcp-gsheets для production.
3. **Связка с реестрами серии** — договоры (B51), УПД (B58), SaaS (B83); MCP = слой правок поверх таблицы.
4. **Security** — минимальный share, ключ вне git, approval tools, indirect prompt injection, обезличивание.
5. **Verify loop** — после write всегда `get_values`; Connected ≠ authorized.
6. **Fork от B82** — B82 = скрипт пишет в staging; B92 = Agent+MCP без кода.

---

## Таблица фактов

| # | Утверждение | Источник | Дата |
| --- | --- | --- | --- |
| 1 | MCP подключает Cursor к внешним инструментам; Agent вызывает tools в чате. | https://cursor.com/help/customization/mcp | 2026-08-24 |
| 2 | Конфиг: проектный `.cursor/mcp.json` + глобальный `~/.cursor/mcp.json`; при совпадении имени побеждает **проектный**. | https://cursor.com/help/customization/mcp | 2026-08-24 |
| 3 | Локальный MCP: `command`/`args`/`env`; удалённый — поле `url` (+ опционально `headers`). | https://cursor.com/help/customization/mcp | 2026-08-24 |
| 4 | One-click: Customize → MCPs → Add to Cursor; после ручного `mcp.json` — **перезапуск Cursor**. | https://cursor.com/help/customization/mcp | 2026-08-24 |
| 5 | По умолчанию Agent **запрашивает approval** перед MCP-tool; с Cursor 3.6+ — Auto-review / allowlist. | https://cursor.com/help/customization/mcp | 2026-08-24 |
| 6 | Troubleshooting: Output → **MCP Logs** (`Ctrl+Shift+U` / `Cmd+Shift+U`). | https://cursor.com/help/customization/mcp | 2026-08-24 |
| 7 | Cloud Agents поддерживают MCP, настроенные в Cloud Agents dashboard / Team Integrations. | https://cursor.com/help/customization/mcp | 2026-08-24 |
| 8 | 03.08.2026 Cursor анонсировал Google Workspace plugins; в **официальном changelog** детально перечислены **Drive, Gmail, Calendar** (установка Marketplace / Customize). | https://cursor.com/changelog/google-workspace-plugins | 2026-08-24 |
| 9 | В анонсах/обзорах также фигурируют Docs и Sheets, но в тексте changelog Sheets **не расписан** — не утверждать паритет с Drive/Gmail без проверки витрины. | https://cursor.com/changelog/google-workspace-plugins ; https://authorityaitools.com/blog/cursor-google-workspace-plugins-august-2026 | 2026-08-24 |
| 10 | По vibecoding.ru (03–04.08.2026): из пяти обещанных плагинов Docs/Sheets/Slides убрали из витрины; остались Gmail, Drive, Calendar; мин. версия Cursor **3.13.0**; OAuth-bug `cursor://` → Error 400. | https://vibecoding.ru/news/2026/08/03/cursor-google-workspace-plugins | 2026-08-24 |
| 11 | На 24.08.2026 страница https://cursor.com/marketplace/mcp/google-sheets отвечает **404 Not Found** — Path A через Marketplace нельзя обещать «в один клик без проверки». | https://cursor.com/marketplace/mcp/google-sheets | 2026-08-24 |
| 12 | Forum 04.08.2026: Google Sheets MCP auth ломается (Error 400 invalid_request); Local auth может работать; Cloud — Login через https://cursor.com/agents → MCP Servers. | https://forum.cursor.com/t/google-sheet-authentication-is-broken-atm-critical/167413 | 2026-08-24 |
| 13 | Тот же OAuth-баг: in-app Authenticate шлёт `cursor://…/oauth/callback`, Google отклоняет; workaround — agents dashboard или Local. | https://forum.cursor.com/t/google-workspace-plugins-oauth-fails-error-400-invalid-request-on-cursor-redirect/167402 | 2026-08-24 |
| 14 | mayai.ru: плагины Workspace — удалённый MCP Google под правами аккаунта; «Connected» в UI **не гарантирует** валидный Google OAuth — проверять живым tool call. | https://mayai.ru/cursor-otkryl-gmail-i-sheets-agentam/ | 2026-08-24 |
| 15 | Риск MCP+Google: агент наследует права пользователя; в письмах/документах возможна **indirect prompt injection** — human-in-the-loop на write/send. | https://mayai.ru/cursor-otkryl-gmail-i-sheets-agentam/ | 2026-08-24 |
| 16 | Локальный OAuth Cursor **не переезжает автоматически** на Cloud Agents — нужен отдельный коннектор/SA. | https://mayai.ru/cursor-otkryl-gmail-i-sheets-agentam/ | 2026-08-24 |
| 17 | `freema/mcp-gsheets`: Node.js **v20+**, Google Cloud + Sheets API + service account JSON; Cursor: Settings → MCP → New MCP Server; `npx -y mcp-gsheets@latest` + `GOOGLE_APPLICATION_CREDENTIALS`. | https://github.com/freema/mcp-gsheets | 2026-08-24 |
| 18 | Share: добавить `client_email` из JSON на таблицу с ролью **Editor**. | https://github.com/freema/mcp-gsheets | 2026-08-24 |
| 19 | Ключевые tools для реестра: `sheets_get_values`, `sheets_update_values`, `sheets_append_values`, `sheets_batch_get_values`, `sheets_get_metadata`, `sheets_check_access`. | https://github.com/freema/mcp-gsheets | 2026-08-24 |
| 20 | `sheets_append_values`: дефолт `insertDataOption` = **OVERWRITE** — для реестра явно указывать **INSERT_ROWS**. | https://github.com/freema/mcp-gsheets | 2026-08-24 |
| 21 | Sheets API: **300** read/write req/min на проект; **60** read/write req/min на user/project; SA = один user → часто упираются в 60; превышение → HTTP **429**. | https://developers.google.com/workspace/sheets/api/limits | 2026-08-24 |
| 22 | PasteSheet: MCP по `url` в `mcp.json` для публичных листов; private endpoints — платный план от **$9/mo**. | https://dev.to/pastesheet/google-sheets-in-vs-code-cursor-and-windsurf-over-mcp-5467 | 2026-08-24 |
| 23 | В 2026 финотдел автоматизирует классификацию платежей, сверки, управленческую отчётность — Sheets+MCP = **transport правок**, не GL. | https://koda-fd.ru/blog/ai-dlya-finansista-2026/ | 2026-08-24 |

**Не выдумывать:** показы Wordstat; что карточка Sheets «всегда в Marketplace» (на дату research — 404); что SA = доступ ко всему Drive; обещание «без программиста» для Path B без упоминания GCP/SA; паритет Sheets с Drive в официальном changelog.

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

- **Можно ли без программиста?** — Path A (Marketplace+OAuth): да для пилота *если* плагин и auth доступны; Path B (SA+mcp.json): по инструкции, Cursor поможет с JSON; production — 1–2 ч первый реестр.
- **Сколько займёт внедрение?** — SA + mcp.json + один тестовый update: **~1–2 ч**; OAuth-плагин быстрее, если витрина/auth живы.
- **Какие риски для данных?** — OAuth = права Google-аккаунта; SA-ключ = все расшаренные файлы; не класть ПДн; подтверждать write-tools; indirect injection.
- **OAuth или service account?** — OAuth для личного пилота; SA для командного реестра и минимального blast radius (и как обход сломанного Cloud OAuth).
- **Чем отличается от B82?** — B82 = Python/Node скрипт пишет в staging; B92 = Agent в Cursor правит через MCP без скрипта.
- **Работает ли в Cloud Agents?** — локальный OAuth не переезжает автоматически; Login через agents dashboard или SA.

---

## CTA / interlink

- Internal: `/avtomatizaciya-finansov-no-code/`, `/obezlichivanie-dannyh-chatgpt-finansist/`, `/google-sheets-api-integraciya-finotdel/` (B82), `/mcp-cursor-finansist-instrumenty/` (B21)
- Соседние реестры: B51, B58, B83; ротация ключа: B93
- CTA: `https://club.koda-fd.ru/?utm_source=blog&utm_medium=article&utm_campaign=mcp-google-sheets-cursor-reestry` (≤2), `https://t.me/finance_modern?utm_source=blog&utm_medium=article` (≤2)

---

## Handoff marker

`=== EXCALIBUR BLOG RESEARCH ===` — см. `.cursor/excalibur-blog-handoff.md`

**summary:** utility PASS. WebSearch 24.08.2026: Path B (`freema/mcp-gsheets`+SA) — основной production-маршрут; Path A (Marketplace Sheets) — 404 + OAuth `cursor://` баги. Wordstat: MCP `user-mcp-kv` недоступен (⚠️ AUTH WARNING). 23 факта с URL, 9 шагов action_outline. Готов к writer.
