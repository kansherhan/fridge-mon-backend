from sanic.exceptions import SanicException


class FridgeNotFoundError(SanicException):
    status_code = 400
    message = "По такому айди холодильник отсутствует!"
