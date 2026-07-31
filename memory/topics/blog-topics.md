# Blog topics — KODA / Excalibur BLOG

Формат карточек. **Utility-only:** `shared/editorial-utility-only.md`.

**Разрешённые `search_intent`:** `how_to`, `checklist`, `comparison`, `troubleshooting`, `workflow`, `parent_guide`  
**`article_mode`:** только **B**.

Перед research:

```bash
python scripts/excalibur_blog_utility_gate.py --topic-id B13
```

**Уже на блоге (не дублировать slug):** vibe-coding-finansist, avtomatizaciya-finansov-no-code, cursor-ai-agenty-finotchetnost, ot-excel-k-fin-konturu-30-dney, finansovyj-minimalizm, disnejlend-dlya-dannyh, ubijstvo-svyashchennoj-korovy, claude-code-finotdel, obezlichivanie-dannyh-chatgpt-finansist, vygruzka-1c-excel-odata, upravlenie-debitorkoj-reestr-napominaniya, ollama-finotdel-lokalnaya-nejroset, baza-znaniy-chatgpt-cursor-finotdel, nejroset-excel-formuly-finansist, schet-1c-unf-telefon-http-servis, python-finansist-sverka-csv, cursor-finansist-skript-dashbord, mcp-cursor-finansist-instrumenty, google-apps-script-finansist-obnovit-dannye

**Очередь 2026-07 (согласовано):** B13–B23 — автоматизация + вайб-кодинг. Источник 1С: `D:\projects\1С` (`dds-sheets`, `pilot-unf`).  
**Очередь 2026-08 (дозаправка):** B24–B33 — финконтур, банк, n8n, Cursor, сверки.  
**Авто-Scout (GHA перед каждым tick):** если unpublished < 3 → `scripts/excalibur_blog_scout_ci.py` ищет свежие темы (DDG / Cursor Cloud) и дописывает карточки сюда.

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

## B24 — Платёжный календарь в Google Sheets + n8n

- **priority:** P0
- **slug:** platezhnyj-kalendar-google-sheets-n8n
- **h1:** Как собрать платёжный календарь в Google Sheets и напоминания через n8n
- **primary_query:** платёжный календарь google sheets
- **secondary_queries:** кассовый разрыв таблица, напоминание об оплате n8n, платёжный календарь без 1с
- **search_intent:** workflow
- **article_mode:** B
- **author_id:** olga-kondratskaya
- **h2_outline:**
  1. Минимальные колонки календаря: дата, контрагент, сумма, статус
  2. Как считать кассовый разрыв без тяжёлой ERP
  3. n8n: триггер по дате → Telegram/email ответственному
  4. Связка с банковской выпиской (staging, не прямая проводка)
  5. Что не обещать: автоплатёж без подписи и контроля
- **faq_hints:** можно ли без n8n; хватит ли Excel; как не задвоить платежи
- **internal_links:** /avtomatizaciya-finansov-no-code/, /upravlenie-debitorkoj-reestr-napominaniya/
- **cover_scene_hint:** abstract calendar nodes cashflow timeline dark purple blue, no text

---

## B25 — Банковская выписка в staging-таблицу

- **priority:** P0
- **slug:** bankovskaya-vypiska-staging-google-sheets
- **h1:** Как разложить банковскую выписку в staging-таблицу без ручного копипаста
- **primary_query:** банковская выписка в excel автоматически
- **secondary_queries:** загрузка выписки в google sheets, нормализация выписки 1с, staging таблица финансы
- **search_intent:** how_to
- **article_mode:** B
- **author_id:** olga-kondratskaya
- **h2_outline:**
  1. Зачем staging между банком и отчётом
  2. Формат колонок: дата, сумма, контрагент, назначение, hash
  3. Импорт CSV/Excel и типичные ловушки кодировки
  4. Дедуп и правило «не трогать сырой файл»
  5. Куда дальше: ДДС, сверка, дашборд
- **faq_hints:** подойдёт ли выписка из клиента-банка; как жить с несколькими счетами
- **internal_links:** /ot-excel-k-fin-konturu-30-dney/, /python-finansist-sverka-csv/
- **cover_scene_hint:** abstract bank data stream into table grid dark holographic, no text

---

## B26 — План-факт ДДС за вечер

- **priority:** P0
- **slug:** plan-fakt-dds-google-sheets
- **h1:** Как сделать план-факт ДДС в Google Sheets за один вечер
- **primary_query:** план факт ддс excel
- **secondary_queries:** план факт денежный поток, ддс google sheets, отклонение факта от плана
- **search_intent:** how_to
- **article_mode:** B
- **author_id:** olga-kondratskaya
- **h2_outline:**
  1. Что считать планом: недели vs месяцы
  2. Листы: План, Факт, Сводка отклонений
  3. Формулы SUMIFS / QUERY без VBA
  4. Правило категорий: один справочник на все листы
  5. Еженедельный ритуал обновления для CFO
- **faq_hints:** чем отличается от ОПиУ; можно ли без 1с
- **internal_links:** /finansovyj-minimalizm/, /ot-excel-k-fin-konturu-30-dney/
- **cover_scene_hint:** abstract plan vs fact bars holographic dark purple, no text

