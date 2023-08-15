from dataclasses import dataclass


@dataclass
class CreateCompanyParams:
    inn: str
    name: str


@dataclass
class UpdateCompanyParams:
    inn: str
    name: str

    phone: str
    email: str