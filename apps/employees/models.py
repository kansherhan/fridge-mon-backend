from peewee import CharField

from database.models.timestamped import TimestampedWithIDModel


class Employee(TimestampedWithIDModel):
    first_name = CharField()
    last_name = CharField()

    email = CharField(max_length=50, unique=True)
    password = CharField()

    icon_url = CharField(null=True)

    __DICT_IGNORE__ = ["password"]

    @classmethod
    def find_by_email(cls, email):
        return cls.get_or_none(cls.email == email)

    class Meta:
        table_name = "company_employees"
