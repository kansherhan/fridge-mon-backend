from os.path import abspath

APP_NAME = "fridje_mon"
APP_HOST = "0.0.0.0"
APP_PORT = 8000

APPS_FOLDER_NAME = "apps"
APPS_FOLDER_PATH = abspath(APPS_FOLDER_NAME)

DATABASE_PORT = 5432
DATABASE_HOST = "localhost"
DATABASE_USERNAME = "postgres"
DATABASE_PASSWORD = "postgres"
DATABASE_TABLENAME = "fridje_mon"

OAS_URL_PREFIX = "/apidocs"

CORS_ORIGINS = "*"
# CORS_ORIGINS = ",".join(["http://localhost"])

REDIRECTS = {}
