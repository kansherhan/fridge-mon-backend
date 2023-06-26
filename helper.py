from sanic import json
from sanic.exceptions import NotFound

from database.base_models import BaseModel


def models_to_dicts(modals: list[BaseModel]):
    return [item.to_dict() for item in modals]


def models_to_json(modals: list[BaseModel]):
    return json(models_to_dicts(modals))


def model_not_none(model: BaseModel, message: str = None):
    if model != None:
        return model
    else:
        raise NotFound(message)