---

## B27 — Дайджест собственнику из Sheets

- **priority:** P0
- **slug:** daydzhest-sobstvenniku-n8n-telegram
- **h1:** Как собрать еженедельный дайджест собственнику из Google Sheets в Telegram
- **primary_query:** дайджест собственнику telegram
- **secondary_queries:** отчёт собственнику автоматически, n8n google sheets telegram, weekly finance digest
- **search_intent:** workflow
- **article_mode:** B
- **author_id:** olga-kondratskaya
- **h2_outline:**
  1. Какие 5–7 цифр реально читает собственник
  2. Лист «Дайджест»: формулы, не копипаст
  3. n8n: раз в неделю → сообщение в Telegram
  4. Текст без воды: факт / отклонение / вопрос
  5. Безопасность: не слать ПДн и полные выписки
- **faq_hints:** можно ли в MAX; нужен ли отдельный бот
- **internal_links:** /avtomatizaciya-finansov-no-code/, /platezhnyj-kalendar-google-sheets-n8n/
- **cover_scene_hint:** abstract message bubble finance metrics dark ui, no text

---

## B28 — Сверка банк ↔ 1С без ПДн в ChatGPT

- **priority:** P0
- **slug:** sverka-bank-1c-bez-pdn
- **h1:** Как сверить банк и 1С без отправки ПДн в ChatGPT
- **primary_query:** сверка банка и 1с
- **secondary_queries:** сверка выписки 1с, обезличить выписку для ии, сверка оборотов банк учет
- **search_intent:** checklist
- **article_mode:** B
- **author_id:** olga-kondratskaya
- **h2_outline:**
  1. Что сравниваем: обороты, остатки, «висяки»
  2. Маскирование ИНН/счетов до любой нейросети
  3. Локальный маршрут: Python/Claude Code vs облако
  4. Чеклист расхождений: дата, сумма, назначение
  5. Когда звать 1С-ника, а когда хватает таблицы
- **faq_hints:** можно ли полностью в Excel; нужен ли OData
- **internal_links:** /obezlichivanie-dannyh-chatgpt-finansist/, /python-finansist-sverka-csv/
- **cover_scene_hint:** abstract two ledgers merge shield privacy dark, no text

---

## B29 — Категории ДДС: справочник, который не разъедется

- **priority:** P0
- **slug:** spravochnik-kategorij-dds
- **h1:** Как завести справочник категорий ДДС, чтобы отчёты не разъезжались
- **primary_query:** категории ддс справочник
- **secondary_queries:** классификация платежей excel, статьи ддс google sheets, единый справочник финансы
- **search_intent:** how_to
- **article_mode:** B
- **author_id:** olga-kondratskaya
- **h2_outline:**
  1. Сколько категорий достаточно на старте
  2. Лист «Справочник» + запрет свободного ввода
  3. Правила для «Прочее» и переводов между счетами
  4. Как обучить команду одним шаблоном
  5. Связка с дашбордом и план-фактом
- **faq_hints:** чем отличается от плана счетов 1с; можно ли 200 статей
- **internal_links:** /plan-fakt-dds-google-sheets/, /disnejlend-dlya-dannyh/
- **cover_scene_hint:** abstract taxonomy tree nodes finance dark purple, no text

---

## B30 — Power Query для финансиста: обновление без макросов

- **priority:** P0
- **slug:** power-query-finansist-obnovlenie
- **h1:** Как обновлять финтаблицы через Power Query без макросов и VBA
- **primary_query:** power query для финансиста
- **secondary_queries:** power query excel обновление, загрузка csv power query, power query google sheets
- **search_intent:** how_to
- **article_mode:** B
- **author_id:** olga-kondratskaya
- **h2_outline:**
  1. Когда Power Query лучше ручного VLOOKUP
  2. Подключение папки с выгрузками
  3. Типы данных, даты, разделитель `;`
  4. Обновить всё одной кнопкой
  5. Границы: когда уходить в Python/Sheets
- **faq_hints:** есть ли в Excel Online; работает ли на Mac
- **internal_links:** /python-finansist-sverka-csv/, /nejroset-excel-formuly-finansist/
- **cover_scene_hint:** abstract data pipes transform nodes dark ui, no text

---

## B31 — Чеклист закрытия месяца для малого финотдела

- **priority:** P0
- **slug:** cheklist-zakrytiya-mesyaca-finotdel
- **h1:** Чеклист закрытия месяца для малого финотдела: от банка до отчёта собственнику
- **primary_query:** чеклист закрытия месяца финансист
- **secondary_queries:** закрытие месяца управленческий учет, месяц close finance checklist, что проверить перед отчетом
- **search_intent:** checklist
- **article_mode:** B
- **author_id:** olga-kondratskaya
- **h2_outline:**
  1. День −3…0: банк, акты, зарплата
  2. Сверки: банк↔учёт, взаиморасчёты
  3. Управленческие отчёты: ДДС, ОПиУ, долги
  4. Автоматизация: что можно снять с ручного чеклиста
  5. Шаблон чеклиста в Sheets на команду
