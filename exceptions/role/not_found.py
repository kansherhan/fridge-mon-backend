from sanic.exceptions import SanicException


class NotFoundRoleError(SanicException):
    status_code = 400
    message = "Такой роли нету!"
