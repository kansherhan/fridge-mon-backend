from sanic import Blueprint
from sanic.response import JSONResponse, HTTPResponse
from sanic_ext import validate, openapi

from core.app.request import AppRequest

from .request_params import (
    CreateFridgeTemplateParams,
    UpdateFridgeTemplateParams,
)

from .models import FridgeTemplate

from helper import models_to_json


routes = Blueprint("templates", "/templates")


@routes.get("/<company_id:int>/all")
@openapi.summary("Получить список шаблонов холодильника")
async def get_templates(request: AppRequest, company_id: int) -> JSONResponse:
    templates: list[FridgeTemplate] = FridgeTemplate.select().where(
        FridgeTemplate.company == company_id
    )

    return models_to_json(templates)


@routes.post("/")
@openapi.summary("Создать шаблон для создания холодильника")
@validate(json=CreateFridgeTemplateParams)
async def create_fridge_template(
    request: AppRequest,
    body: CreateFridgeTemplateParams,
) -> JSONResponse:
    template: FridgeTemplate = FridgeTemplate.create(
        name=body.name,
        company=body.company_id,
        temperature_lower=body.temperature_lower,
        temperature_upper=body.temperature_upper,
    )

    return template.to_json_response()


@routes.patch("/<template_id:int>")
@openapi.summary("Обновить шаблон компании")
@validate(json=UpdateFridgeTemplateParams)
async def update_fridge_template(
    request: AppRequest,
    template_id: int,
    body: UpdateFridgeTemplateParams,
) -> HTTPResponse:
    template: FridgeTemplate = FridgeTemplate.find_by_id(template_id)

    template.name = body.name
    template.temperature_lower = body.temperature_lower
    template.temperature_upper = body.temperature_upper

    template.save()

    return template.to_json_response()


@routes.delete("/<template_id:int>")
@openapi.summary("Удалить шаблон")
async def delete_fridge_template(request: AppRequest, template_id: int) -> HTTPResponse:
    template: FridgeTemplate = FridgeTemplate.find_by_id(template_id)

    if template == None:
        return

    template.delete_instance()

    return request.empty()
