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

- POST /clients/ - Создать нового пользователя
- GET /clients/{client_id} - Получить пользователя по ID
- GET /clients/ - Получить список пользователей
- DELETE /clients/{client_id} - Удалить пользователя по ID

#### Товары

- POST /goods/ - Создать новый товар
- GET /goods/{goods_id} - Получить товар по ID
- GET /goods/ - Получить список товаров
- DELETE /goods/{goods_id} - Удалить товар по ID

#### Заказы

- POST /orders/ - Создать новый заказ
- GET /orders/{order_id} - Получить заказ по ID
- GET /orders/ - Получить список заказов
- DELETE /orders/{order_id} - Удалить заказ по ID
