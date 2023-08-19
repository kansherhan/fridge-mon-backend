from sanic import Request, Blueprint, text
from sanic.request import File

from redis import Redis

from core.hash import Hash
from core.app.request import AppRequest
from core.response.image import image

from exceptions.image_not_found import ImageNotFoundError

from database.models.imageable import ImageableModel
from ..employees.models import Employee


__IMAGE_NAME__ = "image"

routes = Blueprint("images", "/images")


@routes.get("/get/<image_name>")
async def get_images(request: AppRequest, image_name: str):
    redis: Redis = request.app.ctx.redis

    image_bytes = redis.get(image_name)

    if image_bytes == None:
        raise ImageNotFoundError()

    return image(image_bytes)


@routes.post("/me")
async def set_image_current_user(request: AppRequest):
    file: File = get_image(request)

    redis: Redis = request.app.ctx.redis
    user: Employee = request.ctx.user

    image_filename = update_image(
        user,
        file,
        redis,
        request.config.IMAGE_NAME_LENGTH,
    )

    if image_filename != None:
        return text(image_filename)
    else:
        return request.empty()


def get_image(request: AppRequest) -> File:
    file: File = request.files.get(__IMAGE_NAME__)

    if file == None:
        raise ImageNotFoundError()

    return file


def update_image(
    model: ImageableModel,
    file: File,
    redis: Redis,
    hash_length: int,
) -> str | None:
    if len(file.body) > 0:
        image_filename = Hash.generate_hash(hash_length)

        redis.set(image_filename, file.body)

        model.icon_url = image_filename
        model.save()

        return image_filename
    else:
        if model.icon_url != None:
            redis.delete(model.icon_url)

        model.icon_url = None
        model.save()
