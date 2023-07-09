from peewee import CharField, FloatField, ForeignKeyField

from database.base_models import BaseModel
from ..countries.models import Country


class City(BaseModel):
    name = CharField(unique=True)

    latitude = FloatField()
    longitude = FloatField()

    country = ForeignKeyField(Country, backref="cities")

    class Meta:
        table_name = "cities"
