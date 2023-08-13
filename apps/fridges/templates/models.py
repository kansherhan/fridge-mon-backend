from peewee import CharField, DecimalField, ForeignKeyField

from apps.companies.models import Company
from database.base_models import BaseModel


class FridgeTemplate(BaseModel):
    name = CharField(unique=True)

    company = ForeignKeyField(Company, backref="templates")

    temperature_upper = DecimalField(max_digits=5, decimal_places=2)
    temperature_lower = DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        table_name = "fridge_templates"
