from sanic import Blueprint, Request

routes = Blueprint("measurements", "/measurements")


@routes.get("/")
async def get_measurements(request: Request):
    pass


@routes.get("/<measurement_id:int>")
async def get_measurement(request: Request, measurement_id: int):
    pass


@routes.post("/")
async def create_measurement(request: Request):
    pass


@routes.put("/<measurement_id:int>")
async def update_measurement(request: Request, measurement_id: int):
    pass


@routes.delete("/<measurement_id:int>")
async def remove_measurement(request: Request, measurement_id: int):
    pass
