from sanic.exceptions import SanicException


class CannotCreateOwnerRoleError(SanicException):
    status_code = 400
    message = "Нельзя создать роль создателя!"


class CannotChangeOwnerRoleError(SanicException):
    status_code = 400
    message = "Нельзя менять роль создателя компании!"
