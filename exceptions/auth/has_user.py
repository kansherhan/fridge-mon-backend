from sanic.exceptions import SanicException


class HasUserError(SanicException):
    status_code = 400
    message = "Такой пользователь уже есть, выведите другой!"
