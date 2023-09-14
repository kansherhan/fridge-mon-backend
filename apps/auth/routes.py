import re as regex

from sanic import Blueprint
from sanic_ext import validate, openapi

from core.token import TokenManager
from core.app.request import AppRequest
from core.auth.password import Password

from .models import EmployeeToken as Token
from ..employees.models import Employee

from exceptions.auth.has_user import HasUserError
from exceptions.auth.login import LoginError
from exceptions.employee.username import EmployeeUsernameNotCorectError

from .params import LoginParams, RegistrationParams

from ..employees.routes import USERNAME_REGEX


routes = Blueprint("auth", "/auth")


@routes.post("/login")
@openapi.summary("Авторизации в системе")
@openapi.description("Дает возможность авторизоваться в системе для дальнейшей работы")
@validate(json=LoginParams)
async def login(request: AppRequest, body: LoginParams):
    employee: Employee = Employee.get_or_none(Employee.username == body.username)

    if employee == None:
        raise LoginError()

    if not Password.correct(body.password, employee.password):
        raise LoginError()

    token_hash = TokenManager.generate_token(request.config.TOKEN_LENGTH)

    token: Token = Token.create(
        employee=employee.id,
        token=token_hash,
    )

    return token.to_json_response()


@routes.post("/logout")
@openapi.summary("Выйти из системы")
@openapi.description("И удаления токена авторизации")
@openapi.response(204)
async def logout(request: AppRequest):
    user_token: Token = request.user_token
    user_token.delete_instance()

    return request.empty()


@routes.post("/registration")
@openapi.summary("Регистрация в системе")
@openapi.description("Дает возможность авторизоваться в системе для дальнейшей работы")
@validate(json=RegistrationParams)
async def registration(request: AppRequest, body: RegistrationParams):
    if regex.search(USERNAME_REGEX, body.username) == None:
        raise EmployeeUsernameNotCorectError()

    employee: Employee = Employee.get_or_none(
        Employee.username == body.username,
    )

    if employee != None:
        raise HasUserError()

    password_hash = Password.hash(body.password)

    employee = Employee.create(
        first_name=body.first_name,
        last_name=body.last_name,
        username=body.username,
        password=password_hash,
    )

    return employee.to_json_response()
