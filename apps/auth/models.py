from peewee import ForeignKeyField, CharField

from database.models.timestamped import TimestampedModel
from ..employees.models import Employee


class EmployeeToken(TimestampedModel):
    employee = ForeignKeyField(Employee, backref="tokens")
    token = CharField(unique=True)

    class Meta:
        table_name = "company_employee_tokens"
