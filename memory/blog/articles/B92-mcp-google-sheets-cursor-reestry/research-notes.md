# Research notes — B92

**topic_id:** B92  
**slug:** mcp-google-sheets-cursor-reestry  
**h1:** Как подключить MCP к Google Sheets в Cursor и править реестры без копипаста  
**research_date:** 2026-08-29  
**EXCALIBUR_RUN_DATE:** 2026-08-29  
**publish_target:** koda-fd.ru/blog  
**utility_gate:** PASS (`how_to`, mode B) — подтверждено `excalibur_blog_utility_gate.py`  
**author_id:** olga-kondratskaya  
**related_internal:** `/avtomatizaciya-finansov-no-code/`, `/obezlichivanie-dannyh-chatgpt-finansist/`  
**sibling_queue:** B82 (Sheets API + SA), B21/B03 (MCP в Cursor), B51/B58/B83 (реестры в Sheets), B93 (ротация SA)  
**cover_scene_hint:** abstract holographic finance automation dark #0a0a0f purple #8b5cf6, no text  
**freshness_window:** предпочитать источники после 2026-05-31; факты сверены WebSearch/WebFetch 2026-08-29

---

## utility_verdict

**PASS** — тема utility-only how_to. Читатель получает рабочий маршрут: подключить Google Sheets к Cursor через MCP (рекомендуемый Path B: community `freema/mcp-gsheets` + service account; опциональный Path A: Marketplace/OAuth, если плагин доступен), подготовить реестр без сырых ПДн, прогнать сценарий «найти строку по `doc_key` → обновить статус → перечитать», чеклист безопасности и troubleshooting. Не новость «Cursor открыл Workspace», не обзор всех MCP-серверов, не «напиши свой MCP с нуля».

---

## reader_outcome

После гайда финансист сможет подключить MCP Google Sheets в Cursor, дать агенту доступ только к рабочему реестру (через service account), попросить обновить статус строки или дописать поля без копирования таблицы в чат и проверить результат перечиткой диапазона через MCP-tool.

---

## action_outline

1. **Решить, нужен ли MCP Sheets** — реестр уже в Google Sheets (договоры, УПД, SaaS, заявки), правки повторяются, устали таскать диапазоны в чат; **не** делать, если нужен жёсткий audit trail / сотни таблиц с enterprise ACL — тогда 1С/CLM, Sheets только staging.
2. **Выбрать путь подключения (честно на 29.08.2026)** — **Path B (рекомендуемый для финотдела):** `freema/mcp-gsheets` + service account, share только нужных реестров. **Path A (пилот):** плагин Google Sheets из Marketplace/Customize + OAuth — нестабилен: changelog 03.08 детализирует только Drive/Gmail/Calendar; Sheets то появляется в витрине/форуме, то уходит; OAuth часто ломается на `cursor://` (обход: login на cursor.com/agents).
3. **Подготовить реестр** — одна строка = одна сущность; стабильный `doc_key`; лист `staging` для импорта; в облако без сырых ПДн (ИНН/сумма/статус — да; паспорт, полные ФИО — нет); interlink `/obezlichivanie-dannyh-chatgpt-finansist/`.
4. **Path B: Google Cloud + SA** — проект → включить **Google Sheets API** → service account → JSON-ключ → скопировать `client_email` → «Поделиться» на файл реестра с ролью **Редактор** (без «Уведомить»).
5. **Path B: mcp.json в Cursor** — глобально `~/.cursor/mcp.json` или проектно `.cursor/mcp.json`; блок `mcp-gsheets` с `npx -y mcp-gsheets@latest`, `GOOGLE_PROJECT_ID`, `GOOGLE_APPLICATION_CREDENTIALS` (абсолютный путь); JSON-ключ **не** в git.
6. **Перезапуск и проверка** — полностью закрыть Cursor; Customize → MCPs → зелёный статус; Output → **MCP Logs**; tool `sheets_check_access` → «прочитай A1:C5 листа Реестр».
7. **Рабочий сценарий реестра** — DoD-промпт: `sheets_get_metadata` → найти строку по `doc_key` → `sheets_update_values` / `sheets_append_values` только в колонки статуса/комментария → `sheets_get_values` на ту же строку → сверка; human approval на каждый write-tool.
8. **Безопасность** — allowlist write-tools; минимальный share SA; не класть ПДн; помнить: MCP = запрос/ответ в чате, не триггер по изменению строки; Cloud Agents не наследуют локальный OAuth.
9. **Эксплуатация и рост** — ротация ключа SA (B93); при >80–100 заявок/мес или audit — n8n/ERP, Sheets остаётся staging; соседние реестры B51/B58/B83; fork от B82 (скрипт) → B92 (Agent+MCP без кода).

