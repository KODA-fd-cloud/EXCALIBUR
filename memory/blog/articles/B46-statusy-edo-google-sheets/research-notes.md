# Research notes — B46

**topic_id:** B46  
**slug:** statusy-edo-google-sheets  
**h1:** Как забирать статусы ЭДО (отправлен/подписан) в Google Sheets без ручного мониторинга  
**research_date:** 2026-08-06  
**publish_target:** koda-fd.ru/blog  
**utility_gate:** PASS (`workflow`, mode B)  
**author_id:** olga-kondratskaya  
**internal_links (карточка):** `/avtomatizaciya-finansov-no-code/`, `/obezlichivanie-dannyh-chatgpt-finansist/`  
**related_published:** `/google-apps-script-finansist-obnovit-dannye/`, `/avtomatizaciya-finansov-no-code/`  
**cover_scene_hint:** abstract holographic finance automation dark #0a0a0f purple #8b5cf6, no text

---

## utility_verdict

**PASS** — тема utility-only workflow. Читатель получает: реестр статусов ЭДО в Google Sheets с автоматическим обновлением (отправлен / ожидает подписи / подписан / отклонён), выбор маршрута (Apps Script + API оператора / n8n / полуручный staging), маппинг технических статусов API на бизнес-слой для финотдела, расписание опроса и правила безопасности токенов. Не обзор «что такое ЭДО в 2026», не регламент закупок без интеграции.

---

## reader_outcome

После гайда финансист или бухгалтер сможет собрать в Google Sheets живой реестр документов ЭДО со статусами «отправлен / ожидает контрагента / подписан обеими сторонами / отклонён», настроить автоматическое обновление через API оператора (на примере Контур.Диадок) или n8n, хранить ключи в Script Properties и видеть просрочки без ежедневного входа в кабинет ЭДО.

---

## action_outline

1. **Когда нужно / когда нет** — 5–15 исходящих/входящих документов в день и несколько отделов → реестр в Sheets оправдан; полный СЭД/1С с модулем ЭДО → достаточно синхронизации из учётки; нет API-доступа у оператора → только полуручный экспорт.
2. **Словарь статусов (2 слоя)** — внешний: события обмена с контрагентом (отправлен, доставлен, подписан нами, подписан обеими, отклонён); внутренний: «готово к оплате / на проверке закупок» (не смешивать с API-полем `DocflowStatus`). Зафиксировать 5–7 формулировок без двусмысленности.
3. **Staging-лист `edo_status`** — колонки: `doc_id` (MessageId+EntityId или номер УПД), `counterparty_inn`, `doc_type`, `doc_date`, `amount`, `api_status_raw`, `business_status`, `last_event_at`, `updated_at`, `alert_flag`. Отдельный лист `log` для ошибок API.
4. **Маршрут A: Apps Script + Диадок API** — зарегистрировать интеграцию в Кабинете интегратора (`client_id`), `access_token` в `PropertiesService.getScriptProperties()`; опрос через `POST /V4/GetDocflowEvents` (cursor `AfterIndexKey` в Properties) вместо полного перебора всех документов; маппинг `RecipientResponseStatus` / `DocflowStatus` → `business_status`; upsert по `doc_id`.
5. **Маршрут B: n8n / Make** — HTTP Request к API оператора по расписанию или webhook (если есть); нода Google Sheets Append/Update Row; upsert по `doc_id`; опционально Telegram при смене статуса на «отклонён» или «ожидает подписи > N дней» (паттерн как у шаблонов Diadoc→Sheets).
6. **Маршрут C: полуавтомат (малый объём)** — еженедельный экспорт списка документов из кабинета ЭДО (CSV/Excel) в папку Drive → Apps Script `Utilities.parseCsv()` → merge в staging; подходит до ~30 документов/неделю без API.
7. **Расписание и лимиты** — `ScriptApp.newTrigger(...).timeBased().everyHours(1)` или 2–4 раза в день; учитывать UrlFetch 20 000/день (consumer) и runtime 6 мин/запуск; пагинация GetDocuments/GetDocflowEvents через `AfterIndexKey`, не тащить тело документов (только метаданные статуса).
8. **Проверка недели 1** — сверить 10 строк реестра с кабинетом ЭДО; отдельно проверить кейс «подписано нами ≠ подписано обеими»; журнал `log` без падения всего сценария при 401/402 (истёк токен / подписка API).
9. **Безопасность и масштаб** — токены и `boxId` только в Properties; не отправлять сырые ИНН/суммы в ChatGPT (см. `/obezlichivanie-dannyh-chatgpt-finansist/`); при росте объёма перейти с polling на event-based `GetDocflowEvents`; следующий шаг — алерт в Telegram (отсылка к no-code статье).

