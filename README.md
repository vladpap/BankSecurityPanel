![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)
![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white)


# Пульт охраны банка


## Установка.
- Python3 должен быть уже установлен.
- Рекомендуется использовать среду окружения [venv](https://docs.python.org/3/library/venv.html) 
для изоляции проекта.
 - Используйте `pip` (или `pip3`, если есть конфликт с Python2) для установки зависимостей
```console
$ pip install -r requirements.txt
```

## Секретные данные настройки Джанго

Создать файл `.env` с переменными:

 - Обязательные переменные, для подключения к БД:
    - `DATABASES_HOST`
    - `DATABASES_PORT`
    - `DATABASES_NAME`
    - `DATABASES_USER`
    - `DATABASES_PASSWORD`

 - Пример файла `.env`:
```console
DATABASES_ENGINE=django.db.backends.postgresql
DATABASES_HOST=db.example.com
DATABASES_PORT=5432
DATABASES_NAME=production_db
DATABASES_USER=user
DATABASES_PASSWORD=password

SECRET_KEY=My secret Key

DEBUG=True

ALLOWED_HOSTS=127.0.0.1, localhost

LANGUAGE_CODE=ru-ru
TIME_ZONE=Europe/Moscow

```

## Запуск

```console
$ python manager.py runserver 127.0.0.1:8000
```

После этого переходите по ссылке [127.0.0.1:8000](http://127.0.0.1:8000), вы увидите главную страницу.

## Цели проекта

Код написан в учебных целях — это урок в курсе по Python [Devman](https://dvmn.org).


<img src="https://dvmn.org/assets/img/logo.8d8f24edbb5f.svg" alt= “” width="102" height="25">
