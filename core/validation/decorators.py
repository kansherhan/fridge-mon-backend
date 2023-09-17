from cerberus import Validator
from cerberus.validator import BareValidator
from functools import wraps

from core.app.request import AppRequest

from exceptions.validation.request import (
    RequestDataValidateError,
    RequestDataNotJsonError,
)


__DEFAULT_ARGUMENT_NAME__ = "body"


def __create_dto(dto: object, validator: BareValidator):
    if dto != None:
        return dto(**validator.document)
    else:
        return validator.document


def validate_json(
    schema,
    dto: object = None,
    argument_name=__DEFAULT_ARGUMENT_NAME__,
):
    validator: BareValidator = Validator(schema)

    def vd(f):
        @wraps(f)
        def wrapper(request: AppRequest, *args, **kwargs):
            if request.json is None:
                raise RequestDataNotJsonError()

            validation_passed = validator.validate(request.json)

            if validation_passed:
                document = __create_dto(dto, validator)

                kwargs[argument_name] = document

                return f(request, *args, **kwargs)
            else:
                raise RequestDataValidateError(context=validator.errors)

        return wrapper

    return vd


def validate_args(
    schema,
    dto: object = None,
    argument_name=__DEFAULT_ARGUMENT_NAME__,
):
    validator: BareValidator = Validator(schema)

    def vd(f):
        @wraps(f)
        def wrapper(request: AppRequest, *args, **kwargs):
            validation_passed = validator.validate(dict(request.query_args))

            if validation_passed:
                document = __create_dto(dto, validator)

                kwargs[argument_name] = document

                return f(request, *args, **kwargs)
            else:
                raise RequestDataValidateError(context=validator.errors)

        return wrapper

    return vd
