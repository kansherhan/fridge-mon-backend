from sanic.config import Config
from redis import Redis

from database.connect import CreateDatabaseConnection


class AppContext:
    def __init__(self, config: Config) -> None:
        self.config = config

        self.redis = Redis(
            host=config.REDIS_HOST,
            port=config.REDIS_PORT,
            password=config.REDIS_PASSWORD,
        )

        self.db = CreateDatabaseConnection(
            config.DATABASE_TABLENAME,
            config.DATABASE_USERNAME,
            config.DATABASE_PASSWORD,
            config.DATABASE_HOST,
            config.DATABASE_PORT,
        )
