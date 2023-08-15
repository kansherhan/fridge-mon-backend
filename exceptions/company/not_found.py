from sanic.exceptions import SanicException


class CompanyNotFoundError(SanicException):
    status_code = 400
    message = "По такому айди компания отсутствует!"
