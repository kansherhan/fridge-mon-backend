from peewee import CharField


class ImageableModel:
    icon_url = CharField(null=True)
