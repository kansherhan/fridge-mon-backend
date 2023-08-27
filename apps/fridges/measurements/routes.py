from sanic import Blueprint, Request
from sanic_ext import openapi

from .models import FridgeMeasurement
from ..models import Fridge

from exceptions.data_forbidden import DataForbidden

from helper import models_to_json, model_is_active

routes = Blueprint("measurements", "/measurements")


@routes.get("/<fridge_id:int>/<count:int>")
@openapi.summary("Отправлять информацию о всех изменениях состояния холодильника")
async def get_fridge_on_measurements(request: Request, fridge_id: int, count: int):
    fridge: Fridge = Fridge.find_by_id(fridge_id)

    if not model_is_active(fridge):
        raise DataForbidden()

    measurements = (
        FridgeMeasurement.select()
        .where(FridgeMeasurement.fridge == fridge_id)
        .order_by(FridgeMeasurement.created_at.desc())
        .limit(count)
    )

    return models_to_json(measurements)
