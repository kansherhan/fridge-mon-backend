from peewee import *

from database.base_models import BaseModel


class Country(BaseModel):
    name = CharField(unique=True)

    class Meta:
        table_name = "countries"
