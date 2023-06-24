from peewee import CharField, DecimalField
from database.base_models import BaseModel


class FridgeProduct(BaseModel):
    name = CharField(unique=True)

    temperature_upper = DecimalField(max_digits=5, decimal_places=2)
    temperature_lower = DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        table_name = "fridge_products"
