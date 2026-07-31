# Blog topics — KODA / Excalibur BLOG

Формат карточек. **Utility-only:** `shared/editorial-utility-only.md`.

**Разрешённые `search_intent`:** `how_to`, `checklist`, `comparison`, `troubleshooting`, `workflow`, `parent_guide`  
**`article_mode`:** только **B**.

Перед research:

```bash
python scripts/excalibur_blog_utility_gate.py --topic-id B13
```

**Уже на блоге (не дублировать slug):** vibe-coding-finansist, avtomatizaciya-finansov-no-code, cursor-ai-agenty-finotchetnost, ot-excel-k-fin-konturu-30-dney, finansovyj-minimalizm, disnejlend-dlya-dannyh, ubijstvo-svyashchennoj-korovy, claude-code-finotdel, obezlichivanie-dannyh-chatgpt-finansist

**Очередь 2026-07 (согласовано):** B13–B23 — опубликованы.  
**Очередь 2026-07+ (scout):** B24–B26 — n8n/Make + локальные LLM для финотдела.

---

## B13 — Выгрузка из 1С в Excel через OData

- **priority:** P0
- **slug:** vygruzka-1c-excel-odata
- **h1:** Как выгрузить данные из 1С в Excel через OData: пошагово без программиста
- **primary_query:** выгрузка из 1с в excel
- **secondary_queries:** odata 1с, выгрузка 1с в google sheets, odata standard.odata финансы
- **search_intent:** how_to
- **article_mode:** B
- **author_id:** olga-kondratskaya
- **source_notes:** `D:\projects\1С\dds-sheets` (OData URL, credentials в Apps Script, refreshFrom1C)
- **h2_outline:**
  1. Когда хватает OData, а когда нужен программист 1С
  2. Публикация базы и URL `…/odata/standard.odata`
  3. Выгрузка в Excel / CSV: запрос, фильтр, лимиты
  4. Связка с Google Sheets: кнопка «Обновить из 1С»
  5. Безопасность: отдельный пользователь, права, что не тащить в облако
- **faq_hints:** работает ли odata на унф; нужен ли https; чем отличается от обычной выгрузки excel; можно ли без iis
- **internal_links:** /ot-excel-k-fin-konturu-30-dney/, /obezlichivanie-dannyh-chatgpt-finansist/
- **cover_scene_hint:** abstract holographic data flow dark #0a0a0f purple #8b5cf6 blue #93c5fd, no text on image

---

## B14 — Управление дебиторкой: реестр + напоминания

- **priority:** P0
- **slug:** upravlenie-debitorkoj-reestr-napominaniya
- **h1:** Как настроить управление дебиторкой: реестр просрочки + автоматические напоминания контрагентам
- **primary_query:** как управлять дебиторской задолженностью
- **secondary_queries:** контроль дебиторки, напоминание об оплате контрагенту, реестр просроченной дебиторки
- **search_intent:** workflow
- **article_mode:** B
- **author_id:** olga-kondratskaya
- **h2_outline:**
  1. Минимальный реестр дебиторки: какие колонки обязательны
  2. Статусы и правила просрочки без CRM
  3. Автонапоминания: Google Sheets / Excel → n8n → Telegram/email
  4. Что писать контрагенту: шаблоны без давления и без юррисков
  5. Контроль эффекта: кто ответил, кто оплатил, что эскалировать
- **faq_hints:** можно ли без 1с; как не спамить клиентов; сколько раз напоминать; нужна ли эцп
- **internal_links:** /avtomatizaciya-finansov-no-code/, /ot-excel-k-fin-konturu-30-dney/
- **cover_scene_hint:** abstract holographic network nodes purple blue dark background, no text

---

## B15 — Ollama для финотдела

