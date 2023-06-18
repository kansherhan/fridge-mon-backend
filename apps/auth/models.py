from datetime import datetime
from peewee import ForeignKeyField, CharField, DateTimeField

from database.base_models import BaseModel
from ..employees.models import Employee


class EmployeeToken(BaseModel):
    employee = ForeignKeyField(Employee, backref="employees")
    token = CharField()
    token_created_at = DateTimeField()

    @staticmethod
    def new(token: str, employee: Employee):
        tokenModel = EmployeeToken()
        tokenModel.token = token
        tokenModel.employee = employee
        tokenModel.token_created_at = datetime.now()

        return tokenModel

    class Meta:
        table_name = "company_employee_tokens"
