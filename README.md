# Мониторинг сервера на Python

Скрипт проверяет загрузку CPU, память и диск. Если лимит превышен — отправляет уведомление в Telegram.

## Что делает
- Проверяет CPU, память, диск каждые 60 секунд.
- Если превышен лимит (80%) — отправляет уведомление в Telegram.
- Работает на Linux и Windows.

## Стек
- Python
- psutil
- requests
- Telegram Bot API

## Как запустить
1. Установи библиотеки:
   `pip install psutil requests python-dotenv`
2. Создай `.env` с токеном и chat_id:
