from sanic import json
from sanic.exceptions import BadRequest

from database.models.base import BaseModel
from database.models.status import DataStatus


def models_to_dicts(modals: list[BaseModel]) -> list:
    return [item.to_dict() for item in modals]


def models_to_json(modals: list[BaseModel]) -> str:
    return json(models_to_dicts(modals))


def model_not_none(model: BaseModel, message: str = None) -> any:
    if model != None:
        return model
    else:
        raise BadRequest(message)


def model_is_active(model: BaseModel) -> bool:
    return model.status == DataStatus.ACTIVE
