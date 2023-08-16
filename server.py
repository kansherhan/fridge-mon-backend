from sanic import Sanic
from sanic.config import Config
from sanic.worker.loader import AppLoader

from dispatcher import create_app


def bootstrap():
    loader: AppLoader = AppLoader(factory=create_app)
    app: Sanic = loader.load()
    config: Config = app.config

    app.prepare(
        host=config.APP_HOST,
        port=config.APP_PORT,
        dev=config.DEBUG,
        auto_reload=config.DEBUG,
        fast=not config.DEBUG,
        access_log=config.DEBUG,
        unix=config.APP_UNIX,
    )
    Sanic.serve(primary=app, app_loader=loader)


if __name__ == "__main__":
    bootstrap()
