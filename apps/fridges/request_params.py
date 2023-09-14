from dataclasses import dataclass


@dataclass
class CreateFridgeParams:
    name: str

    company: int
    enterprise: int

    template_id: int

    category_id: int
    manufacturer_id: int

    temperature_upper: float
    temperature_lower: float


@dataclass
class UpdateFridgeParams:
    name: str

    temperature_upper: float
    temperature_lower: float

    status: str
