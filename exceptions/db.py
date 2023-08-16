from sanic.exceptions import SanicException


class DBError(SanicException):
    status_code = 400
    message = "Проблемы с подключением базы данных!"
