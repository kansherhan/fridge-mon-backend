from sanic.exceptions import SanicException


class NotFoundCountyError(SanicException):
    status_code = 400
    message = "С таким названием страна отсутствует!"
