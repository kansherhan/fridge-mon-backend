from sanic import Request, Blueprint
from sanic_ext import openapi

from .models import City
from helper import models_to_json, model_not_none

routes = Blueprint("cities", "/cities")


@routes.get("/")
@openapi.summary("Список городов")
@openapi.description("Отправляеть список городов")
async def get_all_cities(request: Request):
    cities = City.find_all()

    return models_to_json(cities)


@routes.get("/<city_id:int>")
@openapi.summary("Данные о городе")
@openapi.description("Можно получить данные о родном городе указанием его айдишника")
async def get_city(request: Request, city_id: int):
    city = City.find_by_id(city_id)

    return model_not_none(city).to_json_response()
