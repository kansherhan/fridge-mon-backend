from sanic.exceptions import SanicException


class LoginError(SanicException):
    status_code = 400
    message = "Неправильный логин или пароль!"