- **faq_hints:** отличается ли от бухгалтерского закрытия; сколько часов норма
- **internal_links:** /finansovyj-minimalizm/, /daydzhest-sobstvenniku-n8n-telegram/
- **cover_scene_hint:** abstract checklist nodes month close dark holographic, no text

---

## B32 — Make vs n8n для финотдела

- **priority:** P0
- **slug:** make-vs-n8n-finotdel
- **h1:** Make или n8n для финотдела: что выбрать под банк, Sheets и Telegram
- **primary_query:** make или n8n
- **secondary_queries:** n8n vs make финансы, автоматизация финотдела no-code, self-hosted n8n для компании
- **search_intent:** comparison
- **article_mode:** B
- **author_id:** olga-kondratskaya
- **h2_outline:**
  1. Критерии CFO: данные, цена, кто администрирует
  2. Таблица: облако Make vs self-hosted n8n
  3. Типовые сценарии: выписка, напоминания, дайджест
  4. Когда остаться в Sheets без оркестратора
  5. Решение на 90 дней без смены стека
- **faq_hints:** нужен ли программист для n8n; безопаснее ли self-hosted
- **internal_links:** /avtomatizaciya-finansov-no-code/, /platezhnyj-kalendar-google-sheets-n8n/
- **cover_scene_hint:** abstract two paths fork automation dark purple blue, no text

---

## B33 — Акты сверки: реестр и контроль ответов

- **priority:** P0
- **slug:** akty-sverki-reestr-kontrol
- **h1:** Как вести реестр актов сверки и контролировать ответы контрагентов без CRM
- **primary_query:** реестр актов сверки
- **secondary_queries:** контроль актов сверки, акт сверки google sheets, напоминание акт сверки
- **search_intent:** workflow
- **article_mode:** B
- **author_id:** olga-kondratskaya
- **h2_outline:**
  1. Колонки реестра: период, контрагент, статус, дата ответа
  2. Статусы: черновик / отправлен / согласован / спор
  3. Напоминания через Sheets → n8n → email
  4. Что хранить из 1С, чего не тащить в облако
  5. Связка с дебиторкой и закрытием месяца
- **faq_hints:** нужна ли ЭДО; можно ли без 1с
- **internal_links:** /upravlenie-debitorkoj-reestr-napominaniya/, /cheklist-zakrytiya-mesyaca-finotdel/
- **cover_scene_hint:** abstract agreement documents network nodes dark, no text

---

---

## B34 — План счетов управленки в Sheets

- **priority:** P0
- **slug:** plan-schetov-upravlencheskij-sheets
- **h1:** Как завести простой план счетов управленческого учёта в Google Sheets
- **primary_query:** план счетов управленческий учет sheets
- **secondary_queries:** автоматизация финотдела, план счетов управленческий учет sheets, 2026
- **search_intent:** how_to
- **article_mode:** B
- **author_id:** olga-kondratskaya
- **source_notes:** scout_ci 2026-07-31 · trend-scored · tags:план,счетов,управленческий,sheets
- **h2_outline:**
  1. Когда это нужно финотделу (и когда нет)
  2. Подготовка данных и безопасность (без сырых ПДн в облако)
  3. Пошаговая настройка / скрипт / сценарий
  4. Проверка результата и типичные ошибки
  5. Что автоматизировать дальше
- **faq_hints:** можно ли без программиста; сколько займёт внедрение; какие риски для данных
- **internal_links:** /avtomatizaciya-finansov-no-code/, /obezlichivanie-dannyh-chatgpt-finansist/
- **cover_scene_hint:** abstract holographic finance automation dark #0a0a0f purple #8b5cf6, no text

---

## B35 — Сверка банка и учёта через n8n

- **priority:** P0
- **slug:** sverka-banka-n8n-google-sheets
- **h1:** Как сверить банковскую выписку с учётом через n8n и Google Sheets
- **primary_query:** сверка банковской выписки n8n
- **secondary_queries:** автоматизация финотдела, сверка банковской выписки n8n, 2026
- **search_intent:** how_to
- **article_mode:** B
- **author_id:** olga-kondratskaya
- **source_notes:** scout_ci 2026-07-31 · trend-scored · tags:n8n,банк,сверка,sheets
- **h2_outline:**
  1. Когда это нужно финотделу (и когда нет)
  2. Подготовка данных и безопасность (без сырых ПДн в облако)
  3. Пошаговая настройка / скрипт / сценарий
  4. Проверка результата и типичные ошибки
  5. Что автоматизировать дальше
- **faq_hints:** можно ли без программиста; сколько займёт внедрение; какие риски для данных
- **internal_links:** /avtomatizaciya-finansov-no-code/, /obezlichivanie-dannyh-chatgpt-finansist/
- **cover_scene_hint:** abstract holographic finance automation dark #0a0a0f purple #8b5cf6, no text

## Архив очереди (не в работе)

Старые карточки B01–B03, B05–B10, B12 сняты с активной очереди после согласования 2026-07.  
Опубликованные **B04** (`claude-code-finotdel`) и **B11** (`obezlichivanie-dannyh-chatgpt-finansist`) — только в `shared/published-articles.md`.
