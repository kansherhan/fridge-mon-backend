from enum import Enum
from datetime import datetime
from peewee import Model, CharField, PrimaryKeyField, DateTimeField
from sanic import Sanic, json


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
            if type(self.__data__[key]) == datetime:
                dicts[key] = self.__data__[key].strftime("%Y-%m-%d %H:%M:%S")
            else:
                dicts[key] = self.__data__[key]

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
