from peewee import CharField
from database.models.base import BaseModelWithID


class FridgeManufacturer(BaseModelWithID):
    name = CharField(unique=True)

    class Meta:
        table_name = "fridge_manufacturers"
