from sanic import Blueprint, json
from sanic_ext import validate, openapi

from exceptions.employee.not_found import EmployeeNotFoundError

from core.app.request import AppRequest

from .models import Employee
from .roles.models import EmployeeRole

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
    employee: Employee = Employee.find_by_id(employee_id)

    if employee == None:
        raise EmployeeNotFoundError()

    return employee.to_json_response()


@routes.patch("/")
@openapi.summary("Обновить данные данного пользователя")
@validate(json=UpdateEmployeeParams)
async def update_current_employee(request: AppRequest, body: UpdateEmployeeParams):
    employee: Employee = request.user

    employee.first_name = body.first_name
    employee.last_name = body.last_name
    employee.username = body.username
    employee.email = body.email

    employee.save()

    return employee.to_json_response()


@routes.get("/company/<company_id:int>")
@openapi.summary("Получить все пользователи в компании")
async def get_all_company_employees(request: AppRequest, company_id: int):
    roles: list[EmployeeRole] = EmployeeRole.select().where(
        EmployeeRole.company == company_id
    )

    employees: list[dict] = []

    for role in roles:
        employee_dict = role.employee.to_dict()
        employee_dict["role"] = role.role.value

        employees.append(employee_dict)

    return json(employees)
