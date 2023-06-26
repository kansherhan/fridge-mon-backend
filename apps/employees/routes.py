from sanic import Blueprint, Request

from .models import Employee
from helper import model_not_none

routes = Blueprint("employees", "/employees")


@routes.get("/")
async def get_current_employees(request: Request):
    employee: Employee = request.ctx.user

    return employee.to_json_response()


@routes.get("/<employee_id:int>")
async def get_employee(request: Request, employee_id: int):
    employee: Employee = Employee.get_or_none(Employee.id == employee_id)

    return model_not_none(employee).to_json_response()
