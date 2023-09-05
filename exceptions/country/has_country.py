from sanic.exceptions import SanicException


class HasCountryError(SanicException):
    status_code = 400
    message = "С таким названием страна есть!"
