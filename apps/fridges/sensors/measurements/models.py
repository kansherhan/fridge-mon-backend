from enum import Enum

from peewee import DecimalField, ForeignKeyField

from database.base_models import TimestampedModel
from database.fields import EnumField

from ..models import FridgeSensor


class SensorConnectionStatus(Enum):
    CONNECTED = "connected"
    DISCONNECTED = "disconnected"


class FridgeSensorMeasurement(TimestampedModel):
    sensor = ForeignKeyField(FridgeSensor, backref="measurements")

    temperature = DecimalField(max_digits=5, decimal_places=2, null=True)
    humidity = DecimalField(max_digits=5, decimal_places=2, null=True)

    connection_status = EnumField(SensorConnectionStatus)

    class Meta:
        table_name = "fridge_sensor_measurements"
        order_by = "created_at"
