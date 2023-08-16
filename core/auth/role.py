from apps.employees.models import Employee
from apps.companies.models import Company
from apps.employees.roles.models import EmployeeRole, CompanyRole


class AuthRole:
    @staticmethod
    def check(
        user: Employee,
        company: Company,
        need_role: CompanyRole = None,
    ) -> bool:
        user_roles: list[EmployeeRole] = user.roles

        for role in user_roles:
            if role.company.id == company.id:
                if need_role == None:
                    return True
                else:
                    return role.role == need_role

        return False
