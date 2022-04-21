# Yatube API
API для социальной сети Yatube.
## Функционал:
Регистрация, создание и редактирование постов, добавление изображения, комментирование. Используется пагинация постов, кэширование главной страницы.

#### Стек:
Python3, Django 2.2, SimpleJWT
### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/sproggi/api_final_yatube.git
```

```
cd api_final_yatube
```

Cоздать и активировать виртуальное окружение:

```
python -m venv env
```

```
source venv/Scripts/activate
```

```
python -m pip install --upgrade pip
```

Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python manage.py migrate
```

Запустить проект:

```
python manage.py runserver
```
### Документация по API
```sh
127.0.0.1:8000/redoc/
```

### Запросы и эндпоинты:
##### Все посты
```sh
127.0.0.1:8000/api/v1/posts/
```
| Endpoints | Response |
| ------ | ------ |
| [/api/v1/posts/] | All posts. GET, POST. |
| [/api/v1/posts/1/] | First id post. GET, PUT, PATCH, DELETE. |
| [/api/v1/posts/1/comments/] | Comments for post. GET, POST. |
| [/api/v1/posts/1/comments/1/] | Comment, in first post. GET, PUT, PATCH, DELETE.|
| [/api/v1/groups/] | Groups list. GET |
| [/api/v1/groups/1/] | First group. GET |
| [/api/v1/follow/] | Follow list, for request user. GET, POST. |
| [/api/v1/follow/1/] | First follow. GET, PUT, PATCH, DELETE. |
| [/api/v1/users/] | Users list. GET, CREATE |
| [/api/v1/jwt/create/] | JWT Token create. POST, |


[/api/v1/posts/]: <https://127.0.0.1/api/v1/posts/>
[/api/v1/posts/1/]: <https://127.0.0.1/api/v1/posts/1/>
[/api/v1/posts/1/comments/]: <https://127.0.0.1/api/v1/posts/1/comments/>
[/api/v1/posts/1/comments/1/]: <https://127.0.0.1/api/v1/posts/1/comments/1/>
[/api/v1/groups/]: <https://127.0.0.1/api/v1/groups/>
[/api/v1/groups/1/]: <https://127.0.0.1/api/v1/groups/1/>
[/api/v1/follow/]: <https://127.0.0.1/api/v1/follow/>
[/api/v1/follow/1/]: <https://127.0.0.1/api/v1/follow/1/>
[/api/v1/users/]: <https://127.0.0.1/api/v1/users/>
[/api/v1/jwt/create/]: <https://127.0.0.1/api/v1/jwt/create/>