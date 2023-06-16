from sanic import Blueprint

from .manufacturers.routes import routes as manufacturers_routes
from .categories.routes import routes as categories_routes

fridges_routes = Blueprint("fridges", "/")

routes = Blueprint.group(
    fridges_routes, manufacturers_routes, categories_routes, url_prefix="/fridges"
)
