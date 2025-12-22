from datetime import datetime

import khayyam
from peewee import Model, CharField, IntegerField, TextField, ForeignKeyField, \
    Check, DateTimeField
from bus_ticket_bot.models.bot_instance import BotInstance
from bus_ticket_bot.models.db_settings import db

class Tickets(Model):
    full_name = CharField(null=False)
    ticket_type = CharField(null=False, index=True)
    origin_city = CharField(
        default=lambda: (get_default_instance().city_name
        if get_default_instance() else "DefaultCity")
    )
    origin_terminal = CharField(
        default=lambda: (get_default_instance().terminal_name
        if get_default_instance() else "DefaultTerminal")
    )
    city = CharField(null=False, index=True)
    destination_terminal = CharField(null=True)
    date = DateTimeField(default=datetime.now, index=True)
    price = IntegerField(null=False, index=True)
    created_at = DateTimeField(default=datetime.now)

    class Meta:
        database = db
        constraints = [
            Check("ticket_type IN ('VIP', 'Normal', 'Car')"),
            Check("price > 0")
        ]
        indexes = (
            (('date', 'city'), True),
        )


def get_default_instance():
    try:
        return BotInstance.get()
    except BotInstance.DoesNotExist:
        return None
