from sanic import Blueprint
from sanic.response import json
from sanic_ext import validate, openapi

from core.app.request import AppRequest

from database.models.status import DataStatus
from ..companies.models import Company
from ..cities.models import City
from ..fridges.models import Fridge
from ..fridges.measurements.models import FridgeMeasurement
from .models import Enterprise

from exceptions.city.not_found import NotFoundCityError
from exceptions.company.not_found import CompanyNotFoundError
from exceptions.enterprise.not_found import EnterpriseNotFoundError
from exceptions.data_forbidden import DataForbidden

from .request_params import (
    CreateEnterpriseParams,
    UpdateEnterpriseParams,
)

from helper import (
    models_to_dicts,
    models_to_json,
    model_is_active,
)


routes = Blueprint("enterprises", "/enterprises")


@routes.get("/<company_id:int>")
@openapi.summary("Информация о корпорациях в комании")
async def get_enterprises(request: AppRequest, company_id: int):
    company: Company = Company.get_or_none(Company.id == company_id)

    if company == None:
        raise CompanyNotFoundError()
    elif not model_is_active(company):
        raise DataForbidden()

    company_enterprises = Enterprise.select().where(
        Enterprise.company == company.id,
        Enterprise.status == DataStatus.ACTIVE,
    )

    return models_to_json(company_enterprises)


@routes.get("/map/<company_id:int>/<city_id:int>")
@openapi.summary("Данные корпорация по одному городу")
@openapi.description(
    "Отправляет данные корпорация в городе и список холодильников и их последние обновленные данные"
)
async def get_enterprises_locations(request: AppRequest, company_id: int, city_id: int):
    city: City = City.find_by_id(city_id)

    if city == None:
        raise NotFoundCityError()

    city_dict = city.to_dict()

    enterprises = Enterprise.select().where(
        Enterprise.city == city_id,
        Enterprise.status == DataStatus.ACTIVE,
    )

    enterprises_dict: list[Enterprise] = []

    for enterprise in enterprises:
        enterprise_dict = enterprise.to_dict()

        fridges = Fridge.select().where(
            Fridge.enterprise == enterprise.id,
            Fridge.status == DataStatus.ACTIVE,
        )
        enterprise_fridges = []

        for fridge in fridges:
            fridge_dict = fridge.to_dict()

            fridge_dict["measurements"] = models_to_dicts(
                (
                    FridgeMeasurement.select()
                    .where(FridgeMeasurement.fridge == fridge)
                    .order_by(FridgeMeasurement.created_at.desc())
                    .limit(1)
                )
            )
            enterprise_fridges.append(fridge_dict)

        enterprise_dict["fridges"] = enterprise_fridges
        enterprises_dict.append(enterprise_dict)

    city_dict["enterprises"] = enterprises_dict

    return json(city_dict)


@routes.get("/info/<enterprise_id:int>")
@openapi.summary("Информация о корпорации")
async def get_enterprise(request: AppRequest, enterprise_id: int):
    enterprise: Enterprise = Enterprise.get_or_none(Enterprise.id == enterprise_id)

    if enterprise == None:
        raise EnterpriseNotFoundError()
    elif not model_is_active(enterprise):
        raise DataForbidden()

    enterprise_dict = enterprise.to_dict()

    enterprise_fridges = Fridge.select().where(
        Fridge.enterprise == enterprise.id,
        Fridge.status == DataStatus.ACTIVE,
    )

    enterprise_dict["fridges"] = models_to_dicts(enterprise_fridges)

    return json(enterprise_dict)


@routes.post("/<company_id:int>")
@openapi.summary("Создать корпорацию в компании")
@validate(json=CreateEnterpriseParams)
async def create_enterprise(
    request: AppRequest, company_id: int, body: CreateEnterpriseParams
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
    request: AppRequest,
    enterprise_id: int,
    body: UpdateEnterpriseParams,
):
    enterprise: Enterprise = Enterprise.find_by_id(enterprise_id)

    if enterprise == None:
        raise EnterpriseNotFoundError()
    elif not model_is_active(enterprise):
        raise DataForbidden()

    enterprise.name = body.name
    enterprise.address = body.address
    enterprise.latitude = body.latitude
    enterprise.longitude = body.longitude
    enterprise.phone = body.phone
    enterprise.email = body.email

    enterprise.save()

    return enterprise.to_json_response()


@routes.delete("/<enterprise_id:int>")
@openapi.summary("Удалить корпорация из компании")
async def delete_enterprise(request: AppRequest, enterprise_id: int):
    enterprise: Enterprise = Enterprise.find_by_id(enterprise_id)

    if enterprise == None:
        raise EnterpriseNotFoundError()
    elif not model_is_active(enterprise):
        raise DataForbidden()

    enterprise.status = DataStatus.DELETE
    enterprise.save()

    return request.empty()
