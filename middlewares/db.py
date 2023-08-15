from sanic import Request
from peewee import PostgresqlDatabase


async def reload_db_connect(request: Request):
    db: PostgresqlDatabase = request.app.ctx.db

    if db.is_closed() == True:
        db.connect()
