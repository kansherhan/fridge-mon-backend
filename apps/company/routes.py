from sanic import Blueprint, Request, json

from .models import Company
from ..employees.roles.models import CompanyRole
from ..employees.models import Employee
from ..enterprises.models import Enterprise

from helper import models_to_json, model_not_none

routes = Blueprint("companies", "/companies")


@routes.get("/")
async def get_companies(request: Request):
    def _company_exists(role_company: Company, companies: list[Company]) -> bool:
        return any(map(lambda _company: _company.id == role_company.id, companies))

    user: Employee = request.ctx.user

    companies: list[Company] = []

    for role in user.roles:
        role_company: Company = role.company

        if not _company_exists(role_company, companies):
            companies.append(role_company)

    return models_to_json(companies)


@routes.get("/<company_id:int>")
async def get_company(request: Request, company_id: int):
    query: list[Company] = (
        Company.select(Company, Enterprise)
        .join(Enterprise)
        .where(Company.id == company_id)
    )

    enterprises = [company.enterprise.to_dict() for company in query]

    company = model_not_none(query[0]).to_dict()
    company["enterprises"] = enterprises

    return json(company)


@routes.post("/")
async def create_company(request: Request):
    pass


@routes.put("/<company_id:int>")
async def update_company(request: Request, company_id: int):
    pass


@routes.delete("/<company_id:int>")
async def remove_company(request: Request, company_id: int):
    pass
