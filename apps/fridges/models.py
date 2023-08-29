from enum import Enum

from peewee import ForeignKeyField, CharField, DecimalField

from database.models.timestamped import TimestampedWithIDModel
from database.models.status import DataStatus
from database.fields.enum import EnumField

from .categories.models import FridgeCategory as Category
from .manufacturers.models import FridgeManufacturer as Manufacturer
from ..companies.models import Company
from ..enterprises.models import Enterprise


class FridgeStatus(Enum):
    INACTIVE = "inactive"
    ACTIVE = "active"
    BROKEN = "broken"


class Fridge(TimestampedWithIDModel):
    name = CharField()

    serial_number = CharField(unique=True)

    company = ForeignKeyField(Company)
    enterprise = ForeignKeyField(Enterprise, backref="fridges")

    category = ForeignKeyField(Category)
    manufacturer = ForeignKeyField(Manufacturer)

    temperature_upper = DecimalField(max_digits=5, decimal_places=2)
    temperature_lower = DecimalField(max_digits=5, decimal_places=2)

    status = EnumField(DataStatus, default=DataStatus.ACTIVE)
    fridge_status = EnumField(FridgeStatus, default=FridgeStatus.ACTIVE)

    class Meta:
        table_name = "fridges"
