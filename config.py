from os.path import abspath

APP_NAME = "fridge_mon"
APP_HOST = "0.0.0.0"
APP_PORT = 4978
APP_UNIX = "fridge"

APPS_FOLDER_NAME = "apps"
APPS_FOLDER_PATH = abspath(APPS_FOLDER_NAME)

ROUTE_PREFIX = "/api"

DATABASE_PORT = 7894
DATABASE_HOST = "85.198.90.13"
DATABASE_USERNAME = "sherhan"
DATABASE_PASSWORD = "b2330fc4531de135266de49078c270dd"
DATABASE_TABLENAME = "fridge_mon"

REDIS_PORT = 5951
REDIS_HOST = "85.198.90.13"
REDIS_PASSWORD = "716122e5d2fc73f69af7fdfaa366d777"

REQUEST_MAX_SIZE = 3000000

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
