from os.path import abspath

from sanic import Sanic
from sanic.config import Config

from routes import create_routes
from database.connection import create_database_connection
from middlewares.auth import authentication_middleware


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

    return config


def create_app(debug: bool) -> Sanic:
    config = create_config()
    config.APP_DEBUG = config.OAS = debug

    ctx = SanicContext(config)

    app = Sanic(config.APP_NAME, config=config, ctx=ctx)

    create_routes(app)

    app.register_middleware(authentication_middleware)

    app.static("/assets", abspath("./assets"))

    return app
