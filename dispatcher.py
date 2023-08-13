from os.path import abspath
from sys import argv as sys_args

from sanic import Sanic
from sanic.config import Config
from sanic_ext import Extend
from sanic_cors.extension import CORS

from routes import register_routes
from database.connection import create_database_connection


class SanicContext:
    def __init__(self, config: Config) -> None:
        self.db = create_database_connection(
            config.DATABASE_TABLENAME,
            config.DATABASE_USERNAME,
            config.DATABASE_PASSWORD,
            config.DATABASE_HOST,
            config.DATABASE_PORT,
        )


def create_config() -> Config:
    config = Config()
    config.update_config("./config.py")

    config.DEBUG = "--debug" in sys_args
    config.OAS = config.DEBUG

    return config


def register_middlewares(app: Sanic) -> None:
    from middlewares.auth import authentication_middleware

    app.register_middleware(authentication_middleware)


def create_app() -> Sanic:
    config = create_config()

    ctx = SanicContext(config)

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
