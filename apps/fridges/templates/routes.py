from sanic import Blueprint, Request, empty as empty_response
from sanic.response import JSONResponse, HTTPResponse
from sanic_ext import validate, openapi

from .request_params import (
    CreateFridgeTemplateParams,
    UpdateFridgeTemplateParams,
)

from .models import FridgeTemplate

from helper import models_to_json


routes = Blueprint("templates", "/templates")


@routes.get("/<company_id:int>/all")
@openapi.summary("Получить список шаблонов холодильника")
async def get_templates(request: Request, company_id: int) -> JSONResponse:
    templates: list[FridgeTemplate] = FridgeTemplate.select().where(
        FridgeTemplate.company == company_id
    )

    return models_to_json(templates)


@routes.post("/")
@openapi.summary("Создать шаблон для создания холодильника")
@validate(json=CreateFridgeTemplateParams)
async def create_fridge_template(
    request: Request, body: CreateFridgeTemplateParams
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
    request: Request,
    template_id: int,
    body: UpdateFridgeTemplateParams,
) -> HTTPResponse:
    query = FridgeTemplate.update(
        {
            FridgeTemplate.name: body.name,
            FridgeTemplate.temperature_lower: body.temperature_lower,
            FridgeTemplate.temperature_upper: body.temperature_upper,
        }
    ).where(FridgeTemplate.id == template_id)

    query.execute()

    return empty_response()


@routes.delete("/<template_id:int>")
@openapi.summary("Удалить шаблон")
async def delete_fridge_template(request: Request, template_id: int) -> HTTPResponse:
    template: FridgeTemplate = FridgeTemplate.find_by_id(template_id)

    if template == None:
        return

    template.delete_instance()

    return empty_response()