**Workflow для статьи:**  
`Реестр в Sheets → SA share → mcp.json (mcp-gsheets) → Agent read/update по doc_key → перечитка диапазона → регламент CFO`  
*(Path A Marketplace — боковая ветка «если плагин доступен и OAuth прошёл»)*

---

## Яндекс Wordstat (MCP user-mcp-kv)

⚠️ **WORDSTAT UNAVAILABLE:** сервер MCP `user-mcp-kv` в этой Cloud-сессии **не подключён**. В каталоге dynamic tools доступны только `cursor`, `Cursor Automation Tools`, `cursor-cloud`, `cursor-subscriptions`. Вызов `wordstat_get_top_requests` **не выполнен**. Точные показы/мес **не получены** и **не выдуманы**.

Обновление токена / подключение MCP-KV: https://oauth.yandex.ru/authorize?response_type=token&client_id=c654b948515a4a07a4c89648a0831d40

### Таблица спроса (Wordstat)

| Фраза | Показы в месяц |
| --- | --- |
| mcp google sheets cursor | *не получено — MCP недоступен* |
| google sheets mcp | *не получено — MCP недоступен* |
| cursor mcp | *не получено — MCP недоступен* |
| mcp сервер для cursor | *не получено — MCP недоступен* |
| подключить mcp cursor | *не получено — MCP недоступен* |
| автоматизация финотдела | *не получено — MCP недоступен* |

**Экспертная семантика (LSI для writer, без цифр спроса):**

| Кластер | Фразы | Роль |
| --- | --- | --- |
| Primary | mcp google sheets cursor, google sheets mcp cursor | H1, title |
| Setup | mcp.json cursor, mcp-gsheets service account, uvx mcp-google-sheets | H2 пошагово |
| Marketplace | cursor marketplace google sheets, cursor google workspace plugins | Path A / honest note |
| Finance | автоматизация финотдела google sheets, реестр договоров cursor, править реестр без копипаста | угол КОДА |
| Registry | реестр upd google sheets, реестр saas подписок, doc_key find update | кейсы |
| Security | service account json не в git, обезличивание sheets, oauth scopes минимум | FAQ |
| Ops | sheets_check_access, mcp logs cursor, unauthorized google mcp, 429 sheets api | troubleshooting |
| Adjacent | cursor google workspace plugins 2026, mcp cursor finansist | interlink B21/B03 |

**SEO-вывод:** SERP по `mcp google sheets cursor` — **EN how-to community MCP** (freema, xing5, we2go) + **новости Cursor Workspace (август 2026)** + редкие RU-каталоги. Почти нет RU how-to «финансист + реестр + Cursor без копипаста». Угол КОДА: **правка управленческих реестров через MCP**, с Path B как основным и honest note про статус Marketplace Sheets.

---

## SERP (WebSearch Cursor, 29.08.2026)

Приоритет — живой WebSearch/WebFetch; `research-serp.json` (шаг 0) — черновик URL; query `2026 2026` **игнорировать**.

### Primary: `mcp google sheets cursor` / `MCP Google Sheets Cursor setup 2026`

