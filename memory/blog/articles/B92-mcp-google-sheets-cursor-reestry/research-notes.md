# Research notes — B92

**topic_id:** B92  
**slug:** mcp-google-sheets-cursor-reestry  
**h1:** Как подключить MCP к Google Sheets в Cursor и править реестры без копипаста  
**research_date:** 2026-09-13  
**publish_target:** koda-fd.ru/blog  
**utility_gate:** PASS (`how_to`, mode B)  
**author_id:** olga-kondratskaya  
**related_internal:** `/avtomatizaciya-finansov-no-code/`, `/obezlichivanie-dannyh-chatgpt-finansist/`  
**sibling_queue:** B82 (Sheets API + SA), B21 (MCP в Cursor общий), B51/B58/B83 (реестры в Sheets), B93 (ротация SA)  
**cover_scene_hint:** abstract holographic finance automation dark #0a0a0f purple #8b5cf6, no text  
**freshness_window:** prefer sources after 2026-06-15; versions as of 2026-09-13

---

## utility_verdict

**PASS** — тема utility-only how_to. Читатель получает рабочие маршруты подключения Google Sheets к Cursor через MCP (Marketplace/OAuth-плагин **или** community `freema/mcp-gsheets` на service account **или** Google remote `sheetsmcp.googleapis.com` в Developer Preview), подготовку реестра под агентные правки, тестовый сценарий «найти строку → обновить статус → перечитать», чеклист безопасности и troubleshooting. Не новость «Cursor открыл Workspace», не обзор 25 MCP-серверов, не туториал «напиши свой MCP с нуля».

---

## reader_outcome

После гайда финансист сможет подключить MCP Google Sheets в Cursor, дать агенту доступ только к рабочему реестру (через service account или OAuth), попросить обновить статус строки или дописать поля без копирования таблицы в чат и проверить результат перечиткой диапазона через MCP-tool.

---

## action_outline

1. **Решить, нужен ли MCP Sheets** — реестр уже в Google Sheets (договоры, УПД, SaaS, заявки на расход), правки повторяются, устали таскать диапазоны в чат; **не** делать, если нужен жёсткий audit trail / сотни таблиц с enterprise ACL — тогда 1С/CLM, Sheets только staging.
2. **Выбрать путь подключения** — **Path A (пилот):** плагин Google Sheets из Cursor Marketplace / Customize → OAuth личного Google; **Path B (финконтур):** `freema/mcp-gsheets` + service account — расшарить только нужные реестры, ключ в `env`, без доступа агента ко всему Drive (см. B82, B93); **Path C (опционально):** Google first-party remote MCP `https://sheetsmcp.googleapis.com/mcp/v1` — Developer Preview, OAuth, не SA.
3. **Подготовить реестр** — одна строка = одна сущность; стабильный `doc_key`; лист `staging` для импорта; в облако без сырых ПДн (ИНН/сумма/статус — да; паспорт, полные ФИО — нет); interlink `/obezlichivanie-dannyh-chatgpt-finansist/`.
4. **Path B: Google Cloud + SA** — проект → включить **Google Sheets API** → service account → JSON-ключ → скопировать `client_email` → «Поделиться» на файл реестра с ролью **Редактор** (без «Уведомить»).
5. **Path B: mcp.json в Cursor** — глобально `~/.cursor/mcp.json` или проектно `.cursor/mcp.json`; блок `mcp-gsheets` с `npx -y mcp-gsheets@latest` и `GOOGLE_APPLICATION_CREDENTIALS` (абсолютный путь); JSON-ключ **не** в git.
6. **Path A: Marketplace** — Customize → MCPs / Marketplace → Google Sheets → Add → OAuth; минимальные scopes; учитывать: changelog 03.08.2026 детально описывает Drive/Gmail/Calendar; Sheets есть в Marketplace и на форуме, но OAuth для Cloud/SSH может ломаться (workaround через cursor.com/agents).
7. **Проверить подключение** — перезапуск Cursor; Customize → MCPs → зелёный статус; Output → **MCP Logs**; tool `sheets_check_access` (Path B) или живой запрос «прочитай A1:C5 листа Реестр».
8. **Рабочий сценарий реестра** — промпт с DoD: `sheets_get_metadata` → найти строку по `doc_key` → `sheets_update_values` / `sheets_append_values` только в колонки статуса/комментария → `sheets_get_values` на ту же строку → сверка с ожиданием; human approval на каждый write-tool.
9. **Эксплуатация и рост** — allowlist write-tools; ротация ключа SA (B93); при >80–100 заявок/мес или audit — n8n/ERP, Sheets остаётся staging; соседние реестры B51/B58/B83.

