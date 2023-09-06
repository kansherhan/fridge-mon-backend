from peewee import CharField

from database.fields.enum import EnumField
from database.models.status import DataStatus
from database.models.base import BaseModelWithID


class FridgeCategory(BaseModelWithID):
    name = CharField(unique=True)

    status = EnumField(DataStatus, default=DataStatus.ACTIVE)

    class Meta:
        table_name = "fridge_categories"
