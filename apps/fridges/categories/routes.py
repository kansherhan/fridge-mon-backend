from sanic import Blueprint, Request

from .models import FridgeCategory as Category
from helper import models_to_json, model_not_none

routes = Blueprint("categories", "/categories")


@routes.get("/")
async def get_categories(request: Request):
    categories: list[Category] = Category.find_all()

    return models_to_json(categories)


@routes.get("/<category_id:int>")
async def get_category(request: Request, category_id: int):
    category: Category = Category.find_by_id(category_id)

    return model_not_none(category).to_json_response()