| # | URL | Тип | Пробел для КОДА |
| --- | --- | --- | --- |
| 1 | https://cursor.com/ru/help/customization/mcp | Help: mcp.json, approvals, MCP Logs | Канон шагов; нет Sheets-кейса |
| 2 | https://github.com/freema/mcp-gsheets | Community MCP (SA, Node 20+) | EN; tools для реестра; не CFO |
| 3 | https://github.com/xing5/mcp-google-sheets | Popular community (`uvx`) | GCP+SA; не реестры |
| 4 | https://github.com/we2go/google-mcp | npx wizard OAuth/SA | Sheets+Docs; не finance |
| 5 | https://www.usecarly.com/blog/google-sheets-mcp/ | «Нет official Sheets MCP от Google» | Маркетинг workflow SaaS |
| 6 | https://llmversus.com/mcp/google-sheets-mcp | Install guide Cursor/Claude 2026 | Dev setup |
| 7 | https://www.quadratichq.com/ai/mcp/google-sheets | Hosted alternative | Не SA/финконтур |
| 8 | https://mcp-catalog.ru/tutorials/gsheets-cursor | RU: freema → Cursor | Нет угла реестров |

### News / official Workspace (август 2026)

| # | URL | Тип | Пробел |
| --- | --- | --- | --- |
| 1 | https://cursor.com/changelog/google-workspace-plugins | Changelog 03.08.2026 | Только **Drive, Gmail, Calendar** |
| 2 | https://vibecoding.ru/news/2026/08/03/cursor-google-workspace-plugins | RU: из 5 обещанных осталось 3 | Docs/Sheets убраны 04.08; OAuth bug |
| 3 | https://forum.cursor.com/t/google-sheet-authentication-is-broken-atm-critical/167413 | Forum: Sheets auth 400 | Workaround cursor.com/agents |
| 4 | https://www.explainx.ai/blog/cursor-google-workspace-plugins-gmail-drive-calendar-august-2026 | EN gap-анализ | Sheets не в changelog |
| 5 | https://aicatchup.com/news/cursor-google-workspace-plugins | Correction: только 3 плагина | Не how-to |
| 6 | https://mayai.ru/cursor-otkryl-gmail-i-sheets-agentam/ | RU разбор + риски | Контент-завод; мало SA |

### Secondary: `автоматизация финотдела` + реестры Sheets

| # | URL | Тип | Пробел |
| --- | --- | --- | --- |
| 1 | https://koda-fd.ru/blog/ai-dlya-finansista-2026/ | Hub КОДА | Нет MCP Cursor |
| 2 | https://dzen.ru/a/anRW32ni3D3wHjQF | Реестр договоров Sheets | Без MCP |
| 3 | https://dzen.ru/a/aoAqyl_t_ztBh3s7 | Реестр УПД Sheets | Без MCP |
| 4 | https://dzen.ru/a/aoV6BGni3D3wS-su | Sheets API + SA | Скрипт, не Agent MCP |
| 5 | https://datalopata.ru/blog/avtomatizatsija-finansov-sistemnyj-podhod-k-uchetu-v-2026-godu/ | Приоритеты 2026 | ERP-уклон |

### H1-aligned (RU)

| # | URL | Заметка |
| --- | --- | --- |
| 1 | https://mcp-catalog.ru/tutorials/gsheets-cursor | freema/mcp-gsheets |
| 2 | https://mcp-catalog.ru/tutorials/google-sheets-cursor | henilcalagiya variant |
| 3 | https://neurinix.com/2026/06/21/podklyuchenie-mcp-cursor/ | Общий MCP setup |
| 4 | https://khar-ag.ru/docs/cursor-mcp-guide/ | mcp.json RU |

### Конкурентный зазор (угол КОДА)

1. **Finance-first** — «перестань копировать реестр в чат: agent правит строку по `doc_key`».
2. **Path B first** — SA+mcp-gsheets как основной production-путь; Marketplace Sheets — честный optional с рисками августа 2026.
3. **Связка с реестрами серии** — договоры (B51), УПД (B58), SaaS (B83); MCP = слой правок поверх уже спроектированной таблицы.
4. **Security** — минимальный share, ключ вне git, approval tools, indirect prompt injection, обезличивание.
5. **Verify loop** — после write всегда `get_values`; «Connected ≠ authorized».
6. **Fork от B82** — B82 = Python-скрипт; B92 = те же SA+share, но правки через Agent+MCP.

---

## Таблица фактов

