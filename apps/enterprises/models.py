from peewee import CharField, ForeignKeyField, FloatField

from database.base_models import TimestampedModel

from ..company.models import Company


class Enterprise(TimestampedModel):
    name = CharField()
    address = CharField()

    company = ForeignKeyField(Company, backref="enterprises")

    latitude = FloatField()
    longitude = FloatField()

    phone = CharField(max_length=20)
    email = CharField(max_length=50)

    icon_url = CharField(null=True)

    class Meta:
        table_name = "company_enterprises"