**Workflow для статьи:**  
`Реестр в Sheets → (SA share | OAuth plugin | Google remote MCP) → MCP в Cursor → Agent read/update по doc_key → перечитка диапазона → регламент CFO`

---

## Яндекс Wordstat (MCP user-mcp-kv)

⚠️ **WORDSTAT AUTH WARNING:** сервер MCP `user-mcp-kv` в этой Cloud-сессии **не подключён** (в каталоге dynamic tools доступны только `cursor`, `Cursor Automation Tools`, `cursor-cloud`, `cursor-subscriptions`). Вызов `wordstat_get_top_requests` **не выполнен**. Точные показы/мес **не получены** и **не выдуманы**.

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
| Official MCP | sheetsmcp.googleapis.com, google sheets mcp developer preview | FAQ / Path C |
| Finance | автоматизация финотдела google sheets, реестр договоров cursor, править реестр без копипаста | угол КОДА |
| Registry | реестр upd google sheets, реестр saas подписок, doc_key find update | кейсы |
| Security | service account json не в git, обезличивание sheets, oauth scopes минимум, indirect prompt injection | FAQ |
| Ops | sheets_check_access, mcp logs cursor, unauthorized google mcp, cloud agents oauth | troubleshooting |
| Adjacent | cursor google workspace plugins 2026, mcp cursor finansist | interlink B21 |

**SEO-вывод:** SERP по `mcp google sheets cursor` — EN how-to (Merge, Scalekit, community MCP), официальные docs Cursor/Google, RU-каталоги (mcp-catalog.ru) без finance-угла. Почти нет RU how-to «финансист + реестр + Cursor». Угол КОДА: **правка управленческих реестров через MCP без копипаста**, с веткой SA для безопасности и сравнением с B82 (скрипт) и B21 (общий MCP).

---

## SERP (WebSearch Cursor, 13.09.2026)

Приоритет — живой WebSearch; `research-serp.json` (шаг 0) — черновик URL; query `2026 2026` **нерелевантен** — игнорировать.

### Primary: `mcp google sheets cursor 2026`

| # | URL | Тип | Пробел для КОДА |
| --- | --- | --- | --- |
| 1 | https://www.scalekit.com/blog/google-sheets-mcp-vs-api | MCP vs API (31.08.2026) | Dev/product; не реестры CFO |
| 2 | https://developers.google.com/workspace/sheets/api/guides/configure-mcp-server | Official Google Sheets MCP | Preview; Antigravity/Claude; не Cursor finance |
| 3 | https://github.com/freema/mcp-gsheets | Community MCP (SA) | EN; не CFO |
| 4 | https://github.com/we2go/google-mcp | npx wizard OAuth/SA | Sheets+Docs; не реестры |
| 5 | https://github.com/dudegladiator/spreadsheet-mcp | Python/uv, 27 tools | Установка для dev |
| 6 | https://www.merge.dev/blog/google-sheets-mcp-cursor | Merge Agent Handler → Cursor | SaaS-посредник; не SA |
| 7 | https://cursor.com/help/customization/mcp | Официальный MCP help | Канон шагов; нет Sheets-кейса |
| 8 | https://cursor.com/docs/mcp | MCP reference | Нет finance |

### News / official Workspace + Marketplace status

