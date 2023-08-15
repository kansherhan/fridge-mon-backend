from os.path import abspath

APP_NAME = "fridge_mon"
APP_HOST = "0.0.0.0"
APP_PORT = 8000
APP_UNIX = "fridge"

APPS_FOLDER_NAME = "apps"
APPS_FOLDER_PATH = abspath(APPS_FOLDER_NAME)

ROUTE_PREFIX = "/api"

DATABASE_PORT = 5432
DATABASE_HOST = "85.198.90.69"
DATABASE_USERNAME = "postgres"
DATABASE_PASSWORD = "123456"
DATABASE_TABLENAME = "fridge_mon"

HTTP_ALL_METHODS = False

DATETIME_FORMAT = "%Y-%m-%d %H:%M:%S"

OAS_URL_PREFIX = "/api/docs"
OAS_UI_SWAGGER = False

FALLBACK_ERROR_FORMAT = "json"

TOKEN_LIFETIME = 86400
TOKEN_LENGTH = 32

CORS = False
CORS_OPTIONS = {
    "resources": r"/*",
    "origins": "*",
    "methods": ["GET", "POST", "HEAD", "OPTIONS"],
}

REDIRECTS = {}

NO_AUTH_URLS = [
    "/",
    "/api/auth/login",
    "/api/auth/registration",
]
