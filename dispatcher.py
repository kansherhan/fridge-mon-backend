from sys import argv as sys_args

from sanic import Sanic
from sanic.config import Config
from sanic.middleware import Middleware, MiddlewareLocation
from sanic_ext import Extend as SanicExtensionManager
from sanic_cors.extension import CORS as CORSExtension

from core.app.request import AppRequest
from core.app.context import AppContext
from core.listener.event import ListenerEvent

from routes import register_routes


def create_config() -> Config:
    config = Config()
    config.update_config("./config.py")

    config.DEBUG = "--debug" in sys_args
    config.OAS = "--oas" in sys_args
    config.MIGRATION = "--migrate" in sys_args

    if config.DEBUG == True:
        config.OAS = True
        config.APP_UNIX = None

    return config


def register_middlewares(app: Sanic) -> None:
    from middlewares.auth import authentication_middleware

    middlewares = [
        Middleware(
            func=authentication_middleware,
            location=MiddlewareLocation.REQUEST,
            priority=10,
        ),
    ]

    for middleware in middlewares:
        app.register_middleware(middleware)


def register_listeners(app: Sanic) -> None:
    from listeners.migration import register_migrate_task

    listeners = [
        (register_migrate_task, ListenerEvent.AFTER_SERVER_START),
    ]

    for func, event in listeners:
        app.register_listener(func, event.value)


def create_app() -> Sanic:
    config = create_config()
    ctx = AppContext(config)

    app = Sanic(
        name=config.APP_NAME,
        config=config,
        request_class=AppRequest,
        ctx=ctx,
    )

    ctx.extend = SanicExtensionManager(
        app,
        extensions=[
            CORSExtension,
        ],
        config=app.config,
    )

    register_routes(app)
    register_middlewares(app)
    register_listeners(app)

    return app