| # | URL | Тип | Пробел |
| --- | --- | --- | --- |
| 1 | https://cursor.com/changelog/google-workspace-plugins | Changelog 03.08.2026 | Drive/Gmail/Calendar детально; Sheets в теле **не** расписан |
| 2 | https://forum.cursor.com/t/google-sheet-authentication-is-broken-atm-critical/167413 | Bug OAuth Sheets 04.08.2026 | Подтверждает наличие плагина; Local OK, Cloud/SSH redirect broken |
| 3 | https://cursor.com/marketplace | Marketplace | Раздел Data & Analytics: «Query and update sheets…» |
| 4 | https://mayai.ru/cursor-otkryl-gmail-i-sheets-agentam/ | RU разбор релиза | Мало SA/реестров |
| 5 | https://www.ai-native.jp/blog/cursor-google-workspace-plugins-enterprise-guide | EN/JP анализ | Gap changelog vs X (Docs/Sheets) |
| 6 | https://developers.google.com/workspace/sheets/api/limits | Quotas (обн. 03.09.2026) | 300/60 read+write; Sheets MCP tool costs |

### Secondary: `автоматизация финотдела` + Sheets реестры

| # | URL | Тип | Пробел |
| --- | --- | --- | --- |
| 1 | https://dzen.ru/a/anAvymtbQE6qYcKj | Банк→Sheets без 1С (КОДА) | Без MCP Cursor |
| 2 | https://pohodu.media/kak-ja-perestal-vruchnuju-zapolnjat-tablicu-dds/ | Make→Sheets ДДС | Без Cursor |
| 3 | https://koda-fd.ru/blog/ai-dlya-finansista-2026/ | Hub КОДА | Нет MCP Cursor |
| 4 | https://dzen.ru/a/anRW32ni3D3wHjQF | Реестр договоров Sheets | Без MCP |

### H1-aligned RU

| # | URL | Заметка |
| --- | --- | --- |
| 1 | https://mcp-catalog.ru/tutorials/gsheets-cursor | RU: freema/mcp-gsheets — шаблон неточный (args `gsheets`), сверять README |
| 2 | https://mcp-catalog.ru/servers/gsheets | Карточка сервера |
| 3 | https://registry.npmjs.org/mcp-gsheets | npm 1.10.2 (16.08.2026), ~3831 weekly downloads |

### Конкурентный зазор (угол КОДА)

1. **Finance-first** — не «подключи Sheets к Cursor», а «перестань копировать реестр в чат: agent правит строку по `doc_key`».
2. **Три пути с выбором** — OAuth-плагин для пилота vs SA+mcp-gsheets для production финконтура vs Google remote MCP (Preview) для тех, кто в программе разработчиков.
3. **Honest status 09.2026** — Sheets в Marketplace есть; Cloud/SSH OAuth может падать (форум); changelog не детализирует Sheets — проверять live.
4. **Связка с реестрами серии** — договоры (B51), УПД (B58), SaaS (B83); MCP = слой правок поверх уже спроектированной таблицы.
5. **Security block** — минимальный share, ключ вне git, approval tools, indirect prompt injection (Google docs + mayai), обезличивание.
6. **Verify loop** — после write всегда `get_values`; «Connected ≠ authorized».
7. **Fork от B82** — B82 = свой Python-скрипт; B92 = те же SA+share, но правки через Agent+MCP без написания кода.

---

## Таблица фактов

