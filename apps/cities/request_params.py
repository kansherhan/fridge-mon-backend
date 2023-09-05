from dataclasses import dataclass


@dataclass
class CreateCityParams:
    name: str

    latitude: float
    longitude: float

    country: int


@dataclass
class UpdateCityParams:
    name: str

    latitude: float
    longitude: float

    country: int