- **priority:** P0
- **slug:** ollama-finotdel-lokalnaya-nejroset
- **h1:** Как поставить Ollama для финотдела: локальная нейросеть под выгрузки 1С без облака
- **primary_query:** как установить ollama
- **secondary_queries:** локальная нейросеть, ollama для бизнеса, локальная llm финансы
- **search_intent:** how_to
- **article_mode:** B
- **author_id:** olga-kondratskaya
- **h2_outline:**
  1. Зачем финотделу локальная модель вместо ChatGPT
  2. Установка Ollama и выбор модели (Llama / Qwen) под железо
  3. Сценарии: сверка CSV, категоризация ДДС, черновик пояснений
  4. Ограничения: галлюцинации цифр и обязательная ручная проверка
  5. Связка с Cursor / скриптами и политика «сырое 1С не в облако»
- **faq_hints:** какая видеокарта нужна; можно ли на cpu; бесплатно ли; чем хуже chatgpt
- **internal_links:** /obezlichivanie-dannyh-chatgpt-finansist/, /claude-code-finotdel/
- **cover_scene_hint:** abstract local server glow nodes dark mesh purple blue, no text

---

## B16 — База знаний для ChatGPT и Cursor

- **priority:** P0
- **slug:** baza-znaniy-chatgpt-cursor-finotdel
- **h1:** Как сделать базу знаний для ChatGPT и Cursor: свои регламенты без утечки 1С
- **primary_query:** как сделать базу знаний chatgpt
- **secondary_queries:** свои документы в нейросеть, knowledge base cursor, загрузить регламенты в chatgpt
- **search_intent:** how_to
- **article_mode:** B
- **author_id:** olga-kondratskaya
- **h2_outline:**
  1. Что класть в базу знаний финотдела, а что нельзя
  2. Структура папок: регламенты, шаблоны писем, словарь статей ДДС
  3. Подключение в Cursor (@docs / rules) и в ChatGPT (файлы / projects)
  4. Обезличивание и запрет сырых выгрузок в индекс
  5. Проверка: 10 тестовых вопросов и ловля галлюцинаций
- **faq_hints:** отличается ли от custom gpt; можно ли на локальной модели; как обновлять базу
- **internal_links:** /obezlichivanie-dannyh-chatgpt-finansist/, /cursor-ai-agenty-finotchetnost/
- **cover_scene_hint:** abstract glowing document nodes network dark purple blue, no text

---

## B17 — Нейросеть для Excel: формулы и сводные

- **priority:** P0
- **slug:** nejroset-excel-formuly-finansist
- **h1:** Как использовать нейросеть для Excel: ChatGPT пишет формулы, сводные и очистку выгрузок
- **primary_query:** как использовать нейросеть для excel
- **secondary_queries:** chatgpt формулы excel, chatgpt сводные таблицы, ai для excel финансист
- **search_intent:** how_to
- **article_mode:** B
- **author_id:** olga-kondratskaya
- **h2_outline:**
  1. Какие задачи Excel реально отдать нейросети
  2. ChatGPT vs Claude для длинных выгрузок и формул
  3. 10 рабочих промптов: СУММЕСЛИМН, ВПР/XLOOKUP, сводная, дубли, текст по столбцам
  4. Как проверять формулы, чтобы не поймать галлюцинацию в сумме
  5. Когда пора уходить из «просто Excel» в скрипт или staging
- **faq_hints:** можно ли загружать выгрузку 1с; бесплатный тариф хватит ли; excel copilot vs chatgpt
- **internal_links:** /ot-excel-k-fin-konturu-30-dney/, /vibe-coding-finansist/
- **cover_scene_hint:** abstract spreadsheet grid glow holographic dark purple, no text

---

## B18 — Счёт из 1С:УНФ с телефона

- **priority:** P0
- **slug:** schet-1c-unf-telefon-http-servis
- **h1:** Как выставить счёт из 1С:УНФ с телефона: HTTP-сервис + Telegram/PWA
- **primary_query:** выставить счет в 1с
- **secondary_queries:** интеграция 1с telegram, http сервис 1с унф, счет на оплату с телефона
- **search_intent:** how_to
- **article_mode:** B
- **author_id:** olga-kondratskaya
- **source_notes:** `D:\projects\1С\pilot-unf` (расширение InvoiceBot, FastAPI, PWA, bot)
- **h2_outline:**
  1. Задача: счёт клиенту без ожидания бухгалтера
  2. Архитектура: PWA/Telegram → бэкенд → HTTP-сервис УНФ → PDF
  3. Установка расширения InvoiceBot и публикация HTTP-сервиса
  4. Запуск PWA/бота: код доступа, контрагент, НДС, проведение
  5. Ограничения пилота и безопасность (отдельный пользователь, права)
