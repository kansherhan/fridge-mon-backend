from sanic import Blueprint, Request, json

from .models import Category

routes = Blueprint("categories", "/categories")


@routes.get("/")
async def get_categories(request: Request):
    categories = Category.select().order_by(Category.id)

    categories_dicts = [c.to_dict() for c in categories]

    return json(categories_dicts)


@routes.get("/<category_id:int>")
async def get_category(request: Request, category_id: int):
    category: Category = Category.get_or_none(Category.id == category_id)

    if category != None:
        return category.to_json_response()
