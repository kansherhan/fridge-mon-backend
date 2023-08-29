from peewee import CharField

from database.models.timestamped import TimestampedWithIDModel
from database.models.status import DataStatus
from database.fields.enum import EnumField


class Company(TimestampedWithIDModel):
    inn = CharField(max_length=20)
    name = CharField()

    phone = CharField(max_length=20, null=True)
    email = CharField(max_length=50, null=True)

    icon_url = CharField(null=True)

    status = EnumField(DataStatus, default=DataStatus.ACTIVE)

    class Meta:
        table_name = "companies"
