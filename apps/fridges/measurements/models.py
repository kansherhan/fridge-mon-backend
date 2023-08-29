from datetime import datetime

from peewee import DecimalField, ForeignKeyField, DateTimeField

from database.models.base import BaseModel

from ..models import Fridge


class FridgeMeasurement(BaseModel):
    fridge = ForeignKeyField(Fridge, backref="measurements")

    temperature = DecimalField(max_digits=5, decimal_places=2, null=True)
    humidity = DecimalField(max_digits=5, decimal_places=2, null=True)

    created_at = DateTimeField()

    def save(self, *args, **kwargs):
        if self.created_at == None:
            self.created_at = datetime.now()

        return super(FridgeMeasurement, self).save(*args, **kwargs)

    class Meta:
        table_name = "fridge_measurements"
        order_by = "created_at"
        primary_key = False
