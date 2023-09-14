from sanic.exceptions import SanicException


class CityNotFoundError(SanicException):
    status_code = 400
    message = "С таким названием город отсутствует!"
