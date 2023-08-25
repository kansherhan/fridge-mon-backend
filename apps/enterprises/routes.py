from sanic import (
    Blueprint,
    Request,
    empty as empty_response,
)
from sanic.response import json
from sanic_ext import validate, openapi

from peewee import Query

from .request_params import (
    CreateEnterpriseParams,
    UpdateEnterpriseParams,
)

from ..companies.models import Company
from ..cities.models import City
from ..fridges.models import Fridge
from ..fridges.measurements.models import FridgeMeasurement
from .models import Enterprise

from exceptions.enterprise.not_found import EnterpriseNotFoundError

from helper import models_to_json, models_to_dicts, model_not_none


routes = Blueprint("enterprises", "/enterprises")


@routes.get("/<company_id:int>")
@openapi.summary("Информация о корпорациях в комании")
async def get_enterprises(request: Request, company_id: int):
    company: Company = Company.get_or_none(Company.id == company_id)

    return models_to_json(company.enterprises)


@routes.get("/map/<company_id:int>/<city_id:int>")
@openapi.summary("Данные корпорация по одному городу")
@openapi.description(
    "Отправляет данные корпорация в городе и список холодильников и их последние обновленные данные"
)
async def get_enterprises_locations(request: Request, company_id: int, city_id: int):
    city: City = model_not_none(City.find_by_id(city_id))
    city_dict = city.to_dict()

    enterprises = []

    for enterprise in city.enterprises:
        enterprise_dict = enterprise.to_dict()

        fridges = []

        for fridge in enterprise.fridges:
            fridge_dict = fridge.to_dict()

            fridge_dict["measurements"] = models_to_dicts(
                (
                    FridgeMeasurement.select()
                    .where(FridgeMeasurement.fridge == fridge)
                    .order_by(FridgeMeasurement.created_at.desc())
                    .limit(1)
                )
            )
            fridges.append(fridge_dict)

        enterprise_dict["fridges"] = fridges
        enterprises.append(enterprise_dict)

    city_dict["enterprises"] = enterprises

    return json(city_dict)


@routes.get("/info/<enterprise_id:int>")
@openapi.summary("Информация о корпорации")
async def get_enterprise(request: Request, enterprise_id: int):
    enterprise: Enterprise = Enterprise.get_or_none(Enterprise.id == enterprise_id)

    enterprise_dict = model_not_none(enterprise).to_dict()
    enterprise_dict["fridges"] = models_to_dicts(enterprise.fridges)

    return json(enterprise_dict)


@routes.post("/<company_id:int>")
@openapi.summary("Создать корпорацию в компании")
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
@openapi.summary("Обновить данные корпорации")
@validate(json=UpdateEnterpriseParams)
async def update_enterprise(
    request: Request, enterprise_id: int, body: UpdateEnterpriseParams
):
    query: Query = Enterprise.update(
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
@openapi.summary("Удалить корпорация из компании")
async def delete_enterprise(request: Request, enterprise_id: int):
    # TODO: Усправить удаления корпарации без ссылок на обьекты
    enterprise: Enterprise = Enterprise.find_by_id(enterprise_id)

    if enterprise == None:
        raise EnterpriseNotFoundError()

    enterprise.delete_instance()

    return empty_response()
