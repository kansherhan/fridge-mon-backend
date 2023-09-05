from dataclasses import dataclass


@dataclass
class UpdateEmployeeParams:
    first_name: str
    last_name: str

    username: str
    email: str
