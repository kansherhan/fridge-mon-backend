from sanic.exceptions import SanicException


class CountyNotFoundError(SanicException):
    status_code = 400
    message = "С таким названием страна отсутствует!"
