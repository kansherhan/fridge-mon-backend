from sanic import Blueprint, Request
from sanic_ext import openapi

from .models import FridgeManufacturer as Manufacturer
from helper import models_to_json


routes = Blueprint("manufacturers", "/manufacturers")


@routes.get("/")
@openapi.summary("Получить все виды брендов холодильников")
async def get_manufacturers(request: Request):
    manufacturers: list[Manufacturer] = Manufacturer.find_all()

    return models_to_json(manufacturers)
