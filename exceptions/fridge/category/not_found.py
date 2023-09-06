from sanic.exceptions import SanicException


class FridgeCategoryNotFoundError(SanicException):
    status_code = 400
    message = "По такому айди категория отсутствует!"
