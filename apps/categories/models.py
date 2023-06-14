from peewee import CharField
from database.base_models import BaseModel


class Category(BaseModel):
    name_categor = CharField()

    class Meta:
        table_name = "categories"
