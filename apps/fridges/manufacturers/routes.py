from sanic import Blueprint, Request

from .models import FridgeManufacturer as Manufacturer
from helper import models_to_json, model_not_none

routes = Blueprint("manufacturers", "/manufacturers")


@routes.get("/")
async def get_manufacturers(request: Request):
    """Получить все виды брендов холодильников"""

    manufacturers: list[Manufacturer] = Manufacturer.find_all()

    return models_to_json(manufacturers)


@routes.get("/<manufacturer_id:int>")
async def get_manufacturer(request: Request, manufacturer_id: int):
    """Получить один бренд холодильников"""

    manufacturer: Manufacturer = Manufacturer.find_by_id(manufacturer_id)

    return model_not_none(manufacturer).to_json_response()
