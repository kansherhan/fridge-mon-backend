from sanic import (
    Blueprint,
    Request,
    empty as empty_response,
    json,
)
from sanic.response import JSONResponse, HTTPResponse
from sanic_ext import validate, openapi

from exceptions.fridge.not_found import FridgeNotFoundError
from exceptions.data_forbidden import DataForbidden

from .request_params import (
    CreateFridgeParams,
    UpdateFridgeParams,
)

from core.hash import Hash

from database.models.status import DataStatus
from .models import Fridge
from .measurements.models import FridgeMeasurement
from .templates.models import FridgeTemplate
from ..enterprises.models import Enterprise

from .categories.routes import routes as categories_routes
from .manufacturers.routes import routes as manufacturers_routes
from .measurements.routes import routes as measurements_routes
from .templates.routes import routes as templates_routes

from helper import models_to_dicts, model_is_active


fridges_routes = Blueprint("fridges", "/")


@fridges_routes.get("/enterprise/<enterprises_id:int>/")
@openapi.summary("Об всех холодильников в корпорации")
async def get_fridges_on_enterprises(
    request: Request,
    enterprises_id: int,
) -> JSONResponse:
    enterprise: Enterprise = Enterprise.find_by_id(enterprises_id)

    fridges: list[Fridge] = []

    for fridge in enterprise.fridges:
        if model_is_active(fridge):
            fridges.append(fridge.to_dict())

    return json(fridges)


@fridges_routes.get("/<fridge_id:int>")
@openapi.summary("Информация об холодильнике")
async def get_fridge(request: Request, fridge_id: int) -> JSONResponse:
    fridge: Fridge = Fridge.find_by_id(fridge_id)

    if fridge == None:
        raise FridgeNotFoundError()
    elif not model_is_active(fridge):
        raise DataForbidden()

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
async def create_fridge(request: Request, body: CreateFridgeParams) -> JSONResponse:
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
        temperature_lower=body.temperature_lower,
        temperature_upper=body.temperature_upper,
    )

    return fridge.to_json_response()


@fridges_routes.patch("/<fridge_id:int>")
@openapi.summary("Обновить данные холодильника")
@validate(json=UpdateFridgeParams)
async def update_fridge(
    request: Request,
    fridge_id: int,
    body: UpdateFridgeParams,
) -> HTTPResponse:
    fridge: Fridge = Fridge.find_by_id(fridge_id)

    if fridge == None:
        raise FridgeNotFoundError()
    elif not model_is_active(fridge):
        raise DataForbidden()

    fridge.name = body.name
    fridge.temperature_lower = body.temperature_lower
    fridge.temperature_upper = body.temperature_upper
    fridge.status = body.status

    fridge.save()

    return fridge.to_json_response()


@fridges_routes.delete("/<fridge_id:int>")
@openapi.summary("Удалить холодильник из корпорации")
async def remove_fridge(request: Request, fridge_id: int) -> HTTPResponse:
    fridge: Fridge = Fridge.find_by_id(fridge_id)

    if fridge == None:
        raise FridgeNotFoundError()

    fridge.status = DataStatus.DELETE
    fridge.save()

    return empty_response()


routes = Blueprint.group(
    fridges_routes,
    categories_routes,
    manufacturers_routes,
    measurements_routes,
    templates_routes,
    url_prefix="/fridges",
)
