from peewee import CharField, ForeignKeyField, FloatField

from database.models.timestamped import TimestampedModel
from database.models.status import DataStatus
from database.fields.enum import EnumField

from ..companies.models import Company
from ..cities.models import City

__ENTERPRISE_BACKREF__ = "enterprises"


class Enterprise(TimestampedModel):
    name = CharField()

    address = CharField(null=True)

    city = ForeignKeyField(City, backref=__ENTERPRISE_BACKREF__)
    company = ForeignKeyField(Company, backref=__ENTERPRISE_BACKREF__)

    latitude = FloatField()
    longitude = FloatField()

    phone = CharField(max_length=20, null=True)
    email = CharField(max_length=50, null=True)

    icon_url = CharField(null=True)

    status = EnumField(DataStatus, default=DataStatus.ACTIVE)

    class Meta:
        table_name = "company_enterprises"
