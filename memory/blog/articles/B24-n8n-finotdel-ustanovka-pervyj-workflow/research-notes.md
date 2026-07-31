# Research notes — B24

**topic_id:** B24  
**slug:** n8n-finotdel-ustanovka-pervyj-workflow  
**h1:** Как установить n8n для финотдела: Docker, HTTPS и первый workflow Sheets → Telegram  
**research_date:** 2026-07-31  
**freshness_window:** prefer_sources_after_2026-07-01 (контекст research_start: после 2026-05-02)  
**utility_gate (topic):** PASS (`how_to`, mode B) — подтверждено `excalibur_blog_utility_gate.py --topic-id B24`  
**practice_angle:** финотдел ставит self-hosted n8n (Docker + HTTPS), собирает Sheets → Telegram-дайджест, соблюдает контур 152-ФЗ / секреты

---

## utility_verdict

**PASS** — how-to: выбрать Cloud vs self-hosted под выписки/ПДн, поднять n8n на Docker Compose с доменом и HTTPS, задать `WEBHOOK_URL`, собрать первый workflow Google Sheets → фильтр → Telegram, пройти чек-лист безопасности.

---

## reader_outcome

Финансист за вечер поднимает свой n8n за HTTPS, подключает Google Sheets и Telegram-бота и получает рабочий дайджест по новой строке реестра/ДДС – без передачи сырых выписок на чужой SaaS-контур.

---

## action_outline

1. Решить контур: n8n Cloud vs self-hosted (данные выписок, 152-ФЗ, кто администрирует VPS).
2. Подготовить VPS/сервер: Docker Engine + Compose, домен с A-записью, открыты 80/443.
3. Развернуть официальный стек: `.env` + `compose.yaml` (Traefik + `docker.n8n.io/n8nio/n8n`), `N8N_PROTOCOL=https`, `WEBHOOK_URL=https://…/`.
4. Войти в редактор по `https://n8n.ваш-домен`, создать owner-аккаунт, зафиксировать timezone `Europe/Moscow`.
5. Подключить Google Sheets: Custom OAuth2 (Cloud Console → Sheets + Drive API → redirect URI из n8n).
6. Создать Telegram-бота через BotFather, сохранить Access Token в credentials n8n, узнать chat_id.
7. Собрать workflow: Google Sheets Trigger (Row added) → IF/Filter (нужные строки) → Telegram Send Message (дайджест без лишних ПДн).
8. Прогнать тест на тестовой таблице, включить workflow Active, проверить логи execution.
9. Чек-лист безопасности: volume/бэкап, `N8N_ENCRYPTION_KEY`, порт 5678 только localhost, что не слать в Telegram/облако.

---

## Яндекс Wordstat

⚠️ **WORDSTAT OFFLINE / AUTH WARNING:** MCP-сервер `user-mcp-kv` недоступен в Cloud (нет в каталоге MCP). Точные показы за этот прогон **не получены и не выдуманы**.  
OAuth (когда KV снова онлайн): https://oauth.yandex.ru/authorize?response_type=token&client_id=c654b948515a4a07a4c89648a0831d40

**Исторический ориентир (не текущий API):** research B02 от 11.06.2026 фиксировал через Wordstat: `n8n` ~37k, `n8n docker` ~498, `n8n установка` ~364, `автоматизация n8n` ~539. Использовать только как порядок спроса; в статью цифры показов **не вставлять**, пока нет свежего ответа API.

**LSI / семантика для writer (из SERP + карточки темы, без объёмов):**

- как установить n8n, n8n docker, n8n docker compose, n8n self-hosted, n8n vps
- n8n https / ssl / traefik / nginx, WEBHOOK_URL, N8N_HOST
- n8n google sheets, n8n telegram, sheets → telegram
- автоматизация n8n финансы, дайджест собственнику, реестр ДДС
- n8n cloud vs self-hosted, 152-ФЗ, encryption key

---

## SERP (WebSearch Курсора, 31.07.2026)

Приоритет: официальные docs + актуальные гайды 2026. Сырой `research-serp.json` (DuckDuckGo) использован как черновик URL; конкурентный разбор – по WebSearch/WebFetch.

