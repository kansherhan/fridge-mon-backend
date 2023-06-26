from sanic.exceptions import SanicException


class TokenError(SanicException):
    status_code = 400
    message = "Проблемы с токеном авторизации, проверьте существует ли он и верно ли вы указали его!"
