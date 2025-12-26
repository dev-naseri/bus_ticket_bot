from datetime import datetime

from peewee import Model, CharField, IntegerField, Check, DateTimeField
from bus_ticket_bot.models.bot_instance import BotInstance
from bus_ticket_bot.models.db_settings import db
from bus_ticket_bot.services.bot_instance_service import BotInstanceService


class Tickets(Model):
    full_name = CharField(null=False)
    ticket_type = CharField(null=False, index=True)
    origin_city = CharField(
        default=lambda: (BotInstanceService.get_data().city_name
        if BotInstanceService.get_data() else "DefaultTerminal")
    )
    origin_terminal = CharField(
        default=lambda: (BotInstanceService.get_data().terminal_name
        if BotInstanceService.get_data() else "DefaultTerminal")
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