| # | Утверждение | Источник | Дата проверки |
| --- | --- | --- | --- |
| 1 | MCP подключает Cursor к внешним инструментам; Agent вызывает tools в чате. | https://cursor.com/help/customization/mcp | 2026-09-13 |
| 2 | Конфиг MCP: проектный `.cursor/mcp.json` + глобальный `~/.cursor/mcp.json`; при совпадении имени побеждает **проектный**. | https://cursor.com/help/customization/mcp | 2026-09-13 |
| 3 | Локальный MCP: `command`, `args`, `env`; удалённый — поле `url` (+ опционально `headers`). | https://cursor.com/help/customization/mcp | 2026-09-13 |
| 4 | One-click: Customize → MCPs → Add to Cursor; после ручного `mcp.json` — **перезапуск Cursor**. | https://cursor.com/help/customization/mcp | 2026-09-13 |
| 5 | По умолчанию Agent **запрашивает approval** перед MCP-tool; с Cursor 3.6+ — Auto-review / allowlist (`permissions.json`). | https://cursor.com/help/customization/mcp | 2026-09-13 |
| 6 | Troubleshooting: Output → **MCP Logs** (`Ctrl+Shift+U` / `Cmd+Shift+U`). | https://cursor.com/help/customization/mcp | 2026-09-13 |
| 7 | Cloud Agents поддерживают MCP, настроенные в Cloud Agents dashboard / Team MCP; локальный OAuth не «переезжает» сам. | https://cursor.com/help/customization/mcp | 2026-09-13 |
| 8 | 03.08.2026 Cursor анонсировал Google Workspace plugins: в changelog явно перечислены **Drive, Gmail, Calendar**; установка из Marketplace или Customize. | https://cursor.com/changelog/google-workspace-plugins | 2026-09-13 |
| 9 | Sheets/Docs в теле changelog 03.08.2026 **не детализированы** (упоминаются в X/обзорах). | https://cursor.com/changelog/google-workspace-plugins ; https://www.ai-native.jp/blog/cursor-google-workspace-plugins-enterprise-guide | 2026-09-13 |
| 10 | На форуме Cursor (04.08.2026) плагин Google Sheets из Marketplace существует; OAuth для **Cloud и SSH** ломается (redirect Google rejects); **Local** может работать; обход Cloud: auth через https://cursor.com/agents → MCP Servers → Google Sheets → Login. | https://forum.cursor.com/t/google-sheet-authentication-is-broken-atm-critical/167413 | 2026-09-13 |
| 11 | Google first-party Sheets MCP: endpoint `https://sheetsmcp.googleapis.com/mcp/v1`, HTTP + OAuth 2.0; Developer Preview; enable `sheets.googleapis.com` + `sheetsmcp.googleapis.com`. | https://developers.google.com/workspace/sheets/api/guides/configure-mcp-server | 2026-09-13 |
| 12 | Tools Google Sheets MCP: `get_values`, `get_spreadsheet`, `update_spreadsheet`, `update_values`, `update_formulas`, `insert_dimension`. | https://developers.google.com/workspace/sheets/api/guides/configure-mcp-server | 2026-09-13 |
| 13 | Preview: service accounts **не** enroll-ятся в Developer Preview Program; для B2B public apps Preview terms ограничивают внешний доступ до GA. | https://www.scalekit.com/blog/google-sheets-mcp-vs-api | 2026-09-13 |
| 14 | Квоты Sheets API / Sheets MCP: **300** read и **300** write /мин на проект; **60** /мин на user/project; превышение → HTTP **429**; batch = 1 запрос. Docs updated 2026-09-03. | https://developers.google.com/workspace/sheets/api/limits | 2026-09-13 |
| 15 | Позже в **2026** превышение quota limits Sheets API планируется тарифицироваться (standardized model for agent tools). | https://developers.google.com/workspace/sheets/api/limits | 2026-09-13 |
| 16 | `freema/mcp-gsheets`: Node.js **v20+**; установка `npx -y mcp-gsheets@latest` + `GOOGLE_PROJECT_ID` + `GOOGLE_APPLICATION_CREDENTIALS`; актуальная npm **1.10.2** (16.08.2026). | https://github.com/freema/mcp-gsheets ; https://www.npmjs.com/package/mcp-gsheets | 2026-09-13 |
| 17 | Ключевые tools mcp-gsheets для реестра: `sheets_get_values`, `sheets_update_values`, `sheets_append_values`, `sheets_batch_get_values`, `sheets_get_metadata`, `sheets_check_access`. | https://github.com/freema/mcp-gsheets | 2026-09-13 |
| 18 | `sheets_append_values`: по умолчанию `insertDataOption` = **OVERWRITE** — для реестра явно указывать `INSERT_ROWS`, если нужно сдвигать строки. | https://github.com/freema/mcp-gsheets | 2026-09-13 |
| 19 | Service account видит **только** таблицы, расшаренные на `client_email` из JSON; IAM-роли Cloud **не заменяют** Share файла. | https://developers.google.com/workspace/guides/create-credentials#service-account | 2026-09-13 |
| 20 | Scope `https://www.googleapis.com/auth/spreadsheets` — read/write всех расшаренных таблиц SA; применяется ко **всему файлу**; листы защищают ProtectedRange. | https://developers.google.com/workspace/sheets/api/scopes | 2026-09-13 |
| 21 | `we2go/google-mcp`: `npx google-sheet-mcp init` — wizard SA или OAuth; tools `sheets_read_range`, `sheets_update_range` / `sheets_write_range`, `sheets_append_row`. | https://github.com/we2go/google-mcp | 2026-09-13 |
| 22 | `dudegladiator/spreadsheet-mcp`: **27 tools**, auth через service-account JSON. | https://github.com/dudegladiator/spreadsheet-mcp | 2026-09-13 |
| 23 | Риск MCP+Google: агент наследует права пользователя; в письмах/ячейках возможна **indirect prompt injection** — нужен human-in-the-loop на write; Google рекомендует Model Armor / review actions. | https://developers.google.com/workspace/sheets/api/guides/configure-mcp-server ; https://mayai.ru/cursor-otkryl-gmail-i-sheets-agentam/ | 2026-09-13 |
| 24 | «Connected» в Tools & MCP **не гарантирует** успешный Google OAuth — проверять живым read/write. | https://mayai.ru/cursor-otkryl-gmail-i-sheets-agentam/ ; forum Cursor | 2026-09-13 |
| 25 | Реестр договоров в Sheets уместен до **200–300** активных договоров при одном владельце таблицы; иначе CLM/1С. | https://dzen.ru/a/anRW32ni3D3wHjQF | 2026-09-13 |
| 26 | Заявки на расход через Forms→Sheets: при **>80–100** заявок/мес Sheets — staging перед ERP/n8n. | https://dzen.ru/a/aoAx4V_t_ztBh5aj | 2026-09-13 |
| 27 | В 2026 финотдел автоматизирует классификацию платежей, сверки, управленческую отчётность — Sheets+MCP подходит как **transport правок**, не GL. | https://koda-fd.ru/blog/ai-dlya-finansista-2026/ | 2026-09-13 |
| 28 | npm weekly downloads `mcp-gsheets` ≈ **3831** (снимок npm на момент research) — ориентир популярности community-пакета, не Wordstat. | https://www.npmjs.com/package/mcp-gsheets | 2026-09-13 |

