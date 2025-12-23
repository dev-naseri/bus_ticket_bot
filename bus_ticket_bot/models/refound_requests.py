from datetime import datetime

from peewee import Model, CharField, ForeignKeyField, TextField, DateTimeField
from bus_ticket_bot.models.db_settings import db
from bus_ticket_bot.models.purchased_tickets import PurchasedTickets
from bus_ticket_bot.models.users import Users


class RefoundRequests(Model):
    telegram_id = ForeignKeyField(
        Users,
        field=Users.telegram_id,
        backref="telegram_id",
        index=True,
        on_delete="CASCADE",
        on_update="CASCADE"
    )
    receipt_id = ForeignKeyField(
        PurchasedTickets,
        field=PurchasedTickets.receipt,
        backref='receipt_unic_id',
        index=True,
        on_delete="CASCADE",
        on_update="CASCADE"
    )
    refound_request_id = CharField(null=False, unique=True, index=True)
    reason = TextField(null=True, index=True)
    created_at = DateTimeField(default=datetime.now)

    class Meta:
        database = db
