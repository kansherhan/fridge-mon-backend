from peewee import CharField

from database.models.timestamped import TimestampedWithIDModel


class Employee(TimestampedWithIDModel):
    first_name = CharField(max_length=30)
    last_name = CharField(max_length=30)

    username = CharField(max_length=30, unique=True)
    password = CharField()

    email = CharField(max_length=50)

    icon_url = CharField(null=True)

    __DICT_IGNORE__ = ["password"]

    class Meta:
        table_name = "company_employees"
