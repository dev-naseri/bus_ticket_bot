from datetime import datetime

from peewee import Model, CharField, IntegerField, DateTimeField
from bus_ticket_bot.models.db_settings import db


class Admins(Model):
    full_name = CharField(null=True)
    telegram_id = IntegerField(null=False, unique=True, index=True)
    created_at = DateTimeField(default=datetime.now)

    class Meta:
        database = db
