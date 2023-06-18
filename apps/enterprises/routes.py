from sanic import Blueprint, Request

from .models import Enterprise

from helper import models_to_json

__ENTERPRISE_COMPANY_PATH__ = "/<company_id:int>"
__ENTERPRISE_ID_PATH__ = "/<enterprise_id:int>"

routes = Blueprint("enterprises", "/enterprises")


@routes.get(f"{__ENTERPRISE_COMPANY_PATH__}/all")
async def get_enterprises(request: Request, company_id: int):
    enterprises: list[Enterprise] = (
        Enterprise.select()
        .where(Enterprise.company == company_id)
        .order_by(Enterprise.id)
    )

    return models_to_json(enterprises)


@routes.get(__ENTERPRISE_ID_PATH__)
async def get_enterprise(request: Request, company_id: int, enterprise_id: int):
    pass


@routes.post(__ENTERPRISE_COMPANY_PATH__)
async def create_enterprise(request: Request, company_id: int):
    pass


@routes.put(__ENTERPRISE_ID_PATH__)
async def update_enterprise(request: Request, company_id: int, enterprise_id: int):
    pass


@routes.delete(__ENTERPRISE_ID_PATH__)
async def remove_enterprise(request: Request, company_id: int, enterprise_id: int):
    pass
