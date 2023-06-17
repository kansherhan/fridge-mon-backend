from sanic import Blueprint, Request, json
from sanic.exceptions import NotFound

from .models import FridgeManufacturer as Manufacturer

routes = Blueprint("manufacturers", "/manufacturers")


@routes.get("/")
async def get_manufacturers(request: Request):
    manufacturers: list[Manufacturer] = Manufacturer.find_all()

    manufacturer_dicts = [m.to_dict() for m in manufacturers]

    return json(manufacturer_dicts)


@routes.get("/<manufacturer_id:int>")
async def get_manufacturer(request: Request, manufacturer_id: int):
    manufacturer: Manufacturer = Manufacturer.find_by_id(manufacturer_id)

    if manufacturer != None:
        return manufacturer.to_json_response()
    else:
        raise NotFound(f"Could not find manufacturer with id = {manufacturer_id}")
