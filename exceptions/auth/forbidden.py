from sanic.exceptions import SanicException


class ForbiddenError(SanicException):
    status_code: int = 403
    quiet: bool = True
    message: str = "У вас отсутствует права на этот ресурс или действие!"
