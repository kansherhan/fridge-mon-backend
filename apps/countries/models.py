from peewee import *

from database.fields.enum import EnumField
from database.models.status import DataStatus
from database.models.base import BaseModelWithID


class Country(BaseModelWithID):
    name = CharField(unique=True)

    status = EnumField(DataStatus, default=DataStatus.ACTIVE)

    class Meta:
        table_name = "countries"
