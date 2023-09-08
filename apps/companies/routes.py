from sanic import (
    Blueprint,
    json,
)
from sanic_ext import validate, openapi

from core.app.request import AppRequest

from exceptions.role.owner import (
    CannotCreateOwnerRoleError,
    CannotChangeOwnerRoleError,
)
from exceptions.role.not_found import NotFoundRoleError
from exceptions.employee.not_found import EmployeeNotFoundError
from exceptions.company.not_found import CompanyNotFoundError
from exceptions.data_forbidden import DataForbidden

from database.models.status import DataStatus
from .models import Company
from ..enterprises.models import Enterprise
from ..employees.roles.models import EmployeeRole, CompanyRole, ROLES
from ..employees.models import Employee

from .request_params import (
    CreateCompanyParams,
    UpdateCompanyParams,
    CreateCompanyRoleParams,
)

from helper import (
    models_to_json,
    models_to_dicts,
    model_is_active,
)


routes = Blueprint("companies", "/companies")


@routes.get("/")
@openapi.summary("Список компаний пользователя")
@openapi.description("Отправляет все компания в котором работает пользователь")
async def get_companies(request: AppRequest):
    def _company_exists(role_company: Company, companies: list[Company]) -> bool:
        return any(map(lambda _company: _company.id == role_company.id, companies))

    user: Employee = request.ctx.user

    companies: list[Company] = []
    user_roles: list[EmployeeRole] = user.roles

    for role in user_roles:
        current_company: Company = role.company

        if not model_is_active(current_company):
            continue

        if not _company_exists(current_company, companies):
            companies.append(current_company)

    return models_to_json(companies)


@routes.get("/<company_id:int>")
@openapi.summary("Информация о компании")
@openapi.description("Можно получить все компания по ID и их корпорации")
async def get_company(request: AppRequest, company_id: int):
    company: Company = Company.get_or_none(Company.id == company_id)

    if company == None:
        raise CompanyNotFoundError()
    elif not model_is_active(company):
        raise DataForbidden()

    company_enterprises = Enterprise.select().where(
        Enterprise.id == company.id,
        Enterprise.status == DataStatus.ACTIVE,
    )

    company_dict = company.to_dict()
    company_dict["enterprises"] = models_to_dicts(company_enterprises)

    return json(company_dict)


@routes.post("/role")
@openapi.summary("Добавить новую роль компанию")
@validate(json=CreateCompanyRoleParams)
async def create_company_role(request: AppRequest, body: CreateCompanyRoleParams):
    if not body.role.upper() in ROLES:
        raise NotFoundRoleError()

    role = CompanyRole[body.role.upper()]

    employee: Employee = Employee.get_or_none(
        Employee.username == body.username,
    )

    if employee == None:
        raise EmployeeNotFoundError()

    company: Company = Company.find_by_id(body.company)

    if company == None:
        raise CompanyNotFoundError()
    elif not model_is_active(company):
        raise DataForbidden()

    if role == CompanyRole.OWNER:
        raise CannotCreateOwnerRoleError()

    employee_role = EmployeeRole.get_or_none(
        EmployeeRole.employee == employee.id,
        EmployeeRole.company == company.id,
    )

    if employee_role == None:
        employee_role: EmployeeRole = EmployeeRole.create(
            employee=employee,
            company=company,
            role=role,
        )

        return employee_role.to_json_response()
    else:
        if employee_role.role == CompanyRole.OWNER:
            raise CannotChangeOwnerRoleError()

        employee_role.role = role
        employee_role.save()

        return employee_role.to_json_response()


@routes.post("/")
@openapi.summary("Создать компанию")
@validate(json=CreateCompanyParams)
async def create_company(request: AppRequest, body: CreateCompanyParams):
    user: Employee = request.ctx.user

    company: Company = Company.create(
        name=body.name,
    )

    role: EmployeeRole = EmployeeRole.create(
        employee=user,
        company=company,
        role=CompanyRole.OWNER,
    )

    return company.to_json_response()


@routes.patch("/<company_id:int>")
@openapi.summary("Обновить данные своей компании")
@validate(json=UpdateCompanyParams)
async def update_company(
    request: AppRequest, company_id: int, body: UpdateCompanyParams
):
    company: Company = Company.find_by_id(company_id)

    if company == None:
        raise CompanyNotFoundError()
    elif not model_is_active(company):
        raise DataForbidden()

    company.inn = body.inn
    company.name = body.name
    company.phone = body.phone
    company.email = body.email

    company.save()

    return company.to_json_response()


@routes.delete("/<company_id:int>")
@openapi.summary("Удалить компанию которым управляете")
async def delete_company(request: AppRequest, company_id: int):
    company: Company = Company.find_by_id(company_id)

    if company == None:
        raise CompanyNotFoundError()
    elif not model_is_active(company):
        raise DataForbidden()

    company.status = DataStatus.DELETE
    company.save()

    return request.empty()
