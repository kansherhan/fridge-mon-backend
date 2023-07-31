from sanic import Sanic
from sanic.worker.loader import AppLoader

from dispatcher import create_app


def bootstrap():
    loader = AppLoader(factory=create_app)
    app = loader.load()

    app.prepare(
        host=app.config.APP_HOST,
        port=app.config.APP_PORT,
        dev=app.config.DEBUG,
        auto_reload=True,
        fast=not app.config.DEBUG,
    )
    Sanic.serve(primary=app, app_loader=loader)


if __name__ == "__main__":
    bootstrap()
