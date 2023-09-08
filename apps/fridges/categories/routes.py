from sanic import Blueprint
from sanic_ext import openapi, validate

from core.app.request import AppRequest

from database.models.status import DataStatus
from .models import FridgeCategory as Category

from .request_params import (
    CreateFridgeCategoryParams,
    UpdateFridgeCategoryParams,
)

from exceptions.fridge.category.not_found import FridgeCategoryNotFoundError

from helper import models_to_json


routes = Blueprint("categories", "/categories")


@routes.get("/")
@openapi.summary("Получить все категории холодильников")
async def get_categories(request: AppRequest):
    categories: list[Category] = Category.select().where(
        Category.status == DataStatus.ACTIVE
    )

    return models_to_json(categories)


@routes.post("/")
@validate(json=CreateFridgeCategoryParams)
async def create_category(request: AppRequest, body: CreateFridgeCategoryParams):
    category: Category = Category.create(name=body.name)

    return category.to_json_response()


@routes.patch("/<category_id:int>")
@validate(json=UpdateFridgeCategoryParams)
async def update_category(
    request: AppRequest,
    category_id: int,
    body: UpdateFridgeCategoryParams,
):
    category: Category = Category.find_by_id(category_id)

    if category == None:
        raise FridgeCategoryNotFoundError()

    category.name = body.name
    category.save()

    return category.to_json_response()


@routes.delete("/<category_id:int>")
async def delete_category(request: AppRequest, category_id: int):
    category: Category = Category.find_by_id(category_id)

    if category == None:
        raise FridgeCategoryNotFoundError()

    category.status = DataStatus.DELETE
    category.save()

    return request.empty()
