from dataclasses import dataclass


@dataclass
class CreateManufacturersParams:
    device_id: str
    temperature: str
    humidity: str
