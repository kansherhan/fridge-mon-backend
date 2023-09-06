from dataclasses import dataclass


@dataclass
class CreateCompanyParams:
    name: str


@dataclass
class UpdateCompanyParams:
    inn: str
    name: str

    phone: str
    email: str


@dataclass
class CreateCompanyRoleParams:
    username: str
    company: int
    role: str
