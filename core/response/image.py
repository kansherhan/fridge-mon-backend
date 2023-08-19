from sanic.response import HTTPResponse


def image(
    body,
    status_code: int = 200,
    content_type: str = "image\jpeg",
):
    return HTTPResponse(
        body=body,
        status=status_code,
        content_type=content_type,
    )
