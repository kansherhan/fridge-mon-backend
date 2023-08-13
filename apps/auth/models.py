from peewee import ForeignKeyField, CharField

from database.base_models import TimestampedModel
from ..employees.models import Employee


class EmployeeToken(TimestampedModel):
    employee = ForeignKeyField(Employee, backref="tokens")
    token = CharField(unique=True)

    class Meta:
        table_name = "company_employee_tokens"
