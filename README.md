# Kraken Trading Bot

Автоматизированный торговый бот для криптовалютной биржи Kraken с веб-интерфейсом.

## Структура проекта

```
kraken_claude_traiding_bot/
├── config/              # Конфигурационные файлы
│   ├── __init__.py
│   ├── settings.py     # Основные настройки
│   └── logging.py      # Настройки логирования
├── src/                # Исходный код
│   ├── bot/           # Логика торгового бота
│   │   ├── __init__.py
│   │   ├── trading_bot.py    # Основной класс бота
│   │   └── strategies.py     # Торговые стратегии
│   ├── services/      # Сервисы (API, уведомления)
│   │   ├── __init__.py
│   │   ├── kraken_api.py    # Работа с API Kraken
│   │   ├── price_service.py # Сервис получения цен
│   │   └── notifications.py # Уведомления
│   └── utils/         # Вспомогательные функции
│       ├── __init__.py
│       ├── validators.py    # Валидация данных
│       └── helpers.py      # Вспомогательные функции
├── tests/             # Тесты
│   ├── __init__.py
│   ├── test_bot.py
│   ├── test_strategies.py
│   └── test_services.py
├── web/               # Веб-интерфейс
│   ├── static/        # Статические файлы
│   │   ├── css/
│   │   │   └── styles.css
│   │   └── js/
│   │       └── dashboard.js
│   ├── templates/     # HTML шаблоны
│   │   ├── base.html
│   │   ├── dashboard.html
│   │   └── settings.html
│   └── app.py         # Flask приложение
├── .env.example       # Пример переменных окружения
├── Procfile           # Конфигурация для Heroku
├── requirements.txt   # Зависимости
├── runtime.txt        # Версия Python для Heroku
└── setup.py          # Установка пакета

```

## Основные компоненты

### Bot
- `trading_bot.py` - Основной класс бота, управляющий торговлей
- `strategies.py` - Различные торговые стратегии

### Services
- `kraken_api.py` - Взаимодействие с API Kraken
- `price_service.py` - Получение цен криптовалют
- `notifications.py` - Отправка уведомлений

### Web Interface
- Dashboard для мониторинга торгов
- Настройка параметров бота
- Просмотр истории торгов

## Установка

1. Клонируйте репозиторий:
```bash
git clone https://github.com/your-username/kraken_claude_traiding_bot.git
cd kraken_claude_traiding_bot
```

2. Создайте виртуальное окружение:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
.\venv\Scripts\activate  # Windows
```

3. Установите зависимости:
```bash
pip install -r requirements.txt
```

4. Настройте переменные окружения:
```bash
cp .env.example .env
# Отредактируйте .env файл
```

## Настройка окружения

Создайте файл `.env` на основе `.env.example` и укажите:
- `KRAKEN_API_KEY` - Ваш API ключ Kraken
- `KRAKEN_API_SECRET` - Ваш секретный ключ API Kraken
- `FLASK_SECRET_KEY` - Секретный ключ для Flask
- `DEBUG` - Режим отладки (True/False)

## Запуск

### Локально
```bash
python web/app.py
```

### На Heroku
```bash
git push heroku main
```

## Тестирование
```bash
pytest tests/
```

## Мониторинг

- Веб-интерфейс: `http://localhost:5000` (локально)
- Логи Heroku: `heroku logs --tail`

## Безопасность

- Не коммитьте `.env` файл
- Регулярно меняйте API ключи
- Используйте сложные пароли
- Включите двухфакторную аутентификацию

## Лицензия

MIT

## Автор

Ваше имя