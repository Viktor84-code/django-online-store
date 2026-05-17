# Django Online Store

Учебный проект интернет-магазина на Django. Курс Skypro.

## 🚀 Быстрый старт

'''
poetry install
poetry run python manage.py runserver
Открой http://127.0.0.1:8000/
'''
📁 Структура
catalog/ — приложение с главной страницей и контактами

config/ — настройки проекта

🛠 Технологии
Django 6.0

Bootstrap 5

Python 3.13
## Домашнее задание "Базы данных" (16.05.2026)

### Выполненные задачи:

#### 1. Подключение PostgreSQL
- База данных `django_online_store`
- Настройки через `.env` файл
- Переход с SQLite на PostgreSQL

#### 2. Создание моделей
- `Category` (категории товаров)
- `Product` (товары)
- Поля: name, description, image, price, created_at, updated_at, ForeignKey

#### 3. Миграции
- Созданы и применены миграции для всех моделей

#### 4. Админ-панель
- Настроено отображение: list_display, list_filter, search_fields
- Зарегистрированы модели Category, Product, Contact

#### 5. Работа с Shell
- Создание категорий и продуктов через ORM
- Выполнение запросов: filter, update, delete
- Скриншоты в папке `screenshots/`

#### 6. Фикстуры
- Экспорт данных в `fixtures/categories.json` и `fixtures/products.json`

#### 7. Кастомная команда
- `load_test_data` — загрузка тестовых данных из фикстур
- Автоматическая очистка БД перед загрузкой

#### 8. Бонусное задание
- Вывод последних 5 продуктов на главной странице (в консоль)
- Модель `Contact` для хранения обратной связи
- Отображение контактов на странице `contacts.html`
- Страница каталога с товарами из БД

### Структура проекта
django-online-store/
├── catalog/
│ ├── management/commands/
│ │ └── load_test_data.py
│ ├── migrations/
│ ├── templates/catalog/
│ ├── models.py
│ ├── admin.py
│ └── views.py
├── config/
│ └── settings.py
├── fixtures/
│ ├── categories.json
│ └── products.json
├── screenshots/
│ └── (скриншоты shell-команд)
├── .env
└── README.md

# Установка зависимостей
poetry install

# Создание .env файла с настройками БД
# DB_NAME=django_online_store
# DB_USER=postgres
# DB_PASSWORD=your_password
# DB_HOST=localhost
# DB_PORT=5432

# Применение миграций
poetry run python manage.py migrate

# Загрузка тестовых данных
poetry run python manage.py load_test_data

# Запуск сервера
poetry run python manage.py runserver

## Тестирование

Запуск тестов:

poetry run python manage.py test
Покрытие кода тестами:

bash
poetry run coverage run manage.py test
poetry run coverage report
Текущее покрытие: 97%

Качество кода
Форматирование:

bash
poetry run black .
poetry run isort .
Линтинг:

bash
poetry run flake8 .