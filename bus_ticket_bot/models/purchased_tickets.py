from datetime import datetime
from enum import UNIQUE

from peewee import Model, ForeignKeyField, IntegerField, BooleanField, \
    CharField, DateTimeField
from bus_ticket_bot.models.tickets import Tickets
from bus_ticket_bot.models.users import Users
from bus_ticket_bot.models.db_settings import db


class PurchasedTickets(Model):
    telegram_id = ForeignKeyField(
        Users,
        backref="purchased_tickets",
        on_delete="CASCADE",
        index=True
    )
    ticket_id = ForeignKeyField(
        Tickets,
        backref="tickets",
        null=False,
        unique=True,
        on_update="CASCADE",
        on_delete="CASCADE",
        index=True
    )
    transactions_id = IntegerField(null=True, unique=True, index=True)
    active = BooleanField(default=False, index=True)
    receipt = CharField(null=False, unique=True)
    created_at = DateTimeField(default=datetime.now)

    class Meta:
        database = db
