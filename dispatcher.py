from os.path import abspath
from sys import argv as sys_args

from sanic import Sanic
from sanic.config import Config

from routes import create_routes
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

    config.APP_DEBUG = "--debug" in sys_args
    config.AUTHORIZATION = not "--no-auth" in sys_args
    config.OAS = config.APP_DEBUG

    return config


def create_app() -> Sanic:
    config = create_config()

    ctx = SanicContext(config)

    app = Sanic(config.APP_NAME, config=config, ctx=ctx)

    create_routes(app)
    register_middlewares(app)

    app.static("/uploads", abspath("./uploads"), name="uploads")

    return app


def register_middlewares(app: Sanic):
    from middlewares.auth import authentication_middleware

    app.register_middleware(authentication_middleware)
