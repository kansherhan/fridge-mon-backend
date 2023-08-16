from sanic import Request

from peewee import PostgresqlDatabase

from exceptions.db import DBError


async def reload_db_connect(request: Request):
    db: PostgresqlDatabase = request.app.ctx.db

    if db.is_closed() == True:
        is_connected = db.connect()

        if is_connected == False:
            raise DBError()
