from sanic import Blueprint, Request

from .models import FridgeProduct as Product
from helper import models_to_json, model_not_none

routes = Blueprint("products", "/products")


@routes.get("/")
async def get_products(request: Request):
    """Получить все продукты"""

    products: list[Product] = Product.find_all()

    return models_to_json(products)


@routes.get("/<product_id:int>")
async def get_product(request: Request, product_id: int):
    """Получить один продукт"""

    product: Product = Product.find_by_id(product_id)

    return model_not_none(product).to_json_response()
