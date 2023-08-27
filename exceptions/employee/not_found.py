from sanic.exceptions import SanicException


class EmployeeNotFoundError(SanicException):
    status_code = 400
    message = "По этим данным пользователя не нашли!"
