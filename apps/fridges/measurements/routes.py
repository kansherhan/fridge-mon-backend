from sanic import Blueprint, Request
from sanic_ext import openapi

from .models import FridgeMeasurement

from helper import models_to_json

routes = Blueprint("measurements", "/measurements")


@routes.get("/<fridge_id:int>/<count:int>")
@openapi.summary("Отправлять информацию о всех изменениях состояния холодильника")
async def get_fridge_on_measurements(request: Request, fridge_id: int, count: int):
    measurements = (
        FridgeMeasurement.select()
        .where(FridgeMeasurement.fridge == fridge_id)
        .order_by(FridgeMeasurement.created_at.desc())
        .limit(count)
    )

    return models_to_json(measurements)
