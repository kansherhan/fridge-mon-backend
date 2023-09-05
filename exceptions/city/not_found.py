from sanic.exceptions import SanicException


class NotFoundCityError(SanicException):
    status_code = 400
    message = "С таким названием город отсутствует!"