- **faq_hints:** работает ли на унф 1.6 и 3.0; нужен ли программист 1с; можно ли только telegram без pwa
- **internal_links:** /avtomatizaciya-finansov-no-code/, /vygruzka-1c-excel-odata/
- **cover_scene_hint:** abstract phone-to-server data nodes holographic dark purple blue, no text

---

## B19 — Python для финансиста: сверка CSV

- **priority:** P0
- **slug:** python-finansist-sverka-csv
- **h1:** Как начать с Python для финансиста: сверка двух CSV без зависания Excel
- **primary_query:** как начать python для финансиста
- **secondary_queries:** сверка csv python, pandas сверка таблиц, python excel финансы
- **search_intent:** how_to
- **article_mode:** B
- **author_id:** olga-kondratskaya
- **h2_outline:**
  1. Когда Excel уже не тянет две выгрузки
  2. Установка Python и первый запуск скрипта в Cursor
  3. Сверка двух CSV: ключ, суммы, отчёт расхождений
  4. Типичные ошибки: кодировка, разделитель, типы чисел
  5. Куда расти: папка проекта, повторный запуск, Ollama/Claude Code
- **faq_hints:** нужно ли знать программирование; pandas обязателен ли; безопасно ли для 1с-файлов
- **internal_links:** /claude-code-finotdel/, /vibe-coding-finansist/
- **cover_scene_hint:** abstract dual data streams merging nodes dark purple cyan, no text

---

## B20 — Cursor для финансиста: скрипт и дашборд

- **priority:** P0
- **slug:** cursor-finansist-skript-dashbord
- **h1:** Cursor для финансиста: как за вечер собрать скрипт сверки и маленький дашборд
- **primary_query:** cursor ai
- **secondary_queries:** cursor для начинающих, cursor финансист, vibe coding cursor дашборд
- **search_intent:** how_to
- **article_mode:** B
- **author_id:** olga-kondratskaya
- **h2_outline:**
  1. Чем Cursor отличается от чата ChatGPT для рабочих файлов
  2. Подготовка папки проекта: CSV, `.gitignore`, запрет сырых ПДн
  3. Сценарий 1: скрипт сверки двух выгрузок
  4. Сценарий 2: маленький дашборд (Streamlit / простой HTML) из той же папки
  5. Как итерировать промптами и не утонуть в «перепиши всё»
- **faq_hints:** платный ли cursor; нужен ли git; чем отличается от статьи про ai-агентов финотчётности
- **internal_links:** /cursor-ai-agenty-finotchetnost/, /vibe-coding-finansist/, /claude-code-finotdel/
- **cover_scene_hint:** abstract code-path light trails holographic dark purple, no text

---

## B21 — MCP в Cursor для финансиста

- **priority:** P0
- **slug:** mcp-cursor-finansist-instrumenty
- **h1:** MCP в Cursor: как подключить инструменты и перестать копировать CSV руками
- **primary_query:** mcp cursor
- **secondary_queries:** model context protocol cursor, mcp сервер для начинающих, подключить mcp cursor
- **search_intent:** how_to
- **article_mode:** B
- **author_id:** olga-kondratskaya
- **h2_outline:**
  1. MCP простыми словами: зачем это финансисту, а не только разработчику
  2. Что подключать первым: файлы, браузер, таблицы — без «магии 1С»
  3. Пошагово: установить MCP в Cursor и проверить вызов инструмента
  4. Рабочий сценарий: агент читает папку выгрузок и собирает отчёт
  5. Риски: права доступа, секреты в `.env`, что нельзя отдавать серверу
