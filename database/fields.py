from enum import Enum

from peewee import CharField


class EnumField(CharField):
    def __init__(self, enum: type[Enum], *args, **kwargs):
        self.enum = enum
        super(CharField, self).__init__(*args, **kwargs)

    def db_value(self, value):
        if isinstance(value, Enum):
            return value.value
        else:
            return value

    def python_value(self, value):
        return self.enum(value)
