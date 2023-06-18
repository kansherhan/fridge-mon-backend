from peewee import ForeignKeyField, CharField, DecimalField

from database.base_models import TimestampedModel


class Fridge(TimestampedModel):
    company = ForeignKeyField()
