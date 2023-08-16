from sanic import Request

from apps.auth.models import EmployeeToken as Token

from exceptions.auth.token import TokenError, TokenNotFoundError


async def authentication_middleware(request: Request):
    config = request.app.config

    if config.OAS and request.path.startswith(config.OAS_URL_PREFIX):
        return

    if request.path in request.app.config.NO_AUTH_URLS:
        return

    if not request.token:
        raise TokenNotFoundError()

    token: Token = Token.get_or_none(Token.token == request.token)

    if token == None:
        raise TokenError()

    request.ctx.user = token.employee
    request.ctx.user_token = token
