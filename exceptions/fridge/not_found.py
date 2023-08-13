from sanic.exceptions import SanicException


class NotFoundFridge(SanicException):
    status_code = 400
    message = "По такому айди холодильник отсутствует!"
