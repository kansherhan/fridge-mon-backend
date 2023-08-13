from sanic.exceptions import SanicException


class NotFoundCompany(SanicException):
    status_code = 400
    message = "По такому айди компания отсутствует!"
