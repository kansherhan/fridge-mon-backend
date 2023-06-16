from enum import Enum
from datetime import datetime
from peewee import Model, CharField, PrimaryKeyField, DateTimeField
from sanic import Sanic, json


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
    created_at = DateTimeField()
    updated_at = DateTimeField()

    def save(self, *args, **kwargs):
        current_time = datetime.now()

        if self.updated_at is None:
            self.created_at = current_time

        self.updated_at = current_time

        return super(TimestampedModel, self).save(*args, **kwargs)


class EnumField(CharField):
    def __init__(self, enum: type[Enum], *args, **kwargs):
        self.enum = enum
        super(CharField, self).__init__(*args, **kwargs)

    def db_value(self, value):
        return value.value

    def python_value(self, value):
        return self.enum(value)
