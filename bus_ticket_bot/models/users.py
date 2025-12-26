from datetime import datetime

from peewee import Model, CharField, IntegerField, DateTimeField, BooleanField
from bus_ticket_bot.models.db_settings import db


class Users(Model):
    telegram_id = IntegerField(null=False, unique=True, index=True)
    full_name = CharField(null=True, max_length=30)
    phone_number = IntegerField(null=True)
    nationality = BooleanField(default=1)  # 1 = Native, 0 = Immigrant
    national_id = CharField(null=True)
    open_transaction = CharField(default="empty")
    state = CharField(default="Inactive", index=True)
    warnings = IntegerField(default=0, index=True)
    created_at = DateTimeField(default=datetime.now)

    class Meta:
        database = db
