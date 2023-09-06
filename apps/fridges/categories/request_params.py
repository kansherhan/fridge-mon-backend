from dataclasses import dataclass


@dataclass
class CreateFridgeCategoryParams:
    name: str


@dataclass
class UpdateFridgeCategoryParams:
    name: str
