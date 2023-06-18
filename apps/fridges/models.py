from enum import Enum

from peewee import ForeignKeyField, CharField, DecimalField

from database.base_models import TimestampedModel, EnumField, BaseModel

from ..company.models import Company
from ..enterprises.models import Enterprise
from .categories.models import FridgeCategory as Category
from .manufacturers.models import FridgeManufacturer as Manufacturer

__FRIDGE_BACKREF__ = "fridges"


class FridgeStatus(Enum):
    INACTIVE = "inactive"
    ACTIVE = "active"
    BROKEN = "broken"


class Fridge(BaseModel):
    serial_number = CharField()

    company = ForeignKeyField(Company, backref=__FRIDGE_BACKREF__)
    enterprise = ForeignKeyField(Enterprise, backref=__FRIDGE_BACKREF__)
    category = ForeignKeyField(Category, backref=__FRIDGE_BACKREF__)
    manufacturer = ForeignKeyField(Manufacturer, backref=__FRIDGE_BACKREF__)

    temperature_upper = DecimalField(max_digits=5, decimal_places=2)
    temperature_lower = DecimalField(max_digits=5, decimal_places=2)

    status = EnumField(FridgeStatus)

    class Meta:
        table_name = "fridges"
