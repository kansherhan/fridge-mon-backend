from sys import argv as sys_args
from functools import partial

from sanic import Sanic
from sanic.worker.loader import AppLoader

from dispatcher import create_app


def bootstrap(debug: bool):
    loader = AppLoader(factory=partial(create_app, debug))
    app = loader.load()

    app.prepare(
        host=app.config.APP_HOST,
        port=app.config.APP_PORT,
        dev=app.config.APP_DEBUG,
        auto_reload=True,
    )
    Sanic.serve(primary=app, app_loader=loader)


if __name__ == "__main__":
    bootstrap("--debug" in sys_args)
