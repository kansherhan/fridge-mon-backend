from sanic.exceptions import SanicException


class FridgeManufacturerNotFoundError(SanicException):
    status_code = 400
    message = "По такому айди производитель холодильника отсутствует!"
