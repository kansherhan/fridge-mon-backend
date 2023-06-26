from sanic import Blueprint, Request

from .models import Fridge

from .manufacturers.routes import routes as manufacturers_routes
from .categories.routes import routes as categories_routes
from .products.routes import routes as products_routes
from .sensors.routes import routes as sensors_routes

from helper import models_to_json

__FRIDGE_BASE_PATH__ = "/<enterprises_id:int>"
__FRIDGE_WITH_ID_PATH__ = f"{__FRIDGE_BASE_PATH__}/<fridge_id:int>"

fridges_routes = Blueprint("fridges", "/")


@fridges_routes.get(__FRIDGE_BASE_PATH__)
async def get_fridges_on_enterprises(request: Request, enterprises_id: int):
    fridges: list[Fridge] = (
        Fridge.select().where(Fridge.enterprise == enterprises_id).order_by(Fridge.id)
    )

    return models_to_json(fridges)


@fridges_routes.post(__FRIDGE_BASE_PATH__)
async def create_fridge(request: Request, enterprises_id: int):
    pass


@fridges_routes.put(__FRIDGE_WITH_ID_PATH__)
async def update_fridge(request: Request, enterprises_id: int, fridge_id: int):
    pass


@fridges_routes.delete(__FRIDGE_WITH_ID_PATH__)
async def remove_fridge(request: Request, enterprises_id: int, fridge_id: int):
    pass


routes = Blueprint.group(
    fridges_routes,
    manufacturers_routes,
    categories_routes,
    products_routes,
    sensors_routes,
    url_prefix="/fridges",
)
