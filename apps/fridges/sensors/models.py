from peewee import (
    CharField,
    ForeignKeyField,
    IntegerField,
)
from database.base_models import TimestampedModel
from ..models import Fridge


class FridgeSensor(TimestampedModel):
    name = CharField()

    fridge = ForeignKeyField(Fridge, backref="sensors")

    ip_address = CharField(max_length=50)
    exchange_protocol = CharField(max_length=50, null=True)
    start_register = IntegerField(null=True)
    register_count = IntegerField(null=True)

    class Meta:
        table_name = "fridge_sensors"
