from sanic.exceptions import SanicException


class NotFoundEnterprise(SanicException):
    status_code = 400
    message = "Корпорация по этому айди не найдена!"
