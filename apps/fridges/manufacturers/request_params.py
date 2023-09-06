from dataclasses import dataclass


@dataclass
class CreateFridgeManufacturerParams:
    name: str


@dataclass
class UpdateFridgeManufacturerParams:
    name: str
