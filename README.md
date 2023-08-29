# RestAPI для проекта Fridge_Mon

> Все роутинги:
> [85.198.90.69:8000/api/docs](http://85.198.90.69:8000/api/docs),
> [Postman](https://www.postman.com/kansherhan/workspace/fridje-mon)

> Схему базы данных: [dbdiagram.io](https://dbdocs.io/kansherhan/refrigerator-project), пароль: 123456

## Установка

### Установка всех зависимостей, нужен Python 3.11.4 (pip 23.2.1)

```sh
pip install -r requirements.txt
```

Запустить программу:

```sh
python server.py
```

### Аргументы запуска

`--debug` - для работы в режиме отладки
`--oas` - включает документацию(OpenAPI)
`--prod` - для запуска на сервере

### Пути до файлов и картинок:

```
/api/images/get/{file_name}
```

## Решения проблем

### psycopg2

При установке на линуксе может потребовать пакеты:

```sh
# Fedora
sudo dnf install libpq-devel python3-devel gcc

# Ubuntu
sudo apt install libpq-dev python3-dev gcc
```
