from sanic import Blueprint, Request

routes = Blueprint("manufacturers", "/manufacturers")


@routes.get("/")
async def get_manufacturers(request: Request):
    pass


@routes.get("/<manufacturer_id:int>")
async def get_manufacturer(request: Request, manufacturer_id: int):
    pass
