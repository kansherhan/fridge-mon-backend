from sanic import Blueprint, Request

routes = Blueprint("auth", "/auth")


@routes.post("/login", ctx_unauthorized_request=True)
async def login(request: Request):
    pass


@routes.post("/logout")
async def logout(request: Request):
    pass


@routes.post("/registration", ctx_unauthorized_request=True)
async def registration(request: Request):
    pass
