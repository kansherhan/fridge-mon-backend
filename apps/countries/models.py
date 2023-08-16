from peewee import *

from database.models.base import BaseModel


class Country(BaseModel):
    name = CharField(unique=True)

    class Meta:
        table_name = "countries"
