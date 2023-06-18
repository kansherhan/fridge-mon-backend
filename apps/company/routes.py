from sanic import Blueprint, Request, json
from sanic.exceptions import NotFound

from .models import Company

routes = Blueprint("companies", "/companies")


@routes.get("/")
async def get_companies(request: Request):
    companies: list[Company] = Company.find_all()

    companies_dicts = [c.to_dict() for c in companies]

    return json(companies_dicts)


@routes.get("/<company_id:int>")
async def get_company(request: Request, company_id: int):
    company: Company = Company.find_by_id(company_id)

    if company != None:
        return company.to_json_response()
    else:
        raise NotFound(f"Could not find company with id = {company_id}")


@routes.post("/<company_id:int>")
async def create_company(request: Request, company_id: int):
    pass


@routes.put("/<company_id:int>")
async def update_company(request: Request, company_id: int):
    pass


@routes.delete("/<company_id:int>")
async def remove_company(request: Request, company_id: int):
    pass
