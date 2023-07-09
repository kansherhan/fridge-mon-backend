from enum import Enum

from peewee import ForeignKeyField

from database.base_models import BaseModel
from database.fields import EnumField

from ...employees.models import Employee
from ...companies.models import Company
from ...enterprises.models import Enterprise


class CompanyRole(Enum):
    OWNER = "owner"
    ADMINISTRATOR = "administrator"
    MODERATOR = "moderator"
    VIEWER = "viewer"


class EmployeeRole(BaseModel):
    employee = ForeignKeyField(Employee, backref="roles")
    company = ForeignKeyField(Company)
    enterprise = ForeignKeyField(Enterprise, null=True)

    role = EnumField(CompanyRole)

    class Meta:
        table_name = "company_employee_roles"
