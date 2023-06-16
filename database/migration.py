from os import listdir, path
import inspect
from importlib import import_module

from sanic import Sanic
from sanic.config import Config
from peewee import PostgresqlDatabase

from database.base_models import BaseModel

__APPS_MODELS_FILE__ = "models"


def migrate(app: Sanic, config: Config) -> None:
    database_connection: PostgresqlDatabase = app.ctx.db

    apps_folder_names = listdir(config.APPS_FOLDER_PATH)

    for app_name in apps_folder_names:
        app_models_file = path.join(
            config.APPS_FOLDER_PATH, app_name, __APPS_MODELS_FILE__ + ".py"
        )

        if path.exists(app_models_file):
            app_models_module = import_module(
                f"{config.APPS_FOLDER_NAME}.{app_name}.{__APPS_MODELS_FILE__}"
            )

            models = []
            models_classes = inspect.getmembers(app_models_module, inspect.isclass)

            for _class in models_classes:
                [class_name, class_type] = _class

                if (
                    issubclass(class_type, BaseModel)
                    and class_name != BaseModel.__name__
                ):
                    models.append(class_type)

            database_connection.create_tables(models)
