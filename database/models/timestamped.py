from datetime import datetime
from peewee import DateTimeField

from .base import BaseModel


class TimestampedModel(BaseModel):
    created_at = DateTimeField()
    updated_at = DateTimeField()

    def save(self, *args, **kwargs):
        current_time = datetime.now()

        if self.updated_at is None:
            self.created_at = current_time

        self.updated_at = current_time

        return super(TimestampedModel, self).save(*args, **kwargs)
