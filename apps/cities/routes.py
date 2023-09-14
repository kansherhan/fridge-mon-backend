from sanic import Blueprint
from sanic_ext import openapi, validate

from exceptions.city.has_city import HasCityError
from exceptions.city.not_found import CityNotFoundError

from core.app.request import AppRequest

from database.models.status import DataStatus
from .models import City

from .request_params import CreateCityParams, UpdateCityParams

from helper import model, models_to_json


routes = Blueprint("cities", "/cities")


@routes.get("/")
@openapi.summary("Список городов")
@openapi.description("Отправляеть список городов")
async def get_all_cities(request: AppRequest):
    cities = City.select().where(City.status == DataStatus.ACTIVE)

    return models_to_json(cities)


@routes.get("/<city_id:int>")
@openapi.summary("Данные о городе")
@openapi.description("Можно получить данные о родном городе указанием его айдишника")
async def get_city(request: AppRequest, city_id: int):
    city: City = model(
        model=City.find_by_id(city_id),
        not_found_exception=CityNotFoundError,
    )

    return city.to_json_response()


@routes.post("/")
@validate(json=CreateCityParams)
async def create_city(request: AppRequest, body: CreateCityParams):
    city: City = City.get_or_none(City.name == body.name)

    if city != None:
        raise HasCityError()

    city: City = City.create(
        name=body.name,
        latitude=body.latitude,
        longitude=body.longitude,
        country=body.country,
    )

    return city.to_json_response()


@routes.patch("/<city_id:int>")
@validate(json=UpdateCityParams)
async def update_city(request: AppRequest, city_id: int, body: UpdateCityParams):
    city: City = model(
        model=City.get_or_none(City.id == city_id),
        not_found_exception=CityNotFoundError,
    )

    city.name = body.name
    city.latitude = body.latitude
    city.longitude = body.longitude
    city.country = body.country

    city.save()

    return city.to_json_response()


@routes.delete("/<city_id:int>")
async def delete_city(request: AppRequest, city_id: int):
    city: City = model(
        model=City.get_or_none(City.id == city_id),
        not_found_exception=CityNotFoundError,
    )

    city.status = DataStatus.DELETE
    city.save()

    return request.empty()
