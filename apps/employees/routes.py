from sanic import Blueprint, Request

from .models import Employee

routes = Blueprint("employees", "/employees")


@routes.get("/")
async def get_current_employees(request: Request):
    employee: Employee = request.ctx.user

    return employee.to_json_response()


@routes.get("/<employee_id:int>")
async def get_employee(request: Request, _id: int):
    pass


@routes.put("/<employee_id:int>")
async def update_employee(request: Request, _id: int):
    pass


@routes.delete("/<employee_id:int>")
async def remove_employee(request: Request, _id: int):
    pass
