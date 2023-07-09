from sanic import Blueprint, Request

from ..companies.models import Company
from ..cities.models import City
from .models import Enterprise

from helper import models_to_json, models_to_dicts, model_not_none


routes = Blueprint("enterprises", "/enterprises")


@routes.get("/<company_id:int>")
async def get_enterprises(request: Request, company_id: int):
    """Информация о корпорациях в комании"""

    company: Company = Company.get_or_none(Company.id == company_id)

    return models_to_json(company.enterprises)


@routes.get("/map/<company_id:int>/<city_id:int>")
async def get_enterprises_locations(request: Request, company_id: int, city_id: int):
    """Информация о корпорациях в комании"""

    city: City = model_not_none(City.find_by_id(city_id))
    city_dict = city.to_dict()
    city_dict["enterprises"] = models_to_dicts(city.enterprises)


@routes.get("/info/<enterprise_id:int>")
async def get_enterprise(request: Request, enterprise_id: int):
    """Информация о корпорации"""

    enterprise: Enterprise = Enterprise.get_or_none(Enterprise.id == enterprise_id)

    return model_not_none(enterprise).to_json_response()
