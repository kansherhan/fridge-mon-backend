from peewee import PostgresqlDatabase


def CreateDatabaseConnection(
    database_name: str,
    username: str,
    password: str,
    host: str = "127.0.0.1",
    port: int = 5432,
):
    psql = PostgresqlDatabase(
        database_name,
        user=username,
        password=password,
        host=host,
        port=port,
    )

    return psql
