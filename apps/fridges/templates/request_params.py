from dataclasses import dataclass


@dataclass
class CreateFridgeTemplateParams:
    name: str

    company_id: int

    temperature_upper: float
    temperature_lower: float


@dataclass
class UpdateFridgeTemplateParams:
    name: str

    temperature_upper: float
    temperature_lower: float
