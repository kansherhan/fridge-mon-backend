from database.base_models import TimestampedModel, CharField


class Employee(TimestampedModel):
    first_name = CharField()
    last_name = CharField()
    email = CharField(unique=True)
    password = CharField()

    class Meta:
        table_name = "company_employees"
