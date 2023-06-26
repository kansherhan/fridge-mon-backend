from sanic import Blueprint, Request

from ..company.models import Company
from .models import Enterprise

from helper import models_to_json, model_not_none

__ENTERPRISE_COMPANY_PATH__ = "/<company_id:int>"
__ENTERPRISE_ID_PATH__ = "/<enterprise_id:int>"

routes = Blueprint("enterprises", "/enterprises")


@routes.get(f"{__ENTERPRISE_COMPANY_PATH__}/all")
async def get_enterprises(request: Request, company_id: int):
    company: Company = Company.get_or_none(Company.id == company_id)

    return models_to_json(company.enterprises)


@routes.get(__ENTERPRISE_ID_PATH__)
async def get_enterprise(request: Request, enterprise_id: int):
    enterprise: Enterprise = Enterprise.get_or_none(Enterprise.id == enterprise_id)

    return model_not_none(enterprise).to_json_response()


@routes.post(__ENTERPRISE_COMPANY_PATH__)
async def create_enterprise(request: Request, company_id: int):
    pass


@routes.put(__ENTERPRISE_ID_PATH__)
async def update_enterprise(request: Request, company_id: int, enterprise_id: int):
    pass


@routes.delete(__ENTERPRISE_ID_PATH__)
async def remove_enterprise(request: Request, company_id: int, enterprise_id: int):
    pass
