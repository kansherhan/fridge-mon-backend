from sanic.exceptions import SanicException


class HasCityError(SanicException):
    status_code = 400
    message = "С таким названием город есть!"
