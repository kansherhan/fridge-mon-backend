from sanic import Blueprint, json
from sanic_ext import openapi

from core.app.request import AppRequest

from .models import FridgeMeasurement
from ..models import Fridge

from exceptions.fridge.not_found import FridgeNotFoundError

from helper import model, models_to_dicts


routes = Blueprint("measurements", "/measurements")


@routes.get("/<fridge_id:int>/<count:int>")
@openapi.summary("Отправлять информацию о всех изменениях состояния холодильника")
async def get_fridge_on_measurements(request: AppRequest, fridge_id: int, count: int):
    fridge: Fridge = model(
        model=Fridge.find_by_id(fridge_id),
        not_found_exception=FridgeNotFoundError,
    )

    fridge_dict: dict = fridge.to_dict()

    measurements = (
        FridgeMeasurement.select()
        .where(FridgeMeasurement.fridge == fridge_id)
        .order_by(FridgeMeasurement.created_at.desc())
        .limit(count)
    )

    fridge_dict["measurements"] = models_to_dicts(measurements)

    return json(fridge_dict)
