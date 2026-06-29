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

## Домашнее задание "Шаблонизация" (24.05.2026)

### Выполненные задачи:

#### 1. Базовый шаблон и наследование
- Создан `base.html` с общими блоками (header, footer, подключение Bootstrap)
- Все шаблоны наследуют `base.html` через `{% extends 'base.html' %}`
- Создан подшаблон `menu.html` с навигацией (Главная, Каталог, Контакты)
- Подшаблон подключен в `base.html` через `{% include %}`

#### 2. Детальная страница товара
- URL: `/products/<int:pk>/`
- Контроллер `product_detail` получает `pk` через `get_object_or_404`
- Отображает название, цену, полное описание и изображение товара

#### 3. Главная страница каталога
- URL: `/catalog/`
- Использован запрос `Product.objects.all()`
- Цикл `{% for %}` выводит все товары
- Описание обрезано до 100 символов (`truncatewords:20`)
- Если нет фото — отображается заглушка "Нет фото"

#### 4. Переходы между страницами
- С каталога на детальную страницу (кнопка "Подробнее")
- С детальной страницы обратно в каталог (ссылка "Назад к каталогу")

#### 5. Форма добавления товара (доп. задание)
- URL: `/products/create/`
- `ProductForm` на базе `ModelForm`
- Поля: name, description, price, category, image
- Валидация через `form.is_valid()`
- Сохранение в БД через `form.save()`
- Редирект на список товаров после сохранения

#### 6. Пагинация (доп. задание)
- 6 товаров на страницу
- Пагинация через `Paginator` в `catalog` view
- Навигация: Первая, Назад, Вперед, Последняя

#### 7. Качество кода
- Форматирование: `black`, `isort`
- Покрытие тестами: 88%

### Итоговая структура шаблонов
catalog/templates/
├── base.html
├── includes/
│ └── menu.html
└── catalog/
├── catalog.html # список товаров с пагинацией
├── product_detail.html
├── product_create.html
├── contacts.html
└── home.html

## Домашнее задание "Class-Based Views и Блог" (29.05.2026)

### Выполненные задачи:

#### 1. Перевод контроллеров на CBV (Задание 1)
- `HomeView` — TemplateView
- `ContactsView` — TemplateView с обработкой POST
- `ProductListView` — ListView с пагинацией (6 товаров)
- `ProductDetailView` — DetailView
- `ProductCreateView` — CreateView
- `ProductUpdateView` — UpdateView
- `ProductDeleteView` — DeleteView

#### 2. Создание блога (Задание 2)
- Приложение `blog` зарегистрировано в `INSTALLED_APPS`
- Модель `BlogPost` с полями:
  - `title` — заголовок
  - `content` — содержимое
  - `preview` — изображение
  - `created_at` — дата создания
  - `is_published` — признак публикации
  - `views_count` — количество просмотров
- Полный CRUD на CBV (Create, Read, Update, Delete)
- Шаблоны блога наследуют `base.html`
- URL-маршруты: `/blog/` (список), `/blog/<int:pk>/` (детали), `/blog/create/`, `/blog/<int:pk>/update/`, `/blog/<int:pk>/delete/`

#### 3. Модификации блога (Задание 3)
- Увеличение счётчика просмотров при открытии статьи (переопределён `get_object` в `DetailView`)
- В списке статей выводятся только опубликованные (`get_queryset` в `ListView`)
- После редактирования — редирект на страницу статьи (`get_success_url` в `UpdateView`)

#### 4. Тестирование
- 21 тест (модели, views, формы, команды)
- Покрытие каталога: **99%**
- Все тесты проходят успешно

### Итоговая структура проекта
django-online-store/
├── catalog/
│ ├── management/commands/
│ │ └── load_test_data.py
│ ├── migrations/
│ ├── templates/catalog/
│ │ ├── home.html
│ │ ├── product_list.html
│ │ ├── product_detail.html
│ │ ├── product_create.html
│ │ ├── product_edit.html
│ │ ├── product_confirm_delete.html
│ │ ├── contacts.html
│ │ └── menu.html
│ ├── models.py
│ ├── admin.py
│ ├── views.py
│ ├── urls.py
│ └── tests.py
├── blog/
│ ├── migrations/
│ ├── templates/blog/
│ │ ├── blog_list.html
│ │ ├── blog_detail.html
│ │ ├── blog_form.html
│ │ └── blog_confirm_delete.html
│ ├── models.py
│ ├── admin.py
│ ├── views.py
│ ├── urls.py
│ └── tests.py
├── config/
│ └── settings.py
├── fixtures/
├── screenshots/
├── .env
└── README.md

text

### Запуск проекта

# Установка зависимостей
poetry install

# Применение миграций
poetry run python manage.py migrate

# Загрузка тестовых данных (опционально)
poetry run python manage.py load_test_data

# Запуск сервера
poetry run python manage.py runserver
Доступные URL
URL	Описание
/	Главная страница
/catalog/	Каталог товаров
/catalog/product/<int:pk>/	Детальная страница товара
/contacts/	Контакты и обратная связь
/blog/	Список статей блога
/blog/<int:pk>/	Детальная страница статьи
/admin/	Админ-панель
Тестирование
bash
# Запуск всех тестов
poetry run python manage.py test

# Покрытие кода тестами
poetry run coverage run manage.py test
poetry run coverage report
Качество кода
bash
# Форматирование
poetry run black .
poetry run isort .

# Линтинг
poetry run flake8 .

## Домашнее задание "Формы и валидация" (12.06.2026)

### Выполненные задачи:

