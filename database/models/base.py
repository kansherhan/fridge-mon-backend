from enum import Enum
from datetime import datetime
from decimal import Decimal

from config import APP_NAME, DATETIME_FORMAT

from sanic import Sanic, json
from peewee import Model, PrimaryKeyField


class BaseModel(Model):
    _formatters = {
        datetime: lambda value: value.strftime(DATETIME_FORMAT),
        Decimal: lambda value: "{0:f}".format(value),
        Enum: lambda value: value.value,
    }

    __DICT_IGNORE__ = []

    @classmethod
    def _get_formatter(cls, value):
        for type, formatter in cls._formatters.items():
            if isinstance(value, type):
                return formatter
        return None

    def to_dict(self, ignore_keys: list[str] = None):
        if ignore_keys == None:
            ignore_keys = getattr(self, "__DICT_IGNORE__", None)

        dicts = {}

        for key, value in self.__data__.items():
            if ignore_keys and key in ignore_keys:
                continue

            formatter = self._get_formatter(value)

            if formatter != None:
                dicts[key] = formatter(value)
            else:
                dicts[key] = value

        return dicts

    def to_json_response(self, **kwargs):
        return json(self, default=lambda o: o.to_dict(), **kwargs)

    class Meta:
        database = Sanic.get_app(APP_NAME).ctx.db


class BaseHelperModel:
    @classmethod
    def find_by_id(cls, id: int):
        return cls.get_or_none(cls.id == id)

    @classmethod
    def find_all(cls):
        return cls.select().order_by(cls.id)


class BaseModelWithID(BaseModel, BaseHelperModel):
    id = PrimaryKeyField(unique=True)
