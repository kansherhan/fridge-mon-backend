from peewee import CharField, FloatField, ForeignKeyField

from database.fields.enum import EnumField
from database.models.base import BaseModelWithID
from database.models.status import DataStatus

from ..countries.models import Country


class City(BaseModelWithID):
    name = CharField(unique=True)

    latitude = FloatField()
    longitude = FloatField()

    country = ForeignKeyField(Country, backref="cities")

    status = EnumField(DataStatus, default=DataStatus.ACTIVE)

    class Meta:
        table_name = "cities"
