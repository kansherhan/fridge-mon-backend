from peewee import *

from database.models.base import BaseModelWithID


class Country(BaseModelWithID):
    name = CharField(unique=True)

    class Meta:
        table_name = "countries"