- **faq_hints:** mcp это доступ к 1с напрямую; бесплатно ли; чем лучше просто прикрепить файл
- **internal_links:** /cursor-finansist-skript-dashbord/, /cursor-ai-agenty-finotchetnost/
- **cover_scene_hint:** abstract tool nodes connected mesh holographic dark purple blue, no text

---

## B22 — Google Apps Script для финансиста

- **priority:** P1
- **slug:** google-apps-script-finansist-obnovit-dannye
- **h1:** Как сделать кнопку «обновить данные» в Google Sheets через Apps Script
- **primary_query:** как сделать google apps script кнопку
- **secondary_queries:** google таблицы скрипт кнопка, apps script финансы, обновить данные google sheets
- **search_intent:** how_to
- **article_mode:** B
- **author_id:** olga-kondratskaya
- **source_notes:** `D:\projects\1С\dds-sheets\html-dashboard` (Code.gs, refreshFrom1C, webapp)
- **h2_outline:**
  1. Зачем кнопка в таблице, если есть ручной импорт CSV
  2. Первый скрипт: меню и функция «Обновить»
  3. Откуда брать данные: CSV с Диска, webhook, OData 1С
  4. Дашборд поверх листа: HTML-сервис без отдельного сайта
  5. Права, триггеры по времени и типичные поломки развёртывания
- **faq_hints:** можно ли без javascript знаний; безопасно ли хранить пароль 1с; лимиты google
- **internal_links:** /vygruzka-1c-excel-odata/, /avtomatizaciya-finansov-no-code/
- **cover_scene_hint:** abstract sheet grid with refresh pulse nodes dark purple, no text

---

## B23 — Cursor Rules для финотдела

- **priority:** P1
- **slug:** cursor-rules-finotdel
- **h1:** Как настроить Cursor Rules для финотдела: стиль кода, папки и запрет сырых выгрузок 1С
- **primary_query:** как настроить cursor rules
- **secondary_queries:** agents.md cursor, .cursorrules финансы, правила cursor для команды
- **search_intent:** how_to
- **article_mode:** B
- **author_id:** olga-kondratskaya
- **h2_outline:**
  1. Зачем rules, если «и так понятно из чата»
  2. Минимальный набор правил финотдела: папки, CSV, запрет ПДн
  3. Пример `AGENTS.md` / rules: стек, стиль, Definition of Done
  4. Как связать rules с базой знаний и MCP
  5. Внедрение в команду: один шаблон на всех, без культа сложности
- **faq_hints:** rules работают в free тарифе; чем отличается от system prompt; нужно ли для одного человека
- **internal_links:** /baza-znaniy-chatgpt-cursor-finotdel/, /cursor-finansist-skript-dashbord/, /obezlichivanie-dannyh-chatgpt-finansist/
- **cover_scene_hint:** abstract rule-grid nodes locked paths holographic dark purple, no text

---

## B24 — n8n для финотдела: установка и первый workflow

- **priority:** P0
- **slug:** n8n-finotdel-ustanovka-pervyj-workflow
- **h1:** Как установить n8n для финотдела: Docker, HTTPS и первый workflow Sheets → Telegram
- **primary_query:** как установить n8n
- **secondary_queries:** n8n docker, n8n self-hosted, n8n google sheets telegram, автоматизация n8n финансы
- **search_intent:** how_to
- **article_mode:** B
- **author_id:** olga-kondratskaya
- **source_notes:** Wordstat MCP `user-mcp-kv` недоступен в сессии scout 2026-07-31; спрос подтверждён трендами 2026 (n8n AI nodes / self-host) и нишей site-brief (кластер n8n/Make). Цифры показов не выдуманы.
- **h2_outline:**
  1. Зачем финотделу свой n8n, а не только ручные выгрузки
  2. Cloud vs self-hosted: что выбрать под выписки и 152-ФЗ
  3. Установка: Docker Compose, домен, HTTPS, WEBHOOK_URL
  4. Первый workflow: Google Sheets (строка ДДС/реестра) → фильтр → Telegram-дайджест
  5. Чек-лист безопасности: секреты, права Google, что не слать в облако
