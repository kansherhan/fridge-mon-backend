from sanic import Blueprint, Request

from ..company.models import Company
from .models import Enterprise

from helper import models_to_json, model_not_none


routes = Blueprint("enterprises", "/enterprises")


@routes.get("/<company_id:int>")
async def get_enterprises(request: Request, company_id: int):
    """Информация о корпорациях в комании"""

    company: Company = Company.get_or_none(Company.id == company_id)

    return models_to_json(company.enterprises)


@routes.get("/map/<company_id:int>/<city_id:int>")
async def get_enterprises(request: Request, company_id: int, city_id: int):
    """Информация о корпорациях в комании"""

    company: Company = Enterprise.select().where()

    return models_to_json(company.enterprises)


@routes.get("/info/<enterprise_id:int>")
async def get_enterprise(request: Request, enterprise_id: int):
    """Информация о корпорации"""

    enterprise: Enterprise = Enterprise.get_or_none(Enterprise.id == enterprise_id)

    return model_not_none(enterprise).to_json_response()
