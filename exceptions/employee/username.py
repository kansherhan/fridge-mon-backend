from sanic.exceptions import SanicException


class EmployeeUsernameNotCorectError(SanicException):
    status_code = 400
    message = "Логин должен содержать только буквы, цифры, точку или символ нежной подчеркивания!"
