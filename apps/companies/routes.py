from sanic import (
    Blueprint,
    Request,
    json,
    empty as empty_response,
)
from sanic_ext import validate

from exceptions.company.not_found import NotFoundCompany

from .models import Company
from ..employees.roles.models import EmployeeRole, CompanyRole
from ..employees.models import Employee

from .request_params import (
    CreateCompanyParams,
    UpdateCompanyParams,
)

from helper import models_to_json, model_not_none, models_to_dicts

routes = Blueprint("companies", "/companies")


@routes.get("/")
async def get_companies(request: Request):
    """Отправляет все компания в котором работает пользователь"""

    def _company_exists(role_company: Company, companies: list[Company]) -> bool:
        return any(map(lambda _company: _company.id == role_company.id, companies))

    user: Employee = request.ctx.user

    companies: list[Company] = []
    user_roles: list[EmployeeRole] = user.roles

    for role in user_roles:
        role_company: Company = role.company

        if not _company_exists(role_company, companies):
            companies.append(role_company)

    return models_to_json(companies)


@routes.get("/<company_id:int>")
async def get_company(request: Request, company_id: int):
    """Можно получить все компания по ID и их корпорации"""

    company: Company = model_not_none(Company.get_or_none(Company.id == company_id))

    company_dict = company.to_dict()
    company_dict["enterprises"] = models_to_dicts(company.enterprises)

    return json(company_dict)


@routes.post("/")
@validate(json=CreateCompanyParams)
async def create_company(request: Request, body: CreateCompanyParams):
    user: Employee = request.ctx.user

    company: Company = Company.create(
        inn=body.inn,
        name=body.name,
    )

    role: EmployeeRole = EmployeeRole.create(
        employee=user,
        company=company,
        role=CompanyRole.OWNER,
    )

    return company.to_json_response()


@routes.patch("/<company_id:int>")
@validate(json=UpdateCompanyParams)
async def update_company(request: Request, company_id: int, body: UpdateCompanyParams):
    query = Company.update(
        {
            Company.inn: body.inn,
            Company.name: body.name,
            Company.phone: body.phone,
            Company.email: body.email,
        }
    ).where(Company.id == company_id)

    query.execute()

    return empty_response()


@routes.delete("/<company_id:int>")
async def delete_company(request: Request, company_id: int):
    company: Company = Company.find_by_id(company_id)

    if company == None:
        raise NotFoundCompany()

    company.delete_instance()

    return empty_response()
