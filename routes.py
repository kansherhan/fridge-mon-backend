from importlib import import_module
from os import path, listdir

from sanic import Sanic, Request
from sanic.blueprint_group import BlueprintGroup
from sanic.response import redirect, text

__APPS_ROUTES_FILE__ = "routes"
__APPS_ROUTE_VAR_NAME__ = "routes"


def _register_routes(app: Sanic):
    @app.get("/", ctx_unauthorized_request=True)
    async def main_page(request: Request):
        return text("Hello, World!")


def _register_redirect_routes(app: Sanic):
    redirects_routes = app.config.REDIRECTS

    for url, redirect_url in redirects_routes.items():
        app.route(url)(lambda *_, **__: redirect(redirect_url))


def _register_apps_routes(
    main_app_name: str,
    app_root_path: str,
    route_prefix: str,
) -> BlueprintGroup:
    def _create_route_path(app_name: str):
        return path.join(
            app_root_path,
            app_name,
            __APPS_ROUTES_FILE__ + ".py",
        )

    def _import_module(app_name: str):
        module_path = f"{main_app_name}.{app_name}.{__APPS_ROUTES_FILE__}"

        route_module = import_module(module_path)

        if hasattr(module_path, __APPS_ROUTE_VAR_NAME__):
            raise RuntimeError(
                f"В файле у приложения '{app_name}' отсутствует параметр '{__APPS_ROUTE_VAR_NAME__}'!"
            )

        return route_module.routes

    apps_folder_names = listdir(app_root_path)
    routes_group = BlueprintGroup(url_prefix=route_prefix)

    for app_name in apps_folder_names:
        app_routes_file = _create_route_path(app_name)

        if path.exists(app_routes_file):
            routes_group.append(_import_module(app_name))

    return routes_group


def register_routes(app: Sanic):
    _register_routes(app)
    _register_redirect_routes(app)

    app.blueprint(
        _register_apps_routes(
            app.config.APPS_FOLDER_NAME,
            app.config.APPS_FOLDER_PATH,
            app.config.ROUTE_PREFIX,
        )
    )
