from sanic import Blueprint
from sanic_ext import openapi, validate

from core.app.request import AppRequest

from database.models.status import DataStatus
from .models import FridgeManufacturer as Manufacturer

from .request_params import (
    CreateFridgeManufacturerParams,
    UpdateFridgeManufacturerParams,
)

from exceptions.fridge.manufacturers.not_found import FridgeManufacturerNotFoundError

from helper import models_to_json


routes = Blueprint("manufacturers", "/manufacturers")


@routes.get("/")
@openapi.summary("Получить все виды брендов холодильников")
async def get_manufacturers(request: AppRequest):
    manufacturers: list[Manufacturer] = Manufacturer.select().where(
        Manufacturer.status == DataStatus.ACTIVE
    )

    return models_to_json(manufacturers)


@routes.post("/")
@validate(json=CreateFridgeManufacturerParams)
async def create_manufacturer(
    request: AppRequest,
    body: CreateFridgeManufacturerParams,
):
    manufacturer: Manufacturer = Manufacturer.create(name=body.name)

    return manufacturer.to_json_response()


@routes.patch("/<manufacturer_id:int>")
@validate(json=UpdateFridgeManufacturerParams)
async def update_manufacturer(
    request: AppRequest,
    manufacturer_id: int,
    body: UpdateFridgeManufacturerParams,
):
    manufacturer: Manufacturer = Manufacturer.find_by_id(manufacturer_id)

    if manufacturer == None:
        raise FridgeManufacturerNotFoundError()

    manufacturer.name = body.name
    manufacturer.save()

    return manufacturer.to_json_response()


@routes.delete("/<manufacturer_id:int>")
async def delete_manufacturer(request: AppRequest, manufacturer_id: int):
    manufacturer: Manufacturer = Manufacturer.find_by_id(manufacturer_id)

    if manufacturer == None:
        raise FridgeManufacturerNotFoundError()

    manufacturer.status = DataStatus.DELETE
    manufacturer.save()

    return request.empty()
