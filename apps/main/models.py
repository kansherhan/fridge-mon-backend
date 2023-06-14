from peewee import CharField, ForeignKeyField, DecimalField, DateTimeField, IntegerField

from database.base_models import BaseModel


class Category(BaseModel):
    name_categor = CharField()

    class Meta:
        table_name = "categories"


class Company(BaseModel):
    inn = CharField(max_length=20)
    name_compan = CharField()
    address = CharField()
    phone = CharField(max_length=20)
    email = CharField()
    geo_location = CharField()
    icon = CharField()

    class Meta:
        table_name = "companies"


class Enterprise(BaseModel):
    company = ForeignKeyField(Company, backref="enterprises", lazy_load=False)
    name_enterpris = CharField()
    address = CharField()
    phone = CharField(max_length=20)
    email = CharField()
    geo_location = CharField()
    icon = CharField()

    class Meta:
        table_name = "enterprises"


class Manufacturer(BaseModel):
    name_manufacture = CharField()

    class Meta:
        table_name = "manufacturers"


class Refrigerator(BaseModel):
    company = ForeignKeyField(Company, backref="companies", lazy_load=False)
    enterprise = ForeignKeyField(Enterprise, backref="enterprises", lazy_load=False)
    serial_number = CharField(max_length=50)
    label_gis = CharField()
    category = ForeignKeyField(Category, backref="categories", lazy_load=False)
    manufacturer = ForeignKeyField(
        Manufacturer, backref="manufacturers", lazy_load=False
    )
    temperature_upper = DecimalField(max_digits=5, decimal_places=2)
    temperature_lower = DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        table_name = "refrigerators"


class Sensor(BaseModel):
    name_sensor = CharField()
    refrigerator = ForeignKeyField(
        Refrigerator, backref="refrigerators", lazy_load=False
    )
    ip_address = CharField(max_length=50)
    exchange_protocol = CharField(max_length=50)
    start_register = IntegerField()
    register_count = IntegerField()

    class Meta:
        table_name = "sensors"


class Measurement(BaseModel):
    sensor = ForeignKeyField(Sensor, backref="sensors", lazy_load=False)
    temperature = DecimalField(max_digits=5, decimal_places=2)
    humidity = DecimalField(max_digits=5, decimal_places=2)
    measurement_date = DateTimeField()

    class Meta:
        table_name = "measurements"
