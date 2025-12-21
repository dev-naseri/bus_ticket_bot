from peewee import Model, CharField, TextField, IntegerField
from bus_ticket_bot.models.db_settings import db


class BotInstance(Model):
    company_name = CharField(null=False, index=True)
    address = TextField(null=False, index=True)
    call_number = IntegerField(null=False, index=True)
    terminal_name = CharField(null=False, index=True)
    city_name = CharField(null=False, index=True)
    start_message = TextField(null=False, index=True)
    contact_us_message = TextField(null=False, index=True)
    help_message = TextField(null=False, index=True)
    payment_message = TextField(null=False, index=True)
    refund_message = TextField(null=False, index=True)

    class Meta:
        database = db
