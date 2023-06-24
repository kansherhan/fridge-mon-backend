from enum import Enum
from datetime import datetime
from decimal import Decimal

from sanic import Sanic, json
from peewee import Model, PrimaryKeyField, DateTimeField


class BaseModel(Model):
    _formatters = {
        datetime: lambda value: value.strftime("%Y-%m-%d %H:%M:%S"),
        Decimal: lambda value: "{0:f}".format(value),
        Enum: lambda value: value.value,
    }

    id = PrimaryKeyField(unique=True)

    @classmethod
    def find_by_id(cls, id: int):
        return cls.get_or_none(cls.id == id)

    @classmethod
    def find_all(cls):
        return cls.select().order_by(cls.id)

    @classmethod
    def _get_formatter(cls, value):
        for type, formatter in cls._formatters.items():
            if isinstance(value, type):
                return formatter
        return None

    def to_dict(self):
        dicts = {}

        for key, value in self.__data__.items():
            formatter = self._get_formatter(value)

            if formatter != None:
                dicts[key] = formatter(value)
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
