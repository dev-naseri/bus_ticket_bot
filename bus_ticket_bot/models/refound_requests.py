from datetime import datetime

from peewee import Model, CharField, ForeignKeyField, TextField, DateTimeField
from bus_ticket_bot.models.db_settings import db
from bus_ticket_bot.models.purchased_tickets import PurchasedTickets


class RefoundRequests(Model):
    receipt_id = ForeignKeyField(PurchasedTickets, "receipt")
    refound_request_id = CharField(null=False, unique=True, index=True)
    reason = TextField(null=True, index=True)
    created_at = DateTimeField(default=datetime.now)

    class Meta:
        database = db
