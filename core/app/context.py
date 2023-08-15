from sanic.config import Config

from database.connection import create_database_connection


class AppContext:
    def __init__(self, config: Config) -> None:
        self.db = create_database_connection(
            config.DATABASE_TABLENAME,
            config.DATABASE_USERNAME,
            config.DATABASE_PASSWORD,
            config.DATABASE_HOST,
            config.DATABASE_PORT,
        )
