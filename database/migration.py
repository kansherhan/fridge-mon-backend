import bcrypt
from random import randint, uniform as randfloat
from os.path import join as join_path

from sanic import Sanic

from core.hash import Hash

from apps.employees.models import Employee
from apps.employees.roles.models import EmployeeRole, CompanyRole

from apps.cities.models import City
from apps.countries.models import Country

from apps.companies.models import Company
from apps.enterprises.models import Enterprise

from apps.fridges.models import Fridge
from apps.fridges.templates.models import FridgeTemplate
from apps.fridges.measurements.models import FridgeMeasurement


__CAPITALES__ = [
    "admin",
    "primary",
    # "minor",
]

__COUNTRIES__ = [
    "Kazakhstan",
    # "Russia",
    # "Saudi Arabia",
    # "United Arab Emirates",
    # "China",
]

__FRIDGE_COUNT__ = 150
__FRIDGE_MEASUREMENT_COUNT__ = 20


def get_cities(app_root: str) -> list:
    cities = []

    with open(join_path(app_root, "database/datas/cities.csv"), "r") as file:
        for line in file.readlines():
            parts = line.strip().split(",")

            [name, lat, lng, country, capital] = parts

            if country in __COUNTRIES__ and capital in __CAPITALES__:
                cities.append(
                    (
                        name,
                        lat,
                        lng,
                        __COUNTRIES__.index(country) + 1,
                    )
                )

    print(cities)

    return cities


def create_fridges(company: Company, enterprise_count):
    for i in range(__FRIDGE_COUNT__):
        fridge: Fridge = Fridge.create(
            name="Холодильник в магазине",
            serial_number=Hash.generate_hash(96),
            company=company,
            enterprise=randint(1, enterprise_count),
            temperature_upper=randfloat(1, 30),
            temperature_lower=randfloat(5, -75),
        )

        for j in range(randint(3, __FRIDGE_MEASUREMENT_COUNT__)):
            measurement = FridgeMeasurement.create(
                fridge=fridge,
                temperature=randfloat(20, -100),
                humidity=randfloat(0, 100),
            )


def has_data() -> bool:
    country_count = Country.select().count()
    print(country_count, "\x1b[31mHello, World!\x1b[0m")

    return country_count != 0


async def migrate(app: Sanic):
    if has_data():
        return False

    Country.insert_many(
        [[name] for name in __COUNTRIES__],
        fields=[Country.name],
    ).execute()

    City.insert_many(
        get_cities(app.config.APP_ROOT),
        fields=[
            City.name,
            City.latitude,
            City.longitude,
            City.country,
        ],
    ).execute()

    magnum_creater = Employee.create(
        first_name="Magnum",
        last_name="Owner",
        email="info@magnum.kz",
        password=bcrypt.hashpw("123456".encode(), bcrypt.gensalt()),
        icon_url="user.jpg",
    )

    magnum_company = Company.create(
        name="Magnum",
        inn="75345678901",
        phone="+7 766 147 78 85",
        email="info@magnum.kz",
        icon_url="magnum.jpg",
    )

    magnum_owner_role = EmployeeRole.create(
        employee=magnum_creater,
        company=magnum_company,
        role=CompanyRole.OWNER,
    )

    Enterprise.insert_many(
        [
            (
                1,
                "Коктем",
                "г. Алматы, ул. Тимирязева, 37 ТЦ Коктем",
                43.192287,
                76.835896,
                "+7 (778) 147 48 12",
                "info@magnum.kz",
                "magnum.jpg",
                34,
            ),
            (
                1,
                "Люмир",
                "г. Алматы, мкр. Астана, 1/10, ТЦ «Люмир»",
                43.215311,
                76.915598,
                "+7 (707) 852 45 17",
                "info@magnum.kz",
                "magnum.jpg",
                34,
            ),
            (
                1,
                "Айнабулак",
                "г. Алматы, Айнабулак 3 мкр., Жумабаева 98а",
                43.239327,
                76.870250,
                "+7 (776) 123 48 12",
                "info@magnum.kz",
                "magnum.jpg",
                34,
            ),
            (
                1,
                "Шелек",
                "Алматинская обл. Енбекшийказахский р-н с. Шелек Ул. Каипова №1В. 1 этаж, Литер А",
                43.254332,
                76.958198,
                "+7 (778) 212 21 54",
                "info@magnum.kz",
                "magnum.jpg",
                34,
            ),
            (
                1,
                "Мехзавот",
                "г. Алматы, пр. Сакена Сейфуллина, 171/Акан серы",
                43.249334,
                76.873299,
                "+7 (770) 787 58 12",
                "info@magnum.kz",
                "magnum.jpg",
                34,
            ),
            (
                1,
                "Кулагер",
                "г. Астана, ул. Сыганак, 4",
                51.132276,
                71.446072,
                "+7 (770) 787 58 12",
                "info@magnum.kz",
                "magnum.jpg",
                50,
            ),
            (
                1,
                "Аружан",
                "г. Астана, р-н Алматы, ул. Ілияс Жансүгірұлы, дом 8/1, литер Б, 1 этаж",
                51.123657,
                71.410343,
                "+7 (770) 787 58 43",
                "info@magnum.kz",
                "magnum.jpg",
                50,
            ),
            (
                1,
                "Рауан",
                "г. Астана, р-н Сарыарка, Биржан Сал 7",
                51.146368,
                71.377908,
                "+7 (772) 752 13 79",
                "info@magnum.kz",
                "magnum.jpg",
                50,
            ),
            (
                1,
                "Самал",
                "г. Астана, мкр. Самал, 11",
                51.122240,
                71.518176,
                "+7 (770) 787 58 12",
                "info@magnum.kz",
                "magnum.jpg",
                50,
            ),
            (
                1,
                "Женис",
                "г. Астана, р-н Сарыарка, Женіс 55",
                51.095511,
                71.417858,
                "+7 (774) 789 88 19",
                "info@magnum.kz",
                "magnum.jpg",
                50,
            ),
        ],
        fields=[
            Enterprise.company,
            Enterprise.name,
            Enterprise.address,
            Enterprise.latitude,
            Enterprise.longitude,
            Enterprise.phone,
            Enterprise.email,
            Enterprise.icon_url,
            Enterprise.city,
        ],
    ).execute()

    create_fridges(magnum_company, 10)

    return True
