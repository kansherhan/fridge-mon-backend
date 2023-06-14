from sanic import Blueprint, Request, text

routes = Blueprint("main", "/main")


@routes.get("/")
async def test_route(request: Request):
    return text("Work!")
