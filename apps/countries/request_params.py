from dataclasses import dataclass


@dataclass
class CreateCountryParams:
    name: str


@dataclass
class UpdateCountryParams:
    name: str
