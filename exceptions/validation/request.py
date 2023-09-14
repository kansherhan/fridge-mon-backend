from sanic.exceptions import SanicException


class RequestDataValidateError(SanicException):
    status_code = 400
    message = "!"


class RequestDataNotJsonError(SanicException):
    status_code = 400
    message = "!"
