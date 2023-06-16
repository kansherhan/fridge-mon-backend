from datetime import datetime
from peewee import ForeignKeyField, CharField, DateTimeField

from database.base_models import BaseModel
from ..employees.models import CompanyEmployee as Employee


class CompanyEmployeeToken(BaseModel):
    employee = ForeignKeyField(Employee, backref="employees", lazy_load=False)
    token = CharField()
    token_created_at = DateTimeField()

    @classmethod
    def create(token: str):
        tokenModel = CompanyEmployeeToken()
        tokenModel.token = token
        tokenModel.token_created_at = datetime.now()

        tokenModel.save()
