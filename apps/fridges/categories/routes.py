from sanic import Blueprint, Request, json
from sanic.exceptions import NotFound

from .models import FridgeCategory as Category

routes = Blueprint("categories", "/categories")


@routes.get("/")
async def get_categories(request: Request):
    categories: list[Category] = Category.get_all()

    categories_dicts = [c.to_dict() for c in categories]

    return json(categories_dicts)


@routes.get("/<category_id:int>")
async def get_category(request: Request, category_id: int):
    category: Category = Category.find_by_id(category_id)

    if category != None:
        return category.to_json_response()
    else:
        raise NotFound(f"Could not find category with id = {category_id}")
