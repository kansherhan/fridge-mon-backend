from sanic import Request
from sanic.exceptions import Unauthorized, Forbidden

from apps.auth.models import EmployeeToken as Token


async def authentication_middleware(request: Request):
    config = request.app.config

    if not config.AUTHORIZATION:
        return

    if config.APP_DEBUG and request.path.startswith(config.OAS_URL_PREFIX):
        return

    if request.route and hasattr(request.route.ctx, "unauthorized_request"):
        return

    if not request.token:
        raise Unauthorized()

    token: Token = Token.get_or_none(Token.token == request.token)

    if token == None:
        raise Forbidden()

    request.ctx.user = token.employee