---

## Яндекс Wordstat (MCP user-mcp-kv)

⚠️ **WORDSTAT AUTH WARNING:** сервер MCP `user-mcp-kv` в этой Cloud-сессии **не подключён** (доступен только `cursor-cloud`). Вызов `wordstat_get_top_requests` **не выполнен**. Точные показы/мес **не получены** и **не выдуманы**.

Обновление токена: https://oauth.yandex.ru/authorize?response_type=token&client_id=c654b948515a4a07a4c89648a0831d40

**Экспертная семантика (LSI для writer, без цифр спроса):**

| Кластер | Фразы |
| --- | --- |
| Ядро | статусы эдо google sheets, статусы документов эдо таблица, мониторинг эдо google таблицы |
| Операторы | диадок api статус документа, sbis api статус, getdocflowevents, статусы в эдо контур |
| Автоматизация | автоматизация финотдела эдо, n8n диадок google sheets, apps script эдо |
| Бизнес-смысл | отправлен подписан отклонён эдо, регламент статусов эдо, подписано обеими сторонами |
| Контекст 2026 | упд 5.03 эдо 2026, универсальные сообщения эдо, отмена торг-12 эдо |
| No-code | make интеграция эдо, выгрузка статусов эдо без программиста |

**SEO-вывод:** прямого how-to «статусы эдо + google sheets» в SERP почти нет. Выдача забита новостями реформы ЭДО 2026 (УПД 5.03, отмена ТОРГ-12) и регламентами статусов (eodoc, Точка, Диадок). Угол КОДА: **финотдел на Sheets как дашборд статусов ЭДО** + API/event polling + маппинг на бизнес-статусы. Не конкурировать с «переход на ЭДО 2026» и не дублировать B22 (общий Apps Script) / B36 (банк).

---

## SERP (WebSearch Cursor, 06.08.2026)

| # | URL | Тип | Пробел / угол КОДА |
| --- | --- | --- | --- |
| 1 | https://eodoc.ru/statusy-dokumentov-v-edo-reglament-buhgalteriya-zakupki/ | workflow/reglament | Отличный словарь внешний/внутренний слой, но **нет Google Sheets и API** |
| 2 | https://developer.kontur.ru/docs/diadoc-api/instructions/statuses.html | API docs | Канон полей статусов (`RecipientResponseStatus`, `DocflowStatus`) — основа маршрута A |
| 3 | https://developer.kontur.ru/docs/diadoc-api/http/GetDocflowEvents_V4.html | API docs | Event-based polling — ключ к «без ручного мониторинга» |
| 4 | https://developer.kontur.ru/docs/diadoc-api/http/GetDocuments_V4.html | API docs | Альтернатива: фильтр + пагинация 100 документов |
| 5 | https://tochka.com/knowledge/edo/statusy-v-edo/ | explainer | Что значат статусы в UI — для таблицы маппинга |
| 6 | https://companies.rbc.ru/news/rX31PQj7rE/elektronnyij-dokumentooborot-v-2025-2026-godah-chto-izmenitsya-dlya-biznesa/ | news 2026 | Контекст УПД 5.03 — 1 абзац, не ядро статьи |
| 7 | https://www.glavbukh.ru/art/101730-perehod-na-edo-s-chego-nachat-soglashenie-kak-otpravit-i-prinyat-priglashenie | how_to EDO | Переход на ЭДО — другой intent |
| 8 | https://forpes.ru/post/182580 | case study | GetDocflowEvents эффективнее опроса всей очереди в БД |
| 9 | https://flowu.ru/catalog/diadoc-counteragent-tracker | n8n template | Паттерн Diadoc→Sheets (контрагенты; переносим на статусы документов) |
| 10 | https://help.1forma.ru/domains/integrations/edo-smart-actions/ | integration | Синхронизация статусов Диадок — JSON вручную vs автоматизация |
| 11 | https://workspace.google.com/marketplace/app/api_connector/95804724197 | add-on | API Connector — маршрут «без кода» для малых объёмов |
| 12 | https://koda-fd.ru/blog/google-apps-script-finansist-obnovit-dannye/ | свой блог | internal: триггеры, Properties, меню «Обновить» |
| 13 | https://koda-fd.ru/blog/avtomatizaciya-finansov-no-code/ | свой блог | internal CTA no-code |

**Кannibalization:** B22 (Apps Script кнопка), B36 (банк→Sheets), B35 (n8n сверка) — перелинковка, не копировать H2 1:1.

**research-serp.json (шаг 0):** подтверждает доминирование новостей ЭДО-2026 по запросу «статусы эдо google sheets» — **игнорируем как нерелевантный SERP**; приоритет — WebSearch выше.

---

## Таблица фактов

