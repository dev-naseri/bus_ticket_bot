from datetime import datetime

from peewee import Model, CharField, IntegerField, DateTimeField
from bus_ticket_bot.models.db_settings import db


class Users(Model):
    full_name = CharField(null=True)
    telegram_id = IntegerField(null=False, unique=True, index=True)
    state = CharField(default="Inactive", index=True)
    warnings = IntegerField(default=0, index=True)
    created_at = DateTimeField(default=datetime.now)

    class Meta:
        database = db