| # | URL | Тип | Сильные стороны | Слабые / пробелы | Что не копировать |
|---|-----|-----|-----------------|------------------|-------------------|
| 1 | [docs.n8n.io … install-with-docker](https://docs.n8n.io/deploy/host-n8n/install-options/install-with-docker) | Офиц. Docker | Канон: образ `docker.n8n.io/n8nio/n8n`, порт 5678, volume, stable 2.32.6 | Нет угла финотдела | Сухой перевод без сценария ДДС |
| 2 | [docs.n8n.io … use-docker-compose](https://docs.n8n.io/deploy/host-n8n/install-options/use-a-cloud-provider/use-docker-compose) | Офиц. Compose+Traefik | DNS A-запись, `.env`, HTTPS-only, `WEBHOOK_URL`, bind `127.0.0.1:5678` | Нет Sheets/Telegram | Полный yaml 1:1 без объяснения «зачем» |
| 3 | [docs.n8n.io Google OAuth](https://docs.n8n.io/integrations/builtin/credentials/google/oauth-single-service/) | Офиц. credentials | Self-host = Custom OAuth2; Drive API нужен для Sheets; localhost callback ок для дев | Не про финансы | Длинный troubleshooting Google без кейса |
| 4 | [docs.n8n.io Telegram credentials](https://docs.n8n.io/integrations/builtin/credentials/telegram/) | Офиц. Telegram | BotFather `/newbot`, Access Token | Нет chat_id/дайджеста | – |
| 5 | [docs.n8n.io Google Sheets Trigger](https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.googlesheetstrigger/) | Офиц. trigger | Events: Row added / updated / both | Polling-детали в common issues | – |
| 6 | [n8n.io/pricing](https://n8n.io/pricing/) | Офиц. цены | Starter 20€, Pro 50€, Business 667€ (annually); Community на GitHub; execution = полный прогон | Не how-to установки | Продавать Cloud вместо self-host без контекста 152-ФЗ |
| 7 | [ssdnodes … self-host-n8n-vps-docker-https](https://www.ssdnodes.com/learn/lang/ru/self-host-n8n-vps-docker-https) | RU гайд 2026 | `N8N_PROXY_HOPS=1`, 5678 только localhost, WebSocket headers | Хостинг-маркетинг | Цены VPS провайдера |
| 8 | [cloud.servermall.ru … n8n docker compose](https://cloud.servermall.ru/blog/kak-ustanovit-n8n-na-vps-docker-compose-domen-ssl-i-postgresql/) | RU longread | PostgreSQL, бэкапы, firewall, чек-лист прода | Общий DevOps | Агентский CTA «под ключ» |
| 9 | [saramudvlad.ru … n8n-na-vps-2026](https://saramudvlad.ru/articles/kak-ustanovit-n8n-na-vps-2026/) | RU how-to 2026 | Docker + SSL на русском | Мало про финотдел/ПДн | Структура 1:1 |
| 10 | [habr.com/ru/articles/962852](https://habr.com/ru/articles/962852/) | Habr ч.1 | Знакомство + установка для новичков | Не Sheets→Telegram finance | Общий онбординг |
| 11 | [n8n.io integrations Sheets+Telegram](https://n8n.io/integrations/google-sheets/and/telegram/) | Каталог | Подтверждает связку как типовой паттерн | Шаблоны не про ДДС | Чужие шаблоны «задачи/CRM» |

**Паттерн SERP:** топ по «как установить n8n» – VPS + Docker + SSL на русском; англ. кластер – self-hosted Docker 2026. Официальный канон: Traefik Compose. Почти никто не заходит с угла **финотдела + 152-ФЗ + первый дайджест Sheets→Telegram**.

**Пробел КОДА (уникальный угол):**

1. Cloud vs self-hosted именно под выписки/реестры/ПДн (не «для маркетолога»).
2. Первый workflow = строка ДДС/реестра → Telegram-дайджест собственнику/финменеджеру.
3. Чек-лист: что можно слать в Telegram, что держать только на своём n8n, связь с B14 (дебиторка) и B15/B26 (локальные LLM).

**Cannibalization note:** на koda-fd.ru нет статьи про установку n8n. Legacy `/avtomatizaciya-finansov-no-code/` – про no-code в целом; B02 в memory – AI-агенты в n8n (другой intent). B25 (n8n vs Make) и B26 (n8n+Ollama) – соседние spoke; B24 = hub «поставить n8n».

---

## Таблица фактов (цифры/утверждения только с URL)

| # | Факт | Источник | Дата проверки | В текст |
|---|------|----------|---------------|---------|
| 1 | n8n рекомендует Docker для большинства self-host сценариев; образ `docker.n8n.io/n8nio/n8n`; порт UI по умолчанию `5678` | https://docs.n8n.io/deploy/host-n8n/install-options/install-with-docker | 2026-07-31 | да |
| 2 | На 31.07.2026 в docs указаны Current `stable`: **2.32.6**, `beta`: **2.33.2**; для прода – stable | тот же URL + Compose docs | 2026-07-31 | да (с оговоркой «на дату статьи») |
| 3 | Официальный Compose-стек: Traefik (Let's Encrypt) + n8n; доступ **только HTTPS**; `WEBHOOK_URL=https://${SUBDOMAIN}.${DOMAIN_NAME}/`; `N8N_PROTOCOL=https`; порт n8n `127.0.0.1:5678:5678` | https://docs.n8n.io/deploy/host-n8n/install-options/use-a-cloud-provider/use-docker-compose | 2026-07-31 | да |
| 4 | DNS: A-запись поддомена (напр. `n8n`) → IP сервера; `.env`: `DOMAIN_NAME`, `SUBDOMAIN`, `GENERIC_TIMEZONE`, `SSL_EMAIL` | тот же | 2026-07-31 | да |
| 5 | Self-host требует навыков серверов/контейнеров; новичкам docs рекомендуют n8n Cloud | Docker / Compose docs | 2026-07-31 | да |
| 6 | По умолчанию БД – SQLite в volume `/home/node/.n8n`; PostgreSQL поддерживается через `DB_TYPE=postgresdb` | Docker install docs | 2026-07-31 | да |
| 7 | Cloud pricing (annually): Starter **20€/мес** (2.5K executions), Pro **50€** (10K), Business **667€** (40K, self-hosted license); Community Edition – free self-host на GitHub | https://n8n.io/pricing/ | 2026-07-31 | да |
| 8 | Execution = один полный прогон workflow, не шаг; на Cloud trial Starter/Pro карта не нужна | https://n8n.io/pricing/ | 2026-07-31 | да |
| 9 | Cloud: данные на хостинге n8n в EU (Frankfurt); self-hosted – где разместите вы | https://n8n.io/pricing/ (FAQ) | 2026-07-31 | да (для аргумента 152-ФЗ / локализация) |
| 10 | Self-hosted Google: **Managed OAuth2 недоступен** – нужен Custom OAuth2 (Client ID/Secret); для Sheets также включают **Google Drive API** | https://docs.n8n.io/integrations/builtin/credentials/google/oauth-single-service/ | 2026-07-31 | да |
| 11 | OAuth redirect для локальной разработки: `http://localhost:5678/rest/oauth2-credential/callback`; для прода – HTTPS-домен инстанса; mismatch → `redirect_uri_mismatch` | тот же | 2026-07-31 | да |
| 12 | External app в Testing: токены/consent истекают через **7 дней** – нужно переподключать credential | тот же | 2026-07-31 | да |
| 13 | Telegram credential: Access Token от BotFather (`/newbot`); username бота должен оканчиваться на `bot` | https://docs.n8n.io/integrations/builtin/credentials/telegram/ | 2026-07-31 | да |
| 14 | Google Sheets Trigger events: Row added / Row updated / Row added or updated | https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.googlesheetstrigger/ | 2026-07-31 | да |
| 15 | Sheets Trigger работает через **polling** (у Google нет webhook на лист) – интервал настраивается в ноде | community + гайды 2026; docs описывают events | 2026-07-31 | да (без выдуманных «каждые N сек», если не из docs) |
| 16 | Практики прода: `N8N_ENCRYPTION_KEY`, `N8N_PROXY_HOPS=1` за reverse proxy, не светить 5678 в интернет | https://www.ssdnodes.com/learn/lang/ru/self-host-n8n-vps-docker-https ; n8n.spot env guide | 2026-07-31 | да |
| 17 | Обновление Compose: `docker compose pull` → `down` → `up -d` | Docker install docs | 2026-07-31 | да |
| 18 | Tunnel/`--tunnel` / cloudflared – только для локальной разработки, **не для прода** | Docker install docs | 2026-07-31 | да |

**Не утверждать в тексте без отдельной проверки:** точные тарифы VPS в рублях, «n8n бесплатен для любого коммерческого SaaS-реселла» (лицензия Sustainable Use – внутреннее использование Community ок; реселл/hosting для третьих лиц – отдельный вопрос; отсылать к LICENSE/pricing, не давать юр. гарантий).

---

## Угол статьи (how-to для финотдела)

**Боль:** выписки и реестры в Sheets/Excel, дайджест собственнику руками в Telegram, страх отдавать банк.выписки в зарубежный Cloud.

**Ответ:** свой n8n на Docker + HTTPS; первый сценарий `Sheets (новая строка) → фильтр → Telegram`.

**Рекомендации writer:**

- H2 = подзадача + «делать / не делать».
- Схема: `VPS + Docker → HTTPS n8n → Sheets OAuth → BotFather → Trigger → Telegram`.
- Минимум 5 нумерованных шагов установки + отдельный блок workflow + чек-лист безопасности (10+ пунктов можно).
- Не дублировать B25 (полное сравнение с Make) – 1 короткий абзац + ссылка на будущий/related slug.
- CTA: t.me/finance_modern + club.koda-fd.ru (≤3); без salebot; без эмодзи; без длинного тире «—».

---

## FAQ-кандидаты

1. Нужен ли VPS или хватит ноутбука с Docker?  
2. Чем self-hosted n8n отличается от Make / n8n Cloud для финотдела?  
3. Можно ли работать без SSL / только по IP:порт?  
4. Почему OAuth Google не коннектится на self-hosted?  
5. Что писать в Telegram, чтобы не светить ПДн и полные выписки?  
6. Хватит ли SQLite или сразу нужен PostgreSQL?  
7. Как обновлять n8n без потери workflow?  
8. Можно ли потом подключить Ollama для категоризации ДДС? (мостик на B26/B15)

---

## Internal links / CTA

- Planned/related: `/upravlenie-debitorkoj-reestr-napominaniya/`, `/avtomatizaciya-finansov-no-code/`, `/obezlichivanie-dannyh-chatgpt-finansist/`, `/ollama-finotdel-lokalnaya-nejroset/`  
- Spoke в очереди: B25 `n8n-ili-make-finotdel`, B26 `n8n-ollama-kategorizaciya-dds`  
- CTA: https://t.me/finance_modern ; https://club.koda-fd.ru/  
- **no** @koda_salebot

---

## Sources checklist (минимум для writer)

- https://docs.n8n.io/deploy/host-n8n/install-options/install-with-docker  
- https://docs.n8n.io/deploy/host-n8n/install-options/use-a-cloud-provider/use-docker-compose  
- https://docs.n8n.io/integrations/builtin/credentials/google/oauth-single-service/  
- https://docs.n8n.io/integrations/builtin/credentials/telegram/  
- https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.googlesheetstrigger/  
- https://n8n.io/pricing/  
- https://n8n.io/integrations/google-sheets/and/telegram/  
- https://www.ssdnodes.com/learn/lang/ru/self-host-n8n-vps-docker-https  

---

## Handoff summary

- `utility_verdict: PASS`  
- Wordstat: **offline** (цифры не выдуманы)  
- Угол: Docker + HTTPS + Sheets→Telegram + security/152-ФЗ для финотдела  
- Готово к writer