| # | Утверждение | Источник | Дата проверки |
| --- | --- | --- | --- |
| 1 | В API Диадок статусы читаются из структур `Document` или `DocflowV3`/`DocflowV4`; ключевые поля: `SenderSignatureStatus`, `RecipientResponseStatus`, `DocflowStatus`, `RevocationStatus`. | https://developer.kontur.ru/docs/diadoc-api/instructions/statuses.html | 2026-08-06 |
| 2 | `GetDocflowEvents (V4)` возвращает события изменения документов; поддерживает пагинацию через `AfterIndexKey` и фильтр по времени (`TimeBasedFilter`). | https://developer.kontur.ru/docs/diadoc-api/http/GetDocflowEvents_V4.html | 2026-08-06 |
| 3 | Суммарный размер содержимого сущностей в ответе `GetDocflowEvents` не может превышать 1 048 576 байт — для реестра статусов запрашивать метаданные без тел документов. | https://developer.kontur.ru/docs/diadoc-api/http/GetDocflowEvents_V4.html | 2026-08-06 |
| 4 | `GetDocuments (V4)` возвращает не более 100 документов за запрос; при большем объёме — постранично через `AfterIndexKey` и `TotalCount`. | https://developer.kontur.ru/docs/diadoc-api/http/GetDocuments_V4.html | 2026-08-06 |
| 5 | Для интеграции с Диадок API нужны `client_id` из Кабинета интегратора и `access_token` в заголовке `Authorization: Bearer`. | https://developer.kontur.ru/docs/diadoc-api/howtostart/integration.html | 2026-08-06 |
| 6 | Коды ответа API: 401 (нет/неверный токен), 402 (закончилась подписка на API), 403 (нет прав к ящику). | https://developer.kontur.ru/docs/diadoc-api/http/GetDocflowEvents_V4.html | 2026-08-06 |
| 7 | `RecipientResponseStatus = WaitingForRecipientSignature` — документ в ожидании ответной подписи контрагента (типовой «висяк» для мониторинга). | https://developer.kontur.ru/doc/diadoc-api/http/GetDocuments.html | 2026-08-06 |
| 8 | Event-based опрос (`GetDocflowEvents`) эффективнее периодического опроса всей таблицы документов в БД — рекомендация из практики интеграции. | https://forpes.ru/post/182580 | 2026-08-06 |
| 9 | Регламент: разделить внешние статусы обмена и внутреннюю «готовность к оплате»; «подписано» ≠ «можно платить» без внутренних проверок. | https://eodoc.ru/statusy-dokumentov-v-edo-reglament-buhgalteriya-zakupki/ | 2026-08-06 |
| 10 | Рекомендуется не более 5–7 статусов в словаре; формулировки вроде «подписано обеими сторонами» и «подписано нами, ждём контрагента» должны быть разными. | https://eodoc.ru/statusy-dokumentov-v-edo-reglament-buhgalteriya-zakupki/ | 2026-08-06 |
| 11 | С 1 января 2026 для организаций на ЭДО обязателен формат УПД 5.03; электронные ТОРГ-12 и акты по приказам № 551/552 через операторов не ходят. | https://www.glavbukh.ru/art/101730-perehod-na-edo-s-chego-nachat-soglashenie-kak-otpravit-i-prinyat-priglashenie | 2026-08-06 |
| 12 | В 2026 идёт движение к универсальным сообщениям (УС), унифицирующим сценарии обмена; оператор должен поддерживать актуальные форматы. | https://diadoc.com/blog/novoe-v-edo-v-2026-godu-universalnye-soobscheniya-format-ukd-i-vlozheniya | 2026-08-06 |
| 13 | Google Sheets API — REST-интерфейс для чтения/записи ячеек; сам по себе не знает статусов ЭДО, нужен коннектор к API оператора. | https://developers.google.com/workspace/sheets/api/guides/concepts | 2026-08-06 |
| 14 | UrlFetchApp: 20 000 вызовов/день (consumer), 100 000/день (Google Workspace); runtime скрипта до 6 минут за запуск. | https://developers.google.com/apps-script/guides/services/quotas | 2026-08-06 |
| 15 | Лимит installable triggers: 20 на пользователя на скрипт; trigger total runtime 90 min/день (consumer). | https://developers.google.com/apps-script/guides/services/quotas | 2026-08-06 |
| 16 | n8n Google Sheets node поддерживает Append/Update Row; для upsert — search then update/create (паттерн idempotency). | https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.googlesheets/ | 2026-08-06 |
| 17 | Шаблон n8n «Diadoc + Google Sheets» логирует события в таблицу и маршрутизирует по типу (accept/reject/invite) — переносимый паттерн для статусов документов. | https://flowu.ru/catalog/diadoc-counteragent-tracker | 2026-08-06 |
| 18 | Синхронизация статусов Диадок в 1Forma возвращает JSON, который нужно разбирать и сравнивать с локальным реестром — аналог задачи Sheets-реестра. | https://help.1forma.ru/domains/integrations/edo-smart-actions/ | 2026-08-06 |
| 19 | API Connector (Marketplace) позволяет GET/POST к внешнему API из Sheets; free tier ~100 запросов/мес — только для прототипа. | https://workspace.google.com/marketplace/app/api_connector/95804724197 | 2026-08-06 |
| 20 | Типовой набор статусов оператора (пример ЭДО.МИГ24): Sent, AwaitClientSign, Signed, Rejected, Cancelled, Received и др. — для таблицы маппинга. | https://edo.mig24.ru/help/api | 2026-08-06 |

