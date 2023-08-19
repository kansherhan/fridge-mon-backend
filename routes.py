from sanic import Sanic, Request
from sanic.response import text

from core.routing import Routing


def _register_base_routes(app: Sanic) -> None:
    @app.get("/")
    async def main_page(request: Request):
        return text("Hello, World!")


def register_routes(app: Sanic) -> None:
    _register_base_routes(app)

    Routing.RegisterRedirectRoutes(app)
    Routing.RegisterAppsRoutes(app)
