# RestAPI для проекта Fridge_Mon

Установка всех зависимостей, нужен Python 3.9.13 (pip 22.0.4)

```sh
pip install -r requirements.txt
```

Запустить программу:

```sh
python server.py
```

Запустить программу в режиме разработчика:

```sh
python server.py --debug
```

> Можно совмещать аргументы для запуска

> Что бы посмотреть все роутинги: [localhost:8000/apidocs](http://localhost:8000/apidocs), [postman](https://www.postman.com/kansherhan/workspace/fridje-mon)

Пути до файлов и картинок:

```
/uploads/images/companies/{file_name}
/uploads/images/enterprises/{file_name}
/uploads/images/employees/{file_name}
```
