from sanic import Blueprint, Request

routes = Blueprint("employees", "/employees")


@routes.get("/")
async def get_employees(request: Request):
    pass


@routes.get("/<employee_id:int>")
async def get_employee(request: Request, _id: int):
    pass


@routes.post("/<employee_id:int>")
async def create_employee(request: Request, _id: int):
    pass


@routes.put("/<employee_id:int>")
async def update_employee(request: Request, _id: int):
    pass


@routes.delete("/<employee_id:int>")
async def remove_employee(request: Request, _id: int):
    pass
