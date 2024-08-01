Это API для интернет-магазина созданное в учебных целях.
Спомощью которого можно управлять пользователями, товарами и заказами.

## Необходимые модули для работы API

- FastAPI
- SQLAlchemy
- Pydantic
- Uvicorn
- passlib

## Запуск приложения

uvicorn main:app --reload

## Описание конечных точек

#### Пользователи

POST /users/ - Создать нового пользователя
GET /users/{user_id} - Получить пользователя по ID
GET /users/ - Получить список пользователей
DELETE /users/{user_id} - Удалить пользователя по ID

#### Товары

POST /products/ - Создать новый товар
GET /products/{product_id} - Получить товар по ID
GET /products/ - Получить список товаров
DELETE /products/{product_id} - Удалить товар по ID

#### Заказы

POST /orders/ - Создать новый заказ
GET /orders/{order_id} - Получить заказ по ID
GET /orders/ - Получить список заказов
DELETE /orders/{order_id} - Удалить заказ по ID