from enum import Enum

from peewee import ForeignKeyField, CharField, DecimalField

from database.base_models import TimestampedModel
from database.fields import EnumField

from ..companies.models import Company
from ..enterprises.models import Enterprise


class FridgeStatus(Enum):
    INACTIVE = "inactive"
    ACTIVE = "active"
    BROKEN = "broken"


class Fridge(TimestampedModel):
    name = CharField()

    serial_number = CharField(unique=True)

    company = ForeignKeyField(Company)
    enterprise = ForeignKeyField(Enterprise, backref="fridges")

    temperature_upper = DecimalField(max_digits=5, decimal_places=2)
    temperature_lower = DecimalField(max_digits=5, decimal_places=2)

    status = EnumField(FridgeStatus)

    class Meta:
        table_name = "fridges"
