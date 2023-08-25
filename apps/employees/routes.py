import bcrypt

from sanic import Blueprint
from sanic_ext import validate, openapi

from core.app.request import AppRequest

from peewee import Query
from .models import Employee

from helper import model_not_none
from .request_params import UpdateEmployeeParams

routes = Blueprint("employees", "/employees")


@routes.get("/me")
@openapi.summary("Данные о текущем пользователе")
async def get_current_employee(request: AppRequest):
    employee: Employee = request.user

    return employee.to_json_response()


@routes.get("/<employee_id:int>")
@openapi.summary("Вся информация об пользователе поего ID")
async def get_employee(request: AppRequest, employee_id: int):
    employee: Employee = Employee.get_or_none(Employee.id == employee_id)

    return model_not_none(employee).to_json_response()


@routes.patch("/")
@openapi.summary("Обновить данные данного пользователя")
@validate(json=UpdateEmployeeParams)
async def update_current_employee(request: AppRequest, body: UpdateEmployeeParams):
    employee: Employee = request.user

    password_hash = bcrypt.hashpw(
        body.password.encode(),
        bcrypt.gensalt(),
    )

    query: Query = employee.update(
        {
            Employee.first_name: body.first_name,
            Employee.last_name: body.last_name,
            Employee.email: body.email,
            Employee.password: password_hash,
        }
    ).where(Employee.id == employee.id)

    query.execute()

    return request.empty()