| # | Утверждение | Источник | Дата сверки |
| --- | --- | --- | --- |
| 1 | MCP подключает Cursor к внешним инструментам; Agent вызывает tools в чате. | https://cursor.com/ru/help/customization/mcp | 2026-08-29 |
| 2 | Конфиг: проектный `.cursor/mcp.json` + глобальный `~/.cursor/mcp.json`; при совпадении имени побеждает **проектный**. | https://cursor.com/ru/help/customization/mcp | 2026-08-29 |
| 3 | Локальный MCP: `command`/`args`/`env`; удалённый — `url` (+ опционально `headers`). | https://cursor.com/ru/help/customization/mcp | 2026-08-29 |
| 4 | One-click: Customize → MCPs → Add to Cursor; после ручного `mcp.json` — **перезапуск Cursor**. | https://cursor.com/ru/help/customization/mcp | 2026-08-29 |
| 5 | По умолчанию Agent **запрашивает approval** перед MCP-tool; с Cursor 3.6+ — Auto-review / allowlist (`permissions.json`). | https://cursor.com/ru/help/customization/mcp | 2026-08-29 |
| 6 | Troubleshooting: Output → **MCP Logs** (`Ctrl+Shift+U` / `Cmd+Shift+U`). | https://cursor.com/ru/help/customization/mcp | 2026-08-29 |
| 7 | Cloud Agents поддерживают MCP, настроенные в дашборде Cloud Agents / Team Marketplace — не автоматически копируют локальный OAuth. | https://cursor.com/ru/help/customization/mcp | 2026-08-29 |
| 8 | 03.08.2026 Cursor changelog: плагины **Google Drive, Gmail, Google Calendar**; установка из Marketplace или Customize. | https://cursor.com/changelog/google-workspace-plugins | 2026-08-29 |
| 9 | В официальном changelog Sheets/Docs **не детализированы** (только Drive/Gmail/Calendar). | https://cursor.com/changelog/google-workspace-plugins | 2026-08-29 |
| 10 | По vibecoding.ru (04.08.2026): из пяти обещанных Workspace-плагинов в витрине остались **Gmail, Drive, Calendar**; Docs/Sheets убраны; мин. версия Cursor **3.13.0**; OAuth-bug callback `cursor://`. | https://vibecoding.ru/news/2026/08/03/cursor-google-workspace-plugins | 2026-08-29 |
| 11 | Официальные MCP Google Workspace — **Developer Preview**, доступ через программу разработчиков Google. | https://vibecoding.ru/news/2026/08/03/cursor-google-workspace-plugins | 2026-08-29 |
| 12 | Forum 04.08.2026: Google Sheets из Marketplace даёт Error 400 `invalid_request` (OAuth policy); Kevin Neilson (Cursor): обход — Login на https://cursor.com/agents → MCP Servers (другой callback); Local auth может работать. | https://forum.cursor.com/t/google-sheet-authentication-is-broken-atm-critical/167413 | 2026-08-29 |
| 13 | У Google **нет** first-party Google Sheets MCP для внешних AI-клиентов; на практике — community-серверы, оборачивающие Sheets API. | https://www.usecarly.com/blog/google-sheets-mcp/ | 2026-08-29 |
| 14 | `freema/mcp-gsheets`: Node.js **v20+**, GCP + Sheets API + service account JSON; Cursor: `npx -y mcp-gsheets@latest` + `GOOGLE_PROJECT_ID` + `GOOGLE_APPLICATION_CREDENTIALS`. | https://github.com/freema/mcp-gsheets | 2026-08-29 |
| 15 | Ключевые tools для реестра: `sheets_get_values`, `sheets_update_values`, `sheets_append_values`, `sheets_batch_get_values`, `sheets_get_metadata`, `sheets_check_access`. | https://github.com/freema/mcp-gsheets (README) | 2026-08-29 |
| 16 | `sheets_append_values`: default `insertDataOption` = **OVERWRITE** — для реестра явно `INSERT_ROWS`, если нужно сдвигать строки. | https://github.com/freema/mcp-gsheets (README) | 2026-08-29 |
| 17 | Альтернатива: `xing5/mcp-google-sheets` через `uvx mcp-google-sheets@latest` + `SERVICE_ACCOUNT_PATH` (+ часто `DRIVE_FOLDER_ID`). | https://github.com/xing5/mcp-google-sheets | 2026-08-29 |
| 18 | Service account видит **только** таблицы, расшаренные на `client_email`; IAM Cloud **не заменяет** Share файла. | https://developers.google.com/workspace/guides/create-credentials#service-account ; README freema | 2026-08-29 |
| 19 | Scope `https://www.googleapis.com/auth/spreadsheets` — read/write всех расшаренных таблиц SA; применяется ко **всему файлу**; листы — ProtectedRange. | https://developers.google.com/workspace/sheets/api/scopes | 2026-08-29 |
| 20 | Квота Sheets API: read/write **300/мин на проект** и **60/мин на user/project**; превышение → HTTP **429**; квоты refill каждую минуту. | https://developers.google.com/workspace/sheets/api/limits | 2026-08-29 |
| 21 | MCP Sheets — request/response в открытом чате: **нет** триггеров «при изменении строки» и ничего не крутится при закрытом окне. | https://www.usecarly.com/blog/google-sheets-mcp/ | 2026-08-29 |
| 22 | Риск: агент наследует права аккаунта; в письмах/ячейках возможна **indirect prompt injection** — human-in-the-loop на write. | https://mayai.ru/cursor-otkryl-gmail-i-sheets-agentam/ | 2026-08-29 |
| 23 | «Connected» в Tools & MCP **не гарантирует** успешный Google OAuth — проверять живым read/write. | https://mayai.ru/cursor-otkryl-gmail-i-sheets-agentam/ ; forum Cursor | 2026-08-29 |
| 24 | Реестр договоров в Sheets уместен до **200–300** активных договоров при одном владельце; иначе CLM/1С. | https://dzen.ru/a/anRW32ni3D3wHjQF | 2026-08-29 |
| 25 | В 2026 финотдел автоматизирует в первую очередь классификацию платежей, сверки, УО — Sheets+MCP = **transport правок**, не GL. | https://koda-fd.ru/blog/ai-dlya-finansista-2026/ | 2026-08-29 |

