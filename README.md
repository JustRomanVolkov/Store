# Магазин

## О проекте

Этот проект представляет собой простой магазин с обработкой платежей. 

## Функциональность

- **Модель товара (Item)**: товар имеет поля `name`, `description`, `price`.
- **API**:
  - `GET /buy/{id}`: получение Stripe Session ID для оплаты товара.
  - `GET /item/{id}`: получение HTML страницы с информацией о товаре и кнопкой покупки.
- **Бонусные задачи**:
  - Запуск в Docker.
  - Использование переменных среды.
  - Возможность просмотра моделей в кастомной Django Admin с доп. действиями.

## Технологии

- Django и Django Rest Framework
- Stripe API
- Docker и Docker Compose
- PostgreSQL
- Git
- Poetry

## Запуск проекта

### Требования

- Docker и Docker Compose
- Stripe API ключи

### Инструкция

1. Клонируйте репозиторий и перейдите в директорию проекта.
   ```bash
    git clone https://github.com/JustRomanVolkov/store.git
    cd store
   ```

2. Создайте файл `.env` из `.env.like` с необходимыми переменными окружения:

3. Запустите проект с помощью Docker Compose:
   ```bash
    docker-compose up -d
   ```
4. После запуска, проект будет доступен по адресу `http://localhost:8000`.

## Работа с проектом

- Для доступа к админ-панели Django перейдите по адресу `http://localhost:8000/admin`.
- Все конфигурации и зависимости описаны в `Dockerfile` и `docker-compose.yml`.

## Первичные команды:
- создание супер пользователя:
    ```bash
    docker exec -it shop_django python manage.py createsuperuser
    ```
- загрузка в базу данных фикстур (тестовые данные):
   ```bash
    docker exec -it shop_django python manage.py loaddata fixture.json
```
