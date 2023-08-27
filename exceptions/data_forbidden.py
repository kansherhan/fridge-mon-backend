from sanic.exceptions import SanicException


class DataForbidden(SanicException):
    status_code = 400
    message = "Данные которые вы просите были удалены или были архивированы, пожалуйста активируйте их чтобы получить данные!"
