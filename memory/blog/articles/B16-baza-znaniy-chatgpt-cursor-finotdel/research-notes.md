# Research notes — B16

**topic_id:** B16  
**slug:** baza-znaniy-chatgpt-cursor-finotdel  
**h1:** Как сделать базу знаний для ChatGPT и Cursor: свои регламенты без утечки 1С  
**research_date:** 2026-07-22  
**utility_gate:** PASS (`how_to`, mode B)

---

## utility_verdict

**PASS** — how_to: что класть/не класть в knowledge base финотдела; структура папок; подключение в Cursor и ChatGPT; обезличивание; 10 тестовых вопросов против галлюцинаций.

---

## reader_outcome

Финансист собирает папку регламентов/шаблонов/словаря ДДС, подключает её в Cursor и (обезличенно) в ChatGPT Projects/файлы, проверяет 10 вопросами и не пускает сырые выгрузки 1С в индекс.

---

## action_outline

1. Определить whitelist/blacklist содержимого.
2. Собрать структуру папок (regs, templates, dds-dict, faq).
3. Подключить в Cursor (@docs / rules / открытая папка).
4. Подключить в ChatGPT (projects/files) только обезличенное.
5. Запрет сырых выгрузок в индекс.
6. 10 тестовых вопросов + ловля галлюцинаций.
7. Регламент обновления базы.
8. Отличие от Custom GPT.
9. Опция локальной модели (Ollama) для чувствительного контура.

---

## Яндекс Wordstat

⚠️ **WORDSTAT AUTH WARNING:** MCP-KV недоступен. Цифры не выдуманы.

LSI: как сделать базу знаний chatgpt, knowledge base cursor, загрузить регламенты в chatgpt, @docs cursor, custom gpt vs папка.

---

## SERP (22.07.2026)

| URL | Зазор |
| --- | --- |
| https://startduck.com/tutorials/cursor-i-obsidian-… | Cursor+Obsidian vault |
| https://habr.com/ru/companies/bothub/articles/1044774/ | Cursor 2026: rules, skills, индекс |
| https://tochkicamp.ru/guides/second-brain/ | second brain папка+IDE |
| https://vibecoding.by/blog/ii-agenty-… | .cursorrules, агенты |
| teletype Qdrant+Cursor | тяжёлый RAG – не обязателен для старта |

Угол КОДА: финотдел, запрет сырых 1С, словарь ДДС, тест из 10 вопросов.

---

## Факты

| # | Факт | Источник |
| --- | --- | --- |
| 1 | Cursor индексирует открытую папку проекта; правила – `.cursor/rules` / AGENTS. | Habr bothub 2026 |
| 2 | Vault/папка Markdown удобна как база знаний без отдельной БД. | startduck; tochkicamp |
| 3 | Тяжёлый RAG (Qdrant и т.п.) – следующий уровень, не MVP. | teletype |
| 4 | Облачный ChatGPT: загружаемые файлы/projects = данные у провайдера → только обезличенное. | практика + B11 |
| 5 | Custom GPT ≠ замена локальной папке в Cursor для командныйх регламентов. | expert angle |

---

## FAQ

отличие от custom gpt; локальная модель; как обновлять; можно ли 1С выгрузки; сколько файлов; кто владеет актуальностью

## CTA / links

club + telegram; /obezlichivanie-dannyh-chatgpt-finansist/, /cursor-ai-agenty-finotchetnost/; no salebot