**Не выдумывать:** показы Wordstat; «Sheets-плагин всегда стабильно в Marketplace»; что SA = доступ ко всему Drive; обещание «без программиста» для Path B без GCP/SA; цифры ROI из fact-bank про контент-заводы.

**fact-bank.md:** прямых фактов про MCP+Sheets нет — опираться на таблицу выше.

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

- **Можно ли без программиста?** — Path A (Marketplace+OAuth): да для пилота *если* плагин доступен и OAuth прошёл; Path B (SA+mcp.json): по инструкции B82/B92, Cursor поможет с JSON; production — 1–2 ч первый реестр.
- **Сколько займёт внедрение?** — SA + mcp.json + один тестовый update: **~1–2 ч**; OAuth-плагин быстрее, если доступен.
- **Какие риски для данных?** — OAuth = права вашего Google; SA-ключ = все расшаренные файлы; не класть ПДн; подтверждать write-tools; indirect injection.
- **OAuth или service account?** — OAuth для личного пилота; SA для командного реестра и минимального blast radius (**рекомендация статьи**).
- **Чем отличается от B82?** — B82 = Python/Node скрипт пишет в staging; B92 = Agent в Cursor правит через MCP без скрипта.
- **Работает ли в Cloud Agents?** — локальный OAuth не переезжает автоматически; для облака — отдельный коннектор/SA в дашборде.

---

## CTA / interlink

- Internal: `/avtomatizaciya-finansov-no-code/`, `/obezlichivanie-dannyh-chatgpt-finansist/`, `/google-sheets-api-integraciya-finotdel/` (B82), `/mcp-cursor-finansist-instrumenty/` (B21)
- Соседние реестры: B51, B58, B83; ротация ключа: B93
- CTA: `https://club.koda-fd.ru/?utm_source=blog&utm_medium=article&utm_campaign=mcp-google-sheets-cursor-reestry` (≤2), `https://t.me/finance_modern?utm_source=blog&utm_medium=article` (≤2)

---

## Handoff marker

`=== EXCALIBUR BLOG RESEARCH ===` — см. `.cursor/excalibur-blog-handoff.md`
