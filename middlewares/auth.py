from sanic import Request
from sanic.exceptions import Unauthorized

from apps.auth.models import EmployeeToken as Token


async def authentication_middleware(request: Request):
    if not hasattr(request.route.ctx, "unauthorized_request"):
        return

    if not request.token:
        raise Unauthorized()

    token: Token = Token.get_or_none(Token.token == request.token)

    if token == None:
        raise Unauthorized()

    request.ctx.user = token.employee
