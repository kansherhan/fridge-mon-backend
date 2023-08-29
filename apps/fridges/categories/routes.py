from sanic import Blueprint, Request
from sanic_ext import openapi

from .models import FridgeCategory as Category
from helper import models_to_json


routes = Blueprint("categories", "/categories")


@routes.get("/")
@openapi.summary("Получить все категории холодильников")
async def get_categories(request: Request):
    categories: list[Category] = Category.find_all()

    return models_to_json(categories)
