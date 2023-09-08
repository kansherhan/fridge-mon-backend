from sanic import Blueprint
from sanic.response import json
from sanic_ext import validate, openapi

from core.app.request import AppRequest

from database.models.status import DataStatus
from ..companies.models import Company
from ..cities.models import City
from ..fridges.measurements.models import FridgeMeasurement
from .models import Enterprise

from exceptions.company.not_found import CompanyNotFoundError
from exceptions.enterprise.not_found import EnterpriseNotFoundError
from exceptions.data_forbidden import DataForbidden

from .request_params import (
    CreateEnterpriseParams,
    UpdateEnterpriseParams,
)

from helper import (
    models_to_dicts,
    model_not_none,
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

    enterprises: list[Enterprise] = []

    for enterprise in company.enterprises:
        if not model_is_active(enterprise):
            continue

        enterprises.append(enterprise.to_dict())

    return json(enterprises)


@routes.get("/map/<company_id:int>/<city_id:int>")
@openapi.summary("Данные корпорация по одному городу")
@openapi.description(
    "Отправляет данные корпорация в городе и список холодильников и их последние обновленные данные"
)
async def get_enterprises_locations(request: AppRequest, company_id: int, city_id: int):
    city: City = model_not_none(City.find_by_id(city_id))
    city_dict = city.to_dict()

    enterprises = Enterprise.select().where(
        Enterprise.city == city_id,
        Enterprise.status == DataStatus.ACTIVE,
    )

    enterprises_dict: list[Enterprise] = []

    for enterprise in enterprises:
        enterprise_dict = enterprise.to_dict()

        fridges = []

        for fridge in enterprise.fridges:
            if not model_is_active(fridge):
                continue

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
        enterprises_dict.append(enterprise_dict)

    city_dict["enterprises"] = enterprises_dict

    return json(city_dict)


@routes.get("/info/<enterprise_id:int>")
@openapi.summary("Информация о корпорации")
async def get_enterprise(request: AppRequest, enterprise_id: int):
    enterprise: Enterprise = Enterprise.get_or_none(Enterprise.id == enterprise_id)

    if not model_is_active(enterprise):
        raise DataForbidden()

    enterprise_dict = model_not_none(enterprise).to_dict()
    enterprise_dict["fridges"] = models_to_dicts(enterprise.fridges)

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

    enterprise.status = DataStatus.DELETE
    enterprise.save()

    return request.empty()
