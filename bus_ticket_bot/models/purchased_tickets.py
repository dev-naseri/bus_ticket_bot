from datetime import datetime
from enum import UNIQUE

from peewee import Model, ForeignKeyField, IntegerField, BooleanField, \
    CharField, DateTimeField
from bus_ticket_bot.models.tickets import Tickets
from bus_ticket_bot.models.users import Users
from bus_ticket_bot.models.db_settings import db


class PurchasedTickets(Model):
    ticket_id = ForeignKeyField(Tickets, "id")
    user_id = ForeignKeyField(Users, "id")
    transactions_id = IntegerField(null=True, unique=True, index=True)
    active = BooleanField(default=False, index=True)
    receipt = CharField(null=False, unique=True)
    created_at = DateTimeField(default=datetime.now)

    class Meta:
        database = db
