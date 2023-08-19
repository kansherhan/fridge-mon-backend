from importlib import import_module
from os import path, listdir

from sanic import Sanic
from sanic.config import Config
from sanic.blueprint_group import BlueprintGroup
from sanic.response import redirect


class Routing:
    __APPS_ROUTES_FILE__ = "routes"
    __APPS_ROUTE_VAR_NAME__ = "routes"

    @classmethod
    def RegisterRedirectRoutes(cls, app: Sanic) -> None:
        config: Config = app.config
        redirects_routes = config.REDIRECTS_URLS

        for url, redirect_url in redirects_routes.items():
            app.route(url)(lambda *_, **__: redirect(redirect_url))

    @classmethod
    def RegisterAppsRoutes(cls, app: Sanic) -> BlueprintGroup:
        config: Config = app.config

        apps_folder_names = listdir(config.APPS_FOLDER_PATH)
        routes_group = BlueprintGroup(url_prefix=config.ROUTE_PREFIX)

        for app_name in apps_folder_names:
            app_routes_file = cls.__create_route_path(
                config.APPS_FOLDER_PATH,
                app_name,
            )

            if path.exists(app_routes_file):
                routes_group.append(
                    cls.__import_module(
                        config.APPS_FOLDER_NAME,
                        app_name,
                    )
                )

        app.blueprint(routes_group)

    @classmethod
    def __create_route_path(cls, root_path, app_name: str) -> str:
        return path.join(
            root_path,
            app_name,
            cls.__APPS_ROUTES_FILE__ + ".py",
        )

    @classmethod
    def __import_module(cls, app_folder_name: str, app_name: str):
        module_path = f"{app_folder_name}.{app_name}.{cls.__APPS_ROUTES_FILE__}"

        route_module = import_module(module_path)

        if hasattr(module_path, cls.__APPS_ROUTE_VAR_NAME__):
            raise RuntimeError(
                f"В файле у приложения '{app_name}' отсутствует параметр '{cls.__APPS_ROUTE_VAR_NAME__}'!"
            )

        return route_module.routes
