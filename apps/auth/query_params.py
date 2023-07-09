from dataclasses import dataclass


@dataclass
class LoginParams:
    email: str
    password: str


@dataclass
class RegistrationParams:
    first_name: str
    last_name: str
    email: str
    password: str
