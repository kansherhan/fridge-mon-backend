from sanic import Request, Blueprint
from sanic_ext import openapi

from .models import Country

from helper import models_to_json, model_not_none


routes = Blueprint("countries", "/countries")


@routes.get("/")
@openapi.summary("Отправляет список стран")
async def get_all_countries(request: Request):
    countries = Country.find_all()

    return models_to_json(countries)


@routes.get("/<country_id:int>")
@openapi.summary("Данные об одной стране")
async def get_country(request: Request, country_id: int):
    country = Country.find_by_id(country_id)

    return model_not_none(country).to_json_response()


@routes.get("/<country_id:int>/cities")
@openapi.summary("Отправляет список городов в стране")
async def get_country_of_cities(request: Request, country_id: int):
    country = Country.find_by_id(country_id)

    return models_to_json(country.cities)
