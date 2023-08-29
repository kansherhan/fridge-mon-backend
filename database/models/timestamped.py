from datetime import datetime
from peewee import DateTimeField, PrimaryKeyField

from .base import BaseModel, BaseHelperModel


class TimestampedModel(BaseModel):
    created_at = DateTimeField()
    updated_at = DateTimeField()

    def save(self, *args, **kwargs):
        current_time = datetime.now()

        if self.updated_at == None:
            self.created_at = current_time

        self.updated_at = current_time

        return super(TimestampedModel, self).save(*args, **kwargs)


class TimestampedWithIDModel(TimestampedModel, BaseHelperModel):
    id = PrimaryKeyField(unique=True)
