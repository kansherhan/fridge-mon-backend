from sanic.config import Config
from types import SimpleNamespace

from database.connect import CreateDatabaseConnection


class AppContext(SimpleNamespace):
    def __init__(self, config: Config) -> None:
        self.config = config

        self.db = CreateDatabaseConnection(
            config.DATABASE_TABLENAME,
            config.DATABASE_USERNAME,
            config.DATABASE_PASSWORD,
            config.DATABASE_HOST,
            config.DATABASE_PORT,
        )

        self.extend = None
