from os.path import abspath

APP_NAME = "fridge_mon"
APP_HOST = "0.0.0.0"
APP_PORT = 8000
APP_UNIX = "fridge"

APPS_FOLDER_NAME = "apps"
APPS_FOLDER_PATH = abspath(APPS_FOLDER_NAME)

ROUTE_PREFIX = "/api"

DATABASE_PORT = 5432
DATABASE_HOST = "127.0.0.1"
DATABASE_USERNAME = "postgres"
DATABASE_PASSWORD = "123456"
DATABASE_TABLENAME = "fridge_mon"

REDIS_PORT = 6379
REDIS_HOST = "127.0.0.1"
REDIS_PASSWORD = None  # "123456"

HTTP_ALL_METHODS = False

DATETIME_FORMAT = "%Y-%m-%d %H:%M:%S"

OAS_URL_PREFIX = "/api/docs"
OAS_UI_SWAGGER = False

FALLBACK_ERROR_FORMAT = "json"

TOKEN_LIFETIME = 86400
TOKEN_LENGTH = 32

IMAGE_NAME_LENGTH = 64

CORS = False
CORS_OPTIONS = {
    "resources": r"/*",
    "origins": "*",
    "methods": [
        "GET",
        "POST",
        "PUT",
        "HEAD",
        "OPTIONS",
        "PATCH",
        "DELETE",
    ],
}

REDIRECTS_URLS = {
    # "/": "/hello_world", Example, redirect url
}

IGNORE_AUTHORIZATION_URLS = [
    {
        "url": "/",
        "has_params": False,
    },
    {
        "url": "/api/docs",
        "has_params": False,
    },
    {
        "url": "/api/auth/login",
        "has_params": False,
    },
    {
        "url": "/api/auth/registration",
        "has_params": False,
    },
    {
        "url": "/api/images/get",
        "has_params": True,
    },
]
