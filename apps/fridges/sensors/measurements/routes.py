from sanic import Blueprint, Request
from sanic_ext import validate

from .models import FridgeSensorMeasurement as SensorMeasurement
from .request_params import CreateManufacturersParams

from helper import models_to_json

routes = Blueprint("measurements", "/measurements")


@routes.get("/<sensor_id:int>")
async def get_sensor_on_measurements(
    request: Request,
    sensor_id: int,
):
    """Отправлять информацию о всех изменениях состояния сенсора"""

    measurements = (
        SensorMeasurement.select()
        .where(SensorMeasurement.sensor == sensor_id)
        .order_by(SensorMeasurement.created_at.desc())
        .limit(10)
    )

    return models_to_json(measurements)


@routes.post("/save")
@validate(json=CreateManufacturersParams)
async def fridge_manufacturers_save(request: Request, body: CreateManufacturersParams):
    pass
