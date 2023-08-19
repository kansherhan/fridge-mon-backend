from sanic.exceptions import SanicException


class ImageNotFoundError(SanicException):
    status_code = 400
    message = "Отсутствует изображения!"
