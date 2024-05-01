# Сайт фриланс биржа на Django. 

## Используемый стек технологий
- Poetry - менеджер зависимостей
- environs - парсинг переменных окружения
- Фреймворк Django
- Фреймворк Bootstrap
- Django-crispy-forms - улучшение отображения форм
- PostgreSQL - база данных
- Docker, docker-compose

## Фичи
- Регистрация пользователя в качестве фрилансера/заказчика
- Аутентификация и авторизация пользователя
- Стандартная модель пользователя расширена
- Возможность редактирования профиля пользователя
- Личный кабинет фрилансера/заказчика
- Настроен поиск по опыту(ключевым навыкам) или имени
- Написаны тесты для всех страниц сайта
- Админ панель

## Запуск приложения локально с помощью Docker
1. Клонируйте репозиторий:
    ```bash
    git clone git@github.com:fersus85/freelance-stock.git
    ```
2. Перейдите в директорию проекта:
    ```bash
    cd freelance-stock
    ```
3. Запустите docker-compose:
    ```bash
    docker compose up --build -d
   ```
4. Запустите тесты:
   ```bash
   docker-compose exec web python freelance/manage.py test
   ```
5. Создайте superuser:
    ```bash
    docker-compose exec web python freelance/manage.py createsuperuser
    ```

6. Откройте в браузере адрес: 127.0.0.1:8000
