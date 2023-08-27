from enum import Enum

from peewee import ForeignKeyField, CharField, DecimalField

from database.models.timestamped import TimestampedModel
from database.models.status import DataStatus
from database.fields.enum import EnumField

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

    status = EnumField(DataStatus, default=DataStatus.ACTIVE)
    fridge_status = EnumField(FridgeStatus, default=FridgeStatus.ACTIVE)

    class Meta:
        table_name = "fridges"
