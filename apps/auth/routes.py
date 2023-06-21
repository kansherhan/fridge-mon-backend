import bcrypt
from datetime import datetime

from sanic import Blueprint, Request
from sanic.exceptions import Forbidden
from sanic_ext import validate

from utils.token import generate_token

from .models import EmployeeToken as Token
from .query_params import LoginParams, RegistrationParams
from ..employees.models import Employee

routes = Blueprint("auth", "/auth")


@routes.post("/login", ctx_unauthorized_request=True)
@validate(json=LoginParams)
async def login(request: Request, body: LoginParams):
    employee: Employee = Employee.get_or_none(Employee.email == body.email)

    if employee != None:
        if bcrypt.checkpw(body.password.encode(), employee.password.encode()):
            token: Token = employee.tokens[0]

            total_seconds = (datetime.now() - token.updated_at).total_seconds()

            if total_seconds < request.app.config.TOKEN_LIFETIME:
                return token.to_json_response()
            else:
                # TODO: Сделать обработку нового токена
                pass
        else:
            raise Forbidden()


@routes.post("/logout")
async def logout(request: Request):
    user: Employee = request.ctx.user

    for token in user.tokens:
        token.delete_instance()


@routes.post("/registration", ctx_unauthorized_request=True)
@validate(json=RegistrationParams)
async def registration(request: Request, params: RegistrationParams):
    pass
