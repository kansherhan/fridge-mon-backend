from peewee import CharField
from database.base_models import BaseModel


class FridgeCategory(BaseModel):
    name = CharField(unique=True)

    class Meta:
        table_name = "fridge_categories"