---

## FAQ hints (кандидаты)

1. **Можно ли без программиста?** — CSV-импорт + Apps Script по шаблону: да; API Диадок: нужна однократная регистрация интеграции; n8n — без кода, но настройка OAuth.
2. **Сколько займёт внедрение?** — Staging + полуавтомат CSV: один вечер; GetDocflowEvents + trigger: 1–3 дня с тестами.
3. **Какие риски для данных?** — токены API, облако Google, не слать реестр с ИНН в LLM; см. internal `/obezlichivanie-dannyh-chatgpt-finansist/`.
4. **Работает ли со СБИС / другим оператором?** — логика та же (API статусов + Sheets); в статье основной пример Диадок как наиболее документированный API.
5. **Чем отличается от модуля 1С?** — Sheets как лёгкий дашборд для финдира/закупок без доработки 1С; не замена учётной системы.
6. **Как не перепутать «подписано нами» и «подписано обеими»?** — отдельные строки `business_status` + правило в регламенте (факт #9–10).
7. **Что если API вернул 402?** — проверить подписку на API у оператора; fallback на ручной экспорт до продления.
8. **Make или n8n?** — оба через HTTP Request; n8n удобнее self-hosted; Apps Script — нулевая инфра (ссылка `/avtomatizaciya-finansov-no-code/`).

---

## Writer notes

- **author_id:** olga-kondratskaya  
- **article_mode:** B — минимум 5 нумерованных шагов + таблица сравнения маршрутов (Apps Script API / n8n / CSV semi-auto) + таблица маппинга API→business status.  
- **CTA:** клуб KODA ≤2, Telegram ≤2; UTM `?utm_source=blog&utm_medium=article&utm_campaign=statusy-edo-google-sheets`  
- **Не обещать:** юридическую силу статуса в Sheets (источник истины — оператор ЭДО); работу всех операторов из коробки; замену бухгалтерской проверки.  
- **H2 из карточки** заменить на блоки из action_outline (scout-шаблон).  
- **Код:** фрагменты Apps Script (`fetchDocflowEvents_`, `mapStatus_`, `upsertRow_`, `installHourlyTrigger`) — без реальных токенов.  
- **Кontекст 2026:** 1 короткий блок про УПД 5.03 (факт #11), не уводить статью в новости.  
- **Перелинковка:** B22 (триггеры/Properties), B36 (staging-паттерн), internal links из карточки.

---

## Cover hint

abstract holographic finance automation dark #0a0a0f purple #8b5cf6, no text

---

## Готовность к writer

| Критерий | Статус |
| --- | --- |
| Utility gate темы | PASS |
| SERP ≥ 3 конкурента | ✅ (13 URL) |
| Wordstat MCP | ⚠️ сервер недоступен |
| Таблица фактов с URL | ✅ (20 фактов) |
| utility_verdict + action_outline | ✅ (9 шагов) |
| FAQ 5–7 | ✅ (8) |

**Writer:** готов. Вход: этот файл + `research-context.json` + карточка B46 + `site-brief.md`.

---

=== EXCALIBUR BLOG RESEARCH ===
topic_id: B46
article_dir: memory/blog/articles/B46-statusy-edo-google-sheets
status: ✅ PASS
utility_verdict: PASS
reader_outcome: Реестр статусов ЭДО в Google Sheets с автообновлением через API (GetDocflowEvents) или n8n, маппинг на бизнес-статусы, без ежедневного мониторинга кабинета.
summary: SERP без прямого конкурента по primary query; доминируют новости ЭДО-2026 и регламенты статусов. Угол КОДА — Sheets-дашборд + 3 маршрута (Apps Script / n8n / CSV). Wordstat недоступен (MCP user-mcp-kv). 20 фактов с URL, 9 шагов action_outline, 8 FAQ. Internal: avtomatizaciya-finansov-no-code, obezlichivanie-dannyh-chatgpt-finansist. Готов к writer.
===