- **faq_hints:** нужен ли vps; чем отличается от make; хватит ли без ssl; можно ли только локально на ноутбуке
- **internal_links:** /upravlenie-debitorkoj-reestr-napominaniya/, /avtomatizaciya-finansov-no-code/, /obezlichivanie-dannyh-chatgpt-finansist/
- **cover_scene_hint:** abstract workflow nodes pipeline holographic dark purple blue, no text

---

## B25 — n8n или Make для финотдела

- **priority:** P0
- **slug:** n8n-ili-make-finotdel
- **h1:** Как выбрать n8n или Make для финотдела: сравнение под выписки, объём и 152-ФЗ
- **primary_query:** n8n или make
- **secondary_queries:** n8n vs make, make.com или n8n, сравнение n8n make zapier, какая автоматизация для финансов
- **search_intent:** comparison
- **article_mode:** B
- **author_id:** olga-kondratskaya
- **source_notes:** Wordstat MCP недоступен; угол из трендов 2026 (n8n vs Make B2B) + требования финотдела к данным. Цифры показов не выдуманы.
- **h2_outline:**
  1. Критерии выбора для финансиста: данные, объём операций, кто будет чинить сценарий
  2. Таблица сравнения: цена, self-host, интеграции, AI-ноды, риск блокировок
  3. Когда хватает Make: быстрый старт без сервера
  4. Когда брать n8n: выписки, ПДн, 100K+ операций, локальные LLM
  5. Практичный гибрид: Make для внешних сервисов, n8n для чувствительного контура
- **faq_hints:** можно ли мигрировать сценарии; нужен ли программист для n8n; подходит ли zapier из рф
- **internal_links:** /avtomatizaciya-finansov-no-code/, /n8n-finotdel-ustanovka-pervyj-workflow/, /ollama-finotdel-lokalnaya-nejroset/
- **cover_scene_hint:** abstract two path fork nodes holographic dark purple cyan, no text

---

## B26 — n8n + Ollama: локальная категоризация ДДС

- **priority:** P0
- **slug:** n8n-ollama-kategorizaciya-dds
- **h1:** Как связать n8n с Ollama: локальная категоризация ДДС без отправки выписок в облако
- **primary_query:** как связать n8n с ollama
- **secondary_queries:** n8n ollama, локальная llm в n8n, категоризация ддс нейросеть, n8n http ollama api
- **search_intent:** workflow
- **article_mode:** B
- **author_id:** olga-kondratskaya
- **source_notes:** Wordstat MCP недоступен; связка n8n↔Ollama — горячий utility-хвост к B15 без дубля установки Ollama. Цифры показов не выдуманы.
- **h2_outline:**
  1. Зачем гонять ДДС через локальную модель, а не через ChatGPT API
  2. Подготовка: Ollama уже стоит, модель для классификации, endpoint `/v1/chat/completions`
  3. Workflow в n8n: триггер по строке Sheets → HTTP к Ollama → парсинг JSON → запись категории
  4. Промпт и словарь статей: как снизить галлюцинации по суммам
  5. Docker-сеть, host.docker.internal и чек-лист перед продом
- **faq_hints:** работает ли из n8n cloud; какая модель лучше для классификации; нужно ли gpu
- **internal_links:** /ollama-finotdel-lokalnaya-nejroset/, /n8n-finotdel-ustanovka-pervyj-workflow/, /nejroset-excel-formuly-finansist/
- **cover_scene_hint:** abstract local llm node linked to workflow mesh dark purple blue, no text

---

## Архив очереди (не в работе)

Старые карточки B01–B03, B05–B10, B12 сняты с активной очереди после согласования 2026-07.  
Опубликованные **B04** (`claude-code-finotdel`) и **B11** (`obezlichivanie-dannyh-chatgpt-finansist`) — только в `shared/published-articles.md`.
