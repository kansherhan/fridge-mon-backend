import bcrypt

from sanic import Blueprint, Request
from sanic_ext import validate, openapi

from exceptions.auth.has_user import HasUserError
from exceptions.auth.login import LoginError

from core.token import TokenManager
from core.app.request import AppRequest

from .models import EmployeeToken as Token
from .request_params import LoginParams, RegistrationParams
from ..employees.models import Employee


routes = Blueprint("auth", "/auth")


@routes.post("/login")
@openapi.summary("Авторизации в системе")
@openapi.description("Дает возможность авторизоваться в системе для дальнейшей работы")
@validate(json=LoginParams)
async def login(request: AppRequest, body: LoginParams):
    def check_password(password: str, hash: str) -> bool:
        return bcrypt.checkpw(password.encode(), hash.encode())

    employee: Employee = Employee.get_or_none(Employee.email == body.email)

    if employee == None:
        raise LoginError()

    if not check_password(body.password, employee.password):
        raise LoginError()

    token: Token = Token.create(
        employee=employee.id,
        token=TokenManager.generate_token(request.config.TOKEN_LENGTH),
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
async def registration(request: Request, body: RegistrationParams):
    def create_password(password: str) -> str:
        return bcrypt.hashpw(
            password.encode(),
            bcrypt.gensalt(),
        )

    employee: Employee = Employee.get_or_none(
        Employee.email == body.email,
    )

    if employee != None:
        raise HasUserError()

    password_hash = create_password(body.password)

    employee = Employee.create(
        first_name=body.first_name,
        last_name=body.last_name,
        email=body.email,
        password=password_hash,
    )

    token: Token = Token.create(
        employee=employee.id,
        token=TokenManager.generate_token(request.app.config.TOKEN_LENGTH),
    )

    return token.to_json_response()
