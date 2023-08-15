from os.path import abspath
from sys import argv as sys_args

from sanic import Sanic
from sanic.config import Config
from sanic_ext import Extend
from sanic_cors.extension import CORS

from core.app.context import AppContext

from routes import register_routes


def create_config() -> Config:
    config = Config()
    config.update_config("./config.py")

    config.DEBUG = "--debug" in sys_args
    config.OAS = config.DEBUG

    return config


def register_middlewares(app: Sanic) -> None:
    from middlewares.auth import authentication_middleware
    from middlewares.db import reload_db_connect

    app.register_middleware(reload_db_connect)
    app.register_middleware(authentication_middleware)


def create_app() -> Sanic:
    config = create_config()

    ctx = AppContext(config)

    app = Sanic(config.APP_NAME, config=config, ctx=ctx)
    Extend(
        app,
        extensions=[
            CORS,
        ],
        config=config,
    )

    register_routes(app)
    register_middlewares(app)

    app.static("/uploads", abspath("./uploads"), name="uploads")

    return app
