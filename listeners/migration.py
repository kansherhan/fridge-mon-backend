from sanic import Sanic

from database.migration import migrate


async def register_migrate_task(app: Sanic):
    if app.config.MIGRATION:
        await migrate(app)
        # app.add_task(migrate, name="migration")
