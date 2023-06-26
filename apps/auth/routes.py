import bcrypt

from sanic import Blueprint, Request
from sanic.response import empty as empty_response
from sanic.exceptions import Forbidden
from sanic_ext import validate

from exceptions.has_user import HasUserError

from .token import TokenManager
from .models import EmployeeToken as Token
from .query_params import LoginParams, RegistrationParams
from ..employees.models import Employee

routes = Blueprint("auth", "/auth")


@routes.post("/login", ctx_unauthorized_request=True)
@validate(json=LoginParams)
async def login(request: Request, body: LoginParams):
    """Авторизации в системе"""

    employee: Employee = Employee.get_or_none(Employee.email == body.email)

    if employee != None:
        if bcrypt.checkpw(body.password.encode(), employee.password.encode()):
            token: Token = employee.tokens[-1] if len(employee.tokens) > 0 else None

            if token != None and TokenManager.check_token_lifetime(
                token, request.app.config.TOKEN_LIFETIME
            ):
                return token.to_json_response()
            else:
                token: Token = Token.create(
                    employee=employee.id,
                    token=TokenManager.generate_token(request.app.config.TOKEN_LENGTH),
                )

                return token.to_json_response()

    raise Forbidden()


@routes.post("/logout")
async def logout(request: Request):
    """Выйти из системы, удаления всех токенов авторизации"""

    user: Employee = request.ctx.user

    for token in user.tokens:
        token.delete_instance()

    return empty_response()


@routes.post("/registration", ctx_unauthorized_request=True)
@validate(json=RegistrationParams)
async def registration(request: Request, body: RegistrationParams):
    """Регистрация в системе"""

    employee: Employee = Employee.get_or_none(Employee.email == body.email)

    if employee != None:
        raise HasUserError()

    password_hash = bcrypt.hashpw(
        body.password.encode(),
        request.app.config.USER_PASSWORD_SALT,
    )

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
