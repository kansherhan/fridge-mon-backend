from peewee import PostgresqlDatabase


def create_database_connection(
    database_name: str,
    username: str,
    password: str,
    host: str = "localhost",
    port: int = 5432,
):
    psql_db_connection = PostgresqlDatabase(
        database_name, user=username, password=password, host=host, port=port
    )

    return psql_db_connection
