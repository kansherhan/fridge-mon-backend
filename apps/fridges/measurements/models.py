from peewee import DecimalField, ForeignKeyField

from database.base_models import TimestampedModel

from ..models import Fridge


class FridgeMeasurement(TimestampedModel):
    fridge = ForeignKeyField(Fridge, backref="measurements")

    temperature = DecimalField(max_digits=5, decimal_places=2, null=True)
    humidity = DecimalField(max_digits=5, decimal_places=2, null=True)

    class Meta:
        table_name = "fridge_measurements"
        order_by = "created_at"
