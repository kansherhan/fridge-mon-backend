from sanic.exceptions import SanicException


class TokenError(SanicException):
    status_code = 400
    message = "Проблемы с токеном авторизации, проверьте верно ли вы указали его!"


class TokenNotFoundError(SanicException):
    status_code = 400
    message = "Проблемы с токеном авторизации, проверьте существует ли он!"


class TokenLifeCycleError(SanicException):
    status_code = 400
    message = "Ваш токен уже старый, обновите его!"
