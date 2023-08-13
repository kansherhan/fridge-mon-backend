from dataclasses import dataclass


@dataclass
class CreateEnterpriseParams:
    name: str

    city: int

    latitude: float
    longitude: float


@dataclass
class UpdateEnterpriseParams:
    name: str

    address: str

    city: int

    phone: str
    email: str

    latitude: float
    longitude: float
