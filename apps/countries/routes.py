from sanic import Blueprint
from sanic_ext import openapi, validate

from exceptions.country.has_country import HasCountryError
from exceptions.country.not_found import NotFoundCountyError

from core.app.request import AppRequest

from .models import Country

from .request_params import CreateCountryParams, UpdateCountryParams

from helper import models_to_json, model_not_none


routes = Blueprint("countries", "/countries")


@routes.get("/")
@openapi.summary("Отправляет список стран")
async def get_all_countries(request: AppRequest):
    countries = Country.find_all()

    return models_to_json(countries)


@routes.get("/<country_id:int>")
@openapi.summary("Данные об одной стране")
async def get_country(request: AppRequest, country_id: int):
    country = Country.find_by_id(country_id)

    return model_not_none(country).to_json_response()


@routes.get("/<country_id:int>/cities")
@openapi.summary("Отправляет список городов в стране")
async def get_country_of_cities(request: AppRequest, country_id: int):
    country = Country.find_by_id(country_id)

    return models_to_json(country.cities)


@routes.post("/")
@validate(json=CreateCountryParams)
async def create_country(request: AppRequest, body: CreateCountryParams):
    country: Country = Country.get_or_none(Country.name == body.name)

    if country != None:
        raise HasCountryError()

    country: Country = Country.create(name=body.name)

    return country.to_json_response()


@routes.patch("/<country_id:int>")
@validate(json=UpdateCountryParams)
async def update_country(
    request: AppRequest,
    country_id: int,
    body: UpdateCountryParams,
):
    country: Country = Country.get_or_none(Country.id == country_id)

    if country == None:
        raise NotFoundCountyError()

    country.name = body.name

    country.save()

    return country.to_json_response()


@routes.delete("/<country_id:int>")
async def delete_country(request: AppRequest, country_id: int):
    country: Country = Country.get_or_none(Country.id == country_id)

    if country == None:
        raise NotFoundCountyError()

    country.delete_instance()

    return request.empty()
