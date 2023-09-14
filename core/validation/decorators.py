from cerberus import Validator
from cerberus.validator import BareValidator
from functools import wraps

from core.app.request import AppRequest

from exceptions.validation.request import (
    RequestDataValidateError,
    RequestDataNotJsonError,
)


__DEFAULT_ARGUMENT_NAME__ = "body"


def validate_json(
    schema,
    meta_class: object = None,
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
                document = (
                    meta_class(**validator.document)
                    if meta_class != None
                    else validator.document
                )

                kwargs[argument_name] = document

                return f(request, *args, **kwargs)
            else:
                raise RequestDataValidateError(context=validator.errors)

        return wrapper

    return vd


# TODO: Доделать для параметров этот декоратор
def validate_args(schema, argument_name=__DEFAULT_ARGUMENT_NAME__):
    validator: BareValidator = Validator(schema)

    def vd(f):
        @wraps(f)
        def wrapper(request: AppRequest, *args, **kwargs):
            validation_passed = validator.validate(dict(request.query_args))

            if validation_passed:
                kwargs[argument_name] = validator.document

                return f(request, *args, **kwargs)
            else:
                raise RequestDataValidateError(context=validator.errors)

        return wrapper

    return vd
