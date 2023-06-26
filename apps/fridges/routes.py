from sanic import Blueprint, Request

from .models import Fridge

from .manufacturers.routes import routes as manufacturers_routes
from .categories.routes import routes as categories_routes
from .products.routes import routes as products_routes
from .sensors.routes import routes as sensors_routes

from helper import models_to_json

from ..enterprises.models import Enterprise


fridges_routes = Blueprint("fridges", "/")


@fridges_routes.get("/enterprise/<enterprises_id:int>/fridge/<fridge_id:int>")
async def get_fridges_on_enterprises(request: Request, enterprises_id: int):
    """Об всех холодильников в корпорации"""

    enterprise: Enterprise = Enterprise.get_or_none(Enterprise.id == enterprises_id)

    return models_to_json(enterprise.fridges)


routes = Blueprint.group(
    fridges_routes,
    manufacturers_routes,
    categories_routes,
    products_routes,
    sensors_routes,
    url_prefix="/fridges",
)
