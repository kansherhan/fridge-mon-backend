from sanic import Request
from sanic.exceptions import Unauthorized

from apps.auth.models import CompanyEmployeeToken as Token


async def authentication_middleware(request: Request):
    if not hasattr(request.route.ctx, "unauthorized_request"):
        return

    if not request.token:
        raise Unauthorized()

    token = Token.get_or_none(Token.token == request.token)

    if token == None:
        raise Unauthorized()

    request.ctx.user = token.employee
