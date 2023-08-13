from sanic import (
    Blueprint,
    Request,
    empty as empty_response,
)
from sanic.response import json
from sanic_ext import validate

from .request_params import (
    CreateEnterpriseParams,
    UpdateEnterpriseParams,
)

from ..companies.models import Company
from ..cities.models import City
from .models import Enterprise

from exceptions.enterprise.not_found import NotFoundEnterprise

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

    enterprises = []

    for enterprise in city.enterprises:
        enterprise_dict = enterprise.to_dict()
        enterprise_dict["fridges"] = models_to_dicts(enterprise.fridges)
        enterprises.append(enterprise_dict)

    city_dict["enterprises"] = enterprises

    return json(city_dict)


@routes.get("/info/<enterprise_id:int>")
async def get_enterprise(request: Request, enterprise_id: int):
    """Информация о корпорации"""

    enterprise: Enterprise = Enterprise.get_or_none(Enterprise.id == enterprise_id)

    enterprise_dict = model_not_none(enterprise).to_dict()
    enterprise_dict["fridges"] = models_to_dicts(enterprise.fridges)

    return json(enterprise_dict)


@routes.post("/<company_id:int>")
@validate(json=CreateEnterpriseParams)
async def create_enterprise(
    request: Request, company_id: int, body: CreateEnterpriseParams
):
    enterprise: Enterprise = Enterprise.create(
        name=body.name,
        city=body.city,
        company=company_id,
        latitude=body.latitude,
        longitude=body.longitude,
    )

    return enterprise.to_json_response()


@routes.patch("/<enterprise_id:int>")
@validate(json=UpdateEnterpriseParams)
async def update_enterprise(
    request: Request, enterprise_id: int, body: UpdateEnterpriseParams
):
    query = Enterprise.update(
        {
            Enterprise.name: body.name,
            Enterprise.address: body.address,
            Enterprise.latitude: body.latitude,
            Enterprise.longitude: body.longitude,
            Enterprise.phone: body.phone,
            Enterprise.email: body.email,
        }
    ).where(Enterprise.id == enterprise_id)

    query.execute()

    return empty_response()


@routes.delete("/<enterprise_id:int>")
async def delete_enterprise(request: Request, enterprise_id: int):
    enterprise: Enterprise = Enterprise.find_by_id(enterprise_id)

    if enterprise == None:
        raise NotFoundEnterprise()

    enterprise.delete_instance()

    return empty_response()