#### 1. CRUD для продуктов с формами
- `ProductForm` на базе `ModelForm`
- Страницы: создание (`/create/`), редактирование, удаление, список, детали
- Кнопки «Редактировать» и «Удалить» на странице товара

#### 2. Валидация запрещённых слов
- Список слов вынесен в константу: казино, криптовалюта, биржа, дешево, бесплатно, обман, полиция, радар
- Проверка в полях `name` и `description` (регистр не важен)
- Пользователь получает понятное сообщение об ошибке

#### 3. Валидация цены
- Цена не может быть отрицательной
- Кастомный метод `clean_price`
- Сообщение: «Цена не может быть отрицательной»

#### 4. Стилизация форм
- Bootstrap-классы добавлены через `__init__`
- Чекбоксы (если есть) получают класс `form-check-input`
- Остальные поля — `form-control`

#### 5. Загрузка изображений
- Поле `image` в модели Product
- Валидация в `clean_image`: формат JPEG/PNG, размер до 5 МБ
- В шаблонах добавлен `enctype="multipart/form-data"`

#### 6. Дополнительное задание (блог)
- При достижении 100 просмотров статьи отправляется письмо-поздравление
- `congratulation_sent` — флаг для одноразовой отправки
- Письма сохраняются в папку `sent_emails/` (для разработки)

#### 7. Тесты и качество
- 3 новых теста на валидацию формы
- Покрытие каталога: **97%**
- `black`, `isort`, `flake8` — без ошибок
- `mypy` — пропущен (нет stubs для Django)


## Аутентификация и пользователи

### Модель пользователя
- Кастомная модель `User` наследуется от `AbstractUser`
- Поле для входа — `email` (вместо `username`)
- Дополнительные поля:
  - `phone` — номер телефона (уникальный, необязательный)
  - `avatar` — аватар (jpg, jpeg, png, до 5 МБ)
  - `country` — страна (необязательно)

### Регистрация
- Форма регистрации с полями: `email`, `phone`, `avatar`, `country`, `password1`, `password2`
- После регистрации пользователь автоматически входит в систему
- Отправляется приветственное письмо на email (через SMTP Яндекс)

### Вход и выход
- Вход по `email` и `паролю`
- Кастомная форма логина с Bootstrap-стилями
- Выход через POST-запрос (CSRF-защита)

### Профиль пользователя
- Страница профиля (`/users/profile/`) — отображение: email, телефон, аватар, страна
- Редактирование профиля (`/users/profile/edit/`) — изменение телефона, аватара, страны

### Ограничение доступа
- `LoginRequiredMixin` для:
  - Создания, редактирования, удаления товаров
  - Создания, редактирования, удаления записей блога
  - Просмотра и редактирования профиля
- Публичный доступ: список товаров (`/catalog/`)

### Настройки почты
- SMTP Яндекс (`smtp.yandex.ru`, порт 587, TLS)
- Пароль приложения для безопасности


## ✅ Модуль «Права доступа, группы, владельцы» (Homework 2)

### Реализовано:
- Добавлены поля `owner` и `is_published` в модель `Product`
- Настроены кастомные права: `can_unpublish_product`
- Создана группа **«Модератор продуктов»** с правами:
  - `can_unpublish_product`
  - `delete_product`
- Реализован миксин `OwnerOrModeratorMixin` для проверки доступа
- Добавлена автоматическая привязка `owner` при создании продукта
- Кнопки редактирования/удаления отображаются только для владельца или модератора
- Реализована группа **«Контент-менеджер»** для управления блогом
- Написаны тесты: 41 тест, покрытие 95%
- Пройдены: flake8, black, isort, mypy

### Команды для создания групп:
```
poetry run python manage.py create_groups
poetry run python manage.py create_blog_groups
```

## 🚀 Модуль «Кэширование и бизнес-логика» (Homework 3)

### Выполненные задачи:

#### Задание 1. Установка Redis
- Redis установлен и запущен локально (порт 6379)
- Настройки в `settings.py`:
  ```python
  CACHES = {
      'default': {
          'BACKEND': 'django_redis.cache.RedisCache',
          'LOCATION': 'redis://127.0.0.1:6379/1',
          'OPTIONS': {
              'CLIENT_CLASS': 'django_redis.client.DefaultClient',
          }
      }
  }
Зависимости: redis (4.5.4), django-redis (5.4.0)

Задание 2. Кэширование страницы продукта
Страница ProductDetailView закэширована через @method_decorator(cache_page(60 * 15))

Время жизни кэша: 15 минут

Задание 3. Сервисная функция и представление категории
Создан сервис catalog/services.py с функцией get_products_by_category(category_id)

Добавлено представление products_by_category и URL /category/<int:category_id>/

Создан шаблон products_by_category.html с выводом товаров в карточках

Категории выводятся на главной странице каталога

Задание 4. Низкоуровневое кэширование
Реализована функция get_cached_products_by_category(category_id)

Ключ кэша: category_{id}

Время жизни: 15 минут (900 секунд)

Данные сохраняются и извлекаются из Redis

Проверка кэша
bash
# Проверка через Django shell
python manage.py shell
>>> from django.core.cache import cache
>>> cache.get('category_1')  # список товаров
>>> cache.ttl('category_1')   # время жизни в секундах

# Проверка через redis-cli
redis-cli -n 1 keys *  # должен быть ключ :1:category_1
Запуск Redis
bash
redis-server
# или через службу Windows
Зависимости (актуальные версии)
text
redis = ">=4.5.4,<5.0.0"
django-redis = ">=5.4.0,<6.0.0"