**Не выдумывать:** показы Wordstat; что Sheets «всегда стабилен» в Marketplace Cloud; что SA = доступ ко всему Drive; цифру Smithery installs без источника; обещание «без программиста» для Path B без упоминания GCP/SA; что Google remote MCP = GA (это Developer Preview).

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

- **Можно ли без программиста?** — Path A (Marketplace+OAuth): да для пилота, если OAuth проходит; Path B (SA+mcp.json): по инструкции B82/B92, Cursor поможет с JSON; production — 1–2 ч первый реестр.
- **Сколько займёт внедрение?** — SA + mcp.json + один тестовый update: **~1–2 ч**; OAuth-плагин быстрее, если auth работает.
- **Какие риски для данных?** — OAuth = права вашего Google; SA-ключ = все расшаренные файлы; не класть ПДн; подтверждать write-tools; indirect injection из писем/ячеек.
- **OAuth или service account?** — OAuth для личного пилота; SA для командного реестра, cron, минимального blast radius; Google remote MCP — Preview, без SA enrollment.
- **Чем отличается от B82?** — B82 = Python/Node скрипт пишет в staging; B92 = Agent в Cursor правит через MCP без скрипта.
- **Работает ли в Cloud Agents?** — локальный OAuth не переезжает автоматически; Cloud Sheets auth может требовать login через cursor.com/agents; надёжнее SA + Team/Cloud MCP config.
- **Почему 429?** — квота 300 write/мин на проект (60 на user); batch и пауза; см. limits docs.

---

## CTA / interlink

- Internal: `/avtomatizaciya-finansov-no-code/`, `/obezlichivanie-dannyh-chatgpt-finansist/`, `/google-sheets-api-integraciya-finotdel/` (B82), `/mcp-cursor-finansist-instrumenty/` (B21)
- Соседние реестры: B51, B58, B83; ротация ключа: B93
- CTA: `https://club.koda-fd.ru/?utm_source=blog&utm_medium=article&utm_campaign=mcp-google-sheets-cursor-reestry` (≤2), `https://t.me/finance_modern?utm_source=blog&utm_medium=article` (≤2)

---

## Handoff marker

`=== EXCALIBUR BLOG RESEARCH ===` — см. `.cursor/excalibur-blog-handoff.md`
