from sanic.exceptions import SanicException


class TokenNotFoundError(SanicException):
    status_code = 400
    message = "Проблемы с токеном авторизации, проверьте существует ли он!"


class TokenError(SanicException):
    status_code = 400
    message = "Проблемы с токеном авторизации, проверьте верно ли вы указали его!"
