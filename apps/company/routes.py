from sanic import Blueprint, Request, json
from sanic.exceptions import NotFound

from .models import Company
from ..enterprises.models import Enterprise

from helper import models_to_json, model_not_none

routes = Blueprint("companies", "/companies")


@routes.get("/")
async def get_companies(request: Request):
    companies: list[Company] = Company.find_all()

    return models_to_json(companies)


@routes.get("/<company_id:int>")
async def get_company(request: Request, company_id: int):
    query: list[Company] = (
        Company.select(Company, Enterprise)
        .join(Enterprise)
        .where(Company.id == company_id)
    )

    enterprises = []

    for company in query:
        enterprises.append(company.enterprise.to_dict())

    company = model_not_none(company).to_dict()
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
