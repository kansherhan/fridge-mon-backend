from sanic import Request
from sanic.exceptions import Unauthorized


async def _check_token(request) -> bool:
    return True

    if not request.token:
        return False

    try:
        return True
    except:
        return False
    else:
        return True


async def authentication_middleware(request: Request):
    if await _check_token(request):
        pass
    else:
        raise Unauthorized()
