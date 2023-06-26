from enum import Enum

from peewee import ForeignKeyField, CharField, DecimalField

from database.base_models import TimestampedModel
from database.fields import EnumField

from ..company.models import Company
from ..enterprises.models import Enterprise
from .categories.models import FridgeCategory as Category
from .manufacturers.models import FridgeManufacturer as Manufacturer


class FridgeStatus(Enum):
    INACTIVE = "inactive"
    ACTIVE = "active"
    BROKEN = "broken"


class Fridge(TimestampedModel):
    serial_number = CharField()

    company = ForeignKeyField(Company)
    enterprise = ForeignKeyField(Enterprise, backref="fridges")
    category = ForeignKeyField(Category)
    manufacturer = ForeignKeyField(Manufacturer)

    temperature_upper = DecimalField(max_digits=5, decimal_places=2, null=True)
    temperature_lower = DecimalField(max_digits=5, decimal_places=2, null=True)

    average_temperature = DecimalField(max_digits=7, decimal_places=2, null=True)
    average_humidity = DecimalField(max_digits=7, decimal_places=2, null=True)

    status = EnumField(FridgeStatus)

    class Meta:
        table_name = "fridges"
