from enum import Enum

from peewee import ForeignKeyField

from database.models.base import BaseModel
from database.fields.enum import EnumField

from ...employees.models import Employee
from ...companies.models import Company


class CompanyRole(Enum):
    OWNER = "owner"
    ADMINISTRATOR = "administrator"
    MODERATOR = "moderator"
    VIEWER = "viewer"


ROLES = [e.name for e in CompanyRole]


class EmployeeRole(BaseModel):
    employee = ForeignKeyField(Employee, backref="roles")
    company = ForeignKeyField(Company, backref="roles")

    role = EnumField(CompanyRole)

    class Meta:
        table_name = "company_employee_roles"
