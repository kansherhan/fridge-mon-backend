from peewee import Model, PrimaryKeyField, DateTimeField, SQL
from sanic import Sanic, json
from datetime import datetime


class BaseModel(Model):
    id = PrimaryKeyField(unique=True)

    def to_dict(self):
        return self.__data__

    def to_json_response(self, **kwargs):
        return json(self, default=lambda o: o.to_dict(), sort_keys=True, **kwargs)

    class Meta:
        database = Sanic.get_app().ctx.db
        order_by = "id"


class TimestampedModel(BaseModel):
    created_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    updated_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    def save(self, *args, **kwargs):
        current_time = datetime.now()

        if self.updated_at is None:
            self.created_at = current_time

        self.updated_at = current_time

        return super(TimestampedModel, self).save(*args, **kwargs)
