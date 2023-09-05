from dataclasses import dataclass


@dataclass
class LoginParams:
    username: str
    password: str


@dataclass
class RegistrationParams:
    first_name: str
    last_name: str
    username: str
    password: str
