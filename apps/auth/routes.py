from sanic import Blueprint, Request
from sanic_ext import validate

from .models import EmployeeToken as Token
from .query_params import LoginParams, RegistrationParams
from ..employees.models import Employee

routes = Blueprint("auth", "/auth")


@routes.post("/login", ctx_unauthorized_request=True)
@validate(json=LoginParams)
async def login(request: Request, params: LoginParams):
    employee: Employee = Employee.get_or_none(Employee.email == params.email)

    if employee == None:
        return

    token: Token = Token.new(generate_key(), employee)
    token.save()


@routes.post("/logout")
async def logout(request: Request):
    pass


@routes.post("/registration", ctx_unauthorized_request=True)
@validate(json=RegistrationParams)
async def registration(request: Request, params: RegistrationParams):
    pass


def generate_key():
    from binascii import hexlify
    from os import urandom

    return hexlify(urandom(20)).decode()
