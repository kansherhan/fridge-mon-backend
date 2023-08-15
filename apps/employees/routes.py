import bcrypt

from sanic import (
    Blueprint,
    Request,
    empty as empty_response,
)
from sanic_ext import validate, openapi

from .request_params import UpdateEmployeeParams

from .models import Employee

from helper import model_not_none


routes = Blueprint("employees", "/employees")


@routes.get("/")
@openapi.summary("Данные о текущем пользователе")
async def get_current_employee(request: Request):
    employee: Employee = request.ctx.user

    return employee.to_json_response()


@routes.get("/<employee_id:int>")
@openapi.summary("Вся информация об пользователе поего ID")
async def get_employee(request: Request, employee_id: int):
    employee: Employee = Employee.get_or_none(Employee.id == employee_id)

    return model_not_none(employee).to_json_response()


@routes.patch("/")
@openapi.summary("Обновить данные данного пользователя")
@validate(json=UpdateEmployeeParams)
async def update_current_employee(request: Request, body: UpdateEmployeeParams):
    employee: Employee = request.ctx.user

    password_hash = bcrypt.hashpw(
        body.password.encode(),
        bcrypt.gensalt(),
    )

    query = employee.update(
        {
            Employee.first_name: body.first_name,
            Employee.last_name: body.last_name,
            Employee.email: body.email,
            Employee.password: password_hash,
        }
    ).where(Employee.id == employee.id)

    query.execute()

    return empty_response()
