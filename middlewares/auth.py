from sanic import Request

from apps.auth.models import EmployeeToken as Token

from exceptions.token_error import TokenError


async def authentication_middleware(request: Request):
    config = request.app.config

    if not config.AUTHORIZATION:
        return

    if config.DEBUG and request.path.startswith(config.OAS_URL_PREFIX):
        return

    if request.route and hasattr(request.route.ctx, "unauthorized_request"):
        return

    if not request.token:
        raise TokenError()

    token: Token = Token.get_or_none(Token.token == request.token)

    if token == None:
        raise TokenError()

    request.ctx.user = token.employee
