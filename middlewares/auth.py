from core.app.request import AppRequest

from core.token import TokenManager
from apps.auth.models import EmployeeToken as Token

from exceptions.auth.token import (
    TokenError,
    TokenNotFoundError,
    TokenLifeCycleError,
)


async def authentication_middleware(request: AppRequest):
    config = request.config

    for item in config.IGNORE_AUTHORIZATION_URLS:
        if request.path.startswith(item["url"]):
            if item["has_params"] or request.path == item["url"]:
                return

    if not request.token:
        raise TokenNotFoundError()

    token: Token = Token.get_or_none(Token.token == request.token)

    if token == None:
        raise TokenError()

    if not TokenManager.check_token_life_cycle(token, config.TOKEN_LIFETIME):
        raise TokenLifeCycleError()

    request.user = token.employee
    request.user_token = token
