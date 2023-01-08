![example workflow](https://github.com/p0lzi/yamdb_final/actions/workflows/yamdb_workflow.yml/badge.svg)

# Проект «API для Yatube»

### Краткое описание проекта

Учебный проект API для социальной сети. Пользователи могут публиковать посты,
просматривать чужие посты, подписываться на авторов и комментировать их записи.
Для аутентификации используются JWT-токены. Аутентифицированным пользователям
разрешено изменение и удаление своего контента; в остальных случаях доступ
предоставляется только для чтения.

### **Стек**

![python version](https://img.shields.io/badge/Python-3.7-green)
![django version](https://img.shields.io/badge/Django-2.2-green)
![djangorestframework version](https://img.shields.io/badge/DRF-3.12-green)
![simplejwt version](https://img.shields.io/badge/DRFsimplejwt-4.7-green)


### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/p0lzi/infra_sp2.git
```

Перейти в папку infra
```
cd /infra
```

Запустить docker-compose

```
docker-compose up
```

Выполнить миграции

```
docker-compose exec web python manage.py migrate       
```

Создать суперпользователя

```
docker-compose exec web python manage.py createsuperuser   
```    

Собрать статику

``` 
docker-compose exec web python manage.py collectstatic --no-input 
```   


### Документация к API доступна по адресу

**api/v1/redoc/**


### Примеры использования

Пример POST-запроса. Регистрация нового пользователя

```
POST /api/v1/auth/signup/

Request samples

{
  "username": "string",
  "email": "string"
}
```

Пример POST-запроса. Получение JWT-токена.

```
POST /api/v1/auth/token/

Request samples

{
  "username": "string",
  "confirmation_code": number
}
```

Пример POST-запроса. Добавление нового произведения

```
POST /api/v1/titles/

Request samples

{
  "name": "string",
  "year": 0,
  "description": "string",
  "genre": [
    "string"
  ],
  "category": "string"
}
```

Пример GET-запроса. Получить информацию о произведении.
```
GET /api/v1/titles/{title_id}/
```

Пример POST-запроса. Создать категорию.

```
POST /api/v1/titles/

Request samples

{
  "name": "string",
  "slug": "string"
}
```

Пример GET-запроса. Получить список всех категорий.
```
GET /api/v1/categories/
```

Пример POST-запроса. Добавить новый отзыв.

```
POST /api/v1/titles/{title_id}/reviews/

Request samples

{
  "text": "string",
  "score": 1
}
```

Пример GET-запроса. Получить список всех отзывов.
```
GET /api/v1/titles/{title_id}/reviews/
```
Пример POST-запроса. Добавить новый комментарий для отзыва.

```
POST /api/v1/titles/{title_id}/reviews/{review_id}/comments/

Request samples

{
  "text": "string"
}
```
Пример GET-запроса. Получить комментарий для отзыва по id.
```
GET /api/v1/titles/{title_id}/reviews/{review_id}/comments/{comment_id}/
```


### Импорт тестовых данных

Для проверки работы проекта можно наполнить проект тестовыми данными, для этого
можно ввести команду

```
python manage.py import
```

Данная команда импортирует данные по:

- категориям;
- комментариям;
- жанрам;
- отзывам;
- произведениям;
- пользователям

___

## Команда

- [Антон Росляков](https://github.com/Antonros)
- [Егор Ремезов](https://github.com/drode1)
- [Павел Зияев](https://github.com/p0lzi)
- [Яндекс Практикум](https://github.com/yandex-praktikum/)

___ 

