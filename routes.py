from importlib import import_module
from os import path, listdir

from sanic import Sanic, Request
from sanic.response import redirect, text

__APPS_ROUTES_FILE__ = "routes"


def register_routes(app: Sanic):
    @app.get("/")
    async def main_page(request: Request):
        return text("Hello, World!")


def register_redirect_routes(app: Sanic):
    redirects_routes = app.config.REDIRECTS

    for url, redirect_url in redirects_routes.items():
        app.route(url)(lambda *_, **__: redirect(redirect_url))


def importAppsRoutes(app: Sanic):
    apps_folder_names = listdir(app.config.APPS_FOLDER_PATH)

    for app_name in apps_folder_names:
        app_routes_file = path.join(
            app.config.APPS_FOLDER_PATH, app_name, __APPS_ROUTES_FILE__ + ".py"
        )

        if path.exists(app_routes_file):
            app_route_module = import_module(
                f"{app.config.APPS_FOLDER_NAME}.{app_name}.{__APPS_ROUTES_FILE__}"
            )

            app.blueprint(app_route_module.routes)


def create_routes(app: Sanic):
    register_routes(app)
    register_redirect_routes(app)

    importAppsRoutes(app)
