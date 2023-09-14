from sanic import Blueprint, json
from sanic.response import JSONResponse, HTTPResponse
from sanic_ext import validate, openapi

from exceptions.fridge.not_found import FridgeNotFoundError

from .request_params import (
    CreateFridgeParams,
    UpdateFridgeParams,
)

from core.hash import Hash
from core.app.request import AppRequest

from database.models.status import DataStatus
from .models import Fridge
from .measurements.models import FridgeMeasurement
from .templates.models import FridgeTemplate

from .categories.routes import routes as categories_routes
from .manufacturers.routes import routes as manufacturers_routes
from .measurements.routes import routes as measurements_routes
from .templates.routes import routes as templates_routes

from helper import (
    model,
    models_to_dicts,
    models_to_json,
)


fridges_routes = Blueprint("fridges", "/")


@fridges_routes.get("/enterprise/<enterprises_id:int>/")
@openapi.summary("Об всех холодильников в корпорации")
async def get_fridges_on_enterprises(
    request: AppRequest,
    enterprises_id: int,
) -> JSONResponse:
    fridges: list[Fridge] = Fridge.select().where(
        Fridge.enterprise == enterprises_id,
        Fridge.status == DataStatus.ACTIVE,
    )

    return models_to_json(fridges)


@fridges_routes.get("/<fridge_id:int>")
@openapi.summary("Информация об холодильнике")
async def get_fridge(request: AppRequest, fridge_id: int) -> JSONResponse:
    fridge: Fridge = model(
        model=Fridge.find_by_id(fridge_id),
        not_found_exception=FridgeNotFoundError,
    )

    fridge_dict = fridge.to_dict()
    fridge_dict["measurements"] = models_to_dicts(
        (
            FridgeMeasurement.select()
            .where(FridgeMeasurement.fridge == fridge_id)
            .order_by(FridgeMeasurement.created_at.desc())
            .limit(10)
        )
    )

    return json(fridge_dict)


@fridges_routes.post("/")
@openapi.summary("Создать холодильник в корпарации")
@validate(json=CreateFridgeParams)
async def create_fridge(request: AppRequest, body: CreateFridgeParams) -> JSONResponse:
    if body.template_id != -1:
        template: FridgeTemplate = FridgeTemplate.find_by_id(body.template_id)

        if template != None and template.company == body.template_id:
            body.temperature_lower = template.temperature_lower
            body.temperature_upper = template.temperature_upper

    fridge: Fridge = Fridge.create(
        name=body.name,
        company=body.company,
        serial_number=Hash.generate_hash(32),
        enterprise=body.enterprise,
        category=body.category_id,
        manufacturer=body.manufacturer_id,
        temperature_lower=body.temperature_lower,
        temperature_upper=body.temperature_upper,
    )

    return fridge.to_json_response()


@fridges_routes.patch("/<fridge_id:int>")
@openapi.summary("Обновить данные холодильника")
@validate(json=UpdateFridgeParams)
async def update_fridge(
    request: AppRequest,
    fridge_id: int,
    body: UpdateFridgeParams,
) -> JSONResponse:
    fridge: Fridge = model(
        model=Fridge.find_by_id(fridge_id),
        not_found_exception=FridgeNotFoundError,
    )

    fridge.name = body.name
    fridge.temperature_lower = body.temperature_lower
    fridge.temperature_upper = body.temperature_upper
    fridge.fridge_status = body.status

    fridge.save()

    return fridge.to_json_response()


@fridges_routes.delete("/<fridge_id:int>")
@openapi.summary("Удалить холодильник из корпорации")
async def remove_fridge(request: AppRequest, fridge_id: int) -> HTTPResponse:
    fridge: Fridge = model(
        model=Fridge.find_by_id(fridge_id),
        not_found_exception=FridgeNotFoundError,
    )

    fridge.status = DataStatus.DELETE
    fridge.save()

    return request.empty()


routes = Blueprint.group(
    fridges_routes,
    categories_routes,
    manufacturers_routes,
    measurements_routes,
    templates_routes,
    url_prefix="/fridges",
)
