from sanic import Blueprint, Request, json

from ..models import Fridge
from .measurements.models import FridgeSensorMeasurement as SensorMeasurement

from .measurements.routes import routes as measurements_routes

sensor_routes = Blueprint("sensors", "/")


@sensor_routes.get("/<fridge_id:int>")
async def get_sensors_by_fridges(request: Request, fridge_id: int):
    """Отправлять информацию о сенсорах в холодильнике"""

    fridge: Fridge = Fridge.get_or_none(Fridge.id == fridge_id)

    fridge_sensors: list[dict] = []

    for sensor in fridge.sensors:
        sensor_dict = sensor.to_dict()

        measurement: SensorMeasurement = SensorMeasurement.get_or_none(
            SensorMeasurement.sensor == sensor.id
        )

        if measurement != None:
            sensor_dict["measurement"] = measurement.to_dict()

        fridge_sensors.append(sensor_dict)

    return json(fridge_sensors)


routes = Blueprint.group(
    sensor_routes,
    measurements_routes,
    url_prefix="/sensors",
)
