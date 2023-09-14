from sanic import json
from sanic.exceptions import SanicException, BadRequest

from exceptions.data_forbidden import DataForbidden

from database.models.base import BaseModel
from database.models.status import DataStatus


def models_to_dicts(modals: list[BaseModel]) -> list[BaseModel]:
    return [item.to_dict() for item in modals]


def models_to_json(modals: list[BaseModel]) -> str:
    return json(models_to_dicts(modals))


def model(
    model: BaseModel,
    not_found_exception: SanicException = BadRequest,
    data_forbidden: SanicException = DataForbidden,
) -> BaseModel:
    if model == None:
        raise not_found_exception()
    elif hasattr(model, "status") and model.status != DataStatus.ACTIVE:
        raise data_forbidden()

    return model
