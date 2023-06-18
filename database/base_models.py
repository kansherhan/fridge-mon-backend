from enum import Enum
from datetime import datetime
from decimal import Decimal

from sanic import Sanic, json
from peewee import Model, CharField, PrimaryKeyField, DateTimeField


class BaseModel(Model):
    id = PrimaryKeyField(unique=True)

    @classmethod
    def find_by_id(cls, id: int):
        return cls.get_or_none(cls.id == id)

    @classmethod
    def find_all(cls):
        return cls.select().order_by(cls.id)

    def to_dict(self):
        dicts = {}

        for key in self.__data__.keys():
            value = self.__data__[key]
            value_type = type(value)

            if value_type == datetime:
                dicts[key] = value.strftime("%Y-%m-%d %H:%M:%S")
            elif value_type == Decimal:
                dicts[key] = "{0:f}".format(value)
            elif isinstance(value, Enum):
                dicts[key] = value.value
            else:
                dicts[key] = value

        return dicts

    def to_json_response(self, **kwargs):
        return json(self, default=lambda o: o.to_dict(), **kwargs)

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
