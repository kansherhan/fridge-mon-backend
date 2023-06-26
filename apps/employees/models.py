from peewee import CharField

from database.base_models import TimestampedModel


class Employee(TimestampedModel):
    first_name = CharField()
    last_name = CharField()

    email = CharField(max_length=50, unique=True)
    password = CharField()

    icon_url = CharField(null=True)

    __DICT_IGNORE__ = ["password"]

    class Meta:
        table_name = "company_employees"
