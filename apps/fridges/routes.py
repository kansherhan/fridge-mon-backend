from sanic import Blueprint, Request

from .manufacturers.routes import routes as manufacturers_routes
from .categories.routes import routes as categories_routes

__FRIDGE_BASE_PATH__ = "/<enterprises_id:int>"
__FRIDGE_WITH_ID_PATH__ = f"{__FRIDGE_BASE_PATH__}/<fridge_id:int>"

fridges_routes = Blueprint("fridges", "/")


@fridges_routes.get(__FRIDGE_BASE_PATH__)
async def get_fridges(request: Request, enterprises_id: int):
    pass


@fridges_routes.get(__FRIDGE_WITH_ID_PATH__)
async def get_fridge(request: Request, enterprises_id: int, fridge_id: int):
    pass


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
    fridges_routes, manufacturers_routes, categories_routes, url_prefix="/fridges"
)
