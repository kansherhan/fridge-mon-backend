from peewee import CharField
from database.base_models import BaseModel


class FridgeManufacturer(BaseModel):
    name = CharField(unique=True)

    class Meta:
        table_name = "fridge_manufacturers"
