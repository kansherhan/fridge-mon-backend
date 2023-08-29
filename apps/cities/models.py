from peewee import CharField, FloatField, ForeignKeyField

from database.models.base import BaseModelWithID
from ..countries.models import Country


class City(BaseModelWithID):
    name = CharField(unique=True)

    latitude = FloatField()
    longitude = FloatField()

    country = ForeignKeyField(Country, backref="cities")

    class Meta:
        table_name = "cities"
