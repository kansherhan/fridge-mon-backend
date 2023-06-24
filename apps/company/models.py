from peewee import CharField

from database.base_models import TimestampedModel


class Company(TimestampedModel):
    inn = CharField(max_length=20)
    name = CharField()

    phone = CharField(max_length=20, null=True)
    email = CharField(max_length=50, null=True)

    icon_url = CharField(null=True)

    class Meta:
        table_name = "companies"
