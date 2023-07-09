from os.path import abspath

APP_NAME = "fridje_mon"
APP_HOST = "0.0.0.0"
APP_PORT = 8000

APPS_FOLDER_NAME = "apps"
APPS_FOLDER_PATH = abspath(APPS_FOLDER_NAME)

ROUTE_PREFIX = "/api"

DATABASE_PORT = 5432
DATABASE_HOST = "127.0.0.1"
DATABASE_USERNAME = "sherhan"
DATABASE_PASSWORD = "123456"
DATABASE_TABLENAME = "fridge_mon"

DATETIME_FORMAT = "%Y-%m-%d %H:%M:%S"

OAS_URL_PREFIX = "/apidocs"
OAS_UI_SWAGGER = False

FALLBACK_ERROR_FORMAT = "json"

TOKEN_LIFETIME = 86400
TOKEN_LENGTH = 32

CORS_ORIGINS = "*"  # ",".join(["http://localhost", "example.com"])

REDIRECTS = {}
