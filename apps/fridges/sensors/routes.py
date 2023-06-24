from sanic import Blueprint, Request

routes = Blueprint("sensors", "/sensors")


@routes.get("/")
async def get_sensors(request: Request):
    pass


@routes.get("/<sensor_id:int>")
async def get_sensor(request: Request, sensor_id: int):
    pass


@routes.post("/")
async def create_sensor(request: Request):
    pass


@routes.put("/<sensor_id:int>")
async def update_sensor(request: Request, sensor_id: int):
    pass


@routes.delete("/<sensor_id:int>")
async def remove_sensor(request: Request, sensor_id: int):
    pass
