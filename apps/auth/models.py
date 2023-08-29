from datetime import datetime

from peewee import (
    ForeignKeyField,
    CharField,
    DateTimeField,
)

from database.models.base import BaseModel
from ..employees.models import Employee


class EmployeeToken(BaseModel):
    employee = ForeignKeyField(Employee, backref="tokens")
    token = CharField(unique=True)

    created_at = DateTimeField()

    def save(self, *args, **kwargs):
        if self.created_at == None:
            self.created_at = datetime.now()

        return super(EmployeeToken, self).save(*args, **kwargs)

    class Meta:
        table_name = "company_employee_tokens"
        primary_key = False